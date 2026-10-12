"""Closed Project-MCP binding for direct CA-O-200 runtime installation.

This transport boundary owns only the fixed-Project request shape and the
physical reopening needed to turn a documentary native Full Gate packet into
the existing typed installation request.  The reusable installer remains the
sole owner of O200 start, locking, staging, publication, quiescence and
terminal recording.
"""

from __future__ import annotations

import os
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
import stat
import sys
import tomllib
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, JsonValue, RootModel, TypeAdapter, ValidationError


_TOOLS_ROOT = Path(__file__).resolve().parents[1] / "201_TOOLS"
_RELEASE_ROOT = _TOOLS_ROOT / "RELEASE_VERSION"
for _path in (_TOOLS_ROOT, _RELEASE_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from framework_installation import PortableInstallationRequest  # noqa: E402
from framework_package import FrameworkPackageError, provide_installation_package_evidence, verify_framework_package  # noqa: E402
from framework_runtime_installation import (  # noqa: E402
    FrameworkRuntimeInstallationResult,
    install_framework_runtime,
)
from installation_context import TargetProjectRequest  # noqa: E402
from operator_registry import OperatorRegistryError, parse_operators_registry  # noqa: E402
from project_selection import ProjectSelection, ProjectSelectionError, active_selection  # noqa: E402
from retained_full_gate_packet import RetainedNativeFullGatePacket  # noqa: E402
import work_journal  # noqa: E402


MCP_NAME = "install_framework_runtime"
TOOL_NAME = "INSTALL_FRAMEWORK_RUNTIME"
ACTION_ID = "CA-O-200"
DELIVERY_ID = "CA-D-620"
ENTRYPOINT = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/framework_runtime_installation_mcp.py"

_COMMAND_ID_PATTERN = r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,159}$"
_SHA256_LENGTH = 64
_READ_LIMIT = 8 * 1024 * 1024
_RUNTIME_SELECTOR = PurePosixPath(".caprmedio_runtime/installation/current.toml")
_CONTEXTS_ROOT = PurePosixPath(".caprmedio_runtime/installation/contexts")
_SECRET_COMPONENTS = frozenset({"secrets", "credentials", "private_settings"})
_RESULT_OUTCOMES = frozenset(
    {"completed", "blocked_before_delete", "unavailable_after_delete", "effect_uncertain"}
)


