#!/usr/bin/env python3
"""Commit one exact selected source change, independently of Journal history.

Trigger handoffs append a plain observation after the verified commit. A supplied
Context needs no Journal rows, receipts, leases, or sidecars. Dry-run is read-only.
"""

from __future__ import annotations



import argparse
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
from concurrent.futures import CancelledError as FutureCancelledError
from pathlib import Path
from typing import Any, Mapping, Sequence


SCRIPT_PATH = Path(__file__).resolve()
TOOLS_ROOT = SCRIPT_PATH.parents[1]
CONTEXT_ROOT = TOOLS_ROOT / "COMMIT_CONTEXT"
APPENDER_ROOT = TOOLS_ROOT / "APPEND_CHANGE_RECORDS"
for _parent in SCRIPT_PATH.parents:
    if _parent.name == ".caprmedio_runtime":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_tmp" / "cache" / "python")
        break
    if _parent.name == ".caprmedio_install":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_tmp" / "cache" / "python")
        break
    if _parent.name == ".caprmedio":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_tmp" / "cache" / "python")
        break
for _path in (TOOLS_ROOT, CONTEXT_ROOT, APPENDER_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from commit_context_logic import (  # noqa: E402
    ContextError,
    event_message,
    gather_context,
    is_forbidden_commit_path,
    is_journal_path,
    project_path_eligible,
    validate_context,
    repository_root,
)
from operation_error_boundary import ExplicitBlockingRuntimeFailure, FailureRecord  # noqa: E402
from runtime_failure_diagnostics import report_failure  # noqa: E402
from work_journal import PartialAppendError, canonical_json_bytes, canonical_json_digest  # noqa: E402


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
        if "context" in payload:
            raise ToolError("ambiguous-input", "a trigger handoff cannot also provide context")
        trigger = _require_mapping(payload["trigger"], "trigger")
        try:
            return gather_context(root, trigger), "trigger"
        except ContextError as error:
            raise ToolError(error.code, str(error)) from error
    candidate = _require_mapping(payload.get("context", payload), "context")
    return candidate, "context"


def _validated_context(context: Mapping[str, Any]) -> dict[str, Any]:
    """Validate the source Context, not its optional Journal projection."""
    try:
        validate_context(context)
    except ContextError as error:
        raise ToolError(error.code, str(error)) from error
    return dict(context)


def _render_message(context: Mapping[str, Any]) -> str:
    try:
        return event_message(context, context.get("previous_result"))
    except ContextError as error:
        raise ToolError(error.code, str(error)) from error


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
    return project_path_eligible(root, path)


def _is_journal_path(root: Path, path: str) -> bool:
    return is_journal_path(root, path, require_carrier=True)


def _evaluate_governed_boundary(
    root: Path,
    records: Sequence[Mapping[str, str | None]],
) -> dict[str, Any]:
    """Inspect the available Git path frontier without requiring Journal proof."""
    paths = _changed_paths(records)
    forbidden = [
        path
        for path in paths
        if is_forbidden_commit_path(root, path) or path == ".git" or path.startswith(".git/")
    ]
    if forbidden:
        raise ToolError(
            "local-machine-path-staged",
            "installation, runtime, and Git-internal paths cannot be part of a governed commit",
        )
    subjects = sorted(path for path in paths if _is_project_subject_path(root, path))
    journals = sorted(path for path in paths if _is_journal_path(root, path))
    return {
        "governed": bool(subjects or journals),
        "subject_paths": subjects,
        "journal_paths": journals,
        "changed_paths": sorted(paths),
        "validation_results": [{"name": "git-path-boundary", "ok": True}],
    }


def evaluate_pre_commit(root: Path) -> dict[str, Any]:
    root = repository_root(root)
    if _git(root, "ls-files", "-u", "-z"):
        raise ToolError("unresolved-index", "repository index contains unresolved merge entries")
    checked = subprocess.run(
        ["git", "-C", str(root), "diff", "--cached", "--check"], capture_output=True, check=False
    )
    if checked.returncode != 0:
        detail = (checked.stdout or checked.stderr).decode("utf-8", errors="replace").strip()
        raise ToolError("staged-content-invalid", detail or "staged content fails Git validation")
    result = _evaluate_governed_boundary(
        root,
        _staged_change_records(root),
    )
    return {**result, "phase": "pre-commit"}


def evaluate_commit_message(root: Path, message_file: Path) -> dict[str, Any]:
    root = repository_root(root)
    result = _evaluate_governed_boundary(
        root,
        _staged_change_records(root),
    )
    if not result["governed"]:
        return {**result, "phase": "commit-msg"}
    try:
        message = message_file.read_text(encoding="utf-8").rstrip("\n")
    except OSError as error:
        raise ToolError(
            "commit-message-unreadable", f"cannot read commit message carrier: {message_file}"
        ) from error
    if not message or "\n" in message:
        raise ToolError(
            "commit-message-mismatch", "governed commit requires a non-empty single-line message"
        )
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
        )
        valid = True
    except ToolError as error:
        result = {
            "governed": any(
                _is_project_subject_path(root, path) or _is_journal_path(root, path)
                for path in _changed_paths(_commit_change_records(root, parent, commit))
            ),
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
    log = (
        root
        / ".caprmedio_runtime"
        / "logs"
        / "git_hooks"
        / f"{dt.datetime.now().astimezone():%Y-%m-%d}.ndjson"
    )
    log.parent.mkdir(parents=True, exist_ok=True)
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
        "observation_appended": True,
    }


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


