"""Install one package-bound Applicable Methodology delivery after a Full Gate.

This module is deliberately narrower than a general installer.  It accepts the
already re-opened portable-installation preparation, reconstructs only the
package-admitted Methodology source view, and publishes just the compiler-owned
role folders below the Project's declared Applicable Methodology delivery root.
It never writes the authoritative source subtree, a package selector, runtime
configuration, a Skill, or Journal evidence.
"""

from __future__ import annotations

import argparse as _argparse
import builtins
import collections as _collections
import collections.abc as _collections_abc
import contextlib as _contextlib
import contextvars as _contextvars
import dataclasses as _dataclasses
import datetime as _datetime
import __future__ as _future
import hashlib
import importlib.util
import json
import os
import pathlib as _pathlib
import re as _re
import shutil
import stat
import sys
import sysconfig as _sysconfig
import tempfile
import threading
import time as _time
import tomllib
import types
import typing as _typing
import zoneinfo as _zoneinfo
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from framework_installation import (
    InstallationError,
    PortableInstallationPreparation,
    PortableInstallationRequest,
    prepare_portable_installation,
    verify_prospective_portable_full_gate,
)
from framework_package import (
    CATALOG_NAME,
    CurrentPackageSelector,
    FrameworkPackageError,
    PackageInventoryRow,
    VerifiedFrameworkPackage,
    read_source_catalog_records,
    verify_framework_package,
)
from installation_context import (
    CONTEXTS_DIRECTORY,
    InstallationContextError,
    TargetProjectContext,
    bind_target_project_context,
    reopen_target_project_context,
)
from installation_transaction import InstallationPublicationLock, InstallationTransactionError


_TOOLS_ROOT = Path(__file__).resolve().parent
_COMPILER_SPEC = importlib.util.spec_from_file_location(
    "caprmedio_portable_methodology_compiler",
    _TOOLS_ROOT / "COMPILE_APPLICABLE_METHODOLOGY" / "compile_applicable_methodology.py",
)
assert _COMPILER_SPEC and _COMPILER_SPEC.loader
compiler = importlib.util.module_from_spec(_COMPILER_SPEC)
sys.modules[_COMPILER_SPEC.name] = compiler
_COMPILER_SPEC.loader.exec_module(compiler)


_ACTIVE_ROOT = Path("methodology/active")
_SUPPORT_ROOT = Path("methodology/support")
_DEFAULT_OUTPUT_SUFFIX = Path("000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY")
_SOURCE_SUFFIX = Path("000_APPLICABLE_MTHD_sources")
_STAGE_ROOT = Path(".caprmedio_tmp/installation/staging")
_MANIFEST_NAME = "portable-methodology-delivery.json"
_MANIFEST_SCHEMA = "caprmedio.portable_methodology_delivery.v1"
_SHA256_CHARS = frozenset("0123456789abcdef")
_COMPILER_KINDS = frozenset({"methodology", "extension", "configuration"})
_SUPPORT_KIND = "support"
PACKAGE_COMPILER_RELATIVE = Path(
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/"
    "COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py"
)
# The package compiler imports ``artifact_metadata`` by its historic top-level
# name.  That module, in turn, imports these exact local helpers.  Loading the
# closure through the package inventory prevents an N publisher process from
# satisfying those imports from its checkout or from a prior package retained
# in ``sys.modules``.
_PACKAGE_COMPILER_DEPENDENCIES = (
    ("project_runtime", Path("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/project_runtime.py"), False),
    ("VALIDATE_ATOMS.validate_atoms_workers", Path("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/__init__.py"), True),
    ("VALIDATE_ATOMS.validate_atoms_workers.read_io", Path("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/read_io.py"), False),
    ("VALIDATE_ATOMS.validate_atoms_workers.settings", Path("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/settings.py"), False),
    ("project_selection", Path("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/project_selection.py"), False),
    ("artifact_metadata", Path("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/artifact_metadata.py"), False),
)
_PACKAGE_COMPILER_IMPORT_LOCK = threading.RLock()
_PACKAGE_COMPILER_LOCAL_TOP_LEVEL = frozenset({"artifact_metadata", "project_runtime", "project_selection", "VALIDATE_ATOMS"})
_TRUSTED_STDLIB_MODULES = {
    "argparse": _argparse,
    "collections": _collections,
    "collections.abc": _collections_abc,
    "contextlib": _contextlib,
    "contextvars": _contextvars,
    "dataclasses": _dataclasses,
    "datetime": _datetime,
    "__future__": _future,
    "hashlib": hashlib,
    "json": json,
    "os": os,
    "pathlib": _pathlib,
    "re": _re,
    "shutil": shutil,
    "stat": stat,
    "sys": sys,
    "tempfile": tempfile,
    "time": _time,
    "tomllib": tomllib,
    "types": types,
    "typing": _typing,
    "zoneinfo": _zoneinfo,
}


def _trusted_stdlib_module(name: str) -> Any:
    """Return one prebound standard-library module after an origin check.

    The package loader never resolves a standard-library name through the
    mutable ambient ``sys.modules`` table.  This check makes the whitelist a
    real origin boundary rather than just a spelling allowlist.
    """

    module = _TRUSTED_STDLIB_MODULES.get(name)
    if module is None:
        module = _TRUSTED_STDLIB_MODULES.get(name.split(".", 1)[0])
    if module is None:
        raise _error("portable-methodology-package-compiler-dependency-unadmitted", "package compiler imports a standard-library module outside its admitted loader whitelist")
    specification = getattr(module, "__spec__", None)
    origin = getattr(specification, "origin", None)
    if origin in {"built-in", "frozen"}:
        return module
    if not isinstance(origin, str):
        raise _error("portable-methodology-package-compiler-dependency-invalid", "package compiler standard-library dependency has no verifiable origin")
    try:
        stdlib = Path(_sysconfig.get_path("stdlib")).resolve(strict=True)
        source = Path(origin).resolve(strict=True)
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise _error("portable-methodology-package-compiler-dependency-invalid", "package compiler standard-library dependency origin is unavailable") from error
    if not source.is_relative_to(stdlib):
        raise _error("portable-methodology-package-compiler-dependency-invalid", "package compiler standard-library dependency origin is outside Python stdlib")
    return module


