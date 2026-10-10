"""Retain D604's selected O169 command using its existing actual Action start.

No Run or Journal event is created here.  The selected provider supplies its
actual shared Session; source/input/authorization and original Full Gate bytes
are reopened before the immutable command is retained.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
import json
from pathlib import Path, PurePosixPath
from typing import Any

from framework_installation_command import (
    COMMAND_DIRECTORY, FrameworkInstallationCommandError,
    _canonical_json, _command_id, _digest, _duplicate_pairs, _ensure_directory,
    _prior_runtime_selector_sha256, _publish_exact, _registry_reference,
    _regular_bytes, _reject_constant, _relative, _root, _sha256, _text,
)
from framework_package import VerifiedFrameworkPackage, verify_framework_package
from installation_context import TargetProjectContext, TargetProjectRequest, bind_target_project_context
from operator_registry import parse_operators_registry
from release_contract import ReleaseContractError
from release_promotion import admit_selected_native_promotion_start
from retained_full_gate_packet import RetainedNativeFullGatePacket
from workflow_run_support import RunExecutionSession
import work_journal


OPERATION = "promote_selected_runtime"
_KEYS = frozenset({
    "schema_version", "operation", "command_id", "operator", "journal_author",
    "operators_registry_sha256", "action_source", "target_project_context_sha256",
    "package_manifest_sha256", "full_gate_receipt_sha256", "prior_runtime_selector_sha256",
    "selected_start_receipt", "parent_lineage",
})


class SelectedInstallationCommandError(ReleaseContractError):
    """Stable refusal from the selected command boundary."""


def _refuse(code: str, message: str) -> None:
    raise SelectedInstallationCommandError(code, message)


def _registered_journal_author(record: object) -> str | None:
    """D494's literal account name or its explicitly registered mapping."""

    author = record.journal_author
    if author is None and work_journal.AUTHOR_RE.fullmatch(record.name) is not None:
        return record.name
    return author


@dataclass(frozen=True)
class SelectedInstallationCommandReceipt:
    command_id: str
    operator: str
    journal_author: str
    operators_registry_sha256: str
    action_source: Mapping[str, object]
    target_project_context_sha256: str
    package_manifest_sha256: str
    full_gate_receipt_sha256: str
    prior_runtime_selector_sha256: str | None
    selected_start_receipt: Mapping[str, object]
    parent_lineage: tuple[str, ...]
    sha256: str
    payload: bytes


@dataclass(frozen=True)
class SelectedInstallationCommandResult:
    receipt: SelectedInstallationCommandReceipt
    receipt_path: Path
    action_provenance: object


