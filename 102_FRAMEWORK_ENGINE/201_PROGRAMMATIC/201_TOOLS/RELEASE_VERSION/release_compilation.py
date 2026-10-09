"""Child-only Release Methodology rendering from the existing compiler primitives."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import shutil
import sys
import tempfile
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any, Mapping

from release_contract import CandidateBuildRequest, ReleaseContractError, ValidatedCandidate, canonical_json
from release_handoff import (
    CANONICAL_SOURCE_RELATIVE,
    COMPILER_ENTRYPOINT_RELATIVE,
    DERIVED_SOURCE_COPY_RELATIVE,
    MATERIALIZED_RELATIVE,
    CompilerEntrypoint,
    CompilerSuccessEvidence,
    SealedCandidateCompilation,
    SealedMethodologyExport,
    build_validated_candidate,
    read_framework_version_toml,
    revalidate_sealed_methodology_export,
    seal_candidate_compilation,
    tree_sha256,
    validate_source_copy,
)


CHILD_MANIFEST_NAME = "_release_manifest.json"
CHILD_MANIFEST_SCHEMA = "caprmedio.release_version.child_materialization.v1"
PRIVATE_COMPILED_MANIFEST_NAME = "compiled-delivery-manifest.json"
PRIVATE_COMPILED_SCHEMA = "caprmedio.release_version.private_methodology_compilation.v1"
PLACEHOLDER_COMPONENT = "p" * 64
_COMPILER_PATH = Path(__file__).resolve().parents[1] / "COMPILE_APPLICABLE_METHODOLOGY" / "compile_applicable_methodology.py"
EXECUTING_COMPILER_PATH = _COMPILER_PATH.resolve()
_SPEC = importlib.util.spec_from_file_location("_release_version_compiler", _COMPILER_PATH)
if _SPEC is None or _SPEC.loader is None:  # pragma: no cover - installation failure
    raise RuntimeError("Release compiler cannot load the selected Methodology compiler")
_COMPILER = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = _COMPILER
_SPEC.loader.exec_module(_COMPILER)


def _error(code: str, message: str) -> ReleaseContractError:
    return ReleaseContractError(code, message)


def _digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _root(value: Path | str) -> Path:
    root = Path(value).resolve()
    if not root.is_dir():
        raise _error("release-project-missing", "release project root is missing")
    return root


def _relative(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError as error:
        raise _error("release-path-unsafe", "release compiler path escapes project") from error


def _compiler_entrypoint(root: Path) -> CompilerEntrypoint:
    path = root / COMPILER_ENTRYPOINT_RELATIVE
    if path.is_symlink() or not path.is_file():
        raise _error("release-compiler-entrypoint-missing", "selected compiler entrypoint is missing")
    declared_bytes = path.read_bytes()
    executing_bytes = EXECUTING_COMPILER_PATH.read_bytes()
    if declared_bytes != executing_bytes:
        raise _error(
            "release-compiler-identity-mismatch",
            "declared compiler bytes do not match the compiler module executing this render",
        )
    return CompilerEntrypoint(path=COMPILER_ENTRYPOINT_RELATIVE, sha256=_digest(executing_bytes))


def _mkdir_safe(root: Path, relative: str) -> Path:
    """Create one descendant while refusing every existing symlink component."""

    current = root
    for component in Path(relative).parts:
        current = current / component
        if os.path.lexists(current):
            if current.is_symlink() or not current.is_dir():
                raise _error("release-materialization-path-unsafe", "child materialization has an unsafe existing path component")
        else:
            current.mkdir()
    return current


def _child_tree_digest(files: Mapping[str, bytes]) -> str:
    digest = hashlib.sha256()
    for relative, data in sorted(files.items()):
        encoded = relative.encode("utf-8")
        digest.update(len(encoded).to_bytes(8, "big"))
        digest.update(encoded)
        digest.update(len(data).to_bytes(8, "big"))
        digest.update(data)
    return digest.hexdigest()


def _child_manifest_bytes(
    *, candidate_release: str, framework_version: str, version_toml_sha256: str,
    compiler: CompilerEntrypoint, canonical_source_digest: str,
    frontier_digest: str, derived_copy_digest: str, nested_digest: str,
    output_files: Mapping[str, bytes],
) -> bytes:
    rows = [{"path": path, "sha256": _digest(data)} for path, data in sorted(output_files.items())]
    return canonical_json(
        {
            "schema": CHILD_MANIFEST_SCHEMA,
            "candidate_release": candidate_release,
            "framework_version": framework_version,
            "version_toml_sha256": version_toml_sha256,
            "compiler_entrypoint_path": compiler.path,
            "compiler_entrypoint_sha256": compiler.sha256,
            "canonical_source_snapshot_digest": canonical_source_digest,
            "compiler_frontier_digest": frontier_digest,
            "actual_derived_source_copy_sha256": derived_copy_digest,
            "nested_source_recursive_sha256_before": nested_digest,
            "nested_source_recursive_sha256_after": nested_digest,
            "output_rows": rows,
        }
    )


def _render_outputs(
    root: Path, candidates: list[Any], source_root: Path, child_root: Path, *, content_root: Path | None = None,
) -> dict[str, bytes]:
    outputs: dict[str, bytes] = {}
    for candidate in candidates:
        source = root / candidate.source_path
        if not source.is_relative_to(source_root):
            raise _error("release-compiler-source-invalid", f"selected source is outside admitted root: {candidate.source_path}")
        source_bytes_path = source if content_root is None else content_root / source.relative_to(source_root)
        if not source_bytes_path.is_file() or source_bytes_path.is_symlink():
            raise _error("release-compiler-source-invalid", f"selected source bytes are missing: {candidate.source_path}")
        target = child_root / candidate.role_directory / candidate.basename
        relative_source = Path(os.path.relpath(source, start=target.parent)).as_posix()
        rendered = _COMPILER.projection_bytes(source_bytes_path.read_bytes(), relative_source, candidate)
        child_relative = target.relative_to(child_root).as_posix()
        if child_relative == CHILD_MANIFEST_NAME or child_relative in outputs:
            raise _error("release-compiler-output-invalid", "selected compiler output has an unsafe collision")
        outputs[child_relative] = rendered
    if not outputs:
        raise _error("release-compiler-output-empty", "selected compiler rendered no child output")
    return outputs


def _report(root: Path, source_relative: str, output_relative: str) -> tuple[dict[str, Any], list[Any]]:
    canonical = _COMPILER.methodology_paths(root)
    places = _COMPILER.MethodologyPaths(
        source=Path(source_relative), output=Path(output_relative),
        structure_sha256=canonical.structure_sha256, control_root=canonical.control_root,
    )
    report, selected, _snapshot = _COMPILER.compile_report(root, places)
    if not report.get("can_apply"):
        raise _error("release-compiler-blocked", "selected compiler report has diagnostics or unresolved conflicts")
    return report, selected


def _canonical_frontier_from_copied_candidates(candidates: list[Any]) -> str:
    """Map copied-source paths back to their canonical counterparts for D566."""

    copied_root = Path(DERIVED_SOURCE_COPY_RELATIVE)
    canonical_root = Path(CANONICAL_SOURCE_RELATIVE)
    mapped: list[Any] = []
    for candidate in candidates:
        source = Path(candidate.source_path)
        try:
            canonical_source = canonical_root / source.relative_to(copied_root)
        except ValueError as error:
            raise _error("release-copied-frontier-invalid", "compiler selected a source outside the admitted copy") from error
        mapped.append(replace(candidate, source_path=canonical_source.as_posix()))
    return _COMPILER.frontier_digest(mapped)


@dataclass(frozen=True)
class ReleaseCompilationPreflight:
    candidate_release: str
    framework_version: str
    version_toml_sha256: str
    expected_derived_source_copy_sha256: str
    expected_compiled_output_sha256: str
    compiler_entrypoint: CompilerEntrypoint
    canonical_source_snapshot_digest: str
    compiler_frontier_digest: str
    nested_source_recursive_sha256_before: str
    output_files: dict[str, bytes]
    child_manifest_bytes: bytes


@dataclass(frozen=True)
class SealedPrivateMethodologyCompilation:
    """Private selected-snapshot projection bound to exporter seal evidence."""

    methodology_export: SealedMethodologyExport
    compiled_root: str
    compiled_manifest_sha256: str
    compiled_output_sha256: str


def _private_candidate_from_export(root: Path, export_root: Path, atom: Mapping[str, Any]) -> Any:
    """Rebuild only compiler projection metadata for an exporter-selected Atom.

    Activity selection is intentionally *not* rediscovered here: the sealed
    exporter inventory is the selected snapshot.  The compiler is used only
    for its reviewed projection-byte primitive and authored metadata digest.
    """

    source_path = atom.get("source_path")
    atom_id = atom.get("atom_id")
    version = atom.get("version")
    digest = atom.get("sha256")
    if not isinstance(source_path, str) or not isinstance(atom_id, str) or type(version) is not int or not isinstance(digest, str):
        raise _error("release-private-export-invalid", "sealed Atom inventory record is invalid")
    source = export_root / source_path
    if source.is_symlink() or not source.is_file() or _digest(source.read_bytes()) != digest:
        raise _error("release-private-export-stale", "sealed Atom bytes changed before private compilation")
    parts = Path(source_path).parts
    layers = {directory: (name, order) for name, directory, order, _ in _COMPILER.LAYERS}
    if not parts or parts[0] not in layers:
        raise _error("release-private-export-invalid", "sealed Atom source is outside the governed layer topology")
    layer, layer_order = layers[parts[0]]
    extension_id: str | None = None
    extension_revision: str | None = None
    if parts[0] == "002_INSTALLED_EXTENSIONS":
        if len(parts) < 5:
            raise _error("release-private-export-invalid", "sealed extension Atom path is invalid")
        extension_id, extension_revision, role_directory = parts[1], parts[2], parts[3]
    else:
        if len(parts) < 3:
            raise _error("release-private-export-invalid", "sealed core/configuration Atom path is invalid")
        role_directory = parts[1]
    role = _COMPILER.ROLE_BY_DIRECTORY.get(role_directory)
    if role is None or source.suffix != ".md":
        raise _error("release-private-export-invalid", "sealed Atom is outside a compiler role directory")
    try:
        data = source.read_bytes()
        frontmatter, _ = _COMPILER.split_frontmatter(data, source_path)
        if (
            _COMPILER.derive_atom_id(Path(source_path), frontmatter) != atom_id
            or _COMPILER.top_scalar(frontmatter, "status") != "Active"
            or _COMPILER.top_scalar(frontmatter, "version") != str(version)
        ):
            raise _error("release-private-export-stale", "sealed Atom metadata changed before private compilation")
        relative = _relative(root, source)
        return _COMPILER.Candidate(
            layer=layer,
            layer_order=layer_order,
            role=role,
            role_directory=role_directory,
            atom_id=atom_id,
            version=version,
            source_path=relative,
            source_sha256=digest,
            basename=source.name,
            priority=None,
            priority_group=None,
            replacements=(),
            incompatibilities=(),
            definition_term=None,
            definition_subject_path=None,
            output_relative="compiled",
            extension_id=extension_id,
            extension_revision=extension_revision,
            original_relations_sha256=_COMPILER.relations_digest(frontmatter),
        )
    except _COMPILER.CompileError as error:
        raise _error(error.code, error.message) from error


def _private_compiled_manifest(
    handoff: SealedMethodologyExport, compiler: CompilerEntrypoint, output_files: Mapping[str, bytes],
) -> bytes:
    rows = [{"path": path, "sha256": _digest(data)} for path, data in sorted(output_files.items())]
    unsigned = {
        "schema": PRIVATE_COMPILED_SCHEMA,
        "candidate_snapshot_manifest_sha256": handoff.candidate.manifest.sha256,
        "frozen_manifest_sha256": handoff.frozen_manifest_sha256,
        "export_inventory_sha256": handoff.export_inventory_sha256,
        "export_seal_sha256": handoff.export_seal_sha256,
        "source_export_root": handoff.source_export_root,
        "compiler_entrypoint_path": compiler.path,
        "compiler_entrypoint_sha256": compiler.sha256,
        "output_rows": rows,
    }
    return canonical_json({**unsigned, "sha256": _digest(canonical_json(unsigned))})


def read_sealed_private_methodology_compilation(value: SealedMethodologyExport) -> SealedPrivateMethodologyCompilation:
    """Re-open one private compiled delivery and prove all manifest bytes.

    A private ``compiled/`` directory without this final manifest is not a
    delivery.  This gives future full-gate/package consumers the same
    re-open-and-refuse boundary used by the source exporter.
    """

    handoff = revalidate_sealed_methodology_export(value)
    root = _root(handoff.candidate.project_root)
    compiled_root = root / handoff.release_candidate_root / "compiled"
    manifest_path = compiled_root / PRIVATE_COMPILED_MANIFEST_NAME
    if compiled_root.is_symlink() or not compiled_root.is_dir() or manifest_path.is_symlink() or not manifest_path.is_file():
        raise _error("release-private-compiled-unsealed", "private compiled delivery has no regular final manifest")
    try:
        raw = manifest_path.read_bytes()
        manifest = json.loads(raw.decode("utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise _error("release-private-compiled-invalid", "private compiled manifest is unreadable") from error
    required = {
        "schema", "candidate_snapshot_manifest_sha256", "frozen_manifest_sha256", "export_inventory_sha256",
        "export_seal_sha256", "source_export_root", "compiler_entrypoint_path", "compiler_entrypoint_sha256",
        "output_rows", "sha256",
    }
    if not isinstance(manifest, dict) or set(manifest) != required or raw != canonical_json(manifest):
        raise _error("release-private-compiled-invalid", "private compiled manifest is not canonical")
    unsigned = dict(manifest)
    checksum = unsigned.pop("sha256")
    if not isinstance(checksum, str) or checksum != _digest(canonical_json(unsigned)):
        raise _error("release-private-compiled-invalid", "private compiled manifest checksum is invalid")
    bindings = {
        "candidate_snapshot_manifest_sha256": handoff.candidate.manifest.sha256,
        "frozen_manifest_sha256": handoff.frozen_manifest_sha256,
        "export_inventory_sha256": handoff.export_inventory_sha256,
        "export_seal_sha256": handoff.export_seal_sha256,
        "source_export_root": handoff.source_export_root,
    }
    if manifest.get("schema") != PRIVATE_COMPILED_SCHEMA or any(manifest.get(key) != expected for key, expected in bindings.items()):
        raise _error("release-private-compiled-binding-mismatch", "private compiled manifest does not bind the sealed source delivery")
    compiler = _compiler_entrypoint(root)
    if (
        manifest.get("compiler_entrypoint_path") != compiler.path
        or manifest.get("compiler_entrypoint_sha256") != compiler.sha256
        or not isinstance(manifest.get("output_rows"), list)
    ):
        raise _error("release-private-compiled-binding-mismatch", "private compiled manifest does not bind the reviewed compiler")
    # The manifest cannot self-author a reduced projection: reopen the sealed
    # source export and regenerate the exact selected-snapshot bytes before
    # admitting its claimed output rows.
    from release_handoff import _exporter_module

    sealed = _exporter_module().read_sealed_export(release_candidate_root=root / handoff.release_candidate_root)
    atoms = sealed.inventory.get("atoms")
    if not isinstance(atoms, list) or not atoms:
        raise _error("release-private-export-invalid", "sealed Methodology export has no selected Atom rows")
    source_root = root / handoff.source_export_root
    candidates = [_private_candidate_from_export(root, source_root, atom) for atom in atoms if isinstance(atom, Mapping)]
    if len(candidates) != len(atoms):
        raise _error("release-private-export-invalid", "sealed Methodology export Atom rows are invalid")
    expected_rendered = _render_outputs(root, candidates, source_root, compiled_root)
    expected: dict[str, str] = {}
    for row in manifest["output_rows"]:
        if not isinstance(row, Mapping) or set(row) != {"path", "sha256"}:
            raise _error("release-private-compiled-invalid", "private compiled output row is invalid")
        relative, digest = row["path"], row["sha256"]
        path = Path(relative) if isinstance(relative, str) else Path("")
        if (
            not isinstance(relative, str) or not relative or "\\" in relative or path.is_absolute()
            or any(part in {"", ".", ".."} for part in path.parts)
            or not isinstance(digest, str) or len(digest) != 64 or any(char not in "0123456789abcdef" for char in digest)
            or relative in expected
        ):
            raise _error("release-private-compiled-invalid", "private compiled output row is unsafe")
        expected[relative] = digest
    observed: dict[str, bytes] = {}
    for path in compiled_root.rglob("*"):
        if path.is_symlink() or not (path.is_file() or path.is_dir()):
            raise _error("release-private-compiled-invalid", "private compiled delivery contains an unsafe entry")
        if path.is_file() and path != manifest_path:
            observed[path.relative_to(compiled_root).as_posix()] = path.read_bytes()
    if set(observed) != set(expected) or any(_digest(data) != expected[relative] for relative, data in observed.items()):
        raise _error("release-private-compiled-invalid", "private compiled bytes differ from its sealed manifest")
    if observed != expected_rendered:
        raise _error("release-private-compiled-invalid", "private compiled bytes differ from the sealed selected-snapshot projection")
    return SealedPrivateMethodologyCompilation(
        methodology_export=handoff,
        compiled_root=_relative(root, compiled_root),
        compiled_manifest_sha256=checksum,
        compiled_output_sha256=_child_tree_digest({**observed, PRIVATE_COMPILED_MANIFEST_NAME: raw}),
    )


def compile_sealed_methodology_export(value: SealedMethodologyExport) -> SealedPrivateMethodologyCompilation:
    """Compile exactly one exporter-sealed private source delivery.

    The result remains under ``.caprmedio_tmp/release_candidates/<run>/compiled``;
    it neither materializes canonical Methodology nor installs a release.
    """

    handoff = revalidate_sealed_methodology_export(value)
    root = _root(handoff.candidate.project_root)
    candidate_root = root / handoff.release_candidate_root
    export_root = root / handoff.source_export_root
    compiler = _compiler_entrypoint(root)
    # Re-opened handoff validation has already verified the private seal and
    # inventory shape.  Read only the sealed selected Atom rows.
    from release_handoff import _exporter_module  # local import avoids a second public API surface

    exporter_reader = _exporter_module()
    sealed = exporter_reader.read_sealed_export(release_candidate_root=candidate_root)
    atoms = sealed.inventory.get("atoms")
    if not isinstance(atoms, list) or not atoms:
        raise _error("release-private-export-invalid", "sealed Methodology export has no selected Atom rows")
    candidates = [_private_candidate_from_export(root, export_root, atom) for atom in atoms if isinstance(atom, Mapping)]
    if len(candidates) != len(atoms):
        raise _error("release-private-export-invalid", "sealed Methodology export Atom rows are invalid")
    compiled_root = candidate_root / "compiled"
    if compiled_root.exists() or compiled_root.is_symlink():
        raise _error("release-private-compiled-collision", "private candidate compiled delivery already exists")
    rendered = _render_outputs(root, candidates, export_root, compiled_root)
    manifest = _private_compiled_manifest(handoff, compiler, rendered)
    full_tree = {**rendered, PRIVATE_COMPILED_MANIFEST_NAME: manifest}
    expected_digest = _child_tree_digest(full_tree)
    staging = Path(tempfile.mkdtemp(prefix=".private-methodology-compile-", dir=candidate_root))
    try:
        for relative, data in full_tree.items():
            target = staging / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        if _child_tree_digest({path.relative_to(staging).as_posix(): path.read_bytes() for path in staging.rglob("*") if path.is_file()}) != expected_digest:
            raise _error("release-private-compiled-mismatch", "staged private compiled bytes differ from manifest")
        # Read the source seal again before the only private output effect.
        if revalidate_sealed_methodology_export(handoff) != handoff:
            raise _error("release-private-export-stale", "sealed Methodology export changed during private compilation")
        # macOS sandboxed filesystems reject a directory rename into a nested
        # newly-created candidate even when every component is private.  Publish
        # each payload atomically and the self-checking manifest *last*: without
        # that final manifest the delivery is explicitly not consumable.
        compiled_root.mkdir()
        for relative, data in sorted(full_tree.items()):
            if relative == PRIVATE_COMPILED_MANIFEST_NAME:
                continue
            target = compiled_root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = target.with_name(f".{target.name}.next")
            temporary.write_bytes(data)
            os.replace(temporary, target)
        if revalidate_sealed_methodology_export(handoff) != handoff:
            raise _error("release-private-export-stale", "sealed Methodology export changed while private bytes were staged")
        manifest_target = compiled_root / PRIVATE_COMPILED_MANIFEST_NAME
        manifest_next = manifest_target.with_name(f".{manifest_target.name}.next")
        manifest_next.write_bytes(manifest)
        os.replace(manifest_next, manifest_target)
    except Exception:
        shutil.rmtree(compiled_root, ignore_errors=True)
        shutil.rmtree(staging, ignore_errors=True)
        raise
    shutil.rmtree(staging, ignore_errors=True)
    return read_sealed_private_methodology_compilation(handoff)


def preflight_release_compilation(project_root: Path | str, *, candidate_release: str) -> ReleaseCompilationPreflight:
    """Predict complete child bytes before D566 sealing, without writes."""

    root = _root(project_root)
    framework_version, version_toml_sha256 = read_framework_version_toml(root)
    if framework_version != candidate_release:
        raise _error("release-version-mismatch", "root version.toml [framework].version must equal the candidate release")
    source_root = root / CANONICAL_SOURCE_RELATIVE
    if source_root.is_symlink() or not source_root.is_dir():
        raise _error("release-source-missing", "canonical Methodology source root is missing")
    placeholder_root = root / MATERIALIZED_RELATIVE / PLACEHOLDER_COMPONENT
    report, selected = _report(root, CANONICAL_SOURCE_RELATIVE, _relative(root, placeholder_root))
    source_digest = tree_sha256(root, source_root)
    copied_root = root / DERIVED_SOURCE_COPY_RELATIVE
    transformed: list[Any] = []
    for candidate in selected:
        source = root / candidate.source_path
        relative = source.relative_to(source_root)
        transformed.append(replace(candidate, source_path=(Path(DERIVED_SOURCE_COPY_RELATIVE) / relative).as_posix()))
    output_files = _render_outputs(root, transformed, copied_root, placeholder_root, content_root=source_root)
    actual_root = root / MATERIALIZED_RELATIVE / ("a" * 64)
    actual_files = _render_outputs(root, transformed, copied_root, actual_root, content_root=source_root)
    if output_files != actual_files:
        raise _error("release-placeholder-unstable", "candidate child component changes projected output bytes")
    compiler = _compiler_entrypoint(root)
    manifest = _child_manifest_bytes(
        candidate_release=candidate_release,
        framework_version=framework_version,
        version_toml_sha256=version_toml_sha256,
        compiler=compiler,
        canonical_source_digest=source_digest,
        frontier_digest=str(report["source_frontier_digest"]),
        derived_copy_digest=source_digest,
        nested_digest=source_digest,
        output_files=output_files,
    )
    full_tree = {**output_files, CHILD_MANIFEST_NAME: manifest}
    return ReleaseCompilationPreflight(
        candidate_release=candidate_release,
        framework_version=framework_version,
        version_toml_sha256=version_toml_sha256,
        expected_derived_source_copy_sha256=source_digest,
        expected_compiled_output_sha256=_child_tree_digest(full_tree),
        compiler_entrypoint=compiler,
        canonical_source_snapshot_digest=source_digest,
        compiler_frontier_digest=str(report["source_frontier_digest"]),
        nested_source_recursive_sha256_before=source_digest,
        output_files=output_files,
        child_manifest_bytes=manifest,
    )


def build_preflight_validated_candidate(
    project_root: Path | str, *, candidate_release: str, full_suite_environment: Mapping[str, Any],
    candidate_image_reference: str,
) -> tuple[ReleaseCompilationPreflight, ValidatedCandidate]:
    """Use predicted local hashes as D566 expectations, never caller hash values."""

    preflight = preflight_release_compilation(project_root, candidate_release=candidate_release)
    request = CandidateBuildRequest.model_validate(
        {
            "candidate_release": candidate_release,
            "expected_derived_source_copy_sha256": preflight.expected_derived_source_copy_sha256,
            "expected_compiled_output_sha256": preflight.expected_compiled_output_sha256,
            "full_suite_environment": full_suite_environment,
            "candidate_image_reference": candidate_image_reference,
        }
    )
    candidate = build_validated_candidate(
        project_root,
        request,
        observed_source_frontier_digest=preflight.compiler_frontier_digest,
    )
    if candidate.manifest.canonical_source_snapshot_digest != preflight.canonical_source_snapshot_digest:
        raise _error("release-currentness-stale", "preflight source snapshot changed before candidate sealing")
    if (
        candidate.manifest.framework_version != preflight.framework_version
        or candidate.manifest.version_toml_sha256 != preflight.version_toml_sha256
    ):
        raise _error("release-currentness-stale", "preflight root version.toml changed before candidate sealing")
    return preflight, candidate


def render_release_candidate(
    candidate: ValidatedCandidate, preflight: ReleaseCompilationPreflight,
) -> SealedCandidateCompilation:
    """Render the admitted copied source only into its sealed child root."""

    if not isinstance(candidate, ValidatedCandidate) or not isinstance(preflight, ReleaseCompilationPreflight):
        raise _error("release-compilation-untrusted", "renderer requires internal candidate and preflight objects")
    if candidate.intent.candidate_release != preflight.candidate_release:
        raise _error("release-preflight-mismatch", "preflight and candidate release differ")
    if candidate.manifest.expected_compiled_output_sha256 != preflight.expected_compiled_output_sha256:
        raise _error("release-preflight-mismatch", "candidate output expectation differs from preflight")
    if (
        candidate.manifest.framework_version != preflight.framework_version
        or candidate.manifest.version_toml_sha256 != preflight.version_toml_sha256
    ):
        raise _error("release-preflight-mismatch", "candidate version.toml binding differs from preflight")
    current_preflight = preflight_release_compilation(candidate.project_root, candidate_release=candidate.intent.candidate_release)
    if current_preflight != preflight:
        raise _error("release-currentness-stale", "canonical compiler report or predicted child output changed")
    source_copy = validate_source_copy(candidate)
    root = _root(candidate.project_root)
    canonical_before = tree_sha256(root, CANONICAL_SOURCE_RELATIVE)
    if canonical_before != candidate.authority.nested_source_recursive_sha256_before:
        raise _error("release-currentness-stale", "canonical nested source changed before child render")
    child_relative = f"{MATERIALIZED_RELATIVE}/{candidate.manifest.sha256}"
    child_root = root / child_relative
    if child_root.exists() or child_root.is_symlink():
        raise _error("release-child-collision", "sealed child materialization root already exists")
    report, selected = _report(root, DERIVED_SOURCE_COPY_RELATIVE, child_relative)
    if _canonical_frontier_from_copied_candidates(selected) != candidate.manifest.source_frontier_digest:
        raise _error("release-copied-frontier-mismatch", "copied compiler selection does not map to sealed canonical frontier")
    rendered = _render_outputs(root, selected, root / DERIVED_SOURCE_COPY_RELATIVE, child_root)
    if rendered != preflight.output_files:
        raise _error("release-render-mismatch", "copied-source render differs from preflight projection bytes")
    manifest = _child_manifest_bytes(
        candidate_release=candidate.manifest.candidate_release,
        framework_version=candidate.manifest.framework_version,
        version_toml_sha256=candidate.manifest.version_toml_sha256,
        compiler=preflight.compiler_entrypoint,
        canonical_source_digest=candidate.manifest.canonical_source_snapshot_digest,
        frontier_digest=preflight.compiler_frontier_digest,
        derived_copy_digest=source_copy.actual_derived_source_copy_sha256,
        nested_digest=canonical_before,
        output_files=rendered,
    )
    if manifest != preflight.child_manifest_bytes:
        raise _error("release-render-mismatch", "child manifest differs from preflight canonical bytes")
    staged_parent = _mkdir_safe(root, MATERIALIZED_RELATIVE)
    staging = Path(tempfile.mkdtemp(prefix=".release-render-", dir=staged_parent))
    try:
        for relative, data in rendered.items():
            target = staging / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        (staging / CHILD_MANIFEST_NAME).write_bytes(manifest)
        observed = tree_sha256(root, staging)
        if observed != preflight.expected_compiled_output_sha256:
            raise _error("release-render-mismatch", "staged child tree differs from preflight digest")
        os.replace(staging, child_root)
        canonical_after = tree_sha256(root, CANONICAL_SOURCE_RELATIVE)
        if canonical_after != canonical_before:
            raise _error("release-canonical-source-mutated", "child renderer changed canonical source")
    except Exception:
        shutil.rmtree(staging, ignore_errors=True)
        raise
    evidence = CompilerSuccessEvidence(
        candidate_snapshot_manifest_sha256=candidate.manifest.sha256,
        outcome="completed",
        compiler_entrypoint=preflight.compiler_entrypoint,
        compiler_frontier_digest=preflight.compiler_frontier_digest,
        child_materialization_root=child_relative,
        actual_compiled_output_sha256=preflight.expected_compiled_output_sha256,
    )
    return seal_candidate_compilation(source_copy, evidence)


__all__ = [
    "CHILD_MANIFEST_NAME",
    "CHILD_MANIFEST_SCHEMA",
    "PRIVATE_COMPILED_MANIFEST_NAME",
    "PRIVATE_COMPILED_SCHEMA",
    "ReleaseCompilationPreflight",
    "SealedPrivateMethodologyCompilation",
    "build_preflight_validated_candidate",
    "compile_sealed_methodology_export",
    "preflight_release_compilation",
    "read_sealed_private_methodology_compilation",
    "render_release_candidate",
]