class FrameworkRuntimeInstallationMcpError(RuntimeError):
    """Stable refusal before this adapter can delegate an O200 effect."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


class _ClosedRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


class ExecuteRequest(_ClosedRequest):
    """The sole public request variant declared by CA-D-620."""

    operation: Literal["execute"]
    command_id: str = Field(pattern=_COMMAND_ID_PATTERN)
    operator: str = Field(min_length=1, max_length=512)
    native_packet: dict[str, JsonValue]


_REQUESTS = TypeAdapter(ExecuteRequest)


class FrameworkRuntimeInstallationRequest(RootModel[ExecuteRequest]):
    """Canonical transport-neutral request model for the O200 Tool."""


class McpActivation(BaseModel):
    """Declared image-recreation handoff after one fully recorded installation."""

    model_config = ConfigDict(extra="forbid", strict=True)

    schema_version: Literal[1]
    kind: Literal["image_recreation"]
    request_id: str


class FrameworkRuntimeInstallationToolResult(BaseModel):
    """Closed structured result emitted by the O200 transport adapter."""

    model_config = ConfigDict(extra="forbid", strict=True)

    operation: Literal["execute"]
    effect_outcome: Literal[
        "completed", "blocked_before_delete", "unavailable_after_delete", "effect_uncertain"
    ]
    recording_state: Literal["recorded", "recording_pending"]
    result_ref: str
    mcp_activation: McpActivation | None = None


@dataclass(frozen=True)
class _NativeTargetFacts:
    repository_identity: str | bool
    root_locator: str


PacketReader = Callable[[str | Path, Mapping[str, Any]], RetainedNativeFullGatePacket]
Installer = Callable[..., FrameworkRuntimeInstallationResult]
SelectionResolver = Callable[[str | Path], ProjectSelection]


def _refuse(code: str, message: str) -> None:
    raise FrameworkRuntimeInstallationMcpError(code, message)


def _root(value: str | Path) -> Path:
    supplied = Path(value)
    try:
        root = supplied.resolve(strict=True)
        observed = supplied.lstat()
    except (OSError, TypeError, ValueError) as error:
        raise FrameworkRuntimeInstallationMcpError(
            "framework-runtime-installation-mcp-root-invalid", "server Project root is unavailable"
        ) from error
    if stat.S_ISLNK(observed.st_mode) or root.is_symlink() or not root.is_dir():
        _refuse("framework-runtime-installation-mcp-root-invalid", "server Project root is unsafe")
    return root


def _packet_relative(value: object, *, field: str) -> Path:
    """Accept one canonical, non-secret Project-relative packet locator."""

    if not isinstance(value, str) or not value or "\\" in value:
        _refuse("framework-runtime-installation-mcp-packet-invalid", f"{field} must be a safe Project-relative path")
    parsed = PurePosixPath(value)
    if (
        parsed.is_absolute()
        or parsed == PurePosixPath(".")
        or parsed.as_posix() != value
        or any(part in {"", ".", ".."} for part in parsed.parts)
        or any(part.lower().startswith(".env") or part.lower().endswith(".env") or part.lower() in _SECRET_COMPONENTS for part in parsed.parts)
    ):
        _refuse("framework-runtime-installation-mcp-packet-invalid", f"{field} is protected or non-canonical")
    return Path(*parsed.parts)


def _bounded_regular(root: Path, relative: Path, *, label: str, optional: bool = False) -> bytes | None:
    """Read one fixed regular carrier without aliases or an unbounded payload."""

    cursor = root
    try:
        for index, part in enumerate(relative.parts):
            cursor = cursor / part
            try:
                observed = os.lstat(cursor)
            except FileNotFoundError:
                if optional:
                    return None
                raise
            if stat.S_ISLNK(observed.st_mode):
                _refuse("framework-runtime-installation-mcp-input-invalid", f"{label} has a symlinked ancestor")
            if index < len(relative.parts) - 1 and not stat.S_ISDIR(observed.st_mode):
                _refuse("framework-runtime-installation-mcp-input-invalid", f"{label} has an invalid ancestor")
        flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(cursor, flags)
    except FrameworkRuntimeInstallationMcpError:
        raise
    except OSError as error:
        raise FrameworkRuntimeInstallationMcpError(
            "framework-runtime-installation-mcp-input-unavailable", f"{label} is unavailable"
        ) from error
    try:
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode) or before.st_size > _READ_LIMIT:
            _refuse("framework-runtime-installation-mcp-input-invalid", f"{label} is not a bounded regular file")
        payload = bytearray()
        while len(payload) <= _READ_LIMIT:
            chunk = os.read(descriptor, min(8192, _READ_LIMIT + 1 - len(payload)))
            if not chunk:
                break
            payload.extend(chunk)
        after = os.fstat(descriptor)
        if (
            len(payload) > _READ_LIMIT
            or before.st_dev != after.st_dev
            or before.st_ino != after.st_ino
            or before.st_size != after.st_size
            or len(payload) != before.st_size
        ):
            _refuse("framework-runtime-installation-mcp-input-invalid", f"{label} changed while being read")
        return bytes(payload)
    except FrameworkRuntimeInstallationMcpError:
        raise
    except OSError as error:
        raise FrameworkRuntimeInstallationMcpError(
            "framework-runtime-installation-mcp-input-unavailable", f"{label} is unreadable"
        ) from error
    finally:
        os.close(descriptor)


def _preflight_packet_path(root: Path, relative: Path, *, field: str) -> None:
    """Reject missing, special, or symlinked packet locators before decoding."""

    cursor = root
    try:
        for index, part in enumerate(relative.parts):
            cursor = cursor / part
            observed = os.lstat(cursor)
            if stat.S_ISLNK(observed.st_mode):
                _refuse("framework-runtime-installation-mcp-packet-invalid", f"{field} has a symlinked ancestor")
            if index < len(relative.parts) - 1 and not stat.S_ISDIR(observed.st_mode):
                _refuse("framework-runtime-installation-mcp-packet-invalid", f"{field} has an invalid ancestor")
        if not (stat.S_ISREG(observed.st_mode) or stat.S_ISDIR(observed.st_mode)):
            _refuse("framework-runtime-installation-mcp-packet-invalid", f"{field} has an unsupported file type")
    except FrameworkRuntimeInstallationMcpError:
        raise
    except OSError as error:
        raise FrameworkRuntimeInstallationMcpError(
            "framework-runtime-installation-mcp-packet-unavailable", f"{field} is unavailable"
        ) from error


def _preflight_packet_value(root: Path, value: object, *, field: str = "native_packet") -> None:
    """Walk documentary JSON only to harden every tagged ``path`` before read.

    The existing release-checkpoint codec continues to own the native-packet
    grammar.  This walk neither interprets nor rebuilds its types; it merely
    makes every possible packet path safe before that codec can open it.
    """

    if isinstance(value, Mapping):
        kind = value.get("type")
        if kind == "path":
            _preflight_packet_path(root, _packet_relative(value.get("value"), field=field), field=field)
        for key, child in value.items():
            _preflight_packet_value(root, child, field=f"{field}.{key}")
        return
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for index, child in enumerate(value):
            _preflight_packet_value(root, child, field=f"{field}[{index}]")


def read_native_packet(root: str | Path, native_packet: Mapping[str, Any]) -> RetainedNativeFullGatePacket:
    """Safely delegate the closed native packet codec and detached verifier.

    This is the deliberately narrow public reader for CA-D-620.  It performs
    no packet grammar fork: after path/secret/alias preflight it delegates to
    :func:`release_checkpoint._load_native_packet`, which owns the exact
    documentary codec and Full Gate verification.
    """

    project_root = _root(root)
    if not isinstance(native_packet, Mapping):
        _refuse("framework-runtime-installation-mcp-packet-invalid", "native_packet must be a JSON object")
    _preflight_packet_value(project_root, native_packet)
    try:
        from release_checkpoint import _load_native_packet

        packet = _load_native_packet(dict(native_packet), str(project_root))
    except FrameworkRuntimeInstallationMcpError:
        raise
    except Exception as error:
        raise FrameworkRuntimeInstallationMcpError(
            "framework-runtime-installation-mcp-packet-invalid",
            "native_packet cannot be physically decoded and verified",
        ) from error
    if type(packet) is not RetainedNativeFullGatePacket:
        _refuse("framework-runtime-installation-mcp-packet-invalid", "native_packet codec returned an unsupported packet")
    return packet


def _registered_operator(root: Path, selection: ProjectSelection, operator: str) -> None:
    """Reopen the exact current selected Operator registry before decoding."""

    if not isinstance(operator, str) or not operator.strip() or "\x00" in operator or "\n" in operator or "\r" in operator:
        _refuse("framework-runtime-installation-mcp-operator-invalid", "Operator is invalid")
    registry_relative = selection.control_relative / "operators_registry.toml"
    payload = _bounded_regular(root, registry_relative, label="registered Operator evidence")
    assert payload is not None
    try:
        records = parse_operators_registry(payload)
    except OperatorRegistryError as error:
        raise FrameworkRuntimeInstallationMcpError(
            "framework-runtime-installation-mcp-operator-invalid", "registered Operator evidence is invalid"
        ) from error
    matching = [record for record in records if record.name == operator]
    if len(matching) != 1:
        _refuse("framework-runtime-installation-mcp-operator-invalid", "Operator is not uniquely registered for this Project")
    author = matching[0].journal_author
    if author is None and work_journal.AUTHOR_RE.fullmatch(matching[0].name):
        author = matching[0].name
    if author is None:
        _refuse("framework-runtime-installation-mcp-operator-invalid", "Operator has no explicit Journal author mapping")


def _current_native_target_facts(root: Path) -> _NativeTargetFacts:
    """Return authenticated historical repository/root facts when native exists."""

    selector_payload = _bounded_regular(root, Path(*_RUNTIME_SELECTOR.parts), label="current native runtime selector", optional=True)
    if selector_payload is None:
        return _NativeTargetFacts(repository_identity=False, root_locator=root.name)
    try:
        from installed_mcp_binding import _RUNTIME_SELECTOR_KEYS, _context

        selector = tomllib.loads(selector_payload.decode("utf-8"))
        if (
            not isinstance(selector, dict)
            or set(selector) != _RUNTIME_SELECTOR_KEYS
            or selector.get("schema_version") != 1
            or not isinstance(selector.get("target_project_context_sha256"), str)
            or len(selector["target_project_context_sha256"]) != _SHA256_LENGTH
            or set(selector["target_project_context_sha256"]) - frozenset("0123456789abcdef")
        ):
            _refuse("framework-runtime-installation-mcp-native-context-invalid", "current native context selector is invalid")
        digest = selector["target_project_context_sha256"]
        # This existing reader validates the exact digest-named D600 bytes and
        # current controls.  Its compact returned view intentionally omits the
        # two facts CA-D-620 must preserve, so read those already-authenticated
        # bytes below and re-open the same carrier again afterwards.
        _context(root, digest)
        context_payload = _bounded_regular(
            root,
            Path(*_CONTEXTS_ROOT.parts, f"{digest}.toml"),
            label="current native target context",
        )
        assert context_payload is not None
        context = tomllib.loads(context_payload.decode("utf-8"))
        repository_identity = context.get("repository_identity") if isinstance(context, dict) else None
        root_locator = context.get("root_locator") if isinstance(context, dict) else None
        if (
            repository_identity is not False
            and (
                not isinstance(repository_identity, str)
                or len(repository_identity) != _SHA256_LENGTH
                or set(repository_identity) - frozenset("0123456789abcdef")
            )
        ):
            _refuse("framework-runtime-installation-mcp-native-context-invalid", "current native repository identity is invalid")
        if (
            not isinstance(root_locator, str)
            or not root_locator
            or "\\" in root_locator
            or "\x00" in root_locator
            or PurePosixPath(root_locator).is_absolute()
            or PurePosixPath(root_locator).as_posix() != root_locator
            or any(part in {"", ".", ".."} for part in PurePosixPath(root_locator).parts)
        ):
            _refuse("framework-runtime-installation-mcp-native-context-invalid", "current native root locator is invalid")
        _context(root, digest)
        return _NativeTargetFacts(repository_identity=repository_identity, root_locator=root_locator)
    except FrameworkRuntimeInstallationMcpError:
        raise
    except Exception as error:
        raise FrameworkRuntimeInstallationMcpError(
            "framework-runtime-installation-mcp-native-context-invalid",
            "current native target context cannot be reopened",
        ) from error


def _packet_package(root: Path, packet: RetainedNativeFullGatePacket):
    """Reopen the packet's exact package; never substitute a latest package."""

    try:
        retained = packet.retained_candidate
        view = retained.package_evidence.view
        package = verify_framework_package(view.package_root)
    except (AttributeError, FrameworkPackageError, OSError, TypeError, ValueError) as error:
        raise FrameworkRuntimeInstallationMcpError(
            "framework-runtime-installation-mcp-package-invalid", "packet package cannot be physically reopened"
        ) from error
    try:
        relative = package.root.relative_to(root)
    except ValueError as error:
        raise FrameworkRuntimeInstallationMcpError(
            "framework-runtime-installation-mcp-package-invalid", "packet package escapes the fixed Project"
        ) from error
    _preflight_packet_path(root, relative, field="native_packet.package_root")
    evidence = packet.evidence
    if (
        view.actual_package_manifest_sha256 != package.manifest_digest
        or view.source_catalog_sha256 != package.source_catalog_sha256
        or view.framework_version != package.framework_version
        or view.version_toml_sha256 != package.version_toml_sha256
        or evidence.package_manifest_sha256 != package.manifest_digest
        or evidence.source_catalog_sha256 != package.source_catalog_sha256
        or evidence.framework_version != package.framework_version
        or evidence.version_toml_sha256 != package.version_toml_sha256
    ):
        _refuse("framework-runtime-installation-mcp-package-mismatch", "packet evidence differs from its reopened package")
    return package