def _restore_our_index_paths(root: Path, paths: Sequence[str]) -> None:
    if paths:
        _git(root, "reset", "--", *sorted(set(paths)))


def _verify_commit(
    root: Path, *, parent: str, message: str, expected_paths: set[str], expected_tree: str
) -> str:
    commit = _git_text(root, "rev-parse", "HEAD")
    if _git_text(root, "rev-parse", "HEAD^") != parent:
        raise ToolError(
            "commit-parent-mismatch", "created commit does not retain sealed Git base as its parent"
        )
    if _git(root, "show", "-s", "--format=%B", "HEAD").decode("utf-8").strip("\n") != message:
        raise ToolError(
            "commit-message-mismatch",
            "created commit message differs from the deterministic projection",
        )
    changed = _changed_paths(_commit_change_records(root, parent, commit))
    if changed != expected_paths:
        raise ToolError(
            "commit-tree-mismatch",
            "created commit contains paths outside the exact selected subject",
        )
    if _git_text(root, "rev-parse", "HEAD^{tree}") != expected_tree:
        raise ToolError(
            "commit-tree-mismatch", "created commit differs from the exact staged source bytes"
        )
    return commit


def _appender_effects(envelope: object) -> dict[str, Any]:
    """Accept the peer's common envelope while retaining a partial result."""
    value = _require_mapping(envelope, "APPEND_CHANGE_RECORDS result envelope")
    tool = _require_mapping(value.get("tool"), "APPEND_CHANGE_RECORDS tool")
    if tool.get("capability_id") != "APPEND_CHANGE_RECORDS" or tool.get("kind") != "doer":
        raise ToolError("journal-append-failed", "APPEND_CHANGE_RECORDS returned an unsuccessful or incompatible envelope")
    if value.get("ok") is not True and value.get("ok") is not False:
        raise ToolError("journal-append-failed", "APPEND_CHANGE_RECORDS returned an unsuccessful or incompatible envelope")
    return _require_mapping(value.get("result"), "APPEND_CHANGE_RECORDS result")


