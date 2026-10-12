"""Direct CA-O-200 composition for one retained native runtime installation.

This module owns no new authority surface.  It composes the retained Full
Gate, direct-command, D601 stage, target Methodology, and common publisher
that already own their respective physical checks.  In particular, it does
not start an MCP server or retry a partially recorded installation.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import os
from pathlib import Path
import shutil
import stat
import tomllib

from framework_installation import (
    InstallationError,
    PortableInstallationRequest,
    verify_prospective_portable_full_gate,
)
from framework_package import verify_current_package_selector, verify_framework_package
from installation_context import bind_target_project_context
from installation_transaction import InstallationPublicationLock, InstallationTransactionError
from portable_methodology_installation import (
    prepare_target_portable_methodology_publication,
    reopen_prepared_target_portable_methodology_publication,
)
from portable_runtime_materialization import CandidateRuntimeCommandStageRequest
from portable_runtime_publication import (
    DirectPublishedRuntime,
    PreparedNativePublication,
    build_prepared_native_publication,
    execute_direct_native_runtime,
    render_package_selector,
    retained_publication_failure_reason,
)
from framework_installation_command import (
    FrameworkInstallationCommandRequest,
    FrameworkInstallationCommandResult,
    prepare_direct_full_gate_effect_closure,
    record_direct_installation_result,
    run_framework_installation_command,
)


_PACKAGE_SELECTOR = Path(".caprmedio_install/current.toml")
_NATIVE_RUNTIME_SELECTOR = Path(".caprmedio_runtime/installation/current.toml")
_LEGACY_RUNTIME_SELECTOR = Path(".caprmedio_runtime/framework/current.toml")
_LEGACY_TOOLS_SELECTOR = Path(".caprmedio_runtime/tools/current.toml")
_ENTRYPOINT = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/implementation_server.py"
_SHA256 = frozenset("0123456789abcdef")


class FrameworkRuntimeInstallationError(RuntimeError):
    """Stable refusal before an O200 installation effect begins."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


@dataclass(frozen=True)
class FrameworkRuntimeInstallationResult:
    """Actual O200 command plus its one non-replayed native publication result."""

    command: FrameworkInstallationCommandResult
    prepared: PreparedNativePublication | None
    publication: DirectPublishedRuntime


@dataclass(frozen=True)
class _PacketFacts:
    receipt_sha256: str
    image_digest: str


@dataclass(frozen=True)
class _Predecessor:
    # D598 selects a native Framework package.  A legacy Framework predecessor
    # has no D598 selector: its distinct Tools selection is captured only for
    # this pre-/under-lock stale check; the publisher reopens its proof itself.
    package_selector: bytes | None
    legacy_tool_selector: bytes | None
    execution_selector: tuple[Path, bytes] | None
    next_generation: int


def _refuse(code: str, message: str) -> None:
    raise FrameworkRuntimeInstallationError(code, message)


def _target_root(request: PortableInstallationRequest) -> Path:
    if not isinstance(request, PortableInstallationRequest):
        _refuse("runtime-installation-request-invalid", "runtime installation requires a typed portable request")
    try:
        root = Path(request.target.target_root)
        if not root.is_absolute() or ".." in root.parts:
            _refuse("runtime-installation-target-invalid", "target Project root must be an explicit absolute path")
        observed = root.lstat()
    except FrameworkRuntimeInstallationError:
        raise
    except (OSError, TypeError, ValueError) as error:
        raise FrameworkRuntimeInstallationError(
            "runtime-installation-target-invalid", "target Project root is unavailable"
        ) from error
    if root.is_symlink() or not stat.S_ISDIR(observed.st_mode):
        _refuse("runtime-installation-target-invalid", "target Project root is not a real directory")
    return root


