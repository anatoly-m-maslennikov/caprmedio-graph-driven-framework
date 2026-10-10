"""Observed, recoverable selector-first full-Framework and local ca promotion.

A durable private intent precedes exposure. Selector and Skill are separate
effects: a partial publication stays pending and only the exact intent resumes.
No hooks, configuration, Docker command, rollback or image removal is performed.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import tempfile
import tomllib
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Literal

from release_contract import PROJECT_SKILL_TARGET, REQUIRED_ENGINE_SOURCE_PREFIXES, VERSION_TOML_RELATIVE, ReleaseContractError, ValidatedCandidate, canonical_json
from release_handoff import (
    CANONICAL_SOURCE_RELATIVE, CURRENT_SELECTOR_RELATIVE, PackageRow, SealedCandidateCompilation,
    _file, build_validated_candidate, tree_sha256,
)
from release_image import (
    IMAGE_ID, ImageBuildEvidence, ImageVerificationEvidence,
    read_image_execution_artifacts, verify_bound_image_evidence,
)
from release_e2e_gate import CandidateE2EGateEvidence
from release_full_gate import FullGateEvidence, verify_bound_full_gate_evidence
from release_inventory import persistent_regular_files, refuse_secret_path
from selector_publication_lock import selector_publication_lock
from release_packaging import RUNTIME_ROOT, _read_row, _render_manifest, _verify_release
from release_suite import (
    SuiteGateEvidence, _bootstrap_prior_manifest_is_exact,
    _bootstrap_source_context_is_valid, _safe_path,
)


PROMOTION_ROOT = ".caprmedio_runtime/release_promotion"
INTENT_SCHEMA = "caprmedio.release_version.pending_promotion.v1"


def bind_selected_native_n_from_checkpoint(project_root):
    """Reopen N through its exact original selected or direct publication.

    This is a read-only bootstrap, not a candidate or permission supplied by
    Release parameters.  The current D604 command addresses its original Run;
    no newest-result search or inferred Full Gate carrier is admitted.
    """

    import tomllib
    from framework_package import verify_framework_package
    from installed_mcp_binding import _RUNTIME_SELECTOR_KEYS
    from native_selected_installation import _PROOF_KEYS, _read as _read_native_carrier
    from release_checkpoint import read_native_checkpoint_packet
    from release_handoff import bind_native_installed_n
    from selected_installation_command import read_selected_installation_command_receipt, reopen_selected_installation_command_start

    root = Path(project_root).resolve(strict=True)
    selector_path = root / ".caprmedio_runtime/installation/current.toml"
    if not selector_path.exists() and not selector_path.is_symlink():
        return None
    try:
        from selected_execution import SelectedExecution

        def retained_bytes(relative):
            return _read_native_carrier(root / relative, code="release-native-n-carrier-invalid", mode=None)

        selector = tomllib.loads(retained_bytes(".caprmedio_runtime/installation/current.toml").decode("utf-8"))
        generation = selector.get("state_generation")
        if (set(selector) != _RUNTIME_SELECTOR_KEYS or type(selector.get("schema_version")) is not int
                or selector["schema_version"] != 1 or type(generation) is not int or generation < 1):
            raise ValueError("current native selector is not closed")
        package_sha = selector["package_manifest_sha256"]
        context_sha = selector["target_project_context_sha256"]
        if any(not isinstance(item, str) or re.fullmatch(r"[0-9a-f]{64}", item) is None for item in (package_sha, context_sha)):
            raise ValueError("native package or context digest is invalid")
        proof = tomllib.loads(retained_bytes(f".caprmedio_runtime/installation/generations/{generation}/release-proof.toml").decode("utf-8"))
        if set(proof) != _PROOF_KEYS or type(proof.get("schema_version")) is not int or proof["schema_version"] != 2:
            raise ValueError("current native proof is not closed")
        command_sha = proof["installation_command_sha256"]
        if not isinstance(command_sha, str) or re.fullmatch(r"[0-9a-f]{64}", command_sha) is None:
            raise ValueError("current native command digest is invalid")
        command_bytes = retained_bytes(f".caprmedio_runtime/installation/commands/{command_sha}.json")
        command_document = json.loads(command_bytes)
        if isinstance(command_document, dict) and command_document.get("operation") == "install_framework_runtime":
            from framework_installation_command import read_framework_installation_command_receipt, reopen_framework_installation_command_start
            from installed_mcp_binding import _context
            from release_checkpoint import read_direct_native_result_packet, read_direct_native_result_effects

            command = read_framework_installation_command_receipt(command_bytes, expected_sha256=command_sha)
            package = verify_framework_package(root / ".caprmedio_install/releases" / package_sha)
            target_context = _context(root, context_sha)
            if (command.package_manifest_sha256 != package_sha or command.target_project_context_sha256 != context_sha
                    or command.full_gate_receipt_sha256 != proof["full_gate_receipt_sha256"]):
                raise ValueError("direct command differs from current native proof")
            started = reopen_framework_installation_command_start(root, command, action_package=package,
                operators_registry_ref=f"{target_context.control_child_relpath}/operators_registry.toml")
            action_run_id = started["run"]["run_id"]
            if not isinstance(action_run_id, str) or not action_run_id or "/" in action_run_id or "\\" in action_run_id:
                raise ValueError("actual direct Action identity is not one safe path component")
            result_ref = f".caprmedio_tmp/installation/results/{action_run_id}/result.json"
            raw_result = retained_bytes(result_ref)
            effects = read_direct_native_result_effects(raw_result, command=command, action_run_id=action_run_id, state_generation=generation)
            _reopen_completed_direct_native_result(root, started, result_ref, effects)
            packet = read_direct_native_result_packet(raw_result, project_root=str(root), command=command,
                action_run_id=action_run_id, state_generation=generation)
            binding = bind_native_installed_n(root, package, packet, target_context_sha256=context_sha)
            if binding.selected.state_generation != generation or binding.selected.full_gate_receipt_sha256 != command.full_gate_receipt_sha256:
                raise ValueError("direct original packet differs from current native generation")
            return binding
        command = read_selected_installation_command_receipt(
            command_bytes,
            expected_sha256=command_sha,
        )
        reopen_selected_installation_command_start(root, command)
        workflow_run_id = command.parent_lineage[-1]
        store = SelectedExecution(root)
        folder = store.run_directory(workflow_run_id)
        frozen = json.loads(retained_bytes((folder / "selected_request.json").relative_to(root)))
        request = frozen["request"]
        execution = request["execution"]
        if request["run_id"] != workflow_run_id or frozen["graph"]["route"] != "release_version":
            raise ValueError("original selected Run identity differs")
        checkpoint = json.loads(retained_bytes((folder / "release_action_run.json").relative_to(root)))
        packet, publication = read_native_checkpoint_packet(
            checkpoint, project_root=str(root), expected_request=execution["parameters"], expected_workflow_run_id=workflow_run_id,
        )
        if (publication.installation_command_sha256 != command_sha
                or publication.action_run_id != command.command_id
                or publication.package_manifest_sha256 != package_sha
                or publication.target_project_context_sha256 != context_sha):
            raise ValueError("original selected publication differs from current native command")
        package = verify_framework_package(root / ".caprmedio_install/releases" / package_sha)
        binding = bind_native_installed_n(root, package, packet, target_context_sha256=context_sha)
        if (binding.selected.full_gate_receipt_sha256 != command.full_gate_receipt_sha256
                or binding.selected.state_generation != generation):
            raise ValueError("original packet differs from current native generation")
        return binding
    except (KeyError, TypeError, ValueError, OSError, RuntimeError) as error:
        if getattr(error, "code", None) == "release-native-n-direct-packet-association-unavailable":
            raise
        raise ReleaseContractError("release-native-n-checkpoint-unavailable", "current native N requires its exact retained original publication packet") from error


def _reopen_completed_direct_native_result(root: Path, started, result_ref: str, effects) -> None:
    """Require original canonical O200 completion for subsequent N discovery.

    Final self-validation during publication intentionally does not call this
    reader: the publisher has its actual packet but has not terminalized yet.
    """

    import work_journal
    from FIND_AND_FETCH_JOURNAL_EVENTS.find_and_fetch_journal_events import JournalQueryError, capture_snapshot, query

    effect_refs = [effect["reference"] for effect in effects.values()] + [result_ref]
    run = started.get("run", {})
    run_id = run.get("run_id")
    if (started.get("action_id") != "CA-O-200" or started.get("event") != "started" or run.get("kind") != "action"
            or "parent_run_id" in run or run.get("definition", {}).get("atom_id") != "CA-O-200"):
        raise ReleaseContractError("release-native-n-direct-start-invalid", "direct association is not an actual unparented O200 start")
    intent_sha = started.get("llm_session", {}).get("uuid")
    terminal_sha = work_journal.canonical_json_digest({"intent_sha256": intent_sha, "outcome": "completed",
        "result_ref": result_ref, "effect_refs": effect_refs, "report_ref": None})
    terminal_id = f"{run_id}:terminal:{terminal_sha}"
    identities = (started["event_id"], terminal_id)
    try:
        snapshot = capture_snapshot(root)
        if snapshot.get("source_root") != work_journal.configured_journal_root(root).as_posix():
            raise ReleaseContractError("release-native-n-direct-terminal-unavailable", "direct canonical Journal root differs")
        observed = query(snapshot, {"mode": "full_events", "filter": '"event:/run/run_id" = '
            + json.dumps(run_id), "limit": 3})
    except JournalQueryError as error:
        raise ReleaseContractError("release-native-n-direct-terminal-unavailable", "direct canonical Journal coverage is unavailable or ambiguous") from error
    if (observed.get("status") != "complete" or observed.get("coverage", {}).get("complete") is not True
            or len(observed.get("results", [])) != 2):
        raise ReleaseContractError("release-native-n-direct-terminal-unavailable", "direct canonical start/completion coverage is absent or ambiguous")
    events = {}
    for row in observed["results"]:
        event = work_journal.validate_sealed_event(row["event"])
        if event["event_id"] not in identities or event["event_id"] in events:
            raise ReleaseContractError("release-native-n-direct-terminal-unavailable", "direct canonical Action events are ambiguous")
        events[event["event_id"]] = event
    terminal = events[terminal_id]
    preserved = ("schema_version", "kind", "action_id", "author", "llm_session", "structural_scope",
                 "initiative", "run", "definition_bindings", "input_ref", "redaction")
    if (events[started["event_id"]] != dict(started) or any(terminal.get(key) != started.get(key) for key in preserved)
            or terminal.get("event") != "completed" or terminal.get("outcome") != "completed"
            or terminal.get("result_ref") != result_ref or terminal.get("effect_refs") != effect_refs
            or terminal.get("report_ref") is not None):
        raise ReleaseContractError("release-native-n-direct-terminal-unavailable", "direct completion differs from the actual original result and start")


def admit_selected_native_promotion_start(run, context):
    """Reopen the actual selected O169 occurrence and its sealed input binding.

    This consumes the shared Session injected by the selected provider.  It
    creates no Run, Journal record or O200 command and accepts no permission
    assertion from Release parameters.
    """

    from release_actions import ReleaseActionRun, SelectedReleaseActionContext, _fingerprint
    from workflow_run_support import RunExecutionSession, SelectedRunError

    if type(run) is not ReleaseActionRun or type(context) is not SelectedReleaseActionContext:
        raise ReleaseContractError("release-native-promotion-context-untrusted", "selected publication requires the retained Run and context")
    session = run.selected_action_session
    if type(session) is not RunExecutionSession:
        raise ReleaseContractError("release-native-promotion-session-unavailable", "selected publication requires the actual shared Session")
    if (context.workflow_atom_id != "CA-O-164" or context.workflow_version != 9
            or context.action_atom_id != "CA-O-169" or context.step_atom_id not in {"CA-O-178", "CA-O-179"}
            or context.project_root != run.project_root or context.workflow_run_id != run.workflow_run_id
            or context.parent_workflow_run_id != run.workflow_run_id
            or context.parent_step_run_id != context.step_run_id
            or context.frozen_parameters_sha256 != run.frozen_parameters_sha256
            or str(Path(session.tracker.root).resolve(strict=True)) != run.project_root
            or session.request.get("mode") != "execute" or session.request.get("operation_route") != "release_version"):
        raise ReleaseContractError("release-native-promotion-context-mismatch", "selected native publication differs from its retained Workflow occurrence")
    try:
        selected_request = type(run.request).model_validate(session.request.get("parameters"))
    except (TypeError, ValueError) as error:
        raise ReleaseContractError("release-native-promotion-input-mismatch", "shared Session has no exact Release input") from error
    if _fingerprint(selected_request) != run.frozen_parameters_sha256:
        raise ReleaseContractError("release-native-promotion-input-mismatch", "shared Session Release input differs from the frozen candidate")
    actual = {record.get("run_id"): (requested, record) for requested, record in session.actual.items()}
    action_pair = actual.get(context.action_run_id)
    step_pair = actual.get(context.step_run_id)
    workflow_pair = actual.get(context.workflow_run_id)
    if action_pair is None or step_pair is None or workflow_pair is None:
        raise ReleaseContractError("release-native-promotion-start-missing", "selected publication has no actual parent Run lineage")
    action_id, action = action_pair
    _, step = step_pair
    _, workflow = workflow_pair
    if (action.get("kind") != "action" or step.get("kind") != "step" or workflow.get("kind") != "workflow"
            or action.get("parent_run_id") != context.step_run_id
            or step.get("parent_run_id") != context.workflow_run_id
            or action.get("definition", {}).get("atom_id") != "CA-O-169"
            or action.get("definition", {}).get("version") != 5
            or step.get("definition", {}).get("atom_id") != context.step_atom_id
            or workflow.get("definition", {}).get("atom_id") != "CA-O-164"
            or workflow.get("definition", {}).get("version") != 9
            or action_id in session.terminal or action_id in session.interrupted):
        raise ReleaseContractError("release-native-promotion-start-mismatch", "selected publication Action is not the exact running O169 occurrence")
    try:
        provenance = session.read_recorded_action_start(context.action_run_id)
        # The authorization is already sealed by the shared admission.  Reopen
        # its exact route/input/source relationships instead of interpreting a
        # caller Boolean or the existence of a context as permission.
        session.tracker._validate_execute(
            session.request, session.request["proposal_receipt"], session.request["proposal_receipt_digest"],
        )
    except (KeyError, TypeError, ValueError, SelectedRunError) as error:
        raise ReleaseContractError("release-native-promotion-start-untrusted", "canonical selected start or sealed authorization cannot be reopened") from error
    if provenance.parent_lineage != (context.step_run_id, context.workflow_run_id):
        raise ReleaseContractError("release-native-promotion-start-mismatch", "canonical selected start has another parent lineage")
    root = Path(run.project_root)
    for record in (workflow, step, action):
        definition = record["definition"]
        source = _file(root, definition.get("path"))
        if _digest(source.read_bytes()) != definition.get("digest"):
            raise ReleaseContractError("release-native-promotion-source-stale", "selected native publication source definition changed")
    return provenance


@dataclass(frozen=True)
class PromotionEvidence:
    candidate_snapshot_manifest_sha256: str
    outcome: Literal["promoted", "pending", "recording_uncertain"]
    reason: str
    candidate_image_digest: str
    prior_image_digest: str | None
    prior_release: str
    selected_release_root: str
    framework_engine_root: str
    methodology_root: str
    skill_target: str
    intent_sha256: str
    evidence_root: str
    retained_prior_selector_ref: str
    retained_prior_skill_ref: str | None
    receipt_sha256: str | None = None
    framework_version: str = ""
    version_toml_sha256: str = ""


@dataclass(frozen=True)
class NativePromotionEvidence:
    """Observed selected O169 publication, separate from legacy promotion.

    Nullable final identities preserve an unavailable/partial cut-over without
    inventing completion.  This private result never substitutes for the
    shared Action's canonical terminal Journal receipt.
    """

    candidate_snapshot_manifest_sha256: str
    outcome: Literal["promoted", "pending", "effect_uncertain", "recording_uncertain"]
    reason: str
    candidate_image_digest: str
    prior_image_digest: str | None
    prior_release: str
    package_manifest_sha256: str
    full_gate_receipt_sha256: str
    framework_version: str
    version_toml_sha256: str
    action_run_id: str
    action_start_event_id: str
    installation_command_sha256: str
    target_project_context_sha256: str
    state_generation: int
    evidence_root: str
    retained_prior_selector_ref: str
    package_selector_sha256: str | None = None
    runtime_selector_sha256: str | None = None
    release_proof_sha256: str | None = None
    effect_refs: tuple[str, ...] = ()
    receipt_sha256: str | None = None


def _open_retained_native_promotion_packet(candidate, suite, build, verification, e2e, full_gate, prepared_package):
    """Reopen the immutable native packet inputs without currentness admission."""

    from release_full_gate import NativeFullGateEvidence
    from release_retained_candidate import encode_retained_candidate_descriptor, read_retained_candidate_identity
    from retained_full_gate_packet import RetainedNativeFullGatePacket

    if not isinstance(full_gate, NativeFullGateEvidence):
        raise ReleaseContractError("release-native-promotion-gate-untrusted", "selected native publication requires its original native Full Gate")
    root = Path(candidate.project_root)
    sidecar = _file(root, full_gate.package_evidence_relpath)
    descriptor = sidecar.parent.parent / "candidate-snapshot.json"
    retained = read_retained_candidate_identity(
        descriptor, expected_sha256=_digest(encode_retained_candidate_descriptor(candidate.manifest)),
        package_root=prepared_package.private_package_root,
        sidecar_path=sidecar, expected_sidecar_sha256=full_gate.package_evidence_sha256,
    )
    return RetainedNativeFullGatePacket(root, retained, suite, build, verification, e2e, full_gate)


def retained_native_promotion_packet(candidate, compilation, suite, build, verification, e2e, full_gate, prepared_package):
    """Freshly validate a native packet before the selected-N cut-over."""

    packet = _open_retained_native_promotion_packet(
        candidate, suite, build, verification, e2e, full_gate, prepared_package,
    )
    verify_bound_full_gate_evidence(
        candidate, compilation, suite, build, verification, e2e, full_gate,
        retained_package=packet.retained_candidate.package_evidence,
    )
    return packet


def _reopen_historical_native_promotion_packet(candidate, suite, build, verification, e2e, full_gate, prepared_package):
    """Reopen a recorded final native packet after predecessor removal.

    Final disposition and recovery happen after the successful selected-N
    cut-over has removed the old N package.  They must use the immutable D597
    descriptor/package sidecar and detached receipt reader, rather than
    weakening the fresh admission reader used before that cut-over.
    """

    from release_full_gate import verify_detached_native_full_gate_evidence

    packet = _open_retained_native_promotion_packet(
        candidate, suite, build, verification, e2e, full_gate, prepared_package,
    )
    verify_detached_native_full_gate_evidence(
        packet.artifact_root, packet.retained_candidate, packet.suite, packet.build,
        packet.verification, packet.e2e, packet.evidence,
    )
    return packet


def prepare_and_publish_selected_native_runtime(run, context):
    """Compose the shared native preparation under the real selected Action.

    The launch data describes this executing host only and remains inert.
    Runtime preparation may have partial effects; its lock remains uncertain
    if it fails, and this occurrence is never implicitly retried.
    """

    import stat
    from framework_installation import PortableInstallationRequest
    from framework_package import provide_installation_package_evidence, verify_current_package_selector
    from installation_context import TargetProjectRequest, bind_target_project_context
    from installation_transaction import installation_publication_lock
    from portable_runtime_materialization import CandidateRuntimeCommandStageRequest
    from portable_methodology_installation import prepare_candidate_portable_methodology_publication
    from portable_runtime_publication import (
        build_prepared_native_publication,
        render_package_selector,
        retained_publication_failure_reason,
    )
    from selected_installation_command import retain_selected_installation_command
    import work_journal

    admit_selected_native_promotion_start(run, context)
    from release_suite import _active_n_state

    active_n = _active_n_state(Path(run.project_root), run.candidate)
    if active_n != (run.portable_suite.executing_selector_sha256,
                    run.portable_suite.executing_release_package_sha256,
                    run.portable_suite.executing_skill_sha256):
        raise ReleaseContractError("release-native-promotion-prior-stale", "selected N package, execution or complete local ca Skill changed after the original Unit gate")
    packet = retained_native_promotion_packet(
        run.candidate, run.portable_compilation, run.portable_suite, run.build, run.verification,
        run.e2e, run.full_gate, run.prepared_portable_package,
    )
    root = Path(run.project_root)
    package = run.prepared_portable_package.package
    settings_path = work_journal.resolve_settings_path(root)
    settings = tomllib.loads(_file(root, settings_path.relative_to(root).as_posix()).read_text(encoding="utf-8"))
    control = settings_path.parent.relative_to(root).as_posix()
    prior_binding = run.candidate.native_installed_n
    prior_context = None
    if prior_binding is not None:
        from release_handoff import reopen_native_installed_n

        prior_binding = reopen_native_installed_n(root, prior_binding)
        context_sha = prior_binding.selected.target_project_context_sha256
        prior_context = tomllib.loads(_file(root, f".caprmedio_runtime/installation/contexts/{context_sha}.toml").read_text(encoding="utf-8"))
    target = TargetProjectRequest(
        target_root=root, control_child=control, mode="adopt", target_project_identity=settings["project"]["name"],
        settings_path=settings_path, project_structure_path=root / control / "project_structure.toml",
        operators_registry_path=root / control / "operators_registry.toml",
        repository_identity=False if prior_context is None else prior_context["repository_identity"],
        root_locator=root.name if prior_context is None else prior_context["root_locator"],
        package_root=package.root, package_evidence=provide_installation_package_evidence(package.root),
    )
    target_context = bind_target_project_context(target)
    installation = PortableInstallationRequest(
        target=target, retained_gate_receipt_path=root / packet.evidence.evidence_root / "receipt.json", full_gate_packet=packet,
    )
    package_selector = render_package_selector(
        package, full_gate_receipt_sha256=packet.evidence.receipt_sha256,
        image_digest=packet.evidence.candidate_image_digest.removeprefix("sha256:"),
    )
    methodology = prepare_candidate_portable_methodology_publication(
        installation, package=package, target_context=target_context,
        prospective_selector=verify_current_package_selector(package_selector, package),
    )
    uv = shutil.which("uv")
    if uv is None:
        raise ReleaseContractError("release-native-launcher-unavailable", "selected native launch requires actual UV")
    uv_path = Path(uv).resolve(strict=True)
    uv_stat = uv_path.lstat()
    if (uv_path.is_symlink() or not stat.S_ISREG(uv_stat.st_mode) or not uv_stat.st_mode & 0o111
            or any(path.is_symlink() for path in (uv_path.parent, *uv_path.parent.parents))):
        raise ReleaseContractError("release-native-launcher-unavailable", "actual UV executable or parent is unsafe")
    home = Path.home().absolute()
    old_package_selector = _file(root, ".caprmedio_install/current.toml").read_bytes()
    native_selector = root / ".caprmedio_runtime/installation/current.toml"
    if native_selector.exists() or native_selector.is_symlink():
        prior_path = Path(".caprmedio_runtime/installation/current.toml")
        prior_selector = _file(root, prior_path.as_posix()).read_bytes()
        old_generation = tomllib.loads(prior_selector.decode("utf-8"))["state_generation"]
        if type(old_generation) is not int or old_generation < 1:
            raise ReleaseContractError("release-native-generation-invalid", "prior native generation is not positive")
        generation = old_generation + 1
    else:
        prior_path = Path(".caprmedio_runtime/framework/current.toml")
        prior_selector = _file(root, prior_path.as_posix()).read_bytes()
        generation = 1
    command = retain_selected_installation_command(
        run, context, target=target, target_context=target_context, package=package, full_gate_packet=packet,
    )
    stage = CandidateRuntimeCommandStageRequest(
        package=package, target_context=target_context, prospective_package_selector=package_selector,
        full_gate_packet=packet, state_generation=generation,
        entrypoint="102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/implementation_server.py",
        fixed_arguments=("--project-root", "../../..", "--control-root", control),
        invocation_nonce=_digest(context.action_run_id.encode("utf-8")), path_directories=(uv_path.parent,), home=home,
    )
    with installation_publication_lock(
        root, target_context_sha256=target_context.sha256, owner_run_id=context.action_run_id,
        operation="promote_selected_runtime", command_sha256=command.receipt.sha256,
    ) as lock:
        try:
            admit_selected_native_promotion_start(run, context)
            if _active_n_state(root, run.candidate) != active_n:
                raise ReleaseContractError("release-native-promotion-prior-stale", "selected prior N changed before lock-owned preparation")
            prepared = build_prepared_native_publication(
                installation, package=package, target_context=target_context,
                installation_command_sha256=command.receipt.sha256, full_gate_packet=packet,
                runtime_stage_request=stage, methodology_preparation=methodology, state_generation=generation,
                old_package_selector=old_package_selector, old_execution_selector=(prior_path, prior_selector), lock=lock,
            )
            evidence = publish_selected_native_runtime(run, context, command, prepared, lock=lock)
        except (KeyboardInterrupt, InterruptedError, SystemExit, OSError, ValueError, RuntimeError) as error:
            refs = [command.receipt_path.relative_to(root).as_posix(), lock.lock_path.relative_to(root).as_posix()]
            for path in (
                f".caprmedio_runtime/installation/contexts/{target_context.sha256}.toml", ".caprmedio_runtime/config.toml",
                f".caprmedio_tmp/installation/staging/{lock.lock_generation}/stage-manifest.toml",
                f".caprmedio_tmp/installation/proofs/{lock.lock_generation}/release-proof.toml",
            ):
                try:
                    _file(root, path)
                except (OSError, ReleaseContractError):
                    continue
                refs.append(path)
            return (
                "effect_uncertain",
                "native preparation/publication stopped: "
                f"{retained_publication_failure_reason(error)}; exact partial carriers retained, no replay",
                tuple(refs),
                None,
            )
        if evidence.outcome == "promoted" and evidence.receipt_sha256 is not None:
            lock.release("completed")
        return ("completed" if evidence.outcome == "promoted" and evidence.receipt_sha256 else "pending",
                evidence.reason, (f"{evidence.evidence_root}/receipt.json",) if evidence.receipt_sha256 else evidence.effect_refs,
                evidence)


def verify_native_promotion_evidence(candidate, compilation, suite, build, verification,
                                     evidence: NativePromotionEvidence, *, e2e, full_gate,
                                     prepared_package) -> Path:
    """Reopen exact native promotion and original gate before image disposition."""

    from framework_package import verify_framework_package
    from native_selected_installation import reopen_current_native_installation
    from selected_installation_command import read_selected_installation_command_receipt, reopen_selected_installation_command_start

    if (type(evidence) is not NativePromotionEvidence or evidence.outcome != "promoted"
            or not evidence.receipt_sha256 or type(evidence.state_generation) is not int or evidence.state_generation <= 0):
        raise ReleaseContractError("release-native-promotion-evidence-untrusted", "native disposition requires recorded observed publication")
    packet = _reopen_historical_native_promotion_packet(
        candidate, suite, build, verification, e2e, full_gate, prepared_package,
    )
    root = Path(candidate.project_root)
    prefix = f"{PROMOTION_ROOT}/{candidate.manifest.sha256}/observations/attempt-"
    if (not evidence.evidence_root.startswith(prefix) or "/" in evidence.evidence_root.removeprefix(prefix)
            or evidence.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
            or evidence.framework_version != candidate.manifest.framework_version
            or evidence.version_toml_sha256 != candidate.manifest.version_toml_sha256
            or evidence.package_manifest_sha256 != full_gate.package_manifest_sha256
            or evidence.full_gate_receipt_sha256 != full_gate.receipt_sha256
            or evidence.candidate_image_digest != full_gate.candidate_image_digest
            or evidence.prior_release != candidate.authority.executing_release
            or evidence.retained_prior_selector_ref != f"{PROMOTION_ROOT}/{candidate.manifest.sha256}/prior-selector.toml"):
        raise ReleaseContractError("release-native-promotion-evidence-untrusted", "native publication differs from the exact frozen frontier")
    receipt = _file(root, f"{evidence.evidence_root}/receipt.json").read_bytes()
    if (_digest(receipt) != evidence.receipt_sha256
            or receipt != canonical_json(asdict(replace(evidence, receipt_sha256=None)))):
        raise ReleaseContractError("release-native-promotion-evidence-untrusted", "native publication receipt changed or is caller-forged")
    prior = _file(root, evidence.retained_prior_selector_ref).read_bytes()
    if _prior_image(prior) != evidence.prior_image_digest:
        raise ReleaseContractError("release-native-promotion-evidence-untrusted", "native prior image differs from the retained exact selector")
    package = verify_framework_package(root / ".caprmedio_install/releases" / evidence.package_manifest_sha256)
    selected = reopen_current_native_installation(
        root, package, packet, target_context_sha256=evidence.target_project_context_sha256,
    )
    _verify_native_local_ca(root, package)
    if (selected.package_manifest_sha256 != evidence.package_manifest_sha256
            or selected.full_gate_receipt_sha256 != evidence.full_gate_receipt_sha256
            or selected.framework_version != evidence.framework_version
            or selected.version_toml_sha256 != evidence.version_toml_sha256
            or selected.state_generation != evidence.state_generation
            or selected.selector_sha256 != evidence.runtime_selector_sha256
            or selected.release_proof_sha256 != evidence.release_proof_sha256
            or "sha256:" + selected.image_digest != evidence.candidate_image_digest
            or _digest(_file(root, ".caprmedio_install/current.toml").read_bytes()) != evidence.package_selector_sha256):
        raise ReleaseContractError("release-native-promotion-stale", "selected native publication changed after observation")
    command = read_selected_installation_command_receipt(
        _file(root, f".caprmedio_runtime/installation/commands/{evidence.installation_command_sha256}.json").read_bytes(),
        expected_sha256=evidence.installation_command_sha256,
    )
    event = reopen_selected_installation_command_start(root, command)
    if (command.command_id != evidence.action_run_id or event["event_id"] != evidence.action_start_event_id
            or command.prior_runtime_selector_sha256 != _digest(prior)
            or command.package_manifest_sha256 != evidence.package_manifest_sha256
            or command.full_gate_receipt_sha256 != evidence.full_gate_receipt_sha256
            or command.target_project_context_sha256 != evidence.target_project_context_sha256):
        raise ReleaseContractError("release-native-promotion-evidence-untrusted", "native publication command differs from its actual selected Action")
    return root


def _verify_native_local_ca(root, package):
    from release_suite import _active_skill_records

    expected = {row.path.removeprefix("SKILLS/ca/"): (row.sha256, row.mode)
                for row in package.inventory if row.path.startswith("SKILLS/ca/")}
    expected_directories = {parent.as_posix() for name in expected for parent in Path(name).parents if parent != Path(".")}
    files, directories = _active_skill_records(root, PROJECT_SKILL_TARGET)
    if not expected or files != expected or directories != expected_directories:
        raise ReleaseContractError("release-native-promotion-final-skill-stale", "complete project-local ca Skill differs from the exact gated package")


def publish_selected_native_runtime(run, context, command_result, prepared, *, lock) -> NativePromotionEvidence:
    """Use the actual O169 authority over the common physical native publisher.

    Preparation belongs to the shared package/context/Methodology builder.
    This wrapper neither creates O200 intent nor reconstructs a second Run.
    It retains exact partial effects and refuses an existing private intent.
    """

    from portable_runtime_publication import (
        PreparedNativePublication,
        publish_prepared_native_runtime,
        revalidate_prepared_native_predecessor,
    )
    from selected_installation_command import SelectedInstallationCommandResult, read_selected_installation_command_receipt
    from installation_transaction import InstallationPublicationLock
    from native_installation_proof import NativeInstallationProof

    provenance = admit_selected_native_promotion_start(run, context)
    if (context.step_atom_id != "CA-O-178" or type(command_result) is not SelectedInstallationCommandResult
            or type(prepared) is not PreparedNativePublication or type(lock) is not InstallationPublicationLock
            or type(prepared.candidate_proof) is not NativeInstallationProof):
        raise ReleaseContractError("release-native-promotion-preparation-untrusted", "selected publication requires its own command and common typed preparation")
    lock.revalidate()
    command = command_result.receipt
    root = Path(run.project_root)
    expected_command = root / ".caprmedio_runtime/installation/commands" / f"{command.sha256}.json"
    if (command_result.receipt_path != expected_command or command_result.action_provenance != provenance
            or command.command_id != context.action_run_id
            or command.selected_start_receipt != run.selected_action_session.read_recorded_action_start_receipt(context.action_run_id)
            or lock.project_root != root or lock.owner_run_id != context.action_run_id
            or lock.operation != "promote_selected_runtime" or lock.command_sha256 != command.sha256
            or lock.target_context_sha256 != prepared.target_context.sha256
            or command.target_project_context_sha256 != prepared.target_context.sha256
            or command.package_manifest_sha256 != prepared.package.manifest_digest
            or read_selected_installation_command_receipt(_file(root, expected_command.relative_to(root).as_posix()).read_bytes(), expected_sha256=command.sha256) != command):
        raise ReleaseContractError("release-native-promotion-command-stale", "selected publication lock, command or actual start changed")
    packet = retained_native_promotion_packet(
        run.candidate, run.portable_compilation, run.portable_suite, run.build, run.verification,
        run.e2e, run.full_gate, run.prepared_portable_package,
    )
    if (packet.evidence.receipt_sha256 != command.full_gate_receipt_sha256
            or prepared.package.manifest_digest != packet.evidence.package_manifest_sha256
            or prepared.old_execution_selector is None):
        raise ReleaseContractError("release-native-promotion-frontier-mismatch", "prepared publication differs from the original gate or frozen prior selector")
    prior_relative, prior = prepared.old_execution_selector
    if (_file(root, prior_relative.as_posix()).read_bytes() != prior
            or _digest(prior) != command.prior_runtime_selector_sha256):
        raise ReleaseContractError("release-native-promotion-prior-stale", "exact selected prior execution selector changed")
    if prior_relative == Path(".caprmedio_runtime/installation/current.toml"):
        if run.candidate.native_installed_n is None:
            raise ReleaseContractError("release-native-promotion-prior-unbound", "native prior selection was not physically frozen with the candidate")
        revalidate_prepared_native_predecessor(
            prepared,
            run.candidate.native_installed_n,
            lock=lock,
        )
    directory = root / PROMOTION_ROOT / run.candidate.manifest.sha256
    if directory.exists() or directory.is_symlink():
        raise ReleaseContractError("release-native-promotion-retry-refused", "existing native publication intent requires explicit reconciliation without replay")
    _safe_path(root, PROMOTION_ROOT, create=True)
    directory.mkdir()
    prior_ref = f"{PROMOTION_ROOT}/{run.candidate.manifest.sha256}/prior-selector.toml"
    _write(directory / "prior-selector.toml", prior, mode=0o600)
    _write(directory / "selected-command.json", command.payload, mode=0o600)
    _write(directory / "intent.json", canonical_json({
        "schema": "caprmedio.release_version.selected_native_promotion_intent.v1",
        "action_run_id": context.action_run_id, "action_start_event_id": provenance.event_id,
        "candidate_snapshot_manifest_sha256": run.candidate.manifest.sha256,
        "package_manifest_sha256": prepared.package.manifest_digest,
        "full_gate_receipt_sha256": packet.evidence.receipt_sha256,
        "installation_command_sha256": command.sha256,
        "prior_runtime_selector_sha256": _digest(prior),
    }), mode=0o600)
    _sync(directory)
    observations = directory / "observations"
    observations.mkdir()
    attempt = Path(tempfile.mkdtemp(prefix="attempt-", dir=observations))
    evidence = NativePromotionEvidence(
        candidate_snapshot_manifest_sha256=run.candidate.manifest.sha256,
        outcome="pending", reason="native publication has not completed",
        candidate_image_digest=packet.evidence.candidate_image_digest,
        prior_image_digest=_prior_image(prior), prior_release=run.candidate.authority.executing_release,
        package_manifest_sha256=prepared.package.manifest_digest,
        full_gate_receipt_sha256=packet.evidence.receipt_sha256,
        framework_version=run.candidate.manifest.framework_version,
        version_toml_sha256=run.candidate.manifest.version_toml_sha256,
        action_run_id=context.action_run_id, action_start_event_id=provenance.event_id,
        installation_command_sha256=command.sha256,
        target_project_context_sha256=prepared.target_context.sha256,
        state_generation=prepared.candidate_proof.state_generation,
        evidence_root=attempt.relative_to(root).as_posix(), retained_prior_selector_ref=prior_ref,
    )
    try:
        published = publish_prepared_native_runtime(prepared, lock=lock)
        from native_selected_installation import reopen_current_native_installation

        final_selected = reopen_current_native_installation(
            root, published.package, packet, target_context_sha256=prepared.target_context.sha256,
        )
        if (final_selected.package_manifest_sha256 != command.package_manifest_sha256
                or final_selected.full_gate_receipt_sha256 != command.full_gate_receipt_sha256
                or final_selected.state_generation != prepared.candidate_proof.state_generation
                or final_selected.selector_sha256 != published.runtime_selector_sha256):
            raise ReleaseContractError("release-native-promotion-final-stale", "final native generation differs from the same original gated selected publication")
        _verify_native_local_ca(root, published.package)
        effect_refs = (
            ".caprmedio_install/current.toml", ".caprmedio_runtime/installation/current.toml",
            published.generation_proof_path.relative_to(root).as_posix(),
        )
        evidence = replace(
            evidence, outcome="promoted", reason="same gated package and exact native execution selection published",
            package_selector_sha256=published.package_selector_sha256,
            runtime_selector_sha256=published.runtime_selector_sha256,
            release_proof_sha256=_digest(_file(root, effect_refs[2]).read_bytes()),
            effect_refs=effect_refs,
        )
    except (KeyboardInterrupt, InterruptedError, SystemExit) as error:
        evidence = replace(evidence, outcome="effect_uncertain", reason=f"native publication interrupted: {type(error).__name__}; no replay")
    except (OSError, ValueError, RuntimeError) as error:
        evidence = replace(evidence, outcome="effect_uncertain", reason=f"native publication stopped: {getattr(error, 'code', type(error).__name__)}; actual partial effects retained")
    try:
        # Preserve observed concrete carriers even when cut-over failed.  No
        # existence observation is turned into a claim of valid activation.
        observed = []
        for reference in (
            prior_ref, f"{directory.relative_to(root).as_posix()}/intent.json",
            ".caprmedio_install/current.toml", ".caprmedio_runtime/installation/current.toml",
            f".caprmedio_runtime/installation/generations/{evidence.state_generation}/release-proof.toml",
        ):
            try:
                _file(root, reference)
            except (OSError, ReleaseContractError):
                continue
            observed.append(reference)
        evidence = replace(evidence, effect_refs=tuple(observed))
        _write(attempt / "receipt.json", canonical_json(asdict(evidence)), mode=0o600)
        _sync(attempt)
        return replace(evidence, receipt_sha256=_digest((attempt / "receipt.json").read_bytes()))
    except OSError:
        return replace(evidence, outcome="recording_uncertain", reason="native publication observation recording is uncertain")


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _sync(directory: Path) -> None:
    descriptor = os.open(directory, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _write(path: Path, payload: bytes, mode: int = 0o644) -> None:
    with path.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    path.chmod(mode)


def _sync_skill(folder: Path) -> None:
    for path in folder.rglob("*"):
        if path.name != ".DS_Store" and path.is_file():
            with path.open("rb") as stream:
                os.fsync(stream.fileno())
    for path in sorted((item for item in folder.rglob("*") if item.is_dir()),
                       key=lambda item: len(item.parts), reverse=True):
        _sync(path)
    _sync(folder)


def _records(root: Path, folder: Path) -> list[dict]:
    _safe_path(root, folder.relative_to(root).as_posix())
    rows = []
    for path in persistent_regular_files(root, folder):
        rows.append({"path": path.relative_to(folder).as_posix(), "sha256": _digest(path.read_bytes()),
                     "mode": path.stat().st_mode & 0o777})
    return rows


def _skill_records(root: Path, folder: Path) -> list[dict]:
    rows = _records(root, folder)
    expected_directories = {str(parent) for row in rows for parent in Path(row["path"]).parents if str(parent) != "."}
    actual_directories = {path.relative_to(folder).as_posix() for path in folder.rglob("*") if path.is_dir()}
    if actual_directories != expected_directories:
        raise ReleaseContractError("release-promotion-skill-ownership-unknown", "Skill contains undeclared directories")
    return rows


def _inputs(candidate, compilation, suite, build, verification, e2e, full_gate) -> str:
    if (not isinstance(candidate, ValidatedCandidate) or not isinstance(compilation, SealedCandidateCompilation)
            or not isinstance(suite, SuiteGateEvidence) or not isinstance(build, ImageBuildEvidence)
            or not isinstance(verification, ImageVerificationEvidence)
            or not isinstance(e2e, CandidateE2EGateEvidence)
            or not isinstance(full_gate, FullGateEvidence)):
        raise ReleaseContractError("release-promotion-input-untrusted", "promotion requires typed internal gate evidence")
    return _digest(canonical_json({"candidate": candidate.manifest.model_dump(mode="json", by_alias=True),
          "authority": candidate.authority.model_dump(mode="json"), "intent": candidate.intent.model_dump(mode="json"),
          "compilation": compilation.model_dump(mode="json"), "suite": asdict(suite),
          "build": asdict(build), "verification": asdict(verification),
          "e2e": asdict(e2e), "full_gate": asdict(full_gate)}))


def _selector(candidate, image: str, context_sha256: str) -> bytes:
    if IMAGE_ID.fullmatch(image) is None or not _bootstrap_source_context_is_valid(context_sha256):
        raise ReleaseContractError("release-promotion-input-untrusted", "promotion requires a verified immutable image context")
    package = f"{RUNTIME_ROOT.as_posix()}/releases/{candidate.manifest.sha256}"
    members = {"candidate_snapshot_manifest_sha256": candidate.manifest.sha256,
               "release": candidate.manifest.sha256, "candidate_release": candidate.manifest.candidate_release,
               "framework_version": candidate.manifest.framework_version,
               "version_toml_sha256": candidate.manifest.version_toml_sha256,
               "selected_release_root": package, "framework_engine_root": package + "/FRAMEWORK_ENGINE",
               "methodology_root": package + "/METHODOLOGY", "candidate_image_digest": image,
               "candidate_image_context_sha256": context_sha256}
    return ("schema_version = 1\n" + "".join(f"{key} = {json.dumps(value)}\n" for key, value in members.items())).encode()


def _prior_image(selector: bytes) -> str | None:
    parsed = tomllib.loads(selector.decode())
    if (parsed.get("schema_version") == 1 and "package_manifest_sha256" in parsed
            and "target_project_context_sha256" in parsed and isinstance(parsed.get("image_digest"), str)):
        native = "sha256:" + parsed["image_digest"]
        return native if IMAGE_ID.fullmatch(native) else None
    values = {mapping[key] for mapping in (parsed, parsed.get("selection", {})) if isinstance(mapping, dict)
              for key in ("candidate_image_digest", "image_digest") if isinstance(mapping.get(key), str)}
    return next(iter(values)) if len(values) == 1 and IMAGE_ID.fullmatch(next(iter(values))) else None


def _prove_prior_skill(root: Path, candidate: ValidatedCandidate, prior_selector: bytes, skill: Path) -> list[dict]:
    actual = _skill_records(root, skill)
    parsed = tomllib.loads(prior_selector.decode())
    expected_root = f"{RUNTIME_ROOT.as_posix()}/releases/{candidate.authority.executing_release}"
    declared = parsed.get("selected_release_root", parsed.get("release_root", expected_root))
    if declared != expected_root:
        raise ReleaseContractError("release-promotion-skill-ownership-unknown", "prior selector has no exact retained package")
    try:
        package = _safe_path(root, expected_root)
        manifest_bytes = _file(root, f"{expected_root}/manifest.toml").read_bytes()
        manifest = manifest_bytes.decode("utf-8")
        data = tomllib.loads(manifest)
        bootstrap_prior = _bootstrap_prior_manifest_is_exact(
            parsed, manifest_bytes, candidate.authority.executing_release
        )
        base_manifest_fields = {"schema_version", "candidate_snapshot_manifest_sha256", "package", "files"}
        version_manifest_fields = base_manifest_fields | {"framework_version", "version_toml_sha256"}
        versioned_package = set(data) == version_manifest_fields
        if (set(data) not in (base_manifest_fields, version_manifest_fields)
                or data["schema_version"] != 2 or data["package"] != "caprmedio-framework"
                or (data["candidate_snapshot_manifest_sha256"] != candidate.authority.executing_release
                    and not (bootstrap_prior and _bootstrap_source_context_is_valid(
                        data["candidate_snapshot_manifest_sha256"]
                    )))):
            raise ValueError("retained prior manifest is not selected N")
        rows = [PackageRow.model_validate({"resource": row["resource"], "source_path": row["source_path"],
                "destination_path": row["destination"], "sha256": row["sha256"], "mode": row["mode"]}) for row in data["files"]]
        control_rows = [row for row in rows if row.resource == "PACKAGE_CONTROL"]
        if ({row.resource for row in rows} not in ({"FRAMEWORK_ENGINE", "METHODOLOGY", "SKILL"}, {"FRAMEWORK_ENGINE", "METHODOLOGY", "SKILL", "PACKAGE_CONTROL"})
                or not any(row.destination_path.startswith("METHODOLOGY/compiled/") for row in rows)
                or not any(row.destination_path.startswith("METHODOLOGY/sources/") for row in rows)
                or not {"SKILLS/ca/SKILL.md", "SKILLS/ca/agents/openai.yaml"} <= {row.destination_path for row in rows}
                or any(not any(row.source_path.startswith(prefix) for row in rows if row.resource == "FRAMEWORK_ENGINE")
                       for prefix in REQUIRED_ENGINE_SOURCE_PREFIXES)):
            raise ValueError("retained prior package is incomplete")
        if versioned_package:
            if len(control_rows) != 1 or (
                control_rows[0].source_path != VERSION_TOML_RELATIVE
                or control_rows[0].destination_path != VERSION_TOML_RELATIVE
                or control_rows[0].sha256 != data["version_toml_sha256"]
            ):
                raise ValueError("retained prior package has no exact version.toml control row")
            version_bytes = _file(root, f"{expected_root}/{VERSION_TOML_RELATIVE}").read_bytes()
            version_document = tomllib.loads(version_bytes.decode("utf-8"))
            if (
                not isinstance(version_document.get("framework"), dict)
                or version_document["framework"].get("version") != data["framework_version"]
                or _digest(version_bytes) != data["version_toml_sha256"]
            ):
                raise ValueError("retained prior package root version.toml is not exact")
        elif control_rows:
            raise ValueError("legacy retained prior package has an undeclared version control row")
        _verify_release(
            package,
            manifest if bootstrap_prior else _render_manifest(
                candidate.authority.executing_release, rows,
                framework_version=data.get("framework_version") if versioned_package else None,
                version_toml_sha256=data.get("version_toml_sha256") if versioned_package else None,
            ),
            rows,
            framework_version=data.get("framework_version") if versioned_package else None,
            version_toml_sha256=data.get("version_toml_sha256") if versioned_package else None,
        )
        expected = _skill_records(root, package / "SKILLS/ca")
        if actual != expected:
            raise ValueError("public Skill differs from retained N")
    except (OSError, ValueError, RuntimeError) as error:
        raise ReleaseContractError("release-promotion-skill-ownership-unknown", "existing Skill is not proven by the exact retained N package") from error
    return actual


def _gate_artifacts(root, suite, build, verification, e2e, full_gate):
    return {item.evidence_root: _records(root, root / item.evidence_root)
            for item in (suite, build, verification, e2e, full_gate)}


def _pending(root: Path, directory: Path, input_sha: str) -> tuple[dict, str]:
    payload = _file(root, f"{directory.relative_to(root).as_posix()}/intent.json").read_bytes()
    checksum = _file(root, f"{directory.relative_to(root).as_posix()}/intent.sha256").read_text()
    if _digest(payload) != checksum or canonical_json(json.loads(payload)) != payload:
        raise ReleaseContractError("release-promotion-intent-untrusted", "private pending intent is changed or unsealed")
    intent = json.loads(payload)
    if intent.get("schema") != INTENT_SCHEMA or intent.get("inputs_sha256") != input_sha:
        raise ReleaseContractError("release-promotion-retry-mismatch", "only the exact admitted promotion may resume")
    return intent, checksum


def _resume_currentness(root, candidate, compilation, suite, build, verification, e2e, full_gate, intent):
    # Observe current source bytes without pretending the selector still names N.
    observed = build_validated_candidate(root, candidate.intent,
                                        observed_source_frontier_digest=candidate.authority.source_frontier_digest)
    previous = candidate.manifest.model_dump(mode="json", by_alias=True)
    current = observed.manifest.model_dump(mode="json", by_alias=True)
    for key in ("executing_release", "sha256"):
        previous.pop(key)
        current.pop(key)
    if previous != current or compilation.authority != candidate.authority:
        raise ReleaseContractError("release-promotion-currentness-stale", "candidate source or compilation binding changed after admission")
    if (
        compilation.framework_version != candidate.manifest.framework_version
        or compilation.version_toml_sha256 != candidate.manifest.version_toml_sha256
        or full_gate.framework_version != candidate.manifest.framework_version
        or full_gate.version_toml_sha256 != candidate.manifest.version_toml_sha256
    ):
        raise ReleaseContractError("release-promotion-currentness-stale", "candidate version.toml binding changed after admission")
    if (tree_sha256(root, compilation.source_copy_root) != compilation.actual_derived_source_copy_sha256
            or tree_sha256(root, compilation.child_materialization_root) != compilation.actual_compiled_output_sha256):
        raise ReleaseContractError("release-promotion-currentness-stale", "source copy or compiled materialization changed")
    for row in compilation.package_rows:
        _read_row(root, row)
    package = _safe_path(root, intent["selected_release_root"])
    _verify_release(
        package,
        _render_manifest(
            candidate.manifest.sha256, compilation.package_rows,
            framework_version=candidate.manifest.framework_version,
            version_toml_sha256=candidate.manifest.version_toml_sha256,
        ),
        compilation.package_rows,
        framework_version=candidate.manifest.framework_version,
        version_toml_sha256=candidate.manifest.version_toml_sha256,
    )
    verify_bound_full_gate_evidence(candidate, compilation, suite, build, verification, e2e, full_gate)
    if _gate_artifacts(root, suite, build, verification, e2e, full_gate) != intent["gate_artifacts"]:
        raise ReleaseContractError("release-promotion-gates-stale", "original admitted suite or image artifacts changed")
    if _skill_records(root, package / "SKILLS/ca") != intent["candidate_skill"]:
        raise ReleaseContractError("release-promotion-skill-stale", "planned complete Skill changed")
    # Original execution proof is reopened independently of active selection;
    # the current source/package checks above remain this consumer's duty.
    read_image_execution_artifacts(candidate, compilation, suite, build, verification)


def _publish_selector(staged: Path, target: Path) -> None:
    os.replace(staged, target)
    _sync(target.parent)


def _publish_skill(staged: Path, target: Path) -> None:
    if os.path.lexists(target):
        raise ReleaseContractError("release-promotion-skill-ownership-unknown", "public Skill target appeared before publication")
    os.replace(staged, target)
    _sync(target.parent)


def promote_bound_release(candidate: ValidatedCandidate, compilation: SealedCandidateCompilation,
                          suite: SuiteGateEvidence, build: ImageBuildEvidence,
                          verification: ImageVerificationEvidence, *, e2e: CandidateE2EGateEvidence,
                          full_gate: FullGateEvidence) -> PromotionEvidence:
    """Admit once, retain N, then publish selector and exact project Skill."""
    with selector_publication_lock(candidate.project_root):
        return _promote_bound_release_locked(candidate, compilation, suite, build, verification,
                                             e2e=e2e, full_gate=full_gate)


def _promote_bound_release_locked(candidate: ValidatedCandidate, compilation: SealedCandidateCompilation,
                                 suite: SuiteGateEvidence, build: ImageBuildEvidence,
                                 verification: ImageVerificationEvidence, *, e2e: CandidateE2EGateEvidence,
                                 full_gate: FullGateEvidence) -> PromotionEvidence:
    """The existing promotion sequence runs under the sole selector lock."""
    # Typed evidence and the exact input digest are checked before a retry can
    # reopen its admitted intent. Its gates are reopened below before effects;
    # a stale original artifact remains an observed pending recovery.
    input_sha = _inputs(candidate, compilation, suite, build, verification, e2e, full_gate)
    root = Path(candidate.project_root)
    relative = f"{PROMOTION_ROOT}/{candidate.manifest.sha256}"
    directory = root / relative
    target = root / PROJECT_SKILL_TARGET
    selector = root / CURRENT_SELECTOR_RELATIVE
    if directory.exists() or directory.is_symlink():
        _safe_path(root, relative)
        intent, checksum = _pending(root, directory, input_sha)
    else:
        # Image/Unit evidence alone can never create a promotable intent.
        verify_bound_full_gate_evidence(candidate, compilation, suite, build, verification, e2e, full_gate)
        verify_bound_image_evidence(candidate, compilation, suite, build, verification)
        prior = _file(root, CURRENT_SELECTOR_RELATIVE).read_bytes()
        # Refuse unsafe ancestors even when the public target is absent.
        for parent in (root / ".agents", root / ".agents/skills", target):
            if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
                raise ReleaseContractError("release-promotion-skill-ownership-unknown", "public Skill path is unsafe")
        old_skill = _prove_prior_skill(root, candidate, prior, target) if target.exists() else None
        package_relative = f"{RUNTIME_ROOT.as_posix()}/releases/{candidate.manifest.sha256}"
        package = _safe_path(root, package_relative)
        planned = _skill_records(root, package / "SKILLS/ca")
        intent = {"schema": INTENT_SCHEMA, "inputs_sha256": input_sha,
                  "candidate_snapshot_manifest_sha256": candidate.manifest.sha256,
                  "framework_version": candidate.manifest.framework_version,
                  "version_toml_sha256": candidate.manifest.version_toml_sha256,
                  "prior_release": candidate.authority.executing_release, "prior_selector_sha256": _digest(prior),
                  "candidate_selector_sha256": _digest(_selector(
                      candidate, verification.candidate_image_digest, build.context_sha256
                  )),
                  "candidate_image_digest": verification.candidate_image_digest, "prior_image_digest": _prior_image(prior),
                  "selected_release_root": package_relative, "prior_skill": old_skill, "candidate_skill": planned,
                  "e2e_receipt_sha256": e2e.receipt_sha256,
                  "e2e_evidence_root": e2e.evidence_root,
                  "full_gate_receipt_sha256": full_gate.receipt_sha256,
                  "full_gate_evidence_root": full_gate.evidence_root,
                  "gate_artifacts": _gate_artifacts(root, suite, build, verification, e2e, full_gate)}
        parent = _safe_path(root, PROMOTION_ROOT, create=True)
        staging = Path(tempfile.mkdtemp(prefix=".admission-", dir=parent))
        try:
            _write(staging / "prior-selector.toml", prior)
            _write(staging / "candidate-selector.toml", _selector(
                candidate, verification.candidate_image_digest, build.context_sha256
            ))
            shutil.copytree(package / "SKILLS/ca", staging / "candidate-skill", copy_function=shutil.copy2)
            if _skill_records(root, staging / "candidate-skill") != planned:
                raise ReleaseContractError("release-promotion-skill-stale", "private staged Skill differs from admitted package")
            _sync_skill(staging / "candidate-skill")
            payload = canonical_json(intent)
            checksum = _digest(payload)
            _write(staging / "intent.json", payload)
            _write(staging / "intent.sha256", checksum.encode())
            _sync(staging)
            os.rename(staging, directory)
            _sync(parent)
        except Exception:
            # Keep any incomplete private admission for inspection; expose nothing.
            raise
    outcome, reason = "pending", "promotion effects remain incomplete"
    try:
        prior = _file(root, f"{relative}/prior-selector.toml").read_bytes()
        planned_selector = _selector(candidate, verification.candidate_image_digest, build.context_sha256)
        if (_digest(prior) != intent["prior_selector_sha256"]
                or _digest(planned_selector) != intent["candidate_selector_sha256"]):
            raise ReleaseContractError("release-promotion-intent-untrusted", "retained selection bytes changed")
        active = _file(root, CURRENT_SELECTOR_RELATIVE).read_bytes()
        if active not in (prior, planned_selector):
            raise ReleaseContractError("release-promotion-selection-stale", "selector is neither the exact prior nor admitted candidate")
        _resume_currentness(root, candidate, compilation, suite, build, verification, e2e, full_gate, intent)
        backup = directory / "prior-skill"
        if target.exists() or target.is_symlink():
            active_skill = _skill_records(root, target)
            if active_skill not in (intent["prior_skill"], intent["candidate_skill"]):
                raise ReleaseContractError("release-promotion-skill-ownership-unknown", "public Skill changed after admission")
        else:
            active_skill = None
        if backup.exists() and _skill_records(root, backup) != intent["prior_skill"]:
            raise ReleaseContractError("release-promotion-skill-ownership-unknown", "retained prior Skill changed")
        if active == prior:
            if active_skill != intent["prior_skill"] or backup.exists():
                raise ReleaseContractError("release-promotion-selection-stale", "prior selection no longer has its exact Skill")
            verify_bound_full_gate_evidence(candidate, compilation, suite, build, verification, e2e, full_gate)
            _publish_selector(directory / "candidate-selector.toml", selector)
        if active_skill != intent["candidate_skill"]:
            if active_skill is not None:
                if backup.exists():
                    raise ReleaseContractError("release-promotion-skill-ownership-unknown", "prior Skill recovery carrier already exists")
                os.rename(target, backup)
                _sync(directory)
                _sync(target.parent)
            elif intent["prior_skill"] is not None and not backup.exists():
                raise ReleaseContractError("release-promotion-skill-ownership-unknown", "missing public prior Skill has no retained recovery copy")
            _safe_path(root, ".agents/skills", create=True)
            staged_skill = directory / "candidate-skill"
            if _skill_records(root, staged_skill) != intent["candidate_skill"]:
                raise ReleaseContractError("release-promotion-skill-stale", "staged candidate Skill changed")
            _publish_skill(staged_skill, target)
        _resume_currentness(root, candidate, compilation, suite, build, verification, e2e, full_gate, intent)
        if (_file(root, CURRENT_SELECTOR_RELATIVE).read_bytes() != planned_selector
                or _skill_records(root, target) != intent["candidate_skill"]):
            raise ReleaseContractError("release-promotion-observation-incomplete", "candidate selector or public Skill is not observed")
        outcome, reason = "promoted", "exact candidate selector and complete project Skill observed"
    except (OSError, ValueError, RuntimeError) as error:
        reason = f"promotion pending: {getattr(error, 'code', type(error).__name__)}"
    evidence = PromotionEvidence(candidate.manifest.sha256, outcome, reason, intent["candidate_image_digest"],
               intent["prior_image_digest"], intent["prior_release"], intent["selected_release_root"],
               intent["selected_release_root"] + "/FRAMEWORK_ENGINE", intent["selected_release_root"] + "/METHODOLOGY",
               PROJECT_SKILL_TARGET, checksum, f"{relative}/observations/recording-unavailable", f"{relative}/prior-selector.toml",
               f"{relative}/prior-skill" if (directory / "prior-skill").exists() else None,
               framework_version=candidate.manifest.framework_version,
               version_toml_sha256=candidate.manifest.version_toml_sha256)
    try:
        observations = _safe_path(root, f"{relative}/observations", create=True)
        attempt = Path(tempfile.mkdtemp(prefix="attempt-", dir=observations))
        evidence = replace(evidence, evidence_root=attempt.relative_to(root).as_posix())
        payload = canonical_json(asdict(evidence))
        _write(attempt / "receipt.json", payload)
        _sync(attempt)
        return replace(evidence, receipt_sha256=_digest(payload))
    except (OSError, ReleaseContractError):
        return replace(evidence, outcome="recording_uncertain", reason="promotion observation recording is uncertain")


def verify_bound_promotion_evidence(candidate, compilation, suite, build, verification,
                                    evidence: PromotionEvidence, *, e2e: CandidateE2EGateEvidence,
                                    full_gate: FullGateEvidence) -> Path:
    """Reopen exact observed promotion for later, independently gated retirement."""
    verify_bound_full_gate_evidence(candidate, compilation, suite, build, verification, e2e, full_gate)
    input_sha = _inputs(candidate, compilation, suite, build, verification, e2e, full_gate)
    if not isinstance(evidence, PromotionEvidence) or evidence.outcome != "promoted" or not evidence.receipt_sha256:
        raise ReleaseContractError("release-promotion-evidence-untrusted", "retirement requires a recorded observed promotion")
    if build.execution_kind != "docker-subprocess" or verification.execution_kind != "docker-subprocess":
        raise ReleaseContractError("release-promotion-evidence-untrusted", "mock image admission is never actual promotion proof")
    root = Path(candidate.project_root)
    directory = _safe_path(root, f"{PROMOTION_ROOT}/{candidate.manifest.sha256}")
    intent, checksum = _pending(root, directory, input_sha)
    expected_prefix = directory.relative_to(root).as_posix() + "/observations/attempt-"
    if (not evidence.evidence_root.startswith(expected_prefix) or "/" in evidence.evidence_root[len(expected_prefix):]
            or evidence.intent_sha256 != checksum or evidence.prior_image_digest != intent["prior_image_digest"]
            or evidence.candidate_image_digest != intent["candidate_image_digest"]
            or evidence.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
            or evidence.framework_version != candidate.manifest.framework_version
            or evidence.version_toml_sha256 != candidate.manifest.version_toml_sha256
            or intent.get("framework_version") != candidate.manifest.framework_version
            or intent.get("version_toml_sha256") != candidate.manifest.version_toml_sha256
            or evidence.prior_release != intent["prior_release"]
            or evidence.selected_release_root != intent["selected_release_root"]
            or evidence.framework_engine_root != intent["selected_release_root"] + "/FRAMEWORK_ENGINE"
            or evidence.methodology_root != intent["selected_release_root"] + "/METHODOLOGY"
            or evidence.skill_target != PROJECT_SKILL_TARGET
            or evidence.retained_prior_selector_ref != directory.relative_to(root).as_posix() + "/prior-selector.toml"
            or intent.get("e2e_receipt_sha256") != e2e.receipt_sha256
            or intent.get("e2e_evidence_root") != e2e.evidence_root
            or intent.get("full_gate_receipt_sha256") != full_gate.receipt_sha256
            or intent.get("full_gate_evidence_root") != full_gate.evidence_root):
        raise ReleaseContractError("release-promotion-evidence-untrusted", "promotion receipt is outside the exact admitted observation")
    receipt = _file(root, f"{evidence.evidence_root}/receipt.json").read_bytes()
    if (_digest(receipt) != evidence.receipt_sha256
            or receipt != canonical_json(asdict(replace(evidence, receipt_sha256=None)))):
        raise ReleaseContractError("release-promotion-evidence-untrusted", "promotion receipt is changed or caller-forged")
    _resume_currentness(root, candidate, compilation, suite, build, verification, e2e, full_gate, intent)
    backup = directory / "prior-skill"
    if evidence.retained_prior_skill_ref is not None:
        if (evidence.retained_prior_skill_ref != backup.relative_to(root).as_posix()
                or _skill_records(root, backup) != intent["prior_skill"]):
            raise ReleaseContractError("release-promotion-evidence-stale", "retained prior Skill no longer matches the admitted recovery carrier")
    elif backup.exists() or backup.is_symlink():
        raise ReleaseContractError("release-promotion-evidence-stale", "promotion receipt does not identify its retained prior Skill")
    prior = _file(root, evidence.retained_prior_selector_ref).read_bytes()
    if (_digest(prior) != intent["prior_selector_sha256"] or _prior_image(prior) != evidence.prior_image_digest
            or _file(root, CURRENT_SELECTOR_RELATIVE).read_bytes() != _selector(
                candidate, evidence.candidate_image_digest, build.context_sha256
            )
            or _skill_records(root, root / PROJECT_SKILL_TARGET) != intent["candidate_skill"]):
        raise ReleaseContractError("release-promotion-evidence-stale", "recorded promotion or retained prior identity is no longer observed")
    return root


__all__ = ["PromotionEvidence", "promote_bound_release", "verify_bound_promotion_evidence"]
