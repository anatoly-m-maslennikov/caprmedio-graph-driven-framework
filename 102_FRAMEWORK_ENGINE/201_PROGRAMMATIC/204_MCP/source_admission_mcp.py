"""Closed direct MCP binding for CA-O-199 package-source admission.

The adapter owns the server-bound request and authorization-carrier boundary.
It delegates retained O164/O172 reopening, direct Action start, admission, and
terminal recording to the package producer's host-command bridge.  It neither
constructs a selected-run context nor appends a second Journal event.
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

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter, ValidationError


_TOOLS_ROOT = Path(__file__).resolve().parents[1] / "201_TOOLS"
_RELEASE_ROOT = _TOOLS_ROOT / "RELEASE_VERSION"
for _path in (_TOOLS_ROOT, _RELEASE_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from direct_action_session import (  # noqa: E402
    DirectActionJournalError,
    SOURCE_ADMISSION_ACTION_ID,
    _source_binding,
)
from operator_registry import OperatorRegistryError, parse_operators_registry  # noqa: E402
import work_journal  # noqa: E402


MCP_NAME = "admit_package_sources"
TOOL_NAME = "ADMIT_PACKAGE_SOURCES"
ACTION_ID = "CA-O-199"
DELIVERY_ID = "CA-D-602"
ENTRYPOINT = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/source_admission_mcp.py"
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_COMMAND_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,159}$")
_RUN_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,159}$")
_AUTHORIZATION_BYTES_LIMIT = 64 * 1024


class SourceAdmissionMcpError(RuntimeError):
    """Stable refusal before the host command can have an effect."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


class _ClosedRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


class PreviewRequest(_ClosedRequest):
    operation: Literal["preview"]
    release_run_id: str = Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,159}$")


class ExecuteRequest(_ClosedRequest):
    operation: Literal["execute"]
    command_id: str = Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,159}$")
    release_run_id: str = Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,159}$")
    operator: str = Field(min_length=1, max_length=512)
    authorization_ref: str = Field(min_length=1, max_length=1024)
    observed_snapshot_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")


SourceAdmissionRequest = Annotated[PreviewRequest | ExecuteRequest, Field(discriminator="operation")]
_REQUESTS = TypeAdapter(SourceAdmissionRequest)


@dataclass(frozen=True)
class _Authorization:
    reference: str
    sha256: str
    journal_author: str
    operators_registry_ref: str


Previewer = Callable[..., Mapping[str, Any]]
Executor = Callable[..., Mapping[str, Any]]
ReleaseAuthorizationResolver = Callable[[Path, str], str]


def _refuse(code: str, message: str) -> None:
    raise SourceAdmissionMcpError(code, message)


def _canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _root(value: str | Path) -> Path:
    supplied = Path(value)
    try:
        root = supplied.resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise SourceAdmissionMcpError("source-admission-mcp-root-invalid", "server Project root is unavailable") from error
    if supplied.is_symlink() or root.is_symlink() or not root.is_dir():
        _refuse("source-admission-mcp-root-invalid", "server Project root is unsafe")
    return root


def _relative(value: object, *, field: str) -> tuple[str, Path]:
    if not isinstance(value, str) or not value or "\\" in value:
        _refuse("source-admission-mcp-authorization-invalid", f"{field} must be a safe Project-relative path")
    parsed = PurePosixPath(value)
    if (
        parsed.is_absolute()
        or parsed == PurePosixPath(".")
        or any(part in {"", ".", ".."} for part in parsed.parts)
        or any(part.startswith(".env") or part.endswith(".env") for part in parsed.parts)
        or parsed.as_posix() != value
    ):
        _refuse("source-admission-mcp-authorization-invalid", f"{field} must be a canonical Project-relative path")
    return value, Path(*parsed.parts)