def _optional_regular(root: Path, relative: Path, *, label: str) -> bytes | None:
    """Reopen one fixed current carrier without following an alias."""

    cursor = root
    try:
        for index, part in enumerate(relative.parts):
            cursor = cursor / part
            try:
                observed = os.lstat(cursor)
            except FileNotFoundError:
                return None
            expected = stat.S_ISREG if index == len(relative.parts) - 1 else stat.S_ISDIR
            if stat.S_ISLNK(observed.st_mode) or not expected(observed.st_mode):
                _refuse("runtime-installation-selector-invalid", f"{label} is aliased or has an invalid type")
        if observed.st_nlink != 1:
            _refuse("runtime-installation-selector-invalid", f"{label} is not an unaliased regular carrier")
        before = (observed.st_dev, observed.st_ino, observed.st_size, observed.st_mtime_ns)
        payload = cursor.read_bytes()
        after = cursor.stat()
        if before != (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns):
            _refuse("runtime-installation-selector-stale", f"{label} changed while being reopened")
        return payload
    except FrameworkRuntimeInstallationError:
        raise
    except OSError as error:
        raise FrameworkRuntimeInstallationError(
            "runtime-installation-selector-invalid", f"{label} is unavailable"
        ) from error


def _predecessor(root: Path) -> _Predecessor:
    """Read one closed native or legacy predecessor carrier set.

    Native state is the D598 package selector plus the D600 execution
    selector.  Pre-D600 state instead has the historic Framework and Tools
    selectors; the latter is captured separately so the under-lock reopen
    detects drift, and is never treated as a D598 selector.
    """

    package_selector = _optional_regular(root, _PACKAGE_SELECTOR, label="current reusable Framework-package selector")
    native_selector = _optional_regular(root, _NATIVE_RUNTIME_SELECTOR, label="current native execution selector")
    legacy_selector = _optional_regular(root, _LEGACY_RUNTIME_SELECTOR, label="current legacy Framework execution selector")
    legacy_tool_selector = _optional_regular(root, _LEGACY_TOOLS_SELECTOR, label="current legacy Tools selector")
    if native_selector is not None and legacy_selector is not None:
        _refuse(
            "runtime-installation-predecessor-ambiguous",
            "both native and legacy Framework execution selectors are current",
        )
    if native_selector is not None:
        if package_selector is None:
            _refuse(
                "runtime-installation-predecessor-incomplete",
                "current native Framework execution and D598 package selectors must be present together",
            )
    elif legacy_selector is not None:
        if package_selector is not None:
            _refuse(
                "runtime-installation-predecessor-ambiguous",
                "legacy Framework execution cannot be paired with a D598 package selector",
            )
        if legacy_tool_selector is None:
            _refuse(
                "runtime-installation-predecessor-incomplete",
                "current legacy Framework execution and Tools selectors must be present together",
            )
    elif package_selector is not None:
        _refuse(
            "runtime-installation-predecessor-incomplete",
            "current Framework execution and Tools-package selectors must be present together",
        )
    if native_selector is None and legacy_selector is None:
        return _Predecessor(
            package_selector=None,
            legacy_tool_selector=None,
            execution_selector=None,
            next_generation=1,
        )
    if native_selector is None:
        return _Predecessor(
            package_selector=None,
            legacy_tool_selector=legacy_tool_selector,
            execution_selector=(_LEGACY_RUNTIME_SELECTOR, legacy_selector),
            next_generation=1,
        )
    try:
        document = tomllib.loads(native_selector.decode("utf-8"))
        generation = document.get("state_generation") if isinstance(document, dict) else None
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise FrameworkRuntimeInstallationError(
            "runtime-installation-generation-invalid", "current native generation is not valid TOML"
        ) from error
    if type(generation) is not int or generation < 1:
        _refuse("runtime-installation-generation-invalid", "current native generation is not positive")
    return _Predecessor(
        package_selector=package_selector,
        legacy_tool_selector=None,
        execution_selector=(_NATIVE_RUNTIME_SELECTOR, native_selector),
        next_generation=generation + 1,
    )


