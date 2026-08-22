#!/usr/bin/env python3
"""Commit one sealed governed change and its exact Work Journal sidecars.

The Tool has two deliberately narrow entry points:

* an end-to-end ``COMMIT_TRIGGER`` handoff, which gathers context, invokes the
  Journal Appender, then commits; and
* a commit-only retry envelope containing an already sealed context, the exact
  Appender receipts, and its still-live repository lease.

All output is one schema-versioned machine-readable envelope.  Omitting
``--apply`` executes the full prediction path without changing Git, Journals,
or runtime state.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence


SCRIPT_PATH = Path(__file__).resolve()
TOOLS_ROOT = SCRIPT_PATH.parents[1]
CONTEXT_ROOT = TOOLS_ROOT / "COMMIT_CONTEXT"
APPENDER_ROOT = TOOLS_ROOT / "APPEND_CHANGE_RECORDS"
for _parent in SCRIPT_PATH.parents:
    if _parent.name == ".caprmedio_runtime":
        sys.pycache_prefix = str(_parent / "cache" / "python")
        break
    if _parent.name == ".caprmedio_install":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_runtime" / "cache" / "python")
        break
    if _parent.name == ".caprmedio":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_runtime" / "cache" / "python")
        break
for _path in (TOOLS_ROOT, CONTEXT_ROOT, APPENDER_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from commit_context_logic import ContextError, event_message, gather_context, repository_identity, repository_root  # noqa: E402
from work_journal import WorkJournalError, canonical_json_bytes, canonical_json_digest, validate_sealed_event  # noqa: E402


TOOL_ID = "COMMIT_CHANGE_SET"
TOOL_KIND = "doer"
TOOL_SCHEMA_VERSION = 1
ACTION_TYPES = {"ADD", "MOVE", "UPDATE", "MOVE+UPDATE", "REMOVE"}
HEX64 = __import__("re").compile(r"^[0-9a-f]{64}$")
HEX40 = __import__("re").compile(r"^[0-9a-f]{40}$")


class ToolError(RuntimeError):
    """A deterministic diagnostic returned by this Tool."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


def _require_mapping(value: object, field: str) -> dict[str, Any]:
    if not isinstance(value, Mapping):
        raise ToolError("invalid-input", f"{field} must be an object")
    return dict(value)


def _require_string(value: Mapping[str, Any], field: str) -> str:
    item = value.get(field)
    if not isinstance(item, str) or not item:
        raise ToolError("invalid-input", f"{field} must be a non-empty string")
    return item


def _safe_path(root: Path, value: object, field: str) -> Path:
    if not isinstance(value, str) or not value:
        raise ToolError("invalid-path", f"{field} must be a non-empty repository-relative path")
    relative = Path(value)
    if relative.is_absolute() or ".." in relative.parts or relative.as_posix() in {"", "."}:
        raise ToolError("invalid-path", f"{field} must be a safe repository-relative path")
    return root / relative