def _read_regular(root: Path, relative: Path, *, label: str) -> bytes:
    """Read one bounded regular carrier without following a symlink path."""

    candidate = root
    try:
        for index, part in enumerate(relative.parts):
            candidate = candidate / part
            item = os.lstat(candidate)
            if stat.S_ISLNK(item.st_mode):
                _refuse("source-admission-mcp-authorization-invalid", f"{label} has a symlinked ancestor")
            if index < len(relative.parts) - 1 and not stat.S_ISDIR(item.st_mode):
                _refuse("source-admission-mcp-authorization-invalid", f"{label} has an invalid ancestor")
        flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(candidate, flags)
    except SourceAdmissionMcpError:
        raise
    except OSError as error:
        raise SourceAdmissionMcpError(
            "source-admission-mcp-authorization-unavailable", f"{label} is unavailable",
        ) from error
    try:
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode) or before.st_size > _AUTHORIZATION_BYTES_LIMIT:
            _refuse("source-admission-mcp-authorization-invalid", f"{label} is not a bounded regular file")
        payload = bytearray()
        while len(payload) <= _AUTHORIZATION_BYTES_LIMIT:
            chunk = os.read(descriptor, min(8192, _AUTHORIZATION_BYTES_LIMIT + 1 - len(payload)))
            if not chunk:
                break
            payload.extend(chunk)
        after = os.fstat(descriptor)
        if (
            len(payload) > _AUTHORIZATION_BYTES_LIMIT
            or before.st_dev != after.st_dev
            or before.st_ino != after.st_ino
            or before.st_size != after.st_size
            or len(payload) != before.st_size
        ):
            _refuse("source-admission-mcp-authorization-invalid", f"{label} changed while being read")
        return bytes(payload)
    except SourceAdmissionMcpError:
        raise
    except OSError as error:
        raise SourceAdmissionMcpError(
            "source-admission-mcp-authorization-unavailable", f"{label} is unreadable",
        ) from error
    finally:
        os.close(descriptor)


def _operators_registry_ref(root: Path) -> str:
    """Use the producer's selected-Project registry resolution verbatim."""

    try:
        # The host bridge owns selected Project/control-root resolution.  The
        # adapter must validate the same registry the direct O199 command will
        # reopen, rather than assume the legacy control-root child.
        from source_admission_host_command import _registry_ref

        value = _registry_ref(root)
    except Exception as error:
        raise SourceAdmissionMcpError(
            "source-admission-mcp-operator-unavailable", "configured Operator registry is unavailable",
        ) from error
    normalized, _relative_path = _relative(value, field="configured operators registry")
    return normalized


def _registered_author(root: Path, operator: str, registry_ref: str) -> tuple[str, str]:
    _normalized, registry_path = _relative(registry_ref, field="configured operators registry")
    payload = _read_regular(root, registry_path, label="registered Operator evidence")
    try:
        records = parse_operators_registry(payload)
    except OperatorRegistryError as error:
        raise SourceAdmissionMcpError(
            "source-admission-mcp-operator-invalid", "registered Operator evidence is invalid",
        ) from error
    matching = [record for record in records if record.name == operator]
    if len(matching) != 1:
        _refuse("source-admission-mcp-operator-invalid", "Operator is not uniquely registered for this Project")
    author = matching[0].journal_author
    if author is None and work_journal.AUTHOR_RE.fullmatch(matching[0].name):
        author = matching[0].name
    if author is None:
        _refuse("source-admission-mcp-operator-invalid", "Operator has no explicit Journal author mapping")
    return author, hashlib.sha256(payload).hexdigest()


def _action_source(root: Path) -> dict[str, object]:
    try:
        bound = _source_binding(root, SOURCE_ADMISSION_ACTION_ID)
    except DirectActionJournalError as error:
        raise SourceAdmissionMcpError("source-admission-mcp-source-stale", str(error)) from error
    return {
        "atom_id": bound["atom_id"],
        "version": bound["version"],
        "path": bound["path"],
        "sha256": bound["digest"],
    }


