"""Stage and reopen one inert native D604 release-proof fragment.

This is deliberately not an installation publisher.  It binds already
verified package, context, command-stage, lock, and prospective-selector
bytes, but it does not make the selector current or permit command execution.
"""

from __future__ import annotations

from dataclasses import dataclass, fields as dataclass_fields
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import tomllib

from framework_package import (
    FrameworkPackageError,
    VerifiedFrameworkPackage,
    verify_current_package_selector,
    verify_framework_package,
    provide_installation_package_evidence,
)
from installation_context import TargetProjectContext, TargetProjectRequest
from framework_installation import PortableInstallationRequest
import portable_methodology_installation as methodology
from portable_methodology_installation import (
    PortableMethodologyDelivery, CandidatePortableMethodologyDelivery, TargetPortableMethodologyDelivery,
)
from installation_transaction import InstallationPublicationLock, InstallationTransactionError
from installed_mcp_binding import InstalledMcpBindingError, _context as _read_d600_context
from portable_runtime_materialization import (
    RuntimeCommandStage,
    _canonical_digest,
    _reopen_candidate_package,
    _read_stage_regular,
    _read_target_regular,
    _write_new,
    _validate_fragment_documents,
)
from retained_full_gate_packet import RetainedNativeFullGatePacket


_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_PACKAGE_CURRENT = Path(".caprmedio_install/current.toml")
_PACKAGE_RELEASES = Path(".caprmedio_install/releases")
_CONTEXTS = Path(".caprmedio_runtime/installation/contexts")
_COMMAND_STAGING = Path(".caprmedio_tmp/installation/staging")
_PROOF_STAGING = Path(".caprmedio_tmp/installation/proofs")
_COMMAND_NAME = "command.toml"
_ENVIRONMENT_NAME = "environment.toml"
_WRAPPER_NAME = "wrapper"
_STAGE_MANIFEST_NAME = "stage-manifest.toml"
_PROOF_NAME = "release-proof.toml"
_SELECTOR_NAME = "selector.toml"
_SELECTOR_KEYS = frozenset(
    {
        "schema_version",
        "package_manifest_sha256",
        "target_project_context_sha256",
        "state_generation",
        "installation_lock_generation",
        "image_digest",
    }
)
_PROOF_KEYS = (
    "schema_version",
    "package_manifest_sha256",
    "framework_version",
    "version_toml_sha256",
    "source_catalog_sha256",
    "full_gate_receipt_sha256",
    "image_digest",
    "target_project_context_sha256",
    "state_generation",
    "installation_lock_generation",
    "installation_command_sha256",
    "command_sha256",
    "command_stage_manifest_sha256",
    "methodology_delivery_manifest_ref",
    "methodology_delivery_manifest_sha256",
    "selector_sha256",
)


