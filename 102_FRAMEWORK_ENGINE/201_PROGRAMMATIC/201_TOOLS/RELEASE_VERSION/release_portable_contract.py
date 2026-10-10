"""Read-only sealed inputs for one private portable Framework package.

This boundary binds the current D566 candidate and the actual sealed private
Methodology compilation to the exact files a later package producer may copy.
It deliberately does not assemble a package, select a release, run a gate, or
promote anything.
"""

from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

_TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(_TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_TOOLS_ROOT))

from framework_package import FrameworkPackageError, read_source_catalog_records  # noqa: E402
from release_compilation import SealedPrivateMethodologyCompilation, read_sealed_private_methodology_compilation
from release_contract import ReleaseContractError, ValidatedCandidate, canonical_json
from release_handoff import _exporter_module, _revalidate
from release_inventory import ReleaseInventoryError, persistent_regular_files, refuse_secret_path
from source_catalog_admission import SourceCatalogAdmissionError, read_source_admission_receipt


SCHEMA = "caprmedio.release_version.sealed_portable_candidate_compilation.v1"
ENGINE_ROOT = Path("102_FRAMEWORK_ENGINE")
SKILL_ROOT = ENGINE_ROOT / "202_AGENTIC/205_SKILLS/ca"
DEFAULTS_ROOT = Path("defaults")
DEPENDENCIES = (Path("pyproject.toml"), Path("uv.lock"))
VERSION = Path("version.toml")
CATALOG = Path("catalog.toml")


def _error(code: str, message: str) -> ReleaseContractError:
    return ReleaseContractError(code, message)


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _relative(value: object, *, field: str) -> Path:
    if not isinstance(value, str) or not value or "\\" in value:
        raise _error("portable-contract-path-invalid", f"{field} must be a safe relative path")
    path = Path(value)
    if path.is_absolute() or path == Path(".") or any(part in {"", ".", ".."} for part in path.parts):
        raise _error("portable-contract-path-invalid", f"{field} must be a safe relative path")
    try:
        refuse_secret_path(path)
    except ReleaseInventoryError as error:
        raise _error(error.code, str(error)) from error
    return path


def _root(value: Path | str) -> Path:
    root = Path(value).resolve(strict=True)
    if root.is_symlink() or not root.is_dir():
        raise _error("portable-contract-project-invalid", "candidate project root must be a real directory")
    return root


def _regular_file(root: Path, relative: Path, *, code: str = "portable-contract-source-missing") -> Path:
    _relative(relative.as_posix(), field="source path")
    cursor = root
    for part in relative.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise _error("portable-contract-source-symlink", f"portable source is a symlink: {relative.as_posix()}")
    if not cursor.is_file():
        raise _error(code, f"portable source is not a regular file: {relative.as_posix()}")
    try:
        cursor.resolve(strict=True).relative_to(root)
    except ValueError as error:
        raise _error("portable-contract-source-unsafe", f"portable source escapes project: {relative.as_posix()}") from error
    return cursor


def _regular_tree(root: Path, relative: Path, *, code: str) -> tuple[Path, ...]:
    directory = root / relative
    if directory.is_symlink() or not directory.is_dir():
        raise _error(code, f"portable source directory is missing: {relative.as_posix()}")
    try:
        files = tuple(persistent_regular_files(root, directory))
    except ReleaseInventoryError as error:
        raise _error(error.code, str(error)) from error
    if not files:
        raise _error(code, f"portable source directory is empty: {relative.as_posix()}")
    return files


def _row(resource: str, root: Path, source: Path, destination: Path, *, expected_sha256: str | None = None) -> "PortablePackageRow":
    relative = source.relative_to(root)
    file = _regular_file(root, relative)
    payload = file.read_bytes()
    digest = _digest(payload)
    if expected_sha256 is not None and digest != expected_sha256:
        raise _error("portable-contract-source-stale", f"sealed source digest changed: {relative.as_posix()}")
    return PortablePackageRow(resource, relative.as_posix(), destination.as_posix(), digest, file.stat().st_mode & 0o777)


