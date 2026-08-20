#!/usr/bin/env python3
"""Emit minimal, mutation-free triggers for one governed repository file change.

COMMIT_TRIGGER is a Hook Tool.  It receives host-adapter observations as JSON,
coalesces repeated observations of one adapter source event, and emits the
canonical trigger envelope that COMMIT_CHANGE_SET accepts.  It never classifies
the change, reads the Atom graph, modifies the Git index, writes a Journal, or
invokes the downstream Tool itself.

The ``adapter`` lifecycle commands write only reconstructible registration
state below ``.caprmedio_runtime/state/commit_trigger``.  Observation is always
read-only, including when it suppresses a correlated pipeline Journal or
runtime-state event.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import tomllib
import uuid
from collections import defaultdict
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any


SCRIPT_PATH = Path(__file__).resolve()
PACKAGE_ROOT = SCRIPT_PATH.parents[1]


def _installed_runtime_root(path: Path) -> Path | None:
    for parent in path.parents:
        if parent.name == ".caprmedio_runtime":
            return parent
        if parent.name == ".caprmedio":
            return parent.parent / ".caprmedio_runtime"
    return None


if (runtime_root := _installed_runtime_root(SCRIPT_PATH)) is not None:
    sys.pycache_prefix = str(runtime_root / "cache" / "python")

TOOL_SCHEMA_VERSION = 1
TRIGGER_SCHEMA_VERSION = 1
CAPABILITY_ID = "COMMIT_TRIGGER"
TOOL_KIND = "hook"
RUNTIME_DIRECTORY = Path(".caprmedio_runtime/state/commit_trigger")
REGISTRY_NAME = "adapter_registry.toml"
PIPELINE_CORRELATIONS_NAME = "pipeline_correlations.ndjson"
PACKAGE_NAME = "caprmedio-auto-commit"
PACKAGE_FILES = (
    "caprmedio_relation_types.toml",
    "work_journal.py",
    "COMMIT_TRIGGER/__init__.py",
    "COMMIT_TRIGGER/commit_trigger.py",
    "COMMIT_CONTEXT/commit_context.py",
    "COMMIT_CONTEXT/commit_context_logic.py",
    "APPEND_CHANGE_RECORDS/append_change_records.py",
    "COMMIT_CHANGE_SET/commit_change_set.py",
)
CODEX_HOOK_MATCHER = r"^(apply_patch|functions\.apply_patch|Bash|exec_command|functions\.exec)$"
CODEX_HOOK_TIMEOUT_SECONDS = 120
MANAGED_GIT_HOOKS_PATH = ".caprmedio_runtime/hooks/git"
GIT_HOOK_NAMES = ("pre-commit", "commit-msg", "post-commit")
GIT_HOOK_MARKER = "# CAPRMEDIO managed Git Hook v1"
IDENTIFIER = re.compile(r"[A-Za-z][A-Za-z0-9._-]{0,127}\Z")
UUID_TEXT = re.compile(
    r"[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\Z",
    re.IGNORECASE,
)


class ToolError(RuntimeError):
    """A deterministic, machine-readable Tool failure."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.message = message


@dataclass(frozen=True)
class AdapterSpec:
    """One explicit host-adapter registration."""

    adapter_id: str
    application: str
    host_session_env: str
    fallback_session_env: str | None
    enabled: bool = True

    def __post_init__(self) -> None:
        _require_identifier(self.adapter_id, "adapter_id")
        _require_identifier(self.application, "application")
        _require_environment_name(self.host_session_env, "host_session_env")
        if self.fallback_session_env is not None:
            _require_environment_name(self.fallback_session_env, "fallback_session_env")


@dataclass(frozen=True)
class FileState:
    """A content-addressed eligible-file observation for the polling adapter."""

    path: str
    sha256: str
    identity: str
    line_count: int


@dataclass(frozen=True)
class PipelineCorrelation:
    """One exact downstream Journal transition that must not re-trigger."""

    correlation_id: str
    action_id: str
    event_id: str
    event_digest: str
    carrier: str
    line: int
    previous_carrier_digest: str
    appended_carrier_digest: str

    def __post_init__(self) -> None:
        if not re.fullmatch(r"[0-9a-f]{64}", self.correlation_id):
            raise ToolError("invalid-pipeline-correlation", "correlation_id must be a SHA-256 digest")
        _require_string(self.action_id, "action_id")
        _require_string(self.event_id, "event_id")
        if not re.fullmatch(r"[0-9a-f]{64}", self.event_digest):
            raise ToolError("invalid-pipeline-correlation", "event_digest must be a SHA-256 digest")
        _canonical_path(self.carrier, "carrier")
        if self.line < 1:
            raise ToolError("invalid-pipeline-correlation", "line must be a positive integer")
        for field, value in (
            ("previous_carrier_digest", self.previous_carrier_digest),
            ("appended_carrier_digest", self.appended_carrier_digest),
        ):
            if not re.fullmatch(r"[0-9a-f]{64}", value):
                raise ToolError("invalid-pipeline-correlation", f"{field} must be a SHA-256 digest")


def _require_identifier(value: object, field: str) -> str:
    if not isinstance(value, str) or not IDENTIFIER.fullmatch(value):
        raise ToolError("invalid-identifier", f"{field} must be an ASCII identifier")
    return value


def _require_environment_name(value: object, field: str) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[A-Z_][A-Z0-9_]*", value):
        raise ToolError("invalid-environment-name", f"{field} must be an uppercase environment name")
    return value