def _fixed_installation_request(
    root: Path,
    selection: ProjectSelection,
    packet: RetainedNativeFullGatePacket,
) -> PortableInstallationRequest:
    """Construct only the fixed Project's typed reusable-installer request."""

    if selection.root != root or selection.control_root != root / selection.control_relative:
        _refuse("framework-runtime-installation-mcp-selection-invalid", "fixed Project selection differs from server root")
    project = selection.settings.get("project")
    identity = project.get("name") if isinstance(project, Mapping) else None
    if not isinstance(identity, str) or not identity.strip():
        _refuse("framework-runtime-installation-mcp-selection-invalid", "current Project Settings have no target identity")
    package = _packet_package(root, packet)
    facts = _current_native_target_facts(root)
    try:
        evidence = provide_installation_package_evidence(package.root)
        target = TargetProjectRequest(
            target_root=root,
            control_child=selection.control_relative.as_posix(),
            mode="adopt",
            target_project_identity=identity,
            settings_path=selection.control_root / "caprmedio_project_settings.toml",
            project_structure_path=selection.control_root / "project_structure.toml",
            operators_registry_path=selection.control_root / "operators_registry.toml",
            repository_identity=facts.repository_identity,
            root_locator=facts.root_locator,
            package_root=package.root,
            package_evidence=evidence,
        )
        evidence_root = _packet_relative(packet.evidence.evidence_root, field="native_packet.evidence_root")
        receipt = packet.artifact_root.joinpath(*evidence_root.parts, "receipt.json")
        return PortableInstallationRequest(target=target, retained_gate_receipt_path=receipt, full_gate_packet=packet)
    except FrameworkRuntimeInstallationMcpError:
        raise
    except (AttributeError, FrameworkPackageError, OSError, TypeError, ValueError) as error:
        raise FrameworkRuntimeInstallationMcpError(
            "framework-runtime-installation-mcp-input-invalid", "fixed Project installation request cannot be built"
        ) from error


