"""Internal connected-session form handler; no public Tool or runtime registration."""
from __future__ import annotations

import asyncio
import copy
import difflib
import json
from pathlib import Path

import anyio
from mcp import types
from mcp.shared.exceptions import MCPError, NoBackChannelError
from pydantic import ValidationError

from atom_subject_apply import _parameters, _prepare
from connector_bindings import FileSource, capture_source
import atom_operations as operations
from selected_execution import SelectedExecution, canonical_json
from subject_publication_authorization import (
    _frontier, _reviewed_subject_candidate, authorize_subject_publication,
)

WAIT_SECONDS = 60
FORM_SCHEMA = {
    "type": "object",
    "properties": {
        "review": {"type": "boolean", "title": "I reviewed this exact source and candidate change"},
        "pause": {"type": "boolean", "title": "I have paused editing, scripts, Git and synchronization for the affected frontier until this attempt finishes"},
    },
    "required": ["review", "pause"],
    "additionalProperties": False,
}


def _result(status, *, native_result=None, diagnostic=None):
    data = {"status": status, "result": native_result}
    if native_result is None:
        data.update(effects=[], diagnostics=[diagnostic or status])
    return types.CallToolResult(content=[types.TextContent(type="text", text=json.dumps(data))],
                                structured_content=data, is_error=status != "dispatched")


def _admitted(runner, frozen):
    request = frozen["request"]
    if canonical_json(runner.load(request["run_id"])) != canonical_json(frozen):
        raise ValueError("Host input differs from the exact saved selected request")
    graph = runner._revalidate(frozen)
    execution = request["execution"]
    if execution["mode"] != "execute" or execution["operation_route"] != "update_atom":
        raise ValueError("Only an admitted selected Subject execution can be confirmed")
    runner._validate_requested_runs(execution, graph, request["run_id"])
    runner._validate_query_admission(graph, execution)
    runner._validate_lifecycle_admission(graph, execution,
                                       expected_admission=frozen.get("lifecycle_admission"))
    return execution