class PortableMethodologyInstallationError(RuntimeError):
    """A stable refusal from the package-to-Project Methodology boundary."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(message)


@dataclass(frozen=True)
class PackageCompilerBinding:
    """One admitted immutable compiler carrier in a verified package."""

    package_manifest_sha256: str
    path: str
    sha256: str
    mode: int


@dataclass(frozen=True)
class PortableMethodologyFile:
    """One exact published compiler-owned carrier."""

    path: str
    sha256: str
    mode: int


@dataclass(frozen=True)
class PortableMethodologyDelivery:
    """Immutable post-publication proof for the eventual installation publisher."""

    package_manifest_sha256: str
    source_catalog_sha256: str
    target_project_context_sha256: str
    compiler_sha256: str
    compiler_frontier_sha256: str
    source_view_sha256: str
    authoring_source_sha256: str
    output_tree_sha256: str
    delivery_manifest_sha256: str
    output_root: Path
    delivery_manifest_path: Path
    files: tuple[PortableMethodologyFile, ...]


@dataclass(frozen=True)
class PreparedCandidateMethodologyPublication:
    """Reopened gated candidate bytes, still inert until lock-owned publication.

    This is deliberately not a replacement for a D598 selector and grants no
    activation or execution authority.  It records the exact private export
    and compiled tree already consumed by the native Full Gate, so a later
    selected-release publisher cannot silently compile a fresh projection.
    """

    package_manifest_sha256: str
    source_catalog_sha256: str
    target_project_context_sha256: str
    gate_receipt_sha256: str
    candidate_snapshot_manifest_sha256: str
    candidate_run_id: str
    source_export_root: Path
    compiled_root: Path
    frozen_manifest_sha256: str
    export_inventory_sha256: str
    export_seal_sha256: str
    compiled_manifest_sha256: str
    source_files: tuple[PortableMethodologyFile, ...]
    compiled_files: tuple[PortableMethodologyFile, ...]


@dataclass(frozen=True)
class CandidatePortableMethodologyDelivery:
    """Lock-owned publication proof for bytes previously passed by Full Gate."""

    package_manifest_sha256: str
    source_catalog_sha256: str
    target_project_context_sha256: str
    gate_receipt_sha256: str
    candidate_snapshot_manifest_sha256: str
    candidate_run_id: str
    source_export_sha256: str
    compiled_output_sha256: str
    delivery_manifest_sha256: str
    source_export_root: Path
    output_root: Path
    delivery_manifest_path: Path
    files: tuple[PortableMethodologyFile, ...]


@dataclass(frozen=True)
class PreparedTargetMethodologySource:
    """One selected, verified package member in a direct target source view."""

    identity: str
    kind: str
    package_path: str
    source_view_path: str
    sha256: str
    mode: int


@dataclass(frozen=True)
class PreparedTargetMethodologyFile:
    """One immutable pre-delete compiler output payload."""

    path: str
    sha256: str
    mode: int
    payload: bytes


@dataclass(frozen=True)
class PreparedTargetMethodologyPublication:
    """Target-specific O200 compilation prepared before any deletion.

    Unlike :class:`PreparedCandidateMethodologyPublication`, this value is
    not an O169 promotion copy.  It records a target's explicit selection and
    frozen compiler outputs so the publisher can stage bytes later without
    invoking the compiler after destructive work begins.
    """

    package_manifest_sha256: str
    source_catalog_sha256: str
    target_project_context_sha256: str
    gate_receipt_sha256: str
    selected_source_identities: tuple[str, ...]
    compiler_sha256: str
    compiler_frontier_sha256: str
    source_view_sha256: str
    authoring_source_sha256: str
    source_members: tuple[PreparedTargetMethodologySource, ...]
    files: tuple[PreparedTargetMethodologyFile, ...]
    manifest_bytes: bytes
    manifest_sha256: str


@dataclass(frozen=True)
class TargetPortableMethodologyDelivery:
    """Lock-owned publication proof for one precompiled direct target view."""

    package_manifest_sha256: str
    source_catalog_sha256: str
    target_project_context_sha256: str
    gate_receipt_sha256: str
    compiler_frontier_sha256: str
    source_view_sha256: str
    output_tree_sha256: str
    delivery_manifest_sha256: str
    output_root: Path
    delivery_manifest_path: Path
    files: tuple[PortableMethodologyFile, ...]


@dataclass(frozen=True)
class _SourceMember:
    identity: str
    kind: str
    package_path: Path
    source_relative: Path
    payload: bytes
    sha256: str
    mode: int


def _error(code: str, message: str) -> PortableMethodologyInstallationError:
    return PortableMethodologyInstallationError(code, message)


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _is_sha256(value: object) -> bool:
    return isinstance(value, str) and len(value) == 64 and set(value) <= _SHA256_CHARS


def _safe_absolute(value: object) -> Path | None:
    if not isinstance(value, str):
        return None
    path = Path(value)
    if not path.is_absolute() or ".." in path.parts:
        return None
    return path


def _safe_relative(value: object, *, label: str) -> Path:
    if not isinstance(value, str) or not value:
        raise _error("portable-methodology-path-invalid", f"{label} must be a non-empty relative path")
    relative = Path(value)
    if (
        relative.is_absolute()
        or relative == Path(".")
        or "\\" in value
        or any(part in {"", ".", ".."} for part in relative.parts)
    ):
        raise _error("portable-methodology-path-invalid", f"{label} is unsafe")
    return relative


def _root(value: Path | str) -> Path:
    try:
        supplied = Path(value)
        if not supplied.is_absolute() or ".." in supplied.parts:
            raise _error("portable-methodology-target-invalid", "target Project root must be an explicit absolute path")
        root = Path(os.path.abspath(supplied))
        for ancestor in (root, *root.parents):
            if ancestor.is_symlink():
                raise _error("portable-methodology-target-invalid", "target Project root has a symlinked ancestor")
        observed = root.lstat()
    except PortableMethodologyInstallationError:
        raise
    except (OSError, TypeError, ValueError) as error:
        raise _error("portable-methodology-target-invalid", "target Project root is unavailable") from error
    if not stat.S_ISDIR(observed.st_mode):
        raise _error("portable-methodology-target-invalid", "target Project root is not a regular directory")
    return root


def _regular(root: Path, relative: Path, *, code: str) -> Path:
    path = root
    for component in relative.parts:
        path = path / component
        try:
            observed = path.lstat()
        except OSError as error:
            raise _error(code, f"required carrier is missing: {relative.as_posix()}") from error
        if stat.S_ISLNK(observed.st_mode):
            raise _error("portable-methodology-symlink", f"carrier has a symlink ancestor: {relative.as_posix()}")
    if not stat.S_ISREG(path.stat().st_mode):
        raise _error(code, f"required carrier is not regular: {relative.as_posix()}")
    return path


def _directory(root: Path, relative: Path, *, missing_ok: bool = False) -> Path | None:
    path = root
    for component in relative.parts:
        path = path / component
        try:
            observed = path.lstat()
        except FileNotFoundError:
            if missing_ok:
                return None
            raise _error("portable-methodology-target-missing", f"required directory is missing: {relative.as_posix()}")
        except OSError as error:
            raise _error("portable-methodology-target-invalid", f"cannot inspect directory: {relative.as_posix()}") from error
        if stat.S_ISLNK(observed.st_mode) or not stat.S_ISDIR(observed.st_mode):
            raise _error("portable-methodology-target-invalid", f"directory is unsafe: {relative.as_posix()}")
    return path


def _read(path: Path, *, code: str) -> bytes:
    try:
        before = path.stat()
        payload = path.read_bytes()
        after = path.stat()
    except OSError as error:
        raise _error(code, f"carrier cannot be read: {path.as_posix()}") from error
    if (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns) != (
        after.st_dev,
        after.st_ino,
        after.st_size,
        after.st_mtime_ns,
    ):
        raise _error(code, f"carrier changed while being read: {path.as_posix()}")
    return payload


def _protected_name(name: str) -> bool:
    lowered = name.lower()
    return lowered.startswith(".env") or lowered.endswith(".env")


def _tree_records(root: Path | None) -> tuple[PortableMethodologyFile, ...]:
    if root is None:
        return ()
    records: list[PortableMethodologyFile] = []
    for path in sorted(root.rglob("*"), key=lambda item: item.relative_to(root).as_posix()):
        relative = path.relative_to(root)
        if any(_protected_name(component) for component in relative.parts):
            raise _error("portable-methodology-protected-member", "tree contains a protected member")
        if path.is_symlink():
            raise _error("portable-methodology-symlink", f"tree contains a symlink: {relative.as_posix()}")
        if path.is_dir():
            continue
        if not path.is_file():
            raise _error("portable-methodology-tree-invalid", f"tree contains a non-regular member: {relative.as_posix()}")
        if path.name == ".DS_Store":
            continue
        payload = _read(path, code="portable-methodology-tree-invalid")
        records.append(PortableMethodologyFile(relative.as_posix(), _digest(payload), path.stat().st_mode & 0o777))
    return tuple(records)


def _sealed_export_tree_records(root: Path) -> tuple[PortableMethodologyFile, ...]:
    """Read every physical member for an exporter-inventory ownership check.

    Unlike compiler output, a sealed exporter inventory does not admit a
    ``.DS_Store`` exception.  It must account for the complete delivered tree.
    """

    records: list[PortableMethodologyFile] = []
    for path in sorted(root.rglob("*"), key=lambda item: item.relative_to(root).as_posix()):
        relative = path.relative_to(root)
        if any(_protected_name(component) for component in relative.parts):
            raise _error("portable-methodology-source-export-not-owned", "prior root Methodology export contains a protected member")
        if path.is_symlink():
            raise _error("portable-methodology-symlink", f"prior root Methodology export contains a symlink: {relative.as_posix()}")
        if path.is_dir():
            continue
        if not path.is_file():
            raise _error("portable-methodology-source-export-not-owned", f"prior root Methodology export contains a non-regular member: {relative.as_posix()}")
        payload = _read(path, code="portable-methodology-source-export-not-owned")
        records.append(PortableMethodologyFile(relative.as_posix(), _digest(payload), path.stat().st_mode & 0o777))
    return tuple(records)


def _tree_digest(root: Path | None) -> str:
    return _digest(_canonical_json([record.__dict__ for record in _tree_records(root)]))


def _exporter() -> Any:
    """Load the sealed-export reader, without accepting an export mapping."""

    path = _TOOLS_ROOT / "COMPILE_APPLICABLE_METHODOLOGY" / "methodology_export.py"
    spec = importlib.util.spec_from_file_location("caprmedio_portable_methodology_export", path)
    if spec is None or spec.loader is None:  # pragma: no cover - installation failure
        raise _error("portable-methodology-export-unavailable", "sealed Methodology export reader is unavailable")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _packet_candidate_root(request: PortableInstallationRequest) -> tuple[Path, Any, Any]:
    """Locate the private candidate that the already reopened packet retained.

    The path is intentionally derived only from the retained package layout,
    not from a caller-supplied run id or a current package selector.
    """

    packet = getattr(request, "full_gate_packet", None)
    retained = getattr(packet, "retained_candidate", None)
    package_evidence = getattr(retained, "package_evidence", None)
    view = getattr(package_evidence, "view", None)
    artifact_root = getattr(packet, "artifact_root", None)
    package_root = getattr(view, "package_root", None)
    run_id = getattr(view, "candidate_run_id", None)
    manifest_digest = getattr(view, "actual_package_manifest_sha256", None)
    descriptor_sha = getattr(retained, "candidate_snapshot_manifest_sha256", None)
    if not (
        isinstance(artifact_root, Path)
        and isinstance(package_root, Path)
        and isinstance(run_id, str)
        and run_id
        and isinstance(manifest_digest, str)
        and _is_sha256(manifest_digest)
        and isinstance(descriptor_sha, str)
        and _is_sha256(descriptor_sha)
    ):
        raise _error("portable-methodology-candidate-invalid", "retained Full Gate packet has no complete candidate identity")
    try:
        package_relative = package_root.relative_to(artifact_root)
    except ValueError as error:
        raise _error("portable-methodology-candidate-invalid", "retained package escapes its artifact root") from error
    expected = Path(".caprmedio_tmp") / "release_candidates" / run_id / "package" / manifest_digest
    if package_relative != expected:
        raise _error("portable-methodology-candidate-invalid", "retained package is not in the canonical private candidate layout")
    candidate_root = artifact_root / expected.parent.parent
    if candidate_root.is_symlink() or not candidate_root.is_dir():
        raise _error("portable-methodology-candidate-invalid", "retained private candidate root is unavailable")
    return candidate_root, retained, view


def _read_private_candidate_delivery(
    request: PortableInstallationRequest,
    package: VerifiedFrameworkPackage,
) -> tuple[Path, Path, str, str, str, str, tuple[PortableMethodologyFile, ...], tuple[PortableMethodologyFile, ...], str, str]:
    """Read the existing sealed export and existing compiled delivery only.

    This is a detached analogue of the private compiler reader's *physical*
    manifest checks.  It never creates a ``ValidatedCandidate``, invokes the
    compiler, or regenerates output bytes; the retained Full Gate is already
    the authority for those historic candidate bytes.
    """

    package_compiler, compiler_binding = open_admitted_package_compiler(package)
    candidate_root, retained, view = _packet_candidate_root(request)
    exporter = _exporter()
    try:
        export = exporter.read_sealed_export(release_candidate_root=candidate_root)
    except Exception as error:
        raise _error("portable-methodology-export-invalid", "retained Methodology export is not sealed and valid") from error
    source_root = export.output_root
    if source_root != candidate_root / "methodology":
        raise _error("portable-methodology-export-invalid", "sealed export has an unexpected private root")
    seal_path = candidate_root / exporter.SEAL_NAME
    seal = _regular(candidate_root, Path(exporter.SEAL_NAME), code="portable-methodology-export-invalid")
    try:
        seal_document = json.loads(_read(seal, code="portable-methodology-export-invalid").decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise _error("portable-methodology-export-invalid", "sealed export checksum carrier is unreadable") from error
    export_seal = seal_document.get("sha256") if isinstance(seal_document, Mapping) else None
    if not _is_sha256(export_seal) or seal_path != seal:
        raise _error("portable-methodology-export-invalid", "sealed export checksum carrier is invalid")
    compiled_root = _directory(candidate_root, Path("compiled"))
    assert compiled_root is not None
    manifest_path = _regular(compiled_root, Path("compiled-delivery-manifest.json"), code="portable-methodology-compiled-unsealed")
    raw = _read(manifest_path, code="portable-methodology-compiled-invalid")
    try:
        manifest = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise _error("portable-methodology-compiled-invalid", "private compiled manifest is unreadable") from error
    required = {
        "schema", "candidate_snapshot_manifest_sha256", "frozen_manifest_sha256", "export_inventory_sha256",
        "export_seal_sha256", "source_export_root", "compiler_entrypoint_path", "compiler_entrypoint_sha256",
        "output_rows", "sha256",
    }
    if not isinstance(manifest, Mapping) or set(manifest) != required or raw != _canonical_json(manifest):
        raise _error("portable-methodology-compiled-invalid", "private compiled manifest is not canonical")
    unsigned = dict(manifest)
    checksum = unsigned.pop("sha256", None)
    if not _is_sha256(checksum) or checksum != _digest(_canonical_json(unsigned)):
        raise _error("portable-methodology-compiled-invalid", "private compiled manifest checksum is invalid")
    source_relative = source_root.relative_to(getattr(request.full_gate_packet, "artifact_root"))
    bindings = {
        "schema": "caprmedio.release_version.private_methodology_compilation.v1",
        "candidate_snapshot_manifest_sha256": getattr(retained, "candidate_snapshot_manifest_sha256"),
        "frozen_manifest_sha256": export.frozen_manifest_sha256,
        "export_inventory_sha256": export.inventory_digest,
        "export_seal_sha256": export_seal,
        "source_export_root": source_relative.as_posix(),
    }
    if any(manifest.get(key) != expected for key, expected in bindings.items()):
        raise _error("portable-methodology-compiled-binding-mismatch", "private compiled manifest does not bind the retained sealed export")
    if (
        manifest.get("compiler_entrypoint_path") != compiler_binding.path
        or manifest.get("compiler_entrypoint_sha256") != compiler_binding.sha256
    ):
        raise _error("portable-methodology-compiled-binding-mismatch", "private compiled manifest does not bind the admitted package compiler")
    rows = manifest.get("output_rows")
    if not isinstance(rows, list) or not rows:
        raise _error("portable-methodology-compiled-invalid", "private compiled manifest has no output rows")
    expected: dict[str, str] = {}
    for row in rows:
        if not isinstance(row, Mapping) or set(row) != {"path", "sha256"}:
            raise _error("portable-methodology-compiled-invalid", "private compiled output row is invalid")
        relative = _safe_relative(row.get("path"), label="private compiled output path")
        digest = row.get("sha256")
        if not _is_sha256(digest) or relative.as_posix() in expected:
            raise _error("portable-methodology-compiled-invalid", "private compiled output rows are invalid")
        expected[relative.as_posix()] = digest
    observed = tuple(file for file in _tree_records(compiled_root) if file.path != manifest_path.name)
    if {file.path: file.sha256 for file in observed} != expected:
        raise _error("portable-methodology-compiled-invalid", "private compiled bytes differ from their sealed manifest")
    if any(Path(file.path).parts[0] not in {role for _, role in package_compiler.ROLES} for file in observed):
        raise _error("portable-methodology-compiled-invalid", "private compiled output has an unknown compiler role")
    return (
        source_root,
        compiled_root,
        export.frozen_manifest_sha256,
        export.inventory_digest,
        str(export_seal),
        str(checksum),
        _tree_records(source_root),
        tuple(sorted(observed, key=lambda file: file.path)),
        str(getattr(retained, "candidate_snapshot_manifest_sha256")),
        str(getattr(view, "candidate_run_id")),
    )


def _prepare_candidate_publication(
    request: PortableInstallationRequest,
    *,
    package: VerifiedFrameworkPackage,
    target_context: TargetProjectContext,
    prospective_selector: CurrentPackageSelector,
) -> PreparedCandidateMethodologyPublication:
    target_context = _rebind_target_context(request, target_context)
    try:
        receipt = verify_prospective_portable_full_gate(
            request, package=package, target_context=target_context, selector=prospective_selector,
        )
    except InstallationError as error:
        raise _error("portable-methodology-gate-invalid", "prospective retained Full Gate cannot be reopened") from error
    (
        source_root, compiled_root, frozen, inventory, seal, compiled_manifest,
        source_files, compiled_files, candidate_sha, run_id,
    ) = _read_private_candidate_delivery(request, package)
    return PreparedCandidateMethodologyPublication(
        package_manifest_sha256=package.manifest_digest,
        source_catalog_sha256=package.source_catalog_sha256,
        target_project_context_sha256=target_context.sha256,
        gate_receipt_sha256=receipt,
        candidate_snapshot_manifest_sha256=candidate_sha,
        candidate_run_id=run_id,
        source_export_root=source_root,
        compiled_root=compiled_root,
        frozen_manifest_sha256=frozen,
        export_inventory_sha256=inventory,
        export_seal_sha256=seal,
        compiled_manifest_sha256=compiled_manifest,
        source_files=source_files,
        compiled_files=compiled_files,
    )


def prepare_candidate_portable_methodology_publication(
    request: PortableInstallationRequest,
    *,
    package: VerifiedFrameworkPackage,
    target_context: TargetProjectContext,
    prospective_selector: CurrentPackageSelector,
) -> PreparedCandidateMethodologyPublication:
    """Prepare exact Full-Gate candidate Methodology bytes without publication."""

    return _prepare_candidate_publication(
        request, package=package, target_context=target_context, prospective_selector=prospective_selector,
    )


def reopen_prepared_candidate_portable_methodology_publication(
    request: PortableInstallationRequest,
    value: PreparedCandidateMethodologyPublication,
    *,
    package: VerifiedFrameworkPackage,
    target_context: TargetProjectContext,
    prospective_selector: CurrentPackageSelector,
) -> PreparedCandidateMethodologyPublication:
    """Refuse caller-built/stale prepared facts before a later publication."""

    if not isinstance(value, PreparedCandidateMethodologyPublication):
        raise _error("portable-methodology-prepared-untrusted", "candidate Methodology publication requires a typed prepared fact")
    observed = _prepare_candidate_publication(
        request, package=package, target_context=target_context, prospective_selector=prospective_selector,
    )
    if observed != value:
        raise _error("portable-methodology-prepared-stale", "prepared candidate Methodology bytes differ from retained evidence")
    return observed


def _projection_records(output_root: Path, *, compiler_module: Any = compiler) -> tuple[PortableMethodologyFile, ...]:
    """Inventory only this delivery's role folders, never source authority."""
    records: list[PortableMethodologyFile] = []
    for _, role in compiler_module.ROLES:
        role_root = _directory(output_root, Path(role), missing_ok=True)
        if role_root is None:
            continue
        records.extend(
            PortableMethodologyFile((Path(role) / file.path).as_posix(), file.sha256, file.mode)
            for file in _tree_records(role_root)
        )
    return tuple(sorted(records, key=lambda file: file.path))


