#!/usr/bin/env python3
"""Install all canonical CAPRMEDIO Tools and host Hooks for one project."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import shlex
import shutil
import subprocess
import sys
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


SCRIPT_PATH = Path(__file__).resolve()
TOOLS_ROOT = SCRIPT_PATH.parents[1]
for parent in SCRIPT_PATH.parents:
    if parent.name == ".caprmedio_install":
        sys.pycache_prefix = str(parent.parent / ".caprmedio_runtime/cache/python")
        break
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from framework_installation import (  # noqa: E402
    INSTALL_DIRECTORY,
    InstallationError,
    RUNTIME_DIRECTORY,
    SERVICE_ENTRYPOINT,
    SOURCE_DIRECTORY,
    install_release,
    installation_status,
    resolve_repository,
    source_inventory,
)


TOOL_ID = "INSTALL_TOOLS"
TOOL_KIND = "doer"
TOOL_SCHEMA_VERSION = 1
ADAPTER_ID = "codex-file-events"
MANAGED_HOOKS_PATH = ".caprmedio_install/hooks/git"
LEGACY_HOOKS_PATH = ".caprmedio_runtime/hooks/git"
LAUNCHERS = {
    "commit-trigger": "TOOLS/COMMIT_TRIGGER/commit_trigger.py",
    "install-tools": "TOOLS/INSTALL_TOOLS/install_tools.py",
    "start-background-services": SERVICE_ENTRYPOINT,
}


class ToolError(RuntimeError):
    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(message)


def _json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _envelope(*, ok: bool, mode: str, result: Mapping[str, Any] | None = None, error: Exception | None = None) -> dict[str, Any]:
    diagnostics: list[dict[str, str]] = []
    if error is not None:
        diagnostics.append(
            {
                "code": str(getattr(error, "code", "installation-failed")),
                "message": str(getattr(error, "message", error)),
            }
        )
    return {
        "schema_version": TOOL_SCHEMA_VERSION,
        "tool": {"capability_id": TOOL_ID, "kind": TOOL_KIND},
        "ok": ok,
        "mode": mode,
        "diagnostics": diagnostics,
        "result": dict(result or {}),
    }


def _git_hooks_path(root: Path) -> str | None:
    completed = subprocess.run(
        ["git", "-C", str(root), "config", "--local", "--get", "core.hooksPath"],
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode == 1:
        return None
    if completed.returncode != 0:
        raise ToolError("git-config-failed", (completed.stderr or completed.stdout).strip() or "cannot read core.hooksPath")
    return completed.stdout.strip()


def _set_git_hooks_path(root: Path, value: str | None) -> None:
    arguments = ["git", "-C", str(root), "config", "--local"]
    arguments += ["--unset-all", "core.hooksPath"] if value is None else ["core.hooksPath", value]
    completed = subprocess.run(arguments, capture_output=True, text=True, check=False)
    if completed.returncode not in ({0, 5} if value is None else {0}):
        raise ToolError("git-config-failed", (completed.stderr or completed.stdout).strip() or "cannot update core.hooksPath")


def _preflight(root: Path) -> dict[str, Any]:
    rows, release = source_inventory(root)
    hooks_path = _git_hooks_path(root)
    if hooks_path not in {None, MANAGED_HOOKS_PATH, LEGACY_HOOKS_PATH}:
        raise ToolError("git-hooks-path-conflict", f"repository already uses a different local core.hooksPath: {hooks_path}")
    project_codex = root / ".codex/hooks.json"
    if project_codex.is_file() and not project_codex.is_symlink():
        try:
            document = json.loads(project_codex.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            raise ToolError("codex-hook-config-invalid", f"{project_codex}: invalid JSON") from error
        if not isinstance(document, dict):
            raise ToolError("codex-hook-config-invalid", f"{project_codex}: root must be an object")
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).expanduser().resolve()
    user_codex = codex_home / "hooks.json"
    if user_codex.is_file():
        try:
            user_document = json.loads(user_codex.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            raise ToolError("codex-hook-config-invalid", f"{user_codex}: invalid JSON") from error
        if not isinstance(user_document, dict):
            raise ToolError("codex-hook-config-invalid", f"{user_codex}: root must be an object")
    return {
        "canonical_source": SOURCE_DIRECTORY.as_posix(),
        "install_root": INSTALL_DIRECTORY.as_posix(),
        "runtime_root": RUNTIME_DIRECTORY.as_posix(),
        "release": release,
        "file_count": len(rows),
        "previous_hooks_path": hooks_path,
        "codex_user_hook_carrier": user_codex.as_posix(),
        "hooks": [
            "codex:PreToolUse",
            "codex:PostToolUse",
            "codex:SessionStart",
            "codex:Stop",
            "git:pre-commit",
            "git:commit-msg",
            "git:post-commit",
        ],
    }


def _load_installed_trigger(root: Path, package_root: str):
    path = root / package_root / "COMMIT_TRIGGER/commit_trigger.py"
    spec = importlib.util.spec_from_file_location(f"caprmedio_installed_commit_trigger_{os.getpid()}", path)
    if spec is None or spec.loader is None:
        raise ToolError("installed-trigger-unavailable", f"cannot load installed COMMIT_TRIGGER: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _launcher(root: Path, release: str, relative: str) -> str:
    target = root / INSTALL_DIRECTORY / "releases" / release / relative
    return "\n".join(
        [
            "#!/bin/sh",
            "set -eu",
            'repository=$(git rev-parse --show-toplevel)',
            "exec " + " ".join([shlex.quote(sys.executable), "-I", "-B", shlex.quote(str(target)), "--repository", '"$repository"', '"$@"']),
            "",
        ]
    )


def _write_launchers(root: Path, release: str) -> list[str]:
    directory = root / INSTALL_DIRECTORY / "bin"
    directory.mkdir(parents=True, exist_ok=True)
    carriers: list[str] = []
    for name, relative in LAUNCHERS.items():
        carrier = directory / name
        temporary = directory / f".{name}.{os.getpid()}"
        temporary.write_text(_launcher(root, release, relative), encoding="utf-8", newline="\n")
        temporary.chmod(0o755)
        os.replace(temporary, carrier)
        carriers.append(carrier.relative_to(root).as_posix())
    return carriers


def _legacy_codex_link(root: Path) -> tuple[bool, str | None]:
    carrier = root / ".codex/hooks.json"
    if not carrier.is_symlink():
        return False, None
    link_text = os.readlink(carrier)
    try:
        resolved = carrier.resolve()
    except OSError:
        return False, link_text
    legacy = (root / ".caprmedio_runtime/hooks/codex/hooks.json").resolve()
    return resolved == legacy, link_text


def _remove_legacy_installation(root: Path) -> list[str]:
    removed: list[str] = []
    for relative in (Path(".caprmedio_runtime/installed"), Path(".caprmedio_runtime/hooks")):
        target = root / relative
        if target.is_dir() and not target.is_symlink():
            shutil.rmtree(target)
            removed.append(relative.as_posix())
    return removed


def install(root: Path, *, apply: bool) -> dict[str, Any]:
    root = resolve_repository(root)
    preflight = _preflight(root)
    release_preview = install_release(root, apply=False)
    if not apply:
        return {**preflight, **release_preview, "hooks_installed": False, "launchers": sorted(LAUNCHERS)}

    previous_hooks_path = _git_hooks_path(root)
    codex_was_legacy_link, codex_link_text = _legacy_codex_link(root)
    if previous_hooks_path == LEGACY_HOOKS_PATH:
        _set_git_hooks_path(root, None)
    if codex_was_legacy_link:
        (root / ".codex/hooks.json").unlink()
    try:
        installed = install_release(root, apply=True)
        trigger = _load_installed_trigger(root, str(installed["package_root"]))
        adapter = trigger.AdapterSpec(ADAPTER_ID, "codex", "CODEX_THREAD_ID", "CODEX_SESSION_ID", True)
        adapter_result = trigger.adapter_operation(
            root,
            "install",
            adapter=adapter,
            apply=True,
            manage_host_hooks=True,
        )
        launchers = _write_launchers(root, str(installed["release"]))
        removed = _remove_legacy_installation(root)
    except BaseException:
        if _git_hooks_path(root) == MANAGED_HOOKS_PATH:
            _set_git_hooks_path(root, None)
        if previous_hooks_path is not None:
            _set_git_hooks_path(root, previous_hooks_path)
        carrier = root / ".codex/hooks.json"
        if codex_was_legacy_link and not carrier.exists() and codex_link_text is not None:
            carrier.parent.mkdir(parents=True, exist_ok=True)
            carrier.symlink_to(codex_link_text)
        raise
    status = tool_status(root)
    return {
        **preflight,
        **installed,
        "adapter": adapter_result,
        "hooks_installed": True,
        "launchers": launchers,
        "removed_legacy_installation": removed,
        "status": status,
    }


def tool_status(root: Path) -> dict[str, Any]:
    root = resolve_repository(root)
    installed = installation_status(root)
    if not installed.get("installed"):
        return {**installed, "hooks_installed": False, "launchers_verified": False}
    release = str(installed["release"])
    launchers = {}
    for name, relative in LAUNCHERS.items():
        carrier = root / INSTALL_DIRECTORY / "bin" / name
        expected = _launcher(root, release, relative)
        launchers[name] = carrier.is_file() and os.access(carrier, os.X_OK) and carrier.read_text(encoding="utf-8") == expected
    trigger = _load_installed_trigger(root, str(installed["package_root"]))
    adapter = trigger.adapter_operation(root, "status")
    git_hooks_path = _git_hooks_path(root)
    codex = trigger.codex_hooks_status(root, ADAPTER_ID)
    release_path_fragment = f".caprmedio_install/releases/{release}/"
    hook_carriers = [root / MANAGED_HOOKS_PATH / name for name in trigger.GIT_HOOK_NAMES]
    hooks_verified = (
        git_hooks_path == MANAGED_HOOKS_PATH
        and all(path.is_file() and os.access(path, os.X_OK) and release_path_fragment in path.read_text(encoding="utf-8") for path in hook_carriers)
        and codex["registered"] is True
        and codex["canonical_fragment_present"] is True
        and not codex["project_carrier_present"]
    )
    source_rows, source_release = source_inventory(root)
    return {
        **installed,
        "source_release": source_release,
        "source_file_count": len(source_rows),
        "source_matches_install": source_release == release,
        "hooks_path": git_hooks_path,
        "hooks_installed": hooks_verified,
        "codex_hook_carrier_verified": bool(codex["registered"]),
        "codex_hook": codex,
        "codex_hook_activation": "host-controlled-unverified",
        "codex_hook_operator_action": "Restart or resume each Codex task and review the changed user hooks once with /hooks.",
        "adapter": adapter,
        "launchers": launchers,
        "launchers_verified": all(launchers.values()),
    }


def _describe() -> dict[str, Any]:
    return {
        "capability_id": TOOL_ID,
        "kind": TOOL_KIND,
        "canonical_source": SOURCE_DIRECTORY.as_posix(),
        "install_root": INSTALL_DIRECTORY.as_posix(),
        "runtime_root": RUNTIME_DIRECTORY.as_posix(),
        "commands": {
            "describe": {"mode": "read-only"},
            "status": {"mode": "read-only"},
            "run": {"mode": "dry-run unless --apply", "effect": "install Tools, launchers, adapters, and Hooks"},
        },
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", default=".")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("describe")
    commands.add_parser("status")
    run = commands.add_parser("run")
    run.add_argument("--apply", action="store_true")
    return parser


def cli(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    mode = "read-only"
    try:
        if args.command == "describe":
            result = _describe()
        elif args.command == "status":
            result = tool_status(Path(args.repository))
        else:
            mode = "apply" if args.apply else "dry-run"
            result = install(Path(args.repository), apply=args.apply)
        print(_json(_envelope(ok=True, mode=mode, result=result)))
        return 0
    except (ToolError, InstallationError) as error:
        print(_json(_envelope(ok=False, mode=mode, error=error)))
        return 2


if __name__ == "__main__":
    raise SystemExit(cli())
