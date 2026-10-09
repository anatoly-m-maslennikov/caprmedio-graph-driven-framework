"""Public, installed-package-only Project MCP launcher.

This command accepts one explicit Project root and direct control child.  It
derives the package and target context exclusively from the installed D598/D599
selectors; it never accepts a checkout, source tree, package path, Compose
path, or image argument.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from typing import Any, Literal

from framework_package import (
    FrameworkPackageError,
    VerifiedFrameworkPackage,
    verify_current_package_selector,
    verify_framework_package,
)
from installed_mcp_binding import (
    INSTALL_CURRENT_RELATIVE,
    RUNTIME_CURRENT_RELATIVE,
    InstalledMcpBindingError,
    _PACKAGE_SELECTOR_KEYS,
    _RUNTIME_SELECTOR_KEYS,
    _parse_toml,
    _project_root,
    _regular_file,
    _sha256,
)
from installed_mcp_runtime import (
    InstalledMcpRuntimeError,
    ProjectBindMount,
    StdioContainerRequest,
    launch_installed_mcp_http,
    run_installed_mcp_stdio,
)


_SCHEMA_VERSION = 1
_IMAGE = re.compile(r"sha256:[0-9a-f]{64}\Z")
_STDIO_UV_PREFIX = (
    "uv", "run", "--locked", "--no-sync", "--no-env-file",
    "--group", "rmed-workflow-mcp", "--group", "workflow-orchestrator", "python",
)


class InstalledMcpCliError(RuntimeError):
    """A public installed-MCP CLI refusal without a fallback activation path."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


@dataclass(frozen=True)
class InstalledMcpCliInputs:
    """The exact selector-derived inputs handed into the runtime adapter."""

    project_root: Path
    package: VerifiedFrameworkPackage
    target_context_sha256: str


DockerTransport = Callable[[tuple[str, ...]], object]
LauncherFactory = Callable[[], object]


def _refuse(code: str, message: str) -> None:
    raise InstalledMcpCliError(code, message)


def _load_inputs(project_root: str | Path) -> InstalledMcpCliInputs:
    """Reopen the selected release and D598/D599 selector bytes read-only."""

    try:
        root = _project_root(project_root)
        _, package_selector_payload = _regular_file(
            root, INSTALL_CURRENT_RELATIVE,
            code="installed-cli-package-selector-missing", label="installed package selector",
        )
        package_selector = _parse_toml(
            package_selector_payload,
            code="installed-cli-package-selector-invalid", label="installed package selector",
        )
        if set(package_selector) != _PACKAGE_SELECTOR_KEYS or package_selector.get("schema_version") != _SCHEMA_VERSION:
            _refuse("installed-cli-package-selector-invalid", "installed package selector schema is not closed")
        manifest = _sha256(
            package_selector.get("package_manifest_sha256"),
            code="installed-cli-package-selector-invalid", label="installed package manifest",
        )
        if package_selector.get("release_relpath") != f"releases/{manifest}":
            _refuse("installed-cli-package-selector-invalid", "installed package selector release is not canonical")
        package_root = root / ".caprmedio_install" / "releases" / manifest
        package = verify_framework_package(package_root)
        verify_current_package_selector(package_selector_payload, package)

        _, runtime_selector_payload = _regular_file(
            root, RUNTIME_CURRENT_RELATIVE,
            code="installed-cli-runtime-selector-missing", label="installed runtime selector",
        )
        runtime_selector = _parse_toml(
            runtime_selector_payload,
            code="installed-cli-runtime-selector-invalid", label="installed runtime selector",
        )
        if set(runtime_selector) != _RUNTIME_SELECTOR_KEYS or runtime_selector.get("schema_version") != _SCHEMA_VERSION:
            _refuse("installed-cli-runtime-selector-invalid", "installed runtime selector schema is not closed")
        context = _sha256(
            runtime_selector.get("target_project_context_sha256"),
            code="installed-cli-runtime-selector-invalid", label="target Project context",
        )
        if runtime_selector.get("package_manifest_sha256") != package.manifest_digest:
            _refuse("installed-cli-runtime-selector-invalid", "runtime selector chooses another package")
        if runtime_selector.get("image_digest") != package_selector.get("image_digest"):
            _refuse("installed-cli-runtime-selector-invalid", "runtime selector image differs from package selector")
        return InstalledMcpCliInputs(root, package, context)
    except InstalledMcpCliError:
        raise
    except InstalledMcpBindingError as error:
        raise InstalledMcpCliError(error.code, str(error)) from error
    except FrameworkPackageError as error:
        raise InstalledMcpCliError(error.code, str(error)) from error


