"""Execution-bound adapters for one previously installed Project MCP package.

The functions here deliberately do not build an image, call Docker, read
Project settings, or create state.  They reopen the installed-package
admission immediately before handing a typed request to an injected execution
seam.  This makes a stale in-memory binding unusable as an execution token and
keeps checkout/source-root inputs outside the installed-runtime contract.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
import hashlib
from pathlib import Path, PurePosixPath
import re
from typing import Any, Literal

from framework_package import VerifiedFrameworkPackage
from installed_mcp_binding import (
    MCP_FILES,
    InstalledMcpBinding,
    InstalledMcpBindingError,
    admit_installed_mcp_binding,
)


SHA256 = re.compile(r"[0-9a-f]{64}\Z")
DockerImage = re.compile(r"sha256:[0-9a-f]{64}\Z")
RUNTIME_METADATA_RELATIVE = PurePosixPath(".caprmedio_runtime/runtime/project_mcp")
_TRANSPORTS = frozenset({"http", "stdio"})
_WORKSPACE = PurePosixPath("/workspace")


class InstalledMcpRuntimeError(RuntimeError):
    """A stable refusal from the installed-MCP execution boundary."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


@dataclass(frozen=True)
class InstalledMcpRuntime:
    """One fresh, immutable package admission prepared for one transport.

    ``metadata_root`` is a location descriptor only.  This adapter never
    creates it and does not treat it as execution proof.
    """

    transport: Literal["http", "stdio"]
    project_root: Path
    control_root: str
    target_context_sha256: str
    package_selector_sha256: str
    runtime_selector_sha256: str
    image: str
    compose_file: Path
    entrypoint_file: Path
    server_file: Path
    metadata_root: Path
    binding: InstalledMcpBinding


@dataclass(frozen=True)
class ProjectBindMount:
    """The sole host bind admitted for a stdio MCP container."""

    source: Path
    target: str = "/project"
    read_only: bool = False


@dataclass(frozen=True)
class StdioContainerRequest:
    """A non-publishing stdio container request with one selected Project bind.

    The receiving runner owns process creation.  The Project bind intentionally
    matches the package-admitted HTTP Compose carrier so the MCP can read its
    selected metadata and artifacts.  It is the only host bind: credentials,
    agent files, sockets, checkout/code roots, and additional paths are absent.
    """

    image: str
    entrypoint: tuple[str, ...]
    command: tuple[str, ...]
    entrypoint_file: Path
    server_file: Path
    environment: tuple[tuple[str, str], ...]
    stdin_attached: bool = True
    stdout_attached: bool = True
    network_mode: str = "none"
    published_ports: tuple[str, ...] = ()
    mounts: tuple[ProjectBindMount, ...] = ()
    read_only: bool = True
    cap_drop: tuple[str, ...] = ("ALL",)
    security_opt: tuple[str, ...] = ("no-new-privileges:true",)
    pids_limit: int = 128
    memory_limit: str = "512m"
    cpu_limit: int = 1


BindingAdmitter = Callable[..., InstalledMcpBinding]


def _refuse(code: str, message: str) -> None:
    raise InstalledMcpRuntimeError(code, message)


def _control_root(value: str | Path) -> str:
    if not isinstance(value, (str, Path)) or not str(value):
        _refuse("installed-mcp-control-invalid", "control root must name one direct Project child")
    candidate = PurePosixPath(str(value))
    if (
        candidate.is_absolute()
        or len(candidate.parts) != 1
        or candidate.name in {"", ".", ".."}
        or not candidate.name.startswith(".caprmedio_")
        or candidate.name == ".caprmedio_"
        or candidate.as_posix() != str(value)
    ):
        _refuse("installed-mcp-control-invalid", "control root must be one normalized direct control child")
    return candidate.as_posix()


def _raw_digest(value: object, *, code: str, label: str) -> str:
    if not isinstance(value, str) or SHA256.fullmatch(value) is None:
        _refuse(code, f"{label} must be a lowercase SHA-256")
    return value


def _docker_image(raw_digest: object) -> str:
    return "sha256:" + _raw_digest(raw_digest, code="installed-mcp-binding-invalid", label="binding image")