async def confirm_subject_publication(context, runner, frozen, *, operator_name, staged_manifest):
    """Host-owned inputs only; issue and consume confirmation in this process."""
    session = getattr(context, "session", None)
    request_id = getattr(context, "request_id", None)
    capabilities = getattr(session, "client_capabilities", None)
    elicitation = getattr(capabilities, "elicitation", None)
    if (request_id is None or not getattr(session, "can_send_request", False)
            or getattr(elicitation, "form", None) is None
            or not callable(getattr(session, "elicit_form", None))):
        return _result("unsupported")
    try:
        if type(runner) is not SelectedExecution:
            raise ValueError("The host's existing selected executor is required")
        frozen, staged_manifest = copy.deepcopy(frozen), copy.deepcopy(staged_manifest)
        execution = _admitted(runner, frozen)
        request = _parameters(execution["parameters"])
        prepared = _prepare(runner.root, request)
        intent = prepared["subject_intent"]
        if intent["noop"]:
            raise ValueError("An unchanged no-op needs no publication confirmation")
        staged, candidate, candidate_raw = _reviewed_subject_candidate(
            runner.root, request, prepared, staged_manifest)
        target = FileSource(runner.root, Path(intent["target"]["path"]), intent["target"]["digest"])
        source_raw = target.read_bytes()
        _, fingerprint = operations.read_raw_atom_revision(runner.root, runner.root / target.relative_path)
        saved = capture_source(runner.root, (runner.run_directory(frozen["request"]["run_id"])
                                           / "selected_request.json").relative_to(runner.root))
        originals, authorities = _frontier(runner.root, prepared, execution)
        predecessor = capture_source(runner.root, intent["predecessorArchive"]["path"])
        if predecessor.sha256 is not None:
            raise ValueError("The exact predecessor archive must still be absent")
        pins = (saved, target, staged, candidate, predecessor, *authorities)
        diff = "".join(difflib.unified_diff(source_raw.decode("utf-8").splitlines(keepends=True),
            candidate_raw.decode("utf-8").splitlines(keepends=True),
            fromfile=target.relative_path.as_posix(), tofile=candidate.relative_path.as_posix()))
        message = (
            f"Confirm one Subject publication for Operator {operator_name}.\n"
            f"Request: {execution['request_id']}\n"
            f"Selected Session/Run: {frozen['request']['run_id']}\n"
            f"Requested Runs: {json.dumps(execution['requested_runs'], sort_keys=True)}\n"
            f"Authorization: {execution['operator_authorization']['authorization_ref']}\n"
            f"Intent: {request['subject_intent_sha256']}\n"
            f"Atom: {intent['target']['atom_id']}, Version {intent['target']['version']} -> {intent['target']['version'] + 1}\n"
            f"Current: {target.relative_path.as_posix()} ({target.sha256})\n"
            f"History: {predecessor.relative_path.as_posix()} (currently absent)\n"
            f"Staged manifest: {staged.relative_path.as_posix()} ({staged.sha256})\n"
            f"Candidate: {candidate.relative_path.as_posix()} ({candidate.sha256})\n"
            f"Affected authority frontier: {json.dumps([pin.relative_path.as_posix() for pin in authorities])}\n"
            "Review the exact diff below. Pause manual editing, maintenance/script writes, Git and synchronization "
            "for this current/history/authority frontier until the attempt finishes. "
            "The candidate timestamp is illustrative; publication uses the actual edit time.\n\n"
            + diff
        )
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError, OSError) as error:
        return _result("refused", diagnostic=str(error))
    try:
        reply = await asyncio.wait_for(
            session.elicit_form(message, FORM_SCHEMA, related_request_id=request_id), WAIT_SECONDS)
    except TimeoutError:
        return _result("timed_out")
    except NoBackChannelError:
        return _result("unsupported")
    except ValidationError:
        return _result("malformed_response")
    except (ConnectionError, anyio.EndOfStream, anyio.ClosedResourceError, anyio.BrokenResourceError):
        return _result("disconnected")
    except MCPError:
        return _result("elicitation_failed")
    if type(reply) is not types.ElicitResult or reply.action not in {"accept", "decline", "cancel"}:
        return _result("malformed_response")
    if reply.action != "accept":
        return _result(reply.action if reply.content is None else "malformed_response")
    if (type(reply.content) is not dict or set(reply.content) != {"review", "pause"}
            or any(type(value) is not bool for value in reply.content.values())):
        return _result("malformed_response")
    if not all(reply.content.values()):
        return _result("unconfirmed")

    def recheck_displayed():
        if context.session is not session or context.request_id != request_id:
            raise ValueError("The exact connected form request context changed")
        for pin in pins:
            pin.revalidate()
        _, current_fingerprint = operations.read_raw_atom_revision(runner.root, runner.root / target.relative_path)
        if current_fingerprint != fingerprint or _frontier(runner.root, prepared, execution)[0] != originals:
            raise ValueError("The displayed source identity or original frontier changed during confirmation")
        _admitted(runner, frozen)

    try:
        recheck_displayed()
        confirmation = authorize_subject_publication(runner.root, execution, operator_name=operator_name,
            llm_session={"app": "run-support", "uuid": execution["request_id"]}, staged_manifest=staged_manifest)
        recheck_displayed()
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError, OSError) as error:
        return _result("refused", diagnostic=str(error))
    try:
        return _result("dispatched", native_result=runner._dispatch_confirmed_subject(frozen, confirmation))
    except Exception:
        return _result("uncertain", native_result={
            "disposition": "recording_pending", "outcome": "interrupted_pending",
            "diagnostics": ["Confirmed dispatch failed; inspect current/history files and Run evidence before any separately admitted continuation"],
            "recovery": {"automatic_retry": False, "inspection_required": True},
            "unknown_remainder": [target.relative_path.as_posix(), predecessor.relative_path.as_posix()],
        })
