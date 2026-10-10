"""Closed direct MCP binding for the admitted CA-O-187 restoration Action.

The adapter owns only transport request validation and the D591 Operator-command
carrier check.  It delegates all restoration, retained-result reopening, source
admission, and Docker execution to the pre-existing native boundary.
"""

from __future__ import annotations

import hashlib
import json
import os
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
import re
import stat
import sys
from typing import Annotated, Any, Literal

from pydantic import BaseModel, ConfigDict, Field, JsonValue, RootModel, TypeAdapter, ValidationError


_TOOLS_ROOT = Path(__file__).resolve().parents[1] / "201_TOOLS"
_RELEASE_ROOT = _TOOLS_ROOT / "RELEASE_VERSION"
for _path in (_TOOLS_ROOT, _RELEASE_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from direct_action_session import (  # noqa: E402
    DirectActionJournalError,
    DirectActionSession,
    RESTORATION_ACTION_ID,
    _source_binding,
)
from framework_image_restoration import (  # noqa: E402
    FrameworkImageRestorationError,
    preview_framework_image_restoration,
    recover_framework_image_terminal,
    restore_framework_image,
    validate_framework_image_recording_command,
)
from operator_registry import OperatorRegistryError, parse_operators_registry  # noqa: E402
from release_image import DockerSubprocessExecutor  # noqa: E402
import work_journal  # noqa: E402


MCP_NAME = "restore_framework_image"
TOOL_NAME = "FRAMEWORK_IMAGE_RESTORATION"
ACTION_ID = "CA-O-187"
DELIVERY_ID = "CA-D-591"
ENTRYPOINT = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/framework_image_restoration_mcp.py"
OPERATORS_REGISTRY_REF = ".caprmedio_caprmedio/operators_registry.toml"
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_COMMAND_BYTES_LIMIT = 64 * 1024


class FrameworkImageRestorationMcpError(RuntimeError):
    """A stable refusal before the native direct Action can have an effect."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


class _ClosedRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


class PreviewRequest(_ClosedRequest):
    operation: Literal["preview"]


class ExecuteRequest(_ClosedRequest):
    operation: Literal["execute"]
    requested_run_id: str = Field(min_length=1, max_length=160)
    expected_selector_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    operator: str = Field(min_length=1, max_length=512)
    authorization_ref: str = Field(min_length=1, max_length=1024)
    retry_of_terminal_event_id: str | None = Field(default=None, min_length=1, max_length=1024)


class RecordTerminalRequest(_ClosedRequest):
    operation: Literal["record_terminal"]
    result_ref: str = Field(min_length=1, max_length=1024)
    operator: str = Field(min_length=1, max_length=512)
    authorization_ref: str = Field(min_length=1, max_length=1024)


RestorationRequest = Annotated[
    PreviewRequest | ExecuteRequest | RecordTerminalRequest,
    Field(discriminator="operation"),
]
_REQUESTS = TypeAdapter(RestorationRequest)


class FrameworkImageRestorationRequest(RootModel[RestorationRequest]):
    """Canonical transport-neutral request model for the O187 Tool."""


class FrameworkImageRestorationResult(RootModel[dict[str, JsonValue]]):
    """Canonical open structured result retained by the native O187 boundary."""


class _DescriptorAdapter:
    """Uniform descriptor wrapper; the native adapter remains the invoker."""

    def __init__(self, root: str | Path) -> None:
        self._adapter = FrameworkImageRestorationAdapter(root)

    def invoke(
        self,
        request: FrameworkImageRestorationRequest | RestorationRequest | Mapping[str, Any],
    ) -> dict[str, Any]:
        return self._adapter.invoke(request.root if isinstance(request, FrameworkImageRestorationRequest) else request)


@dataclass(frozen=True)
class _OperatorCommand:
    reference: str
    sha256: str
    operator: str
    journal_author: str


def _refuse(code: str, message: str) -> None:
    raise FrameworkImageRestorationMcpError(code, message)


def _canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _root(value: str | Path) -> Path:
    supplied = Path(value)
    try:
        root = supplied.resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise FrameworkImageRestorationMcpError("framework-image-restoration-mcp-root-invalid", "server Project root is unavailable") from error
    if supplied.is_symlink() or root.is_symlink() or not root.is_dir():
        _refuse("framework-image-restoration-mcp-root-invalid", "server Project root is unsafe")
    return root


def _relative(value: object, *, field: str) -> tuple[str, Path]:
    if not isinstance(value, str) or not value or "\\" in value:
        _refuse("framework-image-restoration-mcp-command-invalid", f"{field} must be a safe Project-relative path")
    parsed = PurePosixPath(value)
    if (parsed.is_absolute() or parsed == PurePosixPath(".")
            or any(part in {"", ".", ".."} for part in parsed.parts)
            or parsed.as_posix() != value):
        _refuse("framework-image-restoration-mcp-command-invalid", f"{field} must be a canonical Project-relative path")
    return value, Path(*parsed.parts)


def _read_regular(root: Path, relative: Path, *, label: str) -> bytes:
    """Read one bounded regular carrier without following a symlink path."""
    candidate = root
    try:
        for index, part in enumerate(relative.parts):
            candidate = candidate / part
            item = os.lstat(candidate)
            if stat.S_ISLNK(item.st_mode):
                _refuse("framework-image-restoration-mcp-command-invalid", f"{label} has a symlinked ancestor")
            if index < len(relative.parts) - 1 and not stat.S_ISDIR(item.st_mode):
                _refuse("framework-image-restoration-mcp-command-invalid", f"{label} has an invalid ancestor")
        flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(candidate, flags)
    except FrameworkImageRestorationMcpError:
        raise
    except OSError as error:
        raise FrameworkImageRestorationMcpError("framework-image-restoration-mcp-command-unavailable", f"{label} is unavailable") from error
    try:
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode) or before.st_size > _COMMAND_BYTES_LIMIT:
            _refuse("framework-image-restoration-mcp-command-invalid", f"{label} is not a bounded regular file")
        payload = bytearray()
        while len(payload) <= _COMMAND_BYTES_LIMIT:
            chunk = os.read(descriptor, min(8192, _COMMAND_BYTES_LIMIT + 1 - len(payload)))
            if not chunk:
                break
            payload.extend(chunk)
        after = os.fstat(descriptor)
        if (len(payload) > _COMMAND_BYTES_LIMIT or before.st_dev != after.st_dev
                or before.st_ino != after.st_ino or before.st_size != after.st_size
                or len(payload) != before.st_size):
            _refuse("framework-image-restoration-mcp-command-invalid", f"{label} changed while being read")
        return bytes(payload)
    except FrameworkImageRestorationMcpError:
        raise
    except OSError as error:
        raise FrameworkImageRestorationMcpError("framework-image-restoration-mcp-command-unavailable", f"{label} is unreadable") from error
    finally:
        os.close(descriptor)


def _registered_author(root: Path, operator: str) -> tuple[str, str]:
    registry_ref, registry_path = _relative(OPERATORS_REGISTRY_REF, field="operators registry")
    del registry_ref
    payload = _read_regular(root, registry_path, label="registered Operator evidence")
    try:
        records = parse_operators_registry(payload)
    except OperatorRegistryError as error:
        raise FrameworkImageRestorationMcpError("framework-image-restoration-mcp-operator-invalid", "registered Operator evidence is invalid") from error
    matching = [record for record in records if record.name == operator]
    if len(matching) != 1:
        _refuse("framework-image-restoration-mcp-operator-invalid", "Operator is not uniquely registered for this Project")
    author = matching[0].journal_author
    if author is None and work_journal.AUTHOR_RE.fullmatch(matching[0].name):
        author = matching[0].name
    if author is None:
        _refuse("framework-image-restoration-mcp-operator-invalid", "Operator has no explicit Journal author mapping")
    return author, hashlib.sha256(payload).hexdigest()


def _action_source(root: Path) -> dict[str, object]:
    try:
        bound = _source_binding(root, RESTORATION_ACTION_ID)
    except DirectActionJournalError as error:
        raise FrameworkImageRestorationMcpError("framework-image-restoration-mcp-source-stale", str(error)) from error
    return {
        "atom_id": bound["atom_id"],
        "version": bound["version"],
        "path": bound["path"],
        "sha256": bound["digest"],
    }


def _request_input(request: ExecuteRequest | RecordTerminalRequest) -> dict[str, str]:
    if isinstance(request, ExecuteRequest):
        value = {
            "requested_run_id": request.requested_run_id,
            "expected_selector_sha256": request.expected_selector_sha256,
        }
        if request.retry_of_terminal_event_id is not None:
            value["retry_of_terminal_event_id"] = request.retry_of_terminal_event_id
        return value
    return {"result_ref": request.result_ref}


def _read_command(root: Path, request: ExecuteRequest | RecordTerminalRequest) -> _OperatorCommand:
    reference, relative = _relative(request.authorization_ref, field="authorization_ref")
    if isinstance(request, RecordTerminalRequest):
        author, _registry_sha256 = _registered_author(root, request.operator)
        try:
            command_sha256 = validate_framework_image_recording_command(
                root,
                result_ref=request.result_ref,
                authorization_ref=reference,
                operator=request.operator,
                journal_author=author,
                operators_registry_ref=OPERATORS_REGISTRY_REF,
            )
        except FrameworkImageRestorationError as error:
            raise FrameworkImageRestorationMcpError(
                "framework-image-restoration-mcp-command-invalid",
                "recording command failed native validation",
            ) from error
        return _OperatorCommand(reference, command_sha256, request.operator, author)
    raw = _read_regular(root, relative, label="Operator command carrier")
    try:
        value = json.loads(raw.decode("utf-8"))
        canonical = _canonical_json(value)
    except (UnicodeDecodeError, ValueError, TypeError) as error:
        raise FrameworkImageRestorationMcpError("framework-image-restoration-mcp-command-invalid", "Operator command carrier is not canonical UTF-8 JSON") from error
    expected_keys = {
        "schema_version", "operation", "command_id", "operator", "journal_author",
        "operators_registry_sha256", "action_source", "input",
    }
    if not isinstance(value, dict) or set(value) != expected_keys or raw != canonical:
        _refuse("framework-image-restoration-mcp-command-invalid", "Operator command carrier has an invalid closed schema")
    if type(value.get("schema_version")) is not int or value["schema_version"] != 1:
        _refuse("framework-image-restoration-mcp-command-invalid", "Operator command carrier schema is unsupported")
    if not isinstance(value.get("command_id"), str) or not value["command_id"].strip() or any(char in value["command_id"] for char in "\r\n"):
        _refuse("framework-image-restoration-mcp-command-invalid", "Operator command ID is invalid")
    if value.get("operation") != request.operation:
        _refuse("framework-image-restoration-mcp-command-mismatch", "Operator command names another operation")
    if value.get("operator") != request.operator:
        _refuse("framework-image-restoration-mcp-command-mismatch", "Operator command names another Operator")
    author, registry_sha256 = _registered_author(root, request.operator)
    if value.get("journal_author") != author:
        _refuse("framework-image-restoration-mcp-command-mismatch", "Operator command Journal author is not currently registered")
    if value.get("operators_registry_sha256") != registry_sha256 or _SHA256.fullmatch(str(value.get("operators_registry_sha256"))) is None:
        _refuse("framework-image-restoration-mcp-command-mismatch", "Operator command registry binding is stale")
    if value.get("action_source") != _action_source(root):
        _refuse("framework-image-restoration-mcp-command-mismatch", "Operator command direct Action source is stale")
    if value.get("input") != _request_input(request):
        _refuse("framework-image-restoration-mcp-command-mismatch", "Operator command input differs from this request")
    command_sha256 = hashlib.sha256(raw).hexdigest()
    if relative.name != f"{command_sha256}.json":
        _refuse("framework-image-restoration-mcp-command-invalid", "Operator command filename does not match its exact bytes")
    return _OperatorCommand(reference, command_sha256, request.operator, author)


class _CommandBoundJournal:
    """Expose a command digest in existing in-memory invocation evidence only."""

    def __init__(self, session: Any, command: _OperatorCommand) -> None:
        self._session = session
        self._command = command

    def _record(self, value: Mapping[str, Any]) -> Mapping[str, Any]:
        run_id = value.get("run_id")
        actual = getattr(self._session, "actual", {}).get(run_id) if isinstance(run_id, str) else None
        if isinstance(actual, dict):
            actual["operator_command"] = {
                "authorization_ref": self._command.reference,
                "sha256": self._command.sha256,
            }
        return value

    def begin_action(self, **kwargs: Any) -> Mapping[str, Any]:
        return self._record(self._session.begin_action(**kwargs))

    def reopen_restoration_for_recording(self, *args: Any, **kwargs: Any) -> Mapping[str, Any]:
        return self._record(self._session.reopen_restoration_for_recording(*args, **kwargs))

    def __getattr__(self, name: str) -> Any:
        return getattr(self._session, name)


class FrameworkImageRestorationAdapter:
    """One server-root-bound D591 request adapter; it accepts no execution seams."""

    def __init__(
        self,
        root: str | Path,
        *,
        session_factory: Callable[..., Any] = DirectActionSession,
        executor_factory: Callable[[], Any] = DockerSubprocessExecutor,
        previewer: Callable[[Path], dict[str, Any]] = preview_framework_image_restoration,
        restorer: Callable[..., dict[str, Any]] = restore_framework_image,
        terminal_recoverer: Callable[..., dict[str, Any]] = recover_framework_image_terminal,
    ) -> None:
        self.root = _root(root)
        self._session_factory = session_factory
        self._executor_factory = executor_factory
        self._previewer = previewer
        self._restorer = restorer
        self._terminal_recoverer = terminal_recoverer

    def invoke(self, request: Mapping[str, Any] | RestorationRequest) -> dict[str, Any]:
        try:
            parsed = request if isinstance(request, (PreviewRequest, ExecuteRequest, RecordTerminalRequest)) else _REQUESTS.validate_python(request)
        except ValidationError as error:
            raise FrameworkImageRestorationMcpError("framework-image-restoration-mcp-request-invalid", "request has an invalid closed schema") from error
        if isinstance(parsed, PreviewRequest):
            # Preview has no Operator authorization but still refuses a stale
            # direct Action source before returning an executable-looking plan.
            _action_source(self.root)
            return self._previewer(self.root)
        command = _read_command(self.root, parsed)
        session = self._session_factory(
            self.root,
            author=command.journal_author,
            operator_authorization={"operator": command.operator, "authorization_ref": command.reference},
            action_id=RESTORATION_ACTION_ID,
        )
        with session:
            journal = session if isinstance(session, DirectActionSession) else _CommandBoundJournal(session, command)
            if isinstance(parsed, ExecuteRequest):
                return self._restorer(
                    self.root,
                    journal=journal,
                    requested_run_id=parsed.requested_run_id,
                    expected_selector_sha256=parsed.expected_selector_sha256,
                    image_executor=self._executor_factory(),
                    retry_of_terminal_event_id=parsed.retry_of_terminal_event_id,
                )
            return self._terminal_recoverer(
                self.root,
                journal=journal,
                result_ref=parsed.result_ref,
                image_executor=self._executor_factory(),
                recording_authorization_ref=command.reference,
            )


def create_adapter(root: str | Path) -> _DescriptorAdapter:
    """Create the sole root-bound adapter used by descriptor-driven providers."""

    return _DescriptorAdapter(root)


def describe_tool() -> dict[str, Any]:
    """Describe O187 without opening carriers, invoking it, or causing an effect."""

    return {
        "schema_version": 1,
        "identity": {
            "name": TOOL_NAME,
            "tool_version": 1,
            "title": "Restore Framework image",
            "description": "Preview or execute the source-bound CA-O-187 Framework image restoration Action.",
            "purpose": "Restore a selected Framework image only through the existing direct Action boundary.",
        },
        "binding": {
            "delivery_atom_id": DELIVERY_ID,
            "action_ids": [ACTION_ID],
            "implementation_entrypoint": ENTRYPOINT,
        },
        "models": {
            "input": {"module": ENTRYPOINT, "symbol": "FrameworkImageRestorationRequest"},
            "output": {"module": ENTRYPOINT, "symbol": "FrameworkImageRestorationResult"},
        },
        "callable": {"module": ENTRYPOINT, "symbol": "create_adapter"},
        "effect_hints": {
            "read_only_hint": False,
            "destructive_hint": False,
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
            "refresh_after_success": False,
        },
        "diagnostics": {
            "error_type": "FrameworkImageRestorationMcpError",
            "discovery_is_effect_free": True,
        },
        "failure_contract": {
            "mode": "raise_stable_refusal",
            "exception": "FrameworkImageRestorationMcpError",
            "invokes_on_discovery": False,
        },
    }


def input_schema() -> dict[str, Any]:
    """Derive the legacy MCP envelope from the canonical descriptor model."""

    request_schema = FrameworkImageRestorationRequest.model_json_schema()
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
    """Reject registration unless current source declares this exact direct Tool."""
    if not isinstance(binding, Mapping):
        return False
    return (
        binding.get("name") == TOOL_NAME
        and binding.get("mcp_name") == MCP_NAME
        and binding.get("entrypoint") == ENTRYPOINT
        and binding.get("action_ids") == [ACTION_ID]
        and binding.get("source_atom") == DELIVERY_ID
    )


def register_framework_image_restoration(server: Any, root: str | Path, *, binding: Mapping[str, Any] | None) -> bool:
    """Register only the current, source-declared direct binding."""
    if not binding_is_admitted(binding):
        return False
    from mcp.server.mcpserver.exceptions import ToolError
    from mcp.types import ToolAnnotations

    adapter = FrameworkImageRestorationAdapter(root)
    annotations = ToolAnnotations(read_only_hint=False, destructive_hint=False, idempotent_hint=False, open_world_hint=False)

    @server.tool(name=MCP_NAME, structured_output=True, annotations=annotations)
    def restore_framework_image_tool(request: RestorationRequest) -> dict[str, Any]:
        """Preview or run the one source-bound O187 restoration Action."""
        try:
            return adapter.invoke(request)
        except (FrameworkImageRestorationMcpError, FrameworkImageRestorationError, DirectActionJournalError) as error:
            raise ToolError(str(error)) from error

    return True


__all__ = [
    "ACTION_ID", "DELIVERY_ID", "ENTRYPOINT", "FrameworkImageRestorationAdapter",
    "FrameworkImageRestorationMcpError", "FrameworkImageRestorationRequest",
    "FrameworkImageRestorationResult", "MCP_NAME", "RestorationRequest", "TOOL_NAME",
    "binding_is_admitted", "create_adapter", "describe_tool", "input_schema",
    "register_framework_image_restoration",
]