def _http_port(value: object) -> int | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 65535:
        _refuse("installed-mcp-port-invalid", "HTTP port must be an integer from 1 through 65535")
    return value


def _relative_package_file(root: Path, value: object, expected: str, label: str) -> Path:
    if not isinstance(value, Path) or not value.is_absolute() or value != root / expected:
        _refuse("installed-mcp-binding-invalid", f"binding {label} is not the exact package carrier")
    try:
        relative = value.relative_to(root)
    except ValueError as error:
        raise InstalledMcpRuntimeError("installed-mcp-binding-invalid", f"binding {label} escapes the package") from error
    if relative.as_posix() != expected:
        _refuse("installed-mcp-binding-invalid", f"binding {label} is not package-relative")
    return value


def _binding_paths(binding: InstalledMcpBinding, project_root: Path) -> tuple[Path, Path, Path]:
    if not isinstance(binding, InstalledMcpBinding):
        _refuse("installed-mcp-binding-invalid", "runtime requires an installed MCP binding")
    root = binding.package_root
    if not isinstance(root, Path) or not root.is_absolute() or root.is_symlink():
        _refuse("installed-mcp-binding-invalid", "binding package root is unavailable")
    manifest = _raw_digest(
        binding.package_manifest_sha256, code="installed-mcp-binding-invalid", label="package manifest",
    )
    if root != project_root / ".caprmedio_install" / "releases" / manifest:
        _refuse("installed-mcp-binding-invalid", "binding package root is not the selected installed release")
    compose = _relative_package_file(root, binding.compose_file, MCP_FILES[-1], "Compose file")
    entrypoint = _relative_package_file(root, root / MCP_FILES[4], MCP_FILES[4], "entrypoint")
    server = _relative_package_file(root, binding.mcp_server, MCP_FILES[1], "server")
    _relative_package_file(root, binding.mcp_http_server, MCP_FILES[0], "HTTP server")
    return compose, entrypoint, server


def _verify_expected_admission(runtime: InstalledMcpRuntime, *, package_selector_sha256: str | None,
                               runtime_selector_sha256: str | None,
                               compose_file: str | Path | None, image: str | None) -> None:
    if package_selector_sha256 is not None and package_selector_sha256 != runtime.package_selector_sha256:
        _refuse("installed-mcp-selector-mismatch", "caller package selector differs from the reopened selector")
    if runtime_selector_sha256 is not None and runtime_selector_sha256 != runtime.runtime_selector_sha256:
        _refuse("installed-mcp-selector-mismatch", "caller runtime selector differs from the reopened selector")
    if compose_file is not None:
        try:
            supplied_compose = Path(compose_file)
        except (TypeError, ValueError) as error:
            raise InstalledMcpRuntimeError("installed-mcp-compose-mismatch", "caller Compose carrier is invalid") from error
        if supplied_compose != runtime.compose_file:
            _refuse("installed-mcp-compose-mismatch", "caller Compose carrier differs from the installed package")
    if image is not None and image != runtime.image:
        _refuse("installed-mcp-image-mismatch", "caller image differs from the installed selector")


