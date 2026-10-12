"""One explicit host command for direct CA-O-199 source admission.

This is not a selected-workflow adapter and accepts no caller authorization
mapping.  Its typed candidate and private-compilation inputs are re-opened as
one physical source snapshot; the Operator display name resolves to a Journal
account only through the Project registry.  The only durable command proof is
the closed D602 command receipt retained before catalog publication.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import stat
import sys
import tempfile
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

_TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(_TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_TOOLS_ROOT))

from direct_action_session import (
    DirectActionJournalError,
    DirectActionSession,
    SOURCE_ADMISSION_ACTION_ID,
)
from operator_registry import OperatorRegistryError, OperatorRegistryRecord, parse_operators_registry
from release_compilation import SealedPrivateMethodologyCompilation
from release_contract import ValidatedCandidate
from release_portable_contract import (
    SealedPortableSourceSnapshot,
    collect_portable_source_snapshot,
    revalidate_portable_source_snapshot,
)
from source_admission_host import (
    SourceAdmissionHostError,
    make_direct_source_admission_invocation_admitter,
)
from source_catalog_admission import (
    AdmissionInvocationRequest,
    SourceCatalogAdmission,
    SourceCatalogAdmissionError,
    admit_package_sources,
)
import work_journal


SCHEMA_VERSION = 1
OPERATION = "admit_package_sources"
COMMAND_DIRECTORY = Path(".caprmedio_runtime/installation/commands")
_SHA256 = re.compile(r"[0-9a-f]{64}")
_COMMAND_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,159}")
_RECEIPT_KEYS = frozenset({
    "schema_version", "operation", "command_id", "operator", "journal_author",
    "action_id", "action_run_id", "action_start_event_id", "snapshot_sha256",
    "action_source", "operators_registry_sha256",
})
_SOURCE_KEYS = frozenset({"atom_id", "version", "path", "sha256"})


class SourceAdmissionCommandError(RuntimeError):
    """Stable refusal from the direct O199 host-command boundary."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


@dataclass(frozen=True)
class SourceAdmissionCommandReceipt:
    """One reopened closed D602 host-command carrier."""

    command_id: str
    operator: str
    journal_author: str
    action_run_id: str
    action_start_event_id: str
    snapshot_sha256: str
    action_source: Mapping[str, object]
    operators_registry_sha256: str
    sha256: str
    payload: bytes


@dataclass(frozen=True)
class SourceAdmissionCommandResult:
    """Actual evidence from one fully reopened direct O199 command."""

    source_snapshot: SealedPortableSourceSnapshot
    command_receipt: SourceAdmissionCommandReceipt
    command_receipt_path: Path
    action_start: Mapping[str, object]
    admission: SourceCatalogAdmission
    terminal: Mapping[str, object]


def _refuse(code: str, message: str) -> None:
    raise SourceAdmissionCommandError(code, message)


def _canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _root(value: str | Path) -> Path:
    try:
        supplied = Path(value)
        root = supplied.resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise SourceAdmissionCommandError("source-admission-command-root-invalid", "Project root is unavailable") from error
    if supplied.is_symlink() or root.is_symlink() or not root.is_dir():
        _refuse("source-admission-command-root-invalid", "Project root must be a regular directory")
    return root


def _relative(value: object, *, field: str) -> PurePosixPath:
    if not isinstance(value, str) or not value or "\\" in value:
        _refuse("source-admission-command-invalid", f"{field} must be a non-empty normalized relative path")
    relative = PurePosixPath(value)
    if relative.is_absolute() or relative == PurePosixPath(".") or any(part in {"", ".", ".."} for part in relative.parts):
        _refuse("source-admission-command-invalid", f"{field} is unsafe")
    if any(part.startswith(".env") or part.endswith(".env") for part in relative.parts):
        _refuse("source-admission-command-invalid", f"{field} names protected state")
    return relative