def _context_paths_for(
    request: PortableInstallationRequest,
    target_context: TargetProjectContext,
) -> tuple[Path, Path, Path]:
    """Reopen the explicit settings/structure carriers bound by preparation."""
    if not isinstance(request, PortableInstallationRequest) or not isinstance(target_context, TargetProjectContext):
        raise _error("portable-methodology-input-untrusted", "Methodology publication requires typed installation request and context")
    root = _root(request.target.target_root)
    control_name = request.target.control_child
    if not isinstance(control_name, str) or Path(control_name).name != control_name or not control_name.startswith(".caprmedio_"):
        raise _error("portable-methodology-context-invalid", "target control child is unsafe")
    control = _directory(root, Path(control_name))
    assert control is not None
    settings = _regular(root, Path(control_name) / "caprmedio_project_settings.toml", code="portable-methodology-context-invalid")
    structure = _regular(root, Path(control_name) / "project_structure.toml", code="portable-methodology-context-invalid")
    if _digest(_read(settings, code="portable-methodology-context-invalid")) != target_context.settings_sha256:
        raise _error("portable-methodology-context-stale", "project settings differ from the prepared target context")
    structure_bytes = _read(structure, code="portable-methodology-context-invalid")
    if _digest(structure_bytes) != target_context.project_structure_sha256:
        raise _error("portable-methodology-context-stale", "Project Structure differs from the prepared target context")
    try:
        document = tomllib.loads(structure_bytes.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise _error("portable-methodology-context-invalid", "Project Structure is not valid UTF-8 TOML") from error
    units = document.get("scope_units") if isinstance(document, Mapping) else None
    source_units = [unit for unit in units if isinstance(unit, Mapping) and unit.get("scope_unit_name") == "METHODOLOGY_SOURCES"] if isinstance(units, list) else []
    if len(source_units) != 1:
        raise _error("portable-methodology-context-invalid", "Project Structure must declare exactly one METHODOLOGY_SOURCES unit")
    output_units = [unit for unit in units if isinstance(unit, Mapping) and unit.get("scope_unit_name") == "APPLICABLE_METHODOLOGY"] if isinstance(units, list) else []
    if len(output_units) != 1:
        raise _error("portable-methodology-context-invalid", "Project Structure must declare exactly one APPLICABLE_METHODOLOGY unit")
    source_relative = _safe_relative(source_units[0].get("authority_path"), label="METHODOLOGY_SOURCES authority_path")
    delivery_value = output_units[0].get("delivery_path")
    output_relative = (
        _safe_relative(delivery_value, label="APPLICABLE_METHODOLOGY delivery_path")
        if delivery_value is not None
        else Path(control_name) / _DEFAULT_OUTPUT_SUFFIX
    )
    legacy_source_relative = output_relative / _SOURCE_SUFFIX
    if source_relative != legacy_source_relative and (
        source_relative == output_relative
        or source_relative.is_relative_to(output_relative)
        or output_relative.is_relative_to(source_relative)
    ):
        raise _error("portable-methodology-context-invalid", "Methodology source authority and Applicable Methodology delivery must not overlap")
    return root, source_relative, output_relative


def _rebind_target_context(
    request: PortableInstallationRequest,
    target_context: TargetProjectContext,
) -> TargetProjectContext:
    """Physically bind every target carrier before trusting a context tuple.

    ``TargetProjectContext.sha256`` is derived data, not a durable authority.
    Rebinding therefore covers the selected Settings, Project Structure,
    Operators Registry, Framework Settings, package evidence, and the D600v2
    Methodology selection.  If an immutable context carrier already exists,
    it must also reopen exactly; otherwise this remains a pre-publication,
    zero-effect bind.
    """

    if not isinstance(request, PortableInstallationRequest) or not isinstance(target_context, TargetProjectContext):
        raise _error("portable-methodology-input-untrusted", "Methodology publication requires typed installation request and context")
    root = _root(request.target.target_root)
    carrier = root / CONTEXTS_DIRECTORY / f"{target_context.sha256}.toml"
    try:
        if carrier.exists() or carrier.is_symlink():
            rebound = reopen_target_project_context(request.target, expected_sha256=target_context.sha256)
        else:
            rebound = bind_target_project_context(request.target)
    except InstallationContextError as error:
        raise _error("portable-methodology-context-stale", "target controls or package evidence cannot be rebound") from error
    if rebound != target_context:
        raise _error("portable-methodology-context-stale", "target controls or package evidence differ from the supplied context")
    return rebound


def _context_paths(
    request: PortableInstallationRequest,
    preparation: PortableInstallationPreparation,
) -> tuple[Path, Path, Path]:
    if not isinstance(preparation, PortableInstallationPreparation):
        raise _error("portable-methodology-input-untrusted", "Methodology publication requires typed installation preparation")
    return _context_paths_for(request, preparation.target_context)


def _reopen_preparation(
    request: PortableInstallationRequest,
    supplied: PortableInstallationPreparation,
) -> PortableInstallationPreparation:
    """Do not trust a caller-built ready dataclass; reopen the Full Gate boundary."""
    try:
        observed = prepare_portable_installation(request)
    except InstallationError as error:
        raise _error("portable-methodology-preparation-invalid", "portable installation preparation cannot be reopened") from error
    if observed != supplied:
        raise _error("portable-methodology-preparation-stale", "portable installation preparation differs from current gate/package evidence")
    if observed.status != "ready" or observed.blocker is not None:
        raise _error("portable-methodology-gate-blocked", "a same-byte retained Full Gate is required before Methodology publication")
    return observed


def _lock_context(request: PortableInstallationRequest, target_context: TargetProjectContext, lock: InstallationPublicationLock) -> None:
    if not isinstance(lock, InstallationPublicationLock):
        raise _error("portable-methodology-lock-required", "Methodology publication requires the concrete installation publication lock")
    root = _root(request.target.target_root)
    if lock.project_root != root or lock.target_context_sha256 != target_context.sha256:
        raise _error("portable-methodology-lock-mismatch", "installation lock does not bind this target context")
    try:
        lock.revalidate()
    except InstallationTransactionError as error:
        raise _error("portable-methodology-lock-invalid", "installation publication lock is not active and owned") from error


def _lock(request: PortableInstallationRequest, preparation: PortableInstallationPreparation, lock: InstallationPublicationLock) -> None:
    _lock_context(request, preparation.target_context, lock)


def _catalog(package: VerifiedFrameworkPackage) -> tuple[tuple[str, Mapping[str, Any]], ...]:
    try:
        reopened = verify_framework_package(package.root)
        if reopened != package:
            raise _error("portable-methodology-package-stale", "package differs from the prepared package")
        catalog = _regular(package.root, Path(CATALOG_NAME), code="portable-methodology-catalog-missing")
        records = read_source_catalog_records(_read(catalog, code="portable-methodology-catalog-invalid"))
    except FrameworkPackageError as error:
        raise _error("portable-methodology-package-invalid", "package inventory or catalog cannot be reopened") from error
    if _digest(_read(catalog, code="portable-methodology-catalog-invalid")) != package.source_catalog_sha256:
        raise _error("portable-methodology-catalog-stale", "catalog bytes differ from the prepared package")
    return records


def _covered(path: Path, record_path: Path) -> bool:
    return path == record_path or path.is_relative_to(record_path)


def _package_payload(package: VerifiedFrameworkPackage, row: PackageInventoryRow) -> bytes:
    relative = _safe_relative(row.path, label="package inventory path")
    path = _regular(package.root, relative, code="portable-methodology-package-member-missing")
    payload = _read(path, code="portable-methodology-package-member-invalid")
    if _digest(payload) != row.sha256 or (path.stat().st_mode & 0o777) != row.mode:
        raise _error("portable-methodology-package-member-stale", f"package member differs from its manifest: {relative.as_posix()}")
    return payload


def _admitted_engine_payload(
    package: VerifiedFrameworkPackage,
    relative: Path,
    *,
    dependency: bool,
) -> tuple[PackageInventoryRow, bytes]:
    """Read one compiler-closure module only through the package inventory."""

    rows = [row for row in package.inventory if row.path == relative.as_posix()]
    if len(rows) != 1 or rows[0].role != "engine":
        code = "portable-methodology-package-compiler-dependency-missing" if dependency else "portable-methodology-package-compiler-missing"
        raise _error(code, f"package does not admit the canonical compiler carrier: {relative.as_posix()}")
    return rows[0], _package_payload(package, rows[0])


def _package_compiler_modules(
    package: VerifiedFrameworkPackage,
    compiler_payload: bytes,
    compiler_binding: PackageCompilerBinding,
) -> Any:
    """Execute the compiler and its local imports from verified package bytes.

    The compiler predates package loading and imports several modules by their
    ordinary top-level names.  Its retained import hook returns the verified
    package modules for the whole compiler lifetime.  The short-lived
    ``sys.modules`` registration below exists only for Python class creation;
    it is never an ambient dependency source after this function returns.
    """

    payloads: dict[str, tuple[Path, bytes, bool]] = {}
    for name, relative, is_package in _PACKAGE_COMPILER_DEPENDENCIES:
        _row, payload = _admitted_engine_payload(package, relative, dependency=True)
        payloads[name] = (relative, payload, is_package)
    module_prefix = f"caprmedio_admitted_package_{compiler_binding.package_manifest_sha256}_{compiler_binding.sha256}"
    compiler_path = package.root / PACKAGE_COMPILER_RELATIVE
    private_names = {
        "VALIDATE_ATOMS": module_prefix,
        "project_runtime": f"{module_prefix}.project_runtime",
        "VALIDATE_ATOMS.validate_atoms_workers": f"{module_prefix}.validate_atoms_workers",
        "VALIDATE_ATOMS.validate_atoms_workers.read_io": f"{module_prefix}.validate_atoms_workers.read_io",
        "VALIDATE_ATOMS.validate_atoms_workers.settings": f"{module_prefix}.validate_atoms_workers.settings",
        "project_selection": f"{module_prefix}.project_selection",
        "artifact_metadata": f"{module_prefix}.artifact_metadata",
    }
    logical_modules: dict[str, types.ModuleType] = {}

    namespace = types.ModuleType(private_names["VALIDATE_ATOMS"])
    namespace.__file__ = (package.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS").as_posix()
    namespace.__package__ = namespace.__name__
    namespace.__path__ = [namespace.__file__]  # type: ignore[attr-defined]
    logical_modules["VALIDATE_ATOMS"] = namespace
    for name, (relative, _payload, is_package) in payloads.items():
        module = types.ModuleType(private_names[name])
        module.__file__ = (package.root / relative).as_posix()
        module.__package__ = module.__name__ if is_package else module.__name__.rpartition(".")[0]
        if is_package:
            module.__path__ = [str(Path(module.__file__).parent)]  # type: ignore[attr-defined]
        logical_modules[name] = module
    compiler_module = types.ModuleType(f"{module_prefix}.compiler")
    compiler_module.__file__ = compiler_path.as_posix()
    compiler_module.__package__ = module_prefix
    for name, module in logical_modules.items():
        parent, separator, child = name.rpartition(".")
        if separator:
            setattr(logical_modules[parent], child, module)
        elif name != "VALIDATE_ATOMS":
            setattr(namespace, name, module)
    setattr(namespace, "compiler", compiler_module)
    private_modules = {module.__name__: module for module in (*logical_modules.values(), compiler_module)}

    stdlib = frozenset(getattr(sys, "stdlib_module_names", ())).union(sys.builtin_module_names)
    compiler_sys = types.ModuleType(f"{module_prefix}._sys")
    compiler_sys.path = list(sys.path)

    def validate_fromlist(target: Any, values: Any) -> None:
        if not values:
            return
        for child in values:
            if not isinstance(child, str):
                raise _error("portable-methodology-package-compiler-dependency-invalid", "package compiler import member is invalid")
            if child == "*":
                exports = getattr(target, "__all__", ())
                if not isinstance(exports, (tuple, list)) or any(not isinstance(value, str) or not hasattr(target, value) for value in exports):
                    raise _error("portable-methodology-package-compiler-dependency-unadmitted", "package compiler wildcard import is not closed over verified members")
            elif not hasattr(target, child):
                # Do not permit CPython's IMPORT_FROM fallback to inspect an
                # ambient ``sys.modules[target.__name__ + '.' + child]``.
                raise _error("portable-methodology-package-compiler-dependency-unadmitted", "package compiler imports a missing member outside its admitted closure")

    def guarded_import(
        name: str,
        globals_value: Mapping[str, object] | None = None,
        locals_value: Mapping[str, object] | None = None,
        fromlist: tuple[str, ...] = (),
        level: int = 0,
    ) -> Any:
        resolved = name
        if level:
            package_name = globals_value.get("__package__") if globals_value is not None else None
            if not isinstance(package_name, str) or not package_name:
                raise _error("portable-methodology-package-compiler-dependency-invalid", "package compiler uses an invalid relative import")
            try:
                resolved = importlib.util.resolve_name("." * level + name, package_name)
            except (ImportError, TypeError, ValueError) as error:
                raise _error("portable-methodology-package-compiler-dependency-invalid", "package compiler relative import is invalid") from error
            target = private_modules.get(resolved)
            if target is None:
                raise _error("portable-methodology-package-compiler-dependency-unadmitted", "package compiler imports a relative dependency outside its admitted closure")
            validate_fromlist(target, fromlist)
            return target if fromlist else namespace
        target = logical_modules.get(resolved)
        if target is not None:
            validate_fromlist(target, fromlist)
            # Match ``__import__``: an ordinary dotted import yields its root,
            # while ``from ... import`` yields the requested module.
            if fromlist or "." not in resolved:
                return target
            return logical_modules[resolved.split(".", 1)[0]]
        root = resolved.split(".", 1)[0]
        if root not in stdlib:
            raise _error("portable-methodology-package-compiler-dependency-unadmitted", "package compiler imports a non-standard dependency outside its admitted closure")
        if resolved == "sys" and globals_value is not None and globals_value.get("__name__") == compiler_module.__name__:
            return compiler_sys
        target = _trusted_stdlib_module(resolved)
        return target if fromlist else _trusted_stdlib_module(root)

    safe_builtins = dict(vars(builtins))
    safe_builtins["__import__"] = guarded_import
    try:
        # Only private, content-addressed aliases are registered.  Historic
        # names stay untouched, so unrelated threads cannot observe a package
        # compiler's temporary dependency closure.
        sys.modules.update(private_modules)
        for name, (_relative, payload, _is_package) in payloads.items():
            logical_modules[name].__dict__["__builtins__"] = safe_builtins
            exec(compile(payload, logical_modules[name].__file__, "exec"), logical_modules[name].__dict__)
        compiler_module.__dict__["__builtins__"] = safe_builtins
        exec(compile(compiler_payload, compiler_module.__file__, "exec"), compiler_module.__dict__)
        try:
            reopened = verify_framework_package(package.root)
        except FrameworkPackageError as error:
            raise _error("portable-methodology-package-compiler-stale", "package compiler closure changed while loading") from error
        if reopened != package:
            raise _error("portable-methodology-package-compiler-stale", "package compiler closure differs from the prepared package")
        return compiler_module
    except PortableMethodologyInstallationError:
        raise
    except Exception as error:
        raise _error("portable-methodology-package-compiler-invalid", "admitted package compiler cannot be loaded") from error


def open_admitted_package_compiler(package: VerifiedFrameworkPackage) -> tuple[Any, PackageCompilerBinding]:
    """Open only the package-manifest-admitted compiler bytes in memory.

    The dynamically executed module is compiled from bytes read through the
    verified package inventory, never imported from the publisher checkout.
    Its name is content-addressed, so an N+1 package cannot reuse a prior
    module object retained in ``sys.modules``.
    """

    if not isinstance(package, VerifiedFrameworkPackage):
        raise _error("portable-methodology-package-compiler-untrusted", "package compiler requires a verified Framework package")
    try:
        observed = verify_framework_package(package.root)
    except FrameworkPackageError as error:
        raise _error("portable-methodology-package-compiler-invalid", "package compiler package cannot be physically reopened") from error
    if observed != package:
        raise _error("portable-methodology-package-compiler-stale", "package compiler differs from the prepared package identity")
    row, payload = _admitted_engine_payload(observed, PACKAGE_COMPILER_RELATIVE, dependency=False)
    binding = PackageCompilerBinding(observed.manifest_digest, row.path, row.sha256, row.mode)
    with _PACKAGE_COMPILER_IMPORT_LOCK:
        module = _package_compiler_modules(observed, payload, binding)
    if _digest(payload) != binding.sha256:
        raise _error("portable-methodology-package-compiler-stale", "admitted package compiler bytes changed while loading")
    return module, binding


def reopen_admitted_package_compiler(
    package: VerifiedFrameworkPackage,
    binding: PackageCompilerBinding,
) -> tuple[Any, PackageCompilerBinding]:
    """Physically re-open the exact package compiler bound by a receipt."""

    if not isinstance(binding, PackageCompilerBinding):
        raise _error("portable-methodology-package-compiler-untrusted", "package compiler binding must be typed")
    module, observed = open_admitted_package_compiler(package)
    if observed != binding:
        raise _error("portable-methodology-package-compiler-stale", "package compiler no longer matches its bound receipt")
    return module, observed


def _material_descriptor(
    records: tuple[tuple[str, Mapping[str, Any]], ...],
    package_path: Path,
    allowed_kinds: set[str] | frozenset[str],
) -> tuple[str, Mapping[str, Any]]:
    """Resolve one material row against the complete admitted catalog.

    Selection is intentionally a separate decision.  A row covered by no
    descriptor or by two tree descriptors is invalid even when neither (or
    only one) happens to be selected for this installation.
    """

    matches = [
        (identity, record)
        for identity, record in records
        if record.get("kind") in allowed_kinds
        and isinstance(record.get("path"), str)
        and _covered(package_path, _safe_relative(record["path"], label="catalog source path"))
    ]
    if not matches:
        raise _error("portable-methodology-row-unadmitted", "Methodology row is not covered by an admitted source descriptor")
    if len(matches) != 1:
        raise _error("portable-methodology-row-overlap", "Methodology row is covered by multiple admitted source descriptors")
    return matches[0]


def _selected_members(
    package: VerifiedFrameworkPackage,
    records: tuple[tuple[str, Mapping[str, Any]], ...],
    selected_identities: Sequence[str],
    selected_pins: Sequence[object],
) -> tuple[_SourceMember, ...]:
    if not isinstance(selected_identities, tuple) or not selected_identities or any(not isinstance(value, str) or not value for value in selected_identities):
        raise _error("portable-methodology-selection-invalid", "prepared package evidence has no exact selected source identities")
    if len(set(selected_identities)) != len(selected_identities):
        raise _error("portable-methodology-selection-invalid", "prepared package evidence repeats a source identity")
    by_identity = {identity: record for identity, record in records}
    if any(identity not in by_identity for identity in selected_identities):
        raise _error("portable-methodology-selection-invalid", "prepared source identity is absent from the package catalog")
    selected = {identity: by_identity[identity] for identity in selected_identities}
    pins_by_identity: dict[str, object] = {}
    for pin in selected_pins:
        identity = getattr(pin, "identity", None)
        if not isinstance(identity, str) or identity in pins_by_identity:
            raise _error("portable-methodology-selection-invalid", "prepared package evidence has invalid source pins")
        pins_by_identity[identity] = pin
    if set(pins_by_identity) != set(by_identity):
        raise _error("portable-methodology-selection-invalid", "prepared package evidence does not close the package catalog")
    for identity, record in selected.items():
        pin = pins_by_identity.get(identity)
        if pin is None or any(
            getattr(pin, field, None) != record.get(field)
            for field in ("kind", "revision", "sha256", "admission_receipt_sha256")
        ):
            raise _error("portable-methodology-selection-invalid", "selected package source pin differs from the catalog")
    result: list[_SourceMember] = []
    seen_destinations: set[Path] = set()
    seen_identity_rows: set[str] = set()
    material_rows = [row for row in package.inventory if row.role in {"methodology", "methodology-support"}]
    if not material_rows:
        raise _error("portable-methodology-input-incomplete", "package has no Methodology delivery rows")
    for row in material_rows:
        package_path = _safe_relative(row.path, label="package Methodology path")
        if row.role == "methodology":
            if not package_path.is_relative_to(_ACTIVE_ROOT):
                raise _error("portable-methodology-layout-invalid", "Methodology row is outside methodology/active")
            source_relative = package_path.relative_to(_ACTIVE_ROOT)
            allowed_kinds = _COMPILER_KINDS
        else:
            if not package_path.is_relative_to(_SUPPORT_ROOT):
                raise _error("portable-methodology-layout-invalid", "support row is outside methodology/support")
            source_relative = package_path.relative_to(_SUPPORT_ROOT)
            allowed_kinds = {_SUPPORT_KIND}
        if not source_relative.parts:
            raise _error("portable-methodology-layout-invalid", "Methodology row has no source-relative path")
        identity, record = _material_descriptor(records, package_path, allowed_kinds)
        # An admitted package may carry alternatives.  Their presence never
        # activates them: only the target context's exact selection enters the
        # isolated compiler view.
        if identity not in selected:
            continue
        payload = _package_payload(package, row)
        destination = source_relative
        if destination in seen_destinations:
            raise _error("portable-methodology-source-collision", "active/support rows collide after fixed-prefix stripping")
        seen_destinations.add(destination)
        seen_identity_rows.add(identity)
        result.append(
            _SourceMember(
                identity=identity,
                kind=str(record["kind"]),
                package_path=package_path,
                source_relative=source_relative,
                payload=payload,
                sha256=row.sha256,
                mode=row.mode,
            )
        )
    for identity, record in selected.items():
        kind = record.get("kind")
        if kind in _COMPILER_KINDS | {_SUPPORT_KIND} and identity not in seen_identity_rows:
            raise _error("portable-methodology-selected-source-missing", "selected catalog descriptor has no package Methodology member")
    return tuple(sorted(result, key=lambda member: member.source_relative.as_posix()))


def _candidate(member: _SourceMember, *, output_relative: Path, compiler_module: Any = compiler) -> Any:
    if member.kind not in _COMPILER_KINDS:
        raise _error("portable-methodology-support-atom", "support cannot be compiled as an Atom")
    source_path = member.package_path.as_posix()
    if member.source_relative.suffix != ".md":
        raise _error("portable-methodology-source-invalid", "selected Methodology Atom is not Markdown")
    parts = member.source_relative.parts
    layers = {directory: (name, order) for name, directory, order, _ in compiler_module.LAYERS}
    if not parts or parts[0] not in layers:
        raise _error("portable-methodology-source-invalid", "selected Methodology Atom is outside the governed source topology")
    layer, layer_order = layers[parts[0]]
    extension_id: str | None = None
    extension_revision: str | None = None
    if parts[0] == "002_INSTALLED_EXTENSIONS":
        if len(parts) < 5:
            raise _error("portable-methodology-source-invalid", "selected extension Methodology path is invalid")
        extension_id, extension_revision, role_directory = parts[1], parts[2], parts[3]
    else:
        if len(parts) < 3:
            raise _error("portable-methodology-source-invalid", "selected core/configuration Methodology path is invalid")
        role_directory = parts[1]
    role = compiler_module.ROLE_BY_DIRECTORY.get(role_directory)
    if role is None:
        raise _error("portable-methodology-source-invalid", "selected Methodology Atom has no compiler role")
    try:
        frontmatter, _ = compiler_module.split_frontmatter(member.payload, source_path)
        if compiler_module.top_scalar(frontmatter, "status") != "Active":
            raise _error("portable-methodology-source-inactive", "package Methodology Atom is not Active")
        version = compiler_module.top_scalar(frontmatter, "version")
        if version is None or not version.isdecimal() or int(version) < 1:
            raise _error("portable-methodology-source-invalid", "package Methodology Atom has an invalid revision")
        return compiler_module.Candidate(
            layer=layer,
            layer_order=layer_order,
            role=role,
            role_directory=role_directory,
            atom_id=compiler_module.derive_atom_id(member.source_relative, frontmatter),
            version=int(version),
            source_path=source_path,
            source_sha256=member.sha256,
            basename=member.source_relative.name,
            priority=compiler_module.top_scalar(frontmatter, "priority"),
            priority_group=compiler_module.top_scalar(frontmatter, "applicable_methodology_priority_group"),
            replacements=compiler_module.relation_targets(frontmatter, compiler_module.RELATION_KINDS["replacement"]),
            incompatibilities=compiler_module.relation_targets(frontmatter, compiler_module.RELATION_KINDS["incompatible"]),
            definition_term=compiler_module.definition_subject(frontmatter, source_path)[0],
            definition_subject_path=compiler_module.definition_subject(frontmatter, source_path)[1],
            output_relative=output_relative.as_posix(),
            extension_id=extension_id,
            extension_revision=extension_revision,
            original_relations_sha256=compiler_module.relations_digest(frontmatter),
        )
    except compiler_module.CompileError as error:
        raise _error(error.code, error.message) from error


def _validate_support(member: _SourceMember, *, compiler_module: Any = compiler) -> None:
    if member.kind != _SUPPORT_KIND:
        return
    if member.source_relative.suffix != ".md" or not member.payload.startswith(b"---\n"):
        return
    try:
        frontmatter, _ = compiler_module.split_frontmatter(member.payload, member.package_path.as_posix())
    except compiler_module.CompileError:
        return
    if compiler_module.top_scalar(frontmatter, "atom_id") is not None:
        raise _error("portable-methodology-support-atom", "support delivery cannot contain an Atom carrier")


def _selected_candidates(
    members: tuple[_SourceMember, ...],
    *,
    output_relative: Path,
    compiler_module: Any = compiler,
) -> tuple[list[Any], str]:
    candidates: list[Any] = []
    for member in members:
        if member.kind == _SUPPORT_KIND:
            _validate_support(member, compiler_module=compiler_module)
        else:
            candidates.append(_candidate(member, output_relative=output_relative, compiler_module=compiler_module))
    if not candidates:
        raise _error("portable-methodology-frontier-empty", "selected package sources contain no active Methodology Atom")
    candidates.sort(key=compiler_module.candidate_sort_key)
    frontier = compiler_module.frontier_digest(candidates)
    conflicts = compiler_module.detect_conflicts(candidates)
    selected, _approval_results, unresolved = compiler_module.resolve_conflicts(candidates, conflicts, [], frontier)
    if unresolved:
        raise _error("portable-methodology-conflict-unresolved", "selected package Methodology has unresolved compiler conflicts")
    if not selected:
        raise _error("portable-methodology-frontier-empty", "compiler selected no Methodology Atom")
    return selected, frontier


def _target_methodology_identities(target_context: TargetProjectContext) -> tuple[str, ...]:
    """Read the D600v2 selection field without falling back to visibility.

    The field is produced by the target-context binder from the canonical
    Framework Settings carrier and optional target Configuration choice.  A
    legacy context deliberately has no compatible implicit selection.
    """

    raw = getattr(target_context, "methodology_source_identities", None)
    if (
        not isinstance(raw, tuple)
        or not raw
        or any(not isinstance(identity, str) or not identity for identity in raw)
        or len(set(raw)) != len(raw)
    ):
        raise _error(
            "portable-methodology-target-selection-missing",
            "target context has no explicit canonical Methodology source selection",
        )
    return raw


def _target_source_members(members: tuple[_SourceMember, ...]) -> tuple[PreparedTargetMethodologySource, ...]:
    return tuple(
        PreparedTargetMethodologySource(
            identity=member.identity,
            kind=member.kind,
            package_path=member.package_path.as_posix(),
            source_view_path=member.source_relative.as_posix(),
            sha256=member.sha256,
            mode=member.mode,
        )
        for member in members
    )


def _target_source_view_sha256(members: tuple[PreparedTargetMethodologySource, ...]) -> str:
    return _digest(_canonical_json([member.__dict__ for member in members]))


def _prospective_source_relation(
    root: Path,
    output_relative: Path,
    package: VerifiedFrameworkPackage,
    member: _SourceMember,
    candidate: Any,
) -> str:
    """Return the durable installed-package relation embedded in a projection."""

    prospective_package_root = root / ".caprmedio_install" / "releases" / package.manifest_digest
    return Path(
        os.path.relpath(
            prospective_package_root / member.package_path,
            start=(root / output_relative / candidate.role_directory),
        )
    ).as_posix()


def _target_preparation_manifest(
    *,
    package: VerifiedFrameworkPackage,
    target_context: TargetProjectContext,
    receipt: str,
    selected: tuple[str, ...],
    compiler_sha256: str,
    frontier: str,
    source_view: str,
    authoring: str,
    sources: tuple[PreparedTargetMethodologySource, ...],
    files: tuple[PreparedTargetMethodologyFile, ...],
) -> tuple[bytes, str]:
    unsigned = {
        "schema": "caprmedio.portable_target_methodology_preparation.v1",
        "package_manifest_sha256": package.manifest_digest,
        "source_catalog_sha256": package.source_catalog_sha256,
        "target_project_context_sha256": target_context.sha256,
        "gate_receipt_sha256": receipt,
        "selected_source_identities": list(selected),
        "compiler_sha256": compiler_sha256,
        "compiler_frontier_sha256": frontier,
        "source_view_sha256": source_view,
        "authoring_source_sha256": authoring,
        "source_members": [member.__dict__ for member in sources],
        "files": [
            {"path": file.path, "sha256": file.sha256, "mode": file.mode}
            for file in files
        ],
    }
    digest = _digest(_canonical_json(unsigned))
    return _canonical_json({**unsigned, "sha256": digest}) + b"\n", digest


def _prepare_target_methodology_publication(
    request: PortableInstallationRequest,
    *,
    package: VerifiedFrameworkPackage,
    target_context: TargetProjectContext,
    prospective_selector: CurrentPackageSelector,
) -> PreparedTargetMethodologyPublication:
    """Compile one explicit target selection while no destructive effect exists."""

    target_context = _rebind_target_context(request, target_context)
    try:
        receipt = verify_prospective_portable_full_gate(
            request, package=package, target_context=target_context, selector=prospective_selector,
        )
    except InstallationError as error:
        raise _error("portable-methodology-gate-invalid", "prospective retained Full Gate cannot be reopened") from error
    root, source_relative, output_relative = _context_paths_for(request, target_context)
    authoring = _tree_digest(_directory(root, source_relative, missing_ok=True))
    records = _catalog(package)
    selected = _target_methodology_identities(target_context)
    members = _selected_members(package, records, selected, target_context.package_evidence.source_pins)
    sources = _target_source_members(members)
    source_view = _target_source_view_sha256(sources)
    package_compiler, compiler_binding = open_admitted_package_compiler(package)
    candidates, frontier = _selected_candidates(
        members, output_relative=output_relative, compiler_module=package_compiler,
    )
    compiler_sha = compiler_binding.sha256
    by_package_path = {member.package_path.as_posix(): member for member in members}
    rendered: list[PreparedTargetMethodologyFile] = []
    destinations: set[str] = set()
    for candidate in candidates:
        member = by_package_path.get(candidate.source_path)
        if member is None:
            raise _error("portable-methodology-target-invalid", "selected compiler candidate lacks a package source member")
        relative = Path(candidate.role_directory) / candidate.basename
        if relative.as_posix() in destinations:
            raise _error("portable-methodology-source-collision", "selected compiler outputs collide")
        destinations.add(relative.as_posix())
        relation = _prospective_source_relation(root, output_relative, package, member, candidate)
        try:
            payload = package_compiler.projection_bytes(member.payload, relation, candidate)
        except package_compiler.CompileError as error:
            raise _error(error.code, error.message) from error
        rendered.append(PreparedTargetMethodologyFile(relative.as_posix(), _digest(payload), 0o644, payload))
    files = tuple(sorted(rendered, key=lambda file: file.path))
    manifest, manifest_sha = _target_preparation_manifest(
        package=package,
        target_context=target_context,
        receipt=receipt,
        selected=selected,
        compiler_sha256=compiler_sha,
        frontier=frontier,
        source_view=source_view,
        authoring=authoring,
        sources=sources,
        files=files,
    )
    return PreparedTargetMethodologyPublication(
        package_manifest_sha256=package.manifest_digest,
        source_catalog_sha256=package.source_catalog_sha256,
        target_project_context_sha256=target_context.sha256,
        gate_receipt_sha256=receipt,
        selected_source_identities=selected,
        compiler_sha256=compiler_sha,
        compiler_frontier_sha256=frontier,
        source_view_sha256=source_view,
        authoring_source_sha256=authoring,
        source_members=sources,
        files=files,
        manifest_bytes=manifest,
        manifest_sha256=manifest_sha,
    )


def prepare_target_portable_methodology_publication(
    request: PortableInstallationRequest,
    *,
    package: VerifiedFrameworkPackage,
    target_context: TargetProjectContext,
    prospective_selector: CurrentPackageSelector,
) -> PreparedTargetMethodologyPublication:
    """Prepare direct O200 target Methodology bytes before installation effects."""

    return _prepare_target_methodology_publication(
        request, package=package, target_context=target_context, prospective_selector=prospective_selector,
    )


def reopen_prepared_target_portable_methodology_publication(
    request: PortableInstallationRequest,
    value: PreparedTargetMethodologyPublication,
    *,
    package: VerifiedFrameworkPackage,
    target_context: TargetProjectContext,
    prospective_selector: CurrentPackageSelector,
) -> PreparedTargetMethodologyPublication:
    """Recompute the pre-delete target compilation and require exact equality.

    Callers use this boundary while the predecessor remains intact.  It is the
    only direct-target revalidation that invokes the compiler; later staging
    consumes the already compared immutable byte payloads.
    """

    if not isinstance(value, PreparedTargetMethodologyPublication):
        raise _error("portable-methodology-target-prepared-untrusted", "direct target publication requires a typed prepared fact")
    observed = _prepare_target_methodology_publication(
        request,
        package=package,
        target_context=target_context,
        prospective_selector=prospective_selector,
    )
    if observed != value:
        raise _error("portable-methodology-target-prepared-stale", "prepared direct target inputs differ from current verified carriers")
    return observed


def _validate_prepared_target_bytes(
    request: PortableInstallationRequest,
    value: PreparedTargetMethodologyPublication,
    *,
    package: VerifiedFrameworkPackage,
    target_context: TargetProjectContext,
    prospective_selector: CurrentPackageSelector,
) -> PreparedTargetMethodologyPublication:
    """Reopen byte bindings after pre-delete rendering, without compiling."""

    if not isinstance(value, PreparedTargetMethodologyPublication):
        raise _error("portable-methodology-target-prepared-untrusted", "direct target publication requires a typed prepared fact")
    target_context = _rebind_target_context(request, target_context)
    try:
        receipt = verify_prospective_portable_full_gate(
            request, package=package, target_context=target_context, selector=prospective_selector,
        )
    except InstallationError as error:
        raise _error("portable-methodology-gate-invalid", "prospective retained Full Gate cannot be reopened") from error
    root, source_relative, output_relative = _context_paths_for(request, target_context)
    records = _catalog(package)
    selected = _target_methodology_identities(target_context)
    members = _selected_members(package, records, selected, target_context.package_evidence.source_pins)
    sources = _target_source_members(members)
    authoring = _tree_digest(_directory(root, source_relative, missing_ok=True))
    package_compiler, compiler_binding = open_admitted_package_compiler(package)
    compiler_sha = compiler_binding.sha256
    # This is an inverse check after the pre-delete compilation boundary.  It
    # parses each package source only to reconstruct the canonical metadata
    # insertion; it must not perform conflict detection or select a new
    # frontier after publication has begun.
    candidates: list[Any] = []
    for member in members:
        if member.kind == _SUPPORT_KIND:
            _validate_support(member, compiler_module=package_compiler)
        else:
            candidates.append(_candidate(member, output_relative=output_relative, compiler_module=package_compiler))
    if not candidates:
        raise _error("portable-methodology-target-prepared-stale", "prepared direct target has no compiler candidates")
    candidates.sort(key=package_compiler.candidate_sort_key)
    observed_frontier = package_compiler.frontier_digest(candidates)
    by_package_path = {member.package_path.as_posix(): member for member in members}
    by_output_path = {file.path: file for file in value.files}
    if len(by_output_path) != len(value.files) or len(by_output_path) != len(candidates):
        raise _error("portable-methodology-target-prepared-stale", "prepared direct target projection does not have one file per selected candidate")
    for candidate in candidates:
        member = by_package_path.get(candidate.source_path)
        output_path = (Path(candidate.role_directory) / candidate.basename).as_posix()
        file = by_output_path.get(output_path)
        if member is None or file is None:
            raise _error("portable-methodology-target-prepared-stale", "prepared direct target projection no longer matches its selected frontier")
        relation = _prospective_source_relation(root, output_relative, package, member, candidate)
        try:
            package_compiler.validate_projection_source_preservation(member.payload, file.payload, relation, candidate)
        except package_compiler.CompileError as error:
            raise _error(error.code, error.message) from error
    manifest, digest = _target_preparation_manifest(
        package=package,
        target_context=target_context,
        receipt=receipt,
        selected=selected,
        compiler_sha256=value.compiler_sha256,
        frontier=value.compiler_frontier_sha256,
        source_view=value.source_view_sha256,
        authoring=value.authoring_source_sha256,
        sources=value.source_members,
        files=value.files,
    )
    if (
        value.package_manifest_sha256 != package.manifest_digest
        or value.source_catalog_sha256 != package.source_catalog_sha256
        or value.target_project_context_sha256 != target_context.sha256
        or value.gate_receipt_sha256 != receipt
        or value.selected_source_identities != selected
        or value.compiler_sha256 != compiler_sha
        or value.compiler_frontier_sha256 != observed_frontier
        or value.source_members != sources
        or value.source_view_sha256 != _target_source_view_sha256(sources)
        or value.authoring_source_sha256 != authoring
        or any(_digest(file.payload) != file.sha256 or file.mode != 0o644 for file in value.files)
        or value.manifest_bytes != manifest
        or value.manifest_sha256 != digest
    ):
        raise _error("portable-methodology-target-prepared-stale", "prepared direct target bytes differ from verified carriers")
    return value


def _mkdir_safe(root: Path, relative: Path) -> Path:
    cursor = root
    for component in relative.parts:
        cursor = cursor / component
        try:
            cursor.mkdir(mode=0o700)
        except FileExistsError:
            pass
        try:
            observed = cursor.lstat()
        except OSError as error:
            raise _error("portable-methodology-stage-invalid", "staging directory cannot be reopened") from error
        if stat.S_ISLNK(observed.st_mode) or not stat.S_ISDIR(observed.st_mode):
            raise _error("portable-methodology-stage-invalid", "staging directory is unsafe")
    return cursor


def _write_new(path: Path, payload: bytes, mode: int) -> None:
    if path.exists() or path.is_symlink():
        raise _error("portable-methodology-stage-collision", f"staged carrier already exists: {path.name}")
    descriptor = None
    try:
        descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, mode)
        os.fchmod(descriptor, mode)
        offset = 0
        while offset < len(payload):
            written = os.write(descriptor, payload[offset:])
            if written <= 0:
                raise OSError("short write")
            offset += written
        os.fsync(descriptor)
    except OSError as error:
        raise _error("portable-methodology-stage-write-failed", f"cannot write staged carrier: {path.as_posix()}") from error
    finally:
        if descriptor is not None:
            os.close(descriptor)
    observed = _regular(path.parent, Path(path.name), code="portable-methodology-stage-write-failed")
    if _read(observed, code="portable-methodology-stage-write-failed") != payload or (observed.stat().st_mode & 0o777) != mode:
        raise _error("portable-methodology-stage-write-failed", "staged carrier bytes or mode differ")


def _stage(
    root: Path,
    lock: InstallationPublicationLock,
    output_relative: Path,
    package: VerifiedFrameworkPackage,
    members: tuple[_SourceMember, ...],
    candidates: Sequence[Any],
    frontier: str,
    authoring_digest: str,
    context_sha256: str,
    *,
    compiler_module: Any | None = None,
    compiler_sha256: str | None = None,
) -> tuple[Path, tuple[PortableMethodologyFile, ...], str, str]:
    """Stage one compiler projection using an explicitly bound implementation.

    The legacy materializer remains a supported public API, but it must not
    render a package-admitted selection through the publisher checkout.  The
    optional defaults retain compatibility for older internal proof fixtures;
    package-backed callers pass both the admitted module and its inventory
    digest explicitly.
    """

    compiler_module = compiler if compiler_module is None else compiler_module
    if compiler_sha256 is None:
        compiler_path = getattr(compiler_module, "__file__", None)
        if not isinstance(compiler_path, str):
            raise _error("portable-methodology-stage-invalid", "compiler module has no source carrier")
        try:
            compiler_sha256 = _digest(Path(compiler_path).read_bytes())
        except OSError as error:
            raise _error("portable-methodology-stage-invalid", "compiler source carrier cannot be read") from error
    if not _is_sha256(compiler_sha256):
        raise _error("portable-methodology-stage-invalid", "compiler source digest is invalid")
    stage_parent = _mkdir_safe(root, _STAGE_ROOT / lock.lock_generation)
    try:
        stage = Path(tempfile.mkdtemp(prefix="methodology-", dir=stage_parent))
    except OSError as error:
        raise _error("portable-methodology-stage-write-failed", "cannot create Methodology staging root") from error
    source_view = _mkdir_safe(stage, Path("source"))
    output = _mkdir_safe(stage, Path("output"))
    for _, role in compiler_module.ROLES:
        _mkdir_safe(output, Path(role))
    for member in members:
        destination = source_view / member.source_relative
        _mkdir_safe(source_view, member.source_relative.parent)
        _write_new(destination, member.payload, member.mode)
    source_view_digest = _tree_digest(source_view)
    rendered: list[PortableMethodologyFile] = []
    by_package_path = {member.package_path.as_posix(): member for member in members}
    for candidate in candidates:
        member = by_package_path.get(candidate.source_path)
        if member is None:
            raise _error("portable-methodology-stage-invalid", "selected compiler candidate lacks its package member")
        role = Path(candidate.role_directory)
        role_root = _mkdir_safe(output, role)
        target = role_root / candidate.basename
        source_view_file = _regular(source_view, member.source_relative, code="portable-methodology-stage-invalid")
        if _digest(_read(source_view_file, code="portable-methodology-stage-invalid")) != member.sha256:
            raise _error("portable-methodology-stage-invalid", "staged source view differs from package source")
        relation = Path(os.path.relpath(package.root / member.package_path, start=(root / output_relative / role))).as_posix()
        try:
            projected = compiler_module.projection_bytes(
                _read(source_view_file, code="portable-methodology-stage-invalid"), relation, candidate,
            )
        except compiler_module.CompileError as error:
            raise _error(error.code, error.message) from error
        _write_new(target, projected, 0o644)
        rendered.append(PortableMethodologyFile((role / candidate.basename).as_posix(), _digest(projected), 0o644))
    files = tuple(sorted(rendered, key=lambda file: file.path))
    output_digest = _tree_digest(output)
    manifest_unsigned: dict[str, object] = {
        "schema": _MANIFEST_SCHEMA,
        "package_manifest_sha256": package.manifest_digest,
        "source_catalog_sha256": package.source_catalog_sha256,
        "target_project_context_sha256": context_sha256,
        "compiler_sha256": compiler_sha256,
        "compiler_frontier_sha256": frontier,
        "source_view_sha256": source_view_digest,
        "authoring_source_sha256": authoring_digest,
        "output_tree_sha256": output_digest,
        "source_members": [
            {
                "identity": member.identity,
                "kind": member.kind,
                "package_path": member.package_path.as_posix(),
                "source_view_path": member.source_relative.as_posix(),
                "sha256": member.sha256,
                "mode": member.mode,
            }
            for member in members
        ],
        "files": [file.__dict__ for file in files],
    }
    manifest = {**manifest_unsigned, "sha256": _digest(_canonical_json(manifest_unsigned))}
    manifest_payload = _canonical_json(manifest) + b"\n"
    _write_new(output / _MANIFEST_NAME, manifest_payload, 0o644)
    return stage, files, source_view_digest, str(manifest["sha256"])


def _stage_gated_compilation(
    root: Path,
    lock: InstallationPublicationLock,
    output_relative: Path,
    prepared: PreparedCandidateMethodologyPublication,
    *,
    compiler_module: Any = compiler,
) -> tuple[Path, tuple[PortableMethodologyFile, ...], str]:
    """Copy only the historic Full-Gate projection; never call the compiler."""

    stage_parent = _mkdir_safe(root, _STAGE_ROOT / lock.lock_generation)
    try:
        stage = Path(tempfile.mkdtemp(prefix="methodology-gated-", dir=stage_parent))
    except OSError as error:
        raise _error("portable-methodology-stage-write-failed", "cannot create gated Methodology staging root") from error
    source_export = _mkdir_safe(stage, Path("source-export"))
    output = _mkdir_safe(stage, Path("output"))
    for _, role in compiler_module.ROLES:
        _mkdir_safe(output, Path(role))
    for file in prepared.source_files:
        relative = _safe_relative(file.path, label="gated source export path")
        source = _regular(prepared.source_export_root, relative, code="portable-methodology-export-invalid")
        payload = _read(source, code="portable-methodology-export-invalid")
        if _digest(payload) != file.sha256 or (source.stat().st_mode & 0o777) != file.mode:
            raise _error("portable-methodology-export-invalid", "gated source export member differs from its prepared inventory")
        target = source_export / relative
        _mkdir_safe(source_export, relative.parent)
        _write_new(target, payload, file.mode)
    if _tree_records(source_export) != tuple(sorted(prepared.source_files, key=lambda file: file.path)):
        raise _error("portable-methodology-stage-invalid", "staged source export differs from retained inventory")
    for file in prepared.compiled_files:
        relative = _safe_relative(file.path, label="gated compiled path")
        source = _regular(prepared.compiled_root, relative, code="portable-methodology-compiled-invalid")
        payload = _read(source, code="portable-methodology-compiled-invalid")
        if _digest(payload) != file.sha256 or (source.stat().st_mode & 0o777) != file.mode:
            raise _error("portable-methodology-compiled-invalid", "gated compiled member differs from its prepared inventory")
        target = output / relative
        _mkdir_safe(output, relative.parent)
        _write_new(target, payload, file.mode)
    output_digest = _tree_digest(output)
    unsigned: dict[str, object] = {
        "schema": _MANIFEST_SCHEMA,
        "package_manifest_sha256": prepared.package_manifest_sha256,
        "source_catalog_sha256": prepared.source_catalog_sha256,
        "target_project_context_sha256": prepared.target_project_context_sha256,
        "candidate_snapshot_manifest_sha256": prepared.candidate_snapshot_manifest_sha256,
        "candidate_run_id": prepared.candidate_run_id,
        "gate_receipt_sha256": prepared.gate_receipt_sha256,
        "frozen_manifest_sha256": prepared.frozen_manifest_sha256,
        "export_inventory_sha256": prepared.export_inventory_sha256,
        "export_seal_sha256": prepared.export_seal_sha256,
        "compiled_manifest_sha256": prepared.compiled_manifest_sha256,
        "source_export_sha256": _digest(_canonical_json([file.__dict__ for file in prepared.source_files])),
        "output_tree_sha256": output_digest,
        "files": [file.__dict__ for file in prepared.compiled_files],
    }
    manifest = {**unsigned, "sha256": _digest(_canonical_json(unsigned))}
    _write_new(output / _MANIFEST_NAME, _canonical_json(manifest) + b"\n", 0o644)
    return stage, prepared.compiled_files, str(manifest["sha256"])


def _stage_prepared_target_compilation(
    root: Path,
    lock: InstallationPublicationLock,
    prepared: PreparedTargetMethodologyPublication,
    *,
    compiler_module: Any = compiler,
) -> tuple[Path, tuple[PortableMethodologyFile, ...], str]:
    """Stage already rendered direct-target bytes; this function never compiles."""

    stage_parent = _mkdir_safe(root, _STAGE_ROOT / lock.lock_generation)
    try:
        stage = Path(tempfile.mkdtemp(prefix="methodology-target-", dir=stage_parent))
    except OSError as error:
        raise _error("portable-methodology-stage-write-failed", "cannot create target Methodology staging root") from error
    output = _mkdir_safe(stage, Path("output"))
    for _, role in compiler_module.ROLES:
        _mkdir_safe(output, Path(role))
    files: list[PortableMethodologyFile] = []
    for file in prepared.files:
        relative = _safe_relative(file.path, label="prepared target compiler path")
        if relative.parts[0] not in {role for _, role in compiler_module.ROLES}:
            raise _error("portable-methodology-target-prepared-invalid", "prepared target output has an unknown compiler role")
        if _digest(file.payload) != file.sha256 or file.mode != 0o644:
            raise _error("portable-methodology-target-prepared-invalid", "prepared target output bytes or mode are invalid")
        target = output / relative
        _mkdir_safe(output, relative.parent)
        _write_new(target, file.payload, file.mode)
        files.append(PortableMethodologyFile(file.path, file.sha256, file.mode))
    ordered = tuple(sorted(files, key=lambda file: file.path))
    if _tree_records(output) != ordered:
        raise _error("portable-methodology-stage-invalid", "staged target projection differs from prepared output")
    unsigned: dict[str, object] = {
        "schema": _MANIFEST_SCHEMA,
        "package_manifest_sha256": prepared.package_manifest_sha256,
        "source_catalog_sha256": prepared.source_catalog_sha256,
        "target_project_context_sha256": prepared.target_project_context_sha256,
        "gate_receipt_sha256": prepared.gate_receipt_sha256,
        "target_preparation_sha256": prepared.manifest_sha256,
        "compiler_sha256": prepared.compiler_sha256,
        "compiler_frontier_sha256": prepared.compiler_frontier_sha256,
        "source_view_sha256": prepared.source_view_sha256,
        "authoring_source_sha256": prepared.authoring_source_sha256,
        "source_members": [member.__dict__ for member in prepared.source_members],
        "output_tree_sha256": _tree_digest(output),
        "files": [file.__dict__ for file in ordered],
    }
    manifest = {**unsigned, "sha256": _digest(_canonical_json(unsigned))}
    _write_new(output / _MANIFEST_NAME, _canonical_json(manifest) + b"\n", 0o644)
    return stage, ordered, str(manifest["sha256"])


def _source_export_root(root: Path) -> Path:
    """Return the one O169 root delivery location, without touching authority."""

    return root / "methodology"


def _prior_source_export_inventory(root: Path) -> tuple[PortableMethodologyFile, ...]:
    """Validate the actual prior exporter inventory as a replacement proof.

    This intentionally delegates row/frozen-manifest invariants to the
    canonical exporter module.  A self-digested arbitrary JSON inventory is
    not ownership evidence for deleting a retained root delivery.
    """

    inventory = _regular(root, Path("methodology-export-inventory.json"), code="portable-methodology-source-export-not-owned")
    raw = _read(inventory, code="portable-methodology-source-export-not-owned")
    try:
        document = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise _error("portable-methodology-source-export-not-owned", "prior root Methodology inventory is unreadable") from error
    required = {
        "atoms", "atom_count", "catalog_pins", "catalog_pin_count", "frozen_manifest", "frozen_manifest_sha256",
        "inventory_sha256", "logical_delivery_root", "schema", "support", "support_count",
    }
    if (
        not isinstance(document, Mapping)
        or set(document) != required
        or document.get("schema") != "caprmedio.methodology_export.v2"
        or document.get("logical_delivery_root") != "methodology"
        or raw != _canonical_json(document) + b"\n"
    ):
        raise _error("portable-methodology-source-export-not-owned", "prior root Methodology inventory is not canonical")
    unsigned = dict(document)
    digest = unsigned.pop("inventory_sha256", None)
    if not _is_sha256(digest) or digest != _digest(_canonical_json(unsigned)):
        raise _error("portable-methodology-source-export-not-owned", "prior root Methodology inventory checksum is invalid")
    exporter = _exporter()
    try:
        frozen = document["frozen_manifest"]
        frozen_sha = document["frozen_manifest_sha256"]
        if not isinstance(frozen, Mapping) or not _is_sha256(frozen_sha):
            raise ValueError("frozen manifest is absent")
        # ``frozen_manifest_bytes`` is the exporter-owned checksum renderer.
        exporter.frozen_manifest_bytes(frozen)
        frozen_required = {
            "active_frontier", "active_frontier_sha256", "catalog_pins", "schema", "selected_atoms",
            "sha256", "source_root", "source_tree_sha256", "support_inventory",
        }
        frozen_schema = frozen.get("schema")
        legacy_schema = exporter.LEGACY_FROZEN_SCHEMA
        current_schema = exporter.FROZEN_SCHEMA
        if frozen_schema == legacy_schema:
            expected_frozen_fields = frozen_required
        elif frozen_schema == current_schema:
            expected_frozen_fields = frozen_required | {"project_binding"}
        else:
            raise ValueError("frozen manifest schema is unsupported")
        frozen_root = frozen.get("source_root")
        frozen_tree = frozen.get("source_tree_sha256")
        if (
            set(frozen) != expected_frozen_fields
            or frozen.get("sha256") != frozen_sha
            or not isinstance(frozen_root, str)
            or _safe_absolute(frozen_root) is None
            or not _is_sha256(frozen_tree)
        ):
            raise ValueError("frozen manifest fields differ")
        if frozen_schema == current_schema:
            binding = frozen["project_binding"]
            binding_fields = {
                "project_root", "control_root", "source_root", "project_settings_path", "project_settings_sha256",
                "project_structure_path", "project_structure_sha256", "instance_settings_path", "instance_settings_sha256",
            }
            if not isinstance(binding, Mapping) or set(binding) != binding_fields:
                raise ValueError("frozen Project binding is invalid")
            project_root = _safe_absolute(binding["project_root"])
            source_root = _safe_absolute(binding["source_root"])
            paths = tuple(_safe_absolute(binding[field]) for field in (
                "control_root", "project_settings_path", "project_structure_path", "instance_settings_path",
            ))
            if (
                project_root is None
                or source_root is None
                or source_root != _safe_absolute(frozen_root)
                or any(path is None or not path.is_relative_to(project_root) for path in (source_root, *paths))
                or not all(_is_sha256(binding[field]) for field in (
                    "project_settings_sha256", "project_structure_sha256",
                ))
                or (binding["instance_settings_sha256"] is not None and not _is_sha256(binding["instance_settings_sha256"]))
            ):
                raise ValueError("frozen Project binding is unsafe")
        active = exporter._atom_records(frozen["active_frontier"], "active_frontier")
        selected = exporter._atom_records(frozen["selected_atoms"], "selected_atoms")
        supports = exporter._pins(frozen["support_inventory"], "support_inventory")
        catalogs = exporter._pins(frozen["catalog_pins"], "catalog_pins")
        if frozen.get("active_frontier_sha256") != exporter._frontier_digest(active) or not set(selected).issubset(set(active)):
            raise ValueError("frozen frontier differs")
        inventory_atoms = document["atoms"]
        if not isinstance(inventory_atoms, list):
            raise ValueError("inventory atoms are invalid")
        atom_rows: list[dict[str, object]] = []
        for row in inventory_atoms:
            if (
                not isinstance(row, Mapping)
                or set(row) != {"atom_id", "destination_path", "digest", "sha256", "source_path", "version"}
                or row.get("destination_path") != row.get("source_path")
                or row.get("digest") != row.get("sha256")
            ):
                raise ValueError("inventory atom row is invalid")
            atom_rows.append({key: row[key] for key in ("atom_id", "sha256", "source_path", "version")})
        atoms = exporter._atom_records(atom_rows, "inventory.atoms")
        inventory_supports = exporter._pins(document["support"], "inventory.support")
        inventory_catalogs = exporter._pins(document["catalog_pins"], "inventory.catalog_pins")
        if (
            type(document.get("atom_count")) is not int
            or type(document.get("support_count")) is not int
            or type(document.get("catalog_pin_count")) is not int
            or document["atom_count"] != len(atoms)
            or document["support_count"] != len(inventory_supports)
            or document["catalog_pin_count"] != len(inventory_catalogs)
            or atoms != selected
            or inventory_supports != supports
            or inventory_catalogs != catalogs
        ):
            raise ValueError("inventory does not match frozen delivery")
    except Exception as error:
        raise _error("portable-methodology-source-export-not-owned", "prior root Methodology inventory fails canonical exporter validation") from error
    paths = {"methodology-export-inventory.json"}
    for relative, row_digest in (
        *((atom.source_path, atom.sha256) for atom in atoms),
        *((pin.path, pin.sha256) for pin in inventory_supports),
    ):
        path = _safe_relative(relative, label="prior root Methodology source path")
        if path.as_posix() in paths:
            raise _error("portable-methodology-source-export-not-owned", "prior root Methodology inventory repeats a member")
        carrier = _regular(root, path, code="portable-methodology-source-export-not-owned")
        if _digest(_read(carrier, code="portable-methodology-source-export-not-owned")) != row_digest:
            raise _error("portable-methodology-source-export-not-owned", "prior root Methodology source differs from its inventory")
        paths.add(path.as_posix())
    actual = _sealed_export_tree_records(root)
    if {file.path for file in actual} != paths:
        raise _error("portable-methodology-source-export-not-owned", "prior root Methodology inventory does not own every file")
    return actual


def _existing_source_export_owned(root: Path, expected: tuple[PortableMethodologyFile, ...]) -> tuple[PortableMethodologyFile, ...] | None:
    """Return an exact or inventory-owned prior export; refuse foreign roots."""

    if not root.exists() and not root.is_symlink():
        return None
    if root.is_symlink() or not root.is_dir():
        raise _error("portable-methodology-source-export-not-owned", "root Methodology delivery is unsafe")
    actual = _tree_records(root)
    if actual == tuple(sorted(expected, key=lambda file: file.path)):
        return actual
    return _prior_source_export_inventory(root)


def _publish_source_export(
    stage: Path,
    root: Path,
    expected: tuple[PortableMethodologyFile, ...],
) -> Path:
    """Publish the captured O169 source export without re-exporting it.

    A pre-existing root is accepted only when it already has the exact same
    inventory; a differently shaped tree has no portable-delivery ownership
    proof and is deliberately left untouched.
    """

    staged = _directory(stage, Path("source-export"))
    assert staged is not None
    target = _source_export_root(root)
    prior = _existing_source_export_owned(target, expected)
    if prior == tuple(sorted(expected, key=lambda file: file.path)):
        return target
    # ``target`` did not exist above.  Every new file is created atomically
    # and all bytes/modes are reopened below before this call returns.
    target = _mkdir_safe(root, Path("methodology"))
    for file in expected:
        relative = _safe_relative(file.path, label="staged source export path")
        payload_path = _regular(staged, relative, code="portable-methodology-stage-invalid")
        payload = _read(payload_path, code="portable-methodology-stage-invalid")
        if _digest(payload) != file.sha256 or (payload_path.stat().st_mode & 0o777) != file.mode:
            raise _error("portable-methodology-stage-invalid", "staged source export differs from its inventory")
        destination = target / relative
        _mkdir_safe(target, relative.parent)
        if destination.exists() or destination.is_symlink():
            _replace_regular(destination, payload, file.mode)
        else:
            _write_new(destination, payload, file.mode)
    if prior is not None:
        expected_paths = {file.path for file in expected}
        for file in prior:
            if file.path in expected_paths:
                continue
            _regular(target, _safe_relative(file.path, label="prior root Methodology source path"), code="portable-methodology-source-export-not-owned").unlink()
    if _tree_records(target) != tuple(sorted(expected, key=lambda file: file.path)):
        raise _error("portable-methodology-source-export-invalid", "published root Methodology export differs from retained inventory")
    return target


def _existing_output_owned(output: Path, *, compiler_module: Any = compiler) -> None:
    try:
        compiler_module.validate_existing_output_ownership(output)
    except compiler_module.CompileError as error:
        raise _error(error.code, error.message) from error
    manifest = output / _MANIFEST_NAME
    if manifest.exists() or manifest.is_symlink():
        carrier = _regular(output, Path(_MANIFEST_NAME), code="portable-methodology-output-not-owned")
        payload = _read(carrier, code="portable-methodology-output-not-owned")
        try:
            document = json.loads(payload.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise _error("portable-methodology-output-not-owned", "existing delivery manifest is not canonical") from error
        if not isinstance(document, Mapping) or document.get("schema") != _MANIFEST_SCHEMA:
            raise _error("portable-methodology-output-not-owned", "existing delivery manifest is not compiler-owned")
        unsigned = dict(document)
        digest = unsigned.pop("sha256", None)
        if (
            not _is_sha256(digest)
            or digest != _digest(_canonical_json(unsigned))
            or payload != _canonical_json(document) + b"\n"
        ):
            raise _error("portable-methodology-output-not-owned", "existing delivery manifest is not canonical")


def _verify_staged(stage: Path, files: tuple[PortableMethodologyFile, ...], manifest_digest: str) -> bytes:
    output = _directory(stage, Path("output"))
    assert output is not None
    actual = _tree_records(output)
    expected = tuple(sorted(files, key=lambda file: file.path))
    actual_without_manifest = tuple(file for file in actual if file.path != _MANIFEST_NAME)
    if actual_without_manifest != expected:
        raise _error("portable-methodology-stage-invalid", "staged projection tree differs from its expected rows")
    manifest = _regular(output, Path(_MANIFEST_NAME), code="portable-methodology-stage-invalid")
    payload = _read(manifest, code="portable-methodology-stage-invalid")
    try:
        document = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise _error("portable-methodology-stage-invalid", "staged delivery manifest is invalid") from error
    if not isinstance(document, Mapping) or document.get("sha256") != manifest_digest or payload != _canonical_json(document) + b"\n":
        raise _error("portable-methodology-stage-invalid", "staged delivery manifest differs")
    unsigned = dict(document)
    digest = unsigned.pop("sha256", None)
    if digest != _digest(_canonical_json(unsigned)):
        raise _error("portable-methodology-stage-invalid", "staged delivery manifest checksum differs")
    return payload


def _role_payloads(role_root: Path) -> dict[Path, tuple[bytes, int]]:
    """Read already-validated compiler-owned carriers for a reversible replace."""
    result: dict[Path, tuple[bytes, int]] = {}
    for path in sorted(role_root.rglob("*"), key=lambda item: item.relative_to(role_root).as_posix()):
        if path.is_dir():
            continue
        if path.name == ".DS_Store":
            continue
        relative = path.relative_to(role_root)
        result[relative] = (_read(path, code="portable-methodology-output-not-owned"), path.stat().st_mode & 0o777)
    return result


def _replace_regular(path: Path, payload: bytes, mode: int) -> None:
    """Atomically replace a single checked compiler carrier in its real parent."""
    parent = _directory(path.parent.parent, Path(path.parent.name))
    assert parent == path.parent
    temporary = path.parent / f".{path.name}.next"
    _write_new(temporary, payload, mode)
    try:
        os.replace(temporary, path)
    except OSError as error:
        try:
            temporary.unlink(missing_ok=True)
        except OSError:
            pass
        raise _error("portable-methodology-publication-failed", "cannot replace a compiler-owned carrier") from error


def _publish(
    stage: Path,
    root: Path,
    output_relative: Path,
    manifest_payload: bytes,
    *,
    compiler_module: Any = compiler,
) -> None:
    """Replace only verified compiler-owned files; never replace enclosing trees.

    Directory replacement is deliberately avoided: the target's enclosing
    Framework directory is not this delivery's property, and per-file atomic
    replacement remains available on filesystems which reject directory rename
    across protected Project surfaces.
    """
    staged_output = _directory(stage, Path("output"))
    assert staged_output is not None
    output_root = _mkdir_safe(root, output_relative)
    _existing_output_owned(output_root, compiler_module=compiler_module)
    prior: dict[Path, tuple[bytes, int]] = {}
    staged: dict[Path, tuple[bytes, int]] = {}
    for _, role in compiler_module.ROLES:
        target_role = _mkdir_safe(output_root, Path(role))
        staged_role = _directory(staged_output, Path(role))
        assert staged_role is not None
        prior.update({Path(role) / relative: value for relative, value in _role_payloads(target_role).items()})
    for file in _tree_records(staged_output):
        if file.path == _MANIFEST_NAME:
            continue
        relative = _safe_relative(file.path, label="staged compiler path")
        if relative.parts[0] not in {role for _, role in compiler_module.ROLES}:
            raise _error("portable-methodology-stage-invalid", "staged compiler carrier has an unknown role")
        carrier = _regular(staged_output, relative, code="portable-methodology-stage-invalid")
        payload = _read(carrier, code="portable-methodology-stage-invalid")
        if _digest(payload) != file.sha256 or (carrier.stat().st_mode & 0o777) != file.mode:
            raise _error("portable-methodology-stage-invalid", "staged compiler carrier differs from its inventory")
        staged[relative] = (payload, file.mode)
    manifest = output_root / _MANIFEST_NAME
    prior_manifest = _read(manifest, code="portable-methodology-output-not-owned") if manifest.exists() else None
    changed: set[Path] = set()
    try:
        for relative, (payload, mode) in staged.items():
            target = output_root / relative
            _mkdir_safe(output_root, relative.parent)
            _replace_regular(target, payload, mode)
            changed.add(relative)
        for relative in set(prior).difference(staged):
            target = _regular(output_root, relative, code="portable-methodology-output-not-owned")
            target.unlink()
            changed.add(relative)
        _replace_regular(manifest, manifest_payload, 0o644)
    except (OSError, PortableMethodologyInstallationError) as error:
        rollback_failed = False
        for relative in changed:
            target = output_root / relative
            try:
                if relative in prior:
                    _replace_regular(target, *prior[relative])
                else:
                    target.unlink(missing_ok=True)
            except (OSError, PortableMethodologyInstallationError):
                rollback_failed = True
        try:
            if prior_manifest is None:
                manifest.unlink(missing_ok=True)
            else:
                _replace_regular(manifest, prior_manifest, 0o644)
        except (OSError, PortableMethodologyInstallationError):
            rollback_failed = True
        raise _error(
            "portable-methodology-publication-uncertain" if rollback_failed else "portable-methodology-publication-failed",
            "Methodology publication failed" if not rollback_failed else "Methodology publication recovery is uncertain",
        ) from error


def _reopen_delivery(
    output_root: Path,
    files: tuple[PortableMethodologyFile, ...],
    manifest_sha256: str,
    *,
    compiler_module: Any = compiler,
) -> tuple[str, Path]:
    _existing_output_owned(output_root, compiler_module=compiler_module)
    actual = _projection_records(output_root, compiler_module=compiler_module)
    if actual != tuple(sorted(files, key=lambda file: file.path)):
        raise _error("portable-methodology-publication-stale", "published role folders differ from staged compilation")
    manifest = _regular(output_root, Path(_MANIFEST_NAME), code="portable-methodology-publication-stale")
    payload = _read(manifest, code="portable-methodology-publication-stale")
    try:
        document = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise _error("portable-methodology-publication-stale", "published delivery manifest is invalid") from error
    if not isinstance(document, Mapping) or document.get("sha256") != manifest_sha256 or payload != _canonical_json(document) + b"\n":
        raise _error("portable-methodology-publication-stale", "published delivery manifest differs")
    return _digest(_canonical_json([file.__dict__ for file in actual])), manifest


def materialize_portable_methodology(
    request: PortableInstallationRequest,
    preparation: PortableInstallationPreparation,
    *,
    lock: InstallationPublicationLock,
) -> PortableMethodologyDelivery:
    """Compile and publish package-admitted Methodology under one owned lock.

    ``preparation`` is reopened from ``request`` before any stage exists, so a
    hand-built status flag, stale selector, changed catalog, or changed Full
    Gate receipt cannot authorize this publication.  This call does not
    activate the package selector or execute any runtime command.
    """
    current = _reopen_preparation(request, preparation)
    _rebind_target_context(request, current.target_context)
    _lock(request, current, lock)
    root, source_relative, output_relative = _context_paths(request, current)
    source_root = _directory(root, source_relative, missing_ok=True)
    authoring_before = _tree_digest(source_root)
    records = _catalog(current.package)
    members = _selected_members(
        current.package,
        records,
        _target_methodology_identities(current.target_context),
        current.target_context.package_evidence.source_pins,
    )
    package_compiler, compiler_binding = open_admitted_package_compiler(current.package)
    candidates, frontier = _selected_candidates(
        members,
        output_relative=output_relative,
        compiler_module=package_compiler,
    )
    stage, files, source_view_digest, manifest_sha256 = _stage(
        root,
        lock,
        output_relative,
        current.package,
        members,
        candidates,
        frontier,
        authoring_before,
        current.target_context.sha256,
        compiler_module=package_compiler,
        compiler_sha256=compiler_binding.sha256,
    )
    try:
        manifest_payload = _verify_staged(stage, files, manifest_sha256)
        _lock(request, current, lock)
        if _tree_digest(_directory(root, source_relative, missing_ok=True)) != authoring_before:
            raise _error("portable-methodology-authoring-stale", "authoritative Methodology source subtree changed before publication")
        _publish(stage, root, output_relative, manifest_payload, compiler_module=package_compiler)
        _lock(request, current, lock)
        if _tree_digest(_directory(root, source_relative, missing_ok=True)) != authoring_before:
            raise _error("portable-methodology-authoring-stale", "authoritative Methodology source subtree changed during publication")
        output_digest, manifest_path = _reopen_delivery(
            root / output_relative,
            files,
            manifest_sha256,
            compiler_module=package_compiler,
        )
        # Reopen the same gate/package context after publication.  The output is
        # derived, so this must not change readiness; a change is stale evidence.
        if _reopen_preparation(request, current) != current:
            raise _error("portable-methodology-preparation-stale", "gate/package evidence changed during Methodology publication")
        return PortableMethodologyDelivery(
            package_manifest_sha256=current.package.manifest_digest,
            source_catalog_sha256=current.package.source_catalog_sha256,
            target_project_context_sha256=current.target_context.sha256,
            compiler_sha256=compiler_binding.sha256,
            compiler_frontier_sha256=frontier,
            source_view_sha256=source_view_digest,
            authoring_source_sha256=authoring_before,
            output_tree_sha256=output_digest,
            delivery_manifest_sha256=manifest_sha256,
            output_root=root / output_relative,
            delivery_manifest_path=manifest_path,
            files=files,
        )
    finally:
        shutil.rmtree(stage, ignore_errors=True)


def publish_prepared_candidate_portable_methodology(
    request: PortableInstallationRequest,
    preparation: PreparedCandidateMethodologyPublication,
    *,
    package: VerifiedFrameworkPackage,
    target_context: TargetProjectContext,
    prospective_selector: CurrentPackageSelector,
    lock: InstallationPublicationLock,
) -> CandidatePortableMethodologyDelivery:
    """Publish the already gated private projection under an owned lock.

    The compiler is intentionally absent from this path.  Exact output bytes
    are reread from the retained candidate's sealed compiled delivery both
    before and after staging; a changed archive or Full Gate packet refuses.
    """

    current = reopen_prepared_candidate_portable_methodology_publication(
        request,
        preparation,
        package=package,
        target_context=target_context,
        prospective_selector=prospective_selector,
    )
    target_context = _rebind_target_context(request, target_context)
    _lock_context(request, target_context, lock)
    root, source_relative, output_relative = _context_paths_for(request, target_context)
    authoring_before = _tree_digest(_directory(root, source_relative, missing_ok=True))
    # Refuse a foreign root delivery before mutating the compiler projection.
    _existing_source_export_owned(_source_export_root(root), current.source_files)
    package_compiler, _compiler_binding = open_admitted_package_compiler(package)
    stage, files, manifest_sha256 = _stage_gated_compilation(
        root, lock, output_relative, current, compiler_module=package_compiler,
    )
    try:
        manifest_payload = _verify_staged(stage, files, manifest_sha256)
        _lock_context(request, target_context, lock)
        if _tree_digest(_directory(root, source_relative, missing_ok=True)) != authoring_before:
            raise _error("portable-methodology-authoring-stale", "authoritative Methodology source subtree changed before publication")
        _publish(stage, root, output_relative, manifest_payload, compiler_module=package_compiler)
        _lock_context(request, target_context, lock)
        if _tree_digest(_directory(root, source_relative, missing_ok=True)) != authoring_before:
            raise _error("portable-methodology-authoring-stale", "authoritative Methodology source subtree changed during publication")
        output_digest, manifest_path = _reopen_delivery(
            root / output_relative, files, manifest_sha256, compiler_module=package_compiler,
        )
        source_root = _publish_source_export(stage, root, current.source_files)
        if _tree_digest(_directory(root, source_relative, missing_ok=True)) != authoring_before:
            raise _error("portable-methodology-authoring-stale", "authoritative Methodology source subtree changed during source-export publication")
        reopened = reopen_prepared_candidate_portable_methodology_publication(
            request,
            current,
            package=package,
            target_context=target_context,
            prospective_selector=prospective_selector,
        )
        if reopened != current:
            raise _error("portable-methodology-prepared-stale", "gated Methodology inputs changed during publication")
        return CandidatePortableMethodologyDelivery(
            package_manifest_sha256=current.package_manifest_sha256,
            source_catalog_sha256=current.source_catalog_sha256,
            target_project_context_sha256=current.target_project_context_sha256,
            gate_receipt_sha256=current.gate_receipt_sha256,
            candidate_snapshot_manifest_sha256=current.candidate_snapshot_manifest_sha256,
            candidate_run_id=current.candidate_run_id,
            source_export_sha256=_digest(_canonical_json([file.__dict__ for file in current.source_files])),
            compiled_output_sha256=output_digest,
            delivery_manifest_sha256=manifest_sha256,
            source_export_root=source_root,
            output_root=root / output_relative,
            delivery_manifest_path=manifest_path,
            files=files,
        )
    finally:
        shutil.rmtree(stage, ignore_errors=True)


def publish_prepared_target_portable_methodology(
    request: PortableInstallationRequest,
    preparation: PreparedTargetMethodologyPublication,
    *,
    package: VerifiedFrameworkPackage,
    target_context: TargetProjectContext,
    prospective_selector: CurrentPackageSelector,
    lock: InstallationPublicationLock,
) -> TargetPortableMethodologyDelivery:
    """Publish pre-delete O200 bytes without invoking the compiler again."""

    current = reopen_prepared_target_portable_methodology_publication(
        request,
        preparation,
        package=package,
        target_context=target_context,
        prospective_selector=prospective_selector,
    )
    target_context = _rebind_target_context(request, target_context)
    _lock_context(request, target_context, lock)
    root, source_relative, output_relative = _context_paths_for(request, target_context)
    authoring_before = _tree_digest(_directory(root, source_relative, missing_ok=True))
    package_compiler, compiler_binding = open_admitted_package_compiler(package)
    if compiler_binding.sha256 != current.compiler_sha256:
        raise _error("portable-methodology-target-prepared-stale", "prepared direct target compiler differs from its admitted package carrier")
    stage, files, manifest_sha256 = _stage_prepared_target_compilation(
        root, lock, current, compiler_module=package_compiler,
    )
    try:
        manifest_payload = _verify_staged(stage, files, manifest_sha256)
        _lock_context(request, target_context, lock)
        if _tree_digest(_directory(root, source_relative, missing_ok=True)) != authoring_before:
            raise _error("portable-methodology-authoring-stale", "authoritative Methodology source subtree changed before publication")
        _publish(stage, root, output_relative, manifest_payload, compiler_module=package_compiler)
        _lock_context(request, target_context, lock)
        if _tree_digest(_directory(root, source_relative, missing_ok=True)) != authoring_before:
            raise _error("portable-methodology-authoring-stale", "authoritative Methodology source subtree changed during publication")
        output_digest, manifest_path = _reopen_delivery(
            root / output_relative, files, manifest_sha256, compiler_module=package_compiler,
        )
        # This is intentionally carrier-only validation.  The full reopener
        # rendered the exact direct-target projection before staging; after
        # publication starts, a publisher may have removed the predecessor
        # and must never recreate a compiler result from a new frontier.
        if _validate_prepared_target_bytes(
            request,
            current,
            package=package,
            target_context=target_context,
            prospective_selector=prospective_selector,
        ) != current:
            raise _error("portable-methodology-target-prepared-stale", "prepared direct target inputs changed during publication")
        return TargetPortableMethodologyDelivery(
            package_manifest_sha256=current.package_manifest_sha256,
            source_catalog_sha256=current.source_catalog_sha256,
            target_project_context_sha256=current.target_project_context_sha256,
            gate_receipt_sha256=current.gate_receipt_sha256,
            compiler_frontier_sha256=current.compiler_frontier_sha256,
            source_view_sha256=current.source_view_sha256,
            output_tree_sha256=output_digest,
            delivery_manifest_sha256=manifest_sha256,
            output_root=root / output_relative,
            delivery_manifest_path=manifest_path,
            files=files,
        )
    finally:
        shutil.rmtree(stage, ignore_errors=True)


__all__ = [
    "CandidatePortableMethodologyDelivery",
    "PACKAGE_COMPILER_RELATIVE",
    "PackageCompilerBinding",
    "PreparedTargetMethodologyFile",
    "PreparedTargetMethodologyPublication",
    "PreparedTargetMethodologySource",
    "PreparedCandidateMethodologyPublication",
    "PortableMethodologyDelivery",
    "PortableMethodologyFile",
    "PortableMethodologyInstallationError",
    "TargetPortableMethodologyDelivery",
    "materialize_portable_methodology",
    "open_admitted_package_compiler",
    "prepare_candidate_portable_methodology_publication",
    "prepare_target_portable_methodology_publication",
    "publish_prepared_candidate_portable_methodology",
    "publish_prepared_target_portable_methodology",
    "reopen_prepared_candidate_portable_methodology_publication",
    "reopen_admitted_package_compiler",
    "reopen_prepared_target_portable_methodology_publication",
]