def reopen_installed_mcp_runtime(
    project_root: str | Path,
    control_root: str | Path,
    verified_package: VerifiedFrameworkPackage,
    *,
    target_context_sha256: str,
    transport: Literal["http", "stdio"],
    package_selector_sha256: str | None = None,
    runtime_selector_sha256: str | None = None,
    compose_file: str | Path | None = None,
    image: str | None = None,
    checkout_root: str | Path | None = None,
    source_root: str | Path | None = None,
    binding_admitter: BindingAdmitter = admit_installed_mcp_binding,
) -> InstalledMcpRuntime:
    """Reopen package, current selectors, context, Compose, and image for one use.

    Optional selector/Compose/image values are assertions, not overrides.  The
    actual values always come from a fresh ``admit_installed_mcp_binding``
    invocation.  ``checkout_root`` and ``source_root`` exist only to refuse
    legacy call sites explicitly; they can never select runtime code.
    """

    if transport not in _TRANSPORTS:
        _refuse("installed-mcp-transport-undesignated", "installed MCP transport is not designated")
    if checkout_root is not None:
        _refuse("installed-mcp-checkout-override-forbidden", "checkout roots cannot select an installed MCP runtime")
    if source_root is not None:
        _refuse("installed-mcp-source-override-forbidden", "source roots cannot select an installed MCP runtime")
    if not isinstance(verified_package, VerifiedFrameworkPackage):
        _refuse("installed-mcp-package-invalid", "runtime requires typed package verification")
    control = _control_root(control_root)
    context_digest = _raw_digest(target_context_sha256, code="installed-mcp-context-invalid", label="target context")
    if not callable(binding_admitter):
        _refuse("installed-mcp-admitter-invalid", "installed MCP binding admitter is unavailable")
    try:
        binding = binding_admitter(
            project_root, verified_package, target_context_sha256=context_digest,
        )
    except InstalledMcpBindingError as error:
        raise InstalledMcpRuntimeError(error.code, str(error)) from error
    except InstalledMcpRuntimeError:
        raise
    except Exception as error:
        raise InstalledMcpRuntimeError("installed-mcp-admission-failed", "installed MCP admission could not reopen") from error
    if binding.target_context.sha256 != context_digest:
        _refuse("installed-mcp-context-mismatch", "reopened target context differs from the selected context")
    if binding.target_context.control_child_relpath != control:
        _refuse("installed-mcp-control-mismatch", "selected control root differs from the reopened target context")
    root = binding.target_context.path.parents[3]
    try:
        supplied_root = Path(project_root)
    except (TypeError, ValueError) as error:
        raise InstalledMcpRuntimeError("installed-mcp-project-invalid", "Project root is invalid") from error
    if supplied_root != root:
        _refuse("installed-mcp-project-mismatch", "admitted target context does not belong to the selected Project")
    expected_context = root / ".caprmedio_runtime" / "installation" / "contexts" / f"{context_digest}.toml"
    if binding.target_context.path != expected_context:
        _refuse("installed-mcp-context-mismatch", "reopened target context carrier is outside the selected Project")
    compose, entrypoint, server = _binding_paths(binding, root)
    package_selector = _raw_digest(
        binding.package_selector_sha256, code="installed-mcp-binding-invalid", label="package selector",
    )
    runtime_selector = _raw_digest(
        binding.runtime_selector_sha256, code="installed-mcp-binding-invalid", label="runtime selector",
    )
    runtime = InstalledMcpRuntime(
        transport=transport,
        project_root=root,
        control_root=control,
        target_context_sha256=context_digest,
        package_selector_sha256=package_selector,
        runtime_selector_sha256=runtime_selector,
        image=_docker_image(binding.image_digest),
        compose_file=compose,
        entrypoint_file=entrypoint,
        server_file=server,
        metadata_root=root.joinpath(*RUNTIME_METADATA_RELATIVE.parts),
        binding=binding,
    )
    _verify_expected_admission(
        runtime,
        package_selector_sha256=package_selector_sha256,
        runtime_selector_sha256=runtime_selector_sha256,
        compose_file=compose_file,
        image=image,
    )
    return runtime


def _image_workspace_path(runtime: InstalledMcpRuntime, path: Path) -> str:
    try:
        relative = path.relative_to(runtime.binding.package_root)
    except ValueError as error:
        raise InstalledMcpRuntimeError("installed-mcp-binding-invalid", "runtime path escapes selected package") from error
    return str(_WORKSPACE / PurePosixPath(relative.as_posix()))


def _project_instance_id(runtime: InstalledMcpRuntime) -> str:
    """Match the explicit Project-selection identity without reading settings."""

    return hashlib.sha256(
        f"{runtime.project_root}\0{runtime.control_root}".encode("utf-8")
    ).hexdigest()