class NativeInstallationProofError(RuntimeError):
    """A stable refusal while staging or reopening prospective D604 evidence."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


@dataclass(frozen=True)
class NativeInstallationProofRequest:
    """Only typed, already-admitted inputs for an inert proof stage."""

    package: VerifiedFrameworkPackage
    target_context: TargetProjectContext
    command_stage: RuntimeCommandStage
    prospective_selector: bytes
    methodology_delivery: PortableMethodologyDelivery | TargetPortableMethodologyDelivery


@dataclass(frozen=True)
class CandidateNativeInstallationProofRequest:
    """Candidate-mode D604 proof inputs before either selector is published."""

    package: VerifiedFrameworkPackage
    target_context: TargetProjectContext
    command_stage: RuntimeCommandStage
    prospective_package_selector: bytes
    prospective_selector: bytes
    full_gate_packet: RetainedNativeFullGatePacket
    methodology_delivery: PortableMethodologyDelivery | TargetPortableMethodologyDelivery | CandidatePortableMethodologyDelivery


@dataclass(frozen=True)
class NativeInstallationProof:
    """Reopened D604 evidence; this result grants neither authority nor a pass."""

    root: Path
    proof_path: Path
    selector_path: Path
    package_manifest_sha256: str
    framework_version: str
    version_toml_sha256: str
    source_catalog_sha256: str
    full_gate_receipt_sha256: str
    image_digest: str
    target_project_context_sha256: str
    state_generation: int
    installation_lock_generation: str
    installation_command_sha256: str
    command_sha256: str
    command_stage_manifest_sha256: str
    methodology_delivery_manifest_ref: str
    methodology_delivery_manifest_sha256: str
    selector_sha256: str


@dataclass(frozen=True)
class NativeMethodologyDeliveryBinding:
    """Physical Methodology fact; the digest covers complete manifest bytes."""

    manifest_ref: str
    manifest_sha256: str
    delivery: PortableMethodologyDelivery | TargetPortableMethodologyDelivery | CandidatePortableMethodologyDelivery
    gate_receipt_sha256: str | None


def _delivery_context(root: Path, package: VerifiedFrameworkPackage, digest: str):
    _read_d600_context(root, digest, verified_package=package)
    raw = _read_target_regular(root, _CONTEXTS / f"{digest}.toml", code="native-proof-delivery-context-invalid", label="delivery context")
    document = _parse_toml(raw, code="native-proof-delivery-context-invalid", label="delivery context")
    values = {field.name: document[field.name] for field in dataclass_fields(TargetProjectContext)
              if field.name != "package_evidence" and field.name in document}
    for name in ("methodology_source_identities",):
        if name in values and isinstance(values[name], list):
            values[name] = tuple(values[name])
    context = TargetProjectContext(**values, package_evidence=provide_installation_package_evidence(package.root))
    if context.sha256 != digest or context.with_digest_toml() != raw:
        _refuse("native-proof-delivery-context-invalid", "delivery context is not the exact canonical target carrier")
    control = root / context.control_child_relpath
    target = TargetProjectRequest(
        target_root=root, control_child=context.control_child_relpath, mode=context.mode,
        target_project_identity=context.target_project_identity,
        settings_path=control / "caprmedio_project_settings.toml",
        project_structure_path=control / "project_structure.toml",
        operators_registry_path=control / "operators_registry.toml",
        repository_identity=context.repository_identity, root_locator=context.root_locator,
        package_root=package.root, package_evidence=context.package_evidence,
    )
    return context, target


def _read_delivery(root: Path, package: VerifiedFrameworkPackage, *, target_context_sha256: str,
                   manifest_ref: str, expected_manifest_sha256: str,
                   full_gate_packet: RetainedNativeFullGatePacket | None) -> NativeMethodologyDeliveryBinding:
    context, target = _delivery_context(root, package, target_context_sha256)
    request = PortableInstallationRequest(target=target, retained_gate_receipt_path=root / "unused",
                                          full_gate_packet=full_gate_packet)
    _, source_relative, output_relative = methodology._context_paths_for(request, context)
    expected_ref = (output_relative / methodology._MANIFEST_NAME).as_posix()
    if manifest_ref != expected_ref:
        _refuse("native-proof-delivery-target-mismatch", "delivery manifest is not this target's canonical Applicable Methodology output")
    raw = _read_target_regular(root, Path(expected_ref), code="native-proof-delivery-stale", label="Methodology delivery manifest", expected_mode=0o644)
    if _sha256(raw) != expected_manifest_sha256:
        _refuse("native-proof-delivery-stale", "delivery manifest raw bytes differ from proof binding")
    document = json.loads(raw.decode("utf-8"))
    if not isinstance(document, dict) or raw != methodology._canonical_json(document) + b"\n":
        _refuse("native-proof-delivery-invalid", "delivery manifest is not canonical JSON")
    unsigned = dict(document)
    semantic_digest = unsigned.pop("sha256", None)
    if semantic_digest != methodology._digest(methodology._canonical_json(unsigned)):
        _refuse("native-proof-delivery-invalid", "delivery manifest semantic checksum is invalid")
    common = {
        "schema": methodology._MANIFEST_SCHEMA, "package_manifest_sha256": package.manifest_digest,
        "source_catalog_sha256": package.source_catalog_sha256, "target_project_context_sha256": context.sha256,
    }
    if any(document.get(key) != value for key, value in common.items()):
        _refuse("native-proof-delivery-binding-mismatch", "delivery manifest names another package, catalog or context")
    output_root = root / output_relative
    package_compiler, compiler_binding = methodology.open_admitted_package_compiler(package)
    actual_files = methodology._projection_records(output_root, compiler_module=package_compiler)
    if not actual_files or document.get("files") != [file.__dict__ for file in actual_files]:
        _refuse("native-proof-delivery-stale", "delivery output bytes or modes differ from the manifest")
    for file in actual_files:
        actual_payload = _read_target_regular(root, output_relative / file.path,
            code="native-proof-delivery-stale", label="Methodology output", expected_mode=file.mode)
        if _sha256(actual_payload) != file.sha256:
            _refuse("native-proof-delivery-stale", "delivery output changed while reopening its inventory")
    output_digest, manifest_path = methodology._reopen_delivery(output_root, actual_files, semantic_digest,
                                                               compiler_module=package_compiler)
    if document.get("output_tree_sha256") != output_digest:
        _refuse("native-proof-delivery-stale", "delivery output tree checksum differs")
    if "candidate_snapshot_manifest_sha256" in document:
        required = set(common) | {"candidate_snapshot_manifest_sha256", "candidate_run_id", "gate_receipt_sha256",
            "frozen_manifest_sha256", "export_inventory_sha256", "export_seal_sha256", "compiled_manifest_sha256",
            "source_export_sha256", "output_tree_sha256", "files", "sha256"}
        if set(document) != required or not isinstance(full_gate_packet, RetainedNativeFullGatePacket):
            _refuse("native-proof-delivery-gate-required", "candidate delivery requires its concrete retained Full Gate packet")
        from release_full_gate import verify_detached_native_full_gate_evidence
        packet = full_gate_packet
        verify_detached_native_full_gate_evidence(packet.artifact_root, packet.retained_candidate, packet.suite,
                                                 packet.build, packet.verification, packet.e2e, packet.evidence)
        (source_root, compiled_root, frozen, inventory, seal, compiled_manifest, source_files,
         compiled_files, candidate_sha, run_id) = methodology._read_private_candidate_delivery(request, package)
        bindings = {
            "candidate_snapshot_manifest_sha256": candidate_sha, "candidate_run_id": run_id,
            "gate_receipt_sha256": packet.evidence.receipt_sha256, "frozen_manifest_sha256": frozen,
            "export_inventory_sha256": inventory, "export_seal_sha256": seal,
            "compiled_manifest_sha256": compiled_manifest,
            "source_export_sha256": methodology._digest(methodology._canonical_json([file.__dict__ for file in source_files])),
        }
        if any(document.get(key) != value for key, value in bindings.items()) or actual_files != compiled_files:
            _refuse("native-proof-delivery-binding-mismatch", "candidate delivery differs from actual Full Gate compilation")
        published_source = methodology._source_export_root(root)
        if methodology._tree_records(published_source) != source_files:
            _refuse("native-proof-delivery-stale", "published source export differs from retained gated sources")
        delivery = CandidatePortableMethodologyDelivery(
            package.manifest_digest, package.source_catalog_sha256, context.sha256,
            packet.evidence.receipt_sha256, candidate_sha, run_id, bindings["source_export_sha256"],
            output_digest, semantic_digest, published_source, output_root, manifest_path, actual_files,
        )
    else:
        base_keys = set(common) | {"compiler_sha256", "compiler_frontier_sha256", "source_view_sha256",
            "authoring_source_sha256", "source_members", "output_tree_sha256", "files", "sha256"}
        target_prepared = "target_preparation_sha256" in document
        if set(document) != base_keys | ({"gate_receipt_sha256", "target_preparation_sha256"} if target_prepared else set()):
            _refuse("native-proof-delivery-invalid", "target delivery manifest schema is not closed")
        selected = methodology._target_methodology_identities(context)
        members = methodology._selected_members(package, methodology._catalog(package), selected, context.package_evidence.source_pins)
        sources = methodology._target_source_members(members)
        candidates = []
        for member in members:
            if member.kind == methodology._SUPPORT_KIND:
                methodology._validate_support(member, compiler_module=package_compiler)
            else:
                candidates.append(methodology._candidate(member, output_relative=output_relative, compiler_module=package_compiler))
        candidates.sort(key=package_compiler.candidate_sort_key)
        frontier = package_compiler.frontier_digest(candidates)
        by_package_path = {member.package_path.as_posix(): member for member in members}
        final_package_root = root / _PACKAGE_RELEASES / package.manifest_digest
        for file in actual_files:
            if file.mode != 0o644:
                _refuse("native-proof-delivery-invalid", "direct projection output mode is not canonical")
            projected = _read_target_regular(root, output_relative / file.path,
                code="native-proof-delivery-stale", label="direct Methodology projection", expected_mode=0o644)
            matches = 0
            for candidate in candidates:
                if (Path(candidate.role_directory) / candidate.basename).as_posix() != file.path:
                    continue
                member = by_package_path[candidate.source_path]
                relation = Path(os.path.relpath(final_package_root / member.package_path,
                    start=root / output_relative / candidate.role_directory)).as_posix()
                try:
                    package_compiler.validate_projection_source_preservation(
                        member.payload, projected, relation, candidate)
                except package_compiler.CompileError:
                    continue
                matches += 1
            if matches != 1:
                _refuse("native-proof-delivery-source-mismatch", "direct projection is not preserved admitted source with canonical final-package metadata")
        source_view = (methodology._target_source_view_sha256(sources) if target_prepared else
            methodology._digest(methodology._canonical_json([methodology.PortableMethodologyFile(
                member.source_relative.as_posix(), member.sha256, member.mode).__dict__
                for member in sorted(members, key=lambda member: member.source_relative.as_posix())])))
        bindings = {
            "compiler_sha256": compiler_binding.sha256,
            "compiler_frontier_sha256": frontier, "source_view_sha256": source_view,
            "authoring_source_sha256": methodology._tree_digest(methodology._directory(root, source_relative, missing_ok=True)),
            "source_members": [source.__dict__ for source in sources],
        }
        if any(document.get(key) != value for key, value in bindings.items()):
            _refuse("native-proof-delivery-binding-mismatch", "target delivery compiler or source bindings changed")
        if target_prepared:
            receipt = _require_digest(document.get("gate_receipt_sha256"), code="native-proof-delivery-invalid", label="delivery gate")
            if full_gate_packet is not None and receipt != full_gate_packet.evidence.receipt_sha256:
                _refuse("native-proof-delivery-binding-mismatch", "target delivery binds another Full Gate")
            prepared_files = tuple(methodology.PreparedTargetMethodologyFile(file.path, file.sha256, file.mode,
                _read_target_regular(root, output_relative / file.path, code="native-proof-delivery-stale", label="delivery output", expected_mode=file.mode))
                for file in actual_files)
            _, prepared_digest = methodology._target_preparation_manifest(
                package=package, target_context=context, receipt=receipt, selected=selected,
                compiler_sha256=bindings["compiler_sha256"], frontier=frontier, source_view=source_view,
                authoring=bindings["authoring_source_sha256"], sources=sources, files=prepared_files,
            )
            if document.get("target_preparation_sha256") != prepared_digest:
                _refuse("native-proof-delivery-binding-mismatch", "delivery does not bind its target preparation")
        if target_prepared:
            delivery = TargetPortableMethodologyDelivery(package.manifest_digest, package.source_catalog_sha256,
                context.sha256, receipt, frontier, source_view, output_digest, semantic_digest,
                output_root, manifest_path, actual_files)
        else:
            delivery = PortableMethodologyDelivery(package.manifest_digest, package.source_catalog_sha256, context.sha256,
                bindings["compiler_sha256"], frontier, source_view, bindings["authoring_source_sha256"], output_digest,
                semantic_digest, output_root, manifest_path, actual_files)
    methodology.reopen_admitted_package_compiler(package, compiler_binding)
    return NativeMethodologyDeliveryBinding(expected_ref, _sha256(raw), delivery, document.get("gate_receipt_sha256"))


def read_native_methodology_delivery(project_root: Path, package: VerifiedFrameworkPackage, *,
        target_context_sha256: str, manifest_ref: str, expected_manifest_sha256: str,
        full_gate_packet: RetainedNativeFullGatePacket | None = None) -> NativeMethodologyDeliveryBinding:
    """Reopen a proof-bound actual delivery; never accept a self-digest as raw SHA."""
    try:
        if not isinstance(package, VerifiedFrameworkPackage) or verify_framework_package(package.root) != package:
            _refuse("native-proof-delivery-package-invalid", "delivery package is not physically verified")
        _require_digest(expected_manifest_sha256, code="native-proof-delivery-invalid", label="raw manifest digest")
        return _read_delivery(project_root, package, target_context_sha256=target_context_sha256,
            manifest_ref=manifest_ref, expected_manifest_sha256=expected_manifest_sha256, full_gate_packet=full_gate_packet)
    except NativeInstallationProofError:
        raise
    except (RuntimeError, OSError, TypeError, ValueError, KeyError) as error:
        raise NativeInstallationProofError("native-proof-delivery-invalid", "actual Methodology delivery cannot be reopened") from error


def reopen_native_methodology_delivery(project_root: Path, package: VerifiedFrameworkPackage,
        target_context: TargetProjectContext,
        delivery: PortableMethodologyDelivery | TargetPortableMethodologyDelivery | CandidatePortableMethodologyDelivery,
        *, full_gate_packet: RetainedNativeFullGatePacket | None = None) -> NativeMethodologyDeliveryBinding:
    """Derive a schema-2 proof binding from the actual typed publisher result."""
    if not isinstance(delivery, (PortableMethodologyDelivery, TargetPortableMethodologyDelivery, CandidatePortableMethodologyDelivery)):
        _refuse("native-proof-delivery-untrusted", "proof requires the actual typed Methodology delivery")
    try:
        ref = delivery.delivery_manifest_path.relative_to(project_root).as_posix()
    except (TypeError, ValueError) as error:
        _refuse("native-proof-delivery-target-mismatch", "delivery manifest belongs to another Project")
    raw = _read_target_regular(project_root, Path(ref), code="native-proof-delivery-stale", label="Methodology delivery manifest", expected_mode=0o644)
    binding = read_native_methodology_delivery(project_root, package, target_context_sha256=target_context.sha256,
        manifest_ref=ref, expected_manifest_sha256=_sha256(raw), full_gate_packet=full_gate_packet)
    if binding.delivery != delivery:
        _refuse("native-proof-delivery-stale", "typed delivery differs from reopened physical output")
    return binding


def _refuse(code: str, message: str) -> None:
    raise NativeInstallationProofError(code, message)


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _parse_toml(payload: bytes, *, code: str, label: str) -> dict[str, object]:
    try:
        document = tomllib.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        _refuse(code, f"{label} is not valid UTF-8 TOML")
    if not isinstance(document, dict):  # pragma: no cover - tomllib returns a dict for table roots.
        _refuse(code, f"{label} is not a TOML table")
    return document


def _require_digest(value: object, *, code: str, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        _refuse(code, f"{label} is not a lowercase SHA-256")
    return value


def _target_root(lock: object) -> tuple[InstallationPublicationLock, Path]:
    if not isinstance(lock, InstallationPublicationLock):
        _refuse("native-proof-lock-required", "proof staging requires the concrete installation publication lock")
    try:
        lock.revalidate()
    except InstallationTransactionError as error:
        _refuse("native-proof-lock-invalid", "installation publication lock is not active")
    root = lock.project_root
    try:
        observed = root.lstat()
    except OSError as error:
        _refuse("native-proof-target-invalid", "locked target root is unavailable")
    if root.is_symlink() or not stat.S_ISDIR(observed.st_mode):
        _refuse("native-proof-target-invalid", "locked target root is not a real directory")
    return lock, root


def _reopen_package(root: Path, value: object):
    if not isinstance(value, VerifiedFrameworkPackage):
        _refuse("native-proof-package-invalid", "proof requires a typed verified Framework package")
    try:
        package = verify_framework_package(value.root)
    except FrameworkPackageError as error:
        _refuse("native-proof-package-invalid", "Framework package cannot be physically reopened")
    if package != value:
        _refuse("native-proof-package-stale", "typed package differs from physical package bytes")
    if package.root != root / _PACKAGE_RELEASES / package.manifest_digest:
        _refuse("native-proof-package-unselected", "package is not at the target selected-release location")
    try:
        selector = verify_current_package_selector(
            _read_target_regular(root, _PACKAGE_CURRENT, code="native-proof-selector-invalid", label="current package selector"),
            package,
        )
    except FrameworkPackageError as error:
        _refuse("native-proof-selector-invalid", "current package selector does not admit the reopened package")
    return package, selector


def _reopen_context(
    root: Path, value: object, package: VerifiedFrameworkPackage, lock: InstallationPublicationLock
) -> TargetProjectContext:
    if not isinstance(value, TargetProjectContext):
        _refuse("native-proof-context-invalid", "proof requires a typed target Project context")
    if value.sha256 != lock.target_context_sha256:
        _refuse("native-proof-context-mismatch", "installation lock names another target context")
    evidence = value.package_evidence
    if (
        evidence.package_manifest_sha256 != package.manifest_digest
        or evidence.catalog_sha256 != package.source_catalog_sha256
        or evidence.verified is not True
    ):
        _refuse("native-proof-context-mismatch", "target context does not bind the reopened package")
    try:
        persisted = _read_d600_context(root, value.sha256, verified_package=package)
    except InstalledMcpBindingError as error:
        _refuse("native-proof-context-invalid", "persisted target context is not a valid D600 carrier")
    if (
        persisted.mode != value.mode
        or persisted.target_project_identity != value.target_project_identity
        or persisted.control_child_relpath != value.control_child_relpath
        or persisted.control_child_relpath == ".caprmedio_"
    ):
        _refuse("native-proof-context-mismatch", "persisted target context differs from typed context identity")
    actual = _read_target_regular(
        root,
        _CONTEXTS / f"{value.sha256}.toml",
        code="native-proof-context-stale",
        label="target context",
    )
    if actual != value.with_digest_toml():
        _refuse("native-proof-context-stale", "persisted target context differs from typed context bytes")
    return value


def _reopen_command_stage(
    root: Path,
    value: object,
    *,
    package: VerifiedFrameworkPackage,
    context: TargetProjectContext,
    lock: InstallationPublicationLock,
) -> tuple[int, str, str]:
    if not isinstance(value, RuntimeCommandStage):
        _refuse("native-proof-command-stage-invalid", "proof requires a typed runtime command stage")
    if value.lock_generation != lock.lock_generation or value.root != root / _COMMAND_STAGING / lock.lock_generation:
        _refuse("native-proof-command-stage-mismatch", "command stage belongs to another installation lock")
    files = {
        _COMMAND_NAME: _read_target_regular(
            root,
            _COMMAND_STAGING / lock.lock_generation / _COMMAND_NAME,
            code="native-proof-command-stage-stale",
            label="staged command",
            expected_mode=0o600,
        ),
        _ENVIRONMENT_NAME: _read_target_regular(
            root,
            _COMMAND_STAGING / lock.lock_generation / _ENVIRONMENT_NAME,
            code="native-proof-command-stage-stale",
            label="staged environment",
            expected_mode=0o600,
        ),
        _WRAPPER_NAME: _read_target_regular(
            root,
            _COMMAND_STAGING / lock.lock_generation / _WRAPPER_NAME,
            code="native-proof-command-stage-stale",
            label="staged wrapper",
            expected_mode=0o700,
        ),
        _STAGE_MANIFEST_NAME: _read_target_regular(
            root,
            _COMMAND_STAGING / lock.lock_generation / _STAGE_MANIFEST_NAME,
            code="native-proof-command-stage-stale",
            label="command stage manifest",
            expected_mode=0o600,
        ),
    }
    try:
        _validate_fragment_documents(files[_COMMAND_NAME], files[_ENVIRONMENT_NAME], files[_WRAPPER_NAME],
                                     files[_STAGE_MANIFEST_NAME], code="native-proof-command-stage-invalid")
    except RuntimeError as error:
        _refuse("native-proof-command-stage-invalid", "staged command fails the shared closed D601 validator")
    command = _parse_toml(files[_COMMAND_NAME], code="native-proof-command-stage-invalid", label="staged command")
    environment = _parse_toml(files[_ENVIRONMENT_NAME], code="native-proof-command-stage-invalid", label="staged environment")
    manifest = _parse_toml(files[_STAGE_MANIFEST_NAME], code="native-proof-command-stage-invalid", label="command stage manifest")
    command_keys = {
        "schema_version", "package_manifest_sha256", "target_project_context_sha256", "state_generation",
        "entrypoint", "argv", "environment_sha256", "wrapper_sha256", "invocation_nonce", "command_sha256",
    }
    if set(command) != command_keys or type(command.get("schema_version")) is not int or command.get("schema_version") != 1:
        _refuse("native-proof-command-stage-invalid", "staged command schema is not closed")
    state_generation = command.get("state_generation")
    if isinstance(state_generation, bool) or not isinstance(state_generation, int) or state_generation < 1:
        _refuse("native-proof-command-stage-invalid", "staged command generation is not native-positive")
    if (
        command.get("package_manifest_sha256") != package.manifest_digest
        or command.get("target_project_context_sha256") != context.sha256
    ):
        _refuse("native-proof-command-stage-mismatch", "staged command binds another package or context")
    command_sha256 = _require_digest(command.get("command_sha256"), code="native-proof-command-stage-invalid", label="command digest")
    if _canonical_digest({key: item for key, item in command.items() if key != "command_sha256"}) != command_sha256:
        _refuse("native-proof-command-stage-invalid", "staged command digest differs from canonical bytes")
    environment_sha256 = _require_digest(
        command.get("environment_sha256"), code="native-proof-command-stage-invalid", label="environment digest"
    )
    wrapper_sha256 = _require_digest(
        command.get("wrapper_sha256"), code="native-proof-command-stage-invalid", label="wrapper digest"
    )
    if (
        set(environment) != {"schema_version", "variables", "environment_sha256"}
        or type(environment.get("schema_version")) is not int
        or environment.get("schema_version") != 1
    ):
        _refuse("native-proof-command-stage-invalid", "staged environment schema is not closed")
    if environment.get("environment_sha256") != environment_sha256 or _canonical_digest(
        {key: item for key, item in environment.items() if key != "environment_sha256"}
    ) != environment_sha256:
        _refuse("native-proof-command-stage-invalid", "staged environment digest differs from canonical bytes")
    if _sha256(files[_WRAPPER_NAME]) != wrapper_sha256:
        _refuse("native-proof-command-stage-invalid", "staged wrapper digest differs from command binding")
    if (
        set(manifest) != {
        "schema_version", "package_manifest_sha256", "target_project_context_sha256", "state_generation", "lock_generation", "files"
        }
        or type(manifest.get("schema_version")) is not int
        or manifest.get("schema_version") != 1
    ):
        _refuse("native-proof-command-stage-invalid", "command stage manifest schema is not closed")
    expected_files = [
        {"path": _COMMAND_NAME, "mode": 0o600, "sha256": _sha256(files[_COMMAND_NAME])},
        {"path": _ENVIRONMENT_NAME, "mode": 0o600, "sha256": _sha256(files[_ENVIRONMENT_NAME])},
        {"path": _WRAPPER_NAME, "mode": 0o700, "sha256": _sha256(files[_WRAPPER_NAME])},
    ]
    if (
        manifest.get("package_manifest_sha256") != package.manifest_digest
        or manifest.get("target_project_context_sha256") != context.sha256
        or manifest.get("state_generation") != state_generation
        or manifest.get("lock_generation") != lock.lock_generation
        or manifest.get("files") != expected_files
    ):
        _refuse("native-proof-command-stage-mismatch", "command stage manifest differs from reopened command carriers")
    if (
        value.package_manifest_sha256 != package.manifest_digest
        or value.target_project_context_sha256 != context.sha256
        or value.state_generation != state_generation
        or value.command_sha256 != command_sha256
        or value.environment_sha256 != environment_sha256
        or value.wrapper_sha256 != wrapper_sha256
    ):
        _refuse("native-proof-command-stage-mismatch", "typed command stage differs from physical staged bytes")
    return state_generation, command_sha256, _sha256(files[_STAGE_MANIFEST_NAME])


def _reopen_selector(
    value: object,
    *,
    package: VerifiedFrameworkPackage,
    context: TargetProjectContext,
    state_generation: int,
    lock: InstallationPublicationLock,
    image_digest: str,
) -> tuple[bytes, str]:
    if not isinstance(value, bytes):
        _refuse("native-proof-prospective-selector-invalid", "prospective selector must be exact TOML bytes")
    selector = _parse_toml(value, code="native-proof-prospective-selector-invalid", label="prospective selector")
    if (
        set(selector) != _SELECTOR_KEYS
        or type(selector.get("schema_version")) is not int
        or selector.get("schema_version") != 1
        or type(selector.get("state_generation")) is not int
        or selector.get("state_generation") < 1
    ):
        _refuse("native-proof-prospective-selector-invalid", "prospective selector schema is not closed")
    if (
        selector.get("package_manifest_sha256") != package.manifest_digest
        or selector.get("target_project_context_sha256") != context.sha256
        or selector.get("state_generation") != state_generation
        or selector.get("installation_lock_generation") != lock.lock_generation
        or selector.get("image_digest") != image_digest
    ):
        _refuse("native-proof-prospective-selector-mismatch", "prospective selector differs from reopened installation inputs")
    return value, _sha256(value)


def _open_proof_parent(root: Path) -> int:
    flags = os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW | os.O_DIRECTORY
    try:
        descriptor = os.open(root, flags)
    except OSError as error:
        _refuse("native-proof-path-unsafe", "target root cannot anchor proof staging")
    try:
        for component in _PROOF_STAGING.parts:
            try:
                os.mkdir(component, mode=0o700, dir_fd=descriptor)
            except FileExistsError:
                pass
            except OSError as error:
                _refuse("native-proof-write-failed", "proof staging ancestor cannot be created")
            try:
                next_descriptor = os.open(component, flags, dir_fd=descriptor)
            except OSError as error:
                _refuse("native-proof-path-unsafe", "proof staging ancestor cannot be safely opened")
            os.close(descriptor)
            descriptor = next_descriptor
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _open_new_proof_stage(parent_fd: int, lock_generation: str) -> int:
    flags = os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW | os.O_DIRECTORY
    try:
        os.mkdir(lock_generation, mode=0o700, dir_fd=parent_fd)
    except FileExistsError:
        _refuse("native-proof-conflict", "proof stage already exists for this installation lock generation")
    except OSError as error:
        _refuse("native-proof-write-failed", "proof stage cannot be created")
    try:
        return os.open(lock_generation, flags, dir_fd=parent_fd)
    except OSError as error:
        _refuse("native-proof-path-unsafe", "proof stage cannot be safely opened")


def _proof_bytes(fields: dict[str, object]) -> bytes:
    lines: list[str] = []
    for key in _PROOF_KEYS:
        value = fields[key]
        if isinstance(value, int):
            lines.append(f"{key} = {value}")
        else:
            lines.append(f"{key} = {_quoted(str(value))}")
    return ("\n".join(lines) + "\n").encode("utf-8")


def _proof_fields(
    package: VerifiedFrameworkPackage,
    selected: object,
    context: TargetProjectContext,
    generation: int,
    command_sha256: str,
    stage_manifest_sha256: str,
    selector_sha256: str,
    lock: InstallationPublicationLock,
    delivery: NativeMethodologyDeliveryBinding,
) -> dict[str, object]:
    full_gate_receipt_sha256 = getattr(selected, "full_gate_receipt_sha256", None)
    image_digest = getattr(selected, "image_digest", None)
    if not isinstance(full_gate_receipt_sha256, str) or not isinstance(image_digest, str):
        _refuse("native-proof-package-invalid", "reopened package selector is invalid")
    return {
        "schema_version": 2,
        "package_manifest_sha256": package.manifest_digest,
        "framework_version": package.framework_version,
        "version_toml_sha256": package.version_toml_sha256,
        "source_catalog_sha256": package.source_catalog_sha256,
        "full_gate_receipt_sha256": full_gate_receipt_sha256,
        "image_digest": image_digest,
        "target_project_context_sha256": context.sha256,
        "state_generation": generation,
        "installation_lock_generation": lock.lock_generation,
        "installation_command_sha256": lock.command_sha256,
        "command_sha256": command_sha256,
        "command_stage_manifest_sha256": stage_manifest_sha256,
        "methodology_delivery_manifest_ref": delivery.manifest_ref,
        "methodology_delivery_manifest_sha256": delivery.manifest_sha256,
        "selector_sha256": selector_sha256,
    }


def _selected_fields(request: NativeInstallationProofRequest, lock: InstallationPublicationLock) -> tuple[dict[str, object], bytes]:
    root = lock.project_root
    package, selected = _reopen_package(root, request.package)
    context = _reopen_context(root, request.target_context, package, lock)
    if not isinstance(request.methodology_delivery, (PortableMethodologyDelivery, TargetPortableMethodologyDelivery)):
        _refuse("native-proof-delivery-untrusted", "installed proof requires a typed target delivery")
    delivery = reopen_native_methodology_delivery(root, package, context, request.methodology_delivery)
    if delivery.gate_receipt_sha256 is not None and delivery.gate_receipt_sha256 != selected.full_gate_receipt_sha256:
        _refuse("native-proof-delivery-binding-mismatch", "installed delivery binds another Full Gate")
    generation, command_sha256, stage_manifest_sha256 = _reopen_command_stage(
        root, request.command_stage, package=package, context=context, lock=lock
    )
    selector, selector_sha256 = _reopen_selector(
        request.prospective_selector,
        package=package,
        context=context,
        state_generation=generation,
        lock=lock,
        image_digest=selected.image_digest,
    )
    return _proof_fields(
        package,
        selected,
        context,
        generation,
        command_sha256,
        stage_manifest_sha256,
        selector_sha256,
        lock,
        delivery,
    ), selector


def _candidate_fields(
    request: CandidateNativeInstallationProofRequest, lock: InstallationPublicationLock
) -> tuple[dict[str, object], bytes]:
    root = lock.project_root
    package = _reopen_candidate_package(
        root,
        request.package,
        request.prospective_package_selector,
        request.full_gate_packet,
    )
    try:
        selected = verify_current_package_selector(request.prospective_package_selector, package)
    except FrameworkPackageError:
        _refuse("native-proof-package-selector-invalid", "prospective package selector does not admit the candidate package")
    context = _reopen_context(root, request.target_context, package, lock)
    delivery = reopen_native_methodology_delivery(root, package, context, request.methodology_delivery,
                                                full_gate_packet=request.full_gate_packet)
    if delivery.gate_receipt_sha256 != selected.full_gate_receipt_sha256:
        _refuse("native-proof-delivery-binding-mismatch", "candidate delivery does not bind the original Full Gate")
    generation, command_sha256, stage_manifest_sha256 = _reopen_command_stage(
        root, request.command_stage, package=package, context=context, lock=lock
    )
    selector, selector_sha256 = _reopen_selector(
        request.prospective_selector,
        package=package,
        context=context,
        state_generation=generation,
        lock=lock,
        image_digest=selected.image_digest,
    )
    return _proof_fields(
        package,
        selected,
        context,
        generation,
        command_sha256,
        stage_manifest_sha256,
        selector_sha256,
        lock,
        delivery,
    ), selector


def _fields(
    request: NativeInstallationProofRequest | CandidateNativeInstallationProofRequest,
    lock: InstallationPublicationLock,
) -> tuple[dict[str, object], bytes]:
    if isinstance(request, NativeInstallationProofRequest):
        return _selected_fields(request, lock)
    if isinstance(request, CandidateNativeInstallationProofRequest):
        return _candidate_fields(request, lock)
    _refuse("native-proof-request-invalid", "proof requires one typed installed or candidate request")
    raise AssertionError("unreachable")


def _proof_from_bytes(payload: bytes, expected: dict[str, object]) -> dict[str, object]:
    proof = _parse_toml(payload, code="native-proof-invalid", label="release proof")
    if (
        set(proof) != set(_PROOF_KEYS)
        or type(proof.get("schema_version")) is not int
        or type(proof.get("state_generation")) is not int
        or proof != expected
    ):
        _refuse("native-proof-mismatch", "release proof differs from reopened installation inputs")
    return proof


def _reopen_proof(
    request: NativeInstallationProofRequest | CandidateNativeInstallationProofRequest,
    lock: InstallationPublicationLock,
) -> NativeInstallationProof:
    fields, selector = _fields(request, lock)
    root = lock.project_root
    relative = _PROOF_STAGING / lock.lock_generation
    selector_path = root / relative / _SELECTOR_NAME
    proof_path = root / relative / _PROOF_NAME
    actual_selector = _read_target_regular(
        root, relative / _SELECTOR_NAME, code="native-proof-reopen-failed", label="staged prospective selector", expected_mode=0o600
    )
    if actual_selector != selector:
        _refuse("native-proof-mismatch", "staged prospective selector differs from reopened selector bytes")
    proof = _proof_from_bytes(
        _read_target_regular(
            root, relative / _PROOF_NAME, code="native-proof-reopen-failed", label="staged release proof", expected_mode=0o600
        ),
        fields,
    )
    return NativeInstallationProof(
        root=root / relative,
        proof_path=proof_path,
        selector_path=selector_path,
        package_manifest_sha256=str(proof["package_manifest_sha256"]),
        framework_version=str(proof["framework_version"]),
        version_toml_sha256=str(proof["version_toml_sha256"]),
        source_catalog_sha256=str(proof["source_catalog_sha256"]),
        full_gate_receipt_sha256=str(proof["full_gate_receipt_sha256"]),
        image_digest=str(proof["image_digest"]),
        target_project_context_sha256=str(proof["target_project_context_sha256"]),
        state_generation=int(proof["state_generation"]),
        installation_lock_generation=str(proof["installation_lock_generation"]),
        installation_command_sha256=str(proof["installation_command_sha256"]),
        command_sha256=str(proof["command_sha256"]),
        command_stage_manifest_sha256=str(proof["command_stage_manifest_sha256"]),
        methodology_delivery_manifest_ref=str(proof["methodology_delivery_manifest_ref"]),
        methodology_delivery_manifest_sha256=str(proof["methodology_delivery_manifest_sha256"]),
        selector_sha256=str(proof["selector_sha256"]),
    )


def _stage_native_installation_proof(
    request: NativeInstallationProofRequest | CandidateNativeInstallationProofRequest,
    *,
    lock: InstallationPublicationLock,
) -> NativeInstallationProof:
    """Write and reopen inert D604 proof bytes; never publish or execute them."""

    concrete_lock, root = _target_root(lock)
    fields, selector = _fields(request, concrete_lock)
    proof_payload = _proof_bytes(fields)
    concrete_lock.revalidate()
    parent_fd = _open_proof_parent(root)
    try:
        stage_fd = _open_new_proof_stage(parent_fd, concrete_lock.lock_generation)
        try:
            _write_new(stage_fd, _SELECTOR_NAME, selector, mode=0o600)
            _write_new(stage_fd, _PROOF_NAME, proof_payload, mode=0o600)
            os.fsync(stage_fd)
            concrete_lock.revalidate()
            if _read_stage_regular(stage_fd, _SELECTOR_NAME, expected_mode=0o600) != selector:
                _refuse("native-proof-reopen-failed", "staged prospective selector bytes differ")
            if _read_stage_regular(stage_fd, _PROOF_NAME, expected_mode=0o600) != proof_payload:
                _refuse("native-proof-reopen-failed", "staged release proof bytes differ")
        finally:
            os.close(stage_fd)
    finally:
        os.close(parent_fd)
    concrete_lock.revalidate()
    return _reopen_proof(request, concrete_lock)


def _read_native_installation_proof(
    request: NativeInstallationProofRequest | CandidateNativeInstallationProofRequest,
    *,
    lock: InstallationPublicationLock,
) -> NativeInstallationProof:
    """Reopen a staged proof against all live typed inputs without effects."""

    concrete_lock, _ = _target_root(lock)
    result = _reopen_proof(request, concrete_lock)
    concrete_lock.revalidate()
    return result


def stage_native_installation_proof(
    request: NativeInstallationProofRequest, *, lock: InstallationPublicationLock
) -> NativeInstallationProof:
    """Write/reopen an installed-package D604 proof with no effects."""

    if not isinstance(request, NativeInstallationProofRequest):
        _refuse("native-proof-request-invalid", "installed proof staging requires a typed request")
    return _stage_native_installation_proof(request, lock=lock)


def read_native_installation_proof(
    request: NativeInstallationProofRequest, *, lock: InstallationPublicationLock
) -> NativeInstallationProof:
    """Reopen an installed-package proof against current selected carriers."""

    if not isinstance(request, NativeInstallationProofRequest):
        _refuse("native-proof-request-invalid", "installed proof reading requires a typed request")
    return _read_native_installation_proof(request, lock=lock)


def stage_candidate_native_installation_proof(
    request: CandidateNativeInstallationProofRequest, *, lock: InstallationPublicationLock
) -> NativeInstallationProof:
    """Write/reopen one candidate D604 proof before selector publication."""

    if not isinstance(request, CandidateNativeInstallationProofRequest):
        _refuse("candidate-proof-request-invalid", "candidate proof staging requires a typed request")
    return _stage_native_installation_proof(request, lock=lock)


def read_candidate_native_installation_proof(
    request: CandidateNativeInstallationProofRequest, *, lock: InstallationPublicationLock
) -> NativeInstallationProof:
    """Reopen one candidate proof using exact prospective D598/D599 bytes."""

    if not isinstance(request, CandidateNativeInstallationProofRequest):
        _refuse("candidate-proof-request-invalid", "candidate proof reading requires a typed request")
    return _read_native_installation_proof(request, lock=lock)


__all__ = [
    "CandidateNativeInstallationProofRequest",
    "NativeInstallationProof",
    "NativeInstallationProofError",
    "NativeInstallationProofRequest",
    "NativeMethodologyDeliveryBinding",
    "read_native_methodology_delivery",
    "reopen_native_methodology_delivery",
    "read_candidate_native_installation_proof",
    "read_native_installation_proof",
    "stage_candidate_native_installation_proof",
    "stage_native_installation_proof",
]