def _regular_bytes(root: Path, relative: PurePosixPath, *, code: str, label: str) -> bytes:
    cursor = root
    try:
        for index, part in enumerate(relative.parts):
            cursor = cursor / part
            metadata = os.lstat(cursor)
            expected = stat.S_ISREG if index == len(relative.parts) - 1 else stat.S_ISDIR
            if stat.S_ISLNK(metadata.st_mode) or not expected(metadata.st_mode):
                _refuse(code, f"{label} is aliased or has an invalid carrier type")
        return cursor.read_bytes()
    except SourceAdmissionCommandError:
        raise
    except OSError as error:
        raise SourceAdmissionCommandError(code, f"{label} is unavailable") from error


def _ensure_directory(root: Path, relative: PurePosixPath) -> Path:
    cursor = root
    try:
        for part in relative.parts:
            cursor = cursor / part
            try:
                metadata = os.lstat(cursor)
            except FileNotFoundError:
                cursor.mkdir(mode=0o755)
                metadata = os.lstat(cursor)
            if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
                _refuse("source-admission-command-publish-invalid", "command receipt directory is aliased or invalid")
    except SourceAdmissionCommandError:
        raise
    except OSError as error:
        raise SourceAdmissionCommandError("source-admission-command-publish-failed", "cannot prepare command receipt directory") from error
    return cursor