def _read_authorization(root: Path, request: ExecuteRequest) -> _Authorization:
    reference, relative = _relative(request.authorization_ref, field="authorization_ref")
    raw = _read_regular(root, relative, label="Operator authorization carrier")
    try:
        value = json.loads(raw.decode("utf-8"))
        canonical = _canonical_json(value)
    except (UnicodeDecodeError, ValueError, TypeError) as error:
        raise SourceAdmissionMcpError(
            "source-admission-mcp-authorization-invalid", "Operator authorization carrier is not canonical UTF-8 JSON",
        ) from error
    expected_keys = {
        "schema_version", "operation", "command_id", "release_run_id", "operator",
        "journal_author", "snapshot_sha256", "operators_registry_sha256", "action_source",
    }
    if not isinstance(value, dict) or set(value) != expected_keys or raw != canonical:
        _refuse("source-admission-mcp-authorization-invalid", "Operator authorization carrier has an invalid closed schema")
    if type(value.get("schema_version")) is not int or value["schema_version"] != 1:
        _refuse("source-admission-mcp-authorization-invalid", "Operator authorization schema is unsupported")
    if value.get("operation") != "admit_package_sources":
        _refuse("source-admission-mcp-authorization-mismatch", "Operator authorization names another operation")
    if value.get("command_id") != request.command_id or _COMMAND_ID.fullmatch(str(value.get("command_id"))) is None:
        _refuse("source-admission-mcp-authorization-mismatch", "Operator authorization command differs from this request")
    if value.get("release_run_id") != request.release_run_id or _RUN_ID.fullmatch(str(value.get("release_run_id"))) is None:
        _refuse("source-admission-mcp-authorization-mismatch", "Operator authorization Release Run differs from this request")
    if value.get("operator") != request.operator:
        _refuse("source-admission-mcp-authorization-mismatch", "Operator authorization names another Operator")
    if value.get("snapshot_sha256") != request.observed_snapshot_sha256 or _SHA256.fullmatch(str(value.get("snapshot_sha256"))) is None:
        _refuse("source-admission-mcp-authorization-mismatch", "Operator authorization snapshot differs from this request")
    registry_ref = _operators_registry_ref(root)
    author, registry_sha256 = _registered_author(root, request.operator, registry_ref)
    if value.get("journal_author") != author:
        _refuse("source-admission-mcp-authorization-mismatch", "Operator authorization Journal author is not currently registered")
    if value.get("operators_registry_sha256") != registry_sha256 or _SHA256.fullmatch(str(value.get("operators_registry_sha256"))) is None:
        _refuse("source-admission-mcp-authorization-mismatch", "Operator authorization registry binding is stale")
    if value.get("action_source") != _action_source(root):
        _refuse("source-admission-mcp-authorization-mismatch", "Operator authorization direct Action source is stale")
    return _Authorization(reference, hashlib.sha256(raw).hexdigest(), author, registry_ref)


def _release_authorization_ref(root: Path, release_run_id: str) -> str:
    """Read only the frozen O164 authorization reference for this Run."""

    try:
        from selected_execution import SelectedExecution

        frozen = SelectedExecution(root).load(release_run_id)
    except Exception as error:
        raise SourceAdmissionMcpError(
            "source-admission-mcp-release-unavailable", "selected Release Run is unavailable",
        ) from error
    try:
        request = frozen.get("request") if isinstance(frozen, Mapping) else None
        execution = request.get("execution") if isinstance(request, Mapping) else None
        authorization = execution.get("operator_authorization") if isinstance(execution, Mapping) else None
        reference = authorization.get("authorization_ref") if isinstance(authorization, Mapping) else None
        release = request.get("run_id") if isinstance(request, Mapping) else None
    except AttributeError as error:  # pragma: no cover - Mapping guards cover normal values.
        raise SourceAdmissionMcpError(
            "source-admission-mcp-release-invalid", "selected Release Run lacks a closed authorization carrier",
        ) from error
    if release != release_run_id:
        _refuse("source-admission-mcp-release-invalid", "selected Release Run identity differs from this request")
    normalized, _relative_path = _relative(reference, field="frozen release authorization_ref")
    return normalized


def _requested_o172(release_run_id: str) -> str:
    if _RUN_ID.fullmatch(release_run_id) is None:
        _refuse("source-admission-mcp-release-invalid", "Release Run identity is invalid")
    return f"{release_run_id}:step:3:action:1"


def _default_previewer(
    root: Path,
    *,
    release_run_id: str,
) -> Mapping[str, Any]:
    """Use only the producer-owned O164/O172 retained-input reader."""

    try:
        from source_admission_host_command import preview_source_admission_command

        preview = preview_source_admission_command(
            root,
            release_run_id=release_run_id,
        )
        snapshot_sha256 = getattr(preview, "snapshot_sha256", None)
        frontier = getattr(preview, "frontier", None)
        requested_action_run_id = getattr(frontier, "requested_action_run_id", None)
        if (
            not isinstance(snapshot_sha256, str)
            or _SHA256.fullmatch(snapshot_sha256) is None
            or requested_action_run_id != _requested_o172(release_run_id)
        ):
            _refuse("source-admission-mcp-preview-invalid", "source-admission preview has an invalid result")
        return {
            "operation": "preview",
            "release_run_id": release_run_id,
            "requested_action_run_id": requested_action_run_id,
            "snapshot_sha256": snapshot_sha256,
        }
    except ImportError as error:
        raise SourceAdmissionMcpError(
            "source-admission-mcp-host-unavailable", "source-admission host bridge is unavailable",
        ) from error
    except Exception as error:
        if isinstance(error, SourceAdmissionMcpError):
            raise
        raise SourceAdmissionMcpError("source-admission-mcp-preview-refused", "source-admission preview was refused") from error