def _relative(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError as error:
        raise ToolError("invalid-path", f"path lies outside repository: {path}") from error


def _git(root: Path, *arguments: str, input_bytes: bytes | None = None) -> bytes:
    completed = subprocess.run(
        ["git", "-C", str(root), *arguments],
        input=input_bytes,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        detail = (completed.stderr or completed.stdout).decode("utf-8", errors="replace").strip()
        raise ToolError("git-command-failed", detail or "Git command failed")
    return completed.stdout


def _git_text(root: Path, *arguments: str) -> str:
    return _git(root, *arguments).decode("utf-8", errors="strict").strip()


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _envelope(*, ok: bool, mode: str, result: Mapping[str, Any] | None = None, error: BaseException | None = None) -> dict[str, Any]:
    diagnostic: list[dict[str, str]] = []
    if error is not None:
        code = getattr(error, "code", "unexpected-error")
        diagnostic.append({"code": str(code), "message": str(error)})
    payload: dict[str, Any] = {
        "schema_version": TOOL_SCHEMA_VERSION,
        "tool": {"capability_id": TOOL_ID, "kind": TOOL_KIND},
        "ok": ok,
        "mode": mode,
        "diagnostics": diagnostic,
    }
    if result is not None:
        payload["result"] = dict(result)
    return payload


def _import_appender() -> Any:
    """Load the peer Tool only after all local paths have been configured."""
    try:
        import append_change_records
    except ImportError as error:  # pragma: no cover - an integration install error
        raise ToolError("peer-tool-unavailable", "APPEND_CHANGE_RECORDS is not importable") from error
    return append_change_records


def _load_payload(source: str) -> dict[str, Any]:
    try:
        raw = sys.stdin.read() if source == "-" else Path(source).read_text(encoding="utf-8")
        value = json.loads(raw)
    except OSError as error:
        raise ToolError("input-unreadable", f"cannot read input: {source}") from error
    except json.JSONDecodeError as error:
        raise ToolError("invalid-json", "input must be one JSON object") from error
    return _require_mapping(value, "input")


def _context_from_payload(root: Path, payload: Mapping[str, Any]) -> tuple[dict[str, Any], str]:
    """Return a context without inventing a third input path."""
    if "trigger" in payload:
        if "context" in payload or "receipts" in payload or "lease" in payload:
            raise ToolError("ambiguous-input", "a trigger handoff cannot also provide context, receipts, or lease")
        trigger = _require_mapping(payload["trigger"], "trigger")
        try:
            return gather_context(root, trigger), "trigger"
        except ContextError as error:
            raise ToolError(error.code, str(error)) from error
    candidate = _require_mapping(payload.get("context", payload), "context")
    return candidate, "context"


def _events_from_context(appender: Any, context: Mapping[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Use APPEND_CHANGE_RECORDS as the sole validator of sealed context."""
    try:
        validated, events = appender.validate_context(context)
    except Exception as error:
        if hasattr(error, "code"):
            raise ToolError(str(error.code), str(error)) from error
        raise ToolError("invalid-context", str(error)) from error
    value = dict(validated)
    _validate_context_identity_and_frontiers(value)
    return value, [dict(event) for event in events]


def _validate_context_identity_and_frontiers(context: Mapping[str, Any]) -> None:
    """Verify the Context seal plus both source and relation frontiers locally."""
    core_fields = (
        "schema_version",
        "action_id",
        "trigger",
        "subject",
        "structural_scope",
        "action_type",
        "sources",
        "result",
        "llm_session",
        "author",
        "occurred_at",
        "timezone",
        "local_date",
        "git_base",
        "frontier",
    )
    try:
        core = {field: context[field] for field in core_fields}
    except KeyError as error:
        raise ToolError("context-field-missing", f"sealed context is missing {error.args[0]}") from error
    if "previous_result_event" in context:
        core["previous_result_event"] = context["previous_result_event"]
    expected_context_id = canonical_json_digest(core)
    if context.get("context_id") != expected_context_id:
        raise ToolError("context-id-mismatch", "context_id no longer matches its sealed authoritative fields")
    frontier = _require_mapping(context.get("frontier"), "context.frontier")
    result = _require_mapping(context.get("result"), "context.result")
    subject = _require_mapping(context.get("subject"), "context.subject")
    source_frontier: dict[str, Any] = {
        "identity": subject.get("identity"),
        "kind": subject.get("kind"),
        # This is the state of the selected *carrier*, not where that carrier
        # was observed (working/index/committed).  Context deliberately seals
        # a present carrier as ``present`` across those observation states.
        "state": "removed" if result.get("state") == "removed" else "present",
        "filename": result.get("filename"),
        "version": result.get("version"),
    }
    if result.get("state") == "present":
        source_frontier.update({"path": result.get("path"), "sha256": result.get("sha256")})
    else:
        snapshots = _require_mapping(context.get("snapshots"), "context.snapshots")
        committed = _require_mapping(snapshots.get("committed"), "context.snapshots.committed")
        source_frontier.update({"path": committed.get("path"), "sha256": committed.get("sha256")})
    if frontier.get("source_sha256") != canonical_json_digest(source_frontier):
        raise ToolError("source-frontier-mismatch", "source frontier digest does not match sealed selected carrier")
    relations = context.get("relations")
    if not isinstance(relations, list):
        raise ToolError("relation-frontier-missing", "sealed context is missing detailed direct relation frontier")
    detailed = []
    for relation in relations:
        row = _require_mapping(relation, "context.relations item")
        detailed.append({key: row.get(key) for key in ("relation_type", "filename", "version", "path", "sha256")})
    if frontier.get("relations_sha256") != canonical_json_digest(detailed):
        raise ToolError("relation-frontier-mismatch", "relation frontier digest does not match detailed direct relations")


def _completed_event(events: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    completed = [dict(event) for event in events if event.get("event") == "completed" and event.get("kind") == "governed_project_change"]
    if len(completed) != 1:
        raise ToolError("invalid-context", "context must project exactly one completed governed_project_change event")
    return completed[0]


def _render_message(context: Mapping[str, Any], events: Sequence[Mapping[str, Any]]) -> str:
    try:
        return event_message(_completed_event(events), context.get("previous_result"))
    except ContextError as error:
        raise ToolError(error.code, str(error)) from error


def _expected_receipt_ids(events: Sequence[Mapping[str, Any]]) -> list[tuple[str, str]]:
    expected: list[tuple[str, str]] = []
    for event in events:
        event_id = event.get("event_id")
        event_digest = event.get("event_digest")
        if not isinstance(event_id, str) or not isinstance(event_digest, str) or not HEX64.fullmatch(event_digest):
            raise ToolError("invalid-context", "sealed Journal event identity is invalid")
        expected.append((event_id, event_digest))
    return expected


def _validate_receipts(root: Path, context: Mapping[str, Any], events: Sequence[Mapping[str, Any]], raw_receipts: object) -> list[dict[str, Any]]:
    if not isinstance(raw_receipts, list):
        raise ToolError("receipt-set-missing", "receipts must be an ordered array")
    expected = _expected_receipt_ids(events)
    if len(raw_receipts) != len(expected):
        raise ToolError("receipt-set-incomplete", "receipt count does not match sealed Journal event set")
    action_id = _require_string(context, "action_id")
    output: list[dict[str, Any]] = []
    for index, (raw_receipt, (event_id, event_digest), event) in enumerate(zip(raw_receipts, expected, events, strict=True), start=1):
        receipt = _require_mapping(raw_receipt, f"receipts[{index}]")
        if receipt.get("event_id") != event_id or receipt.get("event_digest") != event_digest or receipt.get("action_id") != action_id:
            raise ToolError("receipt-set-mismatch", "receipt does not match its sealed Journal event")
        carrier = _safe_path(root, receipt.get("carrier"), f"receipts[{index}].carrier")
        line = receipt.get("line")
        if not isinstance(line, int) or line < 1:
            raise ToolError("receipt-invalid", "receipt.line must be a positive integer")
        for digest_name in ("previous_carrier_digest", "appended_carrier_digest"):
            if not isinstance(receipt.get(digest_name), str) or not HEX64.fullmatch(receipt[digest_name]):
                raise ToolError("receipt-invalid", f"receipt.{digest_name} must be a SHA-256 digest")
        if not carrier.is_file():
            raise ToolError("receipt-carrier-missing", "receipt carrier no longer exists")
        data = carrier.read_bytes()
        lines = data.splitlines(keepends=True)
        if line > len(lines):
            raise ToolError("receipt-line-missing", "receipt line no longer exists in carrier")
        previous = b"".join(lines[: line - 1])
        appended = b"".join(lines[:line])
        if _sha256(previous) != receipt["previous_carrier_digest"] or _sha256(appended) != receipt["appended_carrier_digest"]:
            raise ToolError("receipt-carrier-mismatch", "receipt carrier digests no longer match its sealed line")
        try:
            stored = json.loads(lines[line - 1])
        except json.JSONDecodeError as error:
            raise ToolError("receipt-line-invalid", "receipt line is not JSON") from error
        if stored != dict(event):
            raise ToolError("receipt-event-mismatch", "receipt line does not contain the sealed Journal event")
        output.append(receipt)
    return output


def _lease_path(root: Path) -> Path:
    return root / ".caprmedio_runtime" / "state" / "commit_change_set" / "lease.json"


def _validate_lease(root: Path, context: Mapping[str, Any], events: Sequence[Mapping[str, Any]], raw_lease: object) -> dict[str, Any]:
    lease = _require_mapping(raw_lease, "lease")
    if lease.get("status") != "active":
        raise ToolError("lease-not-live", "lease status must be active")
    action_id = _require_string(context, "action_id")
    token = _require_string(lease, "lease_token")
    if lease.get("action_id") != action_id:
        raise ToolError("lease-action-mismatch", "lease action does not match sealed context")
    path = _lease_path(root)
    if not path.is_file():
        raise ToolError("lease-not-live", "repository lease is absent")
    try:
        stored = _require_mapping(json.loads(path.read_text(encoding="utf-8")), "stored lease")
    except json.JSONDecodeError as error:
        raise ToolError("lease-invalid", "repository lease is not valid JSON") from error
    if stored.get("status") != "active" or stored.get("action_id") != action_id or stored.get("lease_token") != token:
        raise ToolError("lease-not-live", "repository lease no longer belongs to this action")
    context_id = context.get("context_id")
    if stored.get("context_id") not in {None, context_id}:
        raise ToolError("lease-context-mismatch", "repository lease context differs from sealed context")
    expected_ids = [event["event_id"] for event in events]
    if stored.get("event_ids") is not None and stored.get("event_ids") != expected_ids:
        raise ToolError("lease-event-mismatch", "repository lease events differ from sealed context")
    digest = canonical_json_digest(context)
    if stored.get("context_digest") not in {None, digest}:
        raise ToolError("lease-context-mismatch", "repository lease digest differs from sealed context")
    return {"status": "active", "action_id": action_id, "lease_token": token}


def _subject_paths(root: Path, context: Mapping[str, Any]) -> set[str]:
    """Return the only index paths that may already be staged for this action."""
    result = _require_mapping(context.get("result"), "context.result")
    trigger = _require_mapping(context.get("trigger"), "context.trigger")
    subject = _require_mapping(context.get("subject"), "context.subject")
    if subject.get("kind") == "folder":
        snapshots = _require_mapping(context.get("snapshots"), "context.snapshots")
        committed = snapshots.get("committed")
        previous_entries = committed.get("entries", []) if isinstance(committed, Mapping) else []
        current_entries = result.get("entries", []) if result.get("state") == "present" else []
        return {
            str(entry["path"])
            for entry in [*previous_entries, *current_entries]
            if isinstance(entry, Mapping) and isinstance(entry.get("path"), str)
        }
    paths: set[str] = set()
    if result.get("state") == "present":
        current = _safe_path(root, result.get("path"), "context.result.path")
        paths.add(_relative(root, current))
        before = trigger.get("before_path")
        if isinstance(before, str) and before != _relative(root, current):
            paths.add(_relative(root, _safe_path(root, before, "context.trigger.before_path")))
    elif result.get("state") == "removed":
        paths.add(_relative(root, _safe_path(root, trigger.get("before_path"), "context.trigger.before_path")))
    else:
        raise ToolError("invalid-context", "context.result.state is invalid")
    return paths


def _index_blob(root: Path, relative: str) -> bytes | None:
    completed = subprocess.run(
        ["git", "-C", str(root), "show", f":{relative}"],
        capture_output=True,
        check=False,
    )
    if completed.returncode == 0:
        return completed.stdout
    return None


def _working_bytes(path: Path) -> bytes:
    if path.is_symlink():
        return os.readlink(path).encode("utf-8")
    return path.read_bytes()


def _verify_live_relations(root: Path, context: Mapping[str, Any]) -> None:
    relations = context.get("relations")
    if not isinstance(relations, list):
        raise ToolError("invalid-context", "sealed context has no detailed relation frontier")
    for relation in relations:
        item = _require_mapping(relation, "context.relations item")
        path = _safe_path(root, item.get("path"), "context.relations.path")
        expected = item.get("sha256")
        if not path.is_file() or not isinstance(expected, str) or not HEX64.fullmatch(expected):
            raise ToolError("stale-context", "direct relation frontier is unavailable")
        if _sha256(path.read_bytes()) != expected:
            raise ToolError("stale-context", "direct relation frontier digest changed after context sealing")


def _preflight_commit_boundary(root: Path, context: Mapping[str, Any]) -> None:
    """Repeat mutable checks while permitting only sealed subject index entries."""
    git_base = _require_mapping(context.get("git_base"), "context.git_base")
    commit = _require_string(git_base, "commit")
    tree = _require_string(git_base, "tree")
    if _git_text(root, "rev-parse", "HEAD") != commit or _git_text(root, "rev-parse", "HEAD^{tree}") != tree:
        raise ToolError("stale-context", "Git base changed after context sealing")
    allowed = _subject_paths(root, context)
    staged = {value.decode("utf-8") for value in _git(root, "diff", "--cached", "--name-only", "--no-renames", "-z").split(b"\0") if value}
    if not staged.issubset(allowed):
        raise ToolError("unrelated-staged-change", "repository index contains a staged path outside the sealed subject action")
    result = _require_mapping(context.get("result"), "context.result")
    subject = _require_mapping(context.get("subject"), "context.subject")
    if subject.get("kind") == "folder" and result.get("state") == "present":
        entries = result.get("entries")
        if not isinstance(entries, list) or not entries:
            raise ToolError("invalid-context", "present folder result has no entries")
        for entry in entries:
            item = _require_mapping(entry, "context.result.entries item")
            current = _safe_path(root, item.get("path"), "context.result.entries.path")
            expected = item.get("sha256")
            if (not current.is_file() and not current.is_symlink()) or not isinstance(expected, str) or _sha256(_working_bytes(current)) != expected:
                raise ToolError("stale-context", "folder entry no longer matches the sealed result")
            relative = _relative(root, current)
            staged_blob = _index_blob(root, relative)
            if relative in staged and (staged_blob is None or _sha256(staged_blob) != expected):
                raise ToolError("stale-context", "staged folder entry differs from sealed result")
        current_paths = {str(entry["path"]) for entry in entries}
        for previous in allowed.difference(current_paths):
            if (root / previous).exists() or ((root / previous).is_symlink()):
                raise ToolError("stale-context", "removed folder entry has reappeared")
            if previous in staged and _index_blob(root, previous) is not None:
                raise ToolError("stale-context", "staged prior folder entry is not deleted")
    elif result.get("state") == "present":
        current = _safe_path(root, result.get("path"), "context.result.path")
        expected = result.get("sha256")
        if (not current.is_file() and not current.is_symlink()) or not isinstance(expected, str) or _sha256(_working_bytes(current)) != expected:
            raise ToolError("stale-context", "subject carrier no longer matches the sealed result")
        relative = _relative(root, current)
        staged_blob = _index_blob(root, relative)
        if relative in staged and (staged_blob is None or _sha256(staged_blob) != expected):
            raise ToolError("stale-context", "staged subject carrier differs from sealed result")
        for previous in allowed.difference({relative}):
            if previous in staged and _index_blob(root, previous) is not None:
                raise ToolError("stale-context", "staged prior subject carrier is not deleted")
    else:
        for removed in allowed:
            if (root / removed).exists() or (root / removed).is_symlink():
                raise ToolError("stale-context", "removed subject carrier has reappeared")
            if removed in staged and _index_blob(root, removed) is not None:
                raise ToolError("stale-context", "staged removed subject carrier is not deleted")
    _verify_live_relations(root, context)


def _git_show_bytes(root: Path, revision: str, relative: str) -> bytes | None:
    completed = subprocess.run(
        ["git", "-C", str(root), "show", f"{revision}:{relative}"],
        capture_output=True,
        check=False,
    )
    if completed.returncode == 0:
        return completed.stdout
    message = completed.stderr.decode("utf-8", errors="replace")
    if "does not exist" in message or "exists on disk, but not in" in message or "Path '" in message:
        return None
    raise ToolError("git-command-failed", message.strip() or "cannot inspect Git carrier")


def _parse_name_status(payload: bytes) -> list[dict[str, str | None]]:
    """Parse Git's NUL-delimited name-status output without losing renames."""
    tokens = payload.split(b"\0")
    if tokens and tokens[-1] == b"":
        tokens.pop()
    records: list[dict[str, str | None]] = []
    index = 0
    try:
        while index < len(tokens):
            status = tokens[index].decode("ascii", errors="strict")
            index += 1
            if not status or status[0] not in "ACDMRTUXB":
                raise ToolError("git-diff-invalid", "Git returned an unsupported staged status")
            before: str | None = None
            after: str | None = None
            if status[0] in {"R", "C"}:
                before = tokens[index].decode("utf-8", errors="strict")
                after = tokens[index + 1].decode("utf-8", errors="strict")
                index += 2
            else:
                path = tokens[index].decode("utf-8", errors="strict")
                index += 1
                if status[0] == "D":
                    before = path
                else:
                    after = path
                    if status[0] not in {"A"}:
                        before = path
            records.append({"status": status, "before_path": before, "after_path": after})
    except (IndexError, UnicodeDecodeError) as error:
        raise ToolError("git-diff-invalid", "Git returned malformed path data") from error
    return records


def _staged_change_records(root: Path) -> list[dict[str, str | None]]:
    return _parse_name_status(_git(root, "diff", "--cached", "--name-status", "-z", "--find-renames", "HEAD", "--"))


def _commit_change_records(root: Path, parent: str, revision: str) -> list[dict[str, str | None]]:
    return _parse_name_status(_git(root, "diff", "--name-status", "-z", "--find-renames", parent, revision, "--"))


def _changed_paths(records: Sequence[Mapping[str, str | None]]) -> set[str]:
    return {
        path
        for record in records
        for path in (record.get("before_path"), record.get("after_path"))
        if isinstance(path, str) and path
    }


def _is_project_subject_path(root: Path, path: str) -> bool:
    candidate = Path(path)
    if candidate.is_absolute() or not candidate.parts or ".." in candidate.parts or _is_journal_path(path):
        return False
    if len(candidate.parts) > 1 and candidate.parts[0].startswith(".") and candidate.parts[0] != ".caprmedio":
        return False
    completed = subprocess.run(
        ["git", "-C", str(root), "check-ignore", "--no-index", "-q", "--", path],
        check=False,
        capture_output=True,
    )
    if completed.returncode not in {0, 1}:
        raise ToolError("git-ignore-check-failed", completed.stderr.decode("utf-8", "replace").strip() or "cannot evaluate Git ignore rules")
    return completed.returncode == 1


def _is_journal_path(path: str) -> bool:
    candidate = Path(path)
    return (
        len(candidate.parts) >= 3
        and candidate.parts[:2] == (".caprmedio", "work_journal")
        and candidate.suffix == ".ndjson"
    )


def _journal_rows(data: bytes, relative: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(data.splitlines(), start=1):
        if not line:
            continue
        try:
            raw = json.loads(line)
        except json.JSONDecodeError as error:
            raise ToolError("journal-syntax-invalid", f"{relative}:{line_number} is not valid NDJSON") from error
        rows.append(_require_mapping(raw, f"{relative}:{line_number}"))
    return rows


def _validate_event(event: Mapping[str, Any]) -> dict[str, Any]:
    try:
        sealed = validate_sealed_event(event)
    except WorkJournalError as error:
        raise ToolError(error.code, str(error)) from error
    unsigned = dict(sealed)
    digest = unsigned.pop("event_digest", None)
    if not isinstance(digest, str) or not HEX64.fullmatch(digest) or canonical_json_digest(unsigned) != digest:
        raise ToolError("journal-event-digest-invalid", "Journal event digest does not match its canonical record")
    return sealed


def _journal_additions(
    root: Path,
    records: Sequence[Mapping[str, str | None]],
    *,
    base_revision: str,
    current_bytes: Any,
) -> tuple[list[dict[str, Any]], list[str]]:
    events: list[dict[str, Any]] = []
    carriers: list[str] = []
    for record in records:
        paths = [path for path in (record.get("before_path"), record.get("after_path")) if isinstance(path, str)]
        journal_paths = [path for path in paths if _is_journal_path(path)]
        if not journal_paths:
            continue
        if record.get("status", "")[0] not in {"A", "M"} or len(set(journal_paths)) != 1:
            raise ToolError("journal-not-append-only", "Journal carriers may only be added or appended at a governed commit boundary")
        relative = journal_paths[0]
        base = _git_show_bytes(root, base_revision, relative) or b""
        current = current_bytes(relative)
        if current is None or not current.startswith(base):
            raise ToolError("journal-not-append-only", "staged Journal content does not preserve the committed prefix")
        if base and not base.endswith(b"\n"):
            raise ToolError("journal-base-invalid", "committed Journal carrier lacks terminal newline")
        addition = current[len(base) :]
        added_rows = _journal_rows(addition, relative)
        if not added_rows:
            raise ToolError("journal-sidecar-empty", "changed Journal carrier contains no appended record")
        events.extend(_validate_event(row) for row in added_rows)
        carriers.append(relative)
    return events, sorted(set(carriers))


def _base_journal_event(root: Path, revision: str, event_id: str) -> dict[str, Any] | None:
    paths = [
        value
        for value in _git(root, "ls-tree", "-r", "--name-only", "-z", revision, "--", ".caprmedio/work_journal").decode("utf-8").split("\0")
        if value and _is_journal_path(value)
    ]
    for relative in paths:
        data = _git_show_bytes(root, revision, relative)
        if data is None:
            continue
        for row in _journal_rows(data, relative):
            if row.get("event_id") == event_id:
                return _validate_event(row)
    return None


def _previous_result(root: Path, completed: Mapping[str, Any], events: Sequence[Mapping[str, Any]], base_revision: str) -> dict[str, Any] | None:
    previous_id = completed.get("previous_result_event")
    if previous_id is None:
        return None
    if not isinstance(previous_id, str) or not previous_id:
        raise ToolError("previous-result-invalid", "previous_result_event must be a non-empty event identity")
    previous = next((dict(event) for event in events if event.get("event_id") == previous_id), None)
    if previous is None:
        previous = _base_journal_event(root, base_revision, previous_id)
    if previous is None:
        raise ToolError("previous-result-missing", "the completed event's previous result cannot be resolved")
    return _require_mapping(previous.get("result"), "previous Journal result")


def _evaluate_governed_boundary(
    root: Path,
    records: Sequence[Mapping[str, str | None]],
    *,
    base_revision: str,
    current_bytes: Any,
) -> dict[str, Any]:
    paths = _changed_paths(records)
    forbidden = sorted(
        path
        for path in paths
        if path == ".git"
        or path.startswith(".git/")
        or path == ".caprmedio_install"
        or path.startswith(".caprmedio_install/")
        or path == ".caprmedio_runtime"
        or path.startswith(".caprmedio_runtime/")
    )
    if forbidden:
        raise ToolError("local-machine-path-staged", "installation, runtime, and Git-internal paths cannot be part of a governed commit")
    subject_paths = {path for path in paths if _is_project_subject_path(root, path)}
    journal_paths = {path for path in paths if _is_journal_path(path)}
    governed = bool(subject_paths or journal_paths)
    if not governed:
        return {"governed": False, "changed_paths": sorted(paths), "validation_results": [{"name": "ordinary-commit-boundary", "ok": True}]}
    if not subject_paths:
        raise ToolError("governed-subject-missing", "a governed Journal boundary has no project-path subject change")
    if not journal_paths:
        raise ToolError("governed-journal-missing", "a governed Atom boundary has no Journal sidecar")
    events, carriers = _journal_additions(root, records, base_revision=base_revision, current_bytes=current_bytes)
    action_ids = {event.get("action_id") for event in events}
    if len(action_ids) != 1 or not all(isinstance(value, str) and value for value in action_ids):
        raise ToolError("journal-action-mismatch", "all appended Journal records must share one action identity")
    completed = _completed_event(events)
    previous = _previous_result(root, completed, events, base_revision)
    result = _require_mapping(completed.get("result"), "completed result")
    action_type = completed.get("action_type")
    if action_type not in ACTION_TYPES:
        raise ToolError("journal-action-invalid", "completed Journal action_type is invalid")
    if action_type == "ADD":
        if previous is not None or result.get("state") != "present":
            raise ToolError("governed-subject-mismatch", "ADD must have one present result and no previous result")
        expected_subjects = {str(result.get("path"))}
    elif action_type == "REMOVE":
        if previous is None or result.get("state") != "removed":
            raise ToolError("governed-subject-mismatch", "REMOVE must have one removed result and one previous result")
        expected_subjects = {str(previous.get("path"))}
    else:
        if previous is None or result.get("state") != "present":
            raise ToolError("governed-subject-mismatch", f"{action_type} must have present previous and current results")
        expected_subjects = {str(previous.get("path")), str(result.get("path"))}
    subject_kind = completed.get("subject_kind", "file")
    if subject_kind == "folder":
        current_entries = result.get("entries", []) if result.get("state") == "present" else []
        previous_entries = previous.get("entries", []) if isinstance(previous, Mapping) else []
        expected_subjects = {
            str(entry["path"])
            for entry in [*previous_entries, *current_entries]
            if isinstance(entry, Mapping) and isinstance(entry.get("path"), str)
        }
        # Only changed entries appear in a Git boundary; unchanged entries are
        # sealed in the folder result but must not be required in the diff.
        expected_subjects = {
            path for path in expected_subjects
            if _git_show_bytes(root, base_revision, path) != current_bytes(path)
        }
    if not expected_subjects or "None" in expected_subjects or subject_paths != expected_subjects:
        raise ToolError("governed-subject-mismatch", "changed project paths do not match the structured Journal result lineage")
    current_path = result.get("path")
    if result.get("state") == "present" and subject_kind == "folder":
        entries = result.get("entries")
        if not isinstance(entries, list) or canonical_json_digest([
            {"path": Path(entry["path"]).relative_to(str(result.get("path"))).as_posix(), "sha256": entry["sha256"]}
            for entry in entries
        ]) != result.get("sha256"):
            raise ToolError("governed-subject-mismatch", "current folder result has an invalid entry digest")
        for entry in entries:
            current = current_bytes(str(entry["path"]))
            if current is None or _sha256(current) != entry.get("sha256"):
                raise ToolError("governed-subject-mismatch", "current folder entry differs from the Journal result")
    elif result.get("state") == "present":
        if not isinstance(current_path, str) or Path(current_path).name != result.get("filename"):
            raise ToolError("governed-subject-mismatch", "current result filename and path disagree")
        current = current_bytes(current_path)
        if current is None or _sha256(current) != result.get("sha256"):
            raise ToolError("governed-subject-mismatch", "current Atom bytes differ from the Journal result")
    if previous is not None and subject_kind == "folder":
        entries = previous.get("entries")
        if not isinstance(entries, list) or canonical_json_digest([
            {"path": Path(entry["path"]).relative_to(str(previous.get("path"))).as_posix(), "sha256": entry["sha256"]}
            for entry in entries
        ]) != previous.get("sha256"):
            raise ToolError("governed-subject-mismatch", "previous folder result has an invalid entry digest")
        for entry in entries:
            base = _git_show_bytes(root, base_revision, str(entry["path"]))
            if base is None or _sha256(base) != entry.get("sha256"):
                raise ToolError("governed-subject-mismatch", "base folder entry differs from the previous Journal result")
    elif previous is not None:
        previous_path = previous.get("path")
        if not isinstance(previous_path, str) or Path(previous_path).name != previous.get("filename"):
            raise ToolError("governed-subject-mismatch", "previous result filename and path disagree")
        base = _git_show_bytes(root, base_revision, previous_path)
        if base is None or _sha256(base) != previous.get("sha256"):
            raise ToolError("governed-subject-mismatch", "base Atom bytes differ from the previous Journal result")
    allowed_paths = subject_paths | journal_paths
    if paths != allowed_paths:
        raise ToolError("governed-extra-path", "governed commit contains a path outside its subject and Journal sidecars")
    try:
        message = event_message(completed, previous)
    except ContextError as error:
        raise ToolError(error.code, str(error)) from error
    return {
        "governed": True,
        "action_id": next(iter(action_ids)),
        "action_type": action_type,
        "subject_paths": sorted(subject_paths),
        "journal_paths": carriers,
        "changed_paths": sorted(paths),
        "expected_message": message,
        "completed_event_id": completed["event_id"],
        "validation_results": [
            {"name": "singular-governed-subject", "ok": True},
            {"name": "related-journal-sidecars", "ok": True},
            {"name": "structured-result-lineage", "ok": True},
        ],
    }


def evaluate_pre_commit(root: Path) -> dict[str, Any]:
    root = repository_root(root)
    if _git(root, "ls-files", "-u", "-z"):
        raise ToolError("unresolved-index", "repository index contains unresolved merge entries")
    checked = subprocess.run(["git", "-C", str(root), "diff", "--cached", "--check"], capture_output=True, check=False)
    if checked.returncode != 0:
        detail = (checked.stdout or checked.stderr).decode("utf-8", errors="replace").strip()
        raise ToolError("staged-content-invalid", detail or "staged content fails Git validation")
    result = _evaluate_governed_boundary(
        root,
        _staged_change_records(root),
        base_revision="HEAD",
        current_bytes=lambda path: _index_blob(root, path),
    )
    return {**result, "phase": "pre-commit"}


def evaluate_commit_message(root: Path, message_file: Path) -> dict[str, Any]:
    root = repository_root(root)
    result = _evaluate_governed_boundary(
        root,
        _staged_change_records(root),
        base_revision="HEAD",
        current_bytes=lambda path: _index_blob(root, path),
    )
    if not result["governed"]:
        return {**result, "phase": "commit-msg"}
    try:
        message = message_file.read_text(encoding="utf-8").rstrip("\n")
    except OSError as error:
        raise ToolError("commit-message-unreadable", f"cannot read commit message carrier: {message_file}") from error
    if message != result["expected_message"] or "\n" in message:
        raise ToolError("commit-message-mismatch", "governed commit message differs from its exact deterministic Projection")
    return {**result, "phase": "commit-msg", "message_valid": True}


def observe_post_commit(root: Path) -> dict[str, Any]:
    root = repository_root(root)
    commit = _git_text(root, "rev-parse", "HEAD")
    parents = _git_text(root, "rev-list", "--parents", "-n", "1", commit).split()
    parent = parents[1] if len(parents) > 1 else "4b825dc642cb6eb9a060e54bf8d69288fbee4904"
    diagnostics: list[dict[str, str]] = []
    try:
        result = _evaluate_governed_boundary(
            root,
            _commit_change_records(root, parent, commit),
            base_revision=parent,
            current_bytes=lambda path: _git_show_bytes(root, commit, path),
        )
        if result["governed"]:
            message = _git(root, "show", "-s", "--format=%B", commit).decode("utf-8", errors="strict").rstrip("\n")
            if message != result["expected_message"] or "\n" in message:
                raise ToolError("commit-message-mismatch", "created governed commit message differs from its deterministic Projection")
        valid = True
    except ToolError as error:
        result = {
            "governed": any(_is_project_subject_path(root, path) or _is_journal_path(path) for path in _changed_paths(_commit_change_records(root, parent, commit))),
            "changed_paths": sorted(_changed_paths(_commit_change_records(root, parent, commit))),
        }
        diagnostics.append({"code": error.code, "message": str(error)})
        valid = False
    observation_core = {
        "schema_version": 1,
        "event": "commit_observed",
        "commit": commit,
        "parent": parent,
        "governed": bool(result["governed"]),
        "valid": valid,
        "changed_paths": result["changed_paths"],
        "action_id": result.get("action_id"),
        "completed_event_id": result.get("completed_event_id"),
        "diagnostics": diagnostics,
    }
    observation = {"observation_id": canonical_json_digest(observation_core), **observation_core}
    log = root / ".caprmedio_runtime" / "logs" / "git_hooks" / f"{dt.datetime.now().astimezone():%Y-%m-%d}.ndjson"
    log.parent.mkdir(parents=True, exist_ok=True)
    existing_ids = {
        row.get("observation_id")
        for row in _journal_rows(log.read_bytes(), _relative(root, log))
    } if log.is_file() else set()
    appended = observation["observation_id"] not in existing_ids
    if appended:
        with log.open("ab") as handle:
            handle.write(canonical_json_bytes(observation) + b"\n")
            handle.flush()
            os.fsync(handle.fileno())
    return {
        **result,
        "phase": "post-commit",
        "commit": commit,
        "parent": parent,
        "valid": valid,
        "diagnostics": diagnostics,
        "observation": _relative(root, log),
        "observation_appended": appended,
    }


def _stage_blob(root: Path, relative: str, data: bytes, *, mode: str) -> None:
    blob = _git(root, "hash-object", "-w", "--stdin", input_bytes=data).decode("ascii").strip()
    _git(root, "update-index", "--add", "--cacheinfo", f"{mode},{blob},{relative}")


def _tracked_mode(root: Path, relative: str) -> str:
    value = _git_text(root, "ls-tree", "HEAD", "--", relative)
    if not value:
        return "100644"
    return value.split(maxsplit=1)[0]


def _is_tracked(root: Path, relative: str) -> bool:
    completed = subprocess.run(
        ["git", "-C", str(root), "ls-files", "--error-unmatch", "--", relative],
        capture_output=True,
        check=False,
    )
    if completed.returncode in {0, 1}:
        return completed.returncode == 0
    detail = (completed.stderr or completed.stdout).decode("utf-8", errors="replace").strip()
    raise ToolError("git-command-failed", detail or "cannot inspect Git index")


def _stage_subject(root: Path, context: Mapping[str, Any]) -> set[str]:
    result = _require_mapping(context.get("result"), "context.result")
    action_type = context.get("action_type")
    if action_type not in ACTION_TYPES:
        raise ToolError("invalid-context", "context.action_type is invalid")
    trigger = _require_mapping(context.get("trigger"), "context.trigger")
    before_path = trigger.get("before_path")
    staged: set[str] = set()
    subject = _require_mapping(context.get("subject"), "context.subject")
    if subject.get("kind") == "folder":
        snapshots = _require_mapping(context.get("snapshots"), "context.snapshots")
        committed = snapshots.get("committed")
        previous_entries = committed.get("entries", []) if isinstance(committed, Mapping) else []
        current_entries = result.get("entries", []) if result.get("state") == "present" else []
        previous_paths = {str(entry["path"]): str(entry["sha256"]) for entry in previous_entries}
        current_paths = {str(entry["path"]): str(entry["sha256"]) for entry in current_entries}
        for relative, sha256 in sorted(current_paths.items()):
            path = _safe_path(root, relative, "context.result.entries.path")
            if (not path.is_file() and not path.is_symlink()) or _sha256(_working_bytes(path)) != sha256:
                raise ToolError("stale-context", "folder entry no longer exists at its sealed digest")
            base = _git_show_bytes(root, "HEAD", relative)
            if base is None or _sha256(base) != sha256:
                _git(root, "add", "--", relative)
                staged.add(relative)
        for relative in sorted(set(previous_paths).difference(current_paths)):
            path = _safe_path(root, relative, "context.snapshots.committed.entries.path")
            if path.exists() or path.is_symlink():
                raise ToolError("stale-context", "removed folder entry has reappeared")
            if _is_tracked(root, relative):
                _git(root, "update-index", "--force-remove", "--", relative)
                staged.add(relative)
        if not staged:
            raise ToolError("stale-context", "folder action produces no Git entry change")
        return staged
    if result.get("state") == "present":
        current = _safe_path(root, result.get("path"), "context.result.path")
        if not current.is_file() and not current.is_symlink():
            raise ToolError("stale-context", "subject carrier no longer exists")
        relative = _relative(root, current)
        _git(root, "add", "--", relative)
        staged.add(relative)
        if isinstance(before_path, str) and before_path != relative:
            old = _safe_path(root, before_path, "context.trigger.before_path")
            if old.exists():
                raise ToolError("stale-context", "relocated subject previous path has reappeared")
            old_relative = _relative(root, old)
            if _is_tracked(root, old_relative):
                _git(root, "update-index", "--force-remove", "--", old_relative)
                staged.add(old_relative)
        return staged
    if result.get("state") == "removed":
        old = _safe_path(root, before_path, "context.trigger.before_path")
        if old.exists():
            raise ToolError("stale-context", "removed subject carrier has reappeared")
        relative = _relative(root, old)
        if not _is_tracked(root, relative):
            raise ToolError("stale-context", "removed subject carrier is not tracked at commit boundary")
        _git(root, "update-index", "--force-remove", "--", relative)
        staged.add(relative)
        return staged
    raise ToolError("invalid-context", "context.result.state is invalid")


def _stage_receipt_sidecars(root: Path, events: Sequence[Mapping[str, Any]], receipts: Sequence[Mapping[str, Any]]) -> set[str]:
    """Put only receipt-bound NDJSON rows into the index, never adjacent work."""
    by_carrier: dict[str, list[dict[str, Any]]] = {}
    for event, receipt in zip(events, receipts, strict=True):
        relative = _relative(root, _safe_path(root, receipt["carrier"], "receipt.carrier"))
        by_carrier.setdefault(relative, []).append(dict(event))
    staged: set[str] = set()
    for relative, carrier_events in sorted(by_carrier.items()):
        base = _git_show_bytes(root, "HEAD", relative) or b""
        try:
            previous_rows = [json.loads(line) for line in base.splitlines() if line]
        except json.JSONDecodeError as error:
            raise ToolError("journal-base-invalid", "committed Journal carrier is not NDJSON") from error
        known = {(row.get("event_id"), row.get("event_digest")) for row in previous_rows if isinstance(row, Mapping)}
        additions = [event for event in carrier_events if (event["event_id"], event["event_digest"]) not in known]
        if not additions:
            continue
        if base and not base.endswith(b"\n"):
            raise ToolError("journal-base-invalid", "committed Journal carrier lacks terminal newline")
        desired = base + b"".join(canonical_json_bytes(event) + b"\n" for event in additions)
        _stage_blob(root, relative, desired, mode=_tracked_mode(root, relative))
        staged.add(relative)
    return staged


def _restore_our_index_paths(root: Path, paths: Sequence[str]) -> None:
    if paths:
        _git(root, "reset", "--", *sorted(set(paths)))


def _verify_commit(root: Path, *, parent: str, message: str, expected_paths: set[str], events: Sequence[Mapping[str, Any]]) -> str:
    commit = _git_text(root, "rev-parse", "HEAD")
    if _git_text(root, "rev-parse", "HEAD^") != parent:
        raise ToolError("commit-parent-mismatch", "created commit does not retain sealed Git base as its parent")
    if _git(root, "show", "-s", "--format=%B", "HEAD").decode("utf-8").strip("\n") != message:
        raise ToolError("commit-message-mismatch", "created commit message differs from the deterministic projection")
    changed = {value for value in _git(root, "diff-tree", "--no-commit-id", "--name-only", "--no-renames", "-r", "HEAD").decode("utf-8").splitlines() if value}
    if changed != expected_paths:
        raise ToolError("commit-tree-mismatch", "created commit contains paths outside the exact governed subject and sidecars")
    for event in events:
        event_id = event["event_id"]
        found = False
        for path in changed:
            if not path.endswith(".ndjson"):
                continue
            data = _git_show_bytes(root, "HEAD", path)
            if data is not None and any(json.loads(line).get("event_id") == event_id for line in data.splitlines() if line):
                found = True
                break
        if not found:
            raise ToolError("commit-sidecar-mismatch", "created commit does not contain each receipt-bound Journal event")
    return commit


def _record_blocked(appender: Any, root: Path, context: Mapping[str, Any], events: Sequence[Mapping[str, Any]], receipts: Sequence[Mapping[str, Any]], lease: Mapping[str, Any], reason: str) -> None:
    try:
        appender.record_blocked_state(
            root,
            lease=lease,
            action_id=str(context["action_id"]),
            event_ids=[str(event["event_id"]) for event in events],
            receipts=list(receipts),
            reason=reason,
        )
    except Exception as error:
        raise ToolError("blocked-state-write-failed", f"could not preserve failed action state: {error}") from error


def _release_verified_lease(appender: Any, root: Path, lease: Mapping[str, Any]) -> None:
    try:
        appender.release_verified_lease(root, lease)
    except AttributeError as error:  # pragma: no cover - caught by integration until peer lands
        raise ToolError("peer-contract-incomplete", "APPEND_CHANGE_RECORDS does not expose release_verified_lease") from error
    except Exception as error:
        if hasattr(error, "code"):
            raise ToolError(str(error.code), str(error)) from error
        raise ToolError("lease-release-failed", str(error)) from error


def _appender_effects(envelope: object) -> dict[str, Any]:
    """Accept only the peer's common success envelope, never a loose mapping."""
    value = _require_mapping(envelope, "APPEND_CHANGE_RECORDS result envelope")
    tool = _require_mapping(value.get("tool"), "APPEND_CHANGE_RECORDS tool")
    if value.get("ok") is not True or tool.get("capability_id") != "APPEND_CHANGE_RECORDS" or tool.get("kind") != "doer":
        raise ToolError("journal-append-failed", "APPEND_CHANGE_RECORDS returned an unsuccessful or incompatible envelope")
    return _require_mapping(value.get("result"), "APPEND_CHANGE_RECORDS result")


def _block_proven_corrupt_context(appender: Any, root: Path, payload: Mapping[str, Any], cause: ToolError) -> None:
    """Retain a post-append failure only when independent evidence proves it.

    A malformed context normally rejects without a write (E196).  After a
    successful append, though, an operator can present an accidentally damaged
    context such as one missing ``result``.  The live lease, exact receipts,
    and durable Journal lines are sufficient to prove that this is the already
    appended action, so it must become observable and retryable (E204) rather
    than silently disappear.  Nothing is written when that independent proof
    is incomplete or mismatched.
    """
    if "receipts" not in payload or "lease" not in payload:
        return
    context = payload.get("context", payload)
    if not isinstance(context, Mapping):
        return
    action_id = context.get("action_id")
    if not isinstance(action_id, str) or not action_id:
        return
    try:
        supplied_lease = _require_mapping(payload["lease"], "lease")
        token = _require_string(supplied_lease, "lease_token")
        if supplied_lease.get("status") != "active" or supplied_lease.get("action_id") != action_id:
            return
        stored = _require_mapping(json.loads(_lease_path(root).read_text(encoding="utf-8")), "stored lease")
        if stored.get("status") != "active" or stored.get("action_id") != action_id or stored.get("lease_token") != token:
            return
        event_ids = stored.get("event_ids")
        receipts = payload["receipts"]
        if not isinstance(event_ids, list) or not isinstance(receipts, list) or len(event_ids) != len(receipts):
            return
        verified: list[dict[str, Any]] = []
        for raw, expected_event_id in zip(receipts, event_ids, strict=True):
            receipt = _require_mapping(raw, "receipt")
            if receipt.get("action_id") != action_id or receipt.get("event_id") != expected_event_id:
                return
            carrier = _safe_path(root, receipt.get("carrier"), "receipt.carrier")
            line = receipt.get("line")
            if not carrier.is_file() or not isinstance(line, int) or line < 1:
                return
            lines = carrier.read_bytes().splitlines(keepends=True)
            if line > len(lines):
                return
            previous = b"".join(lines[: line - 1])
            appended = b"".join(lines[:line])
            if _sha256(previous) != receipt.get("previous_carrier_digest") or _sha256(appended) != receipt.get("appended_carrier_digest"):
                return
            record = json.loads(lines[line - 1])
            if not isinstance(record, Mapping) or record.get("event_id") != expected_event_id or record.get("action_id") != action_id or record.get("event_digest") != receipt.get("event_digest"):
                return
            verified.append(receipt)
        _record_blocked(
            appender,
            root,
            {"action_id": action_id},
            [{"event_id": event_id} for event_id in event_ids],
            verified,
            {"status": "active", "action_id": action_id, "lease_token": token},
            cause.code,
        )
    except (OSError, json.JSONDecodeError, ToolError):
        return


def _commit_only(
    root: Path,
    appender: Any,
    context: Mapping[str, Any],
    events: Sequence[Mapping[str, Any]],
    receipts: object,
    lease: object,
    *,
    pipeline_correlations: object = (),
) -> dict[str, Any]:
    """Execute the final, receipt-bound Git mutation boundary."""
    verified_receipts = _validate_receipts(root, context, events, receipts)
    verified_lease = _validate_lease(root, context, events, lease)
    try:
        _preflight_commit_boundary(root, context)
    except ToolError as error:
        _record_blocked(appender, root, context, events, verified_receipts, verified_lease, error.code)
        raise
    parent = _require_mapping(context.get("git_base"), "context.git_base").get("commit")
    if not isinstance(parent, str) or not HEX40.fullmatch(parent):
        raise ToolError("invalid-context", "context.git_base.commit is invalid")
    message = _render_message(context, events)
    staged: set[str] = set()
    try:
        staged.update(_stage_subject(root, context))
        staged.update(_stage_receipt_sidecars(root, events, verified_receipts))
        actual_staged = {value for value in _git(root, "diff", "--cached", "--name-only", "--no-renames", "-z").decode("utf-8").split("\0") if value}
        if actual_staged != staged:
            raise ToolError("staging-mismatch", "index does not contain exactly the governed subject and receipt-bound sidecars")
        _git(root, "commit", "-m", message)
        commit = _verify_commit(root, parent=parent, message=message, expected_paths=staged, events=events)
    except ToolError as error:
        _restore_our_index_paths(root, sorted(staged))
        _record_blocked(appender, root, context, events, verified_receipts, verified_lease, error.code)
        raise
    try:
        _release_verified_lease(appender, root, verified_lease)
    except ToolError as error:
        # The commit is already verified, but a retained lease still blocks
        # future work and therefore must be visible for operator recovery.
        _record_blocked(appender, root, context, events, verified_receipts, verified_lease, error.code)
        raise
    return {
        "context": context,
        "receipts": verified_receipts,
        "lease": {**verified_lease, "status": "released"},
        "git_message": message,
        "pipeline_correlations": list(pipeline_correlations) if isinstance(pipeline_correlations, (list, tuple)) else [],
        "commit": commit,
        "validation_results": [
            {"name": "sealed-context", "ok": True},
            {"name": "receipt-set", "ok": True},
            {"name": "live-lease", "ok": True},
            {"name": "pre-mutation-revalidation", "ok": True},
            {"name": "commit-verification", "ok": True},
        ],
    }


def run(root: Path, payload: Mapping[str, Any], *, apply: bool, wait_seconds: float = 30.0) -> dict[str, Any]:
    """Run one complete or commit-only flow; this is the importable Tool API."""
    if wait_seconds < 0:
        raise ToolError("invalid-input", "wait_seconds must be non-negative")
    root = repository_root(root)
    appender = _import_appender()
    context, input_kind = _context_from_payload(root, payload)
    try:
        validated_context, events = _events_from_context(appender, context)
    except ToolError as error:
        if input_kind == "context" and apply:
            _block_proven_corrupt_context(appender, root, payload, error)
        raise
    message = _render_message(validated_context, events)
    if input_kind == "trigger":
        try:
            appended_envelope = appender.run(root, {"context": validated_context}, apply=apply, wait_seconds=wait_seconds)
        except Exception as error:
            if hasattr(error, "code"):
                raise ToolError(str(error.code), str(error)) from error
            raise ToolError("journal-append-failed", str(error)) from error
        appended = _appender_effects(appended_envelope)
        if not apply:
            return {
                "context": validated_context,
                "change_set": {"action_type": validated_context["action_type"], "subject": validated_context["subject"], "sources": validated_context["sources"]},
                "journal_records": events,
                "receipts": appended["receipts"],
                "lease": appended["lease"],
                "git_message": message,
                "validation_results": [*appended.get("validation_results", []), {"name": "commit-prediction", "ok": True}],
                "pipeline_correlations": appended.get("pipeline_correlations", []),
            }
        return _commit_only(
            root,
            appender,
            validated_context,
            events,
            appended.get("receipts"),
            appended.get("lease"),
            pipeline_correlations=appended.get("pipeline_correlations", []),
        )
    if "receipts" not in payload or "lease" not in payload:
        raise ToolError("commit-boundary-input-missing", "commit-only execution requires context, receipts, and lease")
    if not apply:
        # This path deliberately reuses the Appender's dry-run validation but
        # never validates a live lease or mutates any recovery state.
        predicted = _appender_effects(appender.run(root, {"context": validated_context}, apply=False, wait_seconds=wait_seconds))
        return {
            "context": validated_context,
            "change_set": {"action_type": validated_context["action_type"], "subject": validated_context["subject"], "sources": validated_context["sources"]},
            "journal_records": events,
            "receipts": predicted["receipts"],
            "lease": predicted["lease"],
            "git_message": message,
            "validation_results": [*predicted.get("validation_results", []), {"name": "commit-prediction", "ok": True}],
            "pipeline_correlations": predicted.get("pipeline_correlations", []),
        }
    return _commit_only(
        root,
        appender,
        validated_context,
        events,
        payload["receipts"],
        payload["lease"],
        pipeline_correlations=payload.get("pipeline_correlations", []),
    )


def describe() -> dict[str, Any]:
    return {
        "schema_version": TOOL_SCHEMA_VERSION,
        "capability_id": TOOL_ID,
        "kind": TOOL_KIND,
        "canonical_script": "002_FRAMEWORK_ENGINE/TOOLS/COMMIT_CHANGE_SET/commit_change_set.py",
        "input_schema": {
            "trigger_flow": {"required": ["trigger"], "effect": "gather, append, then commit when --apply is present"},
            "commit_only": {"required": ["context", "receipts", "lease"], "effect": "final Git boundary or idempotent retry"},
            "git_hook": {
                "phases": ["pre-commit", "commit-msg", "post-commit"],
                "effect": "evaluate staged or created Git state; only post-commit appends runtime observation evidence",
            },
        },
        "result_envelope": {"ok": "boolean", "mode": "dry-run|apply|read-only|observe", "diagnostics": "ordered machine-readable diagnostics"},
        "dry_run": "fully mutation-free",
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repository",
        "--root",
        dest="repository",
        default=".",
        help="repository root or descendant (--root is a compatibility alias)",
    )
    subcommands = parser.add_subparsers(dest="command", required=True)
    subcommands.add_parser("describe", help="emit the common Tool contract")
    run_parser = subcommands.add_parser("run", help="run an end-to-end trigger or receipt-bound commit")
    run_parser.add_argument("--input", required=True, help="JSON object file or - for stdin")
    run_parser.add_argument("--apply", action="store_true", help="allow Journal and Git mutations; omitted is dry-run")
    run_parser.add_argument("--wait-seconds", type=float, default=30.0, help="maximum repository lease wait for end-to-end apply")
    git_hook = subcommands.add_parser("git-hook", help="evaluate one installed Git Hook boundary")
    git_hook.add_argument("phase", choices=("pre-commit", "commit-msg", "post-commit"))
    git_hook.add_argument("message_file", nargs="?", help="Git-supplied commit message carrier for commit-msg")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "describe":
        print(json.dumps(_envelope(ok=True, mode="read-only", result=describe()), ensure_ascii=False, sort_keys=True, separators=(",", ":")))
        return 0
    if args.command == "git-hook":
        if args.phase == "pre-commit":
            mode = "read-only"
            operation = lambda: evaluate_pre_commit(Path(args.repository))
        elif args.phase == "commit-msg":
            mode = "read-only"
            if args.message_file is None:
                error = ToolError("commit-message-missing", "commit-msg requires Git's message-file argument")
                print(json.dumps(_envelope(ok=False, mode=mode, error=error), ensure_ascii=False, sort_keys=True, separators=(",", ":")))
                return 2
            operation = lambda: evaluate_commit_message(Path(args.repository), Path(args.message_file))
        else:
            mode = "observe"
            operation = lambda: observe_post_commit(Path(args.repository))
        try:
            result = operation()
        except (ToolError, ContextError) as error:
            print(json.dumps(_envelope(ok=False, mode=mode, error=error), ensure_ascii=False, sort_keys=True, separators=(",", ":")))
            return 0 if args.phase == "post-commit" else 2
        ok = result.get("valid", True) is not False
        print(json.dumps(_envelope(ok=ok, mode=mode, result=result), ensure_ascii=False, sort_keys=True, separators=(",", ":")))
        return 0
    mode = "apply" if args.apply else "dry-run"
    try:
        result = run(Path(args.repository), _load_payload(args.input), apply=args.apply, wait_seconds=args.wait_seconds)
    except (ToolError, ContextError) as error:
        print(json.dumps(_envelope(ok=False, mode=mode, error=error), ensure_ascii=False, sort_keys=True, separators=(",", ":")))
        return 2
    print(json.dumps(_envelope(ok=True, mode=mode, result=result), ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