def _actual_result_transport(value: object) -> dict[str, str]:
    """Expose only a real retained result's outcome and recording identity."""

    recording = getattr(getattr(value, "publication", None), "recording", None)
    if not isinstance(recording, Mapping) or set(recording) != {"state", "result_ref", "result", "terminal"}:
        _refuse("framework-runtime-installation-mcp-result-invalid", "installer returned no closed recording")
    state = recording.get("state")
    result_ref = recording.get("result_ref")
    result = recording.get("result")
    terminal = recording.get("terminal")
    if (
        not isinstance(state, str)
        or state not in {"recorded", "recording_pending"}
        or not isinstance(result_ref, str)
        or not isinstance(result, Mapping)
    ):
        _refuse("framework-runtime-installation-mcp-result-invalid", "installer recording is invalid")
    if state == "recorded" and not isinstance(terminal, Mapping):
        _refuse("framework-runtime-installation-mcp-result-invalid", "recorded installation has no terminal result")
    if state == "recording_pending" and terminal is not None:
        _refuse("framework-runtime-installation-mcp-result-invalid", "pending installation has a contradictory terminal result")
    _packet_relative(result_ref, field="installer result_ref")
    outcome = result.get("effect_outcome")
    if not isinstance(outcome, str) or outcome not in _RESULT_OUTCOMES:
        _refuse("framework-runtime-installation-mcp-result-invalid", "installer effect outcome is invalid")
    return {
        "operation": "execute",
        "effect_outcome": outcome,
        "recording_state": state,
        "result_ref": result_ref,
    }