def read_selected_installation_command_receipt(
    payload: bytes, *, expected_sha256: str | None = None,
) -> SelectedInstallationCommandReceipt:
    """Read the separate closed selected variant without granting authority."""

    if not isinstance(payload, bytes):
        _refuse("selected-installation-command-invalid", "selected command bytes are required")
    if expected_sha256 is not None and _sha256(payload) != _digest(expected_sha256, field="expected command digest"):
        _refuse("selected-installation-command-digest-mismatch", "selected command bytes changed")
    try:
        value = json.loads(payload.decode("utf-8"), object_pairs_hook=_duplicate_pairs, parse_constant=_reject_constant)
    except (UnicodeDecodeError, ValueError, FrameworkInstallationCommandError) as error:
        raise SelectedInstallationCommandError("selected-installation-command-invalid", "selected command is not canonical JSON") from error
    if (not isinstance(value, dict) or set(value) != _KEYS or value.get("operation") != OPERATION
            or type(value.get("schema_version")) is not int or value["schema_version"] != 1
            or _canonical_json(value) != payload):
        _refuse("selected-installation-command-invalid", "selected command violates its closed schema")
    source = value["action_source"]
    if (not isinstance(source, dict) or set(source) != {"atom_id", "version", "path", "sha256"}
            or source.get("atom_id") != "CA-O-169" or type(source.get("version")) is not int or source["version"] != 5):
        _refuse("selected-installation-command-invalid", "selected command requires the admitted O169 source")
    _relative(source.get("path"), field="action_source.path")
    _digest(source.get("sha256"), field="action_source.sha256")
    author = _text(value["journal_author"], field="journal_author")
    if work_journal.AUTHOR_RE.fullmatch(author) is None:
        _refuse("selected-installation-command-invalid", "selected command author is not a registered Journal account")
    receipt = value["selected_start_receipt"]
    try:
        RunExecutionSession._validated_started_receipt(receipt)
    except (TypeError, ValueError) as error:
        raise SelectedInstallationCommandError("selected-installation-command-invalid", "selected start receipt is not canonical") from error
    lineage = value["parent_lineage"]
    if (not isinstance(lineage, list) or len(lineage) != 2
            or any(not isinstance(item, str) or not item or item != item.strip() or "\n" in item or "\r" in item for item in lineage)
            or len(set(lineage)) != 2):
        _refuse("selected-installation-command-invalid", "selected command requires the actual Step/Workflow parent chain")
    prior = value["prior_runtime_selector_sha256"]
    if prior is not None:
        _digest(prior, field="prior_runtime_selector_sha256")
    return SelectedInstallationCommandReceipt(
        command_id=_command_id(value["command_id"]),
        operator=_text(value["operator"], field="operator"), journal_author=author,
        operators_registry_sha256=_digest(value["operators_registry_sha256"], field="operators_registry_sha256"),
        action_source=dict(source),
        target_project_context_sha256=_digest(value["target_project_context_sha256"], field="target_project_context_sha256"),
        package_manifest_sha256=_digest(value["package_manifest_sha256"], field="package_manifest_sha256"),
        full_gate_receipt_sha256=_digest(value["full_gate_receipt_sha256"], field="full_gate_receipt_sha256"),
        prior_runtime_selector_sha256=prior, selected_start_receipt=dict(receipt),
        parent_lineage=tuple(lineage), sha256=_sha256(payload), payload=payload,
    )


