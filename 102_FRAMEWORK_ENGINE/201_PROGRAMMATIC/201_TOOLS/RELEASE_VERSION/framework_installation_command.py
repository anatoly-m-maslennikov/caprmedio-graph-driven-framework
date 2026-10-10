"""Retain and bind one direct CA-O-200 installation command.

This boundary prepares no package copy, selector, runtime process, or target
configuration.  It retains D604's closed command input, records/reopens the
actual direct Action start, and returns that still-open Run to the later
publisher.  A caller-provided boolean, selected-workflow envelope, or current
checkout Action source is deliberately not an authorization substitute.
"""

from __future__ import annotations

import hashlib
import json
import os
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import tempfile
from typing import Any


_TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(_TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_TOOLS_ROOT))

from direct_action_session import (
    INSTALLATION_ACTION_ID,
    INSTALLATION_ATOM_RELATIVE,
    INSTALLATION_ATOM_SHA256,
    INSTALLATION_ATOM_VERSION,
    DirectActionJournalError,
    DirectActionSession,
)
from framework_package import FrameworkPackageError, VerifiedFrameworkPackage, verify_framework_package
from installation_context import (
    REGISTRY_FILENAME,
    InstallationContextError,
    TargetProjectContext,
    TargetProjectRequest,
    bind_target_project_context,
)
from operator_registry import OperatorRegistryError, OperatorRegistryRecord, parse_operators_registry
import work_journal


SCHEMA_VERSION = 1
OPERATION = "install_framework_runtime"
COMMAND_DIRECTORY = Path(".caprmedio_runtime/installation/commands")
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_COMMAND_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,159}\Z")
_RECEIPT_KEYS = frozenset(
    {
        "schema_version",
        "operation",
        "command_id",
        "operator",
        "journal_author",
        "operators_registry_sha256",
        "action_source",
        "target_project_context_sha256",
        "package_manifest_sha256",
        "full_gate_receipt_sha256",
        "prior_runtime_selector_sha256",
    }
)
_SOURCE_KEYS = frozenset({"atom_id", "version", "path", "sha256"})
_PRIOR_RUNTIME_SELECTORS = (
    PurePosixPath(".caprmedio_runtime/installation/current.toml"),
    # ``installation_state.LEGACY_SELECTOR`` is the prior migration surface;
    # package selection is not inferred from an arbitrary framework checkout.
    PurePosixPath(".caprmedio_install/current.toml"),
)


