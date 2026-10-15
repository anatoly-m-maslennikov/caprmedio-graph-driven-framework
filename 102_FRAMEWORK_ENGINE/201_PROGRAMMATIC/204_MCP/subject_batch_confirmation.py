"""One actual connected form followed by the existing durable selected queue."""

from __future__ import annotations

import asyncio
import copy
from typing import Any, Callable, Mapping

import anyio
from mcp import types
from mcp.shared.exceptions import MCPError, NoBackChannelError
from pydantic import ValidationError

from selected_execution import canonical_json
from subject_batch import subject_batch_progress_summary
from subject_batch_authorization import (
    CONFIRMATION,
    capture_batch_review,
    load_subject_batch_confirmation,
    persist_subject_batch_confirmation,
    revalidate_batch_review,
)
from subject_publication_confirmation import FORM_SCHEMA, WAIT_SECONDS, _admitted, _result


def _enqueue(runner: Any, frozen: Mapping[str, Any]) -> Any:
    import orchestrator

    request = frozen["request"]
    enqueue: Callable[..., Any] = orchestrator.run
    return enqueue(
        runner.root,
        {
            "operation": "enqueue_selected",
            "run_id": request["run_id"],
            "execution": request["execution"],
        },
    )


def _message(execution: Mapping[str, Any], review: Mapping[str, Any], operator_name: str) -> str:
    pin = execution["parameters"]["subject_batch"]
    packet = review["packet"]
    return (
        f"Confirm one ordered Subjects-only batch for Operator {operator_name}.\n"
        f"Atoms: {len(packet['atoms'])}. Request: {execution['request_id']}.\n"
        f"Complete exact ordered map: {pin['path']}\nSHA-256: {pin['digest']}\n"
        f"Git recovery checkpoint: {packet['git_checkpoint']}\n"
        "Review the complete map at that path, including every exact before descriptor and old/new "
        "governs/depends_on patch and every full edit-draft referenced there. This confirms all of its ordered targets once. "
        "Each changed Atom receives Version +1, actual edit time and its exact old-byte archive. "
        "The existing Workflow runs in the background and stops at the first failed or uncertain target; "
        "earlier completed changes remain. No automatic replay or whole-batch rollback. "
        "Pause outside editing, scripts, Git and synchronization for the reviewed frontier until it ends."
    )


async def _elicit(session: Any, message: str, request_id: Any) -> str:
    try:
        reply = await asyncio.wait_for(
            session.elicit_form(message, FORM_SCHEMA, related_request_id=request_id), WAIT_SECONDS
        )
    except TimeoutError:
        return "timed_out"
    except NoBackChannelError:
        return "unsupported"
    except ValidationError:
        return "malformed_response"
    except ConnectionError, anyio.EndOfStream, anyio.ClosedResourceError, anyio.BrokenResourceError:
        return "disconnected"
    except MCPError:
        return "elicitation_failed"
    if type(reply) is not types.ElicitResult or reply.action not in {"accept", "decline", "cancel"}:
        return "malformed_response"
    if reply.action != "accept":
        return reply.action if reply.content is None else "malformed_response"
    if (
        type(reply.content) is not dict
        or set(reply.content) != {"review", "pause"}
        or any(type(value) is not bool for value in reply.content.values())
    ):
        return "malformed_response"
    return "confirmed" if all(reply.content.values()) else "unconfirmed"


async def confirm_subject_batch_publication(
    context: Any,
    runner: Any,
    frozen: Mapping[str, Any],
    *,
    operator_name: str,
    operator_registry: Any = None,
) -> types.CallToolResult:
    """Persist actual form acceptance before queue admission, independent of this connection."""
    session = getattr(context, "session", None)
    request_id = getattr(context, "request_id", None)
    folder = runner.run_directory(frozen["request"]["run_id"])
    try:
        if canonical_json(runner.load(frozen["request"]["run_id"])) != canonical_json(frozen):
            raise ValueError("Subject batch request differs from its saved exact Run")
        progress = folder / "subject_batch_progress.json"
        if progress.exists():
            return _result(
                "dispatched",
                native_result={
                    "workflow_run_id": frozen["request"]["run_id"],
                    "subject_batch": subject_batch_progress_summary(
                        runner._read(progress),
                        result_ref=progress.relative_to(runner.root).as_posix(),
                    ),
                },
            )
        if (folder / CONFIRMATION).exists():
            load_subject_batch_confirmation(runner, frozen)
            return _result("dispatched", native_result=_enqueue(runner, frozen))
        elicitation = getattr(getattr(session, "client_capabilities", None), "elicitation", None)
        if (
            request_id is None
            or not getattr(session, "can_send_request", False)
            or getattr(elicitation, "form", None) is None
            or not callable(getattr(session, "elicit_form", None))
        ):
            return _result("unsupported")
        frozen = copy.deepcopy(frozen)
        execution = _admitted(runner, frozen)
        review = capture_batch_review(runner, frozen)
        if operator_registry is not None:
            operator_registry.revalidate()
        outcome = await _elicit(session, _message(execution, review, operator_name), request_id)
        if outcome != "confirmed":
            return _result(outcome)
        if context.session is not session or context.request_id != request_id:
            raise ValueError("The actual batch confirmation context changed")
        revalidate_batch_review(runner.root, review)
        if operator_registry is not None:
            operator_registry.revalidate()
        _admitted(runner, frozen)
        persist_subject_batch_confirmation(runner, frozen, review, operator_name=operator_name)
        return _result("dispatched", native_result=_enqueue(runner, frozen))
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError, OSError) as error:
        return _result("refused", diagnostic=str(error))
