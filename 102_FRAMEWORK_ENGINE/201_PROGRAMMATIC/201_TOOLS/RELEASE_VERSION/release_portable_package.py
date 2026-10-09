"""Prepare one private, schema-1 reusable Framework package candidate.

This adapter deliberately has no promotion, selector, runtime, Skill, image,
Full Gate, or Journal effect.  It materializes only a D596 package tree below
the already-private D597 candidate root and delegates package identity and
reopening to :mod:`framework_package`.

The release handoff owns the sealed source rows.  In particular, this module
does not accept an ad-hoc catalog, admission receipt, or package manifest from
a caller: those would create a second authority beside the sealed candidate.
"""

from __future__ import annotations

import hashlib
import shutil
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


_TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(_TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_TOOLS_ROOT))

from framework_package import (  # noqa: E402
    FrameworkPackageError,
    VerifiedFrameworkPackage,
    assemble_framework_package,
    verify_framework_package,
)
from release_inventory import ReleaseInventoryError, persistent_regular_files, refuse_secret_path  # noqa: E402
from release_portable_contract import (  # noqa: E402
    SealedPortableCandidateCompilation,
    revalidate_sealed_portable_compilation,
)
from release_contract import ReleaseContractError  # noqa: E402


PRIVATE_CANDIDATES_ROOT = Path(".caprmedio_tmp/release_candidates")
PRIVATE_PACKAGE_ROOT = Path("package")
ENGINE_ROOT = Path("102_FRAMEWORK_ENGINE")
SKILL_SOURCE_ROOT = ENGINE_ROOT / "202_AGENTIC/205_SKILLS/ca"
DEFAULTS_ROOT = Path("defaults")
REQUIRED_DEPENDENCIES = frozenset({"pyproject.toml", "uv.lock"})
SHA256_LENGTH = 64