class FrameworkInstallationCommandError(RuntimeError):
    """Stable refusal from the O-200/D604 command boundary."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


@dataclass(frozen=True)
class FrameworkInstallationCommandRequest:
    """Closed inputs for one retained, direct O-200 command.

    ``full_gate_receipt_sha256`` is a retained evidence identity, not a pass
    assertion.  The later publisher owns physical Full Gate reopening before
    it is allowed to copy or select anything.
    """

    target: TargetProjectRequest
    target_context: TargetProjectContext
    package: VerifiedFrameworkPackage
    full_gate_receipt_sha256: str
    command_id: str
    operator: str


@dataclass(frozen=True)
class FrameworkInstallationCommandReceipt:
    """One canonical D604 command input, addressed by its exact bytes."""

    command_id: str
    operator: str
    journal_author: str
    operators_registry_sha256: str
    action_source: Mapping[str, object]
    target_project_context_sha256: str
    package_manifest_sha256: str
    full_gate_receipt_sha256: str
    prior_runtime_selector_sha256: str | None
    sha256: str
    payload: bytes


@dataclass(frozen=True)
class FrameworkInstallationCommandResult:
    """One reopened receipt plus the actual still-open O-200 direct Run."""

    target_context: TargetProjectContext
    package: VerifiedFrameworkPackage
    command_receipt: FrameworkInstallationCommandReceipt
    command_receipt_path: Path
    action_start: Mapping[str, object]
    action_provenance: object
    action_session: DirectActionSession


def _refuse(code: str, message: str) -> None:
    raise FrameworkInstallationCommandError(code, message)


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _text(value: object, *, field: str, code: str = "installation-command-receipt-invalid") -> str:
    if not isinstance(value, str) or not value or "\x00" in value or "\r" in value or "\n" in value:
        _refuse(code, f"{field} must be a non-empty single-line string")
    return value


def _digest(value: object, *, field: str, code: str = "installation-command-receipt-invalid") -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        _refuse(code, f"{field} must be a lowercase SHA-256 digest")
    return value


def _command_id(value: object) -> str:
    if not isinstance(value, str) or _COMMAND_ID.fullmatch(value) is None:
        _refuse("installation-command-invalid", "command_id has invalid syntax")
    return value


def _relative(value: object, *, field: str) -> PurePosixPath:
    if not isinstance(value, str) or not value or "\\" in value:
        _refuse("installation-command-invalid", f"{field} must be a normalized Project-relative path")
    relative = PurePosixPath(value)
    if relative.is_absolute() or relative == PurePosixPath(".") or any(part in {"", ".", ".."} for part in relative.parts):
        _refuse("installation-command-invalid", f"{field} is unsafe")
    if any(part.startswith(".env") or part.endswith(".env") for part in relative.parts):
        _refuse("installation-command-invalid", f"{field} names protected state")
    return relative


def _regular_bytes(root: Path, relative: PurePosixPath, *, code: str, label: str) -> bytes:
    cursor = root
    try:
        for index, part in enumerate(relative.parts):
            cursor = cursor / part
            observed = os.lstat(cursor)
            expected = stat.S_ISREG if index == len(relative.parts) - 1 else stat.S_ISDIR
            if stat.S_ISLNK(observed.st_mode) or not expected(observed.st_mode):
                _refuse(code, f"{label} is aliased or has an invalid carrier type")
        before = (observed.st_dev, observed.st_ino, observed.st_size, observed.st_mtime_ns)
        payload = cursor.read_bytes()
        after = cursor.stat()
        if before != (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns):
            _refuse(code, f"{label} changed while being reopened")
        return payload
    except FrameworkInstallationCommandError:
        raise
    except OSError as error:
        raise FrameworkInstallationCommandError(code, f"{label} is unavailable") from error


def _optional_regular_bytes(root: Path, relative: PurePosixPath, *, label: str) -> bytes | None:
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
                _refuse("installation-command-prior-selector-invalid", f"{label} is aliased or invalid")
        before = (observed.st_dev, observed.st_ino, observed.st_size, observed.st_mtime_ns)
        payload = cursor.read_bytes()
        after = cursor.stat()
        if before != (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns):
            _refuse("installation-command-prior-selector-invalid", f"{label} changed while being reopened")
        return payload
    except FrameworkInstallationCommandError:
        raise
    except OSError as error:
        raise FrameworkInstallationCommandError("installation-command-prior-selector-invalid", f"{label} is unavailable") from error


def _root(value: object) -> Path:
    try:
        supplied = Path(value)
        if not supplied.is_absolute() or ".." in supplied.parts:
            _refuse("installation-command-root-invalid", "target Project root must be an absolute normalized directory")
        root = Path(os.path.abspath(supplied))
        for candidate in (root, *root.parents):
            if candidate.is_symlink():
                _refuse("installation-command-root-invalid", "target Project root has a symlinked ancestor")
        observed = root.lstat()
        if not stat.S_ISDIR(observed.st_mode):
            _refuse("installation-command-root-invalid", "target Project root must be a directory")
        return root
    except FrameworkInstallationCommandError:
        raise
    except (OSError, TypeError, ValueError) as error:
        raise FrameworkInstallationCommandError("installation-command-root-invalid", "target Project root is unavailable") from error


def _action_source(value: object, *, code: str) -> dict[str, object]:
    if not isinstance(value, Mapping) or set(value) != _SOURCE_KEYS:
        _refuse(code, "action_source has an invalid closed schema")
    if value.get("atom_id") != INSTALLATION_ACTION_ID or value.get("version") != INSTALLATION_ATOM_VERSION:
        _refuse(code, "action_source is not CA-O-200@1")
    relative = _relative(value.get("path"), field="action_source.path")
    if relative.as_posix() != INSTALLATION_ATOM_RELATIVE.as_posix():
        _refuse(code, "action_source path is not the admitted package Methodology carrier")
    if _digest(value.get("sha256"), field="action_source.sha256", code=code) != INSTALLATION_ATOM_SHA256:
        _refuse(code, "action_source digest is not the admitted CA-O-200 source")
    return {
        "atom_id": INSTALLATION_ACTION_ID,
        "version": INSTALLATION_ATOM_VERSION,
        "path": relative.as_posix(),
        "sha256": INSTALLATION_ATOM_SHA256,
    }


def _duplicate_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            _refuse("installation-command-receipt-invalid", "command receipt contains duplicate object keys")
        result[key] = value
    return result


def _reject_constant(value: str) -> object:
    _refuse("installation-command-receipt-invalid", f"command receipt contains non-JSON value: {value}")
    raise AssertionError("unreachable")


def build_framework_installation_command_receipt(
    *,
    command_id: str,
    operator: str,
    journal_author: str,
    operators_registry_sha256: str,
    action_source: Mapping[str, object],
    target_project_context_sha256: str,
    package_manifest_sha256: str,
    full_gate_receipt_sha256: str,
    prior_runtime_selector_sha256: str | None,
) -> bytes:
    """Encode D604's exact pre-start command input without self-digest."""

    author = _text(journal_author, field="journal_author")
    if work_journal.AUTHOR_RE.fullmatch(author) is None:
        _refuse("installation-command-receipt-invalid", "journal_author is not a Journal account")
    prior = None if prior_runtime_selector_sha256 is None else _digest(
        prior_runtime_selector_sha256,
        field="prior_runtime_selector_sha256",
    )
    return _canonical_json(
        {
            "schema_version": SCHEMA_VERSION,
            "operation": OPERATION,
            "command_id": _command_id(command_id),
            "operator": _text(operator, field="operator"),
            "journal_author": author,
            "operators_registry_sha256": _digest(operators_registry_sha256, field="operators_registry_sha256"),
            "action_source": _action_source(action_source, code="installation-command-receipt-invalid"),
            "target_project_context_sha256": _digest(
                target_project_context_sha256, field="target_project_context_sha256"
            ),
            "package_manifest_sha256": _digest(package_manifest_sha256, field="package_manifest_sha256"),
            "full_gate_receipt_sha256": _digest(full_gate_receipt_sha256, field="full_gate_receipt_sha256"),
            "prior_runtime_selector_sha256": prior,
        }
    )