def _published_ref(root: Path, value: object, *, label: str) -> str:
    """Return one existing regular producer artifact as a safe Project ref."""

    if not isinstance(value, Path):
        _refuse("source-admission-mcp-execute-invalid", f"{label} result has no physical path")
    try:
        relative = value.relative_to(root)
        reference, local = _relative(relative.as_posix(), field=f"{label} result reference")
        candidate = root / local
        metadata = os.lstat(candidate)
        if (
            candidate != value
            or stat.S_ISLNK(metadata.st_mode)
            or not stat.S_ISREG(metadata.st_mode)
            or candidate.resolve(strict=True) != candidate
        ):
            _refuse("source-admission-mcp-execute-invalid", f"{label} result path is unsafe")
    except SourceAdmissionMcpError:
        raise
    except (OSError, RuntimeError, ValueError) as error:
        raise SourceAdmissionMcpError(
            "source-admission-mcp-execute-invalid", f"{label} result path is unavailable",
        ) from error
    return reference


def _terminal_transport(
    root: Path,
    value: object,
    *,
    command_receipt_ref: str,
    admission_receipt_ref: str,
    catalog_ref: str,
    action_run_id: str,
) -> dict[str, object]:
    """Expose one real terminal Journal fact without fabricating its outcome."""

    if not isinstance(value, Mapping):
        _refuse("source-admission-mcp-execute-invalid", "source-admission command has no terminal Journal result")
    expected = {
        "event_id", "run_id", "disposition", "outcome", "result_ref", "effect_refs", "report_ref", "event_receipt",
    }
    if set(value) != expected or value.get("disposition") != "terminal" or value.get("run_id") != action_run_id:
        _refuse("source-admission-mcp-execute-invalid", "source-admission terminal result is invalid")
    outcome = value.get("outcome")
    if not isinstance(outcome, str) or outcome not in {"completed", "no_op", "failed", "partial", "cancelled"}:
        _refuse("source-admission-mcp-execute-invalid", "source-admission terminal outcome is invalid")
    result_ref, _result_path = _relative(value.get("result_ref"), field="terminal result_ref")
    effect_refs = value.get("effect_refs")
    if not isinstance(effect_refs, list):
        _refuse("source-admission-mcp-execute-invalid", "source-admission terminal effects are invalid")
    safe_effect_refs = [_relative(item, field="terminal effect_ref")[0] for item in effect_refs]
    if result_ref != admission_receipt_ref or safe_effect_refs != [command_receipt_ref, admission_receipt_ref, catalog_ref]:
        _refuse("source-admission-mcp-execute-invalid", "source-admission terminal references differ from published results")
    receipt = value.get("event_receipt")
    expected_receipt = {
        "event_id", "action_id", "event_digest", "carrier", "line", "previous_carrier_digest", "appended_carrier_digest",
    }
    if not isinstance(receipt, Mapping) or set(receipt) != expected_receipt:
        _refuse("source-admission-mcp-execute-invalid", "source-admission terminal receipt is invalid")
    event_id = value.get("event_id")
    event_digest = receipt.get("event_digest")
    if (
        not isinstance(event_id, str)
        or not event_id
        or receipt.get("event_id") != event_id
        or receipt.get("action_id") != ACTION_ID
        or not isinstance(event_digest, str)
        or _SHA256.fullmatch(event_digest) is None
        or type(receipt.get("line")) is not int
        or receipt["line"] < 1
        or not isinstance(receipt.get("previous_carrier_digest"), str)
        or _SHA256.fullmatch(receipt["previous_carrier_digest"]) is None
        or not isinstance(receipt.get("appended_carrier_digest"), str)
        or _SHA256.fullmatch(receipt["appended_carrier_digest"]) is None
    ):
        _refuse("source-admission-mcp-execute-invalid", "source-admission terminal receipt is invalid")
    carrier_ref, _carrier_path = _relative(receipt.get("carrier"), field="terminal Journal carrier")
    return {
        "outcome": outcome,
        "event_id": event_id,
        "event_sha256": event_digest,
        "carrier_ref": carrier_ref,
        "carrier_line": receipt["line"],
        "previous_carrier_sha256": receipt["previous_carrier_digest"],
        "raw_sha256": receipt["appended_carrier_digest"],
        "result_ref": result_ref,
        "effect_refs": safe_effect_refs,
    }


