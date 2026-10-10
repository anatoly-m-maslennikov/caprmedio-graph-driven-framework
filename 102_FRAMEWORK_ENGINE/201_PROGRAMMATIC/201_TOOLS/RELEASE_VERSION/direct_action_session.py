"""Canonical Journal recording for explicitly admitted direct Actions.

This deliberately does *not* use the selected-workflow registry, a selected
route, or :class:`workflow_run_support.RunTracker`.  Each admitted Action is
source-pinned and Operator-authorized. Its durable invocation intent is the
canonical ``started`` Journal event; it is written and reopened before any
effect is eligible to run.

The module owns no private Action ledger.  It uses the existing Work Journal's
sealed events, receipt de-duplication, append contexts, and pending-event
recovery.  Therefore an interrupted process cannot silently replay an unknown
installation effect: it may recover the exact original pending Journal event.
Only CA-O-187 additionally admits an explicitly requested recording-only reopen
of an original started Run; the caller must independently observe the retained
actual restoration effects before using the unchanged terminal writer.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import work_journal
from FIND_AND_FETCH_JOURNAL_EVENTS import find_and_fetch_journal_events as journal_query
from FIND_AND_FETCH_JOURNAL_EVENTS.find_and_fetch_journal_events import (
    JournalQueryError,
    capture_snapshot,
    query,
)
from operator_registry import OperatorRegistryError, parse_operators_registry
from workflow_run_support import RecordedActionStartProvenance


DIRECT_ACTION_APP = "direct-action-session"
INITIALIZATION_ACTION_ID = "FRAMEWORK_INITIALIZATION"
RESTORATION_ACTION_ID = "FRAMEWORK_IMAGE_RESTORATION"
STRUCTURAL_SCOPE = "PROJECT_CONFIGURATION"
ACTION_ATOM_ID = "CA-O-180"
ACTION_ATOM_VERSION = 3
ACTION_ATOM_RELATIVE = Path(
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/"
    "CA-O-180-PROJECT_CONFIGURATION-ACTION--initialize-the-first-framework-runtime-and-project-local-ca-skill.md"
)
# This is an intentional source pin.  A changed O-180 source must be reviewed
# and rebound here rather than silently changing what a direct bootstrap Run
# claims to implement.
ACTION_ATOM_SHA256 = "4303a6f35b84b6e36818f3236760173f9216233d881af51f5ac466b5af85bcda"
RESTORATION_ATOM_ID = "CA-O-187"
RESTORATION_ATOM_VERSION = 2
RESTORATION_ATOM_RELATIVE = ACTION_ATOM_RELATIVE.parent / "CA-O-187-PROJECT_CONFIGURATION-ACTION--restore-the-selected-missing-bootstrap-image.md"
RESTORATION_ATOM_SHA256 = "6e0320a7026f37c6e0e4199051d47a4c597cdbe22bb5fb1bfb7b0626258852c1"
SOURCE_ADMISSION_ACTION_ID = "CA-O-199"
SOURCE_ADMISSION_ATOM_VERSION = 2
SOURCE_ADMISSION_ATOM_RELATIVE = ACTION_ATOM_RELATIVE.parent / "CA-O-199-PROJECT_CONFIGURATION-ACTION--admit-local-package-sources.md"
SOURCE_ADMISSION_ATOM_SHA256 = "6b4e510bf5d25ac0b01e7262a79ef6b276272ed52ff02780dfd37f5d63402923"
INSTALLATION_ACTION_ID = "CA-O-200"
INSTALLATION_ATOM_VERSION = 1
# O-200 travels inside the closed Framework package.  Its Project-authority
# source spelling is deliberately *not* a fallback for another target Project.
INSTALLATION_ATOM_RELATIVE = Path(
    "methodology/active/003_PROJECT_CONFIGURATION/09_operations/"
    "CA-O-200-PROJECT_CONFIGURATION-ACTION--install-one-admitted-project-runtime.md"
)
INSTALLATION_ATOM_SHA256 = "ffae75bedb643a4de5a5b081c65333a6bde6ea1055a4b29a6d6481139d0d71ce"
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_RUN_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,159}$")
_OUTCOMES = frozenset({"completed", "no_op", "failed", "cancelled", "partial"})


class DirectActionJournalError(RuntimeError):
    """Stable direct-Action Journal refusal or recording failure."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


@dataclass(frozen=True)
class _ActionDescriptor:
    atom_id: str
    version: int
    path: Path
    digest: str
    instruction: str
    package_owned: bool = False


def _action_descriptor(action_id: str) -> _ActionDescriptor:
    """Select only reviewed direct Actions; callers supply no pins."""
    if action_id == INITIALIZATION_ACTION_ID:
        return _ActionDescriptor(ACTION_ATOM_ID, ACTION_ATOM_VERSION, ACTION_ATOM_RELATIVE,
                                 ACTION_ATOM_SHA256, "first Framework runtime initialization")
    if action_id == RESTORATION_ACTION_ID:
        return _ActionDescriptor(RESTORATION_ATOM_ID, RESTORATION_ATOM_VERSION, RESTORATION_ATOM_RELATIVE,
                                 RESTORATION_ATOM_SHA256, "retained selected Framework image restoration")
    if action_id == SOURCE_ADMISSION_ACTION_ID:
        return _ActionDescriptor(SOURCE_ADMISSION_ACTION_ID, SOURCE_ADMISSION_ATOM_VERSION, SOURCE_ADMISSION_ATOM_RELATIVE,
                                 SOURCE_ADMISSION_ATOM_SHA256, "local package source admission")
    if action_id == INSTALLATION_ACTION_ID:
        return _ActionDescriptor(
            INSTALLATION_ACTION_ID,
            INSTALLATION_ATOM_VERSION,
            INSTALLATION_ATOM_RELATIVE,
            INSTALLATION_ATOM_SHA256,
            "one admitted Project runtime installation",
            package_owned=True,
        )
    raise DirectActionJournalError("direct-action-unadmitted", "direct Action is not admitted for direct execution")


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _safe_ref(value: object, label: str, *, allow_none: bool = False) -> str | None:
    if value is None and allow_none:
        return None
    if not isinstance(value, str) or not value:
        raise DirectActionJournalError("direct-action-invalid-input", f"{label} must be a non-empty repository-relative reference")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise DirectActionJournalError("direct-action-invalid-input", f"{label} must be repository-relative")
    return value