def read_framework_installation_command_receipt(
    payload: bytes | bytearray | memoryview,
    *,
    expected_sha256: str | None = None,
) -> FrameworkInstallationCommandReceipt:
    """Strictly reopen one canonical, digest-addressed D604 command input."""

    if not isinstance(payload, (bytes, bytearray, memoryview)):
        _refuse("installation-command-receipt-invalid", "command receipt payload must be bytes")
    raw = bytes(payload)
    if expected_sha256 is not None and _sha256(raw) != _digest(
        expected_sha256, field="expected command receipt", code="installation-command-receipt-digest-mismatch"
    ):
        _refuse("installation-command-receipt-digest-mismatch", "command receipt bytes differ from their identity")
    try:
        document = json.loads(raw.decode("utf-8"), object_pairs_hook=_duplicate_pairs, parse_constant=_reject_constant)
    except FrameworkInstallationCommandError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise FrameworkInstallationCommandError("installation-command-receipt-invalid", "command receipt is not canonical UTF-8 JSON") from error
    if not isinstance(document, Mapping) or set(document) != _RECEIPT_KEYS:
        _refuse("installation-command-receipt-invalid", "command receipt has an invalid closed schema")
    if type(document.get("schema_version")) is not int or document.get("schema_version") != SCHEMA_VERSION or document.get("operation") != OPERATION:
        _refuse("installation-command-receipt-invalid", "command receipt operation is invalid")
    author = _text(document.get("journal_author"), field="journal_author")
    if work_journal.AUTHOR_RE.fullmatch(author) is None:
        _refuse("installation-command-receipt-invalid", "journal_author is not a Journal account")
    prior = document.get("prior_runtime_selector_sha256")
    if prior is not None:
        prior = _digest(prior, field="prior_runtime_selector_sha256")
    result = FrameworkInstallationCommandReceipt(
        command_id=_command_id(document.get("command_id")),
        operator=_text(document.get("operator"), field="operator"),
        journal_author=author,
        operators_registry_sha256=_digest(document.get("operators_registry_sha256"), field="operators_registry_sha256"),
        action_source=_action_source(document.get("action_source"), code="installation-command-receipt-invalid"),
        target_project_context_sha256=_digest(
            document.get("target_project_context_sha256"), field="target_project_context_sha256"
        ),
        package_manifest_sha256=_digest(document.get("package_manifest_sha256"), field="package_manifest_sha256"),
        full_gate_receipt_sha256=_digest(document.get("full_gate_receipt_sha256"), field="full_gate_receipt_sha256"),
        prior_runtime_selector_sha256=prior,
        sha256=_sha256(raw),
        payload=raw,
    )
    if raw != _canonical_json(dict(document)):
        _refuse("installation-command-receipt-invalid", "command receipt is noncanonical")
    return result


