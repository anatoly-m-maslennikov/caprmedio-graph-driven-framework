"""Physical, non-promoting inputs for one fresh public Full Gate.

This module deliberately stops before executing Unit or candidate-E2E work.
It reopens the immutable native packet, the currently selected native N, the
locally reread public source proof, and the already-admitted public Action.
The returned carrier has no outcome or receipt: a later, bounded producer
must perform and retain the fresh test work.
"""

from __future__ import annotations

import hashlib
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Mapping


_TOOLS_ROOT = Path(__file__).resolve().parents[1]
_PUBLIC_RELEASE_ROOT = _TOOLS_ROOT / "PUBLIC_RELEASE"
_MCP_ROOT = _TOOLS_ROOT.parent / "204_MCP"
for _path in (str(_TOOLS_ROOT), str(_PUBLIC_RELEASE_ROOT), str(_MCP_ROOT)):
    if _path not in sys.path:
        sys.path.insert(0, _path)

from public_release import (  # noqa: E402
    STEPS,
    WORKFLOW_ID,
    SourceProof,
    _expected_runs,
    _parameters,
    _source,
    document_closure_digest,
)
from release_contract import ReleaseContractError  # noqa: E402
from release_full_gate import verify_detached_native_full_gate_evidence  # noqa: E402
from release_handoff import NativeInstalledNBinding, reopen_native_installed_n  # noqa: E402
from release_promotion import bind_selected_native_n_from_checkpoint  # noqa: E402
from release_retained_package import RetainedNativePackageEvidence  # noqa: E402
from retained_full_gate_packet import RetainedNativeFullGatePacket  # noqa: E402
from selected_routes import SELECTED_ROUTE_NAMES, load_selected_manifest  # noqa: E402
from workflow_run_support import RunExecutionSession, RunTracker, _canonical_digest, _proposal  # noqa: E402


_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_IMAGE = re.compile(r"^(?:sha256:)?([0-9a-f]{64})$")
_ACTION_PHASES: dict[str, tuple[Literal["initial", "history_link"], str]] = {
    "CA-O-194": ("initial", "CA-O-193"),
    "CA-O-198": ("history_link", "CA-O-197"),
}


class PublicFreshGateInputError(ReleaseContractError):
    """A public fresh-gate input cannot be physically reopened."""


@dataclass(frozen=True)
class PublicFreshGateInputs:
    """Reopened prerequisites for one later fresh public Full Gate.

    This is neither a pass claim nor an execution authorization.  Its fields
    are populated only by reopen_public_fresh_gate_inputs.
    """

    project_root: Path
    session: RunExecutionSession
    phase: Literal["initial", "history_link"]
    action_run_id: str
    action_definition_id: str
    source: SourceProof
    public_document_closure_sha256: str
    original_packet: RetainedNativeFullGatePacket
    retained_package: RetainedNativePackageEvidence
    current_native_n: NativeInstalledNBinding
    fresh_attempt_root: Path


def _refuse(code: str, message: str) -> None:
    raise PublicFreshGateInputError(code, message)


def _project_root(value: str | Path) -> Path:
    try:
        root = Path(value).resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise PublicFreshGateInputError("public-gate-project-unavailable", "selected Project root is unavailable") from error
    if root.is_symlink() or not root.is_dir():
        _refuse("public-gate-project-invalid", "selected Project root must be one real directory")
    return root