def _control_root(value: object) -> str:
    if not isinstance(value, str) or not value:
        _refuse("installed-cli-control-invalid", "control root is required")
    path = PurePosixPath(value)
    if (
        path.is_absolute() or len(path.parts) != 1 or path.name in {"", ".", ".."}
        or not path.name.startswith(".caprmedio_") or path.name == ".caprmedio_"
        or path.as_posix() != value
    ):
        _refuse("installed-cli-control-invalid", "control root must name one direct Project child")
    return value


def _default_launcher() -> object:
    docker = Path(__file__).resolve().parent.parent / "203_APPS" / "WORKFLOW_ORCHESTRATOR" / "docker"
    if str(docker) not in sys.path:
        sys.path.insert(0, str(docker))
    from project_mcp_launcher import Launcher

    return Launcher()


def _project_instance_id(project_root: Path, control_root: str) -> str:
    return hashlib.sha256(f"{project_root}\0{control_root}".encode("utf-8")).hexdigest()


def _stdio_docker_argv(request: StdioContainerRequest) -> tuple[str, ...]:
    """Translate exactly one validated adapter request into ``docker run`` argv."""

    if not isinstance(request, StdioContainerRequest):
        _refuse("installed-cli-stdio-invalid", "stdio runner requires an admitted request")
    if _IMAGE.fullmatch(request.image) is None:
        _refuse("installed-cli-stdio-invalid", "stdio request image is not immutable")
    if (
        not isinstance(request.entrypoint, tuple)
        or request.entrypoint[:len(_STDIO_UV_PREFIX)] != _STDIO_UV_PREFIX
        or len(request.entrypoint) != len(_STDIO_UV_PREFIX) + 1
    ):
        _refuse("installed-cli-stdio-invalid", "stdio request does not use the managed UV entrypoint")
    entrypoint_file = request.entrypoint[-1]
    if not isinstance(entrypoint_file, str) or not entrypoint_file.startswith("/workspace/"):
        _refuse("installed-cli-stdio-invalid", "stdio entrypoint is not package-owned")
    if not isinstance(request.command, tuple) or request.command != ("mcp",):
        _refuse("installed-cli-stdio-invalid", "stdio service command is not designated")
    if (
        request.stdin_attached is not True or request.stdout_attached is not True
        or request.network_mode != "none" or request.published_ports != ()
        or request.read_only is not True or request.cap_drop != ("ALL",)
        or request.security_opt != ("no-new-privileges:true",)
        or request.pids_limit != 128 or request.memory_limit != "512m" or request.cpu_limit != 1
    ):
        _refuse("installed-cli-stdio-invalid", "stdio resource or network contract differs from admission")
    if not isinstance(request.mounts, tuple) or len(request.mounts) != 1 or not isinstance(request.mounts[0], ProjectBindMount):
        _refuse("installed-cli-stdio-invalid", "stdio request must have one selected Project bind")
    mount = request.mounts[0]
    try:
        source = mount.source
        if (
            not isinstance(source, Path) or not source.is_absolute() or source.is_symlink()
            or not source.is_dir() or source.resolve(strict=True) != source
            or mount.target != "/project" or mount.read_only is not False
        ):
            _refuse("installed-cli-stdio-invalid", "stdio Project bind differs from the admitted target")
    except InstalledMcpCliError:
        raise
    except (OSError, ValueError) as error:
        raise InstalledMcpCliError("installed-cli-stdio-invalid", "stdio Project bind is unavailable") from error
    source_text = str(source)
    if "," in source_text or any(ord(character) < 32 or ord(character) == 127 for character in source_text):
        _refuse("installed-cli-stdio-invalid", "stdio Project bind cannot be serialized safely")
    if not isinstance(request.environment, tuple) or len(request.environment) != 3:
        _refuse("installed-cli-stdio-invalid", "stdio environment is not the selected Project identity")
    if any(
        not isinstance(pair, tuple) or len(pair) != 2
        or not isinstance(pair[0], str) or not isinstance(pair[1], str)
        for pair in request.environment
    ):
        _refuse("installed-cli-stdio-invalid", "stdio environment is malformed")
    environment = dict(request.environment)
    if len(environment) != 3 or set(environment) != {
        "CAPRMEDIO_CONTROL_ROOT", "CAPRMEDIO_PROJECT_INSTANCE_ID", "CAPRMEDIO_HOST_PROJECT_ROOT",
    }:
        _refuse("installed-cli-stdio-invalid", "stdio environment has an unadmitted carrier")
    control = _control_root(environment["CAPRMEDIO_CONTROL_ROOT"])
    if (
        environment["CAPRMEDIO_HOST_PROJECT_ROOT"] != str(source)
        or environment["CAPRMEDIO_PROJECT_INSTANCE_ID"] != _project_instance_id(source, control)
    ):
        _refuse("installed-cli-stdio-invalid", "stdio environment does not bind the selected Project")
    argv = [
        "docker", "run", "--rm", "--interactive", "--init", "--read-only",
        "--tmpfs", "/tmp:size=128m,mode=1777",
        "--pids-limit", "128", "--memory", "512m", "--cpus", "1",
        "--cap-drop", "ALL", "--security-opt", "no-new-privileges:true",
        "--network", "none",
        "--mount", f"type=bind,src={source_text},dst=/project",
    ]
    for name, value in request.environment:
        argv.extend(("--env", f"{name}={value}"))
    argv.extend(("--entrypoint", "uv", request.image, *request.entrypoint[1:], *request.command))
    return tuple(argv)