def _packet_facts(request: PortableInstallationRequest) -> _PacketFacts:
    packet = request.full_gate_packet
    evidence = getattr(packet, "evidence", None)
    receipt = getattr(evidence, "receipt_sha256", None)
    image = getattr(evidence, "candidate_image_digest", None)
    if (
        not isinstance(receipt, str)
        or len(receipt) != 64
        or set(receipt) - _SHA256
        or not isinstance(image, str)
        or not image.startswith("sha256:")
        or len(image.removeprefix("sha256:")) != 64
        or set(image.removeprefix("sha256:")) - _SHA256
    ):
        _refuse("runtime-installation-full-gate-invalid", "retained Full Gate packet has no closed receipt and image identity")
    return _PacketFacts(receipt_sha256=receipt, image_digest=image)


def _actual_uv() -> Path:
    located = shutil.which("uv")
    if located is None:
        _refuse("runtime-installation-uv-unavailable", "package-owned runtime staging requires the actual uv executable")
    try:
        executable = Path(located).resolve(strict=True)
        observed = executable.lstat()
    except OSError as error:
        raise FrameworkRuntimeInstallationError(
            "runtime-installation-uv-unavailable", "actual uv executable cannot be reopened"
        ) from error
    if executable.is_symlink() or not stat.S_ISREG(observed.st_mode) or not observed.st_mode & 0o111:
        _refuse("runtime-installation-uv-unavailable", "actual uv executable is unsafe")
    return executable


def _record_blocked(
    command: FrameworkInstallationCommandResult,
    *,
    packet: object,
    state_generation: int,
    reason: str,
) -> DirectPublishedRuntime:
    """Record a pre-cut-over refusal against the same observed Full Gate."""

    closure = prepare_direct_full_gate_effect_closure(command, full_gate_packet=packet)
    recording = record_direct_installation_result(
        command,
        full_gate_effects=closure,
        state_generation=state_generation,
        effect_outcome="blocked_before_delete",
        reason=reason,
    )
    return DirectPublishedRuntime(publication=None, recording=recording)


def _failure_reason(error: BaseException) -> str:
    return retained_publication_failure_reason(error)