def _ensure_directory(root: Path, relative: PurePosixPath) -> Path:
    cursor = root
    try:
        for part in relative.parts:
            cursor = cursor / part
            try:
                observed = os.lstat(cursor)
            except FileNotFoundError:
                cursor.mkdir(mode=0o700)
                observed = os.lstat(cursor)
            if stat.S_ISLNK(observed.st_mode) or not stat.S_ISDIR(observed.st_mode):
                _refuse("installation-command-publish-invalid", "command receipt directory is aliased or invalid")
        return cursor
    except FrameworkInstallationCommandError:
        raise
    except OSError as error:
        raise FrameworkInstallationCommandError("installation-command-publish-failed", "cannot prepare command receipt directory") from error


def _publish_exact(directory: Path, filename: str, payload: bytes) -> Path:
    target = directory / filename
    try:
        try:
            existing = os.lstat(target)
        except FileNotFoundError:
            existing = None
        if existing is not None:
            if stat.S_ISLNK(existing.st_mode) or not stat.S_ISREG(existing.st_mode) or existing.st_nlink != 1:
                _refuse("installation-command-publish-invalid", "command receipt target is aliased or invalid")
            if target.read_bytes() != payload:
                _refuse("installation-command-receipt-conflict", "existing command receipt differs")
            return target
        descriptor, temporary_name = tempfile.mkstemp(prefix=".installation-command-", dir=directory)
        temporary = Path(temporary_name)
        try:
            os.fchmod(descriptor, 0o600)
            with os.fdopen(descriptor, "wb", closefd=True) as stream:
                stream.write(payload)
                stream.flush()
                os.fsync(stream.fileno())
            try:
                os.link(temporary, target)
            except FileExistsError:
                if target.read_bytes() != payload:
                    _refuse("installation-command-receipt-conflict", "concurrent command receipt differs")
            return target
        finally:
            temporary.unlink(missing_ok=True)
    except FrameworkInstallationCommandError:
        raise
    except OSError as error:
        raise FrameworkInstallationCommandError("installation-command-publish-failed", "cannot publish command receipt") from error


def _registry_reference(request: TargetProjectRequest, context: TargetProjectContext, root: Path) -> PurePosixPath:
    expected = root / context.control_child_relpath / REGISTRY_FILENAME
    try:
        supplied = Path(request.operators_registry_path)
        if not supplied.is_absolute() or supplied != expected:
            _refuse("installation-command-registry-invalid", "operators registry must be the exact selected target control carrier")
        return _relative(supplied.relative_to(root).as_posix(), field="operators_registry_ref")
    except FrameworkInstallationCommandError:
        raise
    except (TypeError, ValueError) as error:
        raise FrameworkInstallationCommandError("installation-command-registry-invalid", "operators registry reference is invalid") from error