def retain_selected_installation_command(
    run: Any, context: Any, *, target: TargetProjectRequest,
    target_context: TargetProjectContext, package: VerifiedFrameworkPackage,
    full_gate_packet: RetainedNativeFullGatePacket,
) -> SelectedInstallationCommandResult:
    """Retain the command after physically rereading its actual selected start."""

    provenance = admit_selected_native_promotion_start(run, context)
    if context.step_atom_id != "CA-O-178":
        _refuse("selected-installation-command-occurrence-invalid", "only the selected promote occurrence may retain installation command input")
    if (type(target) is not TargetProjectRequest or type(target_context) is not TargetProjectContext
            or type(package) is not VerifiedFrameworkPackage or type(full_gate_packet) is not RetainedNativeFullGatePacket):
        _refuse("selected-installation-command-untrusted", "selected command requires concrete target, package and original gate evidence")
    root = _root(target.target_root)
    if str(root) != run.project_root or bind_target_project_context(target) != target_context:
        _refuse("selected-installation-command-context-stale", "selected command target context changed")
    if verify_framework_package(target.package_root) != package:
        _refuse("selected-installation-command-package-stale", "selected command package changed")
    from release_full_gate import verify_detached_native_full_gate_evidence

    retained = verify_detached_native_full_gate_evidence(
        full_gate_packet.artifact_root, full_gate_packet.retained_candidate, full_gate_packet.suite,
        full_gate_packet.build, full_gate_packet.verification, full_gate_packet.e2e, full_gate_packet.evidence,
    )
    if (retained.view.actual_package_manifest_sha256 != package.manifest_digest
            or run.candidate is None or full_gate_packet.retained_candidate.descriptor != run.candidate.manifest
            or full_gate_packet.retained_candidate.candidate_snapshot_manifest_sha256 != run.request.candidate_snapshot_manifest.sha256):
        _refuse("selected-installation-command-package-mismatch", "selected command package differs from the original Full Gate")
    registry_ref = _registry_reference(target, target_context, root)
    registry = _regular_bytes(root, registry_ref, code="selected-installation-command-operator-invalid", label="registered Operator evidence")
    records = parse_operators_registry(registry)
    matches = [record for record in records if _registered_journal_author(record) == provenance.author]
    if len(matches) != 1 or _sha256(registry) != target_context.registry_sha256:
        _refuse("selected-installation-command-operator-invalid", "actual selected author has no exact registered Operator mapping")
    session = run.selected_action_session
    actual = next(record for record in session.actual.values() if record["run_id"] == context.action_run_id)
    definition = actual["definition"]
    payload = _canonical_json({
        "schema_version": 1, "operation": OPERATION, "command_id": context.action_run_id,
        "operator": matches[0].name, "journal_author": provenance.author,
        "operators_registry_sha256": _sha256(registry),
        "action_source": {"atom_id": definition["atom_id"], "version": definition["version"],
                          "path": definition["path"], "sha256": definition["digest"]},
        "target_project_context_sha256": target_context.sha256,
        "package_manifest_sha256": package.manifest_digest,
        "full_gate_receipt_sha256": full_gate_packet.evidence.receipt_sha256,
        "prior_runtime_selector_sha256": _prior_runtime_selector_sha256(root),
        "selected_start_receipt": session.read_recorded_action_start_receipt(context.action_run_id),
        "parent_lineage": list(provenance.parent_lineage),
    })
    receipt = read_selected_installation_command_receipt(payload)
    directory = _ensure_directory(root, PurePosixPath(*COMMAND_DIRECTORY.parts))
    path = _publish_exact(directory, f"{receipt.sha256}.json", payload)
    relative = PurePosixPath(path.relative_to(root).as_posix())
    if (admit_selected_native_promotion_start(run, context) != provenance
            or read_selected_installation_command_receipt(
                _regular_bytes(root, relative, code="selected-installation-command-stale", label="selected installation command"),
                expected_sha256=receipt.sha256,
            ) != receipt or bind_target_project_context(target) != target_context):
        _refuse("selected-installation-command-stale", "selected command changed before publication admission")
    return SelectedInstallationCommandResult(receipt, path, provenance)