@dataclass(frozen=True)
class PortablePackageRow:
    resource: str
    source_path: str
    destination_path: str
    sha256: str
    mode: int

    def record(self) -> dict[str, object]:
        return {
            "destination_path": self.destination_path,
            "mode": self.mode,
            "resource": self.resource,
            "sha256": self.sha256,
            "source_path": self.source_path,
        }


@dataclass(frozen=True)
class SealedPortableCandidateCompilation:
    """Typed, read-only portable package inputs bound to physical evidence."""

    candidate_run_id: str
    candidate: ValidatedCandidate
    private_compilation: SealedPrivateMethodologyCompilation
    portable_package_rows: tuple[PortablePackageRow, ...]
    source_catalog_sha256: str
    input_manifest_sha256: str

    @property
    def candidate_snapshot_manifest_sha256(self) -> str:
        return self.candidate.manifest.sha256

    @property
    def framework_version(self) -> str:
        return self.candidate.manifest.framework_version

    @property
    def version_toml_sha256(self) -> str:
        return self.candidate.manifest.version_toml_sha256

    @property
    def authority(self) -> Any:
        return self.candidate.authority


@dataclass(frozen=True)
class SealedPortableSourceSnapshot:
    """Read-only physical package inputs before catalog/admission finalization.

    The snapshot deliberately carries no root catalog or admission-proof row:
    collecting it observes source bytes only and cannot imply that those bytes
    were admitted for portable package publication.
    """

    candidate_run_id: str
    candidate: ValidatedCandidate
    private_compilation: SealedPrivateMethodologyCompilation
    portable_package_rows: tuple[PortablePackageRow, ...]


def _candidate_run_id(value: object, private: SealedPrivateMethodologyCompilation) -> str:
    if not isinstance(value, str) or not value or "\\" in value or Path(value).name != value or value in {".", ".."}:
        raise _error("portable-contract-run-invalid", "candidate run id must be one safe path component")
    try:
        refuse_secret_path(value)
    except ReleaseInventoryError as error:
        raise _error(error.code, str(error)) from error
    actual = Path(private.methodology_export.release_candidate_root).name
    if actual != value:
        raise _error("portable-contract-run-mismatch", "candidate run id differs from the sealed private compilation")
    return value


def _private_export(root: Path, private: SealedPrivateMethodologyCompilation) -> Any:
    handoff = private.methodology_export
    try:
        return _exporter_module().read_sealed_export(release_candidate_root=root / handoff.release_candidate_root)
    except Exception as error:
        code = getattr(error, "code", "portable-contract-export-invalid")
        raise _error(str(code), "private Methodology export is not sealed") from error


def _private_rows(root: Path, private: SealedPrivateMethodologyCompilation) -> list[PortablePackageRow]:
    export = _private_export(root, private)
    source_root = root / private.methodology_export.source_export_root
    rows: list[PortablePackageRow] = []
    atoms = export.inventory.get("atoms")
    supports = export.inventory.get("support")
    if not isinstance(atoms, list) or not atoms or not isinstance(supports, list) or not supports:
        raise _error("portable-contract-methodology-incomplete", "sealed export must carry selected Atoms and declared support")
    for item in atoms:
        if not isinstance(item, Mapping) or not isinstance(item.get("source_path"), str) or not isinstance(item.get("sha256"), str):
            raise _error("portable-contract-export-invalid", "sealed Atom row is invalid")
        path = _relative(item["source_path"], field="selected Atom source path")
        rows.append(_row("METHODOLOGY", root, source_root / path, Path("methodology/active") / path, expected_sha256=item["sha256"]))
    for item in supports:
        if not isinstance(item, Mapping) or not isinstance(item.get("path"), str) or not isinstance(item.get("sha256"), str):
            raise _error("portable-contract-export-invalid", "sealed support row is invalid")
        path = _relative(item["path"], field="support source path")
        rows.append(_row("METHODOLOGY_SUPPORT", root, source_root / path, Path("methodology/support") / path, expected_sha256=item["sha256"]))
    return rows