def _operator_record(root: Path, registry_ref: PurePosixPath, operator: object) -> tuple[OperatorRegistryRecord, bytes, str]:
    name = _text(operator, field="operator", code="installation-command-operator-invalid")
    payload = _regular_bytes(root, registry_ref, code="installation-command-operator-invalid", label="registered Operator evidence")
    try:
        records = parse_operators_registry(payload)
    except OperatorRegistryError as error:
        raise FrameworkInstallationCommandError("installation-command-operator-invalid", "registered Operator evidence is invalid") from error
    matches = [record for record in records if record.name == name]
    if len(matches) != 1:
        _refuse("installation-command-operator-invalid", "Operator is not uniquely registered for this Project")
    record = matches[0]
    author = record.journal_author
    if author is None and work_journal.AUTHOR_RE.fullmatch(record.name) is not None:
        author = record.name
    if author is None:
        _refuse("installation-command-operator-invalid", "Operator has no explicit Journal author mapping")
    return record, payload, author


def _revalidate_request(request: FrameworkInstallationCommandRequest) -> tuple[Path, TargetProjectContext, VerifiedFrameworkPackage]:
    if not isinstance(request, FrameworkInstallationCommandRequest):
        _refuse("installation-command-untrusted", "installation command requires a typed request")
    if not isinstance(request.target, TargetProjectRequest) or not isinstance(request.target_context, TargetProjectContext):
        _refuse("installation-command-untrusted", "installation command requires typed target context inputs")
    if not isinstance(request.package, VerifiedFrameworkPackage):
        _refuse("installation-command-untrusted", "installation command requires a typed verified Framework package")
    root = _root(request.target.target_root)
    try:
        context = bind_target_project_context(request.target)
    except InstallationContextError as error:
        raise FrameworkInstallationCommandError("installation-command-context-stale", "target controls cannot be revalidated") from error
    if context != request.target_context:
        _refuse("installation-command-context-stale", "typed target context differs from current controls")
    try:
        package = verify_framework_package(request.target.package_root)
    except FrameworkPackageError as error:
        raise FrameworkInstallationCommandError("installation-command-package-invalid", "Framework package cannot be physically reopened") from error
    if package != request.package:
        _refuse("installation-command-package-stale", "typed Framework package differs from current package bytes")
    if (
        package.manifest_digest != context.package_evidence.package_manifest_sha256
        or package.source_catalog_sha256 != context.package_evidence.catalog_sha256
    ):
        _refuse("installation-command-package-mismatch", "target context no longer binds the reopened package")
    return root, context, package


def _prior_runtime_selector_sha256(root: Path) -> str | None:
    observed: list[tuple[str, str]] = []
    for relative in _PRIOR_RUNTIME_SELECTORS:
        payload = _optional_regular_bytes(root, relative, label="prior runtime selector")
        if payload is not None:
            observed.append((relative.as_posix(), _sha256(payload)))
    if len(observed) > 1:
        _refuse("installation-command-prior-selector-ambiguous", "both native and legacy runtime selectors are present")
    return observed[0][1] if observed else None