def install_framework_runtime(
    request: PortableInstallationRequest,
    *,
    command_id: str,
    operator: str,
) -> FrameworkRuntimeInstallationResult:
    """Run the one direct O200 composition without an implicit retry or start.

    All inputs are physically reopened before the direct Action begins.  Once
    that Action is started, preparation errors are retained as its actual
    ``blocked_before_delete`` result; callers receive that recorded outcome
    and must not replay the command automatically.
    """

    root = _target_root(request)
    try:
        context = bind_target_project_context(request.target)
        package = verify_framework_package(request.target.package_root)
    except (InstallationError, RuntimeError) as error:
        raise FrameworkRuntimeInstallationError(
            "runtime-installation-input-invalid", "target context or Framework package cannot be physically reopened"
        ) from error
    if (
        package.manifest_digest != context.package_evidence.package_manifest_sha256
        or package.source_catalog_sha256 != context.package_evidence.catalog_sha256
    ):
        _refuse("runtime-installation-package-mismatch", "target context does not bind the reopened Framework package")
    facts = _packet_facts(request)
    prospective_selector_bytes = render_package_selector(
        package,
        full_gate_receipt_sha256=facts.receipt_sha256,
        image_digest=facts.image_digest.removeprefix("sha256:"),
    )
    try:
        prospective_selector = verify_current_package_selector(prospective_selector_bytes, package)
        verified_receipt = verify_prospective_portable_full_gate(
            request,
            package=package,
            target_context=context,
            selector=prospective_selector,
        )
    except (InstallationError, RuntimeError) as error:
        raise FrameworkRuntimeInstallationError(
            "runtime-installation-full-gate-invalid", "retained native Full Gate cannot be physically reopened"
        ) from error
    if verified_receipt != facts.receipt_sha256:
        _refuse("runtime-installation-full-gate-stale", "reopened Full Gate receipt differs from its packet identity")
    predecessor = _predecessor(root)
    methodology = prepare_target_portable_methodology_publication(
        request,
        package=package,
        target_context=context,
        prospective_selector=prospective_selector,
    )
    uv = _actual_uv()

    command = run_framework_installation_command(
        FrameworkInstallationCommandRequest(
            target=request.target,
            target_context=context,
            package=package,
            full_gate_receipt_sha256=verified_receipt,
            command_id=command_id,
            operator=operator,
        )
    )
    action_run_id = command.action_start.get("run_id") if isinstance(command.action_start, dict) else None
    if not isinstance(action_run_id, str) or not action_run_id:
        _refuse("runtime-installation-command-invalid", "direct O200 command has no actual Action Run identity")
    nonce = hashlib.sha256(action_run_id.encode("utf-8")).hexdigest()

    try:
        lock = InstallationPublicationLock(
            root,
            target_context_sha256=command.target_context.sha256,
            owner_run_id=action_run_id,
            operation="install_framework_runtime",
            command_sha256=command.command_receipt.sha256,
        ).acquire()
    except (InstallationTransactionError, OSError, ValueError) as error:
        publication = _record_blocked(
            command,
            packet=request.full_gate_packet,
            state_generation=predecessor.next_generation,
            reason=_failure_reason(error),
        )
        return FrameworkRuntimeInstallationResult(command=command, prepared=None, publication=publication)
    try:
        try:
            current_predecessor = _predecessor(root)
            if current_predecessor != predecessor:
                _refuse("runtime-installation-predecessor-stale", "current predecessor changed after O200 command start")
            current_methodology = reopen_prepared_target_portable_methodology_publication(
                request,
                methodology,
                package=command.package,
                target_context=command.target_context,
                prospective_selector=prospective_selector,
            )
            stage_request = CandidateRuntimeCommandStageRequest(
                package=command.package,
                target_context=command.target_context,
                prospective_package_selector=prospective_selector_bytes,
                full_gate_packet=request.full_gate_packet,
                state_generation=current_predecessor.next_generation,
                entrypoint=_ENTRYPOINT,
                fixed_arguments=(
                    "--project-root",
                    "../../..",
                    "--control-root",
                    command.target_context.control_child_relpath,
                ),
                invocation_nonce=nonce,
                path_directories=(uv.parent,),
                home=Path.home().absolute(),
            )
            prepared = build_prepared_native_publication(
                request,
                package=command.package,
                target_context=command.target_context,
                installation_command_sha256=command.command_receipt.sha256,
                full_gate_packet=request.full_gate_packet,
                runtime_stage_request=stage_request,
                methodology_preparation=current_methodology,
                state_generation=current_predecessor.next_generation,
                old_package_selector=current_predecessor.package_selector,
                old_execution_selector=current_predecessor.execution_selector,
                lock=lock,
            )
        except (OSError, RuntimeError, ValueError) as error:
            publication = _record_blocked(
                command,
                packet=request.full_gate_packet,
                state_generation=predecessor.next_generation,
                reason=_failure_reason(error),
            )
            if publication.recording.get("state") == "recorded" and lock.active:
                lock.release("blocked")
            return FrameworkRuntimeInstallationResult(command=command, prepared=None, publication=publication)
        # The common executor is the sole classifier for a failure after it
        # begins publication; do not relabel one as pre-delete here.
        publication = execute_direct_native_runtime(command, prepared, lock=lock)
        return FrameworkRuntimeInstallationResult(command=command, prepared=prepared, publication=publication)
    finally:
        if lock.active:
            lock.close_uncertain()


__all__ = [
    "FrameworkRuntimeInstallationError",
    "FrameworkRuntimeInstallationResult",
    "install_framework_runtime",
]