def _validate_source_rows(rows: list[PortablePackageRow]) -> tuple[PortablePackageRow, ...]:
    """Close the pre-catalog source shape without interpreting admission."""

    ordered = tuple(sorted(rows, key=lambda row: (row.destination_path, row.source_path, row.sha256)))
    if len({row.destination_path for row in ordered}) != len(ordered):
        raise _error("portable-contract-row-collision", "portable package rows have duplicate destinations")
    required_resources = {
        "FRAMEWORK_ENGINE",
        "SKILL",
        "DEPENDENCY",
        "PACKAGE_CONTROL",
        "DEFAULT",
        "METHODOLOGY",
        "METHODOLOGY_SUPPORT",
    }
    if {row.resource for row in ordered} != required_resources:
        raise _error("portable-contract-incomplete", "portable source rows are incomplete")
    return ordered


def _logical_digest(rows: tuple[PortablePackageRow, ...], relative: Path) -> str:
    exact = [row for row in rows if Path(row.destination_path).is_relative_to(relative)]
    if not exact:
        raise _error("catalog-source-missing", f"catalog source has no planned portable rows: {relative.as_posix()}")
    if len(exact) == 1 and Path(exact[0].destination_path) == relative:
        return exact[0].sha256
    records = [
        {
            "path": Path(row.destination_path).relative_to(relative).as_posix(),
            "sha256": row.sha256,
            "mode": row.mode,
        }
        for row in sorted(exact, key=lambda row: row.destination_path)
    ]
    return _digest(json.dumps(records, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def _validate_methodology_catalog_coverage(
    rows: tuple[PortablePackageRow, ...],
    records: tuple[tuple[str, Mapping[str, Any]], ...],
) -> None:
    """Require each sealed Methodology row to have one disjoint D561 root.

    This is deliberately a source-snapshot check, not a selection policy.  It
    keeps retained optional Extension and Configuration bytes visible to the
    catalog while leaving target-context selection to its separate boundary.
    """

    expected_singletons = {
        "core": Path("102_FRAMEWORK_ENGINE"),
        "support": Path("methodology/support"),
        "methodology": Path("methodology/active/001_CORE_META_MODEL"),
    }
    compiler_kinds = frozenset({"methodology", "extension", "configuration"})
    compiler_roots: list[Path] = []
    for kind, expected in expected_singletons.items():
        matching = [
            identity
            for identity, record in records
            if record["kind"] == kind and _relative(record["path"], field=f"source.{identity}.path") == expected
        ]
        if len(matching) != 1 or sum(record["kind"] == kind for _identity, record in records) != 1:
            raise _error(
                "catalog-topology-invalid",
                f"catalog must admit exactly one {kind} root at {expected.as_posix()}",
            )

    for identity, record in records:
        kind = str(record["kind"])
        relative = _relative(record["path"], field=f"source.{identity}.path")
        if kind == "configuration" and relative != Path("methodology/active/003_PROJECT_CONFIGURATION"):
            raise _error("catalog-topology-invalid", f"Configuration root is invalid: {identity}")
        if kind == "extension":
            prefix = Path("methodology/active/002_INSTALLED_EXTENSIONS")
            if not relative.is_relative_to(prefix) or len(relative.relative_to(prefix).parts) != 2:
                raise _error("catalog-topology-invalid", f"Extension root is not identity/revision scoped: {identity}")
        if kind in compiler_kinds:
            compiler_roots.append(relative)

    for index, left in enumerate(compiler_roots):
        for right in compiler_roots[index + 1:]:
            if left == right or left.is_relative_to(right) or right.is_relative_to(left):
                raise _error("catalog-methodology-overlap", "catalog Methodology descriptors overlap")

    material_rows = [row for row in rows if row.resource == "METHODOLOGY"]
    if not material_rows:
        raise _error("portable-contract-methodology-incomplete", "sealed portable source snapshot has no Methodology rows")
    for row in material_rows:
        destination = _relative(row.destination_path, field="Methodology destination path")
        matches = [root for root in compiler_roots if destination.is_relative_to(root)]
        if not matches:
            raise _error("catalog-methodology-uncovered", f"catalog does not admit Methodology row: {row.destination_path}")
        if len(matches) != 1:  # Defensive: descriptor overlap is rejected above.
            raise _error("catalog-methodology-overlap", f"catalog admits Methodology row more than once: {row.destination_path}")


def _catalog_records(catalog: bytes, rows: tuple[PortablePackageRow, ...]) -> tuple[tuple[str, Mapping[str, Any]], ...]:
    """Apply the shared closed descriptor reader to planned portable rows."""

    try:
        records = read_source_catalog_records(catalog)
    except FrameworkPackageError as error:
        raise _error(error.code, str(error)) from error
    for identity, record in records:
        path = _relative(record["path"], field=f"source.{identity}.path")
        if _logical_digest(rows, path) != record["sha256"]:
            raise _error("catalog-source-digest-mismatch", f"catalog source digest differs: {identity}")
    _validate_methodology_catalog_coverage(rows, records)
    return records


def _admission_rows(
    root: Path,
    records: tuple[tuple[str, Mapping[str, Any]], ...],
) -> list[PortablePackageRow]:
    """Reopen each catalog-referenced proof once and match every descriptor.

    Catalog metadata never substitutes for the retained canonical receipt.  A
    receipt can cover multiple catalog descriptors, but only one byte-identical
    ``SOURCE_ADMISSION`` row is sealed for that shared proof carrier.
    """

    receipts: dict[str, Any] = {}
    rows: list[PortablePackageRow] = []
    for identity, record in records:
        digest = record["admission_receipt_sha256"]
        if not isinstance(digest, str):  # The shared catalog reader normally catches this first.
            raise _error("catalog-invalid", f"catalog admission receipt is invalid: {identity}")
        receipt = receipts.get(digest)
        if receipt is None:
            relative = Path("admissions") / f"{digest}.json"
            receipt_file = _regular_file(root, relative, code="portable-contract-admission-missing")
            try:
                receipt = read_source_admission_receipt(receipt_file.read_bytes(), expected_sha256=digest)
            except SourceCatalogAdmissionError as error:
                raise _error(error.code, str(error)) from error
            receipts[digest] = receipt
            rows.append(_row("SOURCE_ADMISSION", root, receipt_file, relative, expected_sha256=digest))
        matches = [descriptor for descriptor in receipt.sources if descriptor.identity == identity]
        expected = (
            record["kind"],
            record["revision"],
            record["sha256"],
            record["visibility"],
            record["selection_default"],
            record["path"],
        )
        if len(matches) != 1 or (
            matches[0].kind,
            matches[0].revision,
            matches[0].sha256,
            matches[0].visibility,
            matches[0].selection_default,
            matches[0].path,
        ) != expected:
            raise _error("portable-contract-admission-mismatch", f"admission receipt differs from catalog source: {identity}")
    return rows


def _covered(destination: Path, kind: str, records: tuple[tuple[str, Mapping[str, Any]], ...]) -> bool:
    for _identity, record in records:
        if record["kind"] == kind and (destination == Path(record["path"]) or destination.is_relative_to(Path(record["path"]))):
            return True
    return False


def _validate_rows(rows: list[PortablePackageRow], records: tuple[tuple[str, Mapping[str, Any]], ...]) -> tuple[PortablePackageRow, ...]:
    ordered = tuple(sorted(rows, key=lambda row: (row.destination_path, row.source_path, row.sha256)))
    if len({row.destination_path for row in ordered}) != len(ordered):
        raise _error("portable-contract-row-collision", "portable package rows have duplicate destinations")
    expected_resources = {
        "FRAMEWORK_ENGINE",
        "SKILL",
        "DEPENDENCY",
        "PACKAGE_CONTROL",
        "CATALOG",
        "SOURCE_ADMISSION",
        "DEFAULT",
        "METHODOLOGY",
        "METHODOLOGY_SUPPORT",
    }
    if {row.resource for row in ordered} != expected_resources:
        raise _error("portable-contract-incomplete", "portable package rows are incomplete")
    for row in ordered:
        destination = Path(row.destination_path)
        if row.resource == "FRAMEWORK_ENGINE" and not _covered(destination, "core", records):
            raise _error("catalog-incomplete", f"catalog does not admit Framework Engine row: {row.destination_path}")
        if row.resource == "METHODOLOGY":
            matches = [
                record
                for _identity, record in records
                if record["kind"] in {"methodology", "extension", "configuration"}
                and destination.is_relative_to(Path(record["path"]))
            ]
            if len(matches) != 1:
                raise _error("catalog-incomplete", f"catalog does not admit Methodology row: {row.destination_path}")
        if row.resource == "METHODOLOGY_SUPPORT" and not _covered(destination, "support", records):
            raise _error("catalog-incomplete", f"catalog does not admit support row: {row.destination_path}")
    return ordered


def _manifest_sha256(run_id: str, candidate: ValidatedCandidate, private: SealedPrivateMethodologyCompilation, catalog: str, rows: tuple[PortablePackageRow, ...]) -> str:
    return _digest(canonical_json({
        "candidate_run_id": run_id,
        "candidate_snapshot_manifest_sha256": candidate.manifest.sha256,
        "framework_version": candidate.manifest.framework_version,
        "private_compiled_manifest_sha256": private.compiled_manifest_sha256,
        "private_compiled_output_sha256": private.compiled_output_sha256,
        "schema": SCHEMA,
        "source_catalog_sha256": catalog,
        "version_toml_sha256": candidate.manifest.version_toml_sha256,
        "portable_package_rows": [row.record() for row in rows],
    }))


def collect_portable_source_snapshot(
    candidate: ValidatedCandidate,
    private_compilation: SealedPrivateMethodologyCompilation,
    *,
    candidate_run_id: str,
) -> SealedPortableSourceSnapshot:
    """Collect revalidatable package inputs before catalog/admission finalization.

    This read-only operation opens neither ``catalog.toml`` nor any admission
    proof.  A later boundary supplies and validates those final carriers.
    """

    current = _revalidate(candidate)
    if not isinstance(private_compilation, SealedPrivateMethodologyCompilation):
        raise _error("portable-contract-untrusted", "portable contract requires an actual sealed private compilation")
    observed_private = read_sealed_private_methodology_compilation(private_compilation.methodology_export)
    if observed_private != private_compilation or observed_private.methodology_export.candidate != current:
        raise _error("portable-contract-private-stale", "private Methodology compilation differs from the current candidate")
    root = _root(current.project_root)
    run_id = _candidate_run_id(candidate_run_id, observed_private)
    rows: list[PortablePackageRow] = []
    for file in _regular_tree(root, ENGINE_ROOT, code="portable-contract-engine-missing"):
        relative = file.relative_to(root)
        rows.append(_row("FRAMEWORK_ENGINE", root, file, relative))
    for file in _regular_tree(root, SKILL_ROOT, code="portable-contract-skill-missing"):
        relative = file.relative_to(root)
        rows.append(_row("SKILL", root, file, Path("SKILLS/ca") / file.relative_to(root / SKILL_ROOT)))
    for dependency in DEPENDENCIES:
        rows.append(_row("DEPENDENCY", root, root / dependency, dependency))
    rows.append(_row("PACKAGE_CONTROL", root, root / VERSION, VERSION, expected_sha256=current.manifest.version_toml_sha256))
    for file in _regular_tree(root, DEFAULTS_ROOT, code="portable-contract-defaults-missing"):
        rows.append(_row("DEFAULT", root, file, file.relative_to(root)))
    rows.extend(_private_rows(root, observed_private))
    return SealedPortableSourceSnapshot(
        candidate_run_id=run_id,
        candidate=current,
        private_compilation=observed_private,
        portable_package_rows=_validate_source_rows(rows),
    )


def revalidate_portable_source_snapshot(value: SealedPortableSourceSnapshot) -> SealedPortableSourceSnapshot:
    """Re-open the pre-catalog source inputs and refuse changed evidence."""

    if not isinstance(value, SealedPortableSourceSnapshot):
        raise _error("portable-source-snapshot-untrusted", "portable source snapshot must be typed sealed evidence")
    observed = collect_portable_source_snapshot(
        value.candidate,
        value.private_compilation,
        candidate_run_id=value.candidate_run_id,
    )
    if observed != value:
        raise _error("portable-source-snapshot-stale", "portable source inputs changed after observation")
    return observed


def seal_portable_source_snapshot(
    snapshot: SealedPortableSourceSnapshot,
) -> SealedPortableCandidateCompilation:
    """Finalize one physically revalidated pre-catalog source snapshot.

    This boundary only reads and binds existing catalog/admission evidence.  It
    deliberately re-observes the exact supplied snapshot before opening the
    catalog, so a caller cannot seal a stale pre-admission observation.
    """

    source_snapshot = revalidate_portable_source_snapshot(snapshot)
    root = _root(source_snapshot.candidate.project_root)
    catalog_file = _regular_file(root, CATALOG, code="portable-contract-catalog-missing")
    catalog_bytes = catalog_file.read_bytes()
    catalog_digest = _digest(catalog_bytes)
    catalog_row = _row("CATALOG", root, catalog_file, CATALOG, expected_sha256=catalog_digest)
    rows = [*source_snapshot.portable_package_rows, catalog_row]
    provisional = tuple(sorted(rows, key=lambda row: (row.destination_path, row.source_path, row.sha256)))
    records = _catalog_records(catalog_bytes, provisional)
    rows.extend(_admission_rows(root, records))
    sealed_rows = _validate_rows(rows, records)
    return SealedPortableCandidateCompilation(
        candidate_run_id=source_snapshot.candidate_run_id,
        candidate=source_snapshot.candidate,
        private_compilation=source_snapshot.private_compilation,
        portable_package_rows=sealed_rows,
        source_catalog_sha256=catalog_digest,
        input_manifest_sha256=_manifest_sha256(
            source_snapshot.candidate_run_id,
            source_snapshot.candidate,
            source_snapshot.private_compilation,
            catalog_digest,
            sealed_rows,
        ),
    )


def build_sealed_portable_compilation(
    candidate: ValidatedCandidate,
    private_compilation: SealedPrivateMethodologyCompilation,
    *,
    candidate_run_id: str,
) -> SealedPortableCandidateCompilation:
    """Compatibility wrapper that collects then seals a fresh source snapshot."""

    return seal_portable_source_snapshot(
        collect_portable_source_snapshot(
            candidate,
            private_compilation,
            candidate_run_id=candidate_run_id,
        ),
    )


def revalidate_sealed_portable_compilation(value: SealedPortableCandidateCompilation) -> SealedPortableCandidateCompilation:
    """Re-observe every physical input and refuse a changed sealed contract."""

    if not isinstance(value, SealedPortableCandidateCompilation):
        raise _error("portable-contract-untrusted", "portable compilation must be a typed sealed contract")
    observed = build_sealed_portable_compilation(
        value.candidate,
        value.private_compilation,
        candidate_run_id=value.candidate_run_id,
    )
    if observed != value:
        raise _error("portable-contract-stale", "portable package inputs changed after sealing")
    return observed


__all__ = [
    "PortablePackageRow",
    "SCHEMA",
    "SealedPortableCandidateCompilation",
    "SealedPortableSourceSnapshot",
    "build_sealed_portable_compilation",
    "collect_portable_source_snapshot",
    "revalidate_portable_source_snapshot",
    "revalidate_sealed_portable_compilation",
    "seal_portable_source_snapshot",
]