def stdio_container_request(runtime: InstalledMcpRuntime) -> StdioContainerRequest:
    """Describe the only permitted stdio execution carrier; do not execute it."""

    if not isinstance(runtime, InstalledMcpRuntime) or runtime.transport != "stdio":
        _refuse("installed-mcp-transport-mismatch", "stdio request requires a stdio runtime admission")
    if DockerImage.fullmatch(runtime.image) is None:
        _refuse("installed-mcp-image-mismatch", "stdio image is not immutable")
    return StdioContainerRequest(
        image=runtime.image,
        entrypoint=(
            "uv", "run", "--locked", "--no-sync", "--no-env-file",
            "--group", "rmed-workflow-mcp", "--group", "workflow-orchestrator",
            "python", _image_workspace_path(runtime, runtime.entrypoint_file),
        ),
        command=("mcp",),
        entrypoint_file=runtime.entrypoint_file,
        server_file=runtime.server_file,
        environment=(
            ("CAPRMEDIO_CONTROL_ROOT", runtime.control_root),
            ("CAPRMEDIO_PROJECT_INSTANCE_ID", _project_instance_id(runtime)),
            ("CAPRMEDIO_HOST_PROJECT_ROOT", str(runtime.project_root)),
        ),
        mounts=(ProjectBindMount(runtime.project_root),),
    )


def launch_installed_mcp_http(
    project_root: str | Path,
    control_root: str | Path,
    verified_package: VerifiedFrameworkPackage,
    *,
    target_context_sha256: str,
    launcher: object,
    package_selector_sha256: str | None = None,
    runtime_selector_sha256: str | None = None,
    compose_file: str | Path | None = None,
    image: str | None = None,
    port: int | None = None,
    checkout_root: str | Path | None = None,
    source_root: str | Path | None = None,
    binding_admitter: BindingAdmitter = admit_installed_mcp_binding,
) -> Any:
    """Reopen admission at the HTTP execution boundary and call only its seam.

    The launcher integration owns the implementation of ``launch_admitted``.
    It receives the fresh binding and selector-derived image plus an optional
    validated port assertion; this adapter never falls back to the legacy
    checkout-based ``launch`` method.
    """

    requested_port = _http_port(port)
    runtime = reopen_installed_mcp_runtime(
        project_root, control_root, verified_package,
        target_context_sha256=target_context_sha256,
        transport="http",
        package_selector_sha256=package_selector_sha256,
        runtime_selector_sha256=runtime_selector_sha256,
        compose_file=compose_file,
        image=image,
        checkout_root=checkout_root,
        source_root=source_root,
        binding_admitter=binding_admitter,
    )
    execute = getattr(launcher, "launch_admitted", None)
    if not callable(execute):
        _refuse("installed-mcp-http-seam-missing", "HTTP launcher has no admitted binding seam")
    return execute(
        project_root=runtime.project_root,
        control_root=runtime.control_root,
        binding=runtime.binding,
        image=runtime.image,
        port=requested_port,
    )


def run_installed_mcp_stdio(
    project_root: str | Path,
    control_root: str | Path,
    verified_package: VerifiedFrameworkPackage,
    *,
    target_context_sha256: str,
    runner: Callable[[StdioContainerRequest], Any],
    package_selector_sha256: str | None = None,
    runtime_selector_sha256: str | None = None,
    compose_file: str | Path | None = None,
    image: str | None = None,
    checkout_root: str | Path | None = None,
    source_root: str | Path | None = None,
    binding_admitter: BindingAdmitter = admit_installed_mcp_binding,
) -> Any:
    """Reopen admission and hand the Project-bind-only request to one runner."""

    if not callable(runner):
        _refuse("installed-mcp-stdio-runner-invalid", "stdio runner is unavailable")
    runtime = reopen_installed_mcp_runtime(
        project_root, control_root, verified_package,
        target_context_sha256=target_context_sha256,
        transport="stdio",
        package_selector_sha256=package_selector_sha256,
        runtime_selector_sha256=runtime_selector_sha256,
        compose_file=compose_file,
        image=image,
        checkout_root=checkout_root,
        source_root=source_root,
        binding_admitter=binding_admitter,
    )
    return runner(stdio_container_request(runtime))


__all__ = [
    "InstalledMcpRuntime",
    "InstalledMcpRuntimeError",
    "ProjectBindMount",
    "RUNTIME_METADATA_RELATIVE",
    "StdioContainerRequest",
    "launch_installed_mcp_http",
    "reopen_installed_mcp_runtime",
    "run_installed_mcp_stdio",
    "stdio_container_request",
]
