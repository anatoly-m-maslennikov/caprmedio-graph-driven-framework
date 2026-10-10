"""Closed, effect-free checkpoint codec for a private Release Action Run.

This module deliberately only encodes and restores already-observed local
state.  It does not write a checkpoint, record a Journal Event, invoke a
Tool, import a provider, or recreate a Docker executor.  A caller which has
durably stored the returned bytes must independently re-admit an executor
before an image phase can be attempted after restoration.
"""

from __future__ import annotations

import base64
import hashlib
import json
import math
import tomllib
from dataclasses import asdict, fields
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, TypeVar

from release_actions import (
    PHASES,
    AdmittedImageExecutor,
    LocalReleaseHelperBinding,
    ReleaseActionRun,
    ReleasePhaseResult,
    SelectedReleaseActionContext,
    _fingerprint,
)
from release_compilation import (
    ReleaseCompilationPreflight,
    SealedPrivateMethodologyCompilation,
    read_sealed_private_methodology_compilation,
)
from release_contract import (
    CandidateBuildRequest,
    CandidateSnapshotManifest,
    ReleaseContractError,
    SealedAuthority,
    ValidatedCandidate,
    _safe_relative,
    canonical_json,
)
from release_handoff import (
    CompilerEntrypoint,
    SealedCandidateCompilation,
    SealedMethodologyExport,
    SealedSourceCopy,
    bind_sealed_methodology_export,
)
from release_e2e_gate import CandidateE2EGateEvidence, PortableCandidateE2EGateEvidence, HarnessReceipt
from release_image import (
    ImageBuildEvidence,
    ImageRetirementEvidence,
    ImageVerificationEvidence,
    PortableImageBuildEvidence,
    PortableImageVerificationEvidence,
)
from release_portable_contract import (
    PortableBindingAtom,
    PortablePackageRow,
    SealedPortableCandidateCompilation,
    SealedPortableSourceSnapshot,
    collect_portable_source_snapshot,
    seal_portable_source_snapshot,
)
from release_portable_package import (
    PreparedPortableReleasePackage,
    reopen_portable_release_package,
)
from release_promotion import PromotionEvidence, NativePromotionEvidence
from release_suite import PortableSuiteGateEvidence, SuiteGateEvidence
from release_version import ReleaseVersionRequest


RELEASE_ACTION_CHECKPOINT_SCHEMA = "caprmedio.release_version.action_run_checkpoint.v1"
LEGACY_NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA = "caprmedio.release_version.action_run_checkpoint.v2-portable"
NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA = "caprmedio.release_version.action_run_checkpoint.v3-portable"
_TAGGED_TYPES = {
    "candidate": ValidatedCandidate,
    "preflight": ReleaseCompilationPreflight,
    "source_copy": SealedSourceCopy,
    "compilation": SealedCandidateCompilation,
    "suite": SuiteGateEvidence,
    "package": dict,
    "build": ImageBuildEvidence,
    "verification": ImageVerificationEvidence,
    "e2e": CandidateE2EGateEvidence,
    "promotion": PromotionEvidence,
    "retirement": ImageRetirementEvidence,
}
_STATE_NAMES = (
    "candidate", "preflight", "source_copy", "compilation", "suite", "package", "build",
    "verification", "e2e", "full_gate", "promotion", "retirement",
)
_PHASE_STATE = {
    "freeze": "candidate",
    "validate": "candidate",
    "deliver_sources": "source_copy",
    "compile": "compilation",
    "closed_unit_gate": "suite",
    "stage_candidate": "package",
    "candidate_image_build": "build",
    "candidate_image_canary": "verification",
    "host_candidate_e2e": "e2e",
    "aggregate_full_gate": "full_gate",
    "promote": "promotion",
    "retire": "retirement",
}
_NATIVE_STATE_NAMES = (
    "candidate", "preflight", "methodology_export", "private_compilation",
    "portable_source_snapshot", "portable_compilation", "portable_suite",
    "prepared_portable_package", "build", "verification", "e2e", "full_gate",
    "promotion", "retirement",
)
_NATIVE_PHASE_STATE = {
    "freeze": "candidate",
    "validate": "candidate",
    "deliver_sources": "methodology_export",
    "compile": "portable_compilation",
    "closed_unit_gate": "portable_suite",
    "stage_candidate": "prepared_portable_package",
    "candidate_image_build": "build",
    "candidate_image_canary": "verification",
    "host_candidate_e2e": "e2e",
    "aggregate_full_gate": "full_gate",
    "promote": "promotion",
    "retire": "retirement",
}
_NATIVE_CHECKPOINT_FIELDS = {
    "schema", "kind", "sha256", "project_root", "workflow_run_id", "frozen_parameters_sha256", "request",
    "next_phase", "stopped", "in_progress", "contexts", "results", "shared_recordings", "pending_recordings", "state",
}
_SHA256_HEX = frozenset("0123456789abcdef")
_PENDING_EVENT_OUTCOMES = frozenset({"completed", "no_op", "failed", "cancelled", "partial", "interrupted_pending"})
_T = TypeVar("_T")


def _full_gate_type() -> type[Any]:
    """Resolve the independently owned aggregate model only when needed.

    Earlier Release phases do not need the aggregate implementation.  The
    codec nevertheless refuses any full-gate state unless its producer's
    concrete model is present and exact.
    """

    from release_full_gate import FullGateEvidence

    return FullGateEvidence


def _tagged_type(name: str) -> type[Any]:
    if name == "full_gate":
        return _full_gate_type()
    return _TAGGED_TYPES[name]


def _error(code: str, message: str) -> ReleaseContractError:
    return ReleaseContractError(code, message)


def release_action_checkpoint_sha256(checkpoint: Mapping[str, Any]) -> str:
    """Digest one checkpoint with its self-excluding digest blanked.

    The caller receives only a pure digest calculation.  It does not create a
    carrier, change a Run, or establish any Journal record.
    """

    value = dict(checkpoint)
    value["sha256"] = "0" * 64
    return hashlib.sha256(canonical_json(value)).hexdigest()