def _relative_to_root(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError as error:
        raise FrameworkInstallationCommandError("installation-command-publish-invalid", "command receipt escapes target Project root") from error


def run_framework_installation_command(
    request: FrameworkInstallationCommandRequest,
) -> FrameworkInstallationCommandResult:
    """Retain D604 input then start/reopen the exact direct O-200 Action.

    Success deliberately leaves ``action_session`` open.  The subsequent
    installation publisher must retain/reopen all further proof, observe real
    effects, and append the terminal Journal outcome itself.
    """

    root, context, package = _revalidate_request(request)
    command_id = _command_id(request.command_id)
    full_gate = _digest(request.full_gate_receipt_sha256, field="full_gate_receipt_sha256", code="installation-command-invalid")
    registry_ref = _registry_reference(request.target, context, root)
    record, registry_payload, journal_author = _operator_record(root, registry_ref, request.operator)
    registry_sha256 = _sha256(registry_payload)
    prior = _prior_runtime_selector_sha256(root)
    source = {
        "atom_id": INSTALLATION_ACTION_ID,
        "version": INSTALLATION_ATOM_VERSION,
        "path": INSTALLATION_ATOM_RELATIVE.as_posix(),
        "sha256": INSTALLATION_ATOM_SHA256,
    }
    payload = build_framework_installation_command_receipt(
        command_id=command_id,
        operator=record.name,
        journal_author=journal_author,
        operators_registry_sha256=registry_sha256,
        action_source=source,
        target_project_context_sha256=context.sha256,
        package_manifest_sha256=package.manifest_digest,
        full_gate_receipt_sha256=full_gate,
        prior_runtime_selector_sha256=prior,
    )
    receipt = read_framework_installation_command_receipt(payload)
    directory = _ensure_directory(root, PurePosixPath(*COMMAND_DIRECTORY.parts))
    receipt_path = _publish_exact(directory, f"{receipt.sha256}.json", payload)
    relative_receipt = _relative(_relative_to_root(root, receipt_path), field="command_ref")
    if read_framework_installation_command_receipt(
        _regular_bytes(root, relative_receipt, code="installation-command-receipt-invalid", label="command receipt"),
        expected_sha256=receipt.sha256,
    ) != receipt:
        _refuse("installation-command-receipt-mismatch", "published command receipt differs from exact input")
    session = DirectActionSession(
        root,
        author=journal_author,
        operator_authorization={"operator": record.name, "authorization_ref": "installation-command/" + command_id},
        action_id=INSTALLATION_ACTION_ID,
        action_package=package,
        operators_registry_ref=registry_ref.as_posix(),
    )
    started = None
    try:
        started = session.begin_action(
            action_id=INSTALLATION_ACTION_ID,
            requested_run_id="installation-command:" + _sha256(command_id.encode("utf-8")),
            intent={
                "action_id": INSTALLATION_ACTION_ID,
                "kind": "install_one_admitted_project_runtime",
                "installation_command_sha256": receipt.sha256,
                "target_project_context_sha256": context.sha256,
                "package_manifest_sha256": package.manifest_digest,
                "full_gate_receipt_sha256": full_gate,
                "prior_runtime_selector_sha256": prior,
                "operators_registry_sha256": registry_sha256,
            },
        )
        run_id = started.get("run_id") if isinstance(started, Mapping) else None
        if not isinstance(run_id, str):
            _refuse("installation-command-start-invalid", "direct Action did not return a Run identity")
        actual = session.actual.get(run_id)
        binding = actual.get("binding") if isinstance(actual, Mapping) else None
        if not isinstance(binding, Mapping) or {
            "atom_id": binding.get("atom_id"),
            "version": binding.get("version"),
            "path": binding.get("path"),
            "sha256": binding.get("digest"),
        } != source:
            _refuse("installation-command-source-mismatch", "started Action source differs from retained command source")
        provenance = session.read_recorded_action_start(run_id)
        # The durable start itself may have succeeded while target controls,
        # package, registry, or receipt changed.  Stop before any installation
        # effect and leave that exact start for recovery in this case.
        check_root, check_context, check_package = _revalidate_request(request)
        check_record, check_registry, check_author = _operator_record(check_root, registry_ref, request.operator)
        reopened = read_framework_installation_command_receipt(
            _regular_bytes(check_root, relative_receipt, code="installation-command-receipt-invalid", label="command receipt"),
            expected_sha256=receipt.sha256,
        )
        if (
            check_root != root
            or check_context != context
            or check_package != package
            or check_record.name != record.name
            or check_author != journal_author
            or _sha256(check_registry) != registry_sha256
            or reopened != receipt
        ):
            _refuse("installation-command-stale", "installation command inputs changed before staging")
        return FrameworkInstallationCommandResult(
            target_context=context,
            package=package,
            command_receipt=receipt,
            command_receipt_path=receipt_path,
            action_start=dict(started),
            action_provenance=provenance,
            action_session=session,
        )
    except (DirectActionJournalError, FrameworkInstallationCommandError):
        session.close()
        raise
    except BaseException:
        session.close()
        raise


__all__ = [
    "COMMAND_DIRECTORY",
    "FrameworkInstallationCommandError",
    "FrameworkInstallationCommandReceipt",
    "FrameworkInstallationCommandRequest",
    "FrameworkInstallationCommandResult",
    "OPERATION",
    "SCHEMA_VERSION",
    "build_framework_installation_command_receipt",
    "read_framework_installation_command_receipt",
    "run_framework_installation_command",
]
