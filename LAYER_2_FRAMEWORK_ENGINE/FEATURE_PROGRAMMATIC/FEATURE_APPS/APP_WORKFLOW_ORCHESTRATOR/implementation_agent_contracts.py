"""Bounded response contracts for the Implementation Agent transport."""

from __future__ import annotations

from collections.abc import Mapping
import json
from pathlib import Path
from typing import Any


MAX_OUTPUT_BYTES = 1 * 1024 * 1024
MAX_INPUT_BYTES = 2 * 1024 * 1024
MAX_TRACKED_FILES = 512
MAX_TRACKED_FILE_BYTES = 1 * 1024 * 1024
MAX_TRACKED_TOTAL_BYTES = 8 * 1024 * 1024
ADMITTED_RESULTS = frozenset(
    {
        "evaluation_ready",
        "requirement_ready",
        "evaluation_runnable",
        "complete",
        "blocked",
        "prepared",
        "implemented",
        "passed",
        "failed",
        "expected_initial_failure",
        "implementation_defect",
        "test_implementation_defect",
        "authority_change_required",
        "environment_blocker",
        "unresolved",
        "retry_permitted",
        "retry_blocked",
        "repaired",
    }
)


def output_schema() -> dict[str, Any]:
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "result": {"type": "string", "enum": sorted(ADMITTED_RESULTS)},
            "outputs": {"type": "object"},
            "evidence": {"type": "array"},
            "blockers": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["result", "outputs", "evidence", "blockers"],
    }


def read_output(path: Path) -> dict[str, Any]:
    if not path.is_file() or path.is_symlink() or path.stat().st_size > MAX_OUTPUT_BYTES:
        raise ValueError("Agent output is missing, unsafe, or exceeds the byte limit")
    value = json.loads(path.read_bytes())
    if not isinstance(value, dict):
        raise ValueError("Agent output must be a JSON object")
    validate_output(value)
    return value


def validate_output(response: Mapping[str, Any]) -> None:
    if set(response) != {"result", "outputs", "evidence", "blockers"}:
        raise ValueError("Agent output must contain only the current callback fields")
    if response.get("result") not in ADMITTED_RESULTS:
        raise ValueError("Agent output result is not admitted by the current workflow")
    if not isinstance(response.get("outputs"), Mapping) or not isinstance(
        response.get("evidence"), list
    ):
        raise ValueError("Agent output requires object outputs and array evidence")
    if not isinstance(response.get("blockers"), list) or not all(
        isinstance(item, str) for item in response["blockers"]
    ):
        raise ValueError("Agent output blockers must be an array of strings")


def admit_response(
    response: Mapping[str, Any],
    changes: list[dict[str, str | None]],
    write_admitted: bool,
    sandbox: str,
    timeout: int,
) -> dict[str, Any]:
    outputs = dict(response["outputs"])
    declared = outputs.get("changed_paths")
    try:
        declared_paths = declared_paths_from(declared) if declared is not None else None
    except ValueError as error:
        return blocked(
            str(error),
            evidence=[
                transport_evidence(sandbox, timeout, "out_of_bounds_output", changes=changes)
            ],
        )
    observed_paths = {entry["path"] for entry in changes}
    if changes and not write_admitted:
        return blocked(
            "Implementation Agent changed the workspace without an admitted disposable write capability",
            evidence=[
                transport_evidence(sandbox, timeout, "unadmitted_workspace_change", changes=changes)
            ],
        )
    if declared_paths is not None and declared_paths != observed_paths:
        return blocked(
            "Implementation Agent changed-path output does not match observed workspace changes",
            evidence=[
                transport_evidence(sandbox, timeout, "changed_path_mismatch", changes=changes)
            ],
        )
    if response["result"] in {"implemented", "repaired"} and not changes:
        return blocked(
            "Implementation Agent reported performed code work without observed workspace changes",
            evidence=[transport_evidence(sandbox, timeout, "unobserved_performed_work")],
        )
    if changes:
        outputs["changed_paths"] = changes
    return {
        "result": response["result"],
        "outputs": outputs,
        "evidence": [
            *response["evidence"],
            transport_evidence(sandbox, timeout, "completed", changes=changes),
        ],
        "blockers": list(response["blockers"]),
    }


def declared_paths_from(value: Any) -> set[str]:
    if not isinstance(value, list):
        raise ValueError("Implementation Agent changed_paths must be an array")
    paths: set[str] = set()
    for item in value:
        path = item.get("path") if isinstance(item, Mapping) else item
        if not isinstance(path, str) or not path:
            raise ValueError("Implementation Agent changed_paths contains an invalid path")
        candidate = Path(path)
        if candidate.is_absolute() or ".." in candidate.parts or candidate.as_posix() in {"", "."}:
            raise ValueError("Implementation Agent returned an out-of-bound changed path")
        paths.add(candidate.as_posix())
    if len(paths) != len(value):
        raise ValueError("Implementation Agent changed_paths contains duplicates")
    return paths


def transport_evidence(
    sandbox: str,
    timeout: int,
    status: str,
    returncode: int | None = None,
    *,
    changes: list[dict[str, str | None]] | None = None,
) -> dict[str, Any]:
    evidence: dict[str, Any] = {
        "transport": "codex_cli_non_interactive",
        "sandbox": sandbox,
        "timeout_seconds": timeout,
        "status": status,
    }
    if returncode is not None:
        evidence["returncode"] = returncode
    if changes is not None:
        evidence["observed_changes"] = changes
    return evidence


def blocked(
    reason: str,
    *,
    evidence: list[Any] | None = None,
    blockers: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "result": "blocked",
        "outputs": {},
        "evidence": evidence or [],
        "blockers": blockers or [reason],
    }