def _publish_exact(directory: Path, filename: str, payload: bytes) -> Path:
    target = directory / filename
    try:
        metadata = os.lstat(directory)
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
            _refuse("source-admission-command-publish-invalid", "command receipt directory is invalid")
        try:
            existing = os.lstat(target)
        except FileNotFoundError:
            existing = None
        if existing is not None:
            if stat.S_ISLNK(existing.st_mode) or not stat.S_ISREG(existing.st_mode):
                _refuse("source-admission-command-publish-invalid", "command receipt target is aliased or invalid")
            if target.read_bytes() != payload:
                _refuse("source-admission-command-receipt-conflict", "existing command receipt differs")
            return target
        with tempfile.NamedTemporaryFile(dir=directory, prefix=".source-admission-", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        try:
            os.link(temporary, target)
        except FileExistsError:
            if _regular_bytes(directory, PurePosixPath(filename), code="source-admission-command-publish-invalid", label="command receipt") != payload:
                _refuse("source-admission-command-receipt-conflict", "concurrent command receipt differs")
        finally:
            temporary.unlink(missing_ok=True)
        return target
    except SourceAdmissionCommandError:
        raise
    except OSError as error:
        raise SourceAdmissionCommandError("source-admission-command-publish-failed", "cannot publish command receipt") from error


def _command_id(value: object) -> str:
    if not isinstance(value, str) or _COMMAND_ID.fullmatch(value) is None:
        _refuse("source-admission-command-invalid", "command_id has invalid syntax")
    return value


def _digest(value: object, *, field: str, code: str = "source-admission-command-receipt-invalid") -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        _refuse(code, f"{field} must be a lowercase SHA-256 digest")
    return value


def _text(value: object, *, field: str, code: str = "source-admission-command-receipt-invalid") -> str:
    if not isinstance(value, str) or not value or "\x00" in value or "\r" in value or "\n" in value:
        _refuse(code, f"{field} must be a non-empty single-line string")
    return value


def _action_source(value: object, *, code: str) -> dict[str, object]:
    if not isinstance(value, Mapping) or set(value) != _SOURCE_KEYS:
        _refuse(code, "action_source has an invalid closed schema")
    atom_id = value.get("atom_id")
    version = value.get("version")
    if atom_id != SOURCE_ADMISSION_ACTION_ID or type(version) is not int or version < 1:
        _refuse(code, "action_source is not CA-O-199")
    relative = _relative(value.get("path"), field="action_source.path")
    return {
        "atom_id": SOURCE_ADMISSION_ACTION_ID,
        "version": version,
        "path": relative.as_posix(),
        "sha256": _digest(value.get("sha256"), field="action_source.sha256", code=code),
    }


def _duplicate_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            _refuse("source-admission-command-receipt-invalid", "command receipt contains duplicate object keys")
        result[key] = value
    return result


def _reject_constant(value: str) -> object:
    _refuse("source-admission-command-receipt-invalid", f"command receipt contains non-JSON value: {value}")
    raise AssertionError("unreachable")


def build_source_admission_command_receipt(
    *,
    command_id: str,
    operator: str,
    journal_author: str,
    action_run_id: str,
    action_start_event_id: str,
    snapshot_sha256: str,
    action_source: Mapping[str, object],
    operators_registry_sha256: str,
) -> bytes:
    """Encode the exact D602 host-command receipt without a self-reference."""

    source = _action_source(action_source, code="source-admission-command-receipt-invalid")
    if work_journal.AUTHOR_RE.fullmatch(_text(journal_author, field="journal_author")) is None:
        _refuse("source-admission-command-receipt-invalid", "journal_author is not a Journal account")
    return _canonical_json({
        "schema_version": SCHEMA_VERSION,
        "operation": OPERATION,
        "command_id": _command_id(command_id),
        "operator": _text(operator, field="operator"),
        "journal_author": journal_author,
        "action_id": SOURCE_ADMISSION_ACTION_ID,
        "action_run_id": _text(action_run_id, field="action_run_id"),
        "action_start_event_id": _text(action_start_event_id, field="action_start_event_id"),
        "snapshot_sha256": _digest(snapshot_sha256, field="snapshot_sha256"),
        "action_source": source,
        "operators_registry_sha256": _digest(operators_registry_sha256, field="operators_registry_sha256"),
    })


def read_source_admission_command_receipt(
    payload: bytes | bytearray | memoryview,
    *,
    expected_sha256: str | None = None,
) -> SourceAdmissionCommandReceipt:
    """Read a canonical immutable command receipt and optionally bind its bytes."""

    if not isinstance(payload, (bytes, bytearray, memoryview)):
        _refuse("source-admission-command-receipt-invalid", "command receipt payload must be bytes")
    raw = bytes(payload)
    if expected_sha256 is not None and _sha256(raw) != _digest(expected_sha256, field="expected command receipt", code="source-admission-command-receipt-digest-mismatch"):
        _refuse("source-admission-command-receipt-digest-mismatch", "command receipt bytes differ from their identity")
    try:
        document = json.loads(raw.decode("utf-8"), object_pairs_hook=_duplicate_pairs, parse_constant=_reject_constant)
    except SourceAdmissionCommandError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise SourceAdmissionCommandError("source-admission-command-receipt-invalid", "command receipt is not canonical UTF-8 JSON") from error
    if not isinstance(document, Mapping) or set(document) != _RECEIPT_KEYS:
        _refuse("source-admission-command-receipt-invalid", "command receipt has an invalid closed schema")
    if type(document.get("schema_version")) is not int or document.get("schema_version") != SCHEMA_VERSION or document.get("operation") != OPERATION:
        _refuse("source-admission-command-receipt-invalid", "command receipt operation is invalid")
    journal_author = _text(document.get("journal_author"), field="journal_author")
    if work_journal.AUTHOR_RE.fullmatch(journal_author) is None:
        _refuse("source-admission-command-receipt-invalid", "journal_author is not a Journal account")
    result = SourceAdmissionCommandReceipt(
        command_id=_command_id(document.get("command_id")),
        operator=_text(document.get("operator"), field="operator"),
        journal_author=journal_author,
        action_run_id=_text(document.get("action_run_id"), field="action_run_id"),
        action_start_event_id=_text(document.get("action_start_event_id"), field="action_start_event_id"),
        snapshot_sha256=_digest(document.get("snapshot_sha256"), field="snapshot_sha256"),
        action_source=_action_source(document.get("action_source"), code="source-admission-command-receipt-invalid"),
        operators_registry_sha256=_digest(document.get("operators_registry_sha256"), field="operators_registry_sha256"),
        sha256=_sha256(raw),
        payload=raw,
    )
    if document.get("action_id") != SOURCE_ADMISSION_ACTION_ID or raw != _canonical_json(dict(document)):
        _refuse("source-admission-command-receipt-invalid", "command receipt is noncanonical or names another Action")
    return result


def _operator_record(root: Path, registry_ref: PurePosixPath, operator: object) -> tuple[OperatorRegistryRecord, bytes, str]:
    name = _text(operator, field="operator", code="source-admission-command-operator-invalid")
    payload = _regular_bytes(root, registry_ref, code="source-admission-command-operator-invalid", label="registered Operator evidence")
    try:
        records = parse_operators_registry(payload)
    except OperatorRegistryError as error:
        raise SourceAdmissionCommandError("source-admission-command-operator-invalid", "registered Operator evidence is invalid") from error
    matching = [record for record in records if record.name == name]
    if len(matching) != 1:
        _refuse("source-admission-command-operator-invalid", "Operator is not uniquely registered for this Project")
    record = matching[0]
    author = record.journal_author
    if author is None and work_journal.AUTHOR_RE.fullmatch(record.name) is not None:
        author = record.name
    if author is None:
        _refuse("source-admission-command-operator-invalid", "Operator has no explicit Journal author mapping")
    return record, payload, author


def _command_ref(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError as error:
        raise SourceAdmissionCommandError("source-admission-command-publish-invalid", "command receipt escapes Project root") from error


def _receipt_binder(
    root: Path,
    receipt_path: Path,
    receipt_sha256: str,
    *,
    expected_operator: str,
    expected_registry_sha256: str,
    expected_source: Mapping[str, object],
) -> callable:
    command_ref = _command_ref(receipt_path, root)
    relative = _relative(command_ref, field="command_ref")

    def bind(request: AdmissionInvocationRequest, provenance: object) -> tuple[str, str]:
        raw = _regular_bytes(root, relative, code="source-admission-command-receipt-invalid", label="command receipt")
        receipt = read_source_admission_command_receipt(raw, expected_sha256=receipt_sha256)
        if (
            receipt.snapshot_sha256 != request.snapshot_sha256
            or receipt.operator != expected_operator
            or receipt.operators_registry_sha256 != expected_registry_sha256
            or dict(receipt.action_source) != dict(expected_source)
            or receipt.action_run_id != getattr(provenance, "action_run_id", None)
            or receipt.action_start_event_id != getattr(provenance, "event_id", None)
            or receipt.journal_author != getattr(provenance, "author", None)
        ):
            _refuse("source-admission-command-receipt-mismatch", "command receipt differs from current direct Action provenance")
        return receipt.operator, command_ref

    return bind


def run_source_admission_command(
    candidate: ValidatedCandidate,
    private_compilation: SealedPrivateMethodologyCompilation,
    *,
    candidate_run_id: str,
    operator: str,
    command_id: str,
    operators_registry_ref: str,
) -> SourceAdmissionCommandResult:
    """Run the explicitly commanded direct O199 boundary through D602 output.

    ``candidate`` and ``private_compilation`` must be actual sealed evidence;
    this entry point never accepts catalog rows, a selected-run envelope, or a
    caller-supplied approval flag.  Any error after the start leaves that exact
    canonical start for recovery rather than recording a guessed outcome.
    """

    if not isinstance(candidate, ValidatedCandidate) or not isinstance(private_compilation, SealedPrivateMethodologyCompilation):
        _refuse("source-admission-command-untrusted", "source admission requires actual sealed candidate and private compilation")
    root = _root(candidate.project_root)
    registry_ref = _relative(operators_registry_ref, field="operators_registry_ref")
    command = _command_id(command_id)
    snapshot = collect_portable_source_snapshot(candidate, private_compilation, candidate_run_id=candidate_run_id)
    snapshot = revalidate_portable_source_snapshot(snapshot)
    if _root(snapshot.candidate.project_root) != root:
        _refuse("source-admission-command-project-mismatch", "sealed source snapshot belongs to another Project")
    requested_run_id = "source-admission:" + _sha256(command.encode("utf-8"))
    authorization_ref = "source-admission-command/" + command
    record, _registry_bytes, journal_author = _operator_record(root, registry_ref, operator)
    session = DirectActionSession(
        root,
        author=journal_author,
        operator_authorization={"operator": record.name, "authorization_ref": authorization_ref},
        action_id=SOURCE_ADMISSION_ACTION_ID,
        operators_registry_ref=registry_ref.as_posix(),
    )
    state: dict[str, object] = {}

    def admitter(request: AdmissionInvocationRequest):
        # The writer, rather than a caller, supplies the exact D602 descriptor
        # checksum.  Start only after that observation is available.
        if state:
            _refuse("source-admission-command-start-invalid", "one command cannot bind more than one source snapshot")
        current_record, current_registry, current_author = _operator_record(root, registry_ref, operator)
        registry_sha256 = _sha256(current_registry)
        started = session.begin_action(
            action_id=SOURCE_ADMISSION_ACTION_ID,
            requested_run_id=requested_run_id,
            intent={
                "action_id": SOURCE_ADMISSION_ACTION_ID,
                "kind": "local_package_source_admission",
                "snapshot_sha256": request.snapshot_sha256,
                "operators_registry_sha256": registry_sha256,
            },
        )
        run_id = started["run_id"]
        actual = session.actual.get(run_id)
        binding = actual.get("binding") if isinstance(actual, Mapping) else None
        if not isinstance(binding, Mapping):
            _refuse("source-admission-command-start-invalid", "direct Action start lacks its actual source binding")
        source = {
            "atom_id": binding.get("atom_id"), "version": binding.get("version"),
            "path": binding.get("path"), "sha256": binding.get("digest"),
        }
        receipt_bytes = build_source_admission_command_receipt(
            command_id=command,
            operator=current_record.name,
            journal_author=current_author,
            action_run_id=run_id,
            action_start_event_id=str(started["event_id"]),
            snapshot_sha256=request.snapshot_sha256,
            action_source=source,
            operators_registry_sha256=registry_sha256,
        )
        receipt = read_source_admission_command_receipt(receipt_bytes)
        directory = _ensure_directory(root, PurePosixPath(*COMMAND_DIRECTORY.parts))
        receipt_path = _publish_exact(directory, f"{receipt.sha256}.json", receipt_bytes)
        reopened = read_source_admission_command_receipt(
            _regular_bytes(root, _relative(_command_ref(receipt_path, root), field="command_ref"),
                           code="source-admission-command-receipt-invalid", label="command receipt"),
            expected_sha256=receipt.sha256,
        )
        if reopened != receipt:
            _refuse("source-admission-command-receipt-mismatch", "published command receipt differs from its command")
        binder = _receipt_binder(
            root, receipt_path, receipt.sha256,
            expected_operator=current_record.name,
            expected_registry_sha256=registry_sha256,
            expected_source=source,
        )
        state.update({
            "started": started,
            "run_id": run_id,
            "receipt": reopened,
            "receipt_path": receipt_path,
        })
        return make_direct_source_admission_invocation_admitter(
            root,
            action_session=session,
            action_run_id=run_id,
            operators_registry_ref=registry_ref.as_posix(),
            command_binder=binder,
        )(request)

    with session:
        admission = admit_package_sources(root, snapshot, invocation_admitter=admitter)
        started = state.get("started")
        run_id = state.get("run_id")
        receipt = state.get("receipt")
        receipt_path = state.get("receipt_path")
        if (
            not isinstance(started, Mapping)
            or not isinstance(run_id, str)
            or not isinstance(receipt, SourceAdmissionCommandReceipt)
            or not isinstance(receipt_path, Path)
        ):
            _refuse("source-admission-command-start-invalid", "admission completed without one direct Action command binding")
        effects = [_command_ref(receipt_path, root), _command_ref(admission.receipt_path, root), _command_ref(admission.catalog_path, root)]
        session.record_effects(run_id, result_ref=effects[1], effect_refs=effects)
        terminal = session.finish_action(run_id, outcome="completed", result_ref=effects[1], effect_refs=effects)
        return SourceAdmissionCommandResult(snapshot, receipt, receipt_path, dict(started), admission, terminal)


__all__ = [
    "COMMAND_DIRECTORY",
    "OPERATION",
    "SCHEMA_VERSION",
    "SourceAdmissionCommandError",
    "SourceAdmissionCommandReceipt",
    "SourceAdmissionCommandResult",
    "build_source_admission_command_receipt",
    "read_source_admission_command_receipt",
    "run_source_admission_command",
]