def _mapping(value: Any, required: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != required:
        raise _error("release-checkpoint-invalid", f"{label} has unknown, missing, or non-object members")
    return value


def _text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip() or "\n" in value or "\r" in value:
        raise _error("release-checkpoint-invalid", f"{label} must be one bounded non-empty string")
    return value


def _sha256(value: Any, label: str) -> str:
    value = _text(value, label)
    if len(value) != 64 or any(character not in _SHA256_HEX for character in value):
        raise _error("release-checkpoint-invalid", f"{label} must be one lowercase SHA-256 digest")
    return value


def _local_helper_binding_value(value: LocalReleaseHelperBinding | None) -> dict[str, str]:
    """Encode the two Project-local helper digests for the current Run only."""

    if type(value) is not LocalReleaseHelperBinding:
        raise _error("release-checkpoint-binding-mismatch", "current native checkpoint lacks its frozen local helper binding")
    return {
        "native_hooks_sha256": _sha256(value.native_hooks_sha256, "local_helper_binding.native_hooks_sha256"),
        "local_release_sha256": _sha256(value.local_release_sha256, "local_helper_binding.local_release_sha256"),
    }


def _load_local_helper_binding(value: Any) -> LocalReleaseHelperBinding:
    payload = _mapping(value, {"native_hooks_sha256", "local_release_sha256"}, "local_helper_binding")
    return LocalReleaseHelperBinding(
        native_hooks_sha256=_sha256(payload["native_hooks_sha256"], "local_helper_binding.native_hooks_sha256"),
        local_release_sha256=_sha256(payload["local_release_sha256"], "local_helper_binding.local_release_sha256"),
    )


def _native_checkpoint_envelope(value: Any, label: str) -> tuple[dict[str, Any], LocalReleaseHelperBinding | None]:
    """Read v3 helper-bound checkpoints and retain v2 as documentary-only."""

    if not isinstance(value, dict):
        raise _error("release-checkpoint-invalid", f"{label} must be an object")
    schema = value.get("schema")
    if schema == NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA:
        source = _mapping(value, _NATIVE_CHECKPOINT_FIELDS | {"local_helper_binding"}, label)
        return source, _load_local_helper_binding(source["local_helper_binding"])
    if schema == LEGACY_NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA:
        return _mapping(value, _NATIVE_CHECKPOINT_FIELDS, label), None
    raise _error("release-checkpoint-schema-unsupported", "native checkpoint schema or kind is not supported")


def _index(value: Any, label: str) -> int:
    if type(value) is not int or value < 0 or value >= len(PHASES):
        raise _error("release-checkpoint-invalid", f"{label} is outside the selected phase graph")
    return value


def _safe_path(value: Any, label: str) -> str:
    try:
        return _safe_relative(_text(value, label), label)
    except ValueError as error:
        raise _error("release-checkpoint-invalid", f"{label} is not a safe Project-relative path") from error


def _json_value(value: Any, label: str) -> Any:
    """Reject executable and non-canonical values before JSON serialization."""

    if value is None or type(value) in {bool, int, str}:
        return value
    if type(value) is float:
        if not math.isfinite(value):
            raise _error("release-checkpoint-invalid", f"{label} contains a non-finite number")
        return value
    if isinstance(value, bytes):
        return {"encoding": "base64", "data": base64.b64encode(value).decode("ascii")}
    if isinstance(value, (list, tuple)):
        return [_json_value(item, label) for item in value]
    if isinstance(value, dict):
        if any(not isinstance(key, str) for key in value):
            raise _error("release-checkpoint-invalid", f"{label} has a non-string object key")
        return {key: _json_value(item, label) for key, item in value.items()}
    raise _error("release-checkpoint-invalid", f"{label} contains an unsupported executable or object value")


def _bytes(value: Any, label: str) -> bytes:
    encoded = _mapping(value, {"encoding", "data"}, label)
    if encoded["encoding"] != "base64" or not isinstance(encoded["data"], str):
        raise _error("release-checkpoint-invalid", f"{label} is not a closed base64 byte value")
    try:
        decoded = base64.b64decode(encoded["data"], validate=True)
    except (ValueError, TypeError) as error:
        raise _error("release-checkpoint-invalid", f"{label} has invalid base64 bytes") from error
    if base64.b64encode(decoded).decode("ascii") != encoded["data"]:
        raise _error("release-checkpoint-invalid", f"{label} base64 is not canonical")
    return decoded


def _dump_model(value: Any, cls: type[Any], label: str) -> dict[str, Any]:
    if type(value) is not cls:
        raise _error("release-checkpoint-invalid", f"{label} is not the expected typed value")
    return _json_value(value.model_dump(mode="json", by_alias=True), label)


def _load_model(value: Any, cls: type[_T], label: str) -> _T:
    if not isinstance(value, dict):
        raise _error("release-checkpoint-invalid", f"{label} must be an object")
    try:
        return cls.model_validate(value)
    except (TypeError, ValueError) as error:
        raise _error("release-checkpoint-invalid", f"{label} violates its closed typed contract") from error


def _dump_dataclass(value: Any, cls: type[Any], label: str) -> dict[str, Any]:
    if type(value) is not cls:
        raise _error("release-checkpoint-invalid", f"{label} is not the expected typed value")
    return _json_value(asdict(value), label)


def _load_dataclass(value: Any, cls: type[_T], label: str, *, tuple_fields: frozenset[str] = frozenset()) -> _T:
    required = {item.name for item in fields(cls)}
    payload = _mapping(value, required, label)
    restored = dict(payload)
    for field_name in tuple_fields:
        source = restored.get(field_name)
        if not isinstance(source, list) or any(not isinstance(item, str) for item in source):
            raise _error("release-checkpoint-invalid", f"{label}.{field_name} must be a string list")
        restored[field_name] = tuple(source)
    try:
        return cls(**restored)
    except (TypeError, ValueError) as error:
        raise _error("release-checkpoint-invalid", f"{label} cannot construct its typed state") from error


def _candidate_value(candidate: ValidatedCandidate) -> dict[str, Any]:
    if type(candidate) is not ValidatedCandidate:
        raise _error("release-checkpoint-invalid", "candidate is not locally validated typed state")
    payload = {
        "project_root": candidate.project_root,
        "manifest": _dump_model(candidate.manifest, CandidateSnapshotManifest, "candidate.manifest"),
        "authority": _dump_model(candidate.authority, SealedAuthority, "candidate.authority"),
        "intent": _dump_model(candidate.intent, CandidateBuildRequest, "candidate.intent"),
    }
    if candidate.native_installed_n is not None:
        if candidate.native_installed_n.selected.framework_version != candidate.manifest.executing_release:
            raise _error("release-checkpoint-binding-mismatch", "native N differs from the frozen executing release")
        payload["native_installed_n"] = _native_n_value(candidate.native_installed_n, candidate.project_root)
    return payload


def _load_candidate(value: Any, root: str, *, historical_native_n: bool = False) -> ValidatedCandidate:
    required = {"project_root", "manifest", "authority", "intent"}
    if isinstance(value, dict) and "native_installed_n" in value:
        required.add("native_installed_n")
    payload = _mapping(value, required, "candidate")
    if payload["project_root"] != root:
        raise _error("release-checkpoint-binding-mismatch", "candidate root differs from the checkpoint root")
    manifest = _load_model(payload["manifest"], CandidateSnapshotManifest, "candidate.manifest")
    authority = _load_model(payload["authority"], SealedAuthority, "candidate.authority")
    intent = _load_model(payload["intent"], CandidateBuildRequest, "candidate.intent")
    if (
        authority.executing_release != manifest.executing_release
        or authority.candidate_release != manifest.candidate_release
        or authority.canonical_source_snapshot_digest != manifest.canonical_source_snapshot_digest
        or authority.project_structure_digest != manifest.project_structure_digest
        or authority.framework_settings_digest != manifest.framework_settings_digest
        or authority.source_frontier_digest != manifest.source_frontier_digest
        or authority.nested_source_recursive_sha256_before != manifest.nested_source_recursive_sha256_before
        or authority.expected_candidate_snapshot_manifest_sha256 != manifest.sha256
        or intent.candidate_release != manifest.candidate_release
        or intent.expected_derived_source_copy_sha256 != manifest.expected_derived_source_copy_sha256
        or intent.expected_compiled_output_sha256 != manifest.expected_compiled_output_sha256
        or intent.full_suite_environment != manifest.full_suite_environment
        or intent.candidate_image_reference != manifest.candidate_image.candidate_image_reference
    ):
        raise _error("release-checkpoint-binding-mismatch", "candidate authority or intent is not exactly manifest-bound")
    native_n = _load_native_n(payload["native_installed_n"], root, historical=historical_native_n) if "native_installed_n" in payload else None
    if native_n is not None and native_n.selected.framework_version != manifest.executing_release:
        raise _error("release-checkpoint-binding-mismatch", "native N differs from the frozen executing release")
    return ValidatedCandidate(root, manifest, authority, intent, native_n)


def _native_documentary_types() -> dict[str, type[Any]]:
    from framework_package import PackageBindingAtom, PackageInventoryRow, VerifiedFrameworkPackage
    from installation_context import PackageSourcePin, TargetProjectContext, VerifiedPackageEvidence
    from installed_mcp_binding import InstalledMcpBinding, PackageCaSkillMember, TargetProjectContext as InstalledMcpTargetProjectContext
    from native_selected_installation import NativeSelectedInstallation

    classes = {cls.__name__: cls for cls in (
        PackageBindingAtom, PortableBindingAtom, PackageInventoryRow, VerifiedFrameworkPackage, PackageSourcePin, TargetProjectContext,
        VerifiedPackageEvidence, InstalledMcpBinding, PackageCaSkillMember, NativeSelectedInstallation,
    )}
    classes["InstalledMcpTargetProjectContext"] = InstalledMcpTargetProjectContext
    return classes


def _native_document_value(value: Any, root: str) -> Any:
    """Closed documentary facts only; no import path or executable is encoded."""

    if value is None or type(value) in {str, int, bool}:
        return value
    if isinstance(value, Path):
        if value == Path(root):
            return {"type": "project_root", "value": None}
        try:
            relative = value.relative_to(root).as_posix()
        except ValueError as error:
            raise _error("release-checkpoint-binding-mismatch", "native documentary path escapes Project root") from error
        return {"type": "path", "value": _safe_path(relative, "native documentary path")}
    if type(value) is tuple:
        return {"type": "tuple", "value": [_native_document_value(item, root) for item in value]}
    classes = _native_documentary_types()
    name = next((label for label, cls in classes.items() if type(value) is cls), None)
    if name is None:
        raise _error("release-checkpoint-invalid", "native documentary fact has an unsupported type")
    return {"type": name, "value": {item.name: _native_document_value(getattr(value, item.name), root) for item in fields(value)}}


def _load_native_document(value: Any, root: str) -> Any:
    if value is None or type(value) in {str, int, bool}:
        return value
    tagged = _mapping(value, {"type", "value"}, "native documentary fact")
    name = _text(tagged["type"], "native documentary type")
    if name == "project_root":
        if tagged["value"] is not None:
            raise _error("release-checkpoint-invalid", "native Project root tag has an unexpected value")
        return Path(root)
    if name == "path":
        return Path(root) / _safe_path(tagged["value"], "native documentary path")
    if name == "tuple":
        if not isinstance(tagged["value"], list):
            raise _error("release-checkpoint-invalid", "native documentary tuple is not a list")
        return tuple(_load_native_document(item, root) for item in tagged["value"])
    cls = _native_documentary_types().get(name)
    if cls is None:
        raise _error("release-checkpoint-invalid", "native documentary fact names an unsupported type")
    payload = _mapping(tagged["value"], {item.name for item in fields(cls)}, "native documentary members")
    return cls(**{key: _load_native_document(item, root) for key, item in payload.items()})


def _native_packet_value(packet: Any, root: str) -> dict[str, Any]:
    from retained_full_gate_packet import RetainedNativeFullGatePacket
    from release_full_gate import NativeFullGateEvidence

    if type(packet) is not RetainedNativeFullGatePacket:
        raise _error("release-checkpoint-invalid", "native N requires the original typed Full Gate packet")
    retained = packet.retained_candidate
    return {
        "artifact_root": _native_document_value(packet.artifact_root, root),
        "descriptor_path": _native_document_value(retained.descriptor_path, root),
        "descriptor_sha256": _sha256(retained.descriptor_sha256, "native packet descriptor digest"),
        "package_root": _native_document_value(retained.package_evidence.view.package_root, root),
        "sidecar_path": _native_document_value(retained.package_evidence.receipt_path, root),
        "sidecar_sha256": _sha256(retained.package_evidence.receipt_sha256, "native packet sidecar digest"),
        "suite": _dump_dataclass(packet.suite, PortableSuiteGateEvidence, "native N Unit"),
        "build": _dump_dataclass(packet.build, PortableImageBuildEvidence, "native N build"),
        "verification": _dump_dataclass(packet.verification, PortableImageVerificationEvidence, "native N image"),
        "e2e": _dump_dataclass(packet.e2e, PortableCandidateE2EGateEvidence, "native N E2E"),
        "evidence": _dump_dataclass(packet.evidence, NativeFullGateEvidence, "native N Full Gate"),
    }


def _load_native_packet(value: Any, root: str) -> Any:
    from retained_full_gate_packet import RetainedNativeFullGatePacket
    from release_retained_candidate import read_retained_candidate_identity
    from release_full_gate import NativeFullGateEvidence, verify_detached_native_full_gate_evidence

    payload = _mapping(value, {"artifact_root", "descriptor_path", "descriptor_sha256", "package_root", "sidecar_path", "sidecar_sha256",
                              "suite", "build", "verification", "e2e", "evidence"}, "native N packet")
    retained = read_retained_candidate_identity(
        _load_native_document(payload["descriptor_path"], root),
        expected_sha256=_sha256(payload["descriptor_sha256"], "native N descriptor digest"),
        package_root=_load_native_document(payload["package_root"], root),
        sidecar_path=_load_native_document(payload["sidecar_path"], root),
        expected_sidecar_sha256=_sha256(payload["sidecar_sha256"], "native N sidecar digest"),
    )
    packet = RetainedNativeFullGatePacket(
        _load_native_document(payload["artifact_root"], root), retained,
        _load_dataclass(payload["suite"], PortableSuiteGateEvidence, "native N Unit", tuple_fields=frozenset({"command", "coverage"})),
        _load_dataclass(payload["build"], PortableImageBuildEvidence, "native N build"),
        _load_dataclass(payload["verification"], PortableImageVerificationEvidence, "native N image"),
        _load_e2e(payload["e2e"], native=True),
        _load_dataclass(payload["evidence"], NativeFullGateEvidence, "native N Full Gate"),
    )
    verify_detached_native_full_gate_evidence(packet.artifact_root, packet.retained_candidate, packet.suite,
                                            packet.build, packet.verification, packet.e2e, packet.evidence)
    return packet


def read_direct_native_result_effects(raw: bytes, *, command: Any, action_run_id: str,
                                     state_generation: int) -> dict[str, dict[str, str]]:
    """Read D604's closed actual result; no result becomes execution authority."""

    from framework_installation_command import FrameworkInstallationCommandReceipt

    if type(command) is not FrameworkInstallationCommandReceipt or type(raw) is not bytes:
        raise _error("release-native-n-direct-result-invalid", "direct result requires the actual closed O200 command")
    payload = _canonical_input(raw)
    source = _mapping(payload, {"schema_version", "action_id", "action_run_id", "installation_command_sha256",
                               "package_manifest_sha256", "target_project_context_sha256", "state_generation",
                               "effect_outcome", "reason", "effects"}, "direct installation result")
    if (type(source["schema_version"]) is not int or source["schema_version"] != 1
            or source["action_id"] != "CA-O-200" or source["action_run_id"] != action_run_id
            or source["installation_command_sha256"] != command.sha256
            or source["package_manifest_sha256"] != command.package_manifest_sha256
            or source["target_project_context_sha256"] != command.target_project_context_sha256
            or type(source["state_generation"]) is not int or source["state_generation"] != state_generation
            or type(state_generation) is not int or state_generation < 1):
        raise _error("release-native-n-direct-result-invalid", "direct result differs from actual command or current generation")
    if source["effect_outcome"] != "completed":
        raise _error("release-native-n-direct-publication-unavailable", "subsequent installed-N discovery requires observed completed direct publication")
    if source["reason"] is not None and (not isinstance(source["reason"], str)
            or any(character in source["reason"] for character in ("\x00", "\n", "\r"))):
        raise _error("release-native-n-direct-result-invalid", "direct result reason is not governed")
    if not isinstance(source["effects"], list):
        raise _error("release-native-n-direct-result-invalid", "direct effects must be a closed list")
    kinds = {"package_selector", "runtime_selector", "release_proof", "package_manifest",
             "full_gate_receipt", "retained_candidate_descriptor", "retained_package_sidecar",
             "unit_gate_receipt", "build_receipt", "verification_receipt", "e2e_gate_receipt"}
    effects = {}
    references = set()
    for row in source["effects"]:
        effect = _mapping(row, {"kind", "reference", "sha256"}, "direct effect")
        kind = _text(effect["kind"], "direct effect kind")
        reference = _safe_path(effect["reference"], "direct effect reference")
        if kind not in kinds or kind in effects or reference in references:
            raise _error("release-native-n-direct-result-invalid", "direct effects contain an unknown or ambiguous association")
        effects[kind] = {"kind": kind, "reference": reference, "sha256": _sha256(effect["sha256"], "direct effect digest")}
        references.add(reference)
    expected = {
        "package_selector": ".caprmedio_install/current.toml",
        "runtime_selector": ".caprmedio_runtime/installation/current.toml",
        "release_proof": f".caprmedio_runtime/installation/generations/{state_generation}/release-proof.toml",
        "package_manifest": f".caprmedio_install/releases/{command.package_manifest_sha256}/manifest.toml",
    }
    if any(kind not in effects or effects[kind]["reference"] != reference for kind, reference in expected.items()):
        raise _error("release-native-n-direct-result-invalid", "direct publication effects do not address the exact current carriers")
    if "full_gate_receipt" in effects and effects["full_gate_receipt"]["sha256"] != command.full_gate_receipt_sha256:
        raise _error("release-native-n-direct-result-invalid", "direct result Full Gate differs from its actual command")
    return effects


def read_direct_native_result_packet(raw: bytes, *, project_root: str, command: Any,
                                    action_run_id: str, state_generation: int):
    """Reconstruct the original packet only from seven exact result effects."""

    from dataclasses import replace
    import json
    from native_selected_installation import _read
    from release_handoff import _file
    from release_retained_candidate import DESCRIPTOR_NAME, read_retained_candidate_identity
    from release_full_gate import NativeFullGateEvidence, verify_detached_native_full_gate_evidence
    from retained_full_gate_packet import RetainedNativeFullGatePacket

    root = Path(project_root)
    effects = read_direct_native_result_effects(raw, command=command, action_run_id=action_run_id, state_generation=state_generation)
    required = {"full_gate_receipt", "retained_candidate_descriptor", "retained_package_sidecar",
                "unit_gate_receipt", "build_receipt", "verification_receipt", "e2e_gate_receipt"}
    if not required <= effects.keys():
        raise _error("release-native-n-direct-packet-association-unavailable", "historical direct result lacks its exact original retained Full Gate associations")
    contents = {}
    for kind, effect in effects.items():
        payload = _read(_file(root, effect["reference"]), code="release-native-n-direct-carrier-invalid", mode=None)
        if hashlib.sha256(payload).hexdigest() != effect["sha256"]:
            raise _error("release-native-n-direct-carrier-invalid", "direct result effect carrier changed")
        contents[kind] = payload

    def receipt(kind, cls):
        document = json.loads(contents[kind])
        if cls is PortableCandidateE2EGateEvidence:
            observed = _load_e2e(document, native=True)
        else:
            tuples = frozenset({"command", "coverage"}) if cls is PortableSuiteGateEvidence else frozenset()
            observed = _load_dataclass(document, cls, kind, tuple_fields=tuples)
        if observed.receipt_sha256 is not None or canonical_json(asdict(observed)) != contents[kind]:
            raise _error("release-native-n-direct-carrier-invalid", "original constituent receipt is not closed canonical producer bytes")
        return replace(observed, receipt_sha256=effects[kind]["sha256"])

    gate = receipt("full_gate_receipt", NativeFullGateEvidence)
    suffix = Path(_safe_path(gate.evidence_root, "original aggregate evidence root")) / "receipt.json"
    gate_path = Path(effects["full_gate_receipt"]["reference"])
    if len(gate_path.parts) < len(suffix.parts) or gate_path.parts[-len(suffix.parts):] != suffix.parts:
        raise _error("release-native-n-direct-carrier-invalid", "aggregate association does not address its original evidence root")
    prefix = gate_path.parts[:-len(suffix.parts)]
    artifact_root = root.joinpath(*prefix)
    sidecar = root / effects["retained_package_sidecar"]["reference"]
    descriptor = root / effects["retained_candidate_descriptor"]["reference"]
    if (descriptor != sidecar.parent.parent / DESCRIPTOR_NAME
            or sidecar != artifact_root / _safe_path(gate.package_evidence_relpath, "original sidecar reference")
            or effects["retained_package_sidecar"]["sha256"] != gate.package_evidence_sha256
            or gate.package_manifest_sha256 != command.package_manifest_sha256):
        raise _error("release-native-n-direct-carrier-invalid", "original descriptor, sidecar and package relations differ")
    package_root = descriptor.parent / "package" / gate.package_manifest_sha256
    retained = read_retained_candidate_identity(descriptor,
        expected_sha256=effects["retained_candidate_descriptor"]["sha256"], package_root=package_root,
        sidecar_path=sidecar, expected_sidecar_sha256=gate.package_evidence_sha256)
    suite = receipt("unit_gate_receipt", PortableSuiteGateEvidence)
    build = receipt("build_receipt", PortableImageBuildEvidence)
    verification = receipt("verification_receipt", PortableImageVerificationEvidence)
    e2e = receipt("e2e_gate_receipt", PortableCandidateE2EGateEvidence)
    for kind, evidence in (("unit_gate_receipt", suite), ("build_receipt", build),
                           ("verification_receipt", verification), ("e2e_gate_receipt", e2e)):
        if root / effects[kind]["reference"] != artifact_root / _safe_path(evidence.evidence_root, "original constituent root") / "receipt.json":
            raise _error("release-native-n-direct-carrier-invalid", "constituent association differs from its exact retained root")
    packet = RetainedNativeFullGatePacket(artifact_root, retained, suite, build, verification, e2e, gate)
    verify_detached_native_full_gate_evidence(artifact_root, retained, suite, build, verification, e2e, gate)
    return packet


def _reopen_selected_native_promotion_completion(
    source: Mapping[str, Any], *, root: str, workflow_run_id: str, fingerprint: str,
    candidate: ValidatedCandidate, publication: NativePromotionEvidence,
) -> None:
    """Require the original selected O169 result and terminal Journal fact.

    This is deliberately limited to the completed promotion Action.  Native
    N discovery must not infer a future retirement terminal receipt merely to
    reopen an already-published predecessor.
    """

    import work_journal
    from release_handoff import _file
    from FIND_AND_FETCH_JOURNAL_EVENTS.find_and_fetch_journal_events import JournalQueryError, capture_snapshot, query

    # O164@9 had twelve phases, with O178/O169 promotion at index ten.
    # This documentary reader must not bind retained records to today's graph.
    promote_index = 10

    def historical_index(value: Any, label: str) -> int:
        if type(value) is not int or not 0 <= value < 12:
            raise _error("release-checkpoint-invalid", f"{label} is outside the retained O164@9 phase graph")
        return value
    context_rows = source.get("contexts")
    result_rows = source.get("results")
    recording_rows = source.get("shared_recordings")
    pending_rows = source.get("pending_recordings")
    if not all(isinstance(rows, list) for rows in (context_rows, result_rows, recording_rows, pending_rows)):
        raise _error("release-checkpoint-phase-mismatch", "historical native publication lacks selected Action records")

    def row_at(rows: list[Any], *, label: str, fields: set[str]) -> Mapping[str, Any]:
        matches = []
        for raw in rows:
            row = _mapping(raw, {"index", *fields}, f"historical native {label} record")
            if historical_index(row["index"], f"historical native {label} index") == promote_index:
                matches.append(row)
        if len(matches) != 1:
            raise _error("release-checkpoint-phase-mismatch", f"historical native publication lacks one promote {label}")
        return matches[0]

    context = _load_dataclass(
        row_at(context_rows, label="context", fields={"context"})["context"],
        SelectedReleaseActionContext, "historical native promotion context",
    )
    if (
        context.project_root != root or context.workflow_run_id != workflow_run_id
        or context.parent_workflow_run_id != workflow_run_id
        or context.parent_step_run_id != context.step_run_id
        or context.frozen_parameters_sha256 != fingerprint
        or context.workflow_atom_id != "CA-O-164"
        or type(context.workflow_version) is not int or context.workflow_version != 9
    ):
        raise _error("release-checkpoint-binding-mismatch", "historical native publication is not its frozen O164@9 Run")
    for name in ("step_run_id", "action_run_id"):
        _text(getattr(context, name), f"historical native context.{name}")
    if (context.step_atom_id, context.action_atom_id) != ("CA-O-178", "CA-O-169"):
        raise _error("release-checkpoint-phase-mismatch", "historical native publication is outside retained O178/O169 promotion")
    if context.action_run_id != publication.action_run_id:
        raise _error("release-checkpoint-binding-mismatch", "historical native publication names another selected O169 Action")
    result_payload = _mapping(
        row_at(result_rows, label="result", fields={"result"})["result"],
        {item.name for item in fields(ReleasePhaseResult)}, "historical native promotion result",
    )
    if result_payload["output"] != "promotion" or result_payload["shared_action_recording"] is not None:
        raise _error("release-checkpoint-phase-mismatch", "historical native promotion has another observation type")
    result = _load_dataclass(
        {**result_payload, "output": publication}, ReleasePhaseResult, "historical native promotion result",
        tuple_fields=frozenset({"attempted_effects", "effect_evidence_refs", "declared_run_receipt_refs"}),
    )
    if (
        result.workflow_run_id != context.workflow_run_id or result.step_run_id != context.step_run_id
        or result.action_run_id != context.action_run_id or result.step_atom_id != "CA-O-178"
        or result.action_atom_id != "CA-O-169" or result.phase != "promote"
        or result.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
        or result.recording_state != "shared_session_provider_pending"
        or result.outcome != "completed" or result.output != publication
    ):
        raise _error("release-checkpoint-phase-mismatch", "historical native publication lacks its completed O169 observation")
    recording = row_at(recording_rows, label="shared recording", fields={"terminal_outcome", "receipt_refs"})
    if recording["terminal_outcome"] != "completed":
        raise _error("release-checkpoint-phase-mismatch", "historical native publication has no completed shared Action receipt")
    refs = recording.get("receipt_refs")
    if not isinstance(refs, list) or len(refs) != 1:
        raise _error("release-checkpoint-phase-mismatch", "historical native publication has an ambiguous shared Action receipt")
    terminal_event_id = _text(refs[0], "historical native promotion terminal receipt")
    for raw in pending_rows:
        pending = _mapping(raw, {"index", "event_id", "event_outcome"}, "historical native pending recording")
        if historical_index(pending["index"], "historical native pending index") == promote_index:
            raise _error("release-checkpoint-phase-mismatch", "historical native publication has pending terminal evidence")

    expected_requested_action = f"{workflow_run_id}:step:{promote_index + 1}:action:1"
    expected_result_ref = (
        f".caprmedio_install/workflow_orchestrator/runs/{workflow_run_id}/{expected_requested_action}.json"
    )
    project = Path(root)
    try:
        progress_raw = _file(project, expected_result_ref).read_bytes()
        progress = json.loads(progress_raw)
    except (OSError, ValueError, ReleaseContractError) as error:
        raise _error("release-checkpoint-binding-mismatch", "historical native publication result carrier is unavailable") from error
    if (
        not isinstance(progress, dict)
        or progress_raw != canonical_json(progress)
        or set(progress) != {"result", "action_run_id", "effect_refs", "native_result", "compiler_publication_recording"}
        or not isinstance(progress["result"], str) or not progress["result"]
        or progress["action_run_id"] != context.action_run_id
        or progress["effect_refs"] != list(result.effect_evidence_refs)
        or progress["native_result"] != json.loads(canonical_json(asdict(result)))
    ):
        raise _error("release-checkpoint-binding-mismatch", "historical native publication result differs from the retained O169 observation")

    try:
        snapshot = capture_snapshot(project)
        if snapshot.get("source_root") != work_journal.configured_journal_root(project).as_posix():
            raise _error("release-checkpoint-binding-mismatch", "historical native publication has another canonical Journal root")
        observed = query(snapshot, {
            "mode": "full_events",
            "filter": '"event:/run/run_id" = ' + json.dumps(context.action_run_id),
            "limit": 3,
        })
    except JournalQueryError as error:
        raise _error("release-checkpoint-binding-mismatch", "historical native publication Journal coverage is unavailable") from error
    if (observed.get("status") != "complete" or observed.get("coverage", {}).get("complete") is not True
            or len(observed.get("results", [])) != 2):
        raise _error("release-checkpoint-binding-mismatch", "historical native publication Journal pair is absent or ambiguous")
    events: dict[str, dict[str, Any]] = {}
    for row in observed["results"]:
        event = work_journal.validate_sealed_event(row["event"])
        event_id = event.get("event_id")
        if not isinstance(event_id, str) or event_id in events:
            raise _error("release-checkpoint-binding-mismatch", "historical native publication Journal pair is ambiguous")
        events[event_id] = event
    if set(events) != {publication.action_start_event_id, terminal_event_id}:
        raise _error("release-checkpoint-binding-mismatch", "historical native publication has another Action start or terminal receipt")
    started, terminal = events[publication.action_start_event_id], events[terminal_event_id]
    run = started.get("run")
    definition = run.get("definition") if isinstance(run, Mapping) else None
    if (
        started.get("event") != "started" or started.get("outcome") is not None
        or started.get("action_id") != "CA-O-169" or not isinstance(run, Mapping)
        or run.get("run_id") != context.action_run_id or run.get("kind") != "action"
        or run.get("parent_run_id") != context.step_run_id or not isinstance(definition, Mapping)
        or definition.get("atom_id") != "CA-O-169" or definition.get("version") != 5
        or {"kind": "action", **definition} not in started.get("definition_bindings", [])
    ):
        raise _error("release-checkpoint-binding-mismatch", "historical native publication start differs from selected O169")
    preserved = (
        "schema_version", "kind", "action_id", "author", "llm_session", "structural_scope", "initiative",
        "run", "definition_bindings", "input_ref", "redaction",
    )
    if (
        any(terminal.get(key) != started.get(key) for key in preserved)
        or terminal.get("event") != "completed" or terminal.get("outcome") != "completed"
        or terminal.get("result_ref") != expected_result_ref
        or terminal.get("effect_refs") != list(result.effect_evidence_refs)
        or terminal.get("report_ref") is not None
    ):
        raise _error("release-checkpoint-binding-mismatch", "historical native publication terminal differs from its selected O169 result")


def read_native_checkpoint_packet(payload: Mapping[str, Any], *, project_root: str,
                                  expected_request: Any, expected_workflow_run_id: str):
    """Read historical packet transport without reviving execution authority.

    A subsequent Release may have changed checkout sources.  Installed N is
    therefore attested by the original retained descriptor, package and gate,
    not by rebuilding its source frontier or selecting a recent checkpoint.
    The caller must separately reopen the current native selected generation.
    """

    from dataclasses import replace
    from release_handoff import _file
    from release_full_gate import NativeFullGateEvidence
    from release_retained_candidate import encode_retained_candidate_descriptor, read_retained_candidate_identity
    from retained_full_gate_packet import RetainedNativeFullGatePacket

    source, _helper_binding = _native_checkpoint_envelope(dict(payload), "native historical checkpoint")
    request = _load_model(source["request"], ReleaseVersionRequest, "native historical request")
    expected = ReleaseVersionRequest.model_validate(expected_request)
    if (source["schema"] not in {NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA, LEGACY_NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA} or source["kind"] != "release_action_run"
            or source["sha256"] != release_action_checkpoint_sha256(source)
            or source["project_root"] != project_root or request.project_root != project_root
            or source["workflow_run_id"] != expected_workflow_run_id
            or request != expected or source["frozen_parameters_sha256"] != _fingerprint(request)):
        raise _error("release-checkpoint-binding-mismatch", "historical native packet belongs to another sealed Run")
    state = _mapping(source["state"], set(_NATIVE_STATE_NAMES), "native historical state")
    candidate_payload = state["candidate"]
    required = {"project_root", "manifest", "authority", "intent"}
    if isinstance(candidate_payload, dict) and "native_installed_n" in candidate_payload:
        required.add("native_installed_n")
    candidate_payload = _mapping(candidate_payload, required, "native historical candidate")
    manifest = _load_model(candidate_payload["manifest"], CandidateSnapshotManifest, "native historical manifest")
    authority = _load_model(candidate_payload["authority"], SealedAuthority, "native historical authority")
    intent = _load_model(candidate_payload["intent"], CandidateBuildRequest, "native historical intent")
    if (candidate_payload["project_root"] != project_root or manifest != request.candidate_snapshot_manifest
            or authority.expected_candidate_snapshot_manifest_sha256 != manifest.sha256
            or authority.executing_release != manifest.executing_release
            or authority.candidate_release != manifest.candidate_release
            or intent.candidate_release != manifest.candidate_release):
        raise _error("release-checkpoint-binding-mismatch", "historical packet differs from its frozen candidate")
    candidate = ValidatedCandidate(project_root, manifest, authority, intent)
    package_payload = _mapping(state["prepared_portable_package"], {
        "candidate_run_id", "candidate_snapshot_manifest_sha256", "input_manifest_sha256", "package_manifest_sha256",
    }, "native historical package")
    full = _load_dataclass(state["full_gate"], NativeFullGateEvidence, "native historical Full Gate")
    publication = _load_dataclass(state["promotion"], NativePromotionEvidence, "native historical publication",
                                  tuple_fields=frozenset({"effect_refs"}))
    if (publication.outcome != "promoted" or publication.receipt_sha256 is None
            or full.candidate_snapshot_manifest_sha256 != manifest.sha256
            or publication.candidate_snapshot_manifest_sha256 != manifest.sha256
            or publication.full_gate_receipt_sha256 != full.receipt_sha256
            or publication.package_manifest_sha256 != full.package_manifest_sha256
            or package_payload["candidate_snapshot_manifest_sha256"] != manifest.sha256
            or package_payload["package_manifest_sha256"] != full.package_manifest_sha256
            or package_payload["candidate_run_id"] != full.candidate_run_id
            or package_payload["input_manifest_sha256"] != full.input_manifest_sha256):
        raise _error("release-checkpoint-binding-mismatch", "historical packet lacks exact observed publication")
    _reopen_selected_native_promotion_completion(
        source, root=project_root, workflow_run_id=expected_workflow_run_id,
        fingerprint=_fingerprint(request), candidate=candidate, publication=publication,
    )
    package = reopen_portable_release_package(project_root, full.candidate_run_id, full.package_manifest_sha256)
    sidecar = _file(Path(project_root), full.package_evidence_relpath)
    retained = read_retained_candidate_identity(
        sidecar.parent.parent / "candidate-snapshot.json",
        expected_sha256=hashlib.sha256(encode_retained_candidate_descriptor(manifest)).hexdigest(),
        package_root=package.root, sidecar_path=sidecar,
        expected_sidecar_sha256=full.package_evidence_sha256,
    )
    packet = RetainedNativeFullGatePacket(
        Path(project_root), retained,
        _load_dataclass(state["portable_suite"], PortableSuiteGateEvidence, "native historical Unit", tuple_fields=frozenset({"command", "coverage"})),
        _load_dataclass(state["build"], PortableImageBuildEvidence, "native historical build"),
        _load_dataclass(state["verification"], PortableImageVerificationEvidence, "native historical image"),
        _load_e2e(state["e2e"], native=True), full,
    )
    packet = _load_native_packet(_native_packet_value(packet, project_root), project_root)
    prefix = f".caprmedio_runtime/release_promotion/{manifest.sha256}/observations/attempt-"
    if not publication.evidence_root.startswith(prefix) or "/" in publication.evidence_root.removeprefix(prefix):
        raise _error("release-checkpoint-binding-mismatch", "historical publication observation path is not canonical")
    raw = _file(Path(project_root), f"{publication.evidence_root}/receipt.json").read_bytes()
    if (hashlib.sha256(raw).hexdigest() != publication.receipt_sha256
            or raw != canonical_json(asdict(replace(publication, receipt_sha256=None)))):
        raise _error("release-checkpoint-binding-mismatch", "historical publication observation changed")
    return packet, publication


def _native_n_value(binding: Any, root: str) -> dict[str, Any]:
    from release_handoff import NativeInstalledNBinding

    if type(binding) is not NativeInstalledNBinding:
        raise _error("release-checkpoint-invalid", "native N binding must be concrete typed facts")
    return {"package": _native_document_value(binding.verified_package, root),
            "packet": _native_packet_value(binding.full_gate_packet, root),
            "selected": _native_document_value(binding.selected, root)}


def _load_native_n(value: Any, root: str, *, historical: bool = False) -> Any:
    from release_handoff import NativeInstalledNBinding, reopen_native_installed_n
    from framework_package import VerifiedFrameworkPackage, verify_framework_package
    from native_selected_installation import NativeSelectedInstallation
    from installed_mcp_binding import InstalledMcpBinding

    payload = _mapping(value, {"package", "packet", "selected"}, "native N binding")
    binding = NativeInstalledNBinding(_load_native_document(payload["package"], root),
                                     _load_native_packet(payload["packet"], root),
                                     _load_native_document(payload["selected"], root))
    if not historical:
        return reopen_native_installed_n(root, binding)
    # Historical data is documentary only.  Post-cut-over state verifies it
    # against retained N+1 publication below; it never calls it current N.
    retained = binding.full_gate_packet.retained_candidate.package_evidence.view
    package = binding.verified_package
    actual_package = verify_framework_package(retained.package_root)
    selected = binding.selected
    if (type(package) is not VerifiedFrameworkPackage or type(selected) is not NativeSelectedInstallation
            or type(selected.binding) is not InstalledMcpBinding
            or package.manifest_digest != retained.actual_package_manifest_sha256
            or package.inventory != actual_package.inventory
            or package.binding_atoms != actual_package.binding_atoms
            or package.framework_version != retained.framework_version
            or package.version_toml_sha256 != retained.version_toml_sha256
            or package.source_catalog_sha256 != retained.source_catalog_sha256
            or package.root != Path(root) / ".caprmedio_install/releases" / package.manifest_digest
            or selected.package_manifest_sha256 != package.manifest_digest
            or selected.framework_version != package.framework_version
            or selected.version_toml_sha256 != package.version_toml_sha256
            or selected.source_catalog_sha256 != package.source_catalog_sha256
            or selected.full_gate_receipt_sha256 != binding.full_gate_packet.evidence.receipt_sha256
            or "sha256:" + selected.image_digest != binding.full_gate_packet.evidence.candidate_image_digest
            or selected.binding.package_root != package.root
            or selected.binding.package_manifest_sha256 != package.manifest_digest
            or selected.binding.runtime_selector_sha256 != selected.selector_sha256):
        raise _error("release-checkpoint-binding-mismatch", "documentary native N differs from its original retained package")
    return binding


def _preflight_value(value: ReleaseCompilationPreflight) -> dict[str, Any]:
    if type(value) is not ReleaseCompilationPreflight:
        raise _error("release-checkpoint-invalid", "preflight is not typed state")
    if any(not isinstance(path, str) or not isinstance(contents, bytes) for path, contents in value.output_files.items()):
        raise _error("release-checkpoint-invalid", "preflight output files are not typed bytes")
    return {
        "candidate_release": value.candidate_release,
        "framework_version": value.framework_version,
        "version_toml_sha256": value.version_toml_sha256,
        "expected_derived_source_copy_sha256": value.expected_derived_source_copy_sha256,
        "expected_compiled_output_sha256": value.expected_compiled_output_sha256,
        "compiler_entrypoint": _dump_model(value.compiler_entrypoint, CompilerEntrypoint, "preflight.compiler_entrypoint"),
        "canonical_source_snapshot_digest": value.canonical_source_snapshot_digest,
        "compiler_frontier_digest": value.compiler_frontier_digest,
        "nested_source_recursive_sha256_before": value.nested_source_recursive_sha256_before,
        "output_files": [
            {"path": _safe_path(path, "preflight.output_files.path"), "bytes": _json_value(contents, "preflight.output_files.bytes")}
            for path, contents in sorted(value.output_files.items())
        ],
        "child_manifest_bytes": _json_value(value.child_manifest_bytes, "preflight.child_manifest_bytes"),
    }


def _load_preflight(value: Any, candidate: ValidatedCandidate) -> ReleaseCompilationPreflight:
    payload = _mapping(value, {
        "candidate_release", "framework_version", "version_toml_sha256",
        "expected_derived_source_copy_sha256", "expected_compiled_output_sha256",
        "compiler_entrypoint", "canonical_source_snapshot_digest", "compiler_frontier_digest",
        "nested_source_recursive_sha256_before", "output_files", "child_manifest_bytes",
    }, "preflight")
    if not isinstance(payload["output_files"], list):
        raise _error("release-checkpoint-invalid", "preflight.output_files must be a list")
    output_files: dict[str, bytes] = {}
    previous = None
    for item in payload["output_files"]:
        entry = _mapping(item, {"path", "bytes"}, "preflight.output_file")
        path = _safe_path(entry["path"], "preflight.output_file.path")
        if previous is not None and path <= previous:
            raise _error("release-checkpoint-invalid", "preflight output files are not uniquely canonical ordered")
        previous = path
        output_files[path] = _bytes(entry["bytes"], "preflight.output_file.bytes")
    try:
        preflight = ReleaseCompilationPreflight(
            candidate_release=_text(payload["candidate_release"], "preflight.candidate_release"),
            framework_version=_text(payload["framework_version"], "preflight.framework_version"),
            version_toml_sha256=_sha256(payload["version_toml_sha256"], "preflight.version_toml_sha256"),
            expected_derived_source_copy_sha256=_sha256(payload["expected_derived_source_copy_sha256"], "preflight.expected_derived_source_copy_sha256"),
            expected_compiled_output_sha256=_sha256(payload["expected_compiled_output_sha256"], "preflight.expected_compiled_output_sha256"),
            compiler_entrypoint=_load_model(payload["compiler_entrypoint"], CompilerEntrypoint, "preflight.compiler_entrypoint"),
            canonical_source_snapshot_digest=_sha256(payload["canonical_source_snapshot_digest"], "preflight.canonical_source_snapshot_digest"),
            compiler_frontier_digest=_sha256(payload["compiler_frontier_digest"], "preflight.compiler_frontier_digest"),
            nested_source_recursive_sha256_before=_sha256(payload["nested_source_recursive_sha256_before"], "preflight.nested_source_recursive_sha256_before"),
            output_files=output_files,
            child_manifest_bytes=_bytes(payload["child_manifest_bytes"], "preflight.child_manifest_bytes"),
        )
    except (TypeError, ValueError) as error:
        raise _error("release-checkpoint-invalid", "preflight cannot construct typed state") from error
    manifest = candidate.manifest
    if (
        preflight.candidate_release != manifest.candidate_release
        or preflight.framework_version != manifest.framework_version
        or preflight.version_toml_sha256 != manifest.version_toml_sha256
        or preflight.expected_derived_source_copy_sha256 != manifest.expected_derived_source_copy_sha256
        or preflight.expected_compiled_output_sha256 != manifest.expected_compiled_output_sha256
        or preflight.canonical_source_snapshot_digest != manifest.canonical_source_snapshot_digest
        or preflight.compiler_frontier_digest != candidate.authority.source_frontier_digest
        or preflight.nested_source_recursive_sha256_before != manifest.nested_source_recursive_sha256_before
    ):
        raise _error("release-checkpoint-binding-mismatch", "preflight is not exactly candidate-bound")
    return preflight


def _tag(name: str, value: Any) -> dict[str, Any]:
    if name not in _STATE_NAMES:
        raise _error("release-checkpoint-invalid", "checkpoint has an unknown state tag")
    if name == "candidate":
        payload = _candidate_value(value)
    elif name == "preflight":
        payload = _preflight_value(value)
    elif name == "source_copy":
        if type(value) is not SealedSourceCopy:
            raise _error("release-checkpoint-invalid", "source_copy is not typed state")
        payload = {
            "candidate": _candidate_value(value.candidate),
            "source_copy_root": _safe_path(value.source_copy_root, "source_copy.source_copy_root"),
            "actual_derived_source_copy_sha256": _sha256(value.actual_derived_source_copy_sha256, "source_copy.actual_derived_source_copy_sha256"),
        }
    elif name in {"compilation"}:
        payload = _dump_model(value, SealedCandidateCompilation, name)
    elif name == "package":
        payload = _package_value(value)
    else:
        payload = _dump_dataclass(value, _tagged_type(name), name)
    return {"tag": name, "value": payload}


def _package_value(value: Any) -> dict[str, Any]:
    if type(value) is not dict:
        raise _error("release-checkpoint-invalid", "package is not a typed package result")
    required = {"staged", "verified", "candidate_snapshot_manifest_sha256", "release_root", "file_count"}
    payload = _mapping(value, required, "package")
    if type(payload["staged"]) is not bool or payload["verified"] is not True or type(payload["file_count"]) is not int or payload["file_count"] < 0:
        raise _error("release-checkpoint-invalid", "package result has invalid closed values")
    return {
        "staged": payload["staged"],
        "verified": True,
        "candidate_snapshot_manifest_sha256": _sha256(payload["candidate_snapshot_manifest_sha256"], "package.candidate_snapshot_manifest_sha256"),
        "release_root": _safe_path(payload["release_root"], "package.release_root"),
        "file_count": payload["file_count"],
    }


def _load_e2e(value: Any, *, native: bool = False) -> CandidateE2EGateEvidence:
    """Restore nested host-E2E receipts as their closed dataclass types."""

    cls = PortableCandidateE2EGateEvidence if native else CandidateE2EGateEvidence
    required = {item.name for item in fields(cls)}
    payload = _mapping(value, required, "e2e")
    rows = payload["harness_receipts"]
    if not isinstance(rows, list):
        raise _error("release-checkpoint-invalid", "e2e.harness_receipts must be a list")
    restored_rows = tuple(
        _load_dataclass(row, HarnessReceipt, "e2e.harness_receipt", tuple_fields=frozenset({"argv"}))
        for row in rows
    )
    restored = dict(payload)
    restored["harness_receipts"] = restored_rows
    try:
        return cls(**restored)
    except (TypeError, ValueError) as error:
        raise _error("release-checkpoint-invalid", "e2e cannot construct typed state") from error


def _load_tag(value: Any, candidate: ValidatedCandidate | None, root: str) -> tuple[str, Any]:
    tagged = _mapping(value, {"tag", "value"}, "tagged state")
    name = _text(tagged["tag"], "tagged state.tag")
    if name not in _STATE_NAMES:
        raise _error("release-checkpoint-invalid", "checkpoint names an unsupported typed state")
    if name == "candidate":
        return name, _load_candidate(tagged["value"], root)
    if candidate is None:
        raise _error("release-checkpoint-binding-mismatch", f"{name} appears before its sealed candidate")
    if name == "preflight":
        return name, _load_preflight(tagged["value"], candidate)
    if name == "source_copy":
        payload = _mapping(tagged["value"], {"candidate", "source_copy_root", "actual_derived_source_copy_sha256"}, "source_copy")
        restored_candidate = _load_candidate(payload["candidate"], root)
        source_copy = SealedSourceCopy(
            restored_candidate,
            _safe_path(payload["source_copy_root"], "source_copy.source_copy_root"),
            _sha256(payload["actual_derived_source_copy_sha256"], "source_copy.actual_derived_source_copy_sha256"),
        )
        if source_copy.candidate != candidate or source_copy.actual_derived_source_copy_sha256 != candidate.manifest.expected_derived_source_copy_sha256:
            raise _error("release-checkpoint-binding-mismatch", "source copy is not exactly candidate-bound")
        return name, source_copy
    if name == "compilation":
        restored = _load_model(tagged["value"], SealedCandidateCompilation, "compilation")
        if (restored.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
                or restored.authority != candidate.authority
                or restored.framework_version != candidate.manifest.framework_version
                or restored.version_toml_sha256 != candidate.manifest.version_toml_sha256):
            raise _error("release-checkpoint-binding-mismatch", "compilation is not exactly candidate-bound")
        return name, restored
    if name == "package":
        package = _package_value(tagged["value"])
        if package["candidate_snapshot_manifest_sha256"] != candidate.manifest.sha256:
            raise _error("release-checkpoint-binding-mismatch", "package is not exactly candidate-bound")
        return name, package
    cls = _tagged_type(name)
    tuples = {
        "suite": frozenset({"command", "coverage"}),
        "retirement": frozenset({"retaining_container_refs", "observed_rollback_refs", "required_rollback_refs"}),
    }.get(name, frozenset())
    if name == "e2e":
        restored = _load_e2e(tagged["value"])
    else:
        restored = _load_dataclass(tagged["value"], cls, name, tuple_fields=tuples)
    if getattr(restored, "candidate_snapshot_manifest_sha256", None) != candidate.manifest.sha256:
        raise _error("release-checkpoint-binding-mismatch", f"{name} is not exactly candidate-bound")
    return name, restored


def _context_value(context: SelectedReleaseActionContext) -> dict[str, Any]:
    if type(context) is not SelectedReleaseActionContext:
        raise _error("release-checkpoint-invalid", "context is not selected typed state")
    return _dump_dataclass(context, SelectedReleaseActionContext, "context")


# Checkpoints preserve the selected Workflow definition recorded when the Run
# began.  Retain the immediately preceding O164 revision for status/recovery,
# but reject an unknown revision rather than silently rebinding it.
_SUPPORTED_RELEASE_WORKFLOW_VERSIONS = frozenset({5, 6, 9, 11})


def _load_context(value: Any, index: int, *, root: str, workflow_run_id: str, fingerprint: str) -> SelectedReleaseActionContext:
    context = _load_dataclass(value, SelectedReleaseActionContext, "context")
    if (
        context.project_root != root
        or context.workflow_run_id != workflow_run_id
        or context.parent_workflow_run_id != workflow_run_id
        or context.parent_step_run_id != context.step_run_id
        or context.frozen_parameters_sha256 != fingerprint
        or context.workflow_atom_id != "CA-O-164"
        or type(context.workflow_version) is not int
        or context.workflow_version not in _SUPPORTED_RELEASE_WORKFLOW_VERSIONS
    ):
        raise _error("release-checkpoint-binding-mismatch", "context does not belong to the frozen selected Run")
    for name, identity in (("step_run_id", context.step_run_id), ("action_run_id", context.action_run_id)):
        _text(identity, f"context.{name}")
    step, action, _phase = PHASES[index]
    if (context.step_atom_id, context.action_atom_id) != (step, action):
        raise _error("release-checkpoint-phase-mismatch", "context Step/Action is outside its selected phase")
    return context


def _result_value(result: ReleasePhaseResult) -> dict[str, Any]:
    if type(result) is not ReleasePhaseResult:
        raise _error("release-checkpoint-invalid", "phase result is not typed state")
    # ``asdict`` would recursively expand the typed ``output`` evidence before
    # this codec can apply its closed tag.  Copy every other exact dataclass
    # member directly, so the output has one and only one admitted encoding.
    payload = {
        item.name: _json_value(getattr(result, item.name), f"result.{item.name}")
        for item in fields(ReleasePhaseResult)
        if item.name != "output"
    }
    output = result.output
    if output is None:
        payload["output"] = None
        return payload
    matching = [name for name, cls in _TAGGED_TYPES.items() if type(output) is cls]
    if not matching and type(output) is _full_gate_type():
        matching = ["full_gate"]
    if len(matching) != 1:
        raise _error("release-checkpoint-invalid", "phase result output is not an admitted typed Release observation")
    payload["output"] = _tag(matching[0], output)
    return payload


def _shared_recording(value: Any, label: str) -> dict[str, str] | None:
    """Validate the one current closed retirement-recording handoff.

    This is deliberately a packet for the shared recorder, not its durable
    receipt.  The checkpoint keeps it only so recovery can request that same
    recorder action without inventing or broadening the private Release Run.
    """

    if value is None:
        return None
    packet = _mapping(value, {
        "on_recorded_result", "candidate_snapshot_manifest_sha256", "prior_image_digest",
        "retirement_receipt_ref", "retirement_receipt_sha256",
    }, label)
    return {
        "on_recorded_result": _text(packet["on_recorded_result"], f"{label}.on_recorded_result"),
        "candidate_snapshot_manifest_sha256": _sha256(packet["candidate_snapshot_manifest_sha256"], f"{label}.candidate_snapshot_manifest_sha256"),
        "prior_image_digest": _text(packet["prior_image_digest"], f"{label}.prior_image_digest"),
        "retirement_receipt_ref": _safe_path(packet["retirement_receipt_ref"], f"{label}.retirement_receipt_ref"),
        "retirement_receipt_sha256": _sha256(packet["retirement_receipt_sha256"], f"{label}.retirement_receipt_sha256"),
    }


def _load_result(value: Any, index: int, context: SelectedReleaseActionContext, candidate: ValidatedCandidate) -> ReleasePhaseResult:
    required = {item.name for item in fields(ReleasePhaseResult)}
    payload = _mapping(value, required, "result")
    output = payload["output"]
    restored_output = None
    if output is not None:
        tag, restored_output = _load_tag(output, candidate, candidate.project_root)
        expected = _PHASE_STATE[PHASES[index][2]]
        if tag != expected:
            raise _error("release-checkpoint-phase-mismatch", "phase result output has an invalid observation type")
    copied = dict(payload)
    copied["output"] = restored_output
    if "shared_action_recording" in copied:
        copied["shared_action_recording"] = _shared_recording(copied["shared_action_recording"], "result.shared_action_recording")
    result = _load_dataclass(copied, ReleasePhaseResult, "result", tuple_fields=frozenset({"attempted_effects", "effect_evidence_refs", "declared_run_receipt_refs"}))
    step, action, phase = PHASES[index]
    if (
        result.workflow_run_id != context.workflow_run_id
        or result.step_run_id != context.step_run_id
        or result.action_run_id != context.action_run_id
        or result.step_atom_id != step
        or result.action_atom_id != action
        or result.phase != phase
        or result.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
        or result.recording_state != "shared_session_provider_pending"
        or result.outcome not in {"prepared", "completed", "blocked", "failed", "pending", "effect_uncertain"}
    ):
        raise _error("release-checkpoint-phase-mismatch", "result does not match its selected phase context")
    if result.output is not None and result.output != restored_output:
        raise _error("release-checkpoint-invalid", "result output was not reconstructed exactly")
    if result.shared_action_recording is not None:
        packet = _shared_recording(result.shared_action_recording, "result.shared_action_recording")
        if (
            index != len(PHASES) - 1
            or result.phase != "retire"
            or result.outcome != "pending"
            or result.effect_outcome != "retired"
            or packet["candidate_snapshot_manifest_sha256"] != candidate.manifest.sha256
            or not isinstance(result.output, ImageRetirementEvidence)
            or packet["prior_image_digest"] != result.output.prior_image_digest
            or packet["retirement_receipt_sha256"] != result.output.receipt_sha256
            or packet["retirement_receipt_ref"] != f"{result.output.evidence_root}/receipt.json"
        ):
            raise _error("release-checkpoint-phase-mismatch", "shared recording handoff is not the exact terminal retirement packet")
    return result


def _canonical_input(value: bytes | str) -> dict[str, Any]:
    raw = value if isinstance(value, bytes) else value.encode("utf-8") if isinstance(value, str) else None
    if raw is None:
        raise _error("release-checkpoint-invalid", "checkpoint must be canonical JSON bytes or text")
    try:
        decoded = json.loads(raw.decode("utf-8"), parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    except (UnicodeDecodeError, ValueError, TypeError) as error:
        raise _error("release-checkpoint-invalid", "checkpoint is not valid canonical JSON") from error
    if not isinstance(decoded, dict) or canonical_json(decoded) != raw:
        raise _error("release-checkpoint-invalid", "checkpoint JSON is not canonical and closed")
    return decoded


# ``_load_state`` needs two values before it can restore later fields.  Keeping
# that state local avoids a global registry or provider side channel.
class _StateReader:
    def __init__(self, root: str) -> None:
        self.root = root
        self.candidate: ValidatedCandidate | None = None

    def read(self, name: str, value: Any) -> Any:
        if value is None:
            return None
        tag, restored = _load_tag(value, self.candidate, self.root)
        if tag != name:
            raise _error("release-checkpoint-invalid", "state field tag does not match its fixed field")
        if name == "candidate":
            self.candidate = restored
        return restored


def _state_value(run: ReleaseActionRun, name: str) -> Any:
    value = getattr(run, name)
    return None if value is None else _tag(name, value)


def _validate_state_dependencies(state: dict[str, Any], candidate: ValidatedCandidate | None, preflight: ReleaseCompilationPreflight | None) -> None:
    if (candidate is None) != (preflight is None):
        raise _error("release-checkpoint-phase-mismatch", "candidate and preflight must be retained together")
    if candidate is None:
        if any(state[name] is not None for name in _STATE_NAMES[2:]):
            raise _error("release-checkpoint-phase-mismatch", "post-freeze evidence lacks the frozen candidate")
        return
    source_copy = state["source_copy"]
    compilation = state["compilation"]
    suite = state["suite"]
    package = state["package"]
    build = state["build"]
    verification = state["verification"]
    e2e = state["e2e"]
    full_gate = state["full_gate"]
    promotion = state["promotion"]
    retirement = state["retirement"]
    if source_copy is None and any(value is not None for value in (compilation, suite, package, build, verification, e2e, full_gate, promotion, retirement)):
        raise _error("release-checkpoint-phase-mismatch", "post-delivery evidence lacks the retained source copy")
    if compilation is None and any(value is not None for value in (suite, package, build, verification, e2e, full_gate, promotion, retirement)):
        raise _error("release-checkpoint-phase-mismatch", "post-compilation evidence lacks compilation")
    if suite is None and any(value is not None for value in (package, build, verification, e2e, full_gate, promotion, retirement)):
        raise _error("release-checkpoint-phase-mismatch", "post-suite evidence lacks suite evidence")
    if package is None and any(value is not None for value in (build, verification, e2e, full_gate, promotion, retirement)):
        raise _error("release-checkpoint-phase-mismatch", "image evidence lacks candidate package staging")
    if build is None and any(value is not None for value in (verification, e2e, full_gate, promotion, retirement)):
        raise _error("release-checkpoint-phase-mismatch", "later evidence lacks image build evidence")
    if verification is None and any(value is not None for value in (e2e, full_gate, promotion, retirement)):
        raise _error("release-checkpoint-phase-mismatch", "later evidence lacks candidate verification")
    if e2e is None and any(value is not None for value in (full_gate, promotion, retirement)):
        raise _error("release-checkpoint-phase-mismatch", "later evidence lacks host candidate E2E evidence")
    if full_gate is None and any(value is not None for value in (promotion, retirement)):
        raise _error("release-checkpoint-phase-mismatch", "later evidence lacks aggregate full-gate evidence")
    if promotion is not None and (not e2e.passed or not full_gate.passed):
        raise _error("release-checkpoint-phase-mismatch", "promotion lacks passing host E2E and aggregate evidence")
    if full_gate is not None and (
        full_gate.phase_map_sha256 != suite.phase_map_sha256
        or full_gate.phase_map_sha256 != e2e.phase_map_sha256
        or full_gate.candidate_image_digest != build.candidate_image_digest
        or full_gate.candidate_image_digest != verification.candidate_image_digest
        or full_gate.candidate_image_digest != e2e.candidate_image_digest
        or full_gate.suite_receipt_sha256 != suite.receipt_sha256
        or full_gate.build_receipt_sha256 != build.receipt_sha256
        or full_gate.image_receipt_sha256 != verification.receipt_sha256
        or full_gate.e2e_receipt_sha256 != e2e.receipt_sha256
    ):
        raise _error("release-checkpoint-binding-mismatch", "aggregate differs from its exact retained predecessor receipts")
    if promotion is None and retirement is not None:
        raise _error("release-checkpoint-phase-mismatch", "retirement evidence lacks promotion evidence")


def _validate_phase_continuity(
    *, next_phase: int, stopped: bool, in_progress: SelectedReleaseActionContext | None,
    contexts: dict[int, SelectedReleaseActionContext], results: dict[int, ReleasePhaseResult],
) -> None:
    if next_phase < 0 or next_phase > len(PHASES):
        raise _error("release-checkpoint-phase-mismatch", "next phase is outside the selected Workflow")
    completed = set(range(next_phase))
    if set(results) - (completed | ({next_phase} if next_phase < len(PHASES) else set())):
        raise _error("release-checkpoint-phase-mismatch", "checkpoint has a result outside the reachable prefix")
    for index in completed:
        if index not in contexts or index not in results or results[index].outcome != "completed":
            raise _error("release-checkpoint-phase-mismatch", "completed prefix lacks exact completed observations")
    if any(index not in contexts for index in results):
        raise _error("release-checkpoint-phase-mismatch", "result has no retained selected context")
    terminal = results.get(next_phase) if next_phase < len(PHASES) else None
    if terminal is not None and terminal.outcome == "completed":
        raise _error("release-checkpoint-phase-mismatch", "completed result did not advance the selected phase")
    if in_progress is not None:
        if next_phase >= len(PHASES) or contexts.get(next_phase) != in_progress or terminal is not None:
            raise _error("release-checkpoint-phase-mismatch", "in-progress state is not one reachable selected phase")
        if stopped:
            raise _error("release-checkpoint-phase-mismatch", "stopped Run cannot retain an in-progress effect")
    elif not stopped and (terminal is not None or set(results) != completed):
        raise _error("release-checkpoint-phase-mismatch", "active Run has an unadvanced terminal result")
    elif stopped and terminal is None and next_phase < len(PHASES):
        raise _error("release-checkpoint-phase-mismatch", "stopped Run lacks terminal or interrupted phase evidence")


def _validate_result_outputs(results: dict[int, ReleasePhaseResult], state: dict[str, Any]) -> None:
    """A result may point only to the exact retained observation for its phase."""

    for index, result in results.items():
        expected = state[_PHASE_STATE[PHASES[index][2]]]
        if result.output is not None and result.output != expected:
            raise _error("release-checkpoint-phase-mismatch", "phase result does not retain its exact state observation")
        if result.outcome == "completed" and result.output is None:
            raise _error("release-checkpoint-phase-mismatch", "completed phase lacks its typed observation")


def _shared_recordings_value(
    shared_recordings: Mapping[int, Mapping[str, Any]] | None,
    results: Mapping[int, ReleasePhaseResult],
) -> list[dict[str, Any]]:
    """Encode only durable shared Action-terminal receipt references.

    These entries are not another Journal.  They are the exact receipt
    references already issued by the shared dispatcher, retained beside the
    private frontier so recovery can distinguish a recorded terminal Action
    from an uncertain effect.
    """

    if shared_recordings is None:
        return []
    if not isinstance(shared_recordings, Mapping):
        raise _error("release-checkpoint-invalid", "shared recordings must be indexed typed state")
    indexed: list[tuple[int, Mapping[str, Any]]] = []
    for raw_index, source in shared_recordings.items():
        index = _index(raw_index, "shared_recordings.index")
        indexed.append((index, source))
    records: list[dict[str, Any]] = []
    for index, source in sorted(indexed):
        if index not in results:
            raise _error("release-checkpoint-phase-mismatch", "shared recording has no retained phase result")
        packet = _mapping(source, {"terminal_outcome", "receipt_refs"}, "shared_recording")
        terminal_outcome = _text(packet["terminal_outcome"], "shared_recording.terminal_outcome")
        if terminal_outcome not in {"completed", "no_op", "failed", "cancelled", "partial", "interrupted_pending"}:
            raise _error("release-checkpoint-invalid", "shared recording has an unsupported terminal outcome")
        refs = packet["receipt_refs"]
        if not isinstance(refs, (list, tuple)) or not refs:
            raise _error("release-checkpoint-invalid", "shared recording requires canonical receipt references")
        receipt_refs = [_text(reference, "shared_recording.receipt_refs") for reference in refs]
        if len(set(receipt_refs)) != len(receipt_refs):
            raise _error("release-checkpoint-invalid", "shared recording repeats one canonical receipt reference")
        records.append({"index": index, "terminal_outcome": terminal_outcome, "receipt_refs": receipt_refs})
    if len({record["index"] for record in records}) != len(records):
        raise _error("release-checkpoint-invalid", "shared recordings repeat one selected phase")
    return records


def _load_shared_recordings(value: Any, results: Mapping[int, ReleasePhaseResult]) -> dict[int, dict[str, Any]]:
    if not isinstance(value, list):
        raise _error("release-checkpoint-invalid", "shared recordings must be a canonical list")
    restored: dict[int, dict[str, Any]] = {}
    prior = -1
    for source in value:
        packet = _mapping(source, {"index", "terminal_outcome", "receipt_refs"}, "shared_recording")
        index = _index(packet["index"], "shared_recording.index")
        if index <= prior or index not in results:
            raise _error("release-checkpoint-phase-mismatch", "shared recording is unordered, repeated, or has no phase result")
        prior = index
        terminal_outcome = _text(packet["terminal_outcome"], "shared_recording.terminal_outcome")
        if terminal_outcome not in {"completed", "no_op", "failed", "cancelled", "partial", "interrupted_pending"}:
            raise _error("release-checkpoint-invalid", "shared recording has an unsupported terminal outcome")
        refs = packet["receipt_refs"]
        if not isinstance(refs, list) or not refs:
            raise _error("release-checkpoint-invalid", "shared recording requires canonical receipt references")
        receipt_refs = [_text(reference, "shared_recording.receipt_refs") for reference in refs]
        if len(set(receipt_refs)) != len(receipt_refs):
            raise _error("release-checkpoint-invalid", "shared recording repeats one canonical receipt reference")
        restored[index] = {"terminal_outcome": terminal_outcome, "receipt_refs": tuple(receipt_refs)}
    return restored


def _pending_recordings_value(
    pending_recordings: Mapping[int, Mapping[str, Any]] | None,
    results: Mapping[int, ReleasePhaseResult],
    shared_recordings: Mapping[int, Mapping[str, Any]],
) -> list[dict[str, Any]]:
    """Encode unresolved shared-recorder identities without treating them as proof.

    A pending entry names the single sealed Journal event whose original bytes
    the shared recorder must reconcile.  It is deliberately not a receipt,
    terminal result, or authority to advance a Release phase.  Its
    ``event_outcome`` is the original outcome sealed in the failed Journal
    append; it is not a claim that a durable terminal receipt exists.
    """

    if pending_recordings is None:
        return []
    if not isinstance(pending_recordings, Mapping):
        raise _error("release-checkpoint-invalid", "pending recordings must be indexed typed state")
    indexed: list[tuple[int, Mapping[str, Any]]] = []
    for raw_index, source in pending_recordings.items():
        index = _index(raw_index, "pending_recordings.index")
        if not isinstance(source, Mapping):
            raise _error("release-checkpoint-invalid", "pending recording must be one closed object")
        indexed.append((index, source))
    records: list[dict[str, Any]] = []
    seen_event_ids: set[str] = set()
    for index, source in sorted(indexed):
        if index not in results:
            raise _error("release-checkpoint-phase-mismatch", "pending recording has no retained phase result")
        if index in shared_recordings:
            raise _error("release-checkpoint-phase-mismatch", "one phase cannot be both pending and durably recorded")
        packet = _mapping(dict(source), {"event_id", "event_outcome"}, "pending_recording")
        event_id = _text(packet["event_id"], "pending_recording.event_id")
        event_outcome = _text(packet["event_outcome"], "pending_recording.event_outcome")
        if event_outcome not in _PENDING_EVENT_OUTCOMES:
            raise _error("release-checkpoint-invalid", "pending recording has an unsupported original event outcome")
        if event_id in seen_event_ids:
            raise _error("release-checkpoint-invalid", "pending recordings repeat one event identity")
        seen_event_ids.add(event_id)
        records.append({"index": index, "event_id": event_id, "event_outcome": event_outcome})
    if len({record["index"] for record in records}) != len(records):
        raise _error("release-checkpoint-invalid", "pending recordings repeat one selected phase")
    return records


def _load_pending_recordings(
    value: Any,
    results: Mapping[int, ReleasePhaseResult],
    shared_recordings: Mapping[int, Mapping[str, Any]],
) -> dict[int, dict[str, str]]:
    if not isinstance(value, list):
        raise _error("release-checkpoint-invalid", "pending recordings must be a canonical list")
    restored: dict[int, dict[str, str]] = {}
    prior = -1
    seen_event_ids: set[str] = set()
    for source in value:
        packet = _mapping(source, {"index", "event_id", "event_outcome"}, "pending_recording")
        index = _index(packet["index"], "pending_recording.index")
        if index <= prior or index not in results:
            raise _error("release-checkpoint-phase-mismatch", "pending recording is unordered, repeated, or has no phase result")
        if index in shared_recordings:
            raise _error("release-checkpoint-phase-mismatch", "one phase cannot be both pending and durably recorded")
        prior = index
        event_id = _text(packet["event_id"], "pending_recording.event_id")
        event_outcome = _text(packet["event_outcome"], "pending_recording.event_outcome")
        if event_outcome not in _PENDING_EVENT_OUTCOMES:
            raise _error("release-checkpoint-invalid", "pending recording has an unsupported original event outcome")
        if event_id in seen_event_ids:
            raise _error("release-checkpoint-invalid", "pending recordings repeat one event identity")
        seen_event_ids.add(event_id)
        restored[index] = {"event_id": event_id, "event_outcome": event_outcome}
    return restored


def _native_portable_run(run: ReleaseActionRun) -> bool:
    """Identify the current O164@11 portable frontier from selected contexts only."""

    contexts = [*run.contexts.values()]
    if run.in_progress is not None:
        contexts.append(run.in_progress)
    versions = {context.workflow_version for context in contexts}
    if not versions:
        return False
    if versions == {11}:
        return True
    if versions <= {5, 6}:
        return False
    raise _error("release-checkpoint-binding-mismatch", "checkpoint mixes unsupported selected workflow revisions")


def _native_rows(rows: tuple[PortablePackageRow, ...], label: str) -> list[dict[str, Any]]:
    if not isinstance(rows, tuple) or any(type(row) is not PortablePackageRow for row in rows):
        raise _error("release-checkpoint-invalid", f"{label} is not exact portable row state")
    return [_json_value(row.record(), label) for row in rows]


def _load_native_rows(value: Any, label: str) -> tuple[PortablePackageRow, ...]:
    if not isinstance(value, list):
        raise _error("release-checkpoint-invalid", f"{label} must be a canonical row list")
    rows: list[PortablePackageRow] = []
    for item in value:
        payload = _mapping(item, {"resource", "source_path", "destination_path", "sha256", "mode"}, label)
        resource = _text(payload["resource"], f"{label}.resource")
        source_path = _safe_path(payload["source_path"], f"{label}.source_path")
        destination_path = _safe_path(payload["destination_path"], f"{label}.destination_path")
        digest = _sha256(payload["sha256"], f"{label}.sha256")
        mode = payload["mode"]
        if type(mode) is not int or not 0 <= mode <= 0o777:
            raise _error("release-checkpoint-invalid", f"{label}.mode is invalid")
        rows.append(PortablePackageRow(resource, source_path, destination_path, digest, mode))
    return tuple(rows)


def _native_export_value(value: Any) -> dict[str, Any]:
    if type(value) is not SealedMethodologyExport:
        raise _error("release-checkpoint-invalid", "methodology_export is not typed portable state")
    return {
        "release_candidate_root": _safe_path(value.release_candidate_root, "methodology_export.release_candidate_root"),
        "source_export_root": _safe_path(value.source_export_root, "methodology_export.source_export_root"),
        "frozen_manifest_sha256": _sha256(value.frozen_manifest_sha256, "methodology_export.frozen_manifest_sha256"),
        "export_inventory_sha256": _sha256(value.export_inventory_sha256, "methodology_export.export_inventory_sha256"),
        "export_seal_sha256": _sha256(value.export_seal_sha256, "methodology_export.export_seal_sha256"),
    }


def _load_native_export(value: Any, candidate: ValidatedCandidate, root: str, *, historical: bool = False) -> SealedMethodologyExport:
    payload = _mapping(value, {
        "release_candidate_root", "source_export_root", "frozen_manifest_sha256",
        "export_inventory_sha256", "export_seal_sha256",
    }, "methodology_export")
    release_root = _safe_path(payload["release_candidate_root"], "methodology_export.release_candidate_root")
    expected = {
        "release_candidate_root": release_root,
        "source_export_root": _safe_path(payload["source_export_root"], "methodology_export.source_export_root"),
        "frozen_manifest_sha256": _sha256(payload["frozen_manifest_sha256"], "methodology_export.frozen_manifest_sha256"),
        "export_inventory_sha256": _sha256(payload["export_inventory_sha256"], "methodology_export.export_inventory_sha256"),
        "export_seal_sha256": _sha256(payload["export_seal_sha256"], "methodology_export.export_seal_sha256"),
    }
    if historical:
        from release_handoff import _exporter_module, _assert_export_inventory_bound, _export_seal_sha256

        exporter = _exporter_module()
        export = exporter.read_sealed_export(release_candidate_root=Path(root) / release_root)
        _assert_export_inventory_bound(candidate, export, exporter)
        observed = SealedMethodologyExport(
            candidate, release_root, export.output_root.relative_to(root).as_posix(),
            export.frozen_manifest_sha256, export.inventory_digest,
            _export_seal_sha256(Path(root) / release_root, exporter),
        )
    else:
        observed = bind_sealed_methodology_export(candidate, Path(root) / release_root)
    if _native_export_value(observed) != expected:
        raise _error("release-checkpoint-binding-mismatch", "private Methodology export changed after checkpoint")
    return observed


def _native_private_value(value: Any) -> dict[str, Any]:
    if type(value) is not SealedPrivateMethodologyCompilation:
        raise _error("release-checkpoint-invalid", "private_compilation is not typed portable state")
    return {
        "compiled_root": _safe_path(value.compiled_root, "private_compilation.compiled_root"),
        "compiled_manifest_sha256": _sha256(value.compiled_manifest_sha256, "private_compilation.compiled_manifest_sha256"),
        "compiled_output_sha256": _sha256(value.compiled_output_sha256, "private_compilation.compiled_output_sha256"),
    }


def _load_native_private(value: Any, export: SealedMethodologyExport, *, historical: bool = False) -> SealedPrivateMethodologyCompilation:
    payload = _mapping(value, {"compiled_root", "compiled_manifest_sha256", "compiled_output_sha256"}, "private_compilation")
    expected = {
        "compiled_root": _safe_path(payload["compiled_root"], "private_compilation.compiled_root"),
        "compiled_manifest_sha256": _sha256(payload["compiled_manifest_sha256"], "private_compilation.compiled_manifest_sha256"),
        "compiled_output_sha256": _sha256(payload["compiled_output_sha256"], "private_compilation.compiled_output_sha256"),
    }
    if historical:
        from release_compilation import PRIVATE_COMPILED_MANIFEST_NAME, PRIVATE_COMPILED_SCHEMA, _child_tree_digest
        from release_handoff import _file
        from release_inventory import persistent_regular_files

        root = Path(export.candidate.project_root)
        compiled_root = root / expected["compiled_root"]
        raw = _file(root, f"{expected['compiled_root']}/{PRIVATE_COMPILED_MANIFEST_NAME}").read_bytes()
        manifest = json.loads(raw)
        unsigned = dict(manifest)
        checksum = unsigned.pop("sha256", None)
        if (raw != canonical_json(manifest) or checksum != hashlib.sha256(canonical_json(unsigned)).hexdigest()
                or manifest.get("schema") != PRIVATE_COMPILED_SCHEMA
                or manifest.get("candidate_snapshot_manifest_sha256") != export.candidate.manifest.sha256
                or manifest.get("frozen_manifest_sha256") != export.frozen_manifest_sha256
                or manifest.get("export_inventory_sha256") != export.export_inventory_sha256
                or manifest.get("export_seal_sha256") != export.export_seal_sha256
                or manifest.get("source_export_root") != export.source_export_root):
            raise _error("release-checkpoint-binding-mismatch", "retained private compilation differs from its sealed export")
        observed_files = {path.relative_to(compiled_root).as_posix(): path.read_bytes()
                          for path in persistent_regular_files(root, compiled_root)}
        output_rows = [{"path": path, "sha256": hashlib.sha256(payload).hexdigest()}
                       for path, payload in sorted(observed_files.items()) if path != PRIVATE_COMPILED_MANIFEST_NAME]
        if manifest.get("output_rows") != output_rows:
            raise _error("release-checkpoint-binding-mismatch", "retained private compiled inventory changed")
        observed = SealedPrivateMethodologyCompilation(export, expected["compiled_root"], checksum, _child_tree_digest(observed_files))
    else:
        observed = read_sealed_private_methodology_compilation(export)
    if _native_private_value(observed) != expected:
        raise _error("release-checkpoint-binding-mismatch", "private Methodology compilation changed after checkpoint")
    return observed


def _native_binding_atoms_value(value: Any, label: str) -> list[dict[str, Any]]:
    """Encode the closed frozen binding frontier without executable meaning."""

    if not isinstance(value, tuple) or any(type(atom) is not PortableBindingAtom for atom in value):
        raise _error("release-checkpoint-invalid", f"{label} is not an exact frozen binding frontier")
    records = [
        {
            "atom_id": _text(atom.atom_id, f"{label}.atom_id"),
            "source_path": _safe_path(atom.source_path, f"{label}.source_path"),
            "sha256": _sha256(atom.sha256, f"{label}.sha256"),
            "version": atom.version,
        }
        for atom in value
    ]
    if (
        any(type(record["version"]) is not int or record["version"] < 1 for record in records)
        or records != sorted(records, key=lambda record: str(record["source_path"]))
        or len({str(record["source_path"]) for record in records}) != len(records)
        or len({(str(record["atom_id"]), int(record["version"])) for record in records}) != len(records)
    ):
        raise _error("release-checkpoint-invalid", f"{label} is not canonical")
    return records


def _load_native_binding_atoms(value: Any, label: str) -> tuple[PortableBindingAtom, ...]:
    """Decode one exact, source-path ordered frozen binding frontier."""

    if not isinstance(value, list):
        raise _error("release-checkpoint-invalid", f"{label} must be a canonical binding list")
    atoms: list[PortableBindingAtom] = []
    for index, raw in enumerate(value):
        payload = _mapping(raw, {"atom_id", "source_path", "sha256", "version"}, f"{label}[{index}]")
        atom_id = _text(payload["atom_id"], f"{label}[{index}].atom_id")
        source_path = _safe_path(payload["source_path"], f"{label}[{index}].source_path")
        sha256 = _sha256(payload["sha256"], f"{label}[{index}].sha256")
        version = payload["version"]
        if type(version) is not int or version < 1:
            raise _error("release-checkpoint-invalid", f"{label}[{index}].version is invalid")
        atoms.append(PortableBindingAtom(atom_id, version, source_path, sha256))
    ordered = tuple(sorted(atoms, key=lambda atom: atom.source_path))
    if (
        tuple(atoms) != ordered
        or len({atom.source_path for atom in ordered}) != len(ordered)
        or len({(atom.atom_id, atom.version) for atom in ordered}) != len(ordered)
    ):
        raise _error("release-checkpoint-invalid", f"{label} is not canonical")
    return ordered


def _native_binding_frontier_payload(
    value: Any,
    required: set[str],
    label: str,
) -> tuple[dict[str, Any], tuple[PortableBindingAtom, ...]]:
    """Read current frontier data or a provably binding-free legacy payload."""

    if not isinstance(value, dict):
        raise _error("release-checkpoint-invalid", f"{label} has unknown, missing, or non-object members")
    keys = set(value)
    if keys == required:
        return value, ()
    if keys != required | {"binding_atoms"}:
        raise _error("release-checkpoint-invalid", f"{label} has unknown, missing, or non-object members")
    return value, _load_native_binding_atoms(value["binding_atoms"], f"{label}.binding_atoms")


def _validate_native_binding_frontier(
    rows: tuple[PortablePackageRow, ...],
    atoms: tuple[PortableBindingAtom, ...],
    label: str,
) -> None:
    """Keep projected package rows inseparable from their frozen raw pins."""

    bindings = tuple(row for row in rows if row.resource == "BINDING_PROJECTION")
    if not atoms:
        if bindings:
            raise _error("release-checkpoint-binding-mismatch", f"{label} has binding projections without a frozen frontier")
        return
    expected_destinations = {
        (Path("methodology/bindings") / atom.source_path).as_posix()
        for atom in atoms
    }
    if (
        len(bindings) != len(atoms)
        or {row.destination_path for row in bindings} != expected_destinations
        or len({row.destination_path for row in bindings}) != len(bindings)
    ):
        raise _error("release-checkpoint-binding-mismatch", f"{label} binding projections differ from the frozen frontier")


def _native_snapshot_value(value: Any) -> dict[str, Any]:
    if type(value) is not SealedPortableSourceSnapshot:
        raise _error("release-checkpoint-invalid", "portable_source_snapshot is not typed state")
    return {
        "candidate_run_id": _text(value.candidate_run_id, "portable_source_snapshot.candidate_run_id"),
        "rows": _native_rows(value.portable_package_rows, "portable_source_snapshot.rows"),
        "binding_atoms": _native_binding_atoms_value(value.binding_atoms, "portable_source_snapshot.binding_atoms"),
    }


def _load_native_snapshot(value: Any, candidate: ValidatedCandidate, private: SealedPrivateMethodologyCompilation, *, historical: bool = False) -> SealedPortableSourceSnapshot:
    payload, expected_atoms = _native_binding_frontier_payload(
        value, {"candidate_run_id", "rows"}, "portable_source_snapshot",
    )
    run_id = _text(payload["candidate_run_id"], "portable_source_snapshot.candidate_run_id")
    expected_rows = _load_native_rows(payload["rows"], "portable_source_snapshot.rows")
    _validate_native_binding_frontier(expected_rows, expected_atoms, "portable_source_snapshot")
    if historical:
        from release_handoff import _file
        from release_portable_contract import _private_rows

        for row in expected_rows:
            path = _file(Path(candidate.project_root), row.source_path)
            if hashlib.sha256(path.read_bytes()).hexdigest() != row.sha256 or path.stat().st_mode & 0o777 != row.mode:
                raise _error("release-checkpoint-binding-mismatch", "retained portable source bytes changed")
        private_rows, observed_atoms = _private_rows(Path(candidate.project_root), private)
        if observed_atoms != expected_atoms:
            raise _error("release-checkpoint-binding-mismatch", "retained portable binding frontier changed")
        if (
            tuple(row for row in private_rows if row.resource == "BINDING_PROJECTION")
            != tuple(row for row in expected_rows if row.resource == "BINDING_PROJECTION")
        ):
            raise _error("release-checkpoint-binding-mismatch", "retained portable binding projections changed")
        observed = SealedPortableSourceSnapshot(run_id, candidate, private, expected_rows, expected_atoms)
    else:
        observed = collect_portable_source_snapshot(candidate, private, candidate_run_id=run_id)
    if observed.portable_package_rows != expected_rows or observed.binding_atoms != expected_atoms:
        raise _error("release-checkpoint-binding-mismatch", "portable pre-catalog source snapshot changed after checkpoint")
    return observed


def _native_compilation_value(value: Any) -> dict[str, Any]:
    if type(value) is not SealedPortableCandidateCompilation:
        raise _error("release-checkpoint-invalid", "portable_compilation is not typed state")
    return {
        "candidate_run_id": _text(value.candidate_run_id, "portable_compilation.candidate_run_id"),
        "source_catalog_sha256": _sha256(value.source_catalog_sha256, "portable_compilation.source_catalog_sha256"),
        "input_manifest_sha256": _sha256(value.input_manifest_sha256, "portable_compilation.input_manifest_sha256"),
        "rows": _native_rows(value.portable_package_rows, "portable_compilation.rows"),
        "binding_atoms": _native_binding_atoms_value(value.binding_atoms, "portable_compilation.binding_atoms"),
    }


def _load_native_compilation(value: Any, snapshot: SealedPortableSourceSnapshot, *, historical: bool = False) -> SealedPortableCandidateCompilation:
    payload, expected_atoms = _native_binding_frontier_payload(
        value,
        {"candidate_run_id", "source_catalog_sha256", "input_manifest_sha256", "rows"},
        "portable_compilation",
    )
    expected_rows = _load_native_rows(payload["rows"], "portable_compilation.rows")
    expected = {
        "candidate_run_id": _text(payload["candidate_run_id"], "portable_compilation.candidate_run_id"),
        "source_catalog_sha256": _sha256(payload["source_catalog_sha256"], "portable_compilation.source_catalog_sha256"),
        "input_manifest_sha256": _sha256(payload["input_manifest_sha256"], "portable_compilation.input_manifest_sha256"),
        "rows": _native_rows(expected_rows, "portable_compilation.rows"),
        "binding_atoms": _native_binding_atoms_value(expected_atoms, "portable_compilation.binding_atoms"),
    }
    _validate_native_binding_frontier(expected_rows, expected_atoms, "portable_compilation")
    if expected_atoms != snapshot.binding_atoms:
        raise _error("release-checkpoint-binding-mismatch", "portable compilation binding frontier differs from its source snapshot")
    if historical:
        from release_portable_contract import _manifest_sha256
        from release_handoff import _file

        for row in expected_rows:
            path = _file(Path(snapshot.candidate.project_root), row.source_path)
            if hashlib.sha256(path.read_bytes()).hexdigest() != row.sha256 or path.stat().st_mode & 0o777 != row.mode:
                raise _error("release-checkpoint-binding-mismatch", "retained portable compilation bytes changed")
        observed = SealedPortableCandidateCompilation(
            expected["candidate_run_id"], snapshot.candidate, snapshot.private_compilation, expected_rows,
            expected["source_catalog_sha256"], _manifest_sha256(
                expected["candidate_run_id"], snapshot.candidate, snapshot.private_compilation,
                expected["source_catalog_sha256"], expected_rows, expected_atoms,
            ),
            expected_atoms,
        )
    else:
        observed = seal_portable_source_snapshot(snapshot)
    if _native_compilation_value(observed) != expected:
        raise _error("release-checkpoint-binding-mismatch", "portable catalog/admission compilation changed after checkpoint")
    return observed


def _native_package_value(value: Any) -> dict[str, Any]:
    if type(value) is not PreparedPortableReleasePackage:
        raise _error("release-checkpoint-invalid", "prepared_portable_package is not typed state")
    return {
        "candidate_run_id": _text(value.candidate_run_id, "prepared_portable_package.candidate_run_id"),
        "candidate_snapshot_manifest_sha256": _sha256(value.candidate_snapshot_manifest_sha256, "prepared_portable_package.candidate_snapshot_manifest_sha256"),
        "input_manifest_sha256": _sha256(value.input_manifest_sha256, "prepared_portable_package.input_manifest_sha256"),
        "package_manifest_sha256": _sha256(value.package_manifest_sha256, "prepared_portable_package.package_manifest_sha256"),
    }


def _load_native_package(value: Any, root: str, portable: SealedPortableCandidateCompilation) -> PreparedPortableReleasePackage:
    payload = _mapping(value, {
        "candidate_run_id", "candidate_snapshot_manifest_sha256", "input_manifest_sha256", "package_manifest_sha256",
    }, "prepared_portable_package")
    candidate_run_id = _text(payload["candidate_run_id"], "prepared_portable_package.candidate_run_id")
    candidate_sha = _sha256(payload["candidate_snapshot_manifest_sha256"], "prepared_portable_package.candidate_snapshot_manifest_sha256")
    manifest_sha = _sha256(payload["package_manifest_sha256"], "prepared_portable_package.package_manifest_sha256")
    input_sha = _sha256(payload["input_manifest_sha256"], "prepared_portable_package.input_manifest_sha256")
    if (candidate_run_id != portable.candidate_run_id or candidate_sha != portable.candidate_snapshot_manifest_sha256
            or input_sha != portable.input_manifest_sha256):
        raise _error("release-checkpoint-binding-mismatch", "private portable package differs from sealed portable compilation")
    package = reopen_portable_release_package(root, candidate_run_id, manifest_sha)
    return PreparedPortableReleasePackage(candidate_run_id, candidate_sha, input_sha, package)


def _native_dataclass_value(value: Any, cls: type[Any], label: str) -> dict[str, Any]:
    return _dump_dataclass(value, cls, label)


def _native_state_value(run: ReleaseActionRun, name: str) -> Any:
    value = getattr(run, name)
    if value is None:
        return None
    if name == "candidate":
        return _candidate_value(value)
    if name == "preflight":
        return _preflight_value(value)
    if name == "methodology_export":
        return _native_export_value(value)
    if name == "private_compilation":
        return _native_private_value(value)
    if name == "portable_source_snapshot":
        return _native_snapshot_value(value)
    if name == "portable_compilation":
        return _native_compilation_value(value)
    if name == "portable_suite":
        return _native_dataclass_value(value, PortableSuiteGateEvidence, name)
    if name == "prepared_portable_package":
        return _native_package_value(value)
    if name == "build":
        return _native_dataclass_value(value, PortableImageBuildEvidence, name)
    if name == "verification":
        return _native_dataclass_value(value, PortableImageVerificationEvidence, name)
    if name == "e2e":
        return _dump_dataclass(value, PortableCandidateE2EGateEvidence, name)
    if name == "full_gate":
        from release_full_gate import NativeFullGateEvidence
        return _native_dataclass_value(value, NativeFullGateEvidence, name)
    if name == "promotion":
        return _native_dataclass_value(value, NativePromotionEvidence, name)
    if name == "retirement":
        return _native_dataclass_value(value, ImageRetirementEvidence, name)
    raise _error("release-checkpoint-invalid", "native checkpoint has an unsupported state field")


def _load_native_state(value: Mapping[str, Any], root: str, *, documentary_publication_frontier: bool = False) -> dict[str, Any]:
    state_payload = _mapping(dict(value), set(_NATIVE_STATE_NAMES), "native state")
    state: dict[str, Any] = {name: None for name in _NATIVE_STATE_NAMES}
    historical = state_payload["promotion"] is not None or documentary_publication_frontier
    if state_payload["candidate"] is not None:
        state["candidate"] = _load_candidate(state_payload["candidate"], root, historical_native_n=historical)
    candidate = state["candidate"]
    if candidate is None:
        if any(state_payload[name] is not None for name in _NATIVE_STATE_NAMES[1:]):
            raise _error("release-checkpoint-phase-mismatch", "native post-freeze state lacks candidate")
        return state
    if state_payload["preflight"] is None:
        raise _error("release-checkpoint-phase-mismatch", "native candidate lacks compiler preflight")
    state["preflight"] = _load_preflight(state_payload["preflight"], candidate)
    if state_payload["methodology_export"] is not None:
        state["methodology_export"] = _load_native_export(state_payload["methodology_export"], candidate, root, historical=historical)
    if state_payload["private_compilation"] is not None:
        if state["methodology_export"] is None:
            raise _error("release-checkpoint-phase-mismatch", "native private compilation lacks export")
        state["private_compilation"] = _load_native_private(state_payload["private_compilation"], state["methodology_export"], historical=historical)
    if state_payload["portable_source_snapshot"] is not None:
        if state["private_compilation"] is None:
            raise _error("release-checkpoint-phase-mismatch", "native source snapshot lacks private compilation")
        state["portable_source_snapshot"] = _load_native_snapshot(
            state_payload["portable_source_snapshot"], candidate, state["private_compilation"],
            historical=historical,
        )
    if state_payload["portable_compilation"] is not None:
        if state["portable_source_snapshot"] is None:
            raise _error("release-checkpoint-phase-mismatch", "native portable compilation lacks source snapshot")
        state["portable_compilation"] = _load_native_compilation(
            state_payload["portable_compilation"], state["portable_source_snapshot"],
            historical=historical,
        )
    portable = state["portable_compilation"]
    if state_payload["portable_suite"] is not None:
        state["portable_suite"] = _load_dataclass(
            state_payload["portable_suite"], PortableSuiteGateEvidence, "portable_suite",
            tuple_fields=frozenset({"command", "coverage"}),
        )
    if state_payload["prepared_portable_package"] is not None:
        if portable is None:
            raise _error("release-checkpoint-phase-mismatch", "native package lacks portable compilation")
        state["prepared_portable_package"] = _load_native_package(
            state_payload["prepared_portable_package"], root, portable,
        )
    if state_payload["build"] is not None:
        state["build"] = _load_dataclass(state_payload["build"], PortableImageBuildEvidence, "build")
    if state_payload["verification"] is not None:
        state["verification"] = _load_dataclass(state_payload["verification"], PortableImageVerificationEvidence, "verification")
    if state_payload["e2e"] is not None:
        state["e2e"] = _load_e2e(state_payload["e2e"], native=True)
    if state_payload["full_gate"] is not None:
        from release_full_gate import NativeFullGateEvidence
        state["full_gate"] = _load_dataclass(state_payload["full_gate"], NativeFullGateEvidence, "full_gate")
    if state_payload["promotion"] is not None:
        state["promotion"] = _load_dataclass(
            state_payload["promotion"], NativePromotionEvidence, "promotion",
            tuple_fields=frozenset({"effect_refs"}),
        )
    if state_payload["retirement"] is not None:
        nullable_tuples = frozenset({"retaining_container_refs", "observed_rollback_refs", "required_rollback_refs"})
        state["retirement"] = _load_dataclass(
            state_payload["retirement"], ImageRetirementEvidence, "retirement",
            tuple_fields=frozenset(name for name in nullable_tuples if state_payload["retirement"].get(name) is not None),
        )
    if portable is None and any(state[name] is not None for name in _NATIVE_STATE_NAMES[6:]):
        raise _error("release-checkpoint-phase-mismatch", "native later evidence lacks portable compilation")
    if state["portable_suite"] is None and any(state[name] is not None for name in _NATIVE_STATE_NAMES[8:]):
        raise _error("release-checkpoint-phase-mismatch", "native image evidence lacks Unit evidence")
    if state["prepared_portable_package"] is None and any(state[name] is not None for name in _NATIVE_STATE_NAMES[8:]):
        raise _error("release-checkpoint-phase-mismatch", "native image evidence lacks private prepared package")
    if state["promotion"] is not None and state["full_gate"] is None:
        raise _error("release-checkpoint-phase-mismatch", "native publication lacks retained Full Gate")
    if state["retirement"] is not None and state["promotion"] is None:
        raise _error("release-checkpoint-phase-mismatch", "native retirement lacks publication evidence")
    _validate_native_evidence_bindings(state)
    if state["promotion"] is not None:
        _verify_native_publication_documentary_state(state, root)
    return state


def _verify_native_publication_documentary_state(state: Mapping[str, Any], root: str) -> None:
    """Prove post-effect documentary restoration without reselecting removed N."""

    from dataclasses import replace
    from release_handoff import _file
    from release_promotion import PROMOTION_ROOT, _reopen_historical_native_promotion_packet, verify_native_promotion_evidence
    from selected_installation_command import read_selected_installation_command_receipt, reopen_selected_installation_command_start

    publication = state["promotion"]
    candidate = state["candidate"]
    packet = _reopen_historical_native_promotion_packet(
        candidate, state["portable_suite"], state["build"],
        state["verification"], state["e2e"], state["full_gate"], state["prepared_portable_package"],
    )
    prefix = f"{PROMOTION_ROOT}/{candidate.manifest.sha256}/observations/attempt-"
    if (publication.outcome not in {"promoted", "pending", "effect_uncertain", "recording_uncertain"}
            or publication.full_gate_receipt_sha256 != packet.evidence.receipt_sha256
            or not publication.evidence_root.startswith(prefix) or "/" in publication.evidence_root.removeprefix(prefix)
            or publication.retained_prior_selector_ref != f"{PROMOTION_ROOT}/{candidate.manifest.sha256}/prior-selector.toml"):
        raise _error("release-checkpoint-binding-mismatch", "native documentary publication differs from the original retained frontier")
    if publication.receipt_sha256 is None:
        # A failed receipt write cannot establish a trusted post-effect codec
        # frontier.  The provider retains its pre-effect checkpoint and uses
        # existing unknown-effect recovery rather than inventing this record.
        raise _error("release-checkpoint-binding-mismatch", "native documentary publication lacks its actual observation receipt")
    raw = _file(Path(root), f"{publication.evidence_root}/receipt.json").read_bytes()
    if (hashlib.sha256(raw).hexdigest() != publication.receipt_sha256
            or raw != canonical_json(asdict(replace(publication, receipt_sha256=None)))):
        raise _error("release-checkpoint-binding-mismatch", "native documentary publication receipt changed")
    command = read_selected_installation_command_receipt(
        _file(Path(root), f".caprmedio_runtime/installation/commands/{publication.installation_command_sha256}.json").read_bytes(),
        expected_sha256=publication.installation_command_sha256,
    )
    event = reopen_selected_installation_command_start(Path(root), command)
    prior = _file(Path(root), publication.retained_prior_selector_ref).read_bytes()
    if (command.command_id != publication.action_run_id or event["event_id"] != publication.action_start_event_id
            or command.prior_runtime_selector_sha256 != hashlib.sha256(prior).hexdigest()
            or command.target_project_context_sha256 != publication.target_project_context_sha256
            or command.package_manifest_sha256 != publication.package_manifest_sha256
            or command.full_gate_receipt_sha256 != publication.full_gate_receipt_sha256):
        raise _error("release-checkpoint-binding-mismatch", "native documentary publication differs from its actual selected command")
    binding = candidate.native_installed_n
    if binding is not None:
        selected = binding.selected
        prior_document = tomllib.loads(prior.decode("utf-8"))
        if (hashlib.sha256(prior).hexdigest() != selected.selector_sha256
                or prior_document.get("package_manifest_sha256") != selected.package_manifest_sha256
                or prior_document.get("target_project_context_sha256") != selected.target_project_context_sha256
                or prior_document.get("state_generation") != selected.state_generation
                or prior_document.get("image_digest") != selected.image_digest):
            raise _error("release-checkpoint-binding-mismatch", "documentary prior native N differs from the actual retained selector")
        prior_proof = _file(Path(root), f".caprmedio_runtime/installation/generations/{selected.state_generation}/release-proof.toml").read_bytes()
        context = selected.binding.target_context
        from installed_mcp_binding import _context as reopen_mcp_target_context

        prior_context = _file(Path(root), f".caprmedio_runtime/installation/contexts/{context.sha256}.toml").read_bytes()
        if (hashlib.sha256(prior_proof).hexdigest() != selected.release_proof_sha256
                or context.path != Path(root) / f".caprmedio_runtime/installation/contexts/{context.sha256}.toml"
                or reopen_mcp_target_context(Path(root), context.sha256) != context):
            raise _error("release-checkpoint-binding-mismatch", "documentary native N generation/context evidence changed")
    if publication.outcome == "promoted":
        verify_native_promotion_evidence(
            candidate, state["portable_compilation"], state["portable_suite"], state["build"], state["verification"], publication,
            e2e=state["e2e"], full_gate=state["full_gate"], prepared_package=state["prepared_portable_package"],
        )


def _validate_native_evidence_bindings(state: Mapping[str, Any]) -> None:
    """Keep the documentary native frontier on one exact candidate/package.

    This verifies retained identity relationships, never a gate pass or effect
    authority.  Publication consumers still reopen original physical receipts.
    """

    candidate, portable = state["candidate"], state["portable_compilation"]
    if candidate is None or portable is None:
        return
    expected = {
        "candidate_snapshot_manifest_sha256": candidate.manifest.sha256,
        "candidate_run_id": portable.candidate_run_id,
        "input_manifest_sha256": portable.input_manifest_sha256,
        "source_catalog_sha256": portable.source_catalog_sha256,
        "framework_version": portable.framework_version,
        "version_toml_sha256": portable.version_toml_sha256,
    }
    package = state["prepared_portable_package"]
    if package is not None:
        expected["package_manifest_sha256"] = package.package_manifest_sha256
    for name in ("portable_suite", "build", "verification", "e2e", "full_gate", "promotion", "retirement"):
        observed = state[name]
        if observed is not None and any(
            getattr(observed, field) != identity
            for field, identity in expected.items() if hasattr(observed, field)
        ):
            raise _error("release-checkpoint-binding-mismatch", f"native {name} belongs to another frozen frontier")
    full_gate = state["full_gate"]
    if full_gate is not None:
        for field, predecessor in (
            ("suite_receipt_sha256", "portable_suite"),
            ("build_receipt_sha256", "build"),
            ("image_receipt_sha256", "verification"),
            ("e2e_receipt_sha256", "e2e"),
        ):
            if state[predecessor] is None or getattr(full_gate, field) != state[predecessor].receipt_sha256:
                raise _error("release-checkpoint-binding-mismatch", "native aggregate differs from retained predecessor receipts")
    image = state["verification"]
    if image is not None:
        for name in ("e2e", "full_gate"):
            if state[name] is not None and state[name].candidate_image_digest != image.candidate_image_digest:
                raise _error("release-checkpoint-binding-mismatch", "native gate differs from the retained immutable image")
    promotion = state["promotion"]
    if promotion is not None and (full_gate is None or promotion.full_gate_receipt_sha256 != full_gate.receipt_sha256):
        raise _error("release-checkpoint-binding-mismatch", "native publication differs from its original Full Gate receipt")
    retirement = state["retirement"]
    if retirement is not None and (
        promotion is None or retirement.promotion_receipt_sha256 != promotion.receipt_sha256
        or retirement.prior_image_digest != promotion.prior_image_digest
        or retirement.candidate_image_digest != promotion.candidate_image_digest
    ):
        raise _error("release-checkpoint-binding-mismatch", "native disposition differs from its observed publication")


def _native_result_value(result: ReleasePhaseResult, index: int) -> dict[str, Any]:
    if type(result) is not ReleasePhaseResult:
        raise _error("release-checkpoint-invalid", "native phase result is not typed state")
    payload = {
        item.name: _json_value(getattr(result, item.name), f"native result.{item.name}")
        for item in fields(ReleasePhaseResult)
        if item.name != "output"
    }
    output = result.output
    if output is None:
        payload["output"] = None
    else:
        phase = PHASES[index][2]
        expected = _NATIVE_PHASE_STATE.get(phase)
        if expected is None:
            raise _error("release-checkpoint-invalid", "native phase cannot retain an unknown publication output")
        payload["output"] = expected
    return payload


def _load_native_result(
    value: Any, index: int, context: SelectedReleaseActionContext,
    candidate: ValidatedCandidate, state: Mapping[str, Any],
) -> ReleasePhaseResult:
    required = {item.name for item in fields(ReleasePhaseResult)}
    payload = _mapping(value, required, "native result")
    output_name = payload["output"]
    expected = _NATIVE_PHASE_STATE.get(PHASES[index][2])
    if output_name is not None:
        if output_name != expected or expected is None:
            raise _error("release-checkpoint-phase-mismatch", "native result output has an invalid observation type")
        output = state[expected]
        if output is None:
            raise _error("release-checkpoint-phase-mismatch", "native result output has no retained observation")
    else:
        output = None
    copied = dict(payload)
    copied["output"] = output
    copied["shared_action_recording"] = _shared_recording(
        copied.get("shared_action_recording"), "native result.shared_action_recording",
    )
    result = _load_dataclass(
        copied, ReleasePhaseResult, "native result",
        tuple_fields=frozenset({"attempted_effects", "effect_evidence_refs", "declared_run_receipt_refs"}),
    )
    step, action, phase = PHASES[index]
    if (
        result.workflow_run_id != context.workflow_run_id or result.step_run_id != context.step_run_id
        or result.action_run_id != context.action_run_id or result.step_atom_id != step
        or result.action_atom_id != action or result.phase != phase
        or result.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
        or result.recording_state != "shared_session_provider_pending"
        or result.outcome not in {"prepared", "completed", "blocked", "failed", "pending", "effect_uncertain"}
    ):
        raise _error("release-checkpoint-phase-mismatch", "native result does not match its selected phase context")
    if result.shared_action_recording is not None:
        packet = result.shared_action_recording
        if (phase != "retire" or result.outcome != "pending" or result.effect_outcome != "retired"
                or packet["on_recorded_result"] != "complete exact prior N-image disposition"
                or type(output) is not ImageRetirementEvidence or output.outcome != "retired"
                or packet["candidate_snapshot_manifest_sha256"] != candidate.manifest.sha256
                or packet["prior_image_digest"] != output.prior_image_digest
                or packet["retirement_receipt_sha256"] != output.receipt_sha256
                or packet["retirement_receipt_ref"] != f"{output.evidence_root}/receipt.json"
                or result.effect_evidence_refs != (packet["retirement_receipt_ref"],)):
            raise _error("release-checkpoint-phase-mismatch", "native retirement shared recording differs from its retained exact effect")
    return result


def _validate_native_result_outputs(results: Mapping[int, ReleasePhaseResult], state: Mapping[str, Any]) -> None:
    for index, result in results.items():
        expected_name = _NATIVE_PHASE_STATE.get(PHASES[index][2])
        expected = None if expected_name is None else state[expected_name]
        if result.output is not None and result.output != expected:
            raise _error("release-checkpoint-phase-mismatch", "native phase result differs from retained native observation")
        if result.outcome == "completed" and result.output is None:
            raise _error("release-checkpoint-phase-mismatch", "completed native phase lacks typed observation")


def _native_partial_publication_hint(source: Mapping[str, Any]) -> bool:
    """Documentary decoding hint only; complete validation still follows."""

    if source.get("in_progress") is not None and type(source.get("next_phase")) is int and source["next_phase"] in {10, 11} and source.get("stopped") is False:
        return True
    if source.get("stopped") is True and isinstance(source.get("results"), list):
        return any(isinstance(row, dict) and type(row.get("index")) is int and row["index"] in {10, 11} and isinstance(row.get("result"), dict)
                   and isinstance(row["result"].get("outcome"), str) and row["result"]["outcome"] in {"effect_uncertain", "pending"} for row in source["results"])
    return False


def _reopen_native_partial_frontier_start(root: str, context: SelectedReleaseActionContext,
                                         pending: Mapping[str, str] | None = None) -> None:
    """Read bounded canonical start/pending records, without an executor grant."""

    import json
    import work_journal
    from operator_registry import parse_operators_registry
    from selected_installation_command import _registered_journal_author
    from release_handoff import _file
    from native_selected_installation import _read as raw_physical_native_carrier
    from FIND_AND_FETCH_JOURNAL_EVENTS.find_and_fetch_journal_events import capture_snapshot, query

    def read_physical_native_carrier(path, *, code, mode=None):
        try:
            return raw_physical_native_carrier(path, code=code, mode=mode)
        except (ValueError, OSError) as error:
            raise _error(code, "partial documentary carrier is absent, aliased or changed") from error

    project = Path(root)
    if context.workflow_version != 9 or context.step_atom_id not in {"CA-O-178", "CA-O-179"} or context.action_atom_id != "CA-O-169":
        raise _error("release-checkpoint-phase-mismatch", "documentary partial frontier is not selected native publication")
    identities = (context.action_run_id, context.step_run_id, context.workflow_run_id)
    if len(set(identities)) != 3:
        raise _error("release-checkpoint-binding-mismatch", "partial publication Run identities are ambiguous")
    snapshot = capture_snapshot(project)
    if snapshot.get("source_root") != work_journal.configured_journal_root(project).as_posix():
        raise _error("release-checkpoint-binding-mismatch", "partial frontier reader has another canonical Journal root")
    result = query(snapshot, {"mode": "full_events", "filter": '"event:/event" = "started" AND "event:/run/run_id" IN ('
                             + ", ".join(json.dumps(identity) for identity in identities) + ")", "limit": 4})
    if result.get("status") != "complete" or result.get("coverage", {}).get("complete") is not True or len(result.get("results", [])) != 3:
        raise _error("release-checkpoint-binding-mismatch", "partial frontier canonical starts are absent, ambiguous or incompletely covered")
    events = {}
    for match in result["results"]:
        event = work_journal.validate_sealed_event(match["event"])
        run = event.get("run", {})
        identity = run.get("run_id")
        if identity not in identities or identity in events or event.get("schema_version") != 5 or event.get("kind") != "workflow_execution":
            raise _error("release-checkpoint-binding-mismatch", "partial frontier has conflicting canonical Run starts")
        events[identity] = event
    action, step, workflow = (events[identity] for identity in identities)
    for event, kind, atom_id, version in ((action, "action", "CA-O-169", 5), (step, "step", context.step_atom_id, None), (workflow, "workflow", "CA-O-164", 9)):
        record = event["run"]
        source = record.get("definition", {})
        if (event.get("event") != "started" or record.get("kind") != kind or source.get("atom_id") != atom_id
                or (version is not None and source.get("version") != version)
                or event.get("author") != action.get("author") or event.get("action_id") != action.get("action_id")
                or event.get("llm_session") != action.get("llm_session")
                or hashlib.sha256(read_physical_native_carrier(
                    _file(project, _safe_path(source.get("path"), "canonical start source")),
                    code="release-checkpoint-binding-mismatch", mode=None)).hexdigest() != source.get("digest")
                or {"kind": kind, **source} not in event.get("definition_bindings", [])):
            raise _error("release-checkpoint-binding-mismatch", "partial frontier canonical source or attribution changed")
    if (action["run"].get("parent_run_id") != context.step_run_id or step["run"].get("parent_run_id") != context.workflow_run_id
            or "parent_run_id" in workflow["run"] or {"kind": "action", **action["run"]["definition"]} not in workflow.get("definition_bindings", [])):
        raise _error("release-checkpoint-binding-mismatch", "partial frontier canonical parent chain changed")
    settings = work_journal.resolve_settings_path(project)
    registry = read_physical_native_carrier(_file(project, (settings.parent / "operators_registry.toml").relative_to(project).as_posix()),
                                           code="release-checkpoint-binding-mismatch", mode=None)
    if sum(_registered_journal_author(record) == action.get("author") for record in parse_operators_registry(registry)) != 1:
        raise _error("release-checkpoint-binding-mismatch", "partial frontier canonical author is not an actual registered account")
    if pending is not None:
        event_id = _safe_path(pending["event_id"], "pending canonical event id")
        if "/" in event_id:
            raise _error("release-checkpoint-binding-mismatch", "pending canonical event id is not one identity")
        carrier = project / work_journal.configured_runtime_root(project) / "state/work_journal/pending" / f"{event_id}.json"
        pending_bytes = read_physical_native_carrier(_file(project, carrier.relative_to(project).as_posix()),
                                                    code="release-checkpoint-binding-mismatch", mode=None)
        _payload, event, _append_context, observed = work_journal._read_pending_event(project, event_id)
        if (json.loads(pending_bytes) != _payload or read_physical_native_carrier(carrier, code="release-checkpoint-binding-mismatch", mode=None) != pending_bytes
                or observed != carrier or event.get("run") != action["run"] or event.get("event") == "started"
                or event.get("outcome") != pending["event_outcome"] or event.get("author") != action["author"]
                or event.get("action_id") != action["action_id"] or event.get("llm_session") != action["llm_session"]
                or event.get("definition_bindings") != action.get("definition_bindings")):
            raise _error("release-checkpoint-binding-mismatch", "pending canonical recording differs from the exact partial publication occurrence")
        recorded = query(snapshot, {"mode": "full_events", "filter": '"event:/event_id" = ' + json.dumps(event_id), "limit": 2})
        if (recorded.get("status") != "complete" or recorded.get("coverage", {}).get("complete") is not True
                or len(recorded.get("results", [])) > 1
                or any(work_journal.validate_sealed_event(row["event"]) != event for row in recorded.get("results", []))):
            raise _error("release-checkpoint-binding-mismatch", "pending recording has ambiguous or changed canonical Journal evidence")


def _validate_native_partial_frontier(root: str, *, state: Mapping[str, Any],
                                      in_progress: SelectedReleaseActionContext | None,
                                      contexts: Mapping[int, SelectedReleaseActionContext],
                                      results: Mapping[int, ReleasePhaseResult],
                                      pending: Mapping[int, Mapping[str, str]]) -> None:
    from release_promotion import retained_native_promotion_packet

    index = 11 if 11 in results and results[11].outcome in {"effect_uncertain", "pending"} else 10
    context = in_progress if in_progress is not None else contexts.get(index)
    if context is None or (in_progress is None and (index not in results or results[index].outcome not in {"effect_uncertain", "pending"})):
        raise _error("release-checkpoint-phase-mismatch", "partial native publication hint lacks its validated stopped or in-progress occurrence")
    retained_native_promotion_packet(state["candidate"], state["portable_compilation"], state["portable_suite"],
                                    state["build"], state["verification"], state["e2e"], state["full_gate"], state["prepared_portable_package"])
    _reopen_native_partial_frontier_start(root, context, pending.get(11 if context.step_atom_id == "CA-O-179" else 10))


def _encode_native_release_action_checkpoint(
    run: ReleaseActionRun, *, shared_recordings: Mapping[int, Mapping[str, Any]] | None,
    pending_recordings: Mapping[int, Mapping[str, Any]] | None,
) -> bytes:
    root = str(Path(run.project_root).resolve(strict=True))
    request = _load_model(run.request.model_dump(mode="json", by_alias=True), ReleaseVersionRequest, "request")
    if request.project_root != root or _fingerprint(request) != _sha256(run.frozen_parameters_sha256, "frozen_parameters_sha256"):
        raise _error("release-checkpoint-binding-mismatch", "native run request, root, or fingerprint is not frozen")
    contexts = []
    for index, context in sorted(run.contexts.items()):
        if context.workflow_version != 11:
            raise _error("release-checkpoint-binding-mismatch", "native checkpoint context is not current O164@11")
        _load_context(_context_value(context), _index(index, "contexts.index"), root=root,
                      workflow_run_id=run.workflow_run_id, fingerprint=run.frozen_parameters_sha256)
        contexts.append({"index": index, "context": _context_value(context)})
    state = {name: _native_state_value(run, name) for name in _NATIVE_STATE_NAMES}
    partial_hint = _native_partial_publication_hint({
        "in_progress": run.in_progress, "next_phase": run.next_phase, "stopped": run.stopped,
        "results": [{"index": index, "result": {"outcome": result.outcome}} for index, result in run.results.items()],
    })
    restored_state = _load_native_state(state, root, documentary_publication_frontier=partial_hint)
    candidate = restored_state["candidate"]
    results = []
    for index, result in sorted(run.results.items()):
        if candidate is None or index not in run.contexts:
            raise _error("release-checkpoint-phase-mismatch", "native result has no frozen candidate or context")
        encoded = _native_result_value(result, index)
        _load_native_result(encoded, index, run.contexts[index], candidate, restored_state)
        results.append({"index": index, "result": encoded})
    if run.in_progress is not None:
        if run.in_progress.workflow_version != 11:
            raise _error("release-checkpoint-binding-mismatch", "native in-progress context is not current O164@11")
        _load_context(_context_value(run.in_progress), run.next_phase, root=root,
                      workflow_run_id=run.workflow_run_id, fingerprint=run.frozen_parameters_sha256)
    _validate_phase_continuity(next_phase=run.next_phase, stopped=run.stopped, in_progress=run.in_progress,
                               contexts=run.contexts, results=run.results)
    _validate_native_result_outputs(run.results, restored_state)
    recording_payload = _shared_recordings_value(shared_recordings, run.results)
    pending_payload = _pending_recordings_value(
        pending_recordings, run.results, {record["index"]: record for record in recording_payload},
    )
    if partial_hint:
        _validate_native_partial_frontier(root, state=restored_state, in_progress=run.in_progress,
                                          contexts=run.contexts, results=run.results,
                                          pending={row["index"]: {"event_id": row["event_id"], "event_outcome": row["event_outcome"]} for row in pending_payload})
    payload = {
        "schema": NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA,
        "kind": "release_action_run",
        "sha256": "0" * 64,
        "project_root": root,
        "workflow_run_id": _text(run.workflow_run_id, "workflow_run_id"),
        "frozen_parameters_sha256": _sha256(run.frozen_parameters_sha256, "frozen_parameters_sha256"),
        "request": _dump_model(request, ReleaseVersionRequest, "request"),
        "next_phase": run.next_phase,
        "stopped": run.stopped,
        "in_progress": None if run.in_progress is None else _context_value(run.in_progress),
        "contexts": contexts,
        "results": results,
        "shared_recordings": recording_payload,
        "pending_recordings": pending_payload,
        "state": state,
        "local_helper_binding": _local_helper_binding_value(run.local_helper_binding),
    }
    if type(run.stopped) is not bool:
        raise _error("release-checkpoint-invalid", "native stopped must be a boolean")
    payload["sha256"] = release_action_checkpoint_sha256(payload)
    return canonical_json(payload)


def encode_release_action_checkpoint(
    run: ReleaseActionRun, *, shared_recordings: Mapping[int, Mapping[str, Any]] | None = None,
    pending_recordings: Mapping[int, Mapping[str, Any]] | None = None,
) -> bytes:
    """Return one canonical, closed JSON checkpoint without persisting it."""

    if type(run) is not ReleaseActionRun:
        raise _error("release-checkpoint-invalid", "checkpoint requires one private ReleaseActionRun")
    if _native_portable_run(run):
        return _encode_native_release_action_checkpoint(
            run, shared_recordings=shared_recordings, pending_recordings=pending_recordings,
        )
    root = str(Path(run.project_root).resolve(strict=True))
    if root != run.project_root:
        raise _error("release-checkpoint-binding-mismatch", "run root is not canonical")
    request = _load_model(run.request.model_dump(mode="json", by_alias=True), ReleaseVersionRequest, "request")
    if request.project_root != root or _fingerprint(request) != _sha256(run.frozen_parameters_sha256, "frozen_parameters_sha256"):
        raise _error("release-checkpoint-binding-mismatch", "run request, root, or fingerprint is not frozen")
    contexts = []
    for index, context in sorted(run.contexts.items()):
        index = _index(index, "contexts.index")
        _load_context(_context_value(context), index, root=root, workflow_run_id=run.workflow_run_id, fingerprint=run.frozen_parameters_sha256)
        contexts.append({"index": index, "context": _context_value(context)})
    results = []
    candidate = run.candidate
    if candidate is not None:
        candidate = _load_candidate(_candidate_value(candidate), root)
    for index, result in sorted(run.results.items()):
        index = _index(index, "results.index")
        if candidate is None or index not in run.contexts:
            raise _error("release-checkpoint-phase-mismatch", "result has no frozen candidate or context")
        _load_result(_result_value(result), index, run.contexts[index], candidate)
        results.append({"index": index, "result": _result_value(result)})
    if run.in_progress is not None:
        _load_context(_context_value(run.in_progress), run.next_phase, root=root, workflow_run_id=run.workflow_run_id, fingerprint=run.frozen_parameters_sha256)
    state = {name: _state_value(run, name) for name in _STATE_NAMES}
    reader = _StateReader(root)
    restored_state = {name: reader.read(name, state[name]) for name in _STATE_NAMES}
    _validate_state_dependencies(restored_state, reader.candidate, restored_state["preflight"])
    _validate_phase_continuity(next_phase=run.next_phase, stopped=run.stopped, in_progress=run.in_progress,
                               contexts=run.contexts, results=run.results)
    _validate_result_outputs(run.results, restored_state)
    recording_payload = _shared_recordings_value(shared_recordings, run.results)
    pending_recording_payload = _pending_recordings_value(
        pending_recordings, run.results,
        {record["index"]: record for record in recording_payload},
    )
    payload = {
        "schema": RELEASE_ACTION_CHECKPOINT_SCHEMA,
        "kind": "release_action_run",
        "sha256": "0" * 64,
        "project_root": root,
        "workflow_run_id": _text(run.workflow_run_id, "workflow_run_id"),
        "frozen_parameters_sha256": _sha256(run.frozen_parameters_sha256, "frozen_parameters_sha256"),
        "request": _dump_model(request, ReleaseVersionRequest, "request"),
        "next_phase": run.next_phase,
        "stopped": run.stopped,
        "in_progress": None if run.in_progress is None else _context_value(run.in_progress),
        "contexts": contexts,
        "results": results,
        "shared_recordings": recording_payload,
        "pending_recordings": pending_recording_payload,
        "state": state,
    }
    if type(run.stopped) is not bool:
        raise _error("release-checkpoint-invalid", "stopped must be a boolean")
    payload["sha256"] = release_action_checkpoint_sha256(payload)
    return canonical_json(payload)


def dump_release_checkpoint(
    run: ReleaseActionRun, *, shared_recordings: Mapping[int, Mapping[str, Any]] | None = None,
    pending_recordings: Mapping[int, Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    """Return a closed, digest-sealed checkpoint envelope without persisting it."""

    return json.loads(encode_release_action_checkpoint(
        run, shared_recordings=shared_recordings, pending_recordings=pending_recordings,
    ).decode("utf-8"))


def derive_unknown_effect_terminal_checkpoint(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Derive, but never replace, N15's stopped unknown-effect frontier.

    The original checkpoint is historical evidence for the host-loss boundary.
    This narrowly scoped codec operation restores that evidence, proves the
    one admitted pre-effect frontier, and emits a *separate* terminal
    checkpoint.  It has no Journal, provider, Docker, or filesystem effect.

    Its caller is responsible for retaining the original checkpoint bytes and
    choosing the governed companion carrier for the returned payload.
    """

    if not isinstance(payload, Mapping):
        raise _error("release-checkpoint-invalid", "unknown-effect resolution requires one checkpoint envelope")
    run, shared_recordings, pending_recordings = _restore_release_action_checkpoint(canonical_json(dict(payload)))
    context = run.in_progress
    if (
        run.workflow_run_id != "release-epic-resume-20261006-N15"
        or run.next_phase != 4
        or run.stopped is not False
        or context is None
        or set(run.contexts) != {0, 1, 2, 3, 4}
        or set(run.results) != {0, 1, 2, 3}
        or any(run.results[index].outcome != "completed" for index in range(4))
        or set(shared_recordings) != {0, 1, 2, 3}
        or pending_recordings
    ):
        raise _error("release-checkpoint-unknown-effect-mismatch", "checkpoint is not the admitted N15 unknown-effect frontier")
    if any(
        record.get("terminal_outcome") != "completed"
        or not isinstance(record.get("receipt_refs"), tuple)
        or len(record["receipt_refs"]) != 1
        for record in shared_recordings.values()
    ):
        raise _error("release-checkpoint-unknown-effect-mismatch", "checkpoint predecessor receipts are not exact completed records")
    step, action, phase = PHASES[4]
    if (
        context != run.contexts[4]
        or context.workflow_run_id != run.workflow_run_id
        or context.step_run_id != "release-epic-resume-20261006-N15:step:5"
        or context.action_run_id != "release-epic-resume-20261006-N15:step:5:action:1"
        or (context.step_atom_id, context.action_atom_id, phase) != (step, action, "closed_unit_gate")
        or run.candidate is None
    ):
        raise _error("release-checkpoint-unknown-effect-mismatch", "checkpoint has a different N15 in-progress occurrence")

    run.results[4] = ReleasePhaseResult(
        workflow_run_id=context.workflow_run_id,
        step_run_id=context.step_run_id,
        action_run_id=context.action_run_id,
        step_atom_id=step,
        action_atom_id=action,
        phase=phase,
        outcome="effect_uncertain",
        reason="unknown_effect",
        candidate_snapshot_manifest_sha256=run.candidate.manifest.sha256,
        attempted_effects=(),
        effect_evidence_refs=(),
        declared_run_receipt_refs=(),
    )
    run.in_progress = None
    run.stopped = True
    # The terminal companion must retain the same completed predecessor
    # receipts.  The original carrier remains untouched; this copy only adds
    # the stopped phase-four uncertainty result.
    return dump_release_checkpoint(run, shared_recordings=shared_recordings, pending_recordings={})


def _restore_native_release_action_checkpoint(
    payload: Mapping[str, Any], *, image_executor: AdmittedImageExecutor | None = None,
) -> tuple[ReleaseActionRun, dict[int, dict[str, Any]], dict[int, dict[str, str]]]:
    """Restore the closed current O164@11 portable frontier without coercion."""

    source, helper_binding = _native_checkpoint_envelope(dict(payload), "native checkpoint")
    if source["schema"] not in {NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA, LEGACY_NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA} or source["kind"] != "release_action_run":
        raise _error("release-checkpoint-schema-unsupported", "native checkpoint schema or kind is not supported")
    if _sha256(source["sha256"], "sha256") != release_action_checkpoint_sha256(source):
        raise _error("release-checkpoint-digest-mismatch", "native checkpoint content digest does not match its canonical bytes")
    root = str(Path(_text(source["project_root"], "project_root")).resolve(strict=True))
    if source["project_root"] != root:
        raise _error("release-checkpoint-binding-mismatch", "native checkpoint root is not canonical")
    workflow_run_id = _text(source["workflow_run_id"], "workflow_run_id")
    fingerprint = _sha256(source["frozen_parameters_sha256"], "frozen_parameters_sha256")
    request = _load_model(source["request"], ReleaseVersionRequest, "request")
    if request.project_root != root or _fingerprint(request) != fingerprint:
        raise _error("release-checkpoint-binding-mismatch", "native checkpoint request root or fingerprint does not match")
    if type(source["next_phase"]) is not int or not 0 <= source["next_phase"] <= len(PHASES) or type(source["stopped"]) is not bool:
        raise _error("release-checkpoint-phase-mismatch", "native checkpoint next phase or stopped value is invalid")
    if image_executor is not None and (
        type(image_executor) is not AdmittedImageExecutor or image_executor.project_root != root
        or image_executor.workflow_run_id != workflow_run_id or not callable(getattr(image_executor.executor, "run", None))
    ):
        raise _error("release-checkpoint-executor-unadmitted", "restored native Run executor is not externally re-admitted")
    partial_hint = _native_partial_publication_hint(source)
    state = _load_native_state(source["state"], root, documentary_publication_frontier=partial_hint)
    candidate = state["candidate"]
    contexts: dict[int, SelectedReleaseActionContext] = {}
    if not isinstance(source["contexts"], list):
        raise _error("release-checkpoint-invalid", "native contexts must be a canonical list")
    for entry in source["contexts"]:
        record = _mapping(entry, {"index", "context"}, "native context record")
        index = _index(record["index"], "native contexts.index")
        if index in contexts:
            raise _error("release-checkpoint-invalid", "native contexts repeat a selected phase")
        context = _load_context(record["context"], index, root=root, workflow_run_id=workflow_run_id, fingerprint=fingerprint)
        if context.workflow_version != 11:
            raise _error("release-checkpoint-binding-mismatch", "native checkpoint context is not current O164@11")
        contexts[index] = context
    if not isinstance(source["results"], list) or candidate is None:
        if source["results"] or candidate is not None:
            raise _error("release-checkpoint-invalid", "native results require one frozen candidate")
        results: dict[int, ReleasePhaseResult] = {}
    else:
        results = {}
        for entry in source["results"]:
            record = _mapping(entry, {"index", "result"}, "native result record")
            index = _index(record["index"], "native results.index")
            if index in results or index not in contexts:
                raise _error("release-checkpoint-invalid", "native result repeats or lacks selected context")
            results[index] = _load_native_result(record["result"], index, contexts[index], candidate, state)
    in_progress = None
    if source["in_progress"] is not None:
        in_progress = _load_context(source["in_progress"], source["next_phase"], root=root,
                                    workflow_run_id=workflow_run_id, fingerprint=fingerprint)
        if in_progress.workflow_version != 11:
            raise _error("release-checkpoint-binding-mismatch", "native in-progress context is not current O164@11")
    _validate_phase_continuity(next_phase=source["next_phase"], stopped=source["stopped"], in_progress=in_progress,
                               contexts=contexts, results=results)
    _validate_native_result_outputs(results, state)
    shared_recordings = _load_shared_recordings(source["shared_recordings"], results)
    pending_recordings = _load_pending_recordings(source["pending_recordings"], results, shared_recordings)
    if partial_hint:
        _validate_native_partial_frontier(root, state=state, in_progress=in_progress,
                                          contexts=contexts, results=results, pending=pending_recordings)
    return ReleaseActionRun(
        project_root=root,
        workflow_run_id=workflow_run_id,
        frozen_parameters_sha256=fingerprint,
        request=request,
        image_executor=image_executor,
        next_phase=source["next_phase"],
        stopped=source["stopped"],
        in_progress=in_progress,
        contexts=contexts,
        results=results,
        local_helper_binding=helper_binding,
        **state,
    ), shared_recordings, pending_recordings


def _restore_release_action_checkpoint(
    checkpoint: bytes | str, *, image_executor: AdmittedImageExecutor | None = None,
) -> tuple[ReleaseActionRun, dict[int, dict[str, Any]], dict[int, dict[str, str]]]:
    """Restore exact private state; an executor is deliberately reinjected externally."""

    decoded = _canonical_input(checkpoint)
    if decoded.get("schema") in {NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA, LEGACY_NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA}:
        return _restore_native_release_action_checkpoint(decoded, image_executor=image_executor)
    payload = _mapping(decoded, {
        "schema", "kind", "sha256", "project_root", "workflow_run_id", "frozen_parameters_sha256", "request",
        "next_phase", "stopped", "in_progress", "contexts", "results", "shared_recordings", "pending_recordings", "state",
    }, "checkpoint")
    if payload["schema"] != RELEASE_ACTION_CHECKPOINT_SCHEMA or payload["kind"] != "release_action_run":
        raise _error("release-checkpoint-schema-unsupported", "checkpoint schema or kind is not supported")
    if _sha256(payload["sha256"], "sha256") != release_action_checkpoint_sha256(payload):
        raise _error("release-checkpoint-digest-mismatch", "checkpoint content digest does not match its canonical bytes")
    root = str(Path(_text(payload["project_root"], "project_root")).resolve(strict=True))
    if payload["project_root"] != root:
        raise _error("release-checkpoint-binding-mismatch", "checkpoint root is not canonical")
    workflow_run_id = _text(payload["workflow_run_id"], "workflow_run_id")
    fingerprint = _sha256(payload["frozen_parameters_sha256"], "frozen_parameters_sha256")
    request = _load_model(payload["request"], ReleaseVersionRequest, "request")
    if request.project_root != root or _fingerprint(request) != fingerprint:
        raise _error("release-checkpoint-binding-mismatch", "request root or fingerprint does not match checkpoint")
    if type(payload["next_phase"]) is not int or not 0 <= payload["next_phase"] <= len(PHASES) or type(payload["stopped"]) is not bool:
        raise _error("release-checkpoint-phase-mismatch", "checkpoint next phase or stopped value is invalid")
    if image_executor is not None and (
        type(image_executor) is not AdmittedImageExecutor
        or image_executor.project_root != root
        or image_executor.workflow_run_id != workflow_run_id
        or not callable(getattr(image_executor.executor, "run", None))
    ):
        raise _error("release-checkpoint-executor-unadmitted", "restored Run executor is not externally re-admitted")
    reader = _StateReader(root)
    state_payload = _mapping(payload["state"], set(_STATE_NAMES), "state")
    state = {name: reader.read(name, state_payload[name]) for name in _STATE_NAMES}
    candidate = reader.candidate
    _validate_state_dependencies(state, candidate, state["preflight"])
    contexts: dict[int, SelectedReleaseActionContext] = {}
    if not isinstance(payload["contexts"], list):
        raise _error("release-checkpoint-invalid", "contexts must be a canonical list")
    for entry in payload["contexts"]:
        record = _mapping(entry, {"index", "context"}, "context record")
        index = _index(record["index"], "contexts.index")
        if index in contexts:
            raise _error("release-checkpoint-invalid", "contexts repeat a selected phase")
        contexts[index] = _load_context(record["context"], index, root=root, workflow_run_id=workflow_run_id, fingerprint=fingerprint)
    if not isinstance(payload["results"], list) or candidate is None:
        if payload["results"] or candidate is not None:
            raise _error("release-checkpoint-invalid", "results require one frozen candidate")
        results: dict[int, ReleasePhaseResult] = {}
    else:
        results = {}
        for entry in payload["results"]:
            record = _mapping(entry, {"index", "result"}, "result record")
            index = _index(record["index"], "results.index")
            if index in results or index not in contexts:
                raise _error("release-checkpoint-invalid", "result repeats or lacks its selected context")
            results[index] = _load_result(record["result"], index, contexts[index], candidate)
    in_progress = None
    if payload["in_progress"] is not None:
        in_progress = _load_context(payload["in_progress"], payload["next_phase"], root=root,
                                    workflow_run_id=workflow_run_id, fingerprint=fingerprint)
    _validate_phase_continuity(next_phase=payload["next_phase"], stopped=payload["stopped"], in_progress=in_progress,
                               contexts=contexts, results=results)
    _validate_result_outputs(results, state)
    shared_recordings = _load_shared_recordings(payload["shared_recordings"], results)
    pending_recordings = _load_pending_recordings(payload["pending_recordings"], results, shared_recordings)
    return ReleaseActionRun(
        project_root=root,
        workflow_run_id=workflow_run_id,
        frozen_parameters_sha256=fingerprint,
        request=request,
        image_executor=image_executor,
        next_phase=payload["next_phase"],
        stopped=payload["stopped"],
        in_progress=in_progress,
        contexts=contexts,
        results=results,
        **state,
    ), shared_recordings, pending_recordings


def restore_release_action_checkpoint(
    checkpoint: bytes | str, *, image_executor: AdmittedImageExecutor | None = None,
) -> ReleaseActionRun:
    """Restore exact private state; an executor is deliberately reinjected externally."""

    run, _shared_recordings, _pending_recordings = _restore_release_action_checkpoint(
        checkpoint, image_executor=image_executor,
    )
    return run


def load_release_checkpoint(
    payload: Mapping[str, Any], *, expected_request: ReleaseVersionRequest | Mapping[str, Any],
    expected_workflow_run_id: str, image_executor: AdmittedImageExecutor | None = None,
) -> tuple[ReleaseActionRun, dict[int, dict[str, Any]]]:
    """Restore a sealed envelope only for the caller's exact frozen Run.

    The shared terminal records are returned separately because the private
    ``ReleaseActionRun`` intentionally owns no Journal or dispatcher state.
    Their receipt references must be admitted by the shared dispatcher before
    it treats an effect as terminal; this function never does that admission.
    """

    if not isinstance(payload, Mapping):
        raise _error("release-checkpoint-invalid", "checkpoint envelope must be one object")
    expected = expected_request if type(expected_request) is ReleaseVersionRequest else _load_model(
        expected_request, ReleaseVersionRequest, "expected_request",
    )
    expected_id = _text(expected_workflow_run_id, "expected_workflow_run_id")
    run, recordings, _pending_recordings = _restore_release_action_checkpoint(
        canonical_json(dict(payload)), image_executor=image_executor,
    )
    if run.workflow_run_id != expected_id or run.request != expected or run.frozen_parameters_sha256 != _fingerprint(expected):
        raise _error("release-checkpoint-binding-mismatch", "checkpoint is not for the exact expected frozen Release Run")
    return run, recordings


def extract_pending_recordings(payload: Mapping[str, Any]) -> Mapping[int, Mapping[str, str]]:
    """Return immutable pending-recorder identities from one sealed checkpoint.

    The returned values are recovery hints only.  A caller must still reopen
    the exact pending Journal Event through the canonical shared recorder and
    obtain a durable receipt before it may regard a phase as terminal.
    """

    if not isinstance(payload, Mapping):
        raise _error("release-checkpoint-invalid", "checkpoint envelope must be one object")
    _run, _recordings, pending_recordings = _restore_release_action_checkpoint(canonical_json(dict(payload)))
    return MappingProxyType({
        index: MappingProxyType(dict(record))
        for index, record in pending_recordings.items()
    })


__all__ = [
    "RELEASE_ACTION_CHECKPOINT_SCHEMA",
    "NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA",
    "derive_unknown_effect_terminal_checkpoint",
    "release_action_checkpoint_sha256",
    "dump_release_checkpoint",
    "encode_release_action_checkpoint",
    "load_release_checkpoint",
    "extract_pending_recordings",
    "restore_release_action_checkpoint",
]
