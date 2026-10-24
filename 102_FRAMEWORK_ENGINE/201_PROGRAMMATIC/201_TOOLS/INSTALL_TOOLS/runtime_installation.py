"""Install host settings and adapters independently of any Project."""

from __future__ import annotations

import os
from pathlib import Path
import sys

from operation_error_boundary import operation_error_boundary
from runtime_failure_diagnostics import report_failure
from INSTALL_TOOLS.codex_harness import CodexHarness
from INSTALL_TOOLS.host_installation_io import HostInstallationError
from INSTALL_TOOLS.host_installation_lock import installation_lock
from INSTALL_TOOLS.host_runtime_settings import HostRuntimeSettings


def _runtime_root(value, projects_root):
    base = os.environ.get("XDG_DATA_HOME") or str(Path.home() / ".local/share")
    root = Path(value or (Path(base) / "caprmedio/runtime")).expanduser()
    if not root.is_absolute() or ".." in root.parts or root.resolve() != root:
        raise HostInstallationError("Host runtime directory must be canonical and absolute")
    if root == root.parent or root.is_relative_to(projects_root):
        raise HostInstallationError("Host runtime must live outside the repositories folder")
    return root


def _docker_launcher(image):
    parent = Path(__file__).resolve().parents[2]
    directory = parent / "HOST_RUNTIME"
    if not directory.is_dir():
        directory = parent / "203_APPS/WORKFLOW_ORCHESTRATOR/docker"
    if not directory.is_dir():
        raise HostInstallationError("Shared Docker launcher is unavailable in this distribution")
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))
    from shared_mcp_launch_support import _image
    from shared_mcp_launcher import SharedMcpLauncher

    _image(image)
    return SharedMcpLauncher()


def _apply_configuration(settings, adapter):
    completed = []
    try:
        for stage in (settings, adapter):
            if stage is not None:
                completed.append(stage)
                stage.apply()
    except BaseException as error:
        failures = []
        for stage in reversed(completed):
            try:
                stage.restore()
            except Exception as rollback_error:
                failures.append(type(rollback_error).__name__)
        if failures:
            raise HostInstallationError("Installation failed with rollback conflicts") from error
        raise


def _prepare_adapter(harness, root, settings):
    if harness is None:
        return None
    adapter = CodexHarness(
        runtime_root=root,
        endpoint=f"http://127.0.0.1:{settings.preview['http_port']}/mcp",
        hook_source=Path(__file__).with_name("codex_project_context_hook.py"),
    )
    if adapter.codex_home.is_relative_to(Path(settings.preview["projects_root"])):
        raise HostInstallationError("Global CODEX_HOME must live outside the repositories folder")
    return adapter


def _container_error(error):
    failure, secondary = report_failure(
        None, error, component="HOST_INSTALLER", operation="start_shared_runtime"
    )
    return {
        "outcome": "failed",
        "ready": False,
        "condition": failure.code,
        "error": type(error).__name__,
        "diagnostic_error": secondary,
    }


def _start_container(launcher, settings, image):
    if image is None:
        return {"outcome": "not_requested", "ready": False}

    @operation_error_boundary(on_error=_container_error)
    def start():
        return launcher.apply(settings.path, image)

    return start()


def install_runtime(
    *,
    projects_root=None,
    host_settings=None,
    http_port=None,
    max_loaded_projects=None,
    harness=None,
    runtime_root=None,
    image=None,
    apply=False,
    launcher=None,
):
    if harness not in (None, "codex"):
        raise HostInstallationError("Unsupported harness")
    settings = HostRuntimeSettings(
        projects_root=projects_root,
        host_settings=host_settings,
        http_port=http_port,
        max_loaded_projects=max_loaded_projects,
    )
    root = _runtime_root(runtime_root, Path(settings.preview["projects_root"]))
    adapter = _prepare_adapter(harness, root, settings)
    if image is not None:
        launcher = launcher or _docker_launcher(image)
    proposal = {
        "scope": "runtime",
        "applied": False,
        "settings": settings.preview,
        "runtime_root": str(root),
        "harness": adapter.preview if adapter else None,
        "container": {"outcome": "planned" if image else "not_requested", "ready": False},
        "image": image,
    }
    if not apply:
        return proposal
    with installation_lock(settings.path.parent):
        _apply_configuration(settings, adapter)
        container = _start_container(launcher, settings, image)
    harness_result = None if adapter is None else {**adapter.preview, "mode": "apply"}
    return {**proposal, "applied": True, "harness": harness_result, "container": container}
