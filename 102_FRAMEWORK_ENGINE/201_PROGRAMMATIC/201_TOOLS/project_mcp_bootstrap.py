"""Copy the package-owned Project MCP bootstrap without activating it."""

from __future__ import annotations

import os
from pathlib import Path
import stat
import tempfile


BOOTSTRAP_RELATIVE = Path(
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/start_mcp.py"
)
TARGET_RELATIVE = Path(".caprmedio_runtime/start_mcp.py")


class ProjectMcpBootstrapError(RuntimeError):
    """The bootstrap copy cannot be made without following an unsafe path."""


def _directory(path: Path) -> None:
    try:
        mode = path.lstat().st_mode
    except OSError as error:
        raise ProjectMcpBootstrapError("project-mcp-bootstrap-path-unavailable") from error
    if path.is_symlink() or not stat.S_ISDIR(mode):
        raise ProjectMcpBootstrapError("project-mcp-bootstrap-path-unsafe")


def _regular(path: Path) -> None:
    try:
        mode = path.lstat().st_mode
    except OSError as error:
        raise ProjectMcpBootstrapError("project-mcp-bootstrap-source-unavailable") from error
    if path.is_symlink() or not stat.S_ISREG(mode):
        raise ProjectMcpBootstrapError("project-mcp-bootstrap-source-unsafe")


def deploy_project_mcp_bootstrap(project_root: Path | str, package_root: Path | str) -> Path:
    """Refresh only the target bootstrap from one already-installed package.

    This copy deliberately does not import or execute the bootstrap, MCP, or
    Workflow code.  Existing runtime configuration and state remain untouched.
    """

    root, package = Path(project_root), Path(package_root)
    _directory(root)
    _directory(package)
    try:
        relative_package = package.relative_to(root)
    except ValueError as error:
        raise ProjectMcpBootstrapError("project-mcp-bootstrap-package-unsafe") from error
    if ".." in relative_package.parts:
        raise ProjectMcpBootstrapError("project-mcp-bootstrap-package-unsafe")
    cursor = root
    for component in relative_package.parts:
        cursor /= component
        _directory(cursor)
    source = package / BOOTSTRAP_RELATIVE
    cursor = package
    for component in BOOTSTRAP_RELATIVE.parts[:-1]:
        cursor /= component
        try:
            mode = cursor.lstat().st_mode
        except OSError as error:
            raise ProjectMcpBootstrapError("project-mcp-bootstrap-source-unavailable") from error
        if cursor.is_symlink() or not stat.S_ISDIR(mode):
            raise ProjectMcpBootstrapError("project-mcp-bootstrap-source-unsafe")
    _regular(source)
    if not source.stat().st_mode & 0o111:
        raise ProjectMcpBootstrapError("project-mcp-bootstrap-source-unsafe")
    runtime = root / TARGET_RELATIVE.parent
    if runtime.exists() or runtime.is_symlink():
        _directory(runtime)
    else:
        runtime.mkdir(mode=0o700)
        _directory(runtime)
    target = root / TARGET_RELATIVE
    if target.exists() or target.is_symlink():
        _regular(target)
    try:
        payload = source.read_bytes()
        source_mode = stat.S_IMODE(source.stat().st_mode)
        descriptor, temporary_name = tempfile.mkstemp(prefix=".start_mcp.", dir=runtime)
        temporary = Path(temporary_name)
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.chmod(source_mode)
        os.replace(temporary, target)
        return target
    except OSError as error:
        try:
            temporary.unlink(missing_ok=True)
        except (UnboundLocalError, OSError):
            pass
        raise ProjectMcpBootstrapError("project-mcp-bootstrap-copy-failed") from error


__all__ = [
    "BOOTSTRAP_RELATIVE",
    "TARGET_RELATIVE",
    "ProjectMcpBootstrapError",
    "deploy_project_mcp_bootstrap",
]