def _digest(value: object, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise DirectActionJournalError("direct-action-invalid-input", f"{label} must be a lowercase SHA-256 digest")
    return value


def _regular_root(value: str | Path) -> Path:
    try:
        root = Path(value).resolve(strict=True)
    except OSError as error:
        raise DirectActionJournalError("direct-action-root-invalid", "project root does not exist") from error
    if root.is_symlink() or not root.is_dir():
        raise DirectActionJournalError("direct-action-root-invalid", "project root must be a regular directory")
    return root


def _read_regular_relative(root: Path, relative: Path, *, code: str, label: str) -> bytes:
    """Read an exact Project carrier without crossing a symlinked ancestor."""
    candidate = root
    try:
        for part in relative.parts:
            candidate = candidate / part
            if candidate.is_symlink():
                raise DirectActionJournalError(code, f"{label} has a symlinked ancestor")
        if not candidate.is_file():
            raise DirectActionJournalError(code, f"{label} is unavailable")
        return candidate.read_bytes()
    except DirectActionJournalError:
        raise
    except OSError as error:
        raise DirectActionJournalError(code, f"{label} is unreadable") from error


def _verified_action_package(value: object) -> object:
    """Reopen the sole package type admitted to carry O-200's source."""

    try:
        from framework_package import FrameworkPackageError, VerifiedFrameworkPackage, verify_framework_package
    except ImportError as error:  # pragma: no cover - protects isolated Journal readers.
        raise DirectActionJournalError("direct-action-package-invalid", "Framework package verifier is unavailable") from error
    if not isinstance(value, VerifiedFrameworkPackage):
        raise DirectActionJournalError(
            "direct-action-package-required",
            "CA-O-200 requires a typed physically verified Framework package",
        )
    try:
        reopened = verify_framework_package(value.root)
    except FrameworkPackageError as error:
        raise DirectActionJournalError("direct-action-package-invalid", "CA-O-200 package cannot be physically reopened") from error
    if reopened != value:
        raise DirectActionJournalError("direct-action-package-stale", "CA-O-200 package differs from its typed verified handoff")
    return reopened


def _source_binding(
    root: Path,
    action_id: str = INITIALIZATION_ACTION_ID,
    *,
    action_package: object | None = None,
) -> dict[str, Any]:
    descriptor = _action_descriptor(action_id)
    name = descriptor.atom_id.removeprefix("CA-")
    source_root = root
    if descriptor.package_owned:
        package = _verified_action_package(action_package)
        source_root = getattr(package, "root")
        inventory = getattr(package, "inventory", ())
        expected = [
            row
            for row in inventory
            if getattr(row, "path", None) == descriptor.path.as_posix()
        ]
        if len(expected) != 1 or getattr(expected[0], "sha256", None) != descriptor.digest or getattr(expected[0], "role", None) != "methodology":
            raise DirectActionJournalError(
                "direct-action-package-invalid",
                "CA-O-200 source is not one admitted active Methodology package member",
            )
    payload = _read_regular_relative(
        source_root,
        descriptor.path,
        code="direct-action-source-stale",
        label=f"the exact {name} source carrier",
    )
    if _sha256(payload) != descriptor.digest:
        raise DirectActionJournalError("direct-action-source-stale", f"the exact {name} source digest is not admitted")
    return {
        "kind": "action",
        "atom_id": descriptor.atom_id,
        "version": descriptor.version,
        "path": descriptor.path.as_posix(),
        "digest": descriptor.digest,
    }


def _authorization(
    root: Path,
    value: Mapping[str, Any],
    *,
    journal_author: str,
    operators_registry_ref: Path,
) -> dict[str, str]:
    if not isinstance(value, Mapping) or set(value) != {"operator", "authorization_ref"}:
        raise DirectActionJournalError(
            "direct-action-authorization-required",
            "explicit Operator authorization requires operator and authorization_ref",
        )
    operator = value.get("operator")
    if not isinstance(operator, str) or not operator.strip() or "\n" in operator or "\r" in operator:
        raise DirectActionJournalError("direct-action-authorization-required", "Operator identity must be a non-empty single line")
    try:
        entries = parse_operators_registry(_read_regular_relative(
            root,
            operators_registry_ref,
            code="direct-action-authorization-required",
            label="registered Operator evidence",
        ))
    except OperatorRegistryError as error:
        raise DirectActionJournalError(
            "direct-action-authorization-required",
            "registered Operator evidence is unavailable",
        ) from error
    matching = [entry for entry in entries if entry.name == operator]
    if len(matching) != 1:
        raise DirectActionJournalError(
            "direct-action-authorization-required",
            "explicit Operator is not registered for this Project",
        )
    registered_author = matching[0].journal_author
    if registered_author is None:
        # Legacy registries may use the Journal account itself as the display
        # name.  A human display name is never inferred as an account alias.
        registered_author = matching[0].name if work_journal.AUTHOR_RE.fullmatch(matching[0].name) else None
    if registered_author != journal_author:
        raise DirectActionJournalError(
            "direct-action-authorization-required",
            "registered Operator does not map to this Journal author",
        )
    return {"operator": operator, "authorization_ref": str(_safe_ref(value.get("authorization_ref"), "authorization_ref"))}


def _image_digest(value: object) -> str:
    if not isinstance(value, str) or not value.startswith("sha256:") or _SHA256.fullmatch(value.removeprefix("sha256:")) is None:
        raise DirectActionJournalError("direct-action-invalid-input", "intent.image_digest must be an immutable sha256 image ID")
    return value


def _intent(value: Mapping[str, Any], action_id: str = INITIALIZATION_ACTION_ID) -> dict[str, Any]:
    if action_id == RESTORATION_ACTION_ID:
        expected = {"action_id", "kind", "manifest_sha256", "source_context_sha256",
                    "selected_selector_sha256", "old_image_digest", "retained_proof_receipt_sha256",
                    "retained_context_sha256"}
        if not isinstance(value, Mapping) or set(value) != expected:
            raise DirectActionJournalError("direct-action-invalid-intent", "restoration intent has unsupported or missing fields")
        if value.get("action_id") != RESTORATION_ACTION_ID or value.get("kind") != "retained_selected_framework_image_restoration":
            raise DirectActionJournalError("direct-action-invalid-intent", "intent does not describe the admitted restoration Action")
        return {
            "action_id": RESTORATION_ACTION_ID,
            "kind": "retained_selected_framework_image_restoration",
            "old_image_digest": _image_digest(value.get("old_image_digest")),
            **{field: _digest(value.get(field), f"intent.{field}") for field in
               ("manifest_sha256", "source_context_sha256", "selected_selector_sha256",
                "retained_proof_receipt_sha256", "retained_context_sha256")},
        }
    if action_id == SOURCE_ADMISSION_ACTION_ID:
        expected = {"action_id", "kind", "snapshot_sha256", "operators_registry_sha256"}
        if not isinstance(value, Mapping) or set(value) != expected:
            raise DirectActionJournalError("direct-action-invalid-intent", "source-admission intent has unsupported or missing fields")
        if value.get("action_id") != SOURCE_ADMISSION_ACTION_ID or value.get("kind") != "local_package_source_admission":
            raise DirectActionJournalError("direct-action-invalid-intent", "intent does not describe the admitted source-admission Action")
        return {
            "action_id": SOURCE_ADMISSION_ACTION_ID,
            "kind": "local_package_source_admission",
            "snapshot_sha256": _digest(value.get("snapshot_sha256"), "intent.snapshot_sha256"),
            "operators_registry_sha256": _digest(value.get("operators_registry_sha256"), "intent.operators_registry_sha256"),
        }
    if action_id == INSTALLATION_ACTION_ID:
        expected = {
            "action_id", "kind", "installation_command_sha256", "target_project_context_sha256",
            "package_manifest_sha256", "full_gate_receipt_sha256", "prior_runtime_selector_sha256",
            "operators_registry_sha256",
        }
        if not isinstance(value, Mapping) or set(value) != expected:
            raise DirectActionJournalError("direct-action-invalid-intent", "installation intent has unsupported or missing fields")
        if value.get("action_id") != INSTALLATION_ACTION_ID or value.get("kind") != "install_one_admitted_project_runtime":
            raise DirectActionJournalError("direct-action-invalid-intent", "intent does not describe the admitted installation Action")
        prior = value.get("prior_runtime_selector_sha256")
        if prior is not None:
            prior = _digest(prior, "intent.prior_runtime_selector_sha256")
        return {
            "action_id": INSTALLATION_ACTION_ID,
            "kind": "install_one_admitted_project_runtime",
            "installation_command_sha256": _digest(value.get("installation_command_sha256"), "intent.installation_command_sha256"),
            "target_project_context_sha256": _digest(value.get("target_project_context_sha256"), "intent.target_project_context_sha256"),
            "package_manifest_sha256": _digest(value.get("package_manifest_sha256"), "intent.package_manifest_sha256"),
            "full_gate_receipt_sha256": _digest(value.get("full_gate_receipt_sha256"), "intent.full_gate_receipt_sha256"),
            "prior_runtime_selector_sha256": prior,
            "operators_registry_sha256": _digest(value.get("operators_registry_sha256"), "intent.operators_registry_sha256"),
        }
    _action_descriptor(action_id)
    expected = {"action_id", "kind", "manifest_sha256", "source_context_sha256", "image_digest"}
    if not isinstance(value, Mapping) or set(value) != expected:
        raise DirectActionJournalError("direct-action-invalid-intent", "initialization intent has unsupported or missing fields")
    if value.get("action_id") != INITIALIZATION_ACTION_ID or value.get("kind") != "first_framework_runtime_installation":
        raise DirectActionJournalError("direct-action-invalid-intent", "intent does not describe the admitted first-runtime Action")
    return {
        "action_id": INITIALIZATION_ACTION_ID,
        "kind": "first_framework_runtime_installation",
        "manifest_sha256": _digest(value.get("manifest_sha256"), "intent.manifest_sha256"),
        "source_context_sha256": _digest(value.get("source_context_sha256"), "intent.source_context_sha256"),
        "image_digest": _image_digest(value.get("image_digest")),
    }


def _journal_root(root: Path) -> Path | None:
    """Return only the configured canonical Journal root without creating it."""
    try:
        journal_root = root / work_journal.configured_journal_root(root)
    except (OSError, RuntimeError) as error:
        raise DirectActionJournalError("direct-action-journal-unavailable", "canonical Work Journal is unavailable") from error
    if not journal_root.exists():
        return None
    if journal_root.is_symlink() or not journal_root.is_dir():
        raise DirectActionJournalError("direct-action-journal-invalid", "canonical Work Journal root is not a regular directory")
    return journal_root


def _bounded_journal_events(
    root: Path,
    filter_expression: str,
) -> tuple[list[dict[str, Any]], Mapping[str, Any] | None]:
    """Reopen a complete, bounded canonical Journal frontier exactly once.

    Direct Action evidence must never select the first matching NDJSON line.
    The Journal query snapshot is the sole physical frontier: it rejects unsafe
    members and duplicate identities before query, then revalidates the same
    bounded carrier bytes before returning the complete match set.
    """
    journal_root = _journal_root(root)
    if journal_root is None:
        return [], None
    try:
        configured = work_journal.configured_journal_root(root)
        snapshot = capture_snapshot(root)
        if snapshot.get("source_root") != configured.as_posix():
            raise DirectActionJournalError(
                "direct-action-journal-invalid",
                "bounded Journal reader has a different canonical root",
            )
        observed = query(snapshot, {"mode": "full_events", "filter": filter_expression})
    except JournalQueryError as error:
        raise DirectActionJournalError(
            "direct-action-journal-unavailable",
            "bounded canonical Work Journal coverage is unavailable",
        ) from error
    if (
        observed.get("status") != "complete"
        or observed.get("coverage", {}).get("complete") is not True
    ):
        raise DirectActionJournalError(
            "direct-action-journal-incomplete",
            "bounded canonical Work Journal coverage is incomplete",
        )
    rows = observed.get("results")
    if not isinstance(rows, list):
        raise DirectActionJournalError("direct-action-journal-invalid", "bounded Journal result is malformed")
    events: list[dict[str, Any]] = []
    for row in rows:
        if not isinstance(row, Mapping) or set(row) != {"event_id", "event"}:
            raise DirectActionJournalError("direct-action-journal-invalid", "bounded Journal event result is malformed")
        try:
            event = work_journal.validate_sealed_event(row["event"])
        except work_journal.WorkJournalError as error:
            raise DirectActionJournalError("direct-action-journal-invalid", "bounded Journal event is not sealed") from error
        if row["event_id"] != event["event_id"]:
            raise DirectActionJournalError("direct-action-journal-invalid", "bounded Journal event identity differs from its carrier")
        events.append(event)
    return events, snapshot


def _receipt_from_sidecar(
    root: Path,
    event: Mapping[str, Any],
    snapshot: Mapping[str, Any],
) -> dict[str, Any]:
    """Bind the canonical receipt to one bounded physical Journal coordinate."""
    event_id = event.get("event_id")
    if not isinstance(event_id, str) or not event_id or Path(event_id).name != event_id:
        raise DirectActionJournalError("direct-action-journal-invalid", "reopened Journal event has an unsafe identity")
    try:
        retained, _ = journal_query._resolve_retained_snapshot(snapshot)
        records = retained.get("records")
        members = retained.get("members")
        limits = retained.get("limits")
        if not isinstance(records, list) or not isinstance(members, list) or not isinstance(limits, Mapping):
            raise JournalQueryError("invalid-snapshot")
        matched = [record for record in records if isinstance(record, Mapping) and record.get("event_id") == event_id]
        if len(matched) != 1:
            raise JournalQueryError("invalid-retained-provenance")
        coordinate = matched[0]
        expected_coordinate = {"event_id", "event", "member", "line", "offset", "raw_digest"}
        if set(coordinate) != expected_coordinate or coordinate.get("event") != dict(event):
            raise JournalQueryError("invalid-retained-provenance")
        member = coordinate.get("member")
        line = coordinate.get("line")
        offset = coordinate.get("offset")
        raw_digest = coordinate.get("raw_digest")
        member_path = Path(member) if isinstance(member, str) else None
        if (
            member_path is None
            or member_path.is_absolute()
            or ".." in member_path.parts
            or type(line) is not int
            or line < 1
            or type(offset) is not int
            or offset < 0
            or not isinstance(raw_digest, str)
            or _SHA256.fullmatch(raw_digest) is None
        ):
            raise JournalQueryError("invalid-retained-provenance")
        expected_members = [candidate for candidate in members if isinstance(candidate, Mapping) and candidate.get("ref") == member]
        if len(expected_members) != 1:
            raise JournalQueryError("invalid-retained-provenance")
        source_member = expected_members[0]
        if set(source_member) != {"ref", "prefix_bytes", "prefix_digest"}:
            raise JournalQueryError("invalid-retained-provenance")
        prefix_bytes = source_member.get("prefix_bytes")
        prefix_digest = source_member.get("prefix_digest")
        max_file_bytes = limits.get("max_file_bytes")
        max_total_read_bytes = limits.get("max_total_read_bytes")
        if (
            type(prefix_bytes) is not int
            or prefix_bytes < 0
            or not isinstance(prefix_digest, str)
            or _SHA256.fullmatch(prefix_digest) is None
            or type(max_file_bytes) is not int
            or max_file_bytes < 1
            or type(max_total_read_bytes) is not int
            or max_total_read_bytes < 1
        ):
            raise JournalQueryError("invalid-retained-provenance")
        content, _ = journal_query._read_member(
            root / member_path,
            max_file_bytes=max_file_bytes,
            total_read=0,
            max_total_read=max_total_read_bytes,
        )
        if len(content) != prefix_bytes or _sha256(content) != prefix_digest:
            raise JournalQueryError("changed-member")
        current_records = journal_query._member_events(member, content)
        current = [record for record in current_records if record.get("event_id") == event_id]
        if len(current) != 1 or current[0] != coordinate:
            raise JournalQueryError("invalid-retained-provenance")
        lines = content.splitlines(keepends=True)
        if line > len(lines):
            raise JournalQueryError("invalid-retained-provenance")
        before = b"".join(lines[: line - 1])
        if len(before) != offset:
            raise JournalQueryError("invalid-retained-provenance")
        expected_receipt = {
            "event_id": event_id,
            "action_id": event["action_id"],
            "event_digest": event["event_digest"],
            "carrier": member,
            "line": line,
            "previous_carrier_digest": _sha256(before),
            "appended_carrier_digest": _sha256(before + lines[line - 1]),
        }
    except JournalQueryError as error:
        raise DirectActionJournalError(
            "direct-action-journal-invalid",
            "bounded Journal receipt provenance is unavailable",
        ) from error
    try:
        receipt_relative = work_journal.configured_runtime_root(root) / "state/work_journal/receipts" / f"{event_id}.json"
    except (OSError, RuntimeError) as error:
        raise DirectActionJournalError("direct-action-journal-unavailable", "canonical Work Journal receipt is unavailable") from error
    try:
        receipt = json.loads(
            _read_regular_relative(
                root,
                receipt_relative,
                code="direct-action-journal-invalid",
                label="canonical Work Journal receipt",
            )
        )
    except json.JSONDecodeError as error:
        raise DirectActionJournalError("direct-action-journal-invalid", "canonical Work Journal receipt is malformed") from error
    expected_keys = {
        "event_id",
        "action_id",
        "event_digest",
        "carrier",
        "line",
        "previous_carrier_digest",
        "appended_carrier_digest",
    }
    if not isinstance(receipt, dict) or set(receipt) != expected_keys:
        raise DirectActionJournalError("direct-action-journal-invalid", "canonical Work Journal receipt has unsupported fields")
    if receipt != expected_receipt:
        raise DirectActionJournalError("direct-action-journal-invalid", "canonical Work Journal receipt differs from its sealed event")
    return receipt


def _reopen_event(root: Path, event_id: str) -> tuple[dict[str, Any], dict[str, Any]] | None:
    """Read one already-appended sealed event and reconstruct its receipt.

    This is a Journal reader, not a second event store.  The event is proven
    from one bounded physical Journal frontier; the receipt retains the exact
    seven-field canonical writer sidecar rather than re-enumerating carriers.
    """
    if not isinstance(event_id, str) or not event_id:
        raise DirectActionJournalError("direct-action-journal-invalid", "Journal event identity is invalid")
    events, snapshot = _bounded_journal_events(
        root,
        '"event:/event_id" = ' + json.dumps(event_id),
    )
    if not events:
        return None
    if len(events) != 1 or events[0]["event_id"] != event_id:
        raise DirectActionJournalError("direct-action-journal-invalid", "canonical Journal event identity is ambiguous")
    if snapshot is None:  # Defensive: a physical event cannot come from an absent Journal.
        raise DirectActionJournalError("direct-action-journal-invalid", "canonical Journal event lacks bounded provenance")
    event = events[0]
    return event, _receipt_from_sidecar(root, event, snapshot)


class DirectActionSession:
    """One explicitly authorized closed direct Action backed only by Journal v5.

    ``actual``, ``terminal``, and ``receipts`` are intentionally small
    observable state for the installer.  They are not a durable side ledger;
    the canonical Work Journal remains the only durable Run evidence.
    """

    def __init__(
        self,
        project_root: str | Path,
        *,
        author: str,
        operator_authorization: Mapping[str, Any],
        action_id: str = INITIALIZATION_ACTION_ID,
        action_package: object | None = None,
        operators_registry_ref: str | Path = ".caprmedio_caprmedio/operators_registry.toml",
        timezone: str = "UTC",
        now: Callable[[], dt.datetime] | None = None,
    ) -> None:
        self.descriptor = _action_descriptor(action_id)
        self.action_id = action_id
        if self.descriptor.package_owned:
            self._action_package = _verified_action_package(action_package)
        elif action_package is not None:
            raise DirectActionJournalError(
                "direct-action-package-unadmitted",
                "only CA-O-200 accepts a Framework package Action source",
            )
        else:
            self._action_package = None
        self.root = _regular_root(project_root)
        registry_ref = _safe_ref(str(operators_registry_ref), "operators_registry_ref")
        self.operators_registry_ref = Path(str(registry_ref))
        try:
            work_journal.validate_partition(author, "2000-01-01", timezone)
        except work_journal.WorkJournalError as error:
            raise DirectActionJournalError("direct-action-journal-context-invalid", str(error)) from error
        self.author = author
        self.timezone = timezone
        self.authorization = _authorization(
            self.root,
            operator_authorization,
            journal_author=self.author,
            operators_registry_ref=self.operators_registry_ref,
        )
        self._now = now or (lambda: dt.datetime.now(dt.UTC))
        self.actual: dict[str, dict[str, Any]] = {}
        self.terminal: dict[str, dict[str, Any]] = {}
        self.receipts: list[dict[str, Any]] = []
        self.pending: dict[str, dict[str, Any]] = {}
        self._observed: dict[str, dict[str, Any]] = {}
        self._invocation_locks: list[tuple[str, Any]] = []
        self._closed = False

    def __enter__(self) -> "DirectActionSession":
        if self._closed:
            raise DirectActionJournalError("direct-action-invocation-closed", "direct Action session is closed")
        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
        del exc_type, exc, traceback
        self.close()

    def close(self) -> None:
        """Release a locally held invocation lock without inferring an outcome.

        Callers should use this session as a context manager.  Closing never
        replays an effect or writes a synthetic terminal fact: a persisted
        ``started`` event remains recovery-only evidence.
        """
        if not self._closed:
            self._release_invocation_lock()
            self._closed = True

    def begin_action(
        self,
        *,
        action_id: str,
        requested_run_id: str,
        intent: Mapping[str, Any],
    ) -> Mapping[str, Any]:
        """Append and reopen the exact started event before any installer effect.

        A new process that sees a previously started action raises a recovery
        requirement.  It never assumes the absent terminal event means no
        effect happened and never emits a second start event.
        """
        if self._closed:
            raise DirectActionJournalError("direct-action-invocation-closed", "direct Action session is closed")
        if action_id != self.action_id:
            raise DirectActionJournalError("direct-action-unadmitted", f"only {self.action_id} is admitted by this Session")
        if not isinstance(requested_run_id, str) or _RUN_ID.fullmatch(requested_run_id) is None:
            raise DirectActionJournalError("direct-action-invalid-run", "requested_run_id has invalid syntax")
        # Construction is not a lease on an earlier registry mapping.  The
        # canonical start must use the Operator/account mapping observable at
        # the point the Journal event is appended.
        _authorization(
            self.root,
            self.authorization,
            journal_author=self.author,
            operators_registry_ref=self.operators_registry_ref,
        )
        normalized_intent = _intent(intent, self.action_id)
        binding = _source_binding(self.root, self.action_id, action_package=self._action_package)
        identity = self._run_identity(requested_run_id, binding)
        run_id = f"direct-action:{identity}"
        existing = self.actual.get(run_id)
        if existing is not None:
            raise DirectActionJournalError(
                "direct-action-invocation-active",
                "this direct Action invocation is already active in this session",
            )
        self._acquire_invocation_lock(requested_run_id, binding)

        try:
            started_id = f"direct-action:{identity}:started"
            pending_start = self._pending_event(started_id)
            if pending_start is not None:
                self._validate_started(pending_start, requested_run_id, normalized_intent, binding, run_id)
                raise DirectActionJournalError(
                    "direct-action-recording-pending",
                    f"canonical started evidence is pending; recover only original event {started_id}",
                )
            reopened = _reopen_event(self.root, started_id)
            if reopened is not None:
                event, _ = reopened
                self._validate_started(event, requested_run_id, normalized_intent, binding, run_id)
                terminal = self._existing_terminal(identity, requested_run_id, normalized_intent, binding, run_id)
                if terminal is not None:
                    raise DirectActionJournalError("direct-action-already-terminal", "this direct Action already has canonical terminal evidence")
                raise DirectActionJournalError(
                    "direct-action-recovery-required",
                    "canonical started evidence exists without a terminal result; inspect or recover the original recording only",
                )

            event = self._event(
                event_id=started_id,
                run_id=run_id,
                requested_run_id=requested_run_id,
                intent=normalized_intent,
                binding=binding,
                event_name="started",
                outcome=None,
                result_ref=None,
                effect_refs=[],
                report_ref=None,
            )
            receipt = self._append(event, result_ref=None, effect_refs=[])
            reopened = _reopen_event(self.root, started_id)
            if reopened is None:
                raise DirectActionJournalError("direct-action-journal-unavailable", "started Action evidence did not reopen after append")
            saved, saved_receipt = reopened
            self._validate_started(saved, requested_run_id, normalized_intent, binding, run_id)
            if saved_receipt != receipt:
                raise DirectActionJournalError("direct-action-journal-invalid", "reopened started receipt differs from append receipt")
            self.actual[run_id] = {
                "requested_run_id": requested_run_id,
                "intent": normalized_intent,
                "binding": binding,
                "event_id": started_id,
                "event_receipt": dict(receipt),
            }
            self.receipts.append(dict(receipt))
            return {"run_id": run_id, "disposition": "started", "event_id": started_id, "event_receipt": dict(receipt)}
        except BaseException:
            self._release_invocation_lock()
            raise

    def read_recorded_action_start(self, action_run_id: str) -> RecordedActionStartProvenance:
        """Reopen one exact direct Action start without creating any evidence.

        This is intentionally the direct-session analogue of the selected-run
        accessor.  It exposes only the sealed Journal provenance required by
        host admission code; it neither authorizes a command nor records an
        outcome.
        """

        if not isinstance(action_run_id, str) or not action_run_id:
            raise DirectActionJournalError("direct-action-start-invalid", "Action Run identity is invalid")
        actual = self.actual.get(action_run_id)
        if not isinstance(actual, Mapping):
            raise DirectActionJournalError("direct-action-start-invalid", "direct Action start is not owned by this Session")
        requested = actual.get("requested_run_id")
        intent = actual.get("intent")
        binding = actual.get("binding")
        event_id = actual.get("event_id")
        if (
            not isinstance(requested, str)
            or not isinstance(intent, Mapping)
            or not isinstance(binding, Mapping)
            or not isinstance(event_id, str)
        ):
            raise DirectActionJournalError("direct-action-start-invalid", "direct Action start evidence is incomplete")
        reopened = _reopen_event(self.root, event_id)
        if reopened is None:
            raise DirectActionJournalError("direct-action-start-invalid", "direct Action start cannot be reopened")
        event, receipt = reopened
        self._validate_started(event, requested, intent, binding, action_run_id)
        if receipt != actual.get("event_receipt"):
            raise DirectActionJournalError("direct-action-start-invalid", "reopened direct Action receipt differs from its recorded start")
        return RecordedActionStartProvenance(
            author=self.author,
            event_id=event_id,
            action_run_id=action_run_id,
            parent_lineage=(),
        )

    def reopen_restoration_for_recording(
        self,
        requested_run_id: str,
        intent: Mapping[str, Any],
    ) -> Mapping[str, Any]:
        """Own the original O-187 Run solely to record independently proven effects.

        This appends no event and never starts or dispatches an Action. The
        coordinator must validate its retained result, proof, image, selector,
        and public Skill before observing effects and calling ``finish_action``.
        Any sealed pending event instead requires exact-byte pending recovery.
        O-180 and source-evolved historical Runs are not admitted by this method.
        """
        if self._closed:
            raise DirectActionJournalError("direct-action-invocation-closed", "direct Action session is closed")
        if self.action_id != RESTORATION_ACTION_ID:
            raise DirectActionJournalError("direct-action-unadmitted", "recording-only reopen is admitted only for O-187 restoration")
        if not isinstance(requested_run_id, str) or _RUN_ID.fullmatch(requested_run_id) is None:
            raise DirectActionJournalError("direct-action-invalid-run", "requested_run_id has invalid syntax")
        normalized_intent = _intent(intent, RESTORATION_ACTION_ID)
        binding = _source_binding(self.root, RESTORATION_ACTION_ID)
        # Constructor admission is not a lease on subsequently removed
        # Operator authority. Reopen the current registry before owning a Run.
        _authorization(
            self.root,
            self.authorization,
            journal_author=self.author,
            operators_registry_ref=self.operators_registry_ref,
        )
        identity = self._run_identity(requested_run_id, binding)
        run_id = f"direct-action:{identity}"
        if run_id in self.actual:
            raise DirectActionJournalError("direct-action-invocation-active", "this direct Action invocation is already active in this session")
        self._acquire_invocation_lock(requested_run_id, binding)
        try:
            self._refuse_restoration_pending(run_id)
            started_id = f"{run_id}:started"
            reopened = _reopen_event(self.root, started_id)
            if reopened is None:
                raise DirectActionJournalError("direct-action-recording-unavailable", "the original canonical started restoration Run is unavailable")
            event, receipt = reopened
            self._validate_started(event, requested_run_id, normalized_intent, binding, run_id)
            if self._existing_terminal(identity, requested_run_id, normalized_intent, binding, run_id) is not None:
                raise DirectActionJournalError("direct-action-already-terminal", "this direct Action already has canonical terminal evidence")
            self.actual[run_id] = {
                "requested_run_id": requested_run_id,
                "intent": normalized_intent,
                "binding": binding,
                "event_id": started_id,
                "event_receipt": dict(receipt),
            }
            self.receipts.append(dict(receipt))
            return {"run_id": run_id, "disposition": "recording_only", "event_id": started_id,
                    "event_receipt": dict(receipt)}
        except BaseException:
            self._release_invocation_lock()
            raise

    def record_effects(self, run_id: str, *, result_ref: str, effect_refs: list[str]) -> None:
        """Keep observed actual effects until the sole terminal writer records them."""
        self._require_open_run(run_id)
        result = str(_safe_ref(result_ref, "result_ref"))
        effects = self._effect_refs(effect_refs)
        observed = {"result_ref": result, "effect_refs": effects}
        prior = self._observed.get(run_id)
        if prior is not None and prior != observed:
            raise DirectActionJournalError("direct-action-effect-mismatch", "one Action Run cannot replace observed actual effects")
        self._observed[run_id] = observed

    def finish_action(
        self,
        run_id: str,
        *,
        outcome: str,
        result_ref: str,
        effect_refs: list[str],
        report_ref: str | None = None,
    ) -> Mapping[str, Any]:
        """Append one terminal fact after effects were observed by the caller."""
        run = self._require_open_run(run_id)
        if outcome not in _OUTCOMES:
            raise DirectActionJournalError("direct-action-invalid-outcome", "outcome is not admitted")
        result = str(_safe_ref(result_ref, "result_ref"))
        effects = self._effect_refs(effect_refs)
        report = _safe_ref(report_ref, "report_ref", allow_none=True)
        observed = self._observed.get(run_id)
        if observed is None:
            raise DirectActionJournalError("direct-action-effects-unobserved", "actual effects must be observed before terminal recording")
        if observed != {"result_ref": result, "effect_refs": effects}:
            raise DirectActionJournalError("direct-action-effect-mismatch", "terminal evidence must retain observed actual effects")
        identity = self._run_identity(run["requested_run_id"], run["binding"])
        event_name = {"completed": "completed", "no_op": "completed", "failed": "failed", "partial": "failed", "cancelled": "abandoned"}[outcome]
        terminal_key = work_journal.canonical_json_digest(
            {
                "intent_sha256": self._intent_identity(run["intent"], run["binding"]),
                "outcome": outcome,
                "result_ref": result,
                "effect_refs": effects,
                "report_ref": report,
            }
        )
        event_id = f"direct-action:{identity}:terminal:{terminal_key}"
        event = self._event(
            event_id=event_id,
            run_id=run_id,
            requested_run_id=run["requested_run_id"],
            intent=run["intent"],
            binding=run["binding"],
            event_name=event_name,
            outcome=outcome,
            result_ref=result,
            effect_refs=effects,
            report_ref=report,
        )
        try:
            reopened = _reopen_event(self.root, event_id)
            if reopened is not None:
                saved, receipt = reopened
                self._validate_terminal(saved, run_id, run["requested_run_id"], run["intent"], run["binding"], event)
                result_value = self._terminal_result(event, receipt)
                self.terminal[run_id] = result_value
                self.receipts.append(dict(receipt))
                return dict(result_value)
            receipt = self._append(event, result_ref=result, effect_refs=effects)
            reopened = _reopen_event(self.root, event_id)
            if reopened is None:
                raise DirectActionJournalError("direct-action-journal-unavailable", "terminal Action evidence did not reopen after append")
            saved, saved_receipt = reopened
            self._validate_terminal(saved, run_id, run["requested_run_id"], run["intent"], run["binding"], event)
            if saved_receipt != receipt:
                raise DirectActionJournalError("direct-action-journal-invalid", "reopened terminal receipt differs from append receipt")
            result_value = self._terminal_result(event, receipt)
            self.terminal[run_id] = result_value
            self.receipts.append(dict(receipt))
            return dict(result_value)
        finally:
            # A completed terminal append, an append failure retained as a
            # pending original event, and an invalid terminal input all end
            # this process-local invocation.  Another process may inspect or
            # recover, but never replay its unknown effect under this lock.
            self._release_invocation_lock()
            self._closed = True

    def recover_pending(self, event_id: str) -> Mapping[str, Any]:
        """Recover only the exact pending direct-Action Journal event bytes.

        This method cannot run an installer effect, create a replacement event,
        or infer an outcome.  It intentionally validates the sealed historic
        definition rather than reading the *current* O-180 source: source
        evolution cannot make the original Journal fact unrecoverable, nor can
        recovery admit a new execution under that historic source binding.
        """
        if not isinstance(event_id, str) or not event_id.startswith("direct-action:"):
            raise DirectActionJournalError("direct-action-pending-invalid", "event_id is not a direct Action event")
        try:
            _, event, _, _ = work_journal._read_pending_event(self.root, event_id)
        except work_journal.WorkJournalError as error:
            raise DirectActionJournalError("direct-action-pending-invalid", str(error)) from error
        binding = event.get("run", {}).get("definition")
        if (
            event.get("schema_version") != 5
            or event.get("kind") != "workflow_execution"
            or event.get("action_id") != self.action_id
            or event.get("event") not in {"started", "completed", "failed", "abandoned"}
            or event.get("author") != self.author
            or event.get("llm_session", {}).get("app") != DIRECT_ACTION_APP
            or event.get("structural_scope") != STRUCTURAL_SCOPE
            or event.get("initiative", {}).get("initiative_ref") != self.authorization["authorization_ref"]
            or event.get("initiative", {}).get("instruction_summary")
            != "Operator " + self.authorization["operator"]
            + " authorized " + self.descriptor.instruction + "; intent SHA-256 "
            + event.get("llm_session", {}).get("uuid", "")
            or event.get("run", {}).get("kind") != "action"
            or not isinstance(event.get("run", {}).get("run_id"), str)
            or not event["run"]["run_id"].startswith("direct-action:")
            or not isinstance(binding, Mapping)
            or set(binding) != {"atom_id", "version", "path", "digest"}
            or binding.get("atom_id") != self.descriptor.atom_id
            or binding.get("path") != self.descriptor.path.as_posix()
            or type(binding.get("version")) is not int
            or binding["version"] < 1
            or not isinstance(binding.get("digest"), str)
            or _SHA256.fullmatch(binding["digest"]) is None
            or event.get("definition_bindings")
            != [{"kind": "action", **dict(binding)}]
        ):
            raise DirectActionJournalError(
                "direct-action-pending-invalid",
                f"pending event does not belong to a sealed {self.descriptor.atom_id} direct Action recording",
            )
        try:
            receipt = work_journal.recover_pending_event(self.root, event_id)
        except work_journal.WorkJournalError as error:
            raise DirectActionJournalError("direct-action-recovery-failed", str(error)) from error
        self.receipts.append(dict(receipt))
        return {"event_id": event_id, "disposition": "recovered", "event_receipt": dict(receipt)}

    def _run_identity(self, requested_run_id: str, binding: Mapping[str, Any]) -> str:
        return work_journal.canonical_json_digest(
            {
                "action_id": self.action_id,
                "requested_run_id": requested_run_id,
                "binding": dict(binding),
                "project_root": str(self.root),
                "structural_scope": STRUCTURAL_SCOPE,
            }
        )

    def _intent_identity(self, intent: Mapping[str, str], binding: Mapping[str, Any]) -> str:
        return work_journal.canonical_json_digest(
            {
                "intent": dict(intent),
                "binding": dict(binding),
                "operator": self.authorization["operator"],
                "authorization_ref": self.authorization["authorization_ref"],
                "author": self.author,
            }
        )

    def _acquire_invocation_lock(self, requested_run_id: str, binding: Mapping[str, Any]) -> None:
        if self._invocation_locks:
            raise DirectActionJournalError("direct-action-invocation-active", "this session already holds a direct Action invocation lock")
        keys = (
            self._boundary_lock_key(),
            "direct-action-invocation:" + self._run_identity(requested_run_id, binding),
        )
        try:
            for key in keys:
                lock = work_journal._event_lock(self.root, key)
                lock.__enter__()
                self._invocation_locks.append((key, lock))
        except (OSError, RuntimeError, work_journal.WorkJournalError) as error:
            self._release_invocation_lock()
            raise DirectActionJournalError(
                "direct-action-lock-unavailable",
                "direct Action boundary or this requested Action Run is already exclusively owned",
            ) from error

    def _release_invocation_lock(self) -> None:
        locks, self._invocation_locks = self._invocation_locks, []
        for _, lock in reversed(locks):
            lock.__exit__(None, None, None)

    def _first_initialization_lock_key(self) -> str:
        """One bootstrap boundary per Project, independent of requested Run ID."""
        return "direct-action-first-initialization:" + work_journal.canonical_json_digest(
            {
                "action_id": INITIALIZATION_ACTION_ID,
                "project_root": str(self.root),
                "structural_scope": STRUCTURAL_SCOPE,
            }
        )

    def _boundary_lock_key(self) -> str:
        if self.action_id == INITIALIZATION_ACTION_ID:
            return self._first_initialization_lock_key()
        if self.action_id == INSTALLATION_ACTION_ID:
            return "direct-action-framework-installation:" + work_journal.canonical_json_digest(
                {"action_id": self.action_id, "project_root": str(self.root), "structural_scope": STRUCTURAL_SCOPE}
            )
        return "direct-action-image-restoration:" + work_journal.canonical_json_digest(
            {"action_id": self.action_id, "project_root": str(self.root), "structural_scope": STRUCTURAL_SCOPE}
        )

    def _event(
        self,
        *,
        event_id: str,
        run_id: str,
        requested_run_id: str,
        intent: Mapping[str, str],
        binding: Mapping[str, Any],
        event_name: str,
        outcome: str | None,
        result_ref: str | None,
        effect_refs: Sequence[str],
        report_ref: str | None,
    ) -> dict[str, Any]:
        moment = self._now()
        if moment.tzinfo is None:
            raise DirectActionJournalError("direct-action-journal-context-invalid", "clock must return a timezone-aware timestamp")
        if self.timezone == "UTC":
            moment = moment.astimezone(dt.UTC)
        payload: dict[str, Any] = {
            "schema_version": 5,
            "kind": "workflow_execution",
            "event_id": event_id,
            "action_id": self.action_id,
            "event": event_name,
            "author": self.author,
            "occurred_at": moment.isoformat(timespec="seconds"),
            "llm_session": {"app": DIRECT_ACTION_APP, "uuid": self._intent_identity(intent, binding)},
            "structural_scope": STRUCTURAL_SCOPE,
            "initiative": {
                "initiative_id": self.descriptor.atom_id,
                "instruction_summary": "Operator " + self.authorization["operator"]
                + " authorized " + self.descriptor.instruction + "; intent SHA-256 "
                + self._intent_identity(intent, binding),
                "initiative_ref": self.authorization["authorization_ref"],
            },
            "run": {
                "run_id": run_id,
                "kind": "action",
                "definition": {key: binding[key] for key in ("atom_id", "version", "path", "digest")},
            },
            "definition_bindings": [dict(binding)],
            "input_ref": self.authorization["authorization_ref"],
            "outcome": outcome,
            "result_ref": result_ref,
            "effect_refs": list(effect_refs),
            "report_ref": report_ref,
            "redaction": {"redacted": False, "fields": []},
        }
        return work_journal.with_event_digest(payload)

    def _context(self, event: Mapping[str, Any]) -> dict[str, Any]:
        occurred_at = dt.datetime.fromisoformat(str(event["occurred_at"]))
        try:
            return work_journal.seal_append_context(
                self.root,
                event,
                author=self.author,
                local_date=occurred_at.date().isoformat(),
                timezone=self.timezone,
            )
        except (OSError, RuntimeError, work_journal.WorkJournalError) as error:
            raise DirectActionJournalError("direct-action-journal-unavailable", "cannot seal canonical Journal append context") from error

    def _append(self, event: Mapping[str, Any], *, result_ref: str | None, effect_refs: list[str]) -> dict[str, Any]:
        context = self._context(event)
        try:
            return work_journal.append_sealed_events(
                self.root,
                [event],
                author=context["author"],
                local_date=context["local_date"],
                timezone=context["timezone"],
                append_context=context,
            )[0]
        except OSError as error:
            try:
                work_journal.store_pending_event(
                    self.root,
                    event,
                    context,
                    result_ref=result_ref,
                    effect_refs=effect_refs,
                    diagnostic="direct Action Journal append failure",
                )
            except (OSError, RuntimeError, work_journal.WorkJournalError) as pending_error:
                raise DirectActionJournalError(
                    "direct-action-recording-unrecoverable",
                    "Journal append failed and original event recovery evidence could not be stored",
                ) from pending_error
            self.pending[str(event["event_id"])] = {
                "event": dict(event),
                "context": context,
                "run_id": event["run"]["run_id"],
            }
            raise DirectActionJournalError(
                "direct-action-recording-pending",
                f"canonical Journal append failed; recover only original event {event['event_id']}",
            ) from error
        except work_journal.WorkJournalError as error:
            # A deterministic identity collision is safe only when reopening
            # proves the recorded event is the exact expected one.  The caller
            # does that immediately after this helper returns or raises.
            raise DirectActionJournalError("direct-action-journal-rejected", str(error)) from error

    def _existing_terminal(
        self,
        identity: str,
        requested_run_id: str,
        intent: Mapping[str, str],
        binding: Mapping[str, Any],
        run_id: str,
    ) -> tuple[dict[str, Any], dict[str, Any]] | None:
        prefix = f"direct-action:{identity}:terminal:"
        found: tuple[dict[str, Any], dict[str, Any]] | None = None
        events, snapshot = _bounded_journal_events(
            self.root,
            '"event:/run/run_id" = ' + json.dumps(run_id),
        )
        if events and snapshot is None:  # Defensive: a physical event cannot come from an absent Journal.
            raise DirectActionJournalError("direct-action-journal-invalid", "canonical Journal event lacks bounded provenance")
        for event in events:
            event_id = event.get("event_id")
            if not isinstance(event_id, str) or not event_id.startswith(prefix):
                continue
            assert snapshot is not None
            receipt = _receipt_from_sidecar(self.root, event, snapshot)
            self._validate_terminal_shape(event, run_id, requested_run_id, intent, binding)
            if found is not None:
                raise DirectActionJournalError("direct-action-journal-invalid", "one direct Action has conflicting terminal evidence")
            found = (event, receipt)
        return found

    def _pending_event(self, event_id: str) -> dict[str, Any] | None:
        """Return the exact sealed pending event, if one exists, without retrying it."""
        try:
            _, event, _, _ = work_journal._read_pending_event(self.root, event_id)
        except work_journal.WorkJournalError as error:
            if error.code == "pending-not-found":
                return None
            raise DirectActionJournalError("direct-action-pending-invalid", str(error)) from error
        return event

    def _refuse_restoration_pending(self, run_id: str) -> None:
        """Refuse every original-Run pending carrier without recovering or replacing it."""
        try:
            relative = work_journal.configured_runtime_root(self.root) / "state/work_journal/pending"
            _safe_ref(relative.as_posix(), "pending Journal root")
            directory = self.root
            for part in relative.parts:
                directory /= part
                if directory.is_symlink() or (directory.exists() and not directory.is_dir()):
                    raise DirectActionJournalError("direct-action-pending-invalid", "pending Journal root has an unsafe ancestor")
            if not directory.exists():
                return
            for carrier in sorted(directory.iterdir()):
                if not carrier.name.startswith(run_id + ":"):
                    continue
                if carrier.is_symlink() or not carrier.is_file() or carrier.suffix != ".json":
                    raise DirectActionJournalError("direct-action-pending-invalid", "original Run pending carrier is unsafe")
                event = self._pending_event(carrier.stem)
                event_run = event.get("run") if event is not None else None
                if not isinstance(event_run, Mapping) or event_run.get("run_id") != run_id:
                    raise DirectActionJournalError("direct-action-pending-invalid", "original Run pending carrier does not retain its event identity")
                raise DirectActionJournalError("direct-action-recording-pending", "original Run has pending Journal evidence; recover only its exact sealed event")
        except (OSError, RuntimeError, work_journal.WorkJournalError) as error:
            if isinstance(error, DirectActionJournalError):
                raise
            raise DirectActionJournalError("direct-action-pending-invalid", "cannot safely inspect original Run pending evidence") from error

    def _validate_started(
        self,
        event: Mapping[str, Any],
        requested_run_id: str,
        intent: Mapping[str, str],
        binding: Mapping[str, Any],
        run_id: str,
    ) -> None:
        if event.get("event") != "started" or event.get("outcome") is not None:
            raise DirectActionJournalError("direct-action-journal-invalid", "reopened event is not a started direct Action")
        self._validate_terminal_shape(event, run_id, requested_run_id, intent, binding, allow_nonterminal=True)

    def _validate_terminal(
        self,
        event: Mapping[str, Any],
        run_id: str,
        requested_run_id: str,
        intent: Mapping[str, str],
        binding: Mapping[str, Any],
        expected: Mapping[str, Any],
    ) -> None:
        self._validate_terminal_shape(event, run_id, requested_run_id, intent, binding)
        if dict(event) != dict(expected):
            raise DirectActionJournalError("direct-action-journal-invalid", "reopened terminal evidence does not match this Action result")

    def _validate_terminal_shape(
        self,
        event: Mapping[str, Any],
        run_id: str,
        requested_run_id: str,
        intent: Mapping[str, str],
        binding: Mapping[str, Any],
        *,
        allow_nonterminal: bool = False,
    ) -> None:
        expected_intent_identity = self._intent_identity(intent, binding)
        actual_session = event.get("llm_session")
        if (
            isinstance(actual_session, Mapping)
            and actual_session.get("app") == DIRECT_ACTION_APP
            and event.get("run", {}).get("run_id") == run_id
            and actual_session.get("uuid") != expected_intent_identity
        ):
            raise DirectActionJournalError(
                "direct-action-intent-conflict",
                "requested_run_id already binds a different immutable direct Action intent",
            )
        if (
            event.get("schema_version") != 5
            or event.get("kind") != "workflow_execution"
            or event.get("action_id") != self.action_id
            or event.get("author") != self.author
            or event.get("llm_session") != {"app": DIRECT_ACTION_APP, "uuid": expected_intent_identity}
            or event.get("structural_scope") != STRUCTURAL_SCOPE
            or event.get("initiative") != {
                "initiative_id": self.descriptor.atom_id,
                "instruction_summary": "Operator " + self.authorization["operator"]
                + " authorized " + self.descriptor.instruction + "; intent SHA-256 "
                + expected_intent_identity,
                "initiative_ref": self.authorization["authorization_ref"],
            }
            or event.get("run") != {
                "run_id": run_id,
                "kind": "action",
                "definition": {key: binding[key] for key in ("atom_id", "version", "path", "digest")},
            }
            or event.get("definition_bindings") != [dict(binding)]
            or event.get("input_ref") != self.authorization["authorization_ref"]
        ):
            raise DirectActionJournalError("direct-action-journal-invalid", "reopened Journal event does not bind this direct Action")
        if not allow_nonterminal and event.get("event") not in {"completed", "failed", "abandoned"}:
            raise DirectActionJournalError("direct-action-journal-invalid", "reopened Journal event is not terminal direct Action evidence")

    @staticmethod
    def _effect_refs(value: object) -> list[str]:
        if not isinstance(value, list) or len(set(value)) != len(value):
            raise DirectActionJournalError("direct-action-invalid-effects", "effect_refs must be a duplicate-free list")
        return [str(_safe_ref(item, "effect_ref")) for item in value]

    def _require_open_run(self, run_id: str) -> dict[str, Any]:
        if self._closed or not self._invocation_locks:
            raise DirectActionJournalError("direct-action-invocation-closed", "direct Action invocation no longer holds its exclusive lock")
        if not isinstance(run_id, str) or run_id not in self.actual:
            raise DirectActionJournalError("direct-action-unknown-run", "Action Run is not started by this session")
        if run_id in self.terminal or any(item.get("run_id") == run_id for item in self.pending.values()):
            raise DirectActionJournalError("direct-action-terminal", "Action Run already has terminal or pending Journal evidence")
        return self.actual[run_id]

    @staticmethod
    def _terminal_result(event: Mapping[str, Any], receipt: Mapping[str, Any]) -> dict[str, Any]:
        return {
            "event_id": event["event_id"],
            "run_id": event["run"]["run_id"],
            "disposition": "terminal",
            "outcome": event["outcome"],
            "result_ref": event["result_ref"],
            "effect_refs": list(event["effect_refs"]),
            "report_ref": event["report_ref"],
            "event_receipt": dict(receipt),
        }


__all__ = [
    "ACTION_ATOM_ID",
    "ACTION_ATOM_RELATIVE",
    "ACTION_ATOM_SHA256",
    "ACTION_ATOM_VERSION",
    "DIRECT_ACTION_APP",
    "DirectActionJournalError",
    "DirectActionSession",
    "INITIALIZATION_ACTION_ID",
    "INSTALLATION_ACTION_ID",
    "INSTALLATION_ATOM_RELATIVE",
    "INSTALLATION_ATOM_SHA256",
    "INSTALLATION_ATOM_VERSION",
    "RESTORATION_ACTION_ID",
    "RESTORATION_ATOM_ID",
    "RESTORATION_ATOM_RELATIVE",
    "RESTORATION_ATOM_SHA256",
    "RESTORATION_ATOM_VERSION",
    "SOURCE_ADMISSION_ACTION_ID",
    "SOURCE_ADMISSION_ATOM_RELATIVE",
    "SOURCE_ADMISSION_ATOM_SHA256",
    "SOURCE_ADMISSION_ATOM_VERSION",
]