def _recording_failure(
    root: Path,
    result: dict[str, Any],
    *,
    code: str,
    message: str,
    correlation_id: str | None,
    diagnostics: Sequence[Mapping[str, Any]] | None = None,
    source: ExplicitBlockingRuntimeFailure | None = None,
) -> dict[str, Any]:
    """Keep the verified commit and expose Journal recording as incomplete."""
    if diagnostics is None:
        failure, secondary = report_failure(
            root,
            source or FailureRecord("WARNING", code, message),
            component=TOOL_ID,
            operation="commit_change_set",
            correlation_id=correlation_id,
        )
        reported = [{"code": failure.code, "message": failure.message}]
        if secondary:
            reported.append({"code": "diagnostic-emission-failed", "message": secondary})
        code, message = failure.code, failure.message
    else:
        reported = [dict(item) for item in diagnostics]
    result["state"] = "partial"
    result["outcome"] = "partial"
    result["incomplete"] = True
    result["error"] = {"code": code, "message": message}
    result["diagnostics"] = reported
    return result


def _commit_only(root: Path, context: Mapping[str, Any]) -> dict[str, Any]:
    """Commit the exact selected source change independently of Journal rows."""
    _preflight_commit_boundary(root, context)
    trigger = _require_mapping(context.get("trigger"), "context.trigger")
    fresh = gather_context(root, {"schema_version": 1, **trigger})
    if fresh["context_id"] != context["context_id"]:
        raise ToolError("stale-context", "source Context changed before staging")
    parent = _require_string(
        _require_mapping(context.get("git_base"), "context.git_base"), "commit"
    )
    message = _render_message(fresh)
    staged: set[str] = set()
    try:
        staged.update(_stage_subject(root, fresh))
        actual = _changed_paths(_staged_change_records(root))
        if actual != staged:
            raise ToolError(
                "staging-mismatch", "index does not contain exactly the selected subject"
            )
        _preflight_commit_boundary(root, fresh)
        evaluate_pre_commit(root)
        tree = _git_text(root, "write-tree")
        _git(root, "commit", "-m", message)
        commit = _verify_commit(
            root, parent=parent, message=message, expected_paths=staged, expected_tree=tree
        )
    except ToolError:
        _restore_our_index_paths(root, sorted(staged))
        raise
    return {
        "context": fresh,
        "git_message": message,
        "commit": commit,
        "validation_results": [
            {"name": "sealed-context", "ok": True},
            {"name": "pre-mutation-revalidation", "ok": True},
            {"name": "commit-verification", "ok": True},
        ],
    }


def run(root: Path, payload: Mapping[str, Any], *, apply: bool) -> dict[str, Any]:
    """Commit a trigger or existing Context; Journal data is never admission proof."""
    root = repository_root(root)
    context, input_kind = _context_from_payload(root, payload)
    context = _validated_context(context)
    if not apply:
        message = _render_message(context)
        predictions = context.get("predictions")
        records = predictions.get("journal_records", []) if isinstance(predictions, Mapping) else []
        return {
            "context": context,
            "change_set": {key: context[key] for key in ("action_type", "subject", "sources")},
            "journal_records": records,
            "git_message": message,
            "validation_results": [{"name": "commit-prediction", "ok": True}],
        }
    result = _commit_only(root, context)
    if input_kind == "trigger":
        # Append the requested observation after the verified commit, not as
        # permission or proof required for that source change.
        try:
            envelope = _import_appender().run(root, {"context": result["context"]}, apply=True)
            logged = _appender_effects(envelope)
            result["receipts"] = logged.get("receipts", [])
            if "uncertain" in logged:
                result["uncertain"] = logged["uncertain"]
            if envelope.get("ok") is not True:
                result = _recording_failure(
                    root,
                    result,
                    code="journal-append-incomplete",
                    message="Journal append stopped before all requested records were observed",
                    correlation_id=result.get("commit"),
                    diagnostics=envelope.get("diagnostics")
                    if isinstance(envelope.get("diagnostics"), list)
                    and envelope["diagnostics"]
                    else None,
                )
        except PartialAppendError as error:
            result["receipts"] = list(error.completed_receipts)
            result["uncertain"] = {
                "record_index": error.uncertain_event_index,
                "state": "unknown",
            }
            result = _recording_failure(
                root,
                result,
                code="journal-append-incomplete",
                message="Journal append stopped before all requested records were observed",
                correlation_id=result.get("commit"),
            )
        except FutureCancelledError:
            raise
        except Exception as error:
            result = _recording_failure(
                root,
                result,
                code="journal-append-failed",
                message="Journal observation append failed",
                correlation_id=result.get("commit"),
                source=error if isinstance(error, ExplicitBlockingRuntimeFailure) else None,
            )
    return result


