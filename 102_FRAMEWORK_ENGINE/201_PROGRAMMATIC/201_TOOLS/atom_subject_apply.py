"""Native, sealed one-target publication of an exact Subjects-only intent."""

from __future__ import annotations

import hashlib
import re
from collections.abc import Mapping
from pathlib import Path
from typing import Any

import atom_operations as operations
from artifact_metadata import current_timestamp


def _fail(code: str, message: str) -> None:
    from lifecycle_intents import LifecycleError
    raise LifecycleError(code, message)


def _parameters(value: Mapping[str, Any]) -> dict[str, Any]:
    required = {"target", "subject_patches", "subject_intent_sha256"}
    if not isinstance(value, Mapping) or not required.issubset(value) or set(value) - (required | {"subject_profile", "semantic_assessment_report"}):
        _fail("subject-update-parameters-invalid", "Subject Update requires one closed target, patch list and intent hash")
    request = dict(value)
    profile = request.get("subject_profile", "legacy")
    if not isinstance(profile, str) or profile not in {"legacy", "approved"}:
        _fail("subject-profile-invalid", "Subject profile must be legacy or approved")
    if not isinstance(request["subject_intent_sha256"], str) or re.fullmatch(r"[0-9a-f]{64}", request["subject_intent_sha256"]) is None:
        _fail("subject-intent-invalid", "Subject intent must have one canonical SHA-256 hash")
    fields = {"atom_id", "path", "filename", "version", "digest", "lifecycle", "status", "updated_at", "content_role", "type"}
    if not isinstance(request["target"], Mapping) or set(request["target"]) != fields:
        _fail("carrier-fields-invalid", "Subject target must carry exactly its complete descriptor")
    return request


def _prepare(root: Path, request: Mapping[str, Any]) -> dict[str, Any]:
    from atom_subject_patch import prepare_subject_intent
    prepared = prepare_subject_intent(root, request["target"], request["subject_patches"],
                                      subject_profile=request.get("subject_profile", "legacy"))
    if prepared["subject_intent_sha256"] != request["subject_intent_sha256"]:
        _fail("subject-intent-stale", "Subject intent differs from the current exact proposal")
    return prepared


def _atom(root: Path, descriptor: Mapping[str, Any], raw: bytes) -> operations.Atom:
    from atom_subject_patch import _raw_frontmatter
    frontmatter, content = _raw_frontmatter(operations, raw.decode("utf-8"))
    path = root / descriptor["path"]
    return operations.Atom(path, descriptor["path"], descriptor["filename"], descriptor["atom_id"],
                           descriptor["lifecycle"], operations._role_directory(path, operations.control_root(root)),
                           frontmatter, content)


def _pin(root: Path, value: object) -> bytes:
    if not isinstance(value, Mapping) or set(value) != {"path", "digest"}:
        _fail("assessment-evidence-invalid", "Subject assessment requires a closed evidence pin")
    relative, digest = value["path"], value["digest"]
    if (not isinstance(relative, str) or not relative or Path(relative).is_absolute() or ".." in Path(relative).parts
            or Path(relative).as_posix() != relative or not isinstance(digest, str)):
        _fail("assessment-evidence-invalid", "Subject assessment pin is unsafe")
    try:
        raw, _ = operations.read_raw_atom_revision(root, root / relative)
    except (OSError, operations.ToolError) as error:
        from lifecycle_intents import LifecycleError
        raise LifecycleError("assessment-evidence-invalid", "Subject assessment pin cannot be safely read") from error
    if hashlib.sha256(raw).hexdigest() != digest:
        _fail("assessment-evidence-invalid", "Subject assessment pin is stale")
    return raw


