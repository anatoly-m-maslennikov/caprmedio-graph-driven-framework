"""Locally observed, effect-free D567 candidate handoffs.

The functions here only read bytes, TOML, and modes. They never copy, compile,
stage, select a runtime, install a Skill, invoke Docker, or record a Journal
event.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import tomllib
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal, Mapping

if TYPE_CHECKING:
    from framework_package import VerifiedFrameworkPackage
    from native_selected_installation import NativeSelectedInstallation
    from retained_full_gate_packet import RetainedNativeFullGatePacket

from pydantic import Field, field_validator, model_validator

from release_contract import (
    IMAGE_DOCKERFILE,
    PROJECT_SKILL_TARGET,
    RELEASE,
    VERSION_TOML_RELATIVE,
    CandidateBuildRequest,
    CandidateImageReference,
    CandidateSnapshotManifest,
    ReleaseContractError,
    SealedAuthority,
    SourceInventoryRow,
    StrictModel,
    ValidatedCandidate,
    _safe_relative,
    candidate_snapshot_manifest_sha256,
    canonical_json,
    encode_candidate_manifest,
)
from release_inventory import ReleaseInventoryError, persistent_regular_files, refuse_secret_path


CANONICAL_SOURCE_RELATIVE = (
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources"
)
PROJECT_STRUCTURE_RELATIVE = ".caprmedio_caprmedio/project_structure.toml"
FRAMEWORK_SETTINGS_RELATIVE = ".caprmedio_caprmedio/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"
CURRENT_SELECTOR_RELATIVE = ".caprmedio_runtime/framework/current.toml"
NATIVE_CURRENT_SELECTOR_RELATIVE = ".caprmedio_runtime/installation/current.toml"
DERIVED_SOURCE_COPY_RELATIVE = "101_LAYER_1_FRAMEWORK_METHODOLOGY/sources"
MATERIALIZED_RELATIVE = ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/_release_materialized"
ENGINE_ROOT_RELATIVE = "102_FRAMEWORK_ENGINE"
SKILL_ROOT_RELATIVE = "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca"
COMPILER_ENTRYPOINT_RELATIVE = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py"
_PINNED_IMAGE_DEPENDENCY_COPY = b"COPY pyproject.toml uv.lock ./"
_PINNED_IMAGE_DEPENDENCY_INPUTS = ("pyproject.toml", "uv.lock")
_HOOK_CONFIGURATION_FILE_NAMES = frozenset(
    {
        ".huskyrc",
        ".pre-commit-config.yaml",
        ".pre-commit-config.yml",
        "husky.config.cjs",
        "husky.config.js",
        "husky.config.mjs",
        "lefthook.yaml",
        "lefthook.yml",
    }
)
_METHODOLOGY_EXPORT_PATH = Path(__file__).resolve().parents[1] / "COMPILE_APPLICABLE_METHODOLOGY" / "methodology_export.py"


@dataclass(frozen=True)
class NativeInstalledNBinding:
    """Actual native N proof inputs and one frozen, physically admitted fact."""

    verified_package: VerifiedFrameworkPackage
    full_gate_packet: RetainedNativeFullGatePacket
    selected: NativeSelectedInstallation


def bind_native_installed_n(project_root: Path | str, verified_package: Any,
                            full_gate_packet: Any, *, target_context_sha256: str) -> NativeInstalledNBinding:
    tools_root = str(Path(__file__).resolve().parents[1])
    if tools_root not in sys.path:
        sys.path.insert(0, tools_root)
    from native_selected_installation import reopen_current_native_installation

    selected = reopen_current_native_installation(
        project_root, verified_package, full_gate_packet, target_context_sha256=target_context_sha256,
    )
    if selected.image_digest.removeprefix("sha256:") != full_gate_packet.evidence.candidate_image_digest.removeprefix("sha256:"):
        raise _error("release-native-n-image-mismatch", "selected native image differs from the actual retained Full Gate image")
    return NativeInstalledNBinding(verified_package, full_gate_packet, selected)


def reopen_native_installed_n(root: Path | str, binding: object) -> NativeInstalledNBinding:
    if not isinstance(binding, NativeInstalledNBinding):
        raise _error("release-native-n-untrusted", "native N requires the concrete admitted package and retained Full Gate packet")
    try:
        observed = bind_native_installed_n(
            root, binding.verified_package, binding.full_gate_packet,
            target_context_sha256=binding.selected.target_project_context_sha256,
        )
    except (RuntimeError, AttributeError, TypeError, ValueError) as error:
        raise _error("release-native-n-stale", "selected native N cannot be physically reopened") from error
    if observed != binding:
        raise _error("release-native-n-stale", "selected native N changed after freezing")
    return observed


def selected_n_selector_relative(candidate: Any) -> str:
    return NATIVE_CURRENT_SELECTOR_RELATIVE if getattr(candidate, "native_installed_n", None) is not None else CURRENT_SELECTOR_RELATIVE


def selected_n_identity(candidate: Any) -> str:
    binding = getattr(candidate, "native_installed_n", None)
    if binding is not None:
        if not isinstance(binding, NativeInstalledNBinding):
            raise _error("release-native-n-untrusted", "native N binding is not typed")
        return binding.full_gate_packet.retained_candidate.candidate_snapshot_manifest_sha256
    return candidate.authority.executing_release


def _error(code: str, message: str) -> ReleaseContractError:
    return ReleaseContractError(code, message)


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _root(value: Path | str) -> Path:
    root = Path(value).resolve()
    if not root.is_dir():
        raise _error("release-project-missing", f"project root is not a directory: {root}")
    return root


def _relative(root: Path, path: Path, *, label: str) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError as error:
        raise _error("release-path-unsafe", f"{label} escapes project root") from error


def _file(root: Path, relative: str, *, code: str = "release-input-missing") -> Path:
    safe = _safe_relative(relative, "relative")
    try:
        refuse_secret_path(safe)
    except ReleaseInventoryError as error:
        raise _error(error.code, str(error)) from error
    path = root / safe
    if path.is_symlink() or not path.is_file():
        raise _error(code, f"required regular file is absent: {safe}")
    try:
        path.resolve(strict=True).relative_to(root)
    except ValueError as error:
        raise _error("release-path-unsafe", f"required file escapes project: {safe}") from error
    return path


def _directory(root: Path, relative: str, *, code: str = "release-input-missing") -> Path:
    safe = _safe_relative(relative, "relative")
    try:
        refuse_secret_path(safe)
    except ReleaseInventoryError as error:
        raise _error(error.code, str(error)) from error
    path = root / safe
    if path.is_symlink() or not path.is_dir():
        raise _error(code, f"required directory is absent: {safe}")
    try:
        path.resolve(strict=True).relative_to(root)
    except ValueError as error:
        raise _error("release-path-unsafe", f"required directory escapes project: {safe}") from error
    return path


def _regular_files(root: Path, directory: Path, *, code: str = "release-input-invalid") -> list[Path]:
    try:
        files = persistent_regular_files(root, directory)
    except ReleaseInventoryError as error:
        raise _error(error.code, str(error)) from error
    if not files:
        raise _error(code, f"required inventory is empty: {_relative(root, directory, label='directory')}")
    return files


def tree_sha256(root: Path | str, directory: Path | str) -> str:
    """Digest the ordered relative-path and byte sequence below one directory."""

    project = _root(root)
    folder = Path(directory)
    if not folder.is_absolute():
        folder = project / folder
    folder = _directory(project, _relative(project, folder, label="tree root"))
    digest = hashlib.sha256()
    for path in _regular_files(project, folder):
        relative = path.relative_to(folder).as_posix().encode("utf-8")
        digest.update(len(relative).to_bytes(8, "big"))
        digest.update(relative)
        contents = path.read_bytes()
        digest.update(len(contents).to_bytes(8, "big"))
        digest.update(contents)
    return digest.hexdigest()


def _selector_release(root: Path) -> str:
    selector = _file(root, CURRENT_SELECTOR_RELATIVE, code="release-selection-missing")
    try:
        payload = tomllib.loads(selector.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise _error("release-selection-invalid", "current framework selector is not valid TOML") from error
    values: list[str] = []
    for mapping in (payload, payload.get("selection") if isinstance(payload.get("selection"), dict) else {}):
        for key in ("executing_release", "selected_release", "release"):
            value = mapping.get(key)
            if isinstance(value, str) and value:
                values.append(value)
        for key in ("selected_release_root", "release_root"):
            value = mapping.get(key)
            if isinstance(value, str) and value:
                values.append(Path(value).name)
    unique = set(values)
    if len(unique) != 1:
        raise _error("release-selection-ambiguous", "current framework selector must name exactly one executing release")
    return unique.pop()


def _inventory_row(root: Path, path: Path, resource: str, destination: str) -> SourceInventoryRow:
    relative = _relative(root, path, label="inventory source")
    return SourceInventoryRow(
        resource=resource,
        source_path=relative,
        source_sha256=_sha256_bytes(path.read_bytes()),
        source_mode=path.stat().st_mode & 0o777,
        destination_path=destination,
    )


def read_framework_version_toml(root: Path | str) -> tuple[str, str]:
    """Read the one sealed root version carrier and its exact byte digest."""

    project = _root(root)
    version_toml = _file(project, VERSION_TOML_RELATIVE, code="release-version-missing")
    payload = version_toml.read_bytes()
    try:
        document = tomllib.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise _error("release-version-invalid", "root version.toml is not valid UTF-8 TOML") from error
    framework = document.get("framework")
    version = framework.get("version") if isinstance(framework, dict) else None
    if not isinstance(version, str) or not RELEASE.fullmatch(version):
        raise _error("release-version-invalid", "root version.toml must declare [framework].version as a stable release identifier")
    return version, _sha256_bytes(payload)


def _image_input_paths(root: Path, dockerfile: Path) -> list[Path]:
    """Observe the fixed dependency inputs declared by the pinned Dockerfile.

    This is intentionally not a general Dockerfile parser.  The known
    repository build instruction has exactly two root dependency inputs; when
    that instruction is present, both are required before the candidate can be
    sealed.
    """

    paths = [dockerfile]
    if _PINNED_IMAGE_DEPENDENCY_COPY in dockerfile.read_bytes():
        paths.extend(
            _file(root, relative, code="release-image-input-missing")
            for relative in _PINNED_IMAGE_DEPENDENCY_INPUTS
        )
    return paths


def _assert_hook_free_skill_payload(root: Path, skill_root: Path) -> list[Path]:
    """Return the retained Skill files only when they contain no hook carrier.

    D563 permits ordinary prose about hooks in the Skill, but the release must
    not deliver executable hook carriers or hook configuration as part of the
    project-local ``ca`` Skill.  Inspect only names and locations; the
    content of Markdown and other ordinary resources is deliberately opaque.
    """

    files = _regular_files(root, skill_root)
    for path in files:
        relative = path.relative_to(skill_root)
        parts = relative.parts
        if len(parts) >= 2 and parts[0] == ".git" and parts[1] == "hooks":
            raise _error("release-skill-hook-forbidden", "Skill payload contains a Git hook carrier")
        if "hooks" in parts:
            raise _error("release-skill-hook-forbidden", "Skill payload contains a hook carrier")
        if len(parts) == 1 and relative.name in _HOOK_CONFIGURATION_FILE_NAMES:
            raise _error("release-skill-hook-forbidden", "Skill payload contains hook configuration")
    return files


def _observed_inventory(root: Path) -> tuple[list[SourceInventoryRow], CandidateImageReference]:
    source_root = _directory(root, CANONICAL_SOURCE_RELATIVE)
    engine_root = _directory(root, ENGINE_ROOT_RELATIVE)
    skill_root = _directory(root, SKILL_ROOT_RELATIVE)
    dockerfile = _file(root, IMAGE_DOCKERFILE)
    version_toml = _file(root, VERSION_TOML_RELATIVE, code="release-version-missing")
    rows: list[SourceInventoryRow] = []
    for path in _regular_files(root, source_root):
        rows.append(_inventory_row(root, path, "METHODOLOGY", f"METHODOLOGY/sources/{path.relative_to(source_root).as_posix()}"))
    for path in _regular_files(root, engine_root):
        if path == dockerfile or path.is_relative_to(skill_root):
            continue
        rows.append(_inventory_row(root, path, "FRAMEWORK_ENGINE", f"FRAMEWORK_ENGINE/{path.relative_to(engine_root).as_posix()}"))
    for path in _assert_hook_free_skill_payload(root, skill_root):
        rows.append(_inventory_row(root, path, "SKILL", f"SKILLS/ca/{path.relative_to(skill_root).as_posix()}"))
    for image_input in _image_input_paths(root, dockerfile):
        if image_input == dockerfile:
            destination = f"IMAGE_INPUT/{dockerfile.relative_to(engine_root).as_posix()}"
        else:
            destination = f"IMAGE_INPUT/{image_input.relative_to(root).as_posix()}"
        rows.append(_inventory_row(root, image_input, "IMAGE_INPUT", destination))
    rows.append(_inventory_row(root, version_toml, "PACKAGE_CONTROL", VERSION_TOML_RELATIVE))
    if not any(row.resource == "FRAMEWORK_ENGINE" for row in rows):
        raise _error("release-inventory-incomplete", "Framework Engine inventory is empty")
    image = CandidateImageReference(
        dockerfile_path=IMAGE_DOCKERFILE,
        dockerfile_sha256=_sha256_bytes(dockerfile.read_bytes()),
        candidate_image_reference="pending-local-observation",
    )
    return rows, image


def build_validated_candidate(
    project_root: Path | str,
    request: CandidateBuildRequest | Mapping[str, Any],
    *,
    observed_source_frontier_digest: str | None = None,
    native_installed_n: NativeInstalledNBinding | None = None,
) -> ValidatedCandidate:
    """Observe local N/currentness and construct one pre-compiler candidate.v2."""

    root = _root(project_root)
    intent = request if isinstance(request, CandidateBuildRequest) else CandidateBuildRequest.model_validate(request)
    source_root = _directory(root, CANONICAL_SOURCE_RELATIVE)
    structure = _file(root, PROJECT_STRUCTURE_RELATIVE)
    settings = _file(root, FRAMEWORK_SETTINGS_RELATIVE)
    if native_installed_n is not None:
        native_installed_n = reopen_native_installed_n(root, native_installed_n)
        executing_release = native_installed_n.selected.framework_version
    else:
        if (root / NATIVE_CURRENT_SELECTOR_RELATIVE).exists() or (root / NATIVE_CURRENT_SELECTOR_RELATIVE).is_symlink():
            raise _error("release-native-n-proof-required", "native runtime requires its physically admitted package and retained Full Gate packet")
        executing_release = _selector_release(root)
    if executing_release == intent.candidate_release:
        raise _error("release-currentness-invalid", "candidate release is already the locally selected release")
    framework_version, version_toml_sha256 = read_framework_version_toml(root)
    if framework_version != intent.candidate_release:
        raise _error("release-version-mismatch", "root version.toml [framework].version must equal the candidate release")
    rows, image = _observed_inventory(root)
    image = image.model_copy(update={"candidate_image_reference": intent.candidate_image_reference})
    snapshot_digest = tree_sha256(root, source_root)
    frontier_digest = observed_source_frontier_digest or snapshot_digest
    manifest = encode_candidate_manifest(
        {
            "executing_release": executing_release,
            "candidate_release": intent.candidate_release,
            "framework_version": framework_version,
            "version_toml_sha256": version_toml_sha256,
            "canonical_source_snapshot_ref": CANONICAL_SOURCE_RELATIVE,
            "canonical_source_snapshot_digest": snapshot_digest,
            "project_structure_digest": _sha256_bytes(structure.read_bytes()),
            "framework_settings_digest": _sha256_bytes(settings.read_bytes()),
            "source_frontier_digest": frontier_digest,
            "nested_source_recursive_sha256_before": snapshot_digest,
            "expected_derived_source_copy_sha256": intent.expected_derived_source_copy_sha256,
            "expected_compiled_output_sha256": intent.expected_compiled_output_sha256,
            "full_suite_environment": intent.full_suite_environment.model_dump(mode="json"),
            "skill_target": PROJECT_SKILL_TARGET,
            "candidate_image": image.model_dump(mode="json"),
            "source_inventory_rows": [row.model_dump(mode="json") for row in rows],
        }
    )
    authority = SealedAuthority(
        executing_release=executing_release,
        candidate_release=intent.candidate_release,
        framework_version=framework_version,
        version_toml_sha256=version_toml_sha256,
        canonical_source_snapshot_digest=snapshot_digest,
        project_structure_digest=_sha256_bytes(structure.read_bytes()),
        framework_settings_digest=_sha256_bytes(settings.read_bytes()),
        source_frontier_digest=frontier_digest,
        nested_source_recursive_sha256_before=snapshot_digest,
        expected_candidate_snapshot_manifest_sha256=manifest.sha256,
    )
    return ValidatedCandidate(str(root), manifest, authority, intent, native_installed_n)


def _revalidate(candidate: ValidatedCandidate) -> ValidatedCandidate:
    if not isinstance(candidate, ValidatedCandidate):
        raise _error("release-candidate-untrusted", "pre-compiler handoff must be a locally validated candidate")
    observed = build_validated_candidate(
        candidate.project_root,
        candidate.intent,
        observed_source_frontier_digest=candidate.authority.source_frontier_digest,
        native_installed_n=candidate.native_installed_n,
    )
    if observed.authority != candidate.authority or observed.manifest != candidate.manifest:
        raise _error("release-currentness-stale", "locally observed selection or sealed candidate inputs changed")
    if candidate.manifest.sha256 != candidate_snapshot_manifest_sha256(candidate.manifest):
        raise _error("candidate-manifest-unsealed", "candidate manifest checksum no longer validates")
    return observed


@dataclass(frozen=True)
class SealedSourceCopy:
    candidate: ValidatedCandidate
    source_copy_root: str
    actual_derived_source_copy_sha256: str


@dataclass(frozen=True)
class SealedMethodologyExport:
    """A private candidate export re-opened through the exporter seal reader.

    This is deliberately a wrapper around the existing strict candidate.v2
    boundary rather than an unsealed caller mapping or an implicit v3 schema.
    The private export is therefore bound both to the locally observed
    candidate snapshot and to the frozen/export-seal checksums it actually
    delivered.
    """

    candidate: ValidatedCandidate
    release_candidate_root: str
    source_export_root: str
    frozen_manifest_sha256: str
    export_inventory_sha256: str
    export_seal_sha256: str


def _exporter_module() -> Any:
    """Load the bounded exporter without treating its payload as authority."""

    spec = importlib.util.spec_from_file_location("_release_handoff_methodology_export", _METHODOLOGY_EXPORT_PATH)
    if spec is None or spec.loader is None:  # pragma: no cover - installation failure
        raise _error("release-methodology-export-unavailable", "sealed Methodology exporter is unavailable")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _private_candidate_root(root: Path, value: Path | str) -> Path:
    supplied = Path(value)
    if not supplied.is_absolute():
        supplied = root / supplied
    candidate = supplied.resolve(strict=False)
    base = (root / ".caprmedio_tmp" / "release_candidates").resolve(strict=False)
    try:
        relative = candidate.relative_to(base)
    except ValueError as error:
        raise _error("release-private-candidate-root-invalid", "Methodology export is outside the private release-candidate root") from error
    if len(relative.parts) != 1 or relative.name in {"", ".", ".."}:
        raise _error("release-private-candidate-root-invalid", "Methodology export must name one private candidate run")
    return candidate


def _export_seal_sha256(candidate_root: Path, exporter: Any) -> str:
    """Read the checksum only after ``read_sealed_export`` has validated it."""

    path = candidate_root / exporter.SEAL_NAME
    if path.is_symlink() or not path.is_file():
        raise _error("release-methodology-export-invalid", "sealed Methodology export has no regular seal")
    try:
        seal = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise _error("release-methodology-export-invalid", "sealed Methodology export seal is unreadable") from error
    value = seal.get("sha256") if isinstance(seal, dict) else None
    if not isinstance(value, str) or len(value) != 64 or any(character not in "0123456789abcdef" for character in value):
        raise _error("release-methodology-export-invalid", "sealed Methodology export checksum is invalid")
    return value


def _assert_export_inventory_bound(candidate: ValidatedCandidate, export: Any, exporter: Any) -> None:
    """Require every frozen/export pin to be one of the candidate source rows."""

    source_rows = {
        row.source_path: row.source_sha256
        for row in candidate.manifest.source_inventory_rows
        if row.resource == "METHODOLOGY"
    }
    inventory = export.inventory
    frozen = inventory.get("frozen_manifest")
    if not isinstance(frozen, Mapping) or frozen.get("source_root") != str(
        _root(candidate.project_root) / CANONICAL_SOURCE_RELATIVE
    ):
        raise _error("release-methodology-export-source-mismatch", "sealed export was not frozen from the candidate canonical source root")
    root = _root(candidate.project_root)
    if frozen.get("schema") != exporter.FROZEN_SCHEMA:
        raise _error("release-methodology-export-project-binding-required", "new Project handoff requires the Project-bound frozen export schema")
    try:
        expected_binding = exporter.reopen_project_export_binding(root, root / CANONICAL_SOURCE_RELATIVE)
    except Exception as error:
        raise _error("release-methodology-export-project-binding-invalid", "Project export controls cannot be physically reopened") from error
    binding = frozen.get("project_binding")
    if not isinstance(binding, Mapping) or binding != expected_binding:
        raise _error("release-methodology-export-project-binding-stale", "frozen export controls differ from the actual Project")
    if (binding.get("project_structure_sha256") != candidate.authority.project_structure_digest
            or binding.get("instance_settings_sha256") != candidate.authority.framework_settings_digest):
        raise _error("release-methodology-export-project-binding-mismatch", "frozen export controls differ from the sealed candidate authority")
    pins: list[Mapping[str, Any]] = []
    for key in ("atoms", "support", "catalog_pins"):
        rows = inventory.get(key)
        if not isinstance(rows, list):
            raise _error("release-methodology-export-invalid", f"sealed export {key} inventory is invalid")
        pins.extend(row for row in rows if isinstance(row, Mapping))
    for pin in pins:
        path = pin.get("source_path", pin.get("path"))
        digest = pin.get("sha256")
        candidate_path = f"{CANONICAL_SOURCE_RELATIVE}/{path}" if isinstance(path, str) else None
        if not isinstance(path, str) or not isinstance(digest, str) or source_rows.get(candidate_path) != digest:
            raise _error("release-methodology-export-source-mismatch", "sealed export pin differs from the candidate source inventory")


def bind_sealed_methodology_export(
    candidate: ValidatedCandidate, release_candidate_root: Path | str,
) -> SealedMethodologyExport:
    """Bind one exporter-sealed private delivery to an unchanged candidate.v2.

    The exporter is the only authority that opens its private delivery.  This
    adapter never accepts an inventory mapping, a caller-supplied checksum, or
    an unsealed source directory.
    """

    current = _revalidate(candidate)
    root = _root(current.project_root)
    candidate_root = _private_candidate_root(root, release_candidate_root)
    exporter = _exporter_module()
    try:
        export = exporter.read_sealed_export(release_candidate_root=candidate_root)
    except Exception as error:
        code = getattr(error, "code", "release-methodology-export-invalid")
        raise _error(str(code), "private Methodology export is not sealed and valid") from error
    _assert_export_inventory_bound(current, export, exporter)
    return SealedMethodologyExport(
        candidate=current,
        release_candidate_root=_relative(root, candidate_root, label="private candidate root"),
        source_export_root=_relative(root, export.output_root, label="private Methodology export"),
        frozen_manifest_sha256=export.frozen_manifest_sha256,
        export_inventory_sha256=export.inventory_digest,
        export_seal_sha256=_export_seal_sha256(candidate_root, exporter),
    )


def revalidate_sealed_methodology_export(value: SealedMethodologyExport) -> SealedMethodologyExport:
    """Re-open the seal immediately before a private compiler consumes it."""

    if not isinstance(value, SealedMethodologyExport):
        raise _error("release-methodology-export-untrusted", "compiler requires a locally bound sealed Methodology export")
    root = _root(value.candidate.project_root)
    observed = bind_sealed_methodology_export(value.candidate, root / value.release_candidate_root)
    if observed != value:
        raise _error("release-methodology-export-stale", "sealed Methodology export changed after handoff binding")
    return observed


def validate_source_copy(candidate: ValidatedCandidate, source_copy_root: Path | str | None = None) -> SealedSourceCopy:
    """Validate a completed derived copy before compiler or package admission."""

    current = _revalidate(candidate)
    root = _root(current.project_root)
    expected = root / DERIVED_SOURCE_COPY_RELATIVE
    supplied = expected if source_copy_root is None else Path(source_copy_root)
    if not supplied.is_absolute():
        supplied = root / supplied
    if supplied.resolve(strict=False) != expected.resolve(strict=False):
        raise _error("release-copy-root-invalid", "derived source copy root is not the D561 delivery root")
    copy_root = _directory(root, DERIVED_SOURCE_COPY_RELATIVE, code="release-copy-missing")
    actual = tree_sha256(root, copy_root)
    if actual != current.manifest.expected_derived_source_copy_sha256:
        raise _error("release-copy-digest-mismatch", "complete derived source copy does not match the sealed expectation")
    return SealedSourceCopy(current, DERIVED_SOURCE_COPY_RELATIVE, actual)


class CompilerEntrypoint(StrictModel):
    path: str
    sha256: str = Field(pattern="^[0-9a-f]{64}$")

    @field_validator("path")
    @classmethod
    def bounded_path(cls, value: str) -> str:
        return _safe_relative(value, "compiler entrypoint")


class CompilerSuccessEvidence(StrictModel):
    """Typed compiler result supplied by the future compiler adapter, never a mapping."""

    candidate_snapshot_manifest_sha256: str = Field(pattern="^[0-9a-f]{64}$")
    outcome: str
    compiler_entrypoint: CompilerEntrypoint
    compiler_frontier_digest: str = Field(pattern="^[0-9a-f]{64}$")
    child_materialization_root: str
    actual_compiled_output_sha256: str = Field(pattern="^[0-9a-f]{64}$")

    @field_validator("child_materialization_root")
    @classmethod
    def bounded_root(cls, value: str) -> str:
        return _safe_relative(value, "child_materialization_root")

    @model_validator(mode="after")
    def completed_only(self) -> "CompilerSuccessEvidence":
        if self.outcome != "completed":
            raise ValueError("compiler evidence must report completed")
        return self


class PackageRow(StrictModel):
    resource: Literal["FRAMEWORK_ENGINE", "METHODOLOGY", "SKILL", "PACKAGE_CONTROL"]
    source_path: str
    destination_path: str
    sha256: str = Field(pattern="^[0-9a-f]{64}$")
    mode: int = Field(ge=0, le=0o777)

    @field_validator("source_path", "destination_path")
    @classmethod
    def bounded_path(cls, value: str, info: Any) -> str:
        return _safe_relative(value, info.field_name)

    @model_validator(mode="after")
    def destination_matches_resource(self) -> "PackageRow":
        prefixes = {
            "FRAMEWORK_ENGINE": "FRAMEWORK_ENGINE/",
            "METHODOLOGY": "METHODOLOGY/",
            "SKILL": "SKILLS/ca/",
            "PACKAGE_CONTROL": VERSION_TOML_RELATIVE,
        }
        if not self.destination_path.startswith(prefixes[self.resource]):
            raise ValueError("package destination is outside its resource root")
        return self


class SealedCandidateCompilation(StrictModel):
    native_installed_n: Any = Field(default=None, exclude=True)
    candidate_snapshot_manifest_sha256: str = Field(pattern="^[0-9a-f]{64}$")
    authority: SealedAuthority
    framework_version: str
    version_toml_sha256: str = Field(pattern="^[0-9a-f]{64}$")
    source_copy_root: str
    expected_derived_source_copy_sha256: str = Field(pattern="^[0-9a-f]{64}$")
    actual_derived_source_copy_sha256: str = Field(pattern="^[0-9a-f]{64}$")
    compiler_entrypoint: CompilerEntrypoint
    compiler_frontier_digest: str = Field(pattern="^[0-9a-f]{64}$")
    expected_compiled_output_sha256: str = Field(pattern="^[0-9a-f]{64}$")
    actual_compiled_output_sha256: str = Field(pattern="^[0-9a-f]{64}$")
    child_materialization_root: str
    package_rows: list[PackageRow] = Field(min_length=1)

    @field_validator("source_copy_root", "child_materialization_root")
    @classmethod
    def bounded_roots(cls, value: str, info: Any) -> str:
        return _safe_relative(value, info.field_name)

    @model_validator(mode="after")
    def complete_package_rows(self) -> "SealedCandidateCompilation":
        if self.native_installed_n is not None and not isinstance(self.native_installed_n, NativeInstalledNBinding):
            raise ValueError("native N handoff must carry a concrete admitted binding")
        if (
            self.framework_version != self.authority.framework_version
            or self.version_toml_sha256 != self.authority.version_toml_sha256
        ):
            raise ValueError("sealed compilation version binding differs from authority")
        destinations = [row.destination_path for row in self.package_rows]
        if len(destinations) != len(set(destinations)):
            raise ValueError("package handoff has destination collisions")
        resources = {row.resource for row in self.package_rows}
        if not {"FRAMEWORK_ENGINE", "METHODOLOGY", "SKILL", "PACKAGE_CONTROL"} <= resources:
            raise ValueError("package handoff is not a complete Framework package")
        controls = [row for row in self.package_rows if row.resource == "PACKAGE_CONTROL"]
        if len(controls) != 1 or (
            controls[0].source_path != VERSION_TOML_RELATIVE
            or controls[0].destination_path != VERSION_TOML_RELATIVE
            or controls[0].sha256 != self.version_toml_sha256
        ):
            raise ValueError("package handoff must retain the exact root version.toml control row")
        if not {"SKILLS/ca/SKILL.md", "SKILLS/ca/agents/openai.yaml"} <= set(destinations):
            raise ValueError("package handoff lacks required ca Skill files")
        return self


def _package_rows(candidate: ValidatedCandidate, materialized_root: Path) -> list[PackageRow]:
    root = _root(candidate.project_root)
    rows: list[PackageRow] = []
    for inventory in candidate.manifest.source_inventory_rows:
        if inventory.resource == "IMAGE_INPUT":
            continue
        path = _file(root, inventory.source_path, code="release-current-input-missing")
        actual_sha = _sha256_bytes(path.read_bytes())
        actual_mode = path.stat().st_mode & 0o777
        if actual_sha != inventory.source_sha256 or actual_mode != inventory.source_mode:
            raise _error("release-currentness-stale", f"source inventory changed: {inventory.source_path}")
        rows.append(PackageRow(resource=inventory.resource, source_path=inventory.source_path, destination_path=inventory.destination_path, sha256=actual_sha, mode=actual_mode))
    for path in _regular_files(root, materialized_root, code="release-compiler-output-invalid"):
        rows.append(
            PackageRow(
                resource="METHODOLOGY",
                source_path=_relative(root, path, label="compiled output"),
                destination_path=f"METHODOLOGY/compiled/{path.relative_to(materialized_root).as_posix()}",
                sha256=_sha256_bytes(path.read_bytes()),
                mode=path.stat().st_mode & 0o777,
            )
        )
    return sorted(rows, key=lambda row: (row.destination_path, row.source_path, row.sha256))


def seal_candidate_compilation(
    source_copy: SealedSourceCopy,
    compiler_evidence: CompilerSuccessEvidence | None = None,
    materialization_root: Path | str | None = None,
) -> SealedCandidateCompilation:
    """Read and seal post-compiler evidence; compilation itself is not invoked."""

    if not isinstance(source_copy, SealedSourceCopy):
        raise _error("release-copy-untrusted", "source copy must be a locally validated sealed source copy")
    candidate = _revalidate(source_copy.candidate)
    root = _root(candidate.project_root)
    copy_root = _directory(root, source_copy.source_copy_root, code="release-copy-missing")
    actual_copy = tree_sha256(root, copy_root)
    if actual_copy != source_copy.actual_derived_source_copy_sha256 or actual_copy != candidate.manifest.expected_derived_source_copy_sha256:
        raise _error("release-copy-digest-mismatch", "source copy is stale, partial, or mismatched")
    expected_materialized = root / MATERIALIZED_RELATIVE / candidate.manifest.sha256
    supplied = expected_materialized if materialization_root is None else Path(materialization_root)
    if not supplied.is_absolute():
        supplied = root / supplied
    if supplied.resolve(strict=False) != expected_materialized.resolve(strict=False):
        raise _error("release-materialization-root-invalid", "compiler output is outside the sealed child materialization root")
    materialized = _directory(root, _relative(root, expected_materialized, label="materialization root"), code="release-compiler-output-missing")
    actual_output = tree_sha256(root, materialized)
    if actual_output != candidate.manifest.expected_compiled_output_sha256:
        raise _error("release-compiler-output-mismatch", "compiler output does not match the sealed expectation")
    compiler = _file(root, COMPILER_ENTRYPOINT_RELATIVE, code="release-compiler-entrypoint-missing")
    observed_entrypoint = CompilerEntrypoint(path=COMPILER_ENTRYPOINT_RELATIVE, sha256=_sha256_bytes(compiler.read_bytes()))
    if not isinstance(compiler_evidence, CompilerSuccessEvidence):
        raise _error("release-compiler-evidence-untrusted", "compiler success evidence must be a typed internal result")
    if compiler_evidence.outcome != "completed":
        raise _error("release-compiler-evidence-mismatch", "compiler evidence does not report a completed invocation")
    if compiler_evidence.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256:
        raise _error("release-compiler-evidence-mismatch", "compiler evidence identifies a different candidate")
    if compiler_evidence.compiler_entrypoint != observed_entrypoint:
        raise _error("release-compiler-evidence-mismatch", "compiler evidence does not match the locally observed compiler")
    if compiler_evidence.compiler_frontier_digest != candidate.authority.source_frontier_digest:
        raise _error("release-compiler-evidence-mismatch", "compiler evidence has a stale frontier")
    if compiler_evidence.child_materialization_root != _relative(root, materialized, label="materialization root"):
        raise _error("release-compiler-evidence-mismatch", "compiler evidence names a different materialization root")
    if compiler_evidence.actual_compiled_output_sha256 != actual_output:
        raise _error("release-compiler-evidence-mismatch", "compiler evidence does not match materialized bytes")
    return SealedCandidateCompilation(
        native_installed_n=candidate.native_installed_n,
        candidate_snapshot_manifest_sha256=candidate.manifest.sha256,
        authority=candidate.authority,
        framework_version=candidate.manifest.framework_version,
        version_toml_sha256=candidate.manifest.version_toml_sha256,
        source_copy_root=source_copy.source_copy_root,
        expected_derived_source_copy_sha256=candidate.manifest.expected_derived_source_copy_sha256,
        actual_derived_source_copy_sha256=actual_copy,
        compiler_entrypoint=observed_entrypoint,
        compiler_frontier_digest=candidate.authority.source_frontier_digest,
        expected_compiled_output_sha256=candidate.manifest.expected_compiled_output_sha256,
        actual_compiled_output_sha256=actual_output,
        child_materialization_root=_relative(root, materialized, label="materialization root"),
        package_rows=_package_rows(candidate, materialized),
    )


__all__ = [
    "CANONICAL_SOURCE_RELATIVE",
    "COMPILER_ENTRYPOINT_RELATIVE",
    "CURRENT_SELECTOR_RELATIVE",
    "NATIVE_CURRENT_SELECTOR_RELATIVE",
    "NativeInstalledNBinding",
    "bind_native_installed_n",
    "reopen_native_installed_n",
    "selected_n_selector_relative",
    "selected_n_identity",
    "DERIVED_SOURCE_COPY_RELATIVE",
    "MATERIALIZED_RELATIVE",
    "VERSION_TOML_RELATIVE",
    "CompilerEntrypoint",
    "CompilerSuccessEvidence",
    "PackageRow",
    "SealedCandidateCompilation",
    "SealedMethodologyExport",
    "SealedSourceCopy",
    "bind_sealed_methodology_export",
    "build_validated_candidate",
    "read_framework_version_toml",
    "revalidate_sealed_methodology_export",
    "seal_candidate_compilation",
    "tree_sha256",
    "validate_source_copy",
]
