"""Source-bound direct Action state with optional plain Journal logging.

Retained invocation observations prevent source-effect replay. Their log
append has no validation, receipt, deduplication or recording-retry prerequisite.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import re
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import work_journal
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
SOURCE_ADMISSION_ATOM_VERSION = 3
SOURCE_ADMISSION_ATOM_RELATIVE = ACTION_ATOM_RELATIVE.parent / "CA-O-199-PROJECT_CONFIGURATION-ACTION--admit-local-package-sources.md"
SOURCE_ADMISSION_ATOM_SHA256 = "210e558c256f923e818dce60cf365500fc61c9b14223f7de6177874dd79b7a73"
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








def _reopen_event(root: Path, event_id: str) -> tuple[dict[str, Any], None] | None:
    """Read a retained invocation observation, not a Journal integrity proof."""
    matches = [event for event in work_journal.read_records(root)
               if isinstance(event, dict) and event.get("event_id") == event_id]
    return (matches[-1], None) if matches else None


class DirectActionSession:
    """One explicitly authorized direct Action with best-effort plain logging.

    ``actual``, ``terminal``, and ``receipts`` are intentionally small
    observable state for the installer.  They are not a durable side ledger;
    retained log observations are one input to the source-operation replay guard.
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
        self.recording_errors: list[str] = []
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

    def begin_action(self, *, action_id: str, requested_run_id: str,
                     intent: Mapping[str, Any]) -> Mapping[str, Any]:
        """Own one authorized invocation; logging is not an effect prerequisite."""
        if self._closed:
            raise DirectActionJournalError("direct-action-invocation-closed", "direct Action session is closed")
        if action_id != self.action_id:
            raise DirectActionJournalError("direct-action-unadmitted", "Action is not admitted by this Session")
        if not isinstance(requested_run_id, str) or _RUN_ID.fullmatch(requested_run_id) is None:
            raise DirectActionJournalError("direct-action-invalid-run", "requested_run_id has invalid syntax")
        _authorization(self.root, self.authorization, journal_author=self.author,
                       operators_registry_ref=self.operators_registry_ref)
        normalized = _intent(intent, self.action_id)
        binding = _source_binding(self.root, self.action_id, action_package=self._action_package)
        identity = self._run_identity(requested_run_id, binding)
        run_id = f"direct-action:{identity}"
        if run_id in self.actual:
            raise DirectActionJournalError("direct-action-invocation-active", "this invocation is already active")
        self._acquire_invocation_lock(requested_run_id, binding)
        try:
            started_id = f"{run_id}:started"
            terminal = self._existing_terminal(identity, requested_run_id, normalized, binding, run_id)
            if terminal is not None:
                raise DirectActionJournalError("direct-action-already-terminal", "retained source invocation must not be replayed")
            reopened = _reopen_event(self.root, started_id)
            if reopened is not None:
                self._validate_started(reopened[0], requested_run_id, normalized, binding, run_id)
                raise DirectActionJournalError("direct-action-recovery-required", "retained source invocation must not be replayed")
            event = self._event(event_id=started_id, run_id=run_id, requested_run_id=requested_run_id,
                                intent=normalized, binding=binding, event_name="started", outcome=None,
                                result_ref=None, effect_refs=[], report_ref=None)
            self.actual[run_id] = {"requested_run_id": requested_run_id, "intent": normalized,
                                  "binding": binding, "authorization": dict(self.authorization),
                                  "event_id": started_id, "event": event}
            self._append(event, result_ref=None, effect_refs=[])
            return {"run_id": run_id, "disposition": "started", "event_id": started_id,
                    "recording_errors": list(self.recording_errors)}
        except BaseException:
            self._release_invocation_lock()
            raise

    def read_recorded_action_start(self, action_run_id: str) -> RecordedActionStartProvenance:
        """Read this Session's actual source-bound Action identity."""
        actual = self.actual.get(action_run_id)
        if not isinstance(actual, Mapping):
            raise DirectActionJournalError("direct-action-start-invalid", "Action is not owned by this Session")
        return RecordedActionStartProvenance(author=self.author, event_id=actual["event_id"],
                                            action_run_id=action_run_id, parent_lineage=())

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

    def finish_action(self, run_id: str, *, outcome: str, result_ref: str,
                      effect_refs: list[str], report_ref: str | None = None) -> Mapping[str, Any]:
        """Retain actual completion regardless of the optional log append."""
        run = self._require_open_run(run_id)
        if outcome not in _OUTCOMES:
            raise DirectActionJournalError("direct-action-invalid-outcome", "outcome is not admitted")
        result = str(_safe_ref(result_ref, "result_ref"))
        effects = self._effect_refs(effect_refs)
        report = _safe_ref(report_ref, "report_ref", allow_none=True)
        recording_ref = run.get("recording_authorization_ref")
        if recording_ref is not None and str(report) != recording_ref:
            raise DirectActionJournalError("direct-action-recording-authorization-invalid", "report differs from command")
        if self._observed.get(run_id) != {"result_ref": result, "effect_refs": effects}:
            raise DirectActionJournalError("direct-action-effects-unobserved", "terminal result must bind observed effects")
        identity = self._run_identity(run["requested_run_id"], run["binding"])
        terminal_key = work_journal.canonical_json_digest({
            "intent_sha256": self._intent_identity(run["intent"], run["binding"], authorization=run.get("authorization")),
            "outcome": outcome, "result_ref": result, "effect_refs": effects, "report_ref": report})
        event_name = {"completed": "completed", "no_op": "completed", "failed": "failed",
                      "partial": "failed", "cancelled": "abandoned"}[outcome]
        event = self._event(event_id=f"direct-action:{identity}:terminal:{terminal_key}", run_id=run_id,
                            requested_run_id=run["requested_run_id"], intent=run["intent"], binding=run["binding"],
                            event_name=event_name, outcome=outcome, result_ref=result,
                            effect_refs=effects, report_ref=report, authorization=run.get("authorization"))
        try:
            value = self._terminal_result(event)
            self.terminal[run_id] = value
            self._append(event, result_ref=result, effect_refs=effects)
            value["recording_errors"] = list(self.recording_errors)
            return dict(value)
        finally:
            self._release_invocation_lock()
            self._closed = True

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

    def _intent_identity(
        self,
        intent: Mapping[str, str],
        binding: Mapping[str, Any],
        *,
        authorization: Mapping[str, Any] | None = None,
    ) -> str:
        identity_authorization = self.authorization if authorization is None else authorization
        return work_journal.canonical_json_digest(
            {
                "intent": dict(intent),
                "binding": dict(binding),
                "operator": identity_authorization["operator"],
                "authorization_ref": identity_authorization["authorization_ref"],
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
        authorization: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        moment = self._now()
        if self.timezone == "UTC":
            moment = moment.astimezone(dt.UTC)
        event_authorization = self.authorization if authorization is None else authorization
        payload: dict[str, Any] = {
            "schema_version": 5,
            "kind": "workflow_execution",
            "event_id": event_id,
            "action_id": self.action_id,
            "event": event_name,
            "author": self.author,
            "occurred_at": moment.isoformat(timespec="seconds"),
            "llm_session": {
                "app": DIRECT_ACTION_APP,
                "uuid": self._intent_identity(intent, binding, authorization=event_authorization),
            },
            "structural_scope": STRUCTURAL_SCOPE,
            "initiative": {
                "initiative_id": self.descriptor.atom_id,
                "instruction_summary": "Operator " + event_authorization["operator"]
                + " authorized " + self.descriptor.instruction + "; intent SHA-256 "
                + self._intent_identity(intent, binding, authorization=event_authorization),
                "initiative_ref": event_authorization["authorization_ref"],
            },
            "run": {
                "run_id": run_id,
                "kind": "action",
                "definition": {key: binding[key] for key in ("atom_id", "version", "path", "digest")},
            },
            "definition_bindings": [dict(binding)],
            "input_ref": event_authorization["authorization_ref"],
            "outcome": outcome,
            "result_ref": result_ref,
            "effect_refs": list(effect_refs),
            "report_ref": report_ref,
            "redaction": {"redacted": False, "fields": []},
        }
        return payload

    def _append(self, event: Mapping[str, Any], *, result_ref: str | None,
                effect_refs: list[str]) -> dict[str, Any] | None:
        del result_ref, effect_refs
        occurred = dt.datetime.fromisoformat(str(event["occurred_at"]))
        try:
            location = work_journal.append_sealed_events(self.root, [event], author=self.author,
                                                        local_date=occurred.date().isoformat(), timezone=self.timezone)[0]
        except (OSError, RuntimeError, TypeError, ValueError) as error:
            self.recording_errors.append(str(error))
            return None
        self.receipts.append(location)
        return location

    def _existing_terminal(self, identity: str, requested_run_id: str, intent: Mapping[str, str],
                           binding: Mapping[str, Any], run_id: str) -> tuple[dict[str, Any], None] | None:
        prefix = f"direct-action:{identity}:terminal:"
        events = [event for event in work_journal.read_records(self.root)
                  if isinstance(event, dict) and str(event.get("event_id", "")).startswith(prefix)]
        if not events:
            return None
        event = events[-1]
        self._validate_terminal_shape(event, run_id, requested_run_id, intent, binding)
        return event, None



    def _validate_started(
        self,
        event: Mapping[str, Any],
        requested_run_id: str,
        intent: Mapping[str, str],
        binding: Mapping[str, Any],
        run_id: str,
        *,
        authorization: Mapping[str, Any] | None = None,
    ) -> None:
        if event.get("event") != "started" or event.get("outcome") is not None:
            raise DirectActionJournalError("direct-action-journal-invalid", "reopened event is not a started direct Action")
        self._validate_terminal_shape(
            event, run_id, requested_run_id, intent, binding,
            allow_nonterminal=True, authorization=authorization,
        )

    def _validate_terminal_shape(
        self,
        event: Mapping[str, Any],
        run_id: str,
        requested_run_id: str,
        intent: Mapping[str, str],
        binding: Mapping[str, Any],
        *,
        allow_nonterminal: bool = False,
        authorization: Mapping[str, Any] | None = None,
    ) -> None:
        event_authorization = self.authorization if authorization is None else authorization
        expected_intent_identity = self._intent_identity(
            intent, binding, authorization=event_authorization,
        )
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
            event.get("action_id") != self.action_id
            or event.get("author") != self.author
            or event.get("llm_session") != {"app": DIRECT_ACTION_APP, "uuid": expected_intent_identity}
            or event.get("structural_scope") != STRUCTURAL_SCOPE
            or event.get("initiative") != {
                "initiative_id": self.descriptor.atom_id,
                "instruction_summary": "Operator " + event_authorization["operator"]
                + " authorized " + self.descriptor.instruction + "; intent SHA-256 "
                + expected_intent_identity,
                "initiative_ref": event_authorization["authorization_ref"],
            }
            or event.get("run") != {
                "run_id": run_id,
                "kind": "action",
                "definition": {key: binding[key] for key in ("atom_id", "version", "path", "digest")},
            }
            or event.get("definition_bindings") != [dict(binding)]
            or event.get("input_ref") != event_authorization["authorization_ref"]
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
        if run_id in self.terminal:
            raise DirectActionJournalError("direct-action-terminal", "Action Run already has an actual terminal result")
        return self.actual[run_id]

    @staticmethod
    def _terminal_result(event: Mapping[str, Any]) -> dict[str, Any]:
        return {key: event[key] for key in ("event_id", "outcome", "result_ref", "effect_refs", "report_ref")} | {
            "run_id": event["run"]["run_id"], "disposition": "terminal"}


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
