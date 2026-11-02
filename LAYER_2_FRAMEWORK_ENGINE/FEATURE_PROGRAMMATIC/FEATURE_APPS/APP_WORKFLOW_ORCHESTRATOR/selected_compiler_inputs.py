"""Executor-bound inputs shared by selected compiler Actions."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from selected_execution_contracts import SelectedExecutionError


def compiler_parameters_for_executor(
    root: Path,
    context: Mapping[str, object],
) -> dict[str, object]:
    """Bind the compiler path to the admitted executor Project only.

    The frozen request names the host Project while the compiler worker sees
    that same Project at its execution root.  Preserve every frozen value
    except this execution-local path and reject a substituted root.
    """
    parameters = context.get("parameters")
    if not isinstance(parameters, Mapping):
        raise SelectedExecutionError("compiler Action frozen parameters are invalid")
    frozen_root = parameters.get("project_root")
    if not isinstance(frozen_root, str) or not frozen_root:
        raise SelectedExecutionError("compiler Action frozen Project root is invalid")
    executor_root = context.get("project_root")
    if not isinstance(executor_root, Path) or executor_root != root:
        raise SelectedExecutionError("compiler Action execution Project root is invalid")
    request = dict(parameters)
    request["project_root"] = executor_root.as_posix()
    return request


def publication_output_paths(plan: object) -> list[str] | None:
    """Return exact, safe output references from a compiler publication plan.

    These are receipt references, not a fresh filesystem observation: a stale
    frontier proves replacement happened before currentness was lost.
    """
    if not isinstance(plan, list):
        return None
    paths: list[str] = []
    for item in plan:
        if not isinstance(item, Mapping):
            return None
        output_path = item.get("output_path")
        if (
            not isinstance(output_path, str)
            or not output_path
            or "\\x00" in output_path
            or "\\" in output_path
        ):
            return None
        candidate = Path(output_path)
        if candidate.is_absolute() or candidate == Path(".") or ".." in candidate.parts:
            return None
        if candidate.as_posix() != output_path:
            return None
        paths.append(output_path)
    if len(paths) != len(set(paths)):
        return None
    return sorted(paths)


__all__ = ["compiler_parameters_for_executor", "publication_output_paths"]