def _default_executor(root: Path, **kwargs: Any) -> Mapping[str, Any]:
    """Delegate the one effect to the producer-owned direct O199 command."""

    try:
        from source_admission_host_command import execute_source_admission_command

        result = execute_source_admission_command(
            root,
            command_id=kwargs["command_id"],
            release_run_id=kwargs["release_run_id"],
            operator=kwargs["operator"],
            # The producer reopens this frozen O164 reference and refuses a
            # changed selected authorization immediately before O199 start.
            # The caller's D602 authorization carrier is checked above and
            # rechecked by ``invoke`` immediately before this delegation.
            authorization_ref=kwargs["release_authorization_ref"],
            observed_snapshot_sha256=kwargs["observed_snapshot_sha256"],
        )
        admission_command = getattr(result, "admission_command", None)
        receipt = getattr(admission_command, "command_receipt", None)
        admission = getattr(admission_command, "admission", None)
        terminal = getattr(admission_command, "terminal", None)
        frontier = getattr(result, "frontier", None)
        snapshot_sha256 = getattr(receipt, "snapshot_sha256", None)
        command_receipt_sha256 = getattr(receipt, "sha256", None)
        action_run_id = getattr(receipt, "action_run_id", None)
        command_receipt_ref = _published_ref(root, getattr(admission_command, "command_receipt_path", None), label="command receipt")
        admission_receipt_sha256 = getattr(getattr(admission, "receipt", None), "sha256", None)
        admission_receipt_ref = _published_ref(root, getattr(admission, "receipt_path", None), label="admission receipt")
        catalog_sha256 = getattr(admission, "catalog_sha256", None)
        catalog_ref = _published_ref(root, getattr(admission, "catalog_path", None), label="catalog")
        if (
            not isinstance(snapshot_sha256, str)
            or _SHA256.fullmatch(snapshot_sha256) is None
            or not isinstance(command_receipt_sha256, str)
            or _SHA256.fullmatch(command_receipt_sha256) is None
            or not isinstance(action_run_id, str)
            or not isinstance(admission_receipt_sha256, str)
            or _SHA256.fullmatch(admission_receipt_sha256) is None
            or not isinstance(catalog_sha256, str)
            or _SHA256.fullmatch(catalog_sha256) is None
            or getattr(frontier, "requested_action_run_id", None) != _requested_o172(kwargs["release_run_id"])
        ):
            _refuse("source-admission-mcp-execute-invalid", "source-admission command has an invalid result")
        terminal_event = _terminal_transport(
            root,
            terminal,
            command_receipt_ref=command_receipt_ref,
            admission_receipt_ref=admission_receipt_ref,
            catalog_ref=catalog_ref,
            action_run_id=action_run_id,
        )
        return {
            "operation": "execute",
            "release_run_id": kwargs["release_run_id"],
            "requested_action_run_id": getattr(frontier, "requested_action_run_id"),
            "snapshot_sha256": snapshot_sha256,
            "outcome": terminal_event["outcome"],
            "command_receipt_sha256": command_receipt_sha256,
            "command_receipt_ref": command_receipt_ref,
            "admission_receipt_sha256": admission_receipt_sha256,
            "admission_receipt_ref": admission_receipt_ref,
            "catalog_sha256": catalog_sha256,
            "catalog_ref": catalog_ref,
            "action_run_id": action_run_id,
            "terminal_event": terminal_event,
        }
    except ImportError as error:
        raise SourceAdmissionMcpError(
            "source-admission-mcp-host-unavailable", "source-admission host bridge is unavailable",
        ) from error
    except Exception as error:
        if isinstance(error, SourceAdmissionMcpError):
            raise
        raise SourceAdmissionMcpError("source-admission-mcp-execute-refused", "source-admission command was refused") from error