class FrameworkRuntimeInstallationAdapter:
    """One fixed-Project CA-O-200 transport adapter.

    The optional callables are construction-only test seams.  They are not
    MCP request fields and production registration always uses the physical
    packet reader, Project selection, and reusable installer above.
    """

    def __init__(
        self,
        root: str | Path,
        *,
        packet_reader: PacketReader = read_native_packet,
        installer: Installer = install_framework_runtime,
        selection_resolver: SelectionResolver = active_selection,
    ) -> None:
        self.root = _root(root)
        if not callable(packet_reader) or not callable(installer) or not callable(selection_resolver):
            _refuse("framework-runtime-installation-mcp-host-invalid", "adapter dependencies are unavailable")
        self._packet_reader = packet_reader
        self._installer = installer
        self._selection_resolver = selection_resolver

    def invoke(self, request: Mapping[str, Any] | ExecuteRequest) -> dict[str, Any]:
        try:
            parsed = request if isinstance(request, ExecuteRequest) else _REQUESTS.validate_python(request)
        except ValidationError as error:
            raise FrameworkRuntimeInstallationMcpError(
                "framework-runtime-installation-mcp-request-invalid", "request has an invalid closed schema"
            ) from error
        try:
            selection = self._selection_resolver(self.root)
        except (ProjectSelectionError, OSError, RuntimeError, TypeError, ValueError) as error:
            raise FrameworkRuntimeInstallationMcpError(
                "framework-runtime-installation-mcp-selection-invalid", "fixed Project selection is unavailable"
            ) from error
        if not isinstance(selection, ProjectSelection):
            _refuse("framework-runtime-installation-mcp-selection-invalid", "fixed Project selection is invalid")
        _registered_operator(self.root, selection, parsed.operator)
        packet = self._packet_reader(self.root, parsed.native_packet)
        if type(packet) is not RetainedNativeFullGatePacket:
            _refuse("framework-runtime-installation-mcp-packet-invalid", "packet reader returned an unsupported packet")
        installation = _fixed_installation_request(self.root, selection, packet)
        try:
            result = self._installer(installation, command_id=parsed.command_id, operator=parsed.operator)
        except FrameworkRuntimeInstallationMcpError:
            raise
        except Exception as error:
            # CA-D-620 has no retry path.  The actual installer owns any
            # started Action's recording; this adapter only reports refusal.
            raise FrameworkRuntimeInstallationMcpError(
                "framework-runtime-installation-mcp-execute-refused", "direct Framework installation was refused"
            ) from error
        transport = _actual_result_transport(result)
        if transport["effect_outcome"] == "completed" and transport["recording_state"] == "recorded":
            # A completed O200 publishes an immutable image.  The parent
            # gateway must not pretend its image-local implementation changed;
            # its existing launcher/recreation path owns that handoff.
            transport["mcp_activation"] = {
                "schema_version": 1, "kind": "image_recreation", "request_id": parsed.command_id,
            }
        return transport


