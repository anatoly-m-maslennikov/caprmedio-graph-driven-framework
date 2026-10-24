"""Install CAPRMEDIO's global Codex hook and HTTP MCP registration."""

from __future__ import annotations

import os
from pathlib import Path
import shlex
from urllib.parse import urlsplit
import venv

from INSTALL_TOOLS.codex_harness_documents import config_content, hooks_content, read_bounded
from INSTALL_TOOLS.host_installation_io import FileUpdate, HostInstallationError
from INSTALL_TOOLS.host_installation_lock import installation_lock


def _path(value: Path, label: str) -> Path:
    path = Path(value).expanduser()
    try:
        valid = path.is_absolute() and path == path.resolve(strict=False)
    except OSError, RuntimeError:
        valid = False
    if not valid:
        raise HostInstallationError("invalid-path", f"{label} must be absolute and canonical")
    return path


def _target(value: Path, label: str, kind: str) -> Path:
    path = _path(value, label)
    invalid = (
        path.exists() and (path.is_symlink() or not path.is_dir())
        if kind == "dir"
        else path.is_symlink() or not path.is_file()
    )
    if invalid:
        expected = "real directory" if kind == "dir" else "existing real file"
        raise HostInstallationError("invalid-path", f"{label} must be an {expected}")
    return path


class CodexHarness:
    """Pure preflight plus explicit global apply/restore for Codex."""

    def __init__(self, *, runtime_root: Path, endpoint: str, hook_source: Path) -> None:
        self.runtime_root = _target(runtime_root, "Codex runtime root", "dir")
        home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
        self.codex_home = _target(home, "CODEX_HOME", "dir")
        self.hook_source = _target(hook_source, "Codex hook source", "file")
        self._hook_content = read_bounded(self.hook_source, "Codex hook source")
        if not isinstance(endpoint, str):
            raise HostInstallationError(
                "invalid-endpoint", "Codex MCP endpoint must be an HTTP(S) URL"
            )
        try:
            split = urlsplit(endpoint)
        except ValueError as error:
            raise HostInstallationError(
                "invalid-endpoint", "Codex MCP endpoint must be an HTTP(S) URL"
            ) from error
        if split.scheme not in {"http", "https"} or not split.netloc:
            raise HostInstallationError(
                "invalid-endpoint", "Codex MCP endpoint must be an HTTP(S) URL"
            )
        self.endpoint = endpoint
        self.script = self.runtime_root / "codex_project_context.py"
        self.venv_root = self.runtime_root / "venv"
        self.python = self.venv_root / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
        if self.venv_root.exists():
            _target(self.venv_root, "Codex host virtual environment", "dir")
            self._check_python()
        hooks, config = self.codex_home / "hooks.json", self.codex_home / "config.toml"
        command = shlex.join((str(self.python), "-B", str(self.script)))
        hook_plan, hooks_original = hooks_content(hooks, command, include_original=True)
        config_plan, config_original = config_content(config, endpoint, include_original=True)
        self._updates = (
            FileUpdate(self.script, self._hook_content),
            FileUpdate(hooks, hook_plan),
            FileUpdate(config, config_plan),
        )
        if self._updates[1].previous_content != hooks_original:
            raise HostInstallationError("preflight-drift", "Codex hooks changed during preflight")
        if self._updates[2].previous_content != config_original:
            raise HostInstallationError("preflight-drift", "Codex config changed during preflight")
        self.hooks_path, self.config_path, self._applied = hooks, config, False

    def _check_python(self) -> None:
        if not self.python.is_file() or not os.access(self.python, os.X_OK):
            raise HostInstallationError(
                "venv-invalid", "Existing Codex host virtual environment has no Python"
            )

    @property
    def previewJSONdict(self) -> dict[str, object]:
        planned = [str(update.path) for update in self._updates if update.changed]
        if not self.venv_root.exists():
            planned.append(str(self.venv_root))
        return {
            "mode": "dry_run",
            "runtime_root": str(self.runtime_root),
            "endpoint": self.endpoint,
            "hook_source": str(self.hook_source),
            "hook_target": str(self.script),
            "venv": str(self.venv_root),
            "python": str(self.python),
            "codex_home": str(self.codex_home),
            "hooks": str(self.hooks_path),
            "config": str(self.config_path),
            "command": shlex.join((str(self.python), "-B", str(self.script))),
            "planned_changes": planned,
            "changed": bool(planned),
            "venv_present": self.venv_root.exists(),
            "applied": self._applied,
            "venv_retained_on_restore": True,
        }

    @property
    def preview(self) -> dict[str, object]:
        return self.previewJSONdict

    def _ensure_home(self) -> None:
        if not self.codex_home.exists():
            try:
                self.codex_home.mkdir(parents=True)
            except OSError as error:
                raise HostInstallationError(
                    "codex-home-failed", "Cannot create CODEX_HOME"
                ) from error
        _target(self.codex_home, "CODEX_HOME", "dir")

    def _ensure_venv(self) -> None:
        if not self.venv_root.exists():
            try:
                venv.EnvBuilder(with_pip=False).create(self.venv_root)
            except (OSError, RuntimeError) as error:
                raise HostInstallationError(
                    "venv-create-failed", "Cannot create Codex host Python"
                ) from error
        _target(self.venv_root, "Codex host virtual environment", "dir")
        self._check_python()

    def apply(self) -> None:
        if self._applied:
            return
        with (
            installation_lock(self.codex_home, ".caprmedio-codex-install.lock"),
            installation_lock(self.runtime_root),
        ):
            self._ensure_home()
            applied: list[FileUpdate] = []
            try:
                self._ensure_venv()
                for update in self._updates:
                    update.apply()
                    applied.append(update)
            except BaseException as error:
                conflicts = []
                for update in reversed(applied):
                    try:
                        update.restore()
                    except HostInstallationError as rollback_error:
                        conflicts.append(str(rollback_error))
                if conflicts:
                    raise HostInstallationError(
                        "restore-conflict", "Rollback conflict: " + conflicts[0]
                    ) from error
                raise
            self._applied = True

    def restore(self) -> None:
        if not self._applied:
            return
        with (
            installation_lock(self.codex_home, ".caprmedio-codex-install.lock"),
            installation_lock(self.runtime_root),
        ):
            conflicts = []
            for update in reversed(self._updates):
                try:
                    update.restore()
                except HostInstallationError as error:
                    conflicts.append(str(error))
            if conflicts:
                raise HostInstallationError("restore-conflict", conflicts[0])
            self._applied = False


__all__ = ["CodexHarness"]