def _assessment(root: Path, request: Mapping[str, Any], target: operations.Atom,
                prepared: Mapping[str, Any]) -> dict[str, Any]:
    from lifecycle_intents import _assessment_json, _mechanical_update_evidence, _semantic_assessment_evidence
    before = prepared["subject_intent"]["target"]
    if prepared["subject_intent"]["noop"]:
        return _mechanical_update_evidence(target, before, prepared["proposed"],
                                           admitted_change_class="no-op", exact_carrier=True)
    raw = _pin(root, request.get("semantic_assessment_report"))
    _, content = operations.split_frontmatter(raw.decode("utf-8"))
    report = _assessment_json(content)
    authority = report.get("authorityPins")
    lineage = report.get("lineageEvidencePins")
    if not isinstance(authority, Mapping) or not isinstance(lineage, list):
        _fail("assessment-evidence-invalid", "Subject assessment comparison is incomplete")
    pins = [request["semantic_assessment_report"], *authority.values(), *lineage]
    for pin in pins:
        _pin(root, pin)
    evidence = _semantic_assessment_evidence(root, target, before, prepared["proposed"], request["semantic_assessment_report"])
    for pin in pins:
        _pin(root, pin)
    return evidence


def _gate(root: Path, request: Mapping[str, Any], intent: Mapping[str, Any], *,
          authorized: bool, session: object, action_run_id: object, prior: object) -> None:
    from workflow_run_support import RunExecutionSession, SelectedRunError, _canonical_digest, _proposal, _validate_common
    from selected_lifecycle_journal import _fresh_prior_receipt
    from work_journal import validate_sealed_event
    if authorized is not True or not isinstance(session, RunExecutionSession) or Path(session.tracker.root).resolve() != root:
        _fail("subject-session-required", "Subject publication requires the actual selected execution Session")
    try:
        sealed = _validate_common(session.request)
        if sealed["mode"] != "execute" or sealed["operation_route"] != "update_atom" or sealed["parameters"] != request:
            _fail("subject-request-mismatch", "Subject publication differs from the sealed selected request")
        before, archive = intent["target"], intent["predecessorArchive"]
        frontier = [before["path"]]
        effects = []
        if not intent["noop"]:
            frontier.append(archive["path"])
            effects = [{"type": "subjectUpdate", "path": before["path"], "atom_id": before["atom_id"],
                        "before_version": before["version"], "version": before["version"] + 1,
                        "subject_intent_sha256": request["subject_intent_sha256"]},
                       {"type": "predecessorArchive", **archive}]
        if sealed["target_frontier"] != frontier or sealed["effects"] != effects:
            _fail("subject-frontier-mismatch", "Subject frontier and effects differ from the exact intent")
        observation = session.tracker._observe(sealed)
        if observation["selected"] is not True or observation["current"] is not True:
            _fail("subject-source-stale", "Selected Subject sources or permission are not current")
        proposal = _proposal(sealed, observation)
        session.tracker._validate_execute(sealed, proposal, _canonical_digest(proposal))
        if not isinstance(action_run_id, str):
            _fail("subject-action-start-required", "Subject publication requires the actual O030 Action Run")
        requested_id, actual = session._actual_by_id(action_run_id)
        if (actual.get("kind") != "action" or actual.get("definition", {}).get("atom_id") != "CA-O-030"
                or requested_id in session.terminal or requested_id in session.interrupted
                or requested_id in session.observed_effects or session.pending):
            _fail("subject-action-start-invalid", "Subject Action is not a fresh effect-free O030 start")
        session.read_recorded_action_start(action_run_id)
        for binding in session.workflow_definition_bindings:
            _pin(root, {"path": binding["path"], "digest": binding["digest"]})
        if not isinstance(prior, Mapping) or set(prior) != {"state", "event", "receipt"} or prior["state"] != "admitted":
            _fail("subject-prior-required", "Subject publication requires the admitted canonical lifecycle prior")
        event = validate_sealed_event(prior["event"])
        expected = {"state": "present", "filename": before["filename"], "version": before["version"],
                    "path": before["path"], "sha256": before["digest"]}
        if event["result"] != expected or prior["receipt"] != _fresh_prior_receipt(root, event):
            _fail("subject-prior-stale", "Subject lifecycle prior differs from the exact current target")
    except (SelectedRunError, OSError, RuntimeError, KeyError, TypeError) as error:
        from lifecycle_intents import LifecycleError
        if isinstance(error, LifecycleError):
            raise
        raise LifecycleError("subject-execution-unadmitted", "Subject selected execution evidence cannot be revalidated") from error