class _DescriptorAdapter:
    """Uniform descriptor wrapper; the native adapter remains the invoker."""

    def __init__(self, root: str | Path) -> None:
        self._adapter = FrameworkRuntimeInstallationAdapter(root)

    def invoke(
        self,
        request: FrameworkRuntimeInstallationRequest | ExecuteRequest | Mapping[str, Any],
    ) -> dict[str, Any]:
        return self._adapter.invoke(
            request.root if isinstance(request, FrameworkRuntimeInstallationRequest) else request
        )


def create_adapter(root: str | Path) -> _DescriptorAdapter:
    """Create the sole root-bound adapter used by descriptor-driven providers."""

    return _DescriptorAdapter(root)


def describe_tool() -> dict[str, Any]:
    """Describe O200 without opening carriers, invoking it, or causing an effect."""

    return {
        "schema_version": 1,
        "identity": {
            "name": TOOL_NAME,
            "tool_version": 1,
            "title": "Install Framework runtime",
            "description": "Execute the source-bound CA-O-200 Framework runtime installation Action.",
            "purpose": "Install the Framework runtime only through the existing direct Action boundary.",
        },
        "binding": {
            "delivery_atom_id": DELIVERY_ID,
            "action_ids": [ACTION_ID],
            "implementation_entrypoint": ENTRYPOINT,
        },
        "models": {
            "input": {"module": ENTRYPOINT, "symbol": "FrameworkRuntimeInstallationRequest"},
            "output": {"module": ENTRYPOINT, "symbol": "FrameworkRuntimeInstallationToolResult"},
        },
        "callable": {"module": ENTRYPOINT, "symbol": "create_adapter"},
        "effect_hints": {
            "read_only_hint": False,
            "destructive_hint": True,
            "idempotent_hint": False,
            "open_world_hint": False,
        },
        "permissions": {
            "execution": "operator_authorized",
            "enforcement": "canonical_action_boundary",
            "metadata_grants_permission": False,
        },
        "source_pins": {"delivery_atom_id": DELIVERY_ID, "action_ids": [ACTION_ID]},
        "admission": {
            "module": ENTRYPOINT,
            "symbol": "binding_is_admitted",
            "refresh_after_success": True,
        },
        "diagnostics": {
            "error_type": "FrameworkRuntimeInstallationMcpError",
            "discovery_is_effect_free": True,
        },
        "failure_contract": {
            "mode": "raise_stable_refusal",
            "exception": "FrameworkRuntimeInstallationMcpError",
            "invokes_on_discovery": False,
        },
    }