def reopen_selected_installation_command_start(
    project_root: Path | str, receipt: SelectedInstallationCommandReceipt,
) -> Mapping[str, object]:
    """Reopen the canonical Action start addressed by the selected command.

    This proves historical final-generation provenance and grants no new
    execution, authorization, retry or publication authority.
    """

    if type(receipt) is not SelectedInstallationCommandReceipt:
        _refuse("selected-installation-command-untrusted", "selected command must be closed typed evidence")
    root = _root(project_root)
    canonical = COMMAND_DIRECTORY / f"{receipt.sha256}.json"
    if read_selected_installation_command_receipt(
        _regular_bytes(root, PurePosixPath(canonical.as_posix()), code="selected-installation-command-stale", label="selected command"),
        expected_sha256=receipt.sha256,
    ) != receipt:
        _refuse("selected-installation-command-stale", "selected command differs from its retained carrier")
    settings_path = work_journal.resolve_settings_path(root)
    registry_ref = PurePosixPath((settings_path.parent / "operators_registry.toml").relative_to(root).as_posix())
    registry = _regular_bytes(root, registry_ref, code="selected-installation-command-operator-invalid", label="registered Operator evidence")
    records = parse_operators_registry(registry)
    matches = [record for record in records if record.name == receipt.operator
               and _registered_journal_author(record) == receipt.journal_author]
    if len(matches) != 1 or _sha256(registry) != receipt.operators_registry_sha256:
        _refuse("selected-installation-command-operator-invalid", "selected command differs from exact registered Operator attribution")
    RunExecutionSession._assert_regular_journal_control(root)
    journal_root = root / work_journal.configured_journal_root(root)
    carrier, line = RunExecutionSession._validated_started_receipt(receipt.selected_start_receipt)
    path = root / carrier
    try:
        path.relative_to(journal_root)
    except ValueError as error:
        raise SelectedInstallationCommandError("selected-installation-command-start-invalid", "start receipt escapes the canonical Journal") from error
    RunExecutionSession._assert_regular_receipt_carrier(root, journal_root, path)
    event = RunExecutionSession._read_receipted_event(root, path, line, receipt.selected_start_receipt)
    actual = event.get("run", {})
    source = actual.get("definition", {})
    if (event.get("schema_version") != 5 or event.get("kind") != "workflow_execution"
            or event.get("event") != "started" or event.get("author") != receipt.journal_author
            or actual.get("kind") != "action" or actual.get("run_id") != receipt.command_id
            or actual.get("parent_run_id") != receipt.parent_lineage[0]
            or {"atom_id": source.get("atom_id"), "version": source.get("version"),
                "path": source.get("path"), "sha256": source.get("digest")} != dict(receipt.action_source)):
        _refuse("selected-installation-command-start-mismatch", "selected command does not bind its canonical O169 start")
    from FIND_AND_FETCH_JOURNAL_EVENTS.find_and_fetch_journal_events import capture_snapshot, query

    snapshot = capture_snapshot(root)
    if snapshot.get("source_root") != journal_root.relative_to(root).as_posix():
        _refuse("selected-installation-command-start-invalid", "bounded Journal reader has a different canonical root")
    parent_filter = (
        '"event:/event" = "started" AND "event:/run/run_id" IN ('
        + ", ".join(json.dumps(identity) for identity in receipt.parent_lineage) + ")"
    )
    parents = query(snapshot, {"mode": "full_events", "filter": parent_filter, "limit": 3})
    if parents.get("status") != "complete" or parents.get("coverage", {}).get("complete") is not True:
        _refuse("selected-installation-command-start-invalid", "bounded parent Journal coverage is incomplete")
    matches = parents.get("results", [])
    if len(matches) != 2:
        _refuse("selected-installation-command-start-ambiguous", "selected parent start records are absent or ambiguous")
    parent_events: dict[str, Mapping[str, Any]] = {}
    for match in matches:
        sealed = work_journal.validate_sealed_event(match["event"])
        record = sealed.get("run", {})
        identity = record.get("run_id")
        if (identity not in receipt.parent_lineage or identity in parent_events
                or sealed.get("schema_version") != 5 or sealed.get("kind") != "workflow_execution"
                or sealed.get("event") != "started" or sealed.get("author") != receipt.journal_author
                or sealed.get("llm_session") != event.get("llm_session")
                or sealed.get("action_id") != event.get("action_id")):
            _refuse("selected-installation-command-start-mismatch", "selected parent Journal records have another source or identity")
        parent_events[identity] = sealed
    step_event, workflow_event = (parent_events[identity] for identity in receipt.parent_lineage)
    step, workflow = step_event["run"], workflow_event["run"]
    if (step.get("kind") != "step" or step.get("parent_run_id") != workflow["run_id"]
            or step.get("definition", {}).get("atom_id") != "CA-O-178"
            or workflow.get("kind") != "workflow" or "parent_run_id" in workflow
            or workflow.get("definition", {}).get("atom_id") != "CA-O-164"
            or workflow.get("definition", {}).get("version") != 9
            or event.get("definition_bindings") != [{"kind": "action", **source}]
            or step_event.get("definition_bindings") != [{"kind": "step", **step["definition"]}]
            or {"kind": "action", **source} not in workflow_event.get("definition_bindings", [])):
        _refuse("selected-installation-command-start-mismatch", "selected command has an invalid canonical Step/Workflow chain")
    return event


__all__ = [
    "OPERATION", "SelectedInstallationCommandError", "SelectedInstallationCommandReceipt",
    "SelectedInstallationCommandResult", "read_selected_installation_command_receipt",
    "retain_selected_installation_command", "reopen_selected_installation_command_start",
]