class SourceAdmissionAdapter:
    """One server-root-bound O199 adapter with no caller execution seams."""

    def __init__(
        self,
        root: str | Path,
        *,
        previewer: Previewer = _default_previewer,
        executor: Executor = _default_executor,
        release_authorization_resolver: ReleaseAuthorizationResolver = _release_authorization_ref,
    ) -> None:
        self.root = _root(root)
        if not callable(previewer) or not callable(executor) or not callable(release_authorization_resolver):
            _refuse("source-admission-mcp-host-invalid", "source-admission host bridge is unavailable")
        self._previewer = previewer
        self._executor = executor
        self._release_authorization_resolver = release_authorization_resolver

    def invoke(self, request: Mapping[str, Any] | SourceAdmissionRequest) -> dict[str, Any]:
        try:
            parsed = request if isinstance(request, (PreviewRequest, ExecuteRequest)) else _REQUESTS.validate_python(request)
        except ValidationError as error:
            raise SourceAdmissionMcpError(
                "source-admission-mcp-request-invalid", "request has an invalid closed schema",
            ) from error
        if isinstance(parsed, PreviewRequest):
            _action_source(self.root)
            result = self._previewer(
                self.root,
                release_run_id=parsed.release_run_id,
            )
            if not isinstance(result, Mapping):
                _refuse("source-admission-mcp-preview-invalid", "source-admission preview has an invalid result")
            return dict(result)
        authorization = _read_authorization(self.root, parsed)
        release_authorization_ref = self._release_authorization_resolver(self.root, parsed.release_run_id)
        # The D602 carrier is not passed as a replacement O164 authority.
        # Reopen it after resolving the selected authorization and directly
        # before producer delegation so a changed carrier cannot authorize a
        # subsequent O199 start.
        current_authorization = _read_authorization(self.root, parsed)
        if current_authorization.sha256 != authorization.sha256:
            _refuse("source-admission-mcp-authorization-changed", "Operator authorization carrier changed before execution")
        result = self._executor(
            self.root,
            command_id=parsed.command_id,
            release_run_id=parsed.release_run_id,
            requested_action_run_id=_requested_o172(parsed.release_run_id),
            operator=parsed.operator,
            authorization_ref=current_authorization.reference,
            release_authorization_ref=release_authorization_ref,
            operators_registry_ref=current_authorization.operators_registry_ref,
            observed_snapshot_sha256=parsed.observed_snapshot_sha256,
        )
        if not isinstance(result, Mapping):
            _refuse("source-admission-mcp-execute-invalid", "source-admission command has an invalid result")
        return dict(result)


def input_schema() -> dict[str, Any]:
    """Return the actual MCP envelope schema, including every closed variant."""

    return {
        "type": "object",
        "additionalProperties": False,
        "required": ["request"],
        "properties": {"request": _REQUESTS.json_schema()},
    }


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


def register_source_admission(server: Any, root: str | Path, *, binding: Mapping[str, Any] | None) -> bool:
    """Register only the current source-declared direct O199 binding."""

    if not binding_is_admitted(binding):
        return False
    from mcp.server.mcpserver.exceptions import ToolError
    from mcp.types import ToolAnnotations

    adapter = SourceAdmissionAdapter(root)
    annotations = ToolAnnotations(read_only_hint=False, destructive_hint=False, idempotent_hint=False, open_world_hint=False)

    @server.tool(name=MCP_NAME, structured_output=True, annotations=annotations)
    def admit_package_sources_tool(request: SourceAdmissionRequest) -> dict[str, Any]:
        """Preview or run the one source-bound O199 admission Action."""

        try:
            return adapter.invoke(request)
        except SourceAdmissionMcpError as error:
            raise ToolError(str(error)) from error

    return True


__all__ = [
    "ACTION_ID", "DELIVERY_ID", "ENTRYPOINT", "ExecuteRequest", "MCP_NAME",
    "PreviewRequest", "SourceAdmissionAdapter", "SourceAdmissionMcpError",
    "SourceAdmissionRequest", "TOOL_NAME", "binding_is_admitted", "input_schema",
    "register_source_admission",
]