def describe() -> dict[str, Any]:
    return {
        "schema_version": TOOL_SCHEMA_VERSION,
        "capability_id": TOOL_ID,
        "kind": TOOL_KIND,
        "canonical_script": "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMMIT_CHANGE_SET/commit_change_set.py",
        "input_schema": {
            "trigger_flow": {
                "required": ["trigger"],
                "effect": "commit the exact change, then append its observation when --apply is present",
            },
            "commit_only": {"required": ["context"], "effect": "final exact-source Git boundary"},
            "git_hook": {
                "phases": ["pre-commit", "commit-msg", "post-commit"],
                "effect": "inspect actual Git paths; post-commit records its observation",
            },
        },
        "result_envelope": {
            "ok": "boolean",
            "mode": "dry-run|apply|read-only|observe",
            "diagnostics": "ordered machine-readable diagnostics",
        },
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
    run_parser = subcommands.add_parser(
        "run", help="commit a selected trigger or sealed source Context"
    )
    run_parser.add_argument("--input", required=True, help="JSON object file or - for stdin")
    run_parser.add_argument(
        "--apply", action="store_true", help="allow Journal and Git mutations; omitted is dry-run"
    )
    git_hook = subcommands.add_parser("git-hook", help="evaluate one installed Git Hook boundary")
    git_hook.add_argument("phase", choices=("pre-commit", "commit-msg", "post-commit"))
    git_hook.add_argument(
        "message_file", nargs="?", help="Git-supplied commit message carrier for commit-msg"
    )
    return parser


def _run_hook(args: argparse.Namespace) -> dict[str, Any]:
    if args.phase == "pre-commit":
        return evaluate_pre_commit(Path(args.repository))
    if args.phase == "post-commit":
        return observe_post_commit(Path(args.repository))
    if args.message_file is None:
        raise ToolError("commit-message-missing", "commit-msg requires Git's message-file argument")
    return evaluate_commit_message(Path(args.repository), Path(args.message_file))


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "describe":
        print(
            json.dumps(
                _envelope(ok=True, mode="read-only", result=describe()),
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 0
    if args.command == "git-hook":
        mode = "observe" if args.phase == "post-commit" else "read-only"
        try:
            result = _run_hook(args)
        except (ToolError, ContextError) as error:
            print(
                json.dumps(
                    _envelope(ok=False, mode=mode, error=error),
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )
            return 0 if args.phase == "post-commit" else 2
        ok = result.get("valid", True) is not False
        print(
            json.dumps(
                _envelope(ok=ok, mode=mode, result=result),
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 0
    mode = "apply" if args.apply else "dry-run"
    try:
        result = run(Path(args.repository), _load_payload(args.input), apply=args.apply)
    except (ToolError, ContextError) as error:
        print(
            json.dumps(
                _envelope(ok=False, mode=mode, error=error),
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 2
    ok = result.get("incomplete") is not True
    print(
        json.dumps(
            _envelope(ok=ok, mode=mode, result=result),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if ok else 2


def _image_main():
    return main()


if __name__ == "__main__":
    # Direct script execution needs the shared process boundary available from the tools root.
    import sys
    from pathlib import Path
    _TOOLS_ROOT = next(p for p in Path(__file__).resolve().parents if p.name in {"201_TOOLS", "TOOLS"})
    if str(_TOOLS_ROOT) not in sys.path:
        sys.path.insert(0, str(_TOOLS_ROOT))
    from runtime_process_boundary import run_process
    raise SystemExit(run_process(_image_main, operation="COMMIT_CHANGE_SET/commit_change_set"))