def input_schema() -> dict[str, Any]:
    """Derive the legacy MCP envelope from the canonical descriptor model."""

    request_schema = FrameworkRuntimeInstallationRequest.model_json_schema()
    definitions = request_schema.pop("$defs", None)
    reference = request_schema.get("$ref")
    if isinstance(definitions, dict) and isinstance(reference, str) and reference.startswith("#/$defs/"):
        request_schema = definitions.get(reference.removeprefix("#/$defs/"), request_schema)
    envelope: dict[str, Any] = {
        "type": "object",
        "additionalProperties": False,
        "required": ["request"],
        "properties": {"request": request_schema},
    }
    if definitions is not None:
        envelope["$defs"] = definitions
    return envelope


def binding_is_admitted(binding: Mapping[str, Any] | None) -> bool:
    """Accept registration only for CA-D-620's exact source declaration."""

    if not isinstance(binding, Mapping):
        return False
    return (
        binding.get("name") == TOOL_NAME
        and binding.get("mcp_name") == MCP_NAME
        and binding.get("entrypoint") == ENTRYPOINT
        and binding.get("action_ids") == [ACTION_ID]
        and binding.get("source_atom") == DELIVERY_ID
    )


def register_framework_runtime_installation(
    server: Any,
    root: str | Path,
    *,
    binding: Mapping[str, Any] | None,
) -> bool:
    """Register the direct tool only when its current source binding is exact."""

    if not binding_is_admitted(binding):
        return False
    from mcp.server.mcpserver.exceptions import ToolError
    from mcp.types import ToolAnnotations

    adapter = FrameworkRuntimeInstallationAdapter(root)
    annotations = ToolAnnotations(read_only_hint=False, destructive_hint=True, idempotent_hint=False, open_world_hint=False)

    @server.tool(name=MCP_NAME, structured_output=True, annotations=annotations)
    def install_framework_runtime_tool(request: ExecuteRequest) -> dict[str, str]:
        """Run one fixed-Project CA-O-200 Framework runtime installation."""

        try:
            return adapter.invoke(request)
        except FrameworkRuntimeInstallationMcpError as error:
            raise ToolError(str(error)) from error

    return True


__all__ = [
    "ACTION_ID",
    "DELIVERY_ID",
    "ENTRYPOINT",
    "ExecuteRequest",
    "FrameworkRuntimeInstallationAdapter",
    "FrameworkRuntimeInstallationMcpError",
    "FrameworkRuntimeInstallationRequest",
    "FrameworkRuntimeInstallationToolResult",
    "MCP_NAME",
    "McpActivation",
    "TOOL_NAME",
    "binding_is_admitted",
    "create_adapter",
    "describe_tool",
    "input_schema",
    "read_native_packet",
    "register_framework_runtime_installation",
]