def _subprocess_transport(argv: tuple[str, ...]) -> int:
    """Run one foreground stdio container with inherited standard streams."""

    completed = subprocess.run(argv, check=False, shell=False)
    return completed.returncode


def docker_stdio_runner(request: StdioContainerRequest, *, transport: DockerTransport = _subprocess_transport) -> int:
    """Run one verified stdio request without ports, secret inputs, or fallbacks."""

    if not callable(transport):
        _refuse("installed-cli-docker-transport-invalid", "Docker transport is unavailable")
    argv = _stdio_docker_argv(request)
    try:
        outcome = transport(argv)
    except OSError as error:
        raise InstalledMcpCliError("installed-cli-docker-failed", "Docker stdio transport could not start") from error
    if isinstance(outcome, bool) or not isinstance(outcome, int):
        _refuse("installed-cli-docker-invalid", "Docker stdio transport did not return an exit status")
    if outcome != 0:
        _refuse("installed-cli-docker-failed", "Docker stdio transport failed")
    return outcome


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True, help="canonical target Project root")
    parser.add_argument("--control-root", required=True, help="one direct .caprmedio_* Project child")
    parser.add_argument("--mode", choices=("http", "stdio"), default="http")
    parser.add_argument("--port", type=int, help="optional HTTP loopback port override")
    return parser


def run_installed_mcp_cli(
    argv: Sequence[str] | None = None,
    *,
    launcher_factory: LauncherFactory = _default_launcher,
    docker_transport: DockerTransport = _subprocess_transport,
) -> Any:
    """Verify selector-owned installed state before the single selected effect."""

    args = build_parser().parse_args(argv)
    control = _control_root(args.control_root)
    inputs = _load_inputs(args.project_root)
    if args.mode == "http":
        if not callable(launcher_factory):
            _refuse("installed-cli-launcher-invalid", "HTTP launcher factory is unavailable")
        launcher = launcher_factory()
        return launch_installed_mcp_http(
            inputs.project_root, control, inputs.package,
            target_context_sha256=inputs.target_context_sha256,
            launcher=launcher, port=args.port,
        )
    if args.port is not None:
        _refuse("installed-cli-port-mode-invalid", "--port is only valid for HTTP mode")
    return run_installed_mcp_stdio(
        inputs.project_root, control, inputs.package,
        target_context_sha256=inputs.target_context_sha256,
        runner=lambda request: docker_stdio_runner(request, transport=docker_transport),
    )


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point.  HTTP prints a safe launcher result; stdio owns stdout."""

    try:
        result = run_installed_mcp_cli(argv)
    except (InstalledMcpCliError, InstalledMcpBindingError, InstalledMcpRuntimeError, FrameworkPackageError) as error:
        print(f"{getattr(error, 'code', 'installed-cli-failed')}: {error}", file=sys.stderr)
        return 2
    if isinstance(result, Mapping):
        print(json.dumps(dict(result), sort_keys=True, separators=(",", ":")))
    return 0


__all__ = [
    "InstalledMcpCliError",
    "InstalledMcpCliInputs",
    "build_parser",
    "docker_stdio_runner",
    "main",
    "run_installed_mcp_cli",
]


if __name__ == "__main__":  # pragma: no cover - exercised through the package-owned UV command.
    raise SystemExit(main())
