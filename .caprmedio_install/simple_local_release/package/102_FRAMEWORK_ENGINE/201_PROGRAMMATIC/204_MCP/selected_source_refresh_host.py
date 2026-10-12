"""Private trusted-host command for D588 selected-source refreshes.

This adapter deliberately has no MCP registration.  It closes the host-derived
Operator and Codex-session inputs before delegating to the existing publisher.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import stat
import sys
import uuid
from collections.abc import Sequence
from typing import Any


_MCP_ROOT = Path(__file__).resolve().parent
_TOOLS_ROOT = _MCP_ROOT.parent / "201_TOOLS"
for _path in (_MCP_ROOT, _TOOLS_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from operator_registry import OperatorRegistryError, parse_operators_registry  # noqa: E402
from release_manifest_authorization import authorize_operator_refresh  # noqa: E402
from release_manifest_publisher import plan_release_manifest_refresh, refresh_release_manifest  # noqa: E402
from selected_source_refresh import registered_source_refresh  # noqa: E402


_OPERATOR_NAME = "Anatoly Maslennikov"
_REGISTRY_REF = Path(".caprmedio_caprmedio/operators_registry.toml")


class SelectedSourceRefreshHostError(RuntimeError):
    """Stable refusal before a host-command execute can have an effect."""


def _reject(message: str) -> None:
    raise SelectedSourceRefreshHostError(message)


def _project_root(project_root: str | Path) -> Path:
    supplied = Path(project_root)
    try:
        root = supplied.resolve(strict=True)
        item = os.lstat(supplied)
    except (OSError, TypeError, ValueError) as error:
        raise SelectedSourceRefreshHostError("selected-source-refresh Project root is unavailable") from error
    if stat.S_ISLNK(item.st_mode) or not stat.S_ISDIR(item.st_mode) or root.is_symlink():
        _reject("selected-source-refresh Project root is unsafe")
    return root


def _read_regular(root: Path, relative: Path) -> bytes:
    candidate = root
    try:
        for index, part in enumerate(relative.parts):
            candidate /= part
            item = os.lstat(candidate)
            if stat.S_ISLNK(item.st_mode):
                _reject("selected-source-refresh operators registry is unsafe")
            if index < len(relative.parts) - 1 and not stat.S_ISDIR(item.st_mode):
                _reject("selected-source-refresh operators registry is unsafe")
        if not stat.S_ISREG(os.stat(candidate, follow_symlinks=False).st_mode):
            _reject("selected-source-refresh operators registry is unsafe")
        return candidate.read_bytes()
    except SelectedSourceRefreshHostError:
        raise
    except OSError as error:
        raise SelectedSourceRefreshHostError("selected-source-refresh operators registry is unavailable") from error


def _operator_context(root: Path) -> tuple[str, str]:
    try:
        records = parse_operators_registry(_read_regular(root, _REGISTRY_REF))
    except OperatorRegistryError as error:
        raise SelectedSourceRefreshHostError("selected-source-refresh operators registry is invalid") from error
    matching = [record for record in records if record.name == _OPERATOR_NAME]
    if len(matching) != 1 or not isinstance(matching[0].journal_author, str) or not matching[0].journal_author:
        _reject("selected-source-refresh Operator identity is missing or ambiguous")
    return matching[0].name, matching[0].journal_author


def _codex_session() -> dict[str, str]:
    values = os.environ
    candidates = [
        (field, values.get(field))
        for field in ("CODEX_THREAD_ID", "CODEX_SESSION_ID")
        if values.get(field)
    ]
    if not candidates:
        _reject("selected-source-refresh Codex session is missing")
    parsed: list[str] = []
    for field, value in candidates:
        if not isinstance(value, str):
            _reject("selected-source-refresh Codex session is invalid")
        try:
            parsed.append(str(uuid.UUID(value)))
        except (ValueError, AttributeError) as error:
            raise SelectedSourceRefreshHostError(
                f"selected-source-refresh {field} must be a UUID"
            ) from error
    if len(set(parsed)) != 1:
        _reject("selected-source-refresh Codex session identifiers conflict")
    return {"app": "codex", "uuid": parsed[0]}


def refresh_selected_release_binding(
    project_root: str | Path, mode: str = "plan",
) -> dict[str, Any]:
    """Run D588 plan or explicit trusted-host execute for one Project root."""
    root = _project_root(project_root)
    if mode == "plan":
        # D588 explicitly requires this to be the only operation in plan mode.
        return plan_release_manifest_refresh(root)
    if mode != "execute":
        _reject("selected-source-refresh mode must be plan or execute")

    session = _codex_session()
    operator_name, journal_author = _operator_context(root)
    registration = registered_source_refresh(root)
    authorization_ref = registration["authorization_ref"]
    plan = plan_release_manifest_refresh(root)
    context = authorize_operator_refresh(
        root, plan, operator_name=operator_name, journal_author=journal_author,
        llm_session=session, authorization_ref=authorization_ref,
    )
    return refresh_release_manifest(root, execute=True, authorization=context)


def main(argv: Sequence[str] | None = None) -> int:
    """Run the private command with only a Project root and an explicit mode."""
    parser = argparse.ArgumentParser(prog="refresh-selected-release-binding")
    parser.add_argument("project_root")
    parser.add_argument("--mode", choices=("plan", "execute"), default="plan")
    arguments = parser.parse_args(argv)
    try:
        result = refresh_selected_release_binding(arguments.project_root, arguments.mode)
    except SelectedSourceRefreshHostError as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