class PortableReleasePackageError(RuntimeError):
    """Stable refusal from the private portable-package preparation boundary."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


@dataclass(frozen=True)
class PreparedPortableReleasePackage:
    """A private candidate package re-opened through the shared verifier."""

    candidate_run_id: str
    candidate_snapshot_manifest_sha256: str
    input_manifest_sha256: str
    package: VerifiedFrameworkPackage

    @property
    def package_manifest_sha256(self) -> str:
        return self.package.manifest_digest

    @property
    def private_package_root(self) -> Path:
        return self.package.root


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _is_sha256(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == SHA256_LENGTH
        and value == value.lower()
        and all(character in "0123456789abcdef" for character in value)
    )


def _safe_relative(value: object, *, field: str) -> Path:
    if not isinstance(value, str) or not value:
        raise PortableReleasePackageError("portable-package-input-invalid", f"{field} must be a non-empty relative path")
    relative = Path(value)
    if relative.is_absolute() or relative == Path(".") or any(part in {"", ".", ".."} for part in relative.parts):
        raise PortableReleasePackageError("portable-package-input-invalid", f"{field} is unsafe")
    try:
        refuse_secret_path(relative)
    except ReleaseInventoryError as error:
        raise PortableReleasePackageError(error.code, str(error)) from error
    return relative


def _root(project_root: Path | str) -> Path:
    supplied = Path(project_root)
    try:
        root = supplied.resolve(strict=True)
    except OSError as error:
        raise PortableReleasePackageError("portable-package-project-missing", "project root is unavailable") from error
    if not root.is_dir() or root.is_symlink():
        raise PortableReleasePackageError("portable-package-project-invalid", "project root must be a real directory")
    return root


def _regular_source(root: Path, relative: Path, *, code: str = "portable-package-source-missing") -> Path:
    cursor = root
    for component in relative.parts:
        cursor = cursor / component
        if cursor.is_symlink():
            raise PortableReleasePackageError("portable-package-source-symlink", f"source is a symlink: {relative.as_posix()}")
    if not cursor.is_file():
        raise PortableReleasePackageError(code, f"required regular source is absent: {relative.as_posix()}")
    try:
        cursor.resolve(strict=True).relative_to(root)
    except ValueError as error:
        raise PortableReleasePackageError("portable-package-source-unsafe", f"source escapes project: {relative.as_posix()}") from error
    return cursor


def _regular_directory(root: Path, relative: Path) -> Path:
    cursor = root
    for component in relative.parts:
        cursor = cursor / component
        if cursor.is_symlink():
            raise PortableReleasePackageError("portable-package-source-symlink", f"source directory is a symlink: {relative.as_posix()}")
    if not cursor.is_dir():
        raise PortableReleasePackageError("portable-package-source-missing", f"required source directory is absent: {relative.as_posix()}")
    try:
        cursor.resolve(strict=True).relative_to(root)
    except ValueError as error:
        raise PortableReleasePackageError("portable-package-source-unsafe", f"source directory escapes project: {relative.as_posix()}") from error
    return cursor


def _row_value(row: object, name: str) -> object:
    value = getattr(row, name, None)
    if value is None:
        raise PortableReleasePackageError("portable-package-input-invalid", f"portable package row lacks {name}")
    return value


def _portable_rows(compilation: SealedPortableCandidateCompilation) -> tuple[object, ...]:
    rows = getattr(compilation, "portable_package_rows", None)
    if not isinstance(rows, (list, tuple)) or not rows:
        raise PortableReleasePackageError(
            "portable-package-input-incomplete",
            "sealed compilation does not carry complete portable package rows",
        )
    return tuple(rows)


def _candidate_run_id(compilation: SealedPortableCandidateCompilation) -> str:
    value = getattr(compilation, "candidate_run_id", None)
    if not isinstance(value, str) or not value or Path(value).name != value or value in {".", ".."}:
        raise PortableReleasePackageError("portable-package-input-incomplete", "sealed compilation lacks a safe candidate run id")
    try:
        refuse_secret_path(value)
    except ReleaseInventoryError as error:
        raise PortableReleasePackageError(error.code, str(error)) from error
    return value


def _row_paths(row: object) -> tuple[str, Path, Path, str, int]:
    resource = _row_value(row, "resource")
    source = _safe_relative(_row_value(row, "source_path"), field="portable row source_path")
    destination = _safe_relative(_row_value(row, "destination_path"), field="portable row destination_path")
    digest = _row_value(row, "sha256")
    mode = _row_value(row, "mode")
    if not isinstance(resource, str) or not _is_sha256(digest) or type(mode) is not int or not 0 <= mode <= 0o777:
        raise PortableReleasePackageError("portable-package-input-invalid", "portable package row has invalid resource, digest, or mode")
    return resource, source, destination, digest, mode


def _require_destination(resource: str, source: Path, destination: Path) -> None:
    if resource == "FRAMEWORK_ENGINE":
        if not source.is_relative_to(ENGINE_ROOT):
            raise PortableReleasePackageError("portable-package-input-invalid", "Engine row source is outside the Framework Engine")
        if destination != source:
            raise PortableReleasePackageError("portable-package-input-invalid", "Engine row must retain its source-relative path")
        return
    if resource == "DEPENDENCY":
        if source.as_posix() not in REQUIRED_DEPENDENCIES or destination != source:
            raise PortableReleasePackageError("portable-package-input-invalid", "dependency row must retain one exact root dependency carrier")
        return
    if resource == "PACKAGE_CONTROL":
        if source != Path("version.toml") or destination != source:
            raise PortableReleasePackageError("portable-package-input-invalid", "package control row must retain root version.toml")
        return
    if resource == "CATALOG":
        if source != Path("catalog.toml") or destination != source:
            raise PortableReleasePackageError("portable-package-input-invalid", "catalog row must retain root catalog.toml")
        return
    if resource == "SOURCE_ADMISSION":
        if (
            source != destination
            or source.parent != Path("admissions")
            or source.suffix != ".json"
            or not _is_sha256(source.stem)
        ):
            raise PortableReleasePackageError("portable-package-input-invalid", "admission row must retain its exact receipt path")
        return
    if resource == "DEFAULT":
        if not source.is_relative_to(DEFAULTS_ROOT) or destination != source:
            raise PortableReleasePackageError("portable-package-input-invalid", "default row must retain its defaults path")
        return
    if resource == "SKILL":
        if not source.is_relative_to(SKILL_SOURCE_ROOT):
            raise PortableReleasePackageError("portable-package-input-invalid", "Skill row source is outside the canonical ca Skill")
        if destination != Path("SKILLS/ca") / source.relative_to(SKILL_SOURCE_ROOT):
            raise PortableReleasePackageError("portable-package-input-invalid", "Skill row destination is invalid")
        return
    if resource == "METHODOLOGY":
        if not destination.is_relative_to(Path("methodology/active")):
            raise PortableReleasePackageError("portable-package-input-invalid", "active Methodology row destination is invalid")
        return
    if resource == "METHODOLOGY_SUPPORT":
        if not destination.is_relative_to(Path("methodology/support")):
            raise PortableReleasePackageError("portable-package-input-invalid", "Methodology support row destination is invalid")
        return
    raise PortableReleasePackageError("portable-package-input-invalid", f"unknown portable package resource: {resource}")


def _observed_files(root: Path, relative: Path) -> set[str]:
    directory = _regular_directory(root, relative)
    try:
        return {item.relative_to(root).as_posix() for item in persistent_regular_files(root, directory)}
    except ReleaseInventoryError as error:
        raise PortableReleasePackageError(error.code, str(error)) from error


def _validate_complete_rows(root: Path, rows: Iterable[object]) -> tuple[tuple[object, ...], dict[str, tuple[str, Path, Path, str, int]]]:
    records = tuple(rows)
    parsed = tuple(_row_paths(row) for row in records)
    if tuple(sorted(parsed, key=lambda item: (item[2].as_posix(), item[1].as_posix(), item[3]))) != parsed:
        raise PortableReleasePackageError("portable-package-input-invalid", "portable package rows must be destination ordered")
    destinations = [item[2].as_posix() for item in parsed]
    if len(destinations) != len(set(destinations)):
        raise PortableReleasePackageError("portable-package-input-invalid", "portable package rows have duplicate destinations")
    for resource, source, destination, _digest, _mode in parsed:
        _require_destination(resource, source, destination)

    by_resource: dict[str, list[tuple[str, Path, Path, str, int]]] = {}
    for item in parsed:
        by_resource.setdefault(item[0], []).append(item)

    # D596 names the *whole* Engine and the canonical ca Skill.  The ca
    # carrier therefore appears once inside the complete Engine and once at
    # SKILLS/ca for package-owned Skill publication; duplicate source bytes
    # are intentional, while their destinations remain unique and sealed.
    expected_engine = _observed_files(root, ENGINE_ROOT)
    actual_engine = {item[1].as_posix() for item in by_resource.get("FRAMEWORK_ENGINE", [])}
    if expected_engine != actual_engine:
        raise PortableReleasePackageError(
            "portable-package-input-incomplete",
            "portable rows do not cover the complete Framework Engine",
        )
    expected_defaults = _observed_files(root, DEFAULTS_ROOT)
    actual_defaults = {item[1].as_posix() for item in by_resource.get("DEFAULT", [])}
    if expected_defaults != actual_defaults:
        raise PortableReleasePackageError("portable-package-input-incomplete", "portable rows do not cover admitted defaults")
    expected_skill = _observed_files(root, SKILL_SOURCE_ROOT)
    actual_skill = {item[1].as_posix() for item in by_resource.get("SKILL", [])}
    if expected_skill != actual_skill:
        raise PortableReleasePackageError("portable-package-input-incomplete", "portable rows do not cover the canonical ca Skill")
    if not by_resource.get("METHODOLOGY") or not by_resource.get("METHODOLOGY_SUPPORT"):
        raise PortableReleasePackageError("portable-package-input-incomplete", "portable rows lack active Methodology or declared support")
    if {item[1].as_posix() for item in by_resource.get("DEPENDENCY", [])} != REQUIRED_DEPENDENCIES:
        raise PortableReleasePackageError("portable-package-input-incomplete", "portable rows lack exact dependency carriers")
    if [item[1].as_posix() for item in by_resource.get("PACKAGE_CONTROL", [])] != ["version.toml"]:
        raise PortableReleasePackageError("portable-package-input-incomplete", "portable rows lack exact version carrier")
    if [item[1].as_posix() for item in by_resource.get("CATALOG", [])] != ["catalog.toml"]:
        raise PortableReleasePackageError("portable-package-input-incomplete", "portable rows lack exact catalog carrier")
    if not by_resource.get("SOURCE_ADMISSION"):
        raise PortableReleasePackageError("portable-package-input-incomplete", "portable rows lack source-admission proof")
    for _resource, source, _destination, digest, _mode in by_resource["SOURCE_ADMISSION"]:
        if source.stem != digest:
            raise PortableReleasePackageError("portable-package-input-invalid", "admission filename must equal its sealed byte digest")
    catalog_rows = {item[1].as_posix(): item for item in by_resource.get("CATALOG", [])}
    return records, catalog_rows


def _validate_catalog_binding(compilation: SealedPortableCandidateCompilation, rows: dict[str, tuple[str, Path, Path, str, int]]) -> None:
    sealed_catalog_digest = getattr(compilation, "source_catalog_sha256", None)
    catalog = rows.get("catalog.toml")
    if not _is_sha256(sealed_catalog_digest) or catalog is None or catalog[3] != sealed_catalog_digest:
        raise PortableReleasePackageError(
            "portable-package-input-incomplete",
            "sealed compilation does not bind the exact catalog carrier",
        )


def _copy_assembly(root: Path, assembly: Path, rows: Iterable[object]) -> None:
    for row in rows:
        _resource, source_relative, destination, expected_digest, expected_mode = _row_paths(row)
        source = _regular_source(root, source_relative)
        payload = source.read_bytes()
        actual_mode = source.stat().st_mode & 0o777
        if _sha256(payload) != expected_digest or actual_mode != expected_mode:
            raise PortableReleasePackageError(
                "portable-package-source-drift",
                f"sealed portable source changed: {source_relative.as_posix()}",
            )
        target = assembly / destination
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream:
            stream.write(payload)
        target.chmod(expected_mode)


def _candidate_package_root(root: Path, candidate_run_id: str) -> Path:
    base = root / PRIVATE_CANDIDATES_ROOT
    for directory in (root / ".caprmedio_tmp", base, base / candidate_run_id, base / candidate_run_id / PRIVATE_PACKAGE_ROOT):
        if directory.is_symlink():
            raise PortableReleasePackageError("portable-package-private-root-unsafe", "private candidate root contains a symlink")
        if directory.exists() and not directory.is_dir():
            raise PortableReleasePackageError("portable-package-private-root-unsafe", "private candidate root is not a directory")
        directory.mkdir(exist_ok=True)
    return base / candidate_run_id / PRIVATE_PACKAGE_ROOT


def prepare_portable_release_package(
    project_root: Path | str,
    sealed_compilation: SealedPortableCandidateCompilation,
) -> PreparedPortableReleasePackage:
    """Prepare and reopen the D596 package beneath one private D597 candidate.

    The caller must already have a typed post-compiler sealed handoff with the
    portable rows and catalog binding.  This function never promotes the
    result, writes an installation selector, activates a runtime, or treats a
    gate/image result as available.
    """

    if not isinstance(sealed_compilation, SealedPortableCandidateCompilation):
        raise PortableReleasePackageError("portable-package-untrusted", "portable package preparation requires a typed sealed portable compilation")
    root = _root(project_root)
    try:
        current = revalidate_sealed_portable_compilation(sealed_compilation)
    except ReleaseContractError as error:
        raise PortableReleasePackageError(error.code, str(error)) from error
    candidate_root = _root(current.candidate.project_root)
    if candidate_root != root:
        raise PortableReleasePackageError("portable-package-project-mismatch", "caller project root differs from the sealed candidate project")
    candidate_sha256 = current.candidate_snapshot_manifest_sha256
    if not _is_sha256(candidate_sha256) or candidate_sha256 != current.authority.expected_candidate_snapshot_manifest_sha256:
        raise PortableReleasePackageError("portable-package-untrusted", "sealed compilation is not bound to its candidate manifest")
    candidate_run_id = _candidate_run_id(current)
    rows, by_source = _validate_complete_rows(root, _portable_rows(current))
    _validate_catalog_binding(current, by_source)
    package_root = _candidate_package_root(root, candidate_run_id)

    staging = Path(tempfile.mkdtemp(prefix=".portable-source-", dir=root / ".caprmedio_tmp"))
    try:
        _copy_assembly(root, staging, rows)
        try:
            package = assemble_framework_package(staging, package_root)
            reopened = verify_framework_package(package.root)
        except FrameworkPackageError as error:
            raise PortableReleasePackageError(error.code, str(error)) from error
        if reopened != package:
            raise PortableReleasePackageError("portable-package-reopen-mismatch", "reopened package differs from assembly handoff")
        if reopened.source_catalog_sha256 != current.source_catalog_sha256:
            raise PortableReleasePackageError("portable-package-catalog-stale", "reopened package catalog differs from sealed catalog")
        if reopened.framework_version != current.framework_version or reopened.version_toml_sha256 != current.version_toml_sha256:
            raise PortableReleasePackageError("portable-package-version-stale", "reopened package version differs from sealed candidate")
        if reopened.manifest_digest == candidate_sha256:
            raise PortableReleasePackageError("portable-package-identity-collision", "candidate and package manifest identities must remain distinct")
        return PreparedPortableReleasePackage(candidate_run_id, candidate_sha256, current.input_manifest_sha256, reopened)
    finally:
        if staging.exists():
            shutil.rmtree(staging, ignore_errors=True)


def reopen_portable_release_package(
    project_root: Path | str,
    candidate_run_id: str,
    package_manifest_sha256: str,
) -> VerifiedFrameworkPackage:
    """Reopen one private candidate package without selecting or promoting it."""

    root = _root(project_root)
    if not isinstance(candidate_run_id, str) or not candidate_run_id or Path(candidate_run_id).name != candidate_run_id:
        raise PortableReleasePackageError("portable-package-input-invalid", "candidate run id is unsafe")
    try:
        refuse_secret_path(candidate_run_id)
    except ReleaseInventoryError as error:
        raise PortableReleasePackageError(error.code, str(error)) from error
    if not _is_sha256(package_manifest_sha256):
        raise PortableReleasePackageError("portable-package-input-invalid", "package manifest digest is invalid")
    package = root / PRIVATE_CANDIDATES_ROOT / candidate_run_id / PRIVATE_PACKAGE_ROOT / package_manifest_sha256
    try:
        return verify_framework_package(package)
    except FrameworkPackageError as error:
        raise PortableReleasePackageError(error.code, str(error)) from error


__all__ = [
    "PRIVATE_CANDIDATES_ROOT",
    "PRIVATE_PACKAGE_ROOT",
    "PortableReleasePackageError",
    "PreparedPortableReleasePackage",
    "prepare_portable_release_package",
    "reopen_portable_release_package",
]