def subject_update_action(root: Path, parameters: Mapping[str, Any], *, execute: bool = False,
                          authorized: bool = False, assessment: Mapping[str, Any] | None = None,
                          session: object | None = None, action_run_id: str | None = None,
                          prior: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Preview or publish one identity-preserving, exactly sealed Subject intent."""

    from atom_subject_patch import materialize_subject_intent
    from lifecycle_intents import LifecycleError, _validate_update_assessment
    root = Path(root).resolve()
    request = _parameters(parameters)
    try:
        prepared = _prepare(root, request)
        intent = prepared["subject_intent"]
        before = intent["target"]
        path = root / before["path"]
        raw, fingerprint = operations.read_raw_atom_revision(root, path)
        if hashlib.sha256(raw).hexdigest() != before["digest"]:
            _fail("subject-source-changed", "Subject target differs from its exact intent")
        target = _atom(root, before, raw)
        base = {"operation": "update", "observed": before,
                "subject_intent": intent, "subject_intent_sha256": prepared["subject_intent_sha256"],
                "effects": [{"state": "unchanged", "carrier": before}], "history": {"prior": before}}
        try:
            evidence = _assessment(root, request, target, prepared)
        except (LifecycleError, operations.ToolError, UnicodeError) as error:
            return {**base, "outcome": "unresolved", "classification": {
                "requested": "semantic_revision", "reason": "semantic-assessment-unverified",
                "diagnostic": getattr(error, "code", "assessment-evidence-invalid")}}
        base["assessment_evidence"] = evidence
        admitted = evidence["admitted_change_class"]
        if not intent["noop"] and admitted != "semantic_revision":
            return {**base, "outcome": "replace_handoff" if admitted == "replacement" else "unresolved",
                    "classification": {"requested": "semantic_revision", "admitted": admitted,
                                       "reason": "semantic-assessment-class-mismatch"}}
        if assessment is not None:
            _validate_update_assessment(request, assessment, evidence)
            base["assessment"] = dict(assessment)
        if intent["noop"]:
            materialized = materialize_subject_intent(root, prepared, before["updated_at"])
            return {**base, "outcome": "no-op", "materialization": materialized["materialization"]}
        if execute is not True:
            return {**base, "outcome": "preview"}
        if assessment is None:
            _fail("assessment-invalid", "Subject execution requires completed O145 assessment")
        _gate(root, request, intent, authorized=authorized, session=session, action_run_id=action_run_id, prior=prior)
        actual_at = current_timestamp(root)
        materialized = materialize_subject_intent(root, prepared, actual_at)
        archive = intent["predecessorArchive"]
        archive_path = root / archive["path"]
        after_raw = materialized["carrier_bytes"]
        after = {**before, "version": materialized["materialization"]["version"],
                 "updated_at": materialized["materialization"]["updated_at"],
                 "digest": materialized["materialization"]["after_sha256"]}
        archived = {**before, "path": archive["path"], "filename": archive_path.name, "lifecycle": "archived"}
        # Final admission is repeated after materialization, not delegated to the caller.
        fresh = _prepare(root, request)
        fresh_evidence = _assessment(root, request, target, fresh)
        _validate_update_assessment(request, assessment, fresh_evidence)
        _gate(root, request, intent, authorized=authorized, session=session, action_run_id=action_run_id, prior=prior)
        current_raw, current_fingerprint = operations.read_raw_atom_revision(root, path)
        if current_raw != raw or current_fingerprint != fingerprint:
            _fail("subject-source-changed", "Subject target changed immediately before publication")
        archive_owner = current_owner = None
        phase = "archive"
        try:
            archive_owner = operations.write_raw_atom_revision(root, archive_path, raw, expected=None, mode=fingerprint[-1])
            archived_raw, archive_readback = operations.read_raw_atom_revision(root, archive_path)
            if archived_raw != raw or archive_readback != archive_owner:
                _fail("subject-history-unconfirmed", "Subject predecessor history readback differs")
            phase = "current"
            current_owner = operations.write_raw_atom_revision(root, path, after_raw, expected=fingerprint, mode=fingerprint[-1])
            phase = "readback"
            actual_raw, actual_fingerprint = operations.read_raw_atom_revision(root, path)
            if actual_raw != after_raw or actual_fingerprint != current_owner:
                _fail("subject-publication-unconfirmed", "Subject current revision readback differs")
            return {**base, "outcome": "applied", "observed": after,
                    "materialization": materialized["materialization"],
                    "effects": [{"state": "changed", "carrier": after}, {"state": "changed", "carrier": archived}],
                    "history": {"prior": before, "revision_class": "semantic_revision", "prior_revision": archived}}
        except Exception as error:
            published = getattr(error, "details", {}).get("publication_fingerprint")
            if phase == "archive" and published is not None:
                archive_owner = tuple(published)
            elif phase == "current" and published is not None:
                current_owner = tuple(published)
            recovery_error = None
            try:
                now_raw, now_fingerprint = operations.read_raw_atom_revision(root, path)
                if current_owner is not None:
                    if now_raw != after_raw or now_fingerprint != current_owner:
                        _fail("subject-rollback-uncertain", "Current revision is no longer owned by this attempt")
                    operations.write_raw_atom_revision(root, path, raw, expected=current_owner, mode=fingerprint[-1])
                elif now_raw != raw or now_fingerprint != fingerprint:
                    _fail("subject-rollback-uncertain", "Current revision changed without confirmed attempt ownership")
                restored, restored_fingerprint = operations.read_raw_atom_revision(root, path)
                if restored != raw or restored_fingerprint[-1] != fingerprint[-1]:
                    _fail("subject-rollback-uncertain", "Exact prior bytes and mode could not be confirmed")
                if archive_owner is not None:
                    operations.write_raw_atom_revision(root, archive_path, None, expected=archive_owner, mode=fingerprint[-1])
                elif phase == "archive" and getattr(error, "code", None) != "subject-destination-stale":
                    try:
                        operations.read_raw_atom_revision(root, archive_path)
                    except FileNotFoundError:
                        pass
                    else:
                        _fail("subject-rollback-uncertain", "History exists without confirmed attempt ownership")
            except Exception as recovery:
                recovery_error = recovery
            failure = {"code": "subject-rollback-uncertain" if recovery_error else "subject-publication-failed",
                       "original": {"type": type(error).__name__, "code": getattr(error, "code", None), "phase": phase}}
            if recovery_error is None:
                return {**base, "outcome": "failed", "failure": failure}
            failure["recovery"] = {"type": type(recovery_error).__name__, "code": getattr(recovery_error, "code", None)}
            return {**base, "outcome": "partial", "failure": failure,
                    "effects": [{"state": "unknown", "carrier": after}, {"state": "unknown", "carrier": archived}],
                    "history": {"prior": before, "prior_revision": archived},
                    "recovery": {"before": before, "current": after, "prior_revision": archived, "automatic_retry": False},
                    "unknown_remainder": [path.relative_to(root).as_posix(), archive["path"]]}
    except operations.ToolError as error:
        raise LifecycleError(error.code, error.message) from error
    except OSError as error:
        raise LifecycleError("subject-source-unavailable", "Subject source cannot be safely revalidated") from error
