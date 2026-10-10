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
from dataclasses import dataclass, field
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
from retained_full_gate_packet import RetainedNativeFullGatePacket
import work_journal


SCHEMA_VERSION = 1
OPERATION = "install_framework_runtime"
COMMAND_DIRECTORY = Path(".caprmedio_runtime/installation/commands")
RESULT_DIRECTORY = Path(".caprmedio_tmp/installation/results")
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
_RESULT_KEYS = frozenset(
    {
        "schema_version",
        "action_id",
        "action_run_id",
        "installation_command_sha256",
        "package_manifest_sha256",
        "target_project_context_sha256",
        "state_generation",
        "effect_outcome",
        "reason",
        "effects",
    }
)
_RESULT_OUTCOMES = frozenset(
    {"completed", "blocked_before_delete", "unavailable_after_delete", "effect_uncertain"}
)
_FULL_GATE_EFFECT_KINDS = (
    "full_gate_receipt",
    "retained_candidate_descriptor",
    "retained_package_sidecar",
    "unit_gate_receipt",
    "build_receipt",
    "verification_receipt",
    "e2e_gate_receipt",
)
_PRIOR_RUNTIME_SELECTORS = (
    PurePosixPath(".caprmedio_runtime/installation/current.toml"),
    # The legacy Framework selector is the old execution binding.  The
    # adjacent ``.caprmedio_install/current.toml`` is a distinct Tool package
    # selector and cannot stand in for this D604 predecessor identity.
    PurePosixPath(".caprmedio_runtime/framework/current.toml"),
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


@dataclass(frozen=True)
class DirectInstallationEffect:
    """One immutable, Project-contained carrier observed for an O200 result."""

    kind: str
    reference: str
    sha256: str


@dataclass(frozen=True)
class _ObservedDirectFullGateClosure:
    """Private, process-local provenance for one physical packet observation.

    D604 retains effect rows in the public direct result, but the rows alone
    must never become an authorization substitute.  This capability is set
    only by the physical Full-Gate reader and is bound to the exact still-open
    O-200 Session.  It is deliberately neither serialized nor comparable.
    """

    action_session: DirectActionSession
    action_run_id: str
    installation_command_sha256: str
    package_manifest_sha256: str
    target_project_context_sha256: str
    full_gate_receipt_sha256: str
    packet: RetainedNativeFullGatePacket


@dataclass(frozen=True)
class DirectFullGateEffectClosure:
    """The seven original Full Gate carriers reopened before replacement.

    This is deliberately a small receipt of the physical re-open, rather than
    a second Full Gate model.  Later result recording consumes these exact
    references after replacement, so it never tries to rediscover a receipt
    from a digest or from whatever gate happens to be newest.
    """

    action_run_id: str
    installation_command_sha256: str
    package_manifest_sha256: str
    target_project_context_sha256: str
    full_gate_receipt_sha256: str
    effects: tuple[DirectInstallationEffect, ...]
    _observation: _ObservedDirectFullGateClosure | None = field(
        default=None,
        init=False,
        repr=False,
        compare=False,
    )


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


def reopen_framework_installation_command_start(
    project_root: str | Path,
    receipt: FrameworkInstallationCommandReceipt,
    *,
    action_package: VerifiedFrameworkPackage,
    operators_registry_ref: str | Path,
) -> Mapping[str, object]:
    """Reopen the exact historical direct O200 start named by ``receipt``.

    This is a reader only.  It deliberately rebuilds the deterministic direct
    Action identity from the immutable command, rereads the selected registry
    and package-owned Methodology source, then validates the canonical Journal
    event through the existing direct-Action validator.  It does not recreate
    a Session run, append Journal evidence, or grant execution authority.
    """

    if type(receipt) is not FrameworkInstallationCommandReceipt:
        _refuse("installation-command-untrusted", "installation command must be closed typed evidence")
    if not isinstance(action_package, VerifiedFrameworkPackage):
        _refuse("installation-command-package-invalid", "installation command needs a typed selected Framework package")
    if action_package.manifest_digest != receipt.package_manifest_sha256:
        _refuse("installation-command-package-mismatch", "selected package differs from retained command package")
    root = _root(project_root)
    registry_ref = _relative(str(operators_registry_ref), field="operators_registry_ref")
    canonical = COMMAND_DIRECTORY / f"{receipt.sha256}.json"
    if read_framework_installation_command_receipt(
        _regular_bytes(root, PurePosixPath(canonical.as_posix()), code="installation-command-receipt-invalid", label="command receipt"),
        expected_sha256=receipt.sha256,
    ) != receipt:
        _refuse("installation-command-stale", "installation command differs from its retained carrier")
    record, registry, author = _operator_record(root, registry_ref, receipt.operator)
    if author != receipt.journal_author or _sha256(registry) != receipt.operators_registry_sha256:
        _refuse("installation-command-operator-invalid", "installation command differs from exact registered Operator attribution")

    # Keep the historic source policy in direct_action_session: the private
    # helper physically rereads the package-owned O200 carrier, verifies it
    # against the package inventory, and returns the one canonical binding.
    from direct_action_session import (
        DirectActionJournalError,
        DirectActionSession,
        INSTALLATION_ACTION_ID,
        STRUCTURAL_SCOPE,
        _source_binding,
    )
    try:
        session = DirectActionSession(
            root,
            author=receipt.journal_author,
            operator_authorization={"operator": record.name, "authorization_ref": "installation-command/" + receipt.command_id},
            action_id=INSTALLATION_ACTION_ID,
            action_package=action_package,
            operators_registry_ref=registry_ref.as_posix(),
        )
        binding = _source_binding(root, INSTALLATION_ACTION_ID, action_package=action_package)
        source = {
            "atom_id": binding["atom_id"],
            "version": binding["version"],
            "path": binding["path"],
            "sha256": binding["digest"],
        }
        if source != dict(receipt.action_source):
            _refuse("installation-command-source-mismatch", "direct O200 source differs from retained command source")
        requested_run_id = "installation-command:" + _sha256(receipt.command_id.encode("utf-8"))
        identity = work_journal.canonical_json_digest({
            "action_id": INSTALLATION_ACTION_ID,
            "requested_run_id": requested_run_id,
            "binding": dict(binding),
            "project_root": str(root),
            "structural_scope": STRUCTURAL_SCOPE,
        })
        action_run_id = "direct-action:" + identity
        from direct_action_session import _reopen_event

        reopened = _reopen_event(root, action_run_id + ":started")
        if reopened is None:
            _refuse("installation-command-start-invalid", "canonical direct O200 start cannot be reopened")
        event, _event_receipt = reopened
        intent = {
            "action_id": INSTALLATION_ACTION_ID,
            "kind": "install_one_admitted_project_runtime",
            "installation_command_sha256": receipt.sha256,
            "target_project_context_sha256": receipt.target_project_context_sha256,
            "package_manifest_sha256": receipt.package_manifest_sha256,
            "full_gate_receipt_sha256": receipt.full_gate_receipt_sha256,
            "prior_runtime_selector_sha256": receipt.prior_runtime_selector_sha256,
            "operators_registry_sha256": receipt.operators_registry_sha256,
        }
        session._validate_started(event, requested_run_id, intent, binding, action_run_id)
        return event
    except FrameworkInstallationCommandError:
        raise
    except DirectActionJournalError as error:
        raise FrameworkInstallationCommandError("installation-command-start-invalid", str(error)) from error
    finally:
        if "session" in locals():
            session.close()


def _direct_result_context(result: object) -> tuple[FrameworkInstallationCommandResult, Path, str]:
    """Reopen the one direct command/start that may own a result carrier."""

    if type(result) is not FrameworkInstallationCommandResult:
        _refuse("installation-command-result-invalid", "direct result requires a closed O200 command result")
    if type(result.action_session) is not DirectActionSession:
        _refuse("installation-command-result-invalid", "direct result requires the original open O200 Session")
    root = _root(result.action_session.root)
    action_run_id = result.action_start.get("run_id") if isinstance(result.action_start, Mapping) else None
    if (
        not isinstance(action_run_id, str)
        or not action_run_id
        or "/" in action_run_id
        or "\\" in action_run_id
        or action_run_id in {".", ".."}
    ):
        _refuse("installation-command-result-invalid", "direct result has no safe actual O200 Run identity")
    if result.command_receipt.package_manifest_sha256 != result.package.manifest_digest:
        _refuse("installation-command-result-invalid", "direct result command names another Framework package")
    if result.command_receipt.target_project_context_sha256 != result.target_context.sha256:
        _refuse("installation-command-result-invalid", "direct result command names another target context")
    if result.command_receipt_path != root / COMMAND_DIRECTORY / f"{result.command_receipt.sha256}.json":
        _refuse("installation-command-result-invalid", "direct result command is not at its canonical digest path")
    try:
        if verify_framework_package(result.package.root) != result.package:
            _refuse("installation-command-result-invalid", "direct result package bytes changed")
        registry_ref = Path(result.target_context.control_child_relpath) / REGISTRY_FILENAME
        reopened_start = reopen_framework_installation_command_start(
            root,
            result.command_receipt,
            action_package=result.package,
            operators_registry_ref=registry_ref,
        )
        reopened_run = reopened_start.get("run")
        if not isinstance(reopened_run, Mapping) or reopened_run.get("run_id") != action_run_id:
            _refuse("installation-command-result-invalid", "reopened O200 start names another Action Run")
        if result.action_session.read_recorded_action_start(action_run_id) != result.action_provenance:
            _refuse("installation-command-result-invalid", "direct O200 start provenance changed")
    except FrameworkInstallationCommandError:
        raise
    except (FrameworkPackageError, RuntimeError, OSError, TypeError, ValueError) as error:
        raise FrameworkInstallationCommandError(
            "installation-command-result-invalid", "direct O200 result inputs cannot be physically reopened"
        ) from error
    return result, root, action_run_id


def _result_effect(
    root: Path,
    *,
    kind: str,
    carrier: Path,
    expected_sha256: str | None = None,
) -> DirectInstallationEffect:
    """Read one exact regular Project carrier and retain its raw-byte hash."""

    if not isinstance(kind, str) or not kind:
        _refuse("installation-command-result-invalid", "direct result effect kind is invalid")
    reference = _relative_to_root(root, carrier)
    payload = _regular_bytes(
        root,
        _relative(reference, field="direct result effect reference"),
        code="installation-command-result-invalid",
        label=f"direct result {kind} carrier",
    )
    observed = _sha256(payload)
    if expected_sha256 is not None and observed != _digest(
        expected_sha256,
        field=f"direct result {kind} digest",
        code="installation-command-full-gate-invalid",
    ):
        _refuse("installation-command-full-gate-invalid", f"original {kind} bytes changed")
    return DirectInstallationEffect(kind=kind, reference=reference, sha256=observed)


def _packet_carrier(
    project_root: Path,
    artifact_root: Path,
    value: object,
    *,
    label: str,
) -> Path:
    """Require a verified packet relation to stay under its Project artifact root."""

    if not isinstance(value, Path) or not value.is_absolute():
        _refuse("installation-command-full-gate-invalid", f"{label} has no absolute original carrier")
    try:
        artifact_root.relative_to(project_root)
        value.relative_to(artifact_root)
    except ValueError as error:
        raise FrameworkInstallationCommandError(
            "installation-command-full-gate-invalid", f"{label} escapes the original retained Project closure"
        ) from error
    return value


def _packet_receipt_carrier(artifact_root: Path, evidence_root: object, *, label: str) -> Path:
    try:
        relative = _relative(evidence_root, field=f"{label} evidence root")
    except FrameworkInstallationCommandError as error:
        raise FrameworkInstallationCommandError(
            "installation-command-full-gate-invalid", f"{label} evidence root is unsafe"
        ) from error
    return artifact_root.joinpath(*relative.parts) / "receipt.json"


def _observe_direct_full_gate_effect_closure(
    command: FrameworkInstallationCommandResult,
    root: Path,
    action_run_id: str,
    *,
    full_gate_packet: RetainedNativeFullGatePacket,
) -> DirectFullGateEffectClosure:
    """Physically observe D604v7's original seven Full Gate carriers.

    This private reader is the only producer of a closure whose rows can later
    be retained by the direct result.  It never resolves a carrier from a
    caller digest, a string, or a latest-result search.
    """

    packet = full_gate_packet
    try:
        from release_full_gate import verify_detached_native_full_gate_evidence

        retained = verify_detached_native_full_gate_evidence(
            packet.artifact_root,
            packet.retained_candidate,
            packet.suite,
            packet.build,
            packet.verification,
            packet.e2e,
            packet.evidence,
        )
    except Exception as error:
        raise FrameworkInstallationCommandError(
            "installation-command-full-gate-invalid", "original Full Gate packet cannot be physically reopened"
        ) from error
    if (
        retained != packet.retained_candidate.package_evidence
        or retained.view.actual_package_manifest_sha256 != command.package.manifest_digest
        or packet.evidence.package_manifest_sha256 != command.package.manifest_digest
        or packet.evidence.receipt_sha256 != command.command_receipt.full_gate_receipt_sha256
    ):
        _refuse("installation-command-full-gate-invalid", "original Full Gate packet differs from the direct command package")
    artifact_root = _packet_carrier(root, Path(packet.artifact_root), Path(packet.artifact_root), label="Full Gate artifact root")
    carriers = (
        (
            "full_gate_receipt",
            _packet_receipt_carrier(artifact_root, packet.evidence.evidence_root, label="Full Gate"),
            packet.evidence.receipt_sha256,
        ),
        (
            "retained_candidate_descriptor",
            _packet_carrier(root, artifact_root, packet.retained_candidate.descriptor_path, label="retained candidate descriptor"),
            packet.retained_candidate.descriptor_sha256,
        ),
        (
            "retained_package_sidecar",
            _packet_carrier(root, artifact_root, retained.receipt_path, label="retained package sidecar"),
            retained.receipt_sha256,
        ),
        (
            "unit_gate_receipt",
            _packet_receipt_carrier(artifact_root, packet.suite.evidence_root, label="Unit gate"),
            packet.suite.receipt_sha256,
        ),
        (
            "build_receipt",
            _packet_receipt_carrier(artifact_root, packet.build.evidence_root, label="build"),
            packet.build.receipt_sha256,
        ),
        (
            "verification_receipt",
            _packet_receipt_carrier(artifact_root, packet.verification.evidence_root, label="verification"),
            packet.verification.receipt_sha256,
        ),
        (
            "e2e_gate_receipt",
            _packet_receipt_carrier(artifact_root, packet.e2e.evidence_root, label="E2E gate"),
            packet.e2e.receipt_sha256,
        ),
    )
    effects = tuple(
        _result_effect(root, kind=kind, carrier=_packet_carrier(root, artifact_root, carrier, label=kind), expected_sha256=digest)
        for kind, carrier, digest in carriers
    )
    if tuple(effect.kind for effect in effects) != _FULL_GATE_EFFECT_KINDS:
        _refuse("installation-command-full-gate-invalid", "original Full Gate closure is incomplete")
    if len({effect.reference for effect in effects}) != len(effects):
        _refuse("installation-command-full-gate-invalid", "original Full Gate closure has ambiguous carriers")
    return DirectFullGateEffectClosure(
        action_run_id=action_run_id,
        installation_command_sha256=command.command_receipt.sha256,
        package_manifest_sha256=command.package.manifest_digest,
        target_project_context_sha256=command.target_context.sha256,
        full_gate_receipt_sha256=command.command_receipt.full_gate_receipt_sha256,
        effects=effects,
    )


def prepare_direct_full_gate_effect_closure(
    result: object,
    *,
    full_gate_packet: object,
) -> DirectFullGateEffectClosure:
    """Observe and retain one process-local original Full Gate closure.

    The public row DTO is intentionally not an authority: it carries an
    opaque observation capability that only this physical reader can create.
    Record-time reopening consumes that capability before it writes a result
    or requests an O-200 terminal event.
    """

    command, root, action_run_id = _direct_result_context(result)
    if type(full_gate_packet) is not RetainedNativeFullGatePacket:
        _refuse("installation-command-full-gate-invalid", "direct result requires the original typed Full Gate packet")
    closure = _observe_direct_full_gate_effect_closure(
        command,
        root,
        action_run_id,
        full_gate_packet=full_gate_packet,
    )
    object.__setattr__(
        closure,
        "_observation",
        _ObservedDirectFullGateClosure(
            action_session=command.action_session,
            action_run_id=action_run_id,
            installation_command_sha256=command.command_receipt.sha256,
            package_manifest_sha256=command.package.manifest_digest,
            target_project_context_sha256=command.target_context.sha256,
            full_gate_receipt_sha256=command.command_receipt.full_gate_receipt_sha256,
            packet=full_gate_packet,
        ),
    )
    return closure


def _reopen_observed_direct_full_gate_effect_closure(
    command: FrameworkInstallationCommandResult,
    root: Path,
    action_run_id: str,
    closure: DirectFullGateEffectClosure,
) -> None:
    """Require the exact physical observation again before result writing."""

    observation = closure._observation
    if type(observation) is not _ObservedDirectFullGateClosure:
        _refuse("installation-command-result-invalid", "direct result Full Gate closure was not physically observed")
    if (
        observation.action_session is not command.action_session
        or observation.action_run_id != action_run_id
        or observation.installation_command_sha256 != command.command_receipt.sha256
        or observation.package_manifest_sha256 != command.package.manifest_digest
        or observation.target_project_context_sha256 != command.target_context.sha256
        or observation.full_gate_receipt_sha256 != command.command_receipt.full_gate_receipt_sha256
        or type(observation.packet) is not RetainedNativeFullGatePacket
    ):
        _refuse("installation-command-result-invalid", "direct result Full Gate closure belongs to another O200 Session")
    observed = _observe_direct_full_gate_effect_closure(
        command,
        root,
        action_run_id,
        full_gate_packet=observation.packet,
    )
    if observed != closure:
        _refuse("installation-command-full-gate-invalid", "original Full Gate closure changed before direct result recording")


def _completed_installation_effects(
    root: Path,
    *,
    package_manifest_sha256: str,
    state_generation: int,
) -> tuple[DirectInstallationEffect, ...]:
    """Observe only the four canonical current carriers of a completed O200."""

    return (
        _result_effect(root, kind="package_selector", carrier=root / ".caprmedio_install/current.toml"),
        _result_effect(root, kind="runtime_selector", carrier=root / ".caprmedio_runtime/installation/current.toml"),
        _result_effect(
            root,
            kind="release_proof",
            carrier=root / ".caprmedio_runtime/installation/generations" / str(state_generation) / "release-proof.toml",
        ),
        _result_effect(
            root,
            kind="package_manifest",
            carrier=root / ".caprmedio_install/releases" / package_manifest_sha256 / "manifest.toml",
        ),
    )


def record_direct_installation_result(
    result: object,
    *,
    full_gate_effects: DirectFullGateEffectClosure,
    state_generation: int,
    effect_outcome: str,
    reason: str | None,
) -> dict[str, object]:
    """Write/reopen one D604 direct result, then request its sole terminal.

    The pre-delete Full Gate closure is supplied only through
    :func:`prepare_direct_full_gate_effect_closure`.  Result recording uses
    those retained rows as-is; it never reopens post-replacement sources to
    infer a new gate association.
    """

    command, root, action_run_id = _direct_result_context(result)
    if type(full_gate_effects) is not DirectFullGateEffectClosure:
        _refuse("installation-command-result-invalid", "direct result requires the retained original Full Gate closure")
    if (
        full_gate_effects.action_run_id != action_run_id
        or full_gate_effects.installation_command_sha256 != command.command_receipt.sha256
        or full_gate_effects.package_manifest_sha256 != command.package.manifest_digest
        or full_gate_effects.target_project_context_sha256 != command.target_context.sha256
        or full_gate_effects.full_gate_receipt_sha256 != command.command_receipt.full_gate_receipt_sha256
        or tuple(effect.kind for effect in full_gate_effects.effects) != _FULL_GATE_EFFECT_KINDS
        or len({effect.reference for effect in full_gate_effects.effects}) != len(full_gate_effects.effects)
    ):
        _refuse("installation-command-result-invalid", "direct result Full Gate closure belongs to another O200 command")
    _reopen_observed_direct_full_gate_effect_closure(command, root, action_run_id, full_gate_effects)
    if isinstance(state_generation, bool) or not isinstance(state_generation, int) or state_generation < 1:
        _refuse("installation-command-result-invalid", "direct result state generation is invalid")
    if effect_outcome not in _RESULT_OUTCOMES:
        _refuse("installation-command-result-invalid", "direct result effect outcome is not governed")
    if reason is not None and (not isinstance(reason, str) or "\x00" in reason or "\n" in reason or "\r" in reason):
        _refuse("installation-command-result-invalid", "direct result reason is invalid")
    effects = list(full_gate_effects.effects)
    if effect_outcome == "completed":
        effects = [
            *_completed_installation_effects(
                root,
                package_manifest_sha256=command.package.manifest_digest,
                state_generation=state_generation,
            ),
            *effects,
        ]
    rows = [{"kind": effect.kind, "reference": effect.reference, "sha256": effect.sha256} for effect in effects]
    if len({row["kind"] for row in rows}) != len(rows) or len({row["reference"] for row in rows}) != len(rows):
        _refuse("installation-command-result-invalid", "direct result effects are ambiguous")
    document = {
        "schema_version": 1,
        "action_id": INSTALLATION_ACTION_ID,
        "action_run_id": action_run_id,
        "installation_command_sha256": command.command_receipt.sha256,
        "package_manifest_sha256": command.package.manifest_digest,
        "target_project_context_sha256": command.target_context.sha256,
        "state_generation": state_generation,
        "effect_outcome": effect_outcome,
        "reason": reason,
        "effects": rows,
    }
    if set(document) != _RESULT_KEYS:
        _refuse("installation-command-result-invalid", "direct result schema is not closed")
    payload = _canonical_json(document)
    directory = _ensure_directory(root, PurePosixPath(*(RESULT_DIRECTORY / action_run_id).parts))
    path = _publish_exact(directory, "result.json", payload)
    result_ref = _relative_to_root(root, path)
    if _regular_bytes(
        root,
        _relative(result_ref, field="direct result reference"),
        code="installation-command-result-invalid",
        label="direct installation result",
    ) != payload:
        _refuse("installation-command-result-invalid", "retained direct result bytes differ")
    effect_refs = [row["reference"] for row in rows] + [result_ref]
    action_outcome = "completed" if effect_outcome == "completed" else (
        "failed" if effect_outcome == "blocked_before_delete" else "partial"
    )
    try:
        command.action_session.record_effects(action_run_id, result_ref=result_ref, effect_refs=effect_refs)
        terminal = command.action_session.finish_action(
            action_run_id,
            outcome=action_outcome,
            result_ref=result_ref,
            effect_refs=effect_refs,
        )
    except RuntimeError:
        return {"state": "recording_pending", "result_ref": result_ref, "result": document, "terminal": None}
    return {"state": "recorded", "result_ref": result_ref, "result": document, "terminal": dict(terminal)}


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
    """Return the current execution selector, preferring native over legacy.

    The legacy Tool selector is intentionally outside this list: it is a
    separate package carrier and therefore cannot be aliased as a Framework
    execution predecessor in the D604 command.
    """

    for relative in _PRIOR_RUNTIME_SELECTORS:
        payload = _optional_regular_bytes(root, relative, label="prior runtime selector")
        if payload is not None:
            return _sha256(payload)
    return None


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
    "RESULT_DIRECTORY",
    "DirectFullGateEffectClosure",
    "DirectInstallationEffect",
    "FrameworkInstallationCommandError",
    "FrameworkInstallationCommandReceipt",
    "FrameworkInstallationCommandRequest",
    "FrameworkInstallationCommandResult",
    "OPERATION",
    "SCHEMA_VERSION",
    "build_framework_installation_command_receipt",
    "prepare_direct_full_gate_effect_closure",
    "read_framework_installation_command_receipt",
    "record_direct_installation_result",
    "reopen_framework_installation_command_start",
    "run_framework_installation_command",
]