def _sha256(value: object, *, field: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        _refuse("public-gate-input-invalid", f"{field} must be a lowercase SHA-256")
    return value


def _image_digest(value: object, *, field: str) -> str:
    if not isinstance(value, str):
        _refuse("public-gate-input-invalid", f"{field} must be an immutable image digest")
    matched = _IMAGE.fullmatch(value)
    if matched is None:
        _refuse("public-gate-input-invalid", f"{field} must be an immutable image digest")
    return matched.group(1)


def _document_closure(source: SourceProof) -> str:
    """Derive R1922's closure through PUBLIC_RELEASE's canonical source codec."""

    return document_closure_digest(source)


def _reopen_source(root: Path, session: RunExecutionSession, source: object) -> tuple[SourceProof, str]:
    if not isinstance(source, SourceProof):
        _refuse("public-gate-source-untrusted", "fresh public gate requires one typed SourceProof")
    request = session.request
    if not isinstance(request, Mapping) or not isinstance(request.get("parameters"), Mapping):
        _refuse("public-gate-session-invalid", "selected public Session has no sealed parameters")
    try:
        parameters = _parameters(request["parameters"])
        release = parameters["release"]
        reopened = _source(source, "public fresh gate source proof", project_root=root, release=release)
    except Exception as error:
        raise PublicFreshGateInputError(
            "public-gate-source-stale", "public SourceProof cannot be physically reread"
        ) from error
    admitted = parameters["source"]
    bindings = (
        ("candidate_snapshot_manifest_sha256", reopened.candidate_snapshot_manifest_sha256),
        ("readme_ref", reopened.readme_ref),
        ("pr_body_ref", reopened.pr_body_ref),
        ("version_history_ref", reopened.version_history_ref),
        ("version_history_summary", reopened.version_history_summary),
    )
    if any(admitted[field] != observed for field, observed in bindings):
        _refuse(
            "public-gate-source-mismatch",
            "admitted public source parameters differ from the physically reopened SourceProof",
        )
    closure = _document_closure(reopened)
    claimed = getattr(reopened, "public_document_closure_sha256", None)
    if _sha256(claimed, field="SourceProof.public_document_closure_sha256") != closure:
        _refuse("public-gate-source-stale", "SourceProof closure differs from locally reread document carriers")
    return reopened, closure


def _require_phase_source(phase: Literal["initial", "history_link"], source: SourceProof) -> None:
    """Keep the derived post-PR link proof out of the initial-gate contract."""

    if phase == "history_link" and (
        source.version_history_pr_url is None
        or type(source.version_history_pr_number) is not int
        or source.version_history_pr_number < 1
    ):
        _refuse(
            "public-gate-history-source-unproven",
            "history-link public gate requires the actual Version History PR URL and number",
        )


def _expected_request_definitions(public_route: Mapping[str, object]) -> dict[str, dict[str, object]]:
    """Project the one source-validated public route into Run definitions."""

    workflow = public_route.get("workflow")
    pairs = public_route.get("ordered_steps")
    if not isinstance(workflow, Mapping) or not isinstance(pairs, list) or len(pairs) != len(STEPS):
        _refuse("public-gate-session-unadmitted", "selected public route has no complete admitted definition frontier")

    pins: list[tuple[str, object]] = [("workflow", workflow)]
    for pair in pairs:
        if not isinstance(pair, Mapping):
            _refuse("public-gate-session-unadmitted", "selected public route has a malformed Step/Action pair")
        pins.extend((("step", pair.get("step")), ("action", pair.get("action"))))

    expected: dict[str, dict[str, object]] = {}
    for kind, pin in pins:
        if not isinstance(pin, Mapping):
            _refuse("public-gate-session-unadmitted", "selected public route has an untyped definition pin")
        atom_id = pin.get("atom_id")
        version = pin.get("version")
        source_path = pin.get("source_path")
        digest = pin.get("digest")
        if (
            not isinstance(atom_id, str)
            or type(version) is not int
            or not isinstance(source_path, str)
            or not isinstance(digest, str)
            or atom_id in expected
        ):
            _refuse("public-gate-session-unadmitted", "selected public route has an invalid definition pin")
        expected[atom_id] = {
            "atom_id": atom_id,
            "version": version,
            "path": source_path,
            "digest": digest,
            "kind": kind,
        }
    return expected


def _admitted_session(root: Path, session: object) -> RunExecutionSession:
    """Reread the canonical public route before accepting an active Session.

    This is a read-only revalidation of the existing selected-run admission;
    it does not publish a manifest or introduce another authorization layer.
    """

    if not isinstance(session, RunExecutionSession) or not isinstance(getattr(session, "tracker", None), RunTracker):
        _refuse("public-gate-session-invalid", "fresh public gate requires one actual selected RunExecutionSession")
    request = session.request
    if not isinstance(request, Mapping):
        _refuse("public-gate-session-invalid", "selected public Session request is unavailable")
    try:
        _expected_runs(request)
        manifest = load_selected_manifest(root)
    except Exception as error:
        raise PublicFreshGateInputError(
            "public-gate-session-unadmitted", "current public selected-route source admission cannot be physically reopened"
        ) from error

    expected_routes = [*SELECTED_ROUTE_NAMES, "release_version", "public.release"]
    routes = manifest.get("routes") if isinstance(manifest, Mapping) else None
    if not isinstance(routes, list) or [row.get("route") if isinstance(row, Mapping) else None for row in routes] != expected_routes:
        _refuse("public-gate-session-unadmitted", "current selected manifest is not the canonical seventeen-route public successor")
    public_route = routes[-1]
    expected_definitions = _expected_request_definitions(public_route)
    definition_manifest = request.get("definition_manifest")
    if (
        not isinstance(definition_manifest, Mapping)
        or dict(definition_manifest) != {
            "manifest_ref": manifest.get("manifest_ref"),
            "manifest_digest": manifest.get("canonical_manifest_sha256"),
        }
        or request.get("source_freshness") != manifest.get("source_freshness")
    ):
        _refuse("public-gate-session-unadmitted", "selected public Session differs from the current canonical manifest")

    requested = request.get("requested_runs")
    if not isinstance(requested, list) or len(requested) != len(expected_definitions):
        _refuse("public-gate-session-unadmitted", "selected public Session has an incomplete requested definition frontier")
    for row in requested:
        definition = row.get("definition") if isinstance(row, Mapping) else None
        atom_id = definition.get("atom_id") if isinstance(definition, Mapping) else None
        expected = expected_definitions.get(atom_id) if isinstance(atom_id, str) else None
        if expected is None or row.get("kind") != expected["kind"] or definition != {
            key: expected[key] for key in ("atom_id", "version", "path", "digest")
        }:
            _refuse("public-gate-session-unadmitted", "selected public Session definition frontier differs from the admitted route")

    tracker = session.tracker
    try:
        observation = tracker._observe(dict(request))
        proposal = _proposal(request, observation)
        tracker._validate_execute(dict(request), proposal, _canonical_digest(proposal))
    except Exception as error:
        raise PublicFreshGateInputError(
            "public-gate-session-unadmitted", "selected public Session has no current execute admission"
        ) from error
    return session


def _reopen_recorded_start(
    session: RunExecutionSession, requested_id: str, actual: Mapping[str, object], *, label: str,
) -> None:
    """Reread one non-Action start receipt without trusting mutable Session state."""

    receipts = getattr(session, "_started_receipts", None)
    receipt = receipts.get(requested_id) if isinstance(receipts, Mapping) else None
    if not isinstance(receipt, Mapping):
        _refuse("public-gate-action-lineage-invalid", f"current public {label} has no retained start receipt")
    try:
        event = session._reopen_started_event(receipt)
    except Exception as error:
        raise PublicFreshGateInputError(
            "public-gate-action-lineage-invalid", f"current public {label} start cannot be physically reread"
        ) from error
    if (
        event.get("schema_version") != 5
        or event.get("kind") != "workflow_execution"
        or event.get("event") != "started"
        or event.get("run") != dict(actual)
    ):
        _refuse(
            "public-gate-action-lineage-invalid",
            f"receipt-addressed public {label} start differs from the admitted active lineage",
        )


def _active_action(root: Path, session: object) -> tuple[RunExecutionSession, Literal["initial", "history_link"], str, str]:
    if not isinstance(session, RunExecutionSession):
        _refuse("public-gate-session-invalid", "fresh public gate requires the admitted RunExecutionSession")
    tracker_root = getattr(getattr(session, "tracker", None), "root", None)
    try:
        if Path(tracker_root).resolve(strict=True) != root:
            _refuse("public-gate-session-root-mismatch", "selected Session belongs to another Project")
    except (OSError, TypeError, ValueError) as error:
        raise PublicFreshGateInputError("public-gate-session-invalid", "selected Session root cannot be reopened") from error
    request = session.request
    if not isinstance(request, Mapping) or request.get("mode") != "execute" or request.get("operation_route") != "public.release":
        _refuse("public-gate-session-invalid", "fresh public gate requires one admitted public.release execute Session")
    if not isinstance(session.requested, Mapping) or not isinstance(session.actual, Mapping):
        _refuse("public-gate-session-invalid", "selected Session has no sealed Run lineage")
    declared = request.get("requested_runs")
    if not isinstance(declared, list):
        _refuse("public-gate-session-invalid", "selected Session has no sealed requested-Run graph")
    derived: dict[str, object] = {}
    for row in declared:
        if not isinstance(row, Mapping) or not isinstance(row.get("requested_run_id"), str) or row["requested_run_id"] in derived:
            _refuse("public-gate-session-invalid", "selected Session requested-Run graph is malformed")
        derived[row["requested_run_id"]] = row
    if derived != dict(session.requested):
        _refuse("public-gate-session-invalid", "selected Session lineage differs from its sealed request")

    found: list[tuple[Literal["initial", "history_link"], str, str]] = []
    for requested_id, requested in session.requested.items():
        if not isinstance(requested_id, str) or not isinstance(requested, Mapping):
            continue
        definition = requested.get("definition")
        action_id = definition.get("atom_id") if isinstance(definition, Mapping) else None
        specification = _ACTION_PHASES.get(action_id)
        if specification is None:
            continue
        record = session.actual.get(requested_id)
        if not isinstance(record, Mapping) or requested_id in session.terminal or requested_id in session.interrupted:
            continue
        phase, expected_parent_action = specification
        parent_requested_id = requested.get("parent_requested_run_id")
        parent_requested = session.requested.get(parent_requested_id) if isinstance(parent_requested_id, str) else None
        parent = session.actual.get(parent_requested_id) if isinstance(parent_requested_id, str) else None
        parent_definition = parent.get("definition") if isinstance(parent, Mapping) else None
        workflow_requested_id = (
            parent_requested.get("parent_requested_run_id") if isinstance(parent_requested, Mapping) else None
        )
        workflow = session.actual.get(workflow_requested_id) if isinstance(workflow_requested_id, str) else None
        workflow_definition = workflow.get("definition") if isinstance(workflow, Mapping) else None
        if (
            requested.get("kind") != "action"
            or record.get("kind") != "action"
            or record.get("definition") != definition
            or not isinstance(record.get("run_id"), str)
            or not record["run_id"]
            or not isinstance(parent_requested, Mapping)
            or parent_requested.get("kind") != "step"
            or not isinstance(parent, Mapping)
            or parent.get("kind") != "step"
            or not isinstance(parent_definition, Mapping)
            or parent_definition.get("atom_id") != expected_parent_action
            or record.get("parent_run_id") != parent.get("run_id")
            or not isinstance(workflow, Mapping)
            or workflow.get("kind") != "workflow"
            or not isinstance(workflow_definition, Mapping)
            or workflow_definition.get("atom_id") != WORKFLOW_ID
            or parent.get("parent_run_id") != workflow.get("run_id")
        ):
            _refuse("public-gate-action-lineage-invalid", "current public Action has no exact started parent Step")
        try:
            provenance = session.read_recorded_action_start(record["run_id"])
        except Exception as error:
            raise PublicFreshGateInputError(
                "public-gate-action-lineage-invalid",
                "current public Action has no receipt-addressed recorded start",
            ) from error
        _reopen_recorded_start(session, parent_requested_id, parent, label="parent Step")
        _reopen_recorded_start(session, workflow_requested_id, workflow, label="Workflow")
        if (
            provenance.action_run_id != record["run_id"]
            or provenance.parent_lineage != (parent["run_id"], workflow["run_id"])
        ):
            _refuse(
                "public-gate-action-lineage-invalid",
                "receipt-addressed public Action start differs from the admitted active lineage",
            )
        found.append((phase, record["run_id"], action_id))
    if len(found) != 1:
        _refuse("public-gate-action-unavailable", "exactly one active O194 or O198 Action is required")
    return session, *found[0]


def _fresh_attempt_root(root: Path, action_run_id: str) -> Path:
    if not isinstance(action_run_id, str) or not action_run_id or "\x00" in action_run_id:
        _refuse("public-gate-action-lineage-invalid", "active public Action has no safe Run identity")
    # Never use a caller-controlled run identifier as a filesystem component.
    return root / ".caprmedio_tmp" / "public_release_full_gate" / hashlib.sha256(action_run_id.encode("utf-8")).hexdigest()


def _reopen_original_packet(root: Path, packet: object) -> RetainedNativePackageEvidence:
    if not isinstance(packet, RetainedNativeFullGatePacket):
        _refuse("public-gate-original-packet-invalid", "fresh public gate requires one typed retained native Full Gate packet")
    try:
        artifact_root = Path(packet.artifact_root).resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise PublicFreshGateInputError(
            "public-gate-original-packet-invalid", "original native Full Gate artifact root is unavailable"
        ) from error
    if artifact_root != root:
        _refuse("public-gate-original-packet-invalid", "original native Full Gate belongs to another Project")
    try:
        retained = verify_detached_native_full_gate_evidence(
            artifact_root,
            packet.retained_candidate,
            packet.suite,
            packet.build,
            packet.verification,
            packet.e2e,
            packet.evidence,
        )
    except Exception as error:
        raise PublicFreshGateInputError(
            "public-gate-original-packet-invalid", "original native Full Gate packet cannot be physically reopened"
        ) from error
    if not isinstance(retained, RetainedNativePackageEvidence):
        _refuse("public-gate-original-packet-invalid", "original native packet did not reopen one typed package proof")
    return retained


def _reopen_current_native_n(root: Path) -> NativeInstalledNBinding:
    try:
        discovered = bind_selected_native_n_from_checkpoint(root)
        if not isinstance(discovered, NativeInstalledNBinding):
            _refuse("public-gate-current-n-unavailable", "current selected native N has no exact package proof")
        observed = reopen_native_installed_n(root, discovered)
    except PublicFreshGateInputError:
        raise
    except Exception as error:
        raise PublicFreshGateInputError(
            "public-gate-current-n-unavailable", "current selected native N cannot be physically reopened"
        ) from error
    if not isinstance(observed, NativeInstalledNBinding):
        _refuse("public-gate-current-n-unavailable", "current selected native N reopened an untyped binding")
    return observed


def _require_same_identity(
    source: SourceProof,
    packet: RetainedNativeFullGatePacket,
    retained: RetainedNativePackageEvidence,
    current: NativeInstalledNBinding,
) -> None:
    """Bind D566/D597 facts to the actual selected N+1 without reopening old N."""

    view = retained.view
    evidence = packet.evidence
    selected = current.selected
    package = current.verified_package
    candidate = packet.retained_candidate
    current_packet = current.full_gate_packet
    if (
        not isinstance(current_packet, RetainedNativeFullGatePacket)
        or getattr(getattr(current_packet, "evidence", None), "receipt_sha256", None) != getattr(evidence, "receipt_sha256", None)
        or getattr(getattr(current_packet, "retained_candidate", None), "candidate_snapshot_manifest_sha256", None)
        != source.candidate_snapshot_manifest_sha256
    ):
        _refuse("public-gate-identity-mismatch", "current selected N+1 does not retain the original candidate Full Gate proof")
    fields = (
        (getattr(candidate, "candidate_snapshot_manifest_sha256", None), source.candidate_snapshot_manifest_sha256),
        (getattr(view, "candidate_snapshot_manifest_sha256", None), source.candidate_snapshot_manifest_sha256),
        (getattr(evidence, "candidate_snapshot_manifest_sha256", None), source.candidate_snapshot_manifest_sha256),
        (getattr(candidate, "framework_version", None), source.framework_version),
        (getattr(view, "framework_version", None), source.framework_version),
        (getattr(evidence, "framework_version", None), source.framework_version),
        (getattr(selected, "framework_version", None), source.framework_version),
        (getattr(package, "framework_version", None), source.framework_version),
        (getattr(candidate, "version_toml_sha256", None), source.version_toml_sha256),
        (getattr(view, "version_toml_sha256", None), source.version_toml_sha256),
        (getattr(evidence, "version_toml_sha256", None), source.version_toml_sha256),
        (getattr(selected, "version_toml_sha256", None), source.version_toml_sha256),
        (getattr(package, "version_toml_sha256", None), source.version_toml_sha256),
    )
    if any(actual != expected for actual, expected in fields):
        _refuse("public-gate-identity-mismatch", "selected N+1 differs from the original candidate or selected Version proof")
    package_sha = _sha256(getattr(view, "actual_package_manifest_sha256", None), field="original package manifest")
    if (
        getattr(evidence, "package_manifest_sha256", None) != package_sha
        or getattr(selected, "package_manifest_sha256", None) != package_sha
        or getattr(package, "manifest_digest", None) != package_sha
        or getattr(view, "source_catalog_sha256", None) != getattr(selected, "source_catalog_sha256", None)
        or getattr(view, "source_catalog_sha256", None) != getattr(package, "source_catalog_sha256", None)
        or getattr(selected, "full_gate_receipt_sha256", None) != getattr(evidence, "receipt_sha256", None)
    ):
        _refuse("public-gate-identity-mismatch", "selected N+1 package proof differs from the original retained packet")
    if _image_digest(getattr(evidence, "candidate_image_digest", None), field="original candidate image") != _image_digest(
        getattr(selected, "image_digest", None), field="selected N+1 image"
    ):
        _refuse("public-gate-identity-mismatch", "selected N+1 image differs from the original retained candidate image")


def reopen_public_fresh_gate_inputs(
    project_root: str | Path,
    session: RunExecutionSession,
    original_packet: RetainedNativeFullGatePacket,
    source: SourceProof,
) -> PublicFreshGateInputs:
    """Reopen the only physical inputs admitted to a later fresh public gate.

    The Action phase is derived from the active admitted Session, not accepted
    from a caller.  This function performs no test execution and writes no
    receipt, candidate, package, image, selector, or Journal carrier.
    """

    root = _project_root(project_root)
    admitted_session = _admitted_session(root, session)
    admitted_session, phase, action_run_id, action_definition_id = _active_action(root, admitted_session)
    reopened_source, closure = _reopen_source(root, admitted_session, source)
    _require_phase_source(phase, reopened_source)
    retained = _reopen_original_packet(root, original_packet)
    current = _reopen_current_native_n(root)
    _require_same_identity(reopened_source, original_packet, retained, current)
    return PublicFreshGateInputs(
        project_root=root,
        session=admitted_session,
        phase=phase,
        action_run_id=action_run_id,
        action_definition_id=action_definition_id,
        source=reopened_source,
        public_document_closure_sha256=closure,
        original_packet=original_packet,
        retained_package=retained,
        current_native_n=current,
        fresh_attempt_root=_fresh_attempt_root(root, action_run_id),
    )


__all__ = [
    "PublicFreshGateInputError",
    "PublicFreshGateInputs",
    "reopen_public_fresh_gate_inputs",
]