def _require_mapping(value: object, field: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ToolError("invalid-observation", f"{field} must be an object")
    return value


def _require_string(value: object, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise ToolError("invalid-observation", f"{field} must be a non-empty string")
    return value


def _canonical_timestamp(value: object) -> str:
    source = _require_string(value, "observed_at")
    normalized = source[:-1] + "+00:00" if source.endswith("Z") else source
    try:
        moment = dt.datetime.fromisoformat(normalized)
    except ValueError as error:
        raise ToolError("invalid-observation-time", "observed_at must be RFC 3339") from error
    if moment.tzinfo is None:
        raise ToolError("invalid-observation-time", "observed_at must include a timezone")
    return moment.astimezone(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canonical_path(value: object, field: str) -> str | None:
    if value is None:
        return None
    raw = _require_string(value, field)
    path = Path(raw)
    if path.is_absolute() or ".." in path.parts or raw.startswith("./"):
        raise ToolError("invalid-observed-path", f"{field} must be a normalized repository-relative path")
    rendered = path.as_posix()
    if rendered in {".", ""}:
        raise ToolError("invalid-observed-path", f"{field} must name a file")
    return rendered


def _canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _sha256(value: object) -> str:
    return hashlib.sha256(_canonical_json(value).encode("utf-8")).hexdigest()


def resolve_repository(path: Path) -> Path:
    """Resolve the repository top level without writing or initializing Git."""

    candidate = path.expanduser().resolve()
    completed = subprocess.run(
        ["git", "-C", str(candidate), "rev-parse", "--show-toplevel"],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise ToolError("repository-not-found", f"cannot resolve Git repository from {candidate}")
    return Path(completed.stdout.strip()).resolve()


def _repository_identity(repository: Path) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repository), "rev-parse", "--git-dir"],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise ToolError("repository-not-found", f"cannot resolve Git metadata for {repository}")
    git_directory = (repository / completed.stdout.strip()).resolve()
    return _sha256({"repository_root": repository.as_posix(), "git_directory": git_directory.as_posix()})


def _validate_uuid(value: object, field: str) -> str:
    raw = _require_string(value, field)
    if not UUID_TEXT.fullmatch(raw):
        raise ToolError("invalid-llm-session", f"{field} must be a UUID")
    return str(uuid.UUID(raw))


def resolve_codex_session(
    explicit_uuid: str | None = None,
    environment: Mapping[str, str] | None = None,
) -> dict[str, str]:
    """Resolve Codex provenance using explicit input, then native host variables."""

    if explicit_uuid is not None:
        return {"app": "codex", "uuid": _validate_uuid(explicit_uuid, "llm_session.uuid")}
    values = os.environ if environment is None else environment
    primary = values.get("CODEX_THREAD_ID")
    fallback = values.get("CODEX_SESSION_ID")
    if primary:
        return {"app": "codex", "uuid": _validate_uuid(primary, "CODEX_THREAD_ID")}
    if fallback:
        return {"app": "codex", "uuid": _validate_uuid(fallback, "CODEX_SESSION_ID")}
    raise ToolError("missing-llm-session", "Codex requires CODEX_THREAD_ID or CODEX_SESSION_ID")


def _resolve_session(
    observation: Mapping[str, Any],
    adapter: AdapterSpec,
    environment: Mapping[str, str],
) -> dict[str, str]:
    candidate = observation.get("llm_session")
    if candidate is not None:
        session = _require_mapping(candidate, "llm_session")
        app = _require_identifier(session.get("app"), "llm_session.app")
        if app != adapter.application:
            raise ToolError("llm-application-mismatch", "llm_session.app does not match the registered adapter")
        return {"app": app, "uuid": _validate_uuid(session.get("uuid"), "llm_session.uuid")}
    primary = environment.get(adapter.host_session_env)
    fallback = environment.get(adapter.fallback_session_env) if adapter.fallback_session_env else None
    if primary:
        return {"app": adapter.application, "uuid": _validate_uuid(primary, adapter.host_session_env)}
    if fallback:
        return {"app": adapter.application, "uuid": _validate_uuid(fallback, adapter.fallback_session_env or "session")}
    raise ToolError(
        "missing-llm-session",
        f"adapter {adapter.adapter_id} requires {adapter.host_session_env}"
        + (f" or {adapter.fallback_session_env}" if adapter.fallback_session_env else ""),
    )


def _is_pipeline_owned(observation: Mapping[str, Any]) -> bool:
    pipeline = observation.get("pipeline")
    if pipeline is None:
        return False
    details = _require_mapping(pipeline, "pipeline")
    if details.get("owned") is not True:
        return False
    action_id = details.get("action_id")
    if not isinstance(action_id, str) or not action_id:
        raise ToolError("invalid-pipeline-correlation", "pipeline-owned observation requires pipeline.action_id")
    kind = details.get("kind")
    if kind not in {"journal", "runtime-state"}:
        raise ToolError("invalid-pipeline-correlation", "pipeline.kind must be journal or runtime-state")
    return True


def _trigger_from_observation(
    observation: Mapping[str, Any],
    adapter: AdapterSpec,
    repository: Path,
    environment: Mapping[str, str],
) -> dict[str, object] | None:
    """Convert one host event to an immutable canonical trigger or suppress it."""

    adapter_id = _require_identifier(observation.get("adapter_id"), "adapter_id")
    if adapter_id != adapter.adapter_id:
        raise ToolError("unregistered-adapter", f"adapter {adapter_id} is not selected")
    if _is_pipeline_owned(observation):
        return None
    source_event_id = _require_string(observation.get("source_event_id"), "source_event_id")
    before_path = _canonical_path(observation.get("before_path"), "before_path")
    after_path = _canonical_path(observation.get("after_path"), "after_path")
    if before_path is None and after_path is None:
        raise ToolError("no-file-change", "observation must include before_path or after_path")
    observed_at = _canonical_timestamp(observation.get("observed_at"))
    llm_session = _resolve_session(observation, adapter, environment)
    repository_identity = _repository_identity(repository)
    identity_source = {
        "schema_version": TRIGGER_SCHEMA_VERSION,
        "adapter_id": adapter_id,
        "source_event_id": source_event_id,
        "repository_id": repository_identity,
    }
    return {
        "schema_version": TRIGGER_SCHEMA_VERSION,
        "trigger_id": _sha256(identity_source),
        "adapter": {"id": adapter_id},
        "source_event_id": source_event_id,
        "repository": {"root": repository.as_posix(), "identity": repository_identity},
        "observed_at": observed_at,
        "before_path": before_path,
        "after_path": after_path,
        "llm_session": llm_session,
    }


def emit_triggers(
    observations: Iterable[Mapping[str, Any]],
    *,
    adapter: AdapterSpec,
    repository: Path | str,
    environment: Mapping[str, str] | None = None,
) -> list[dict[str, object]]:
    """Coalesce accepted host observations without mutating any project state.

    Observations with equal adapter/source-event/repository identities must agree
    on the boundary and session provenance.  Their earliest observation time is
    retained so the result is independent of the host's noisy delivery order.
    """

    if not adapter.enabled:
        return []
    resolved_repository = resolve_repository(Path(repository))
    values = dict(os.environ if environment is None else environment)
    by_identity: dict[str, list[dict[str, object]]] = defaultdict(list)
    for raw in observations:
        trigger = _trigger_from_observation(_require_mapping(raw, "observation"), adapter, resolved_repository, values)
        if trigger is not None:
            by_identity[str(trigger["trigger_id"])].append(trigger)

    triggers: list[dict[str, object]] = []
    for trigger_id in sorted(by_identity):
        candidates = by_identity[trigger_id]
        baseline = candidates[0]
        comparable = ("adapter", "source_event_id", "repository", "before_path", "after_path", "llm_session")
        for candidate in candidates[1:]:
            if any(candidate[field] != baseline[field] for field in comparable):
                raise ToolError(
                    "ambiguous-source-event",
                    f"adapter source event cannot establish one boundary: {baseline['source_event_id']}",
                )
        selected = min(candidates, key=lambda candidate: str(candidate["observed_at"]))
        triggers.append(selected)
    return triggers


def _carrier_identity(relative: str, data: bytes) -> str:
    """Return a stable adapter-level carrier identity without graph traversal.

    The polling adapter needs only enough identity to pair the two path
    candidates of a move.  It does not inspect relations or classify the
    resulting action.  Invalid or non-Markdown carriers fall back to their
    address and are never guessed into a move.
    """

    path = Path(relative)
    if path.suffix != ".md":
        return f"path:{relative}"
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return f"path:{relative}"
    if text.startswith("---\n") and (boundary := text.find("\n---\n", 4)) >= 0:
        frontmatter = text[4:boundary]
        matches = re.findall(r"(?m)^atom_id:\s*['\"]?([^'\"\s]+)['\"]?\s*$", frontmatter)
        if len(matches) == 1:
            return f"atom:{matches[0]}"
    match = re.match(r"(CA-[RMCAPIDEO]-[0-9]+)(?:-|$)", path.name)
    if match:
        return f"atom:{match.group(1)}"
    if "--" in path.name:
        return f"carrier:{path.name.split('--', 1)[0]}"
    return f"path:{relative}"


def scan_governed_files(repository: Path | str) -> dict[str, FileState]:
    """Read the eligible source frontier for the native Codex polling adapter.

    The native adapter treats `.caprmedio` carriers as governed source.  It
    observes Journal carriers too, because a path alone must not determine
    recursion suppression; `PipelineCorrelation` is the authoritative
    suppression signal.  Runtime state is outside governed source and is not
    scanned.
    """

    resolved_repository = resolve_repository(Path(repository))
    control_root = resolved_repository / ".caprmedio"
    if not control_root.is_dir():
        raise ToolError("governed-source-not-found", f"{control_root} does not exist")
    result: dict[str, FileState] = {}
    for path in sorted(control_root.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(resolved_repository).as_posix()
        data = path.read_bytes()
        result[relative] = FileState(
            path=relative,
            sha256=hashlib.sha256(data).hexdigest(),
            identity=_carrier_identity(relative, data),
            line_count=len(data.splitlines()),
        )
    return result


def _watch_source_event_id(
    *,
    adapter_id: str,
    repository: Path,
    before_path: str | None,
    after_path: str | None,
    before_digest: str | None,
    after_digest: str | None,
) -> str:
    return "watch-" + _sha256(
        {
            "schema_version": 1,
            "adapter_id": adapter_id,
            "repository_id": _repository_identity(repository),
            "before_path": before_path,
            "after_path": after_path,
            "before_digest": before_digest,
            "after_digest": after_digest,
        }
    )


def _correlation_for(
    before: FileState | None,
    after: FileState | None,
    correlations: Mapping[str, Sequence[PipelineCorrelation]],
) -> PipelineCorrelation | None:
    if after is None:
        return None
    empty_digest = hashlib.sha256(b"").hexdigest()
    previous_digest = before.sha256 if before is not None else empty_digest
    matched = {
        correlation
        for correlation in correlations.get(after.path, ())
        if correlation.previous_carrier_digest == previous_digest
        and correlation.appended_carrier_digest == after.sha256
        and correlation.line == after.line_count
    }
    if not matched:
        return None
    if len(matched) != 1:
        actions = {correlation.action_id for correlation in matched}
        if len(actions) != 1:
            raise ToolError("ambiguous-pipeline-correlation", "one file event resolves to multiple pipeline actions")
        return sorted(matched, key=lambda item: item.correlation_id)[0]
    return next(iter(matched))


def _watch_observation(
    *,
    adapter_id: str,
    repository: Path,
    observed_at: str,
    before: FileState | None,
    after: FileState | None,
    correlations: Mapping[str, Sequence[PipelineCorrelation]],
) -> dict[str, object]:
    before_path = before.path if before is not None else None
    after_path = after.path if after is not None else None
    observation: dict[str, object] = {
        "adapter_id": adapter_id,
        "source_event_id": _watch_source_event_id(
            adapter_id=adapter_id,
            repository=repository,
            before_path=before_path,
            after_path=after_path,
            before_digest=before.sha256 if before is not None else None,
            after_digest=after.sha256 if after is not None else None,
        ),
        "observed_at": observed_at,
        "before_path": before_path,
        "after_path": after_path,
    }
    correlation = _correlation_for(before, after, correlations)
    if correlation is not None:
        observation["pipeline"] = {
            "owned": True,
            "action_id": correlation.action_id,
            "kind": "journal",
        }
    return observation


def detect_watch_observations(
    previous: Mapping[str, FileState],
    current: Mapping[str, FileState],
    *,
    adapter_id: str,
    repository: Path | str,
    observed_at: str,
    correlations: Mapping[str, Sequence[PipelineCorrelation]] | None = None,
) -> list[dict[str, object]]:
    """Derive deterministic ADD, REMOVE, MOVE, and UPDATE candidates from scans."""

    resolved_repository = resolve_repository(Path(repository))
    _require_identifier(adapter_id, "adapter_id")
    canonical_time = _canonical_timestamp(observed_at)
    active_correlations = {} if correlations is None else dict(correlations)
    removed = {path: previous[path] for path in sorted(set(previous) - set(current))}
    added = {path: current[path] for path in sorted(set(current) - set(previous))}
    observations: list[dict[str, object]] = []

    # A unique stable carrier identity establishes one old/new path boundary,
    # including when the carrier was edited during relocation.  This remains
    # adapter-level event correlation; COMMIT_CONTEXT owns MOVE/UPDATE
    # classification and all graph traversal.
    removed_by_identity: dict[str, list[FileState]] = defaultdict(list)
    added_by_identity: dict[str, list[FileState]] = defaultdict(list)
    for state in removed.values():
        removed_by_identity[state.identity].append(state)
    for state in added.values():
        added_by_identity[state.identity].append(state)
    for identity in sorted(set(removed_by_identity) & set(added_by_identity)):
        before_states = removed_by_identity[identity]
        after_states = added_by_identity[identity]
        if len(before_states) == len(after_states) == 1 and not identity.startswith("path:"):
            before = before_states[0]
            after = after_states[0]
            observations.append(
                _watch_observation(
                    adapter_id=adapter_id,
                    repository=resolved_repository,
                    observed_at=canonical_time,
                    before=before,
                    after=after,
                    correlations=active_correlations,
                )
            )
            removed.pop(before.path)
            added.pop(after.path)

    # Equal content safely pairs remaining opaque carriers without assigning
    # semantic meaning to the boundary.
    removed_by_digest: dict[str, list[FileState]] = defaultdict(list)
    added_by_digest: dict[str, list[FileState]] = defaultdict(list)
    for state in removed.values():
        removed_by_digest[state.sha256].append(state)
    for state in added.values():
        added_by_digest[state.sha256].append(state)
    for digest in sorted(set(removed_by_digest) & set(added_by_digest)):
        before_states = removed_by_digest[digest]
        after_states = added_by_digest[digest]
        if len(before_states) == len(after_states) == 1:
            before = before_states[0]
            after = after_states[0]
            observations.append(
                _watch_observation(
                    adapter_id=adapter_id,
                    repository=resolved_repository,
                    observed_at=canonical_time,
                    before=before,
                    after=after,
                    correlations=active_correlations,
                )
            )
            removed.pop(before.path)
            added.pop(after.path)

    for path in sorted(removed):
        observations.append(
            _watch_observation(
                adapter_id=adapter_id,
                repository=resolved_repository,
                observed_at=canonical_time,
                before=removed[path],
                after=None,
                correlations=active_correlations,
            )
        )
    for path in sorted(added):
        observations.append(
            _watch_observation(
                adapter_id=adapter_id,
                repository=resolved_repository,
                observed_at=canonical_time,
                before=None,
                after=added[path],
                correlations=active_correlations,
            )
        )
    for path in sorted(set(previous) & set(current)):
        before = previous[path]
        after = current[path]
        if before.sha256 != after.sha256:
            observations.append(
                _watch_observation(
                    adapter_id=adapter_id,
                    repository=resolved_repository,
                    observed_at=canonical_time,
                    before=before,
                    after=after,
                    correlations=active_correlations,
                )
            )
    return sorted(observations, key=lambda item: str(item["source_event_id"]))


def _read_pipeline_correlations(path: Path) -> dict[str, tuple[PipelineCorrelation, ...]]:
    """Replay the exact active Journal-transition suppression frontier."""

    if not path.exists():
        return {}
    registrations: dict[str, PipelineCorrelation] = {}
    active: dict[str, bool] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line:
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ToolError("invalid-pipeline-correlation", f"{path}:{line_number}: invalid JSON") from error
        record = _require_mapping(value, "pipeline correlation")
        if record.get("schema_version") != 1:
            raise ToolError("invalid-pipeline-correlation", f"{path}:{line_number}: unsupported schema_version")
        correlation_id = _require_string(record.get("correlation_id"), "correlation_id")
        event = record.get("event")
        if event == "retired":
            if correlation_id not in registrations:
                raise ToolError("invalid-pipeline-correlation", f"{path}:{line_number}: retirement precedes registration")
            if record.get("action_id") != registrations[correlation_id].action_id:
                raise ToolError("invalid-pipeline-correlation", f"{path}:{line_number}: retirement action differs")
            active[correlation_id] = False
            continue
        if event != "registered":
            raise ToolError("invalid-pipeline-correlation", f"{path}:{line_number}: event must be registered or retired")
        transition = _require_mapping(record.get("transition"), "transition")
        correlation = PipelineCorrelation(
            correlation_id=correlation_id,
            action_id=_require_string(record.get("action_id"), "action_id"),
            event_id=_require_string(transition.get("event_id"), "event_id"),
            event_digest=_require_string(transition.get("event_digest"), "event_digest"),
            carrier=_canonical_path(transition.get("carrier"), "carrier") or "",
            line=transition.get("line") if isinstance(transition.get("line"), int) else 0,
            previous_carrier_digest=_require_string(
                transition.get("previous_carrier_digest"), "previous_carrier_digest"
            ),
            appended_carrier_digest=_require_string(
                transition.get("appended_carrier_digest"), "appended_carrier_digest"
            ),
        )
        expected_id = _sha256(
            {
                "action_id": correlation.action_id,
                "transition": {
                    "event_id": correlation.event_id,
                    "event_digest": correlation.event_digest,
                    "carrier": correlation.carrier,
                    "line": correlation.line,
                    "previous_carrier_digest": correlation.previous_carrier_digest,
                    "appended_carrier_digest": correlation.appended_carrier_digest,
                },
            }
        )
        if expected_id != correlation_id:
            raise ToolError("invalid-pipeline-correlation", f"{path}:{line_number}: correlation_id digest differs")
        previous = registrations.get(correlation_id)
        if previous is not None and previous != correlation:
            raise ToolError("invalid-pipeline-correlation", f"{path}:{line_number}: correlation identity collision")
        registrations[correlation_id] = correlation
        active[correlation_id] = True
    grouped: dict[str, list[PipelineCorrelation]] = defaultdict(list)
    for correlation_id, correlation in registrations.items():
        if active.get(correlation_id):
            grouped[correlation.carrier].append(correlation)
    return {
        carrier: tuple(sorted(values, key=lambda item: item.correlation_id))
        for carrier, values in grouped.items()
    }


def watch_triggers(
    *,
    repository: Path | str,
    adapter: AdapterSpec,
    environment: Mapping[str, str] | None = None,
    poll_interval: float = 1.0,
    maximum_polls: int | None = None,
    pipeline_correlation_path: Path | None = None,
    stop: threading.Event | None = None,
) -> Iterable[list[dict[str, object]]]:
    """Yield native Codex polling-adapter handoffs until stopped.

    The caller owns downstream execution.  Each yielded list is already
    deduplicated and may be empty only when no source change was observed.
    """

    if adapter.application != "codex":
        raise ToolError("unsupported-native-adapter", "watch supports only the native Codex adapter")
    if poll_interval <= 0:
        raise ToolError("invalid-poll-interval", "poll_interval must be greater than zero")
    if maximum_polls is not None and maximum_polls < 0:
        raise ToolError("invalid-maximum-polls", "maximum_polls must not be negative")
    resolved_repository = resolve_repository(Path(repository))
    correlation_path = pipeline_correlation_path or _runtime_directory(resolved_repository) / PIPELINE_CORRELATIONS_NAME
    previous = scan_governed_files(resolved_repository)
    polls = 0
    while maximum_polls is None or polls < maximum_polls:
        if stop is not None and stop.is_set():
            return
        time.sleep(poll_interval)
        current = scan_governed_files(resolved_repository)
        correlations = _read_pipeline_correlations(correlation_path)
        observations = detect_watch_observations(
            previous,
            current,
            adapter_id=adapter.adapter_id,
            repository=resolved_repository,
            observed_at=dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            correlations=correlations,
        )
        previous = current
        polls += 1
        if observations:
            yield emit_triggers(observations, adapter=adapter, repository=resolved_repository, environment=environment)


def _runtime_directory(repository: Path) -> Path:
    return repository / RUNTIME_DIRECTORY


def _runtime_root(repository: Path) -> Path:
    return repository / ".caprmedio_runtime"


def _installed_package_root(repository: Path) -> Path:
    return _runtime_root(repository) / "installed" / "tools" / "auto_commit"


def _runtime_manifest_path(repository: Path) -> Path:
    return _installed_package_root(repository) / "current.toml"


def _registry_path(repository: Path) -> Path:
    return _runtime_directory(repository) / REGISTRY_NAME


def _quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _read_registry(repository: Path) -> dict[str, AdapterSpec]:
    path = _registry_path(repository)
    if not path.exists():
        return {}
    try:
        document = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as error:
        raise ToolError("invalid-adapter-registry", f"{path}: invalid TOML") from error
    if document.get("schema_version") != TOOL_SCHEMA_VERSION:
        raise ToolError("invalid-adapter-registry", "adapter registry schema_version is unsupported")
    adapters = document.get("adapters")
    if not isinstance(adapters, Mapping):
        raise ToolError("invalid-adapter-registry", "adapter registry requires [adapters]")
    result: dict[str, AdapterSpec] = {}
    for adapter_id, values in adapters.items():
        if not isinstance(values, Mapping):
            raise ToolError("invalid-adapter-registry", f"adapter {adapter_id} must be a table")
        result[str(adapter_id)] = AdapterSpec(
            adapter_id=str(adapter_id),
            application=_require_string(values.get("application"), f"adapter {adapter_id}.application"),
            host_session_env=_require_string(values.get("host_session_env"), f"adapter {adapter_id}.host_session_env"),
            fallback_session_env=(
                _require_string(values["fallback_session_env"], f"adapter {adapter_id}.fallback_session_env")
                if values.get("fallback_session_env") is not None
                else None
            ),
            enabled=values.get("enabled") is True,
        )
    return result


def _render_registry(adapters: Mapping[str, AdapterSpec]) -> str:
    lines = [f"schema_version = {TOOL_SCHEMA_VERSION}", ""]
    for adapter_id in sorted(adapters):
        adapter = adapters[adapter_id]
        lines.extend(
            [
                f'[adapters.{_quoted(adapter.adapter_id)}]',
                f"application = {_quoted(adapter.application)}",
                f"host_session_env = {_quoted(adapter.host_session_env)}",
            ]
        )
        if adapter.fallback_session_env is not None:
            lines.append(f"fallback_session_env = {_quoted(adapter.fallback_session_env)}")
        lines.extend([f"enabled = {'true' if adapter.enabled else 'false'}", ""])
    return "\n".join(lines)


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def _package_inventory(source_root: Path = PACKAGE_ROOT) -> tuple[list[dict[str, str]], str]:
    rows: list[dict[str, str]] = []
    for relative in PACKAGE_FILES:
        path = source_root / relative
        if not path.is_file() or path.is_symlink():
            raise ToolError("runtime-source-incomplete", f"runtime package source is missing {relative}")
        rows.append({"path": relative, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    release = _sha256({"schema_version": 1, "package": PACKAGE_NAME, "files": rows})
    return rows, release


def _render_package_manifest(release: str, rows: Sequence[Mapping[str, str]]) -> str:
    lines = ["schema_version = 1", f"package = {_quoted(PACKAGE_NAME)}", f"release = {_quoted(release)}", ""]
    for row in rows:
        lines.extend(
            [
                "[[files]]",
                f"path = {_quoted(row['path'])}",
                f"sha256 = {_quoted(row['sha256'])}",
                "",
            ]
        )
    return "\n".join(lines)


def runtime_package_status(repository: Path | str) -> dict[str, object]:
    root = resolve_repository(Path(repository))
    current_path = _runtime_manifest_path(root)
    if not current_path.is_file():
        return {
            "installed": False,
            "package_root": _installed_package_root(root).relative_to(root).as_posix(),
        }
    try:
        current = tomllib.loads(current_path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as error:
        raise ToolError("runtime-manifest-invalid", f"{current_path}: invalid TOML") from error
    release = current.get("release")
    entrypoint = current.get("entrypoint")
    if current.get("schema_version") != 1 or current.get("package") != PACKAGE_NAME:
        raise ToolError("runtime-manifest-invalid", "installed runtime manifest identity is invalid")
    if not isinstance(release, str) or not re.fullmatch(r"[0-9a-f]{64}", release):
        raise ToolError("runtime-manifest-invalid", "installed runtime release is invalid")
    if not isinstance(entrypoint, str):
        raise ToolError("runtime-manifest-invalid", "installed runtime entrypoint is missing")
    release_root = _installed_package_root(root) / "releases" / release
    manifest_path = release_root / "manifest.toml"
    try:
        manifest = tomllib.loads(manifest_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, tomllib.TOMLDecodeError) as error:
        raise ToolError("runtime-release-invalid", "installed runtime release manifest is missing or invalid") from error
    if manifest.get("schema_version") != 1 or manifest.get("package") != PACKAGE_NAME or manifest.get("release") != release:
        raise ToolError("runtime-release-invalid", "installed runtime release identity differs from current.toml")
    rows = manifest.get("files")
    if not isinstance(rows, list):
        raise ToolError("runtime-release-invalid", "installed runtime release has no file inventory")
    checked: list[dict[str, str]] = []
    for raw in rows:
        if not isinstance(raw, Mapping):
            raise ToolError("runtime-release-invalid", "installed runtime file row is invalid")
        relative = raw.get("path")
        expected = raw.get("sha256")
        if not isinstance(relative, str) or Path(relative).is_absolute() or ".." in Path(relative).parts:
            raise ToolError("runtime-release-invalid", "installed runtime file path is unsafe")
        path = release_root / relative
        if not isinstance(expected, str) or not path.is_file() or path.is_symlink():
            raise ToolError("runtime-release-invalid", f"installed runtime file is missing: {relative}")
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            raise ToolError("runtime-release-invalid", f"installed runtime file digest differs: {relative}")
        checked.append({"path": relative, "sha256": actual})
    actual_release = _sha256({"schema_version": 1, "package": PACKAGE_NAME, "files": checked})
    if actual_release != release:
        raise ToolError("runtime-release-invalid", "installed runtime release digest differs")
    entrypoint_path = release_root / entrypoint
    if not entrypoint_path.is_file():
        raise ToolError("runtime-release-invalid", "installed runtime entrypoint does not exist")
    return {
        "installed": True,
        "release": release,
        "package_root": release_root.relative_to(root).as_posix(),
        "entrypoint": entrypoint_path.relative_to(root).as_posix(),
        "file_count": len(checked),
        "verified": True,
    }


def install_runtime_package(repository: Path | str, *, apply: bool) -> dict[str, object]:
    root = resolve_repository(Path(repository))
    rows, release = _package_inventory()
    package_root = _installed_package_root(root)
    release_root = package_root / "releases" / release
    current = {
        "schema_version": 1,
        "package": PACKAGE_NAME,
        "release": release,
        "entrypoint": "COMMIT_TRIGGER/commit_trigger.py",
    }
    result = {
        "installed": apply,
        "release": release,
        "package_root": release_root.relative_to(root).as_posix(),
        "entrypoint": (release_root / current["entrypoint"]).relative_to(root).as_posix(),
        "file_count": len(rows),
        "planned_effect": "install-or-verify-content-addressed-release",
    }
    if not apply:
        return result
    for relative in (
        "installed/tools/auto_commit/releases",
        "state/commit_trigger/hook_snapshots",
        "state/append_change_records",
        "state/commit_change_set",
        "state/work_journal",
        "cache/python",
        "hooks/codex",
        "hooks/git",
        "logs/commit_trigger",
        "logs/git_hooks",
        "history/backups",
        "history/migrations",
    ):
        (_runtime_root(root) / relative).mkdir(parents=True, exist_ok=True)
    for row in rows:
        source = PACKAGE_ROOT / row["path"]
        target = release_root / row["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and hashlib.sha256(target.read_bytes()).hexdigest() != row["sha256"]:
            raise ToolError("runtime-release-collision", f"release target already differs: {row['path']}")
        if not target.exists():
            shutil.copyfile(source, target)
            target.chmod(source.stat().st_mode & 0o777)
    _atomic_write(release_root / "manifest.toml", _render_package_manifest(release, rows))
    _atomic_write(
        package_root / "current.toml",
        "\n".join(
            [
                "schema_version = 1",
                f"package = {_quoted(PACKAGE_NAME)}",
                f"release = {_quoted(release)}",
                f"entrypoint = {_quoted(current['entrypoint'])}",
                "",
            ]
        ),
    )
    return runtime_package_status(root)


def _managed_hook_command(repository: Path, phase: str, adapter_id: str) -> str:
    status = runtime_package_status(repository)
    if status.get("installed") is not True:
        raise ToolError("runtime-not-installed", "install the project-local runtime before the Codex adapter")
    entrypoint = repository / str(status["entrypoint"])
    return " ".join(
        shlex.quote(value)
        for value in (
            sys.executable,
            str(entrypoint),
            "--repository",
            str(repository),
            "codex-hook",
            phase,
            "--adapter-id",
            adapter_id,
        )
    )


def _managed_hook_group(repository: Path, phase: str, adapter_id: str) -> dict[str, object]:
    return {
        "matcher": CODEX_HOOK_MATCHER,
        "hooks": [
            {
                "type": "command",
                "command": _managed_hook_command(repository, phase, adapter_id),
                "timeout": CODEX_HOOK_TIMEOUT_SECONDS,
                "statusMessage": f"CAPRMEDIO auto-commit {phase}",
            }
        ],
    }


def _is_managed_hook_group(value: object) -> bool:
    if not isinstance(value, Mapping):
        return False
    hooks = value.get("hooks")
    if not isinstance(hooks, list):
        return False
    return any(
        isinstance(hook, Mapping)
        and isinstance(hook.get("command"), str)
        and ".caprmedio_runtime/installed/tools/auto_commit/" in str(hook["command"])
        and " codex-hook " in str(hook["command"])
        for hook in hooks
    )


def _hook_document(repository: Path, adapter_id: str, existing: Mapping[str, Any] | None = None) -> dict[str, Any]:
    document = dict(existing or {})
    document.setdefault("description", "Project-local Codex hooks.")
    raw_hooks = document.get("hooks")
    hooks = dict(raw_hooks) if isinstance(raw_hooks, Mapping) else {}
    for event, phase in (("PreToolUse", "pre"), ("PostToolUse", "post")):
        groups = hooks.get(event)
        retained = [group for group in groups if not _is_managed_hook_group(group)] if isinstance(groups, list) else []
        hooks[event] = [*retained, _managed_hook_group(repository, phase, adapter_id)]
    document["hooks"] = hooks
    return document


def _read_hook_document(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as error:
        raise ToolError("codex-hook-config-invalid", f"{path}: invalid JSON") from error
    if not isinstance(value, dict):
        raise ToolError("codex-hook-config-invalid", f"{path}: root must be an object")
    return value


def install_codex_hooks(repository: Path, adapter_id: str) -> dict[str, object]:
    runtime_config = _runtime_root(repository) / "hooks" / "codex" / "hooks.json"
    project_config = repository / ".codex" / "hooks.json"
    managed = _hook_document(repository, adapter_id)
    _atomic_write(runtime_config, json.dumps(managed, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    project_config.parent.mkdir(parents=True, exist_ok=True)
    if not project_config.exists() and not project_config.is_symlink():
        relative_target = os.path.relpath(runtime_config, project_config.parent)
        project_config.symlink_to(relative_target)
        carrier = "runtime-symlink"
    elif project_config.is_symlink() and project_config.resolve() == runtime_config.resolve():
        carrier = "runtime-symlink"
    else:
        existing = _read_hook_document(project_config)
        merged = _hook_document(repository, adapter_id, existing)
        _atomic_write(project_config, json.dumps(merged, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
        carrier = "merged-project-config"
    return {
        "registered": True,
        "carrier": project_config.relative_to(repository).as_posix(),
        "carrier_kind": carrier,
        "runtime_config": runtime_config.relative_to(repository).as_posix(),
    }


def uninstall_codex_hooks(repository: Path) -> dict[str, object]:
    runtime_config = _runtime_root(repository) / "hooks" / "codex" / "hooks.json"
    project_config = repository / ".codex" / "hooks.json"
    changed = False
    if project_config.is_symlink() and project_config.resolve() == runtime_config.resolve():
        project_config.unlink()
        changed = True
    elif project_config.is_file():
        document = _read_hook_document(project_config)
        raw_hooks = document.get("hooks")
        hooks = dict(raw_hooks) if isinstance(raw_hooks, Mapping) else {}
        for event in ("PreToolUse", "PostToolUse"):
            groups = hooks.get(event)
            if isinstance(groups, list):
                retained = [group for group in groups if not _is_managed_hook_group(group)]
                changed = changed or len(retained) != len(groups)
                if retained:
                    hooks[event] = retained
                else:
                    hooks.pop(event, None)
        document["hooks"] = hooks
        _atomic_write(project_config, json.dumps(document, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    try:
        runtime_config.unlink()
    except FileNotFoundError:
        pass
    return {"registered": False, "changed": changed, "carrier": project_config.relative_to(repository).as_posix()}


def _local_git_hooks_path(repository: Path) -> str | None:
    completed = subprocess.run(
        ["git", "-C", str(repository), "config", "--local", "--get", "core.hooksPath"],
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode == 1:
        return None
    if completed.returncode != 0:
        detail = (completed.stderr or completed.stdout).strip()
        raise ToolError("git-config-failed", detail or "cannot read repository-local core.hooksPath")
    return completed.stdout.strip()


def _managed_git_hook_script(repository: Path, hook_name: str) -> str:
    if hook_name not in GIT_HOOK_NAMES:
        raise ToolError("git-hook-invalid", f"unsupported Git Hook: {hook_name}")
    status = runtime_package_status(repository)
    if status.get("installed") is not True:
        raise ToolError("runtime-not-installed", "install the project-local runtime before Git Hooks")
    tool = Path(str(status["package_root"])) / "COMMIT_CHANGE_SET" / "commit_change_set.py"
    return "\n".join(
        [
            "#!/bin/sh",
            GIT_HOOK_MARKER,
            "set -eu",
            'repository=$(git rev-parse --show-toplevel)',
            'git_directory=$(git rev-parse --absolute-git-dir)',
            f'legacy="$git_directory/hooks/{hook_name}"',
            'if [ -x "$legacy" ]; then',
            '  "$legacy" "$@"',
            "fi",
            "exec "
            + " ".join(
                [
                    shlex.quote(sys.executable),
                    "-I",
                    "-B",
                    f'"$repository/{tool.as_posix()}"',
                    "--repository",
                    '"$repository"',
                    "git-hook",
                    hook_name,
                    '"$@"',
                ]
            ),
            "",
        ]
    )


def install_git_hooks(repository: Path) -> dict[str, object]:
    existing = _local_git_hooks_path(repository)
    if existing not in {None, MANAGED_GIT_HOOKS_PATH}:
        raise ToolError(
            "git-hooks-path-conflict",
            f"repository already uses a different local core.hooksPath: {existing}",
        )
    directory = repository / MANAGED_GIT_HOOKS_PATH
    directory.mkdir(parents=True, exist_ok=True)
    carriers: list[str] = []
    for hook_name in GIT_HOOK_NAMES:
        carrier = directory / hook_name
        _atomic_write(carrier, _managed_git_hook_script(repository, hook_name))
        carrier.chmod(0o755)
        carriers.append(carrier.relative_to(repository).as_posix())
    completed = subprocess.run(
        ["git", "-C", str(repository), "config", "--local", "core.hooksPath", MANAGED_GIT_HOOKS_PATH],
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        detail = (completed.stderr or completed.stdout).strip()
        raise ToolError("git-config-failed", detail or "cannot register runtime-owned Git Hooks")
    return {
        "registered": True,
        "hooks_path": MANAGED_GIT_HOOKS_PATH,
        "carriers": carriers,
        "preserved_default_hooks": True,
    }


def uninstall_git_hooks(repository: Path) -> dict[str, object]:
    existing = _local_git_hooks_path(repository)
    changed = False
    if existing == MANAGED_GIT_HOOKS_PATH:
        completed = subprocess.run(
            ["git", "-C", str(repository), "config", "--local", "--unset-all", "core.hooksPath"],
            capture_output=True,
            text=True,
            check=False,
        )
        if completed.returncode not in {0, 5}:
            detail = (completed.stderr or completed.stdout).strip()
            raise ToolError("git-config-failed", detail or "cannot remove runtime-owned Git Hook registration")
        changed = True
    directory = repository / MANAGED_GIT_HOOKS_PATH
    removed: list[str] = []
    for hook_name in GIT_HOOK_NAMES:
        carrier = directory / hook_name
        try:
            first_lines = carrier.read_text(encoding="utf-8").splitlines()[:2]
        except FileNotFoundError:
            continue
        if GIT_HOOK_MARKER not in first_lines:
            raise ToolError("git-hook-carrier-conflict", f"refusing to remove unrecognized runtime Hook carrier: {carrier}")
        carrier.unlink()
        removed.append(carrier.relative_to(repository).as_posix())
    return {
        "registered": False,
        "changed": changed or bool(removed),
        "hooks_path": MANAGED_GIT_HOOKS_PATH,
        "removed": removed,
        "preserved_default_hooks": True,
    }


def _write_registry(repository: Path, adapters: Mapping[str, AdapterSpec]) -> None:
    path = _registry_path(repository)
    if not adapters:
        try:
            path.unlink()
        except FileNotFoundError:
            return
        return
    _atomic_write(path, _render_registry(adapters))


def adapter_operation(
    repository: Path | str,
    operation: str,
    *,
    adapter: AdapterSpec | None = None,
    adapter_id: str | None = None,
    apply: bool = False,
    manage_host_hooks: bool = False,
) -> dict[str, object]:
    """Inspect or explicitly change reconstructible adapter registration state."""

    resolved_repository = resolve_repository(Path(repository))
    registered = _read_registry(resolved_repository)
    if operation == "status":
        project_hook = resolved_repository / ".codex" / "hooks.json"
        git_hooks_path = _local_git_hooks_path(resolved_repository)
        git_hook_carriers = [resolved_repository / MANAGED_GIT_HOOKS_PATH / name for name in GIT_HOOK_NAMES]
        return {
            "repository": resolved_repository.as_posix(),
            "registry": _registry_path(resolved_repository).relative_to(resolved_repository).as_posix(),
            "adapters": [
                {
                    "adapter_id": entry.adapter_id,
                    "application": entry.application,
                    "host_session_env": entry.host_session_env,
                    "fallback_session_env": entry.fallback_session_env,
                    "enabled": entry.enabled,
                }
                for entry in (registered[key] for key in sorted(registered))
            ],
            "host_hook_registered": project_hook.exists() or project_hook.is_symlink(),
            "host_hook_carrier": project_hook.relative_to(resolved_repository).as_posix(),
            "git_hooks_registered": git_hooks_path == MANAGED_GIT_HOOKS_PATH and all(path.is_file() and os.access(path, os.X_OK) for path in git_hook_carriers),
            "git_hooks_path": git_hooks_path,
            "git_hook_carriers": [path.relative_to(resolved_repository).as_posix() for path in git_hook_carriers],
            "runtime_package": runtime_package_status(resolved_repository),
        }

    if operation == "install":
        if adapter is None:
            raise ToolError("missing-adapter", "install requires an adapter specification")
        previous = registered.get(adapter.adapter_id)
        if previous is not None and previous != adapter:
            raise ToolError("adapter-already-registered", f"adapter {adapter.adapter_id} is already registered differently")
        proposed = dict(registered)
        proposed[adapter.adapter_id] = adapter
        effect = "already-installed" if previous is not None else "register-adapter"
    else:
        selected_id = _require_identifier(adapter_id, "adapter_id")
        previous = registered.get(selected_id)
        if previous is None:
            if operation == "uninstall":
                return {"repository": resolved_repository.as_posix(), "effect": "already-uninstalled", "adapter_id": selected_id}
            raise ToolError("adapter-not-registered", f"adapter {selected_id} is not registered")
        proposed = dict(registered)
        if operation == "enable":
            proposed[selected_id] = AdapterSpec(
                selected_id, previous.application, previous.host_session_env, previous.fallback_session_env, True
            )
            effect = "enable-adapter"
        elif operation == "disable":
            proposed[selected_id] = AdapterSpec(
                selected_id, previous.application, previous.host_session_env, previous.fallback_session_env, False
            )
            effect = "disable-adapter"
        elif operation == "uninstall":
            del proposed[selected_id]
            effect = "unregister-adapter"
        else:
            raise ToolError("unknown-operation", f"unknown adapter operation: {operation}")

    hook_result: dict[str, object] | None = None
    if apply and manage_host_hooks and operation == "install":
        assert adapter is not None
        hook_result = {
            "codex": install_codex_hooks(resolved_repository, adapter.adapter_id),
            "git": install_git_hooks(resolved_repository),
        }
    if apply:
        _write_registry(resolved_repository, proposed)
    if apply and manage_host_hooks and operation == "uninstall" and not proposed:
        hook_result = {
            "codex": uninstall_codex_hooks(resolved_repository),
            "git": uninstall_git_hooks(resolved_repository),
        }
    return {
        "repository": resolved_repository.as_posix(),
        "effect": effect,
        "adapter_id": adapter.adapter_id if adapter is not None else adapter_id,
        "apply": apply,
        "host_hooks": hook_result,
    }


def emit_from_registered_adapter(
    observations: Iterable[Mapping[str, Any]],
    *,
    repository: Path | str,
    adapter_id: str,
    environment: Mapping[str, str] | None = None,
) -> list[dict[str, object]]:
    """Emit from one enabled registered adapter; disabled adapters emit nothing."""

    resolved_repository = resolve_repository(Path(repository))
    selected = _read_registry(resolved_repository).get(_require_identifier(adapter_id, "adapter_id"))
    if selected is None:
        return []
    return emit_triggers(observations, adapter=selected, repository=resolved_repository, environment=environment)


def _hook_payload() -> dict[str, Any]:
    raw = sys.stdin.buffer.read(2 * 1024 * 1024 + 1)
    if len(raw) > 2 * 1024 * 1024:
        raise ToolError("codex-hook-input-too-large", "Codex hook input exceeds 2 MiB")
    try:
        value = json.loads(raw or b"{}")
    except json.JSONDecodeError as error:
        raise ToolError("codex-hook-input-invalid", "Codex hook input is not valid JSON") from error
    return dict(_require_mapping(value, "Codex hook input"))


def _hook_snapshot_path(repository: Path, payload: Mapping[str, Any]) -> Path:
    session_id = _require_string(payload.get("session_id"), "session_id")
    tool_use_id = _require_string(payload.get("tool_use_id"), "tool_use_id")
    key = _sha256({"schema_version": 1, "session_id": session_id, "tool_use_id": tool_use_id})
    return _runtime_directory(repository) / "hook_snapshots" / f"{key}.json"


def _frontier_document(frontier: Mapping[str, FileState]) -> dict[str, dict[str, object]]:
    return {
        path: {
            "path": state.path,
            "sha256": state.sha256,
            "identity": state.identity,
            "line_count": state.line_count,
        }
        for path, state in sorted(frontier.items())
    }


def _frontier_from_document(value: object) -> dict[str, FileState]:
    document = _require_mapping(value, "frontier")
    result: dict[str, FileState] = {}
    for path, raw in document.items():
        state = _require_mapping(raw, f"frontier.{path}")
        if state.get("path") != path:
            raise ToolError("codex-hook-snapshot-invalid", "frontier path identity differs")
        sha256 = _require_string(state.get("sha256"), f"frontier.{path}.sha256")
        identity = _require_string(state.get("identity"), f"frontier.{path}.identity")
        line_count = state.get("line_count")
        if not re.fullmatch(r"[0-9a-f]{64}", sha256) or not isinstance(line_count, int) or line_count < 0:
            raise ToolError("codex-hook-snapshot-invalid", f"frontier state is invalid: {path}")
        result[str(path)] = FileState(str(path), sha256, identity, line_count)
    return result


def _hook_log(repository: Path, value: Mapping[str, Any]) -> None:
    path = _runtime_root(repository) / "logs" / "commit_trigger" / f"{dt.date.today().isoformat()}.ndjson"
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor = os.open(path, os.O_APPEND | os.O_CREAT | os.O_WRONLY, 0o600)
    try:
        payload = (_canonical_json(value) + "\n").encode("utf-8")
        offset = 0
        while offset < len(payload):
            written = os.write(descriptor, payload[offset:])
            if written <= 0:
                raise OSError("could not append Codex hook log")
            offset += written
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _hook_eligible(observation: Mapping[str, Any]) -> bool:
    paths = [observation.get("before_path"), observation.get("after_path")]
    selected = [Path(value) for value in paths if isinstance(value, str)]
    if not selected or not all(path.suffix == ".md" and "--" in path.name for path in selected):
        return False
    return not any("archive" in path.parts or "drafts" in path.parts for path in selected)


def _import_commit_change_set() -> Any:
    for path in (PACKAGE_ROOT, PACKAGE_ROOT / "COMMIT_CONTEXT", PACKAGE_ROOT / "APPEND_CHANGE_RECORDS", PACKAGE_ROOT / "COMMIT_CHANGE_SET"):
        if str(path) not in sys.path:
            sys.path.insert(0, str(path))
    try:
        import commit_change_set
    except ImportError as error:
        raise ToolError("peer-tool-unavailable", "COMMIT_CHANGE_SET is not importable from the installed runtime") from error
    return commit_change_set


def codex_hook(repository: Path | str, phase: str, adapter_id: str, payload: Mapping[str, Any]) -> dict[str, object]:
    root = resolve_repository(Path(repository))
    cwd = Path(str(payload.get("cwd") or root)).expanduser().resolve()
    if cwd != root and root not in cwd.parents:
        return {"phase": phase, "effect": "outside-repository", "commit_count": 0}
    snapshot_path = _hook_snapshot_path(root, payload)
    if phase == "pre":
        snapshot = {
            "schema_version": 1,
            "session_id": _require_string(payload.get("session_id"), "session_id"),
            "tool_use_id": _require_string(payload.get("tool_use_id"), "tool_use_id"),
            "frontier": _frontier_document(scan_governed_files(root)),
        }
        _atomic_write(snapshot_path, _canonical_json(snapshot) + "\n")
        return {"phase": phase, "effect": "snapshot", "commit_count": 0}
    if phase != "post":
        raise ToolError("codex-hook-phase-invalid", "Codex hook phase must be pre or post")
    if not snapshot_path.is_file():
        return {"phase": phase, "effect": "no-pre-snapshot", "commit_count": 0}
    try:
        snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ToolError("codex-hook-snapshot-invalid", "Codex pre-hook snapshot is invalid JSON") from error
    snapshot_path.unlink()
    if not isinstance(snapshot, Mapping) or snapshot.get("schema_version") != 1:
        raise ToolError("codex-hook-snapshot-invalid", "Codex pre-hook snapshot schema is invalid")
    if snapshot.get("session_id") != payload.get("session_id") or snapshot.get("tool_use_id") != payload.get("tool_use_id"):
        raise ToolError("codex-hook-snapshot-mismatch", "Codex pre/post hook identities differ")
    selected = _read_registry(root).get(_require_identifier(adapter_id, "adapter_id"))
    if selected is None or not selected.enabled:
        return {"phase": phase, "effect": "adapter-not-enabled", "commit_count": 0}
    session_uuid = _validate_uuid(payload.get("session_id"), "session_id")
    previous = _frontier_from_document(snapshot.get("frontier"))
    current = scan_governed_files(root)
    observed_at = dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    observations = [
        {
            **observation,
            "llm_session": {"app": selected.application, "uuid": session_uuid},
        }
        for observation in detect_watch_observations(
            previous,
            current,
            adapter_id=selected.adapter_id,
            repository=root,
            observed_at=observed_at,
            correlations=_read_pipeline_correlations(_runtime_directory(root) / PIPELINE_CORRELATIONS_NAME),
        )
        if _hook_eligible(observation)
    ]
    triggers = emit_triggers(observations, adapter=selected, repository=root, environment={})
    if not triggers:
        return {"phase": phase, "effect": "no-eligible-change", "commit_count": 0}
    committer = _import_commit_change_set()
    commits: list[dict[str, str]] = []
    for trigger in triggers:
        try:
            result = committer.run(root, {"trigger": trigger}, apply=True)
        except Exception as error:
            _hook_log(
                root,
                {
                    "schema_version": 1,
                    "event": "auto_commit_failed",
                    "trigger_id": trigger["trigger_id"],
                    "error_code": str(getattr(error, "code", "unexpected-error")),
                },
            )
            raise ToolError("auto-commit-failed", str(error)) from error
        commits.append({"trigger_id": str(trigger["trigger_id"]), "commit": str(result["commit"])})
    _hook_log(
        root,
        {
            "schema_version": 1,
            "event": "auto_commit_completed",
            "commits": commits,
        },
    )
    return {"phase": phase, "effect": "committed", "commit_count": len(commits), "commits": commits}


def _envelope(*, ok: bool, mode: str, result: object | None = None, diagnostic: ToolError | None = None) -> dict[str, object]:
    diagnostics: list[dict[str, str]] = []
    if diagnostic is not None:
        diagnostics.append({"code": diagnostic.code, "message": diagnostic.message})
    payload: dict[str, object] = {
        "schema_version": TOOL_SCHEMA_VERSION,
        "tool": {"capability_id": CAPABILITY_ID, "kind": TOOL_KIND},
        "ok": ok,
        "mode": mode,
        "diagnostics": diagnostics,
    }
    if result is not None:
        payload["result"] = result
    return payload


def _load_observations(path: str) -> list[Mapping[str, Any]]:
    try:
        raw = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
        decoded = json.loads(raw)
    except (OSError, json.JSONDecodeError) as error:
        raise ToolError("invalid-input", f"cannot read JSON observations: {error}") from error
    if isinstance(decoded, Mapping) and "observations" in decoded:
        decoded = decoded["observations"]
    if isinstance(decoded, Mapping):
        return [_require_mapping(decoded, "observation")]
    if not isinstance(decoded, list):
        raise ToolError("invalid-input", "observations input must be an object or list")
    return [_require_mapping(item, "observation") for item in decoded]


def _describe() -> dict[str, object]:
    return {
        "capability_id": CAPABILITY_ID,
        "kind": TOOL_KIND,
        "read_only_observe": True,
        "canonical_script": ".caprmedio/200_LAYER_2_FRAMEWORK_ENGINE/TOOLS/COMMIT_TRIGGER/commit_trigger.py",
        "input_schema": {
            "observe": {
                "type": "object",
                "required": ["adapter_id", "source_event_id", "observed_at"],
                "properties": {
                    "adapter_id": {"type": "string"},
                    "source_event_id": {"type": "string"},
                    "observed_at": {"type": "string", "format": "date-time"},
                    "before_path": {"type": ["string", "null"]},
                    "after_path": {"type": ["string", "null"]},
                    "llm_session": {
                        "type": "object",
                        "required": ["app", "uuid"],
                        "properties": {"app": {"type": "string"}, "uuid": {"type": "string", "format": "uuid"}},
                    },
                    "pipeline": {
                        "type": "object",
                        "properties": {
                            "owned": {"const": True},
                            "action_id": {"type": "string"},
                            "kind": {"enum": ["journal", "runtime-state"]},
                        },
                    },
                },
            }
        },
        "commands": {
            "describe": {"effects": []},
            "observe": {"input": "JSON object or {observations: [...]}"},
            "watch": {
                "input": "enabled native Codex adapter and polling controls",
                "effects": [],
                "result": "one read-only handoff envelope per detected source boundary",
            },
            "runtime install": {"effects": ["self-contained project-local runtime package"]},
            "runtime status": {"effects": []},
            "codex-hook": {"input": "Codex hook JSON on stdin", "effects": ["pre snapshot or complete auto-commit flow"]},
            "adapter install": {"input": "adapter identity and host session resolver", "effects": ["runtime registry", "Codex Hook registration", "runtime-owned Git Hook registration"]},
            "adapter status": {"effects": []},
            "adapter enable": {"effects": ["runtime registry"]},
            "adapter disable": {"effects": ["runtime registry"]},
            "adapter uninstall": {"effects": ["runtime registry"]},
        },
        "result_envelope": {"schema_version": TOOL_SCHEMA_VERSION, "diagnostics": "ordered machine-readable diagnostics"},
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", default=".", help="repository root or a path within it")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("describe", help="return machine-readable Tool capability metadata")
    observe = commands.add_parser("observe", help="emit deduplicated trigger handoffs without mutation")
    observe.add_argument("--adapter-id", required=True)
    observe.add_argument("--input", required=True, help="JSON file path or - for stdin")
    watch = commands.add_parser("watch", help="poll native Codex governed source changes without mutation")
    watch.add_argument("--adapter-id", required=True)
    watch.add_argument("--poll-interval", type=float, default=1.0)
    watch.add_argument("--max-events", type=int)
    watch.add_argument("--max-polls", type=int)
    watch.add_argument(
        "--pipeline-correlation-file",
        help="optional NDJSON action/path suppression frontier; default is the Tool runtime path",
    )
    runtime = commands.add_parser("runtime", help="install or inspect the self-contained project-local runtime")
    runtime_commands = runtime.add_subparsers(dest="runtime_command", required=True)
    runtime_install = runtime_commands.add_parser("install")
    runtime_install.add_argument("--apply", action="store_true")
    runtime_commands.add_parser("status")
    codex = commands.add_parser("codex-hook", help="execute one Codex pre/post Tool-use adapter phase")
    codex.add_argument("phase", choices=("pre", "post"))
    codex.add_argument("--adapter-id", required=True)
    adapter = commands.add_parser("adapter", help="manage explicit host-adapter registration")
    adapter_commands = adapter.add_subparsers(dest="adapter_command", required=True)
    install = adapter_commands.add_parser("install")
    install.add_argument("--adapter-id", required=True)
    install.add_argument("--application", required=True)
    install.add_argument("--host-session-env", required=True)
    install.add_argument("--fallback-session-env")
    install.add_argument("--disabled", action="store_true")
    install.add_argument("--apply", action="store_true")
    adapter_commands.add_parser("status")
    for name in ("enable", "disable", "uninstall"):
        mutation = adapter_commands.add_parser(name)
        mutation.add_argument("--adapter-id", required=True)
        mutation.add_argument("--apply", action="store_true")
    return parser


def cli(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.command == "describe":
            result = _describe()
            mode = "read-only"
        elif args.command == "observe":
            triggers = emit_from_registered_adapter(
                _load_observations(args.input),
                repository=args.repository,
                adapter_id=args.adapter_id,
            )
            result = {
                "handoffs": [
                    {"interface": "COMMIT_CHANGE_SET", "trigger": trigger}
                    for trigger in triggers
                ],
                "trigger_count": len(triggers),
            }
            mode = "read-only"
        elif args.command == "watch":
            if args.max_events is not None and args.max_events < 0:
                raise ToolError("invalid-maximum-events", "max_events must not be negative")
            if args.max_events == 0:
                result = {"handoffs": [], "trigger_count": 0, "stream": "watch", "stopped": "event-limit"}
                mode = "read-only"
                print(_canonical_json(_envelope(ok=True, mode=mode, result=result)))
                return 0
            resolved_repository = resolve_repository(Path(args.repository))
            registered = _read_registry(resolved_repository)
            selected = registered.get(_require_identifier(args.adapter_id, "adapter_id"))
            if selected is None or not selected.enabled:
                # Disabled and uninstalled adapters are intentionally silent.
                result = {"handoffs": [], "trigger_count": 0, "stopped": "adapter-not-enabled"}
                mode = "read-only"
            else:
                emitted = 0
                for triggers in watch_triggers(
                    repository=resolved_repository,
                    adapter=selected,
                    poll_interval=args.poll_interval,
                    maximum_polls=args.max_polls,
                    pipeline_correlation_path=(Path(args.pipeline_correlation_file) if args.pipeline_correlation_file else None),
                ):
                    if not triggers:
                        continue
                    remaining = None if args.max_events is None else args.max_events - emitted
                    selected_triggers = triggers if remaining is None else triggers[:remaining]
                    if not selected_triggers:
                        break
                    emitted += len(selected_triggers)
                    print(
                        _canonical_json(
                            _envelope(
                                ok=True,
                                mode="read-only",
                                result={
                                    "handoffs": [
                                        {"interface": "COMMIT_CHANGE_SET", "trigger": trigger}
                                        for trigger in selected_triggers
                                    ],
                                    "trigger_count": len(selected_triggers),
                                    "stream": "watch",
                                },
                            )
                        ),
                        flush=True,
                    )
                    if args.max_events is not None and emitted >= args.max_events:
                        return 0
                result = {"handoffs": [], "trigger_count": 0, "stream": "watch", "stopped": "poll-limit-or-interrupt"}
                mode = "read-only"
        elif args.command == "runtime":
            if args.runtime_command == "status":
                result = runtime_package_status(args.repository)
                mode = "read-only"
            else:
                result = install_runtime_package(args.repository, apply=args.apply)
                mode = "apply" if args.apply else "dry-run"
        elif args.command == "codex-hook":
            result = codex_hook(args.repository, args.phase, args.adapter_id, _hook_payload())
            mode = "apply"
        elif args.adapter_command == "status":
            result = adapter_operation(args.repository, "status")
            mode = "read-only"
        elif args.adapter_command == "install":
            spec = AdapterSpec(
                args.adapter_id,
                args.application,
                args.host_session_env,
                args.fallback_session_env,
                not args.disabled,
            )
            result = adapter_operation(
                args.repository,
                "install",
                adapter=spec,
                apply=args.apply,
                manage_host_hooks=True,
            )
            mode = "apply" if args.apply else "dry-run"
        else:
            result = adapter_operation(
                args.repository,
                args.adapter_command,
                adapter_id=args.adapter_id,
                apply=args.apply,
                manage_host_hooks=True,
            )
            mode = "apply" if args.apply else "dry-run"
    except ToolError as error:
        print(_canonical_json(_envelope(ok=False, mode="read-only", diagnostic=error)))
        return 2
    except KeyboardInterrupt:
        print(
            _canonical_json(
                _envelope(
                    ok=True,
                    mode="read-only",
                    result={"handoffs": [], "trigger_count": 0, "stream": "watch", "stopped": "interrupt"},
                )
            )
        )
        return 0
    print(_canonical_json(_envelope(ok=True, mode=mode, result=result)))
    return 0


if __name__ == "__main__":
    raise SystemExit(cli())
