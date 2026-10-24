# implementation of:
# Method: CA-M-410
"""Validated carriers and atomic I/O for Integrated continuation state."""

from __future__ import annotations

from collections.abc import Mapping
import copy
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any


_TOOLS = Path(__file__).resolve().parents[2] / "201_TOOLS"
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from project_runtime import TemporaryBoundaryError, repository_root  # noqa: E402


MAX_RECORD_BYTES = 512 * 1024
MAX_RECORDS = 128
RUN_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$")
FRONTIER_FIELDS = frozenset(
    {
        "continuation_id",
        "project",
        "run",
        "step",
        "action",
        "request_digest",
        "source_digest",
        "packet_digest",
        "candidate_digest",
        "authorization_digest",
    }
)


class IntegratedFrontierError(RuntimeError):
    """A continuation carrier cannot be safely read, changed, or resumed."""


def canonical(value: object) -> bytes:
    try:
        return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    except (TypeError, ValueError) as error:
        raise IntegratedFrontierError("Integrated value is not JSON-serializable") from error


def digest(value: object) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def text(value: object, name: str) -> str:
    if not isinstance(value, str) or not value or len(value) > 512:
        raise IntegratedFrontierError(f"{name} must be non-empty bounded text")
    return value


def sha(value: object, name: str) -> str:
    result = text(value, name)
    if len(result) != 64 or any(char not in "0123456789abcdef" for char in result):
        raise IntegratedFrontierError(f"{name} must be a lowercase SHA-256 digest")
    return result


def project_root(root: str | Path) -> Path:
    path = Path(root)
    if path.is_symlink():
        raise IntegratedFrontierError("Project root must not be a symlink")
    try:
        resolved = path.resolve(strict=True)
        if not resolved.is_dir() or repository_root(resolved) != resolved:
            raise IntegratedFrontierError("path is not the canonical Project root")
    except (OSError, TemporaryBoundaryError) as error:
        raise IntegratedFrontierError("Project root is unavailable") from error
    return resolved


def directory(path: Path) -> Path:
    cursor = Path(path.anchor)
    for part in path.parts[1:]:
        cursor /= part
        if cursor.is_symlink() or (cursor.exists() and not cursor.is_dir()):
            raise IntegratedFrontierError(f"unsafe runtime directory: {cursor}")
        cursor.mkdir(exist_ok=True)
    return path


def state_path(root: Path, run_id: str) -> Path:
    if not isinstance(run_id, str) or not RUN_ID.fullmatch(run_id):
        raise IntegratedFrontierError("invalid selected Run ID")
    base = root / ".caprmedio_install/workflow_orchestrator/runs"
    directory(base / run_id)
    return base / run_id / "integrated_frontier.json"


def validate_frontier(
    value: Mapping[str, Any], run_id: str, root: Path | None = None
) -> dict[str, Any]:
    if set(value) != FRONTIER_FIELDS:
        raise IntegratedFrontierError("Integrated frontier fields are incomplete or unsupported")
    continuation = text(value.get("continuation_id"), "continuation_id")
    if "/" in continuation or continuation in {".", ".."}:
        raise IntegratedFrontierError("continuation_id is not a safe identity")
    for name in ("project", "run", "step", "action"):
        binding = value.get(name)
        if not isinstance(binding, Mapping):
            raise IntegratedFrontierError(f"{name} binding is invalid")
        expected = {"root", "digest"} if name == "project" else {"id", "digest"}
        if set(binding) != expected:
            raise IntegratedFrontierError(f"{name} binding is invalid")
        key = "root" if name == "project" else "id"
        text(binding.get(key), f"{name}.{key}")
        sha(binding.get("digest"), f"{name}.digest")
    if root is not None:
        expected_root = root.as_posix()
        project = value["project"]
        if project["root"] != expected_root or project["digest"] != digest(expected_root):
            raise IntegratedFrontierError(
                "frontier Project binding differs from the selected Project"
            )
    if value["run"]["id"] != run_id:
        raise IntegratedFrontierError("frontier Run binding differs from the selected Run")
    for name in ("request_digest", "source_digest", "packet_digest", "authorization_digest"):
        sha(value.get(name), name)
    text(value.get("candidate_digest"), "candidate_digest")
    return copy.deepcopy(dict(value))


def validate_submission(value: Mapping[str, Any]) -> dict[str, Any]:
    if set(value) != {"continuation_id", "result", "result_digest"}:
        raise IntegratedFrontierError("Integrated submission fields are incomplete or unsupported")
    result = copy.deepcopy(value.get("result"))
    result_digest = sha(value.get("result_digest"), "result_digest")
    if result_digest != digest(result):
        raise IntegratedFrontierError("submission result digest is stale")
    return {
        "continuation_id": text(value.get("continuation_id"), "continuation_id"),
        "result": result,
        "result_digest": result_digest,
    }
