"""Closed, checkout-independent reusable Framework-package primitives.

This module deliberately has no runtime activation, package-current write, or
promotion policy.  It constructs and reopens a content-addressed package; the
INSTALL_TOOLS facade remains responsible for gated publication of its separate
``.caprmedio_install/current.toml`` selector.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import tempfile
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping


SCHEMA_VERSION = 1
PACKAGE_NAME = "caprmedio-framework"
MANIFEST_NAME = "manifest.toml"
CATALOG_NAME = "catalog.toml"
ENGINE_ROOT = Path("102_FRAMEWORK_ENGINE")
SKILL_ROOT = Path("SKILLS/ca")
DEFAULTS_ROOT = Path("defaults")
METHODOLOGY_ROOT = Path("methodology")
ADMISSIONS_ROOT = Path("admissions")
REQUIRED_TOP_LEVEL_FILES = ("pyproject.toml", "uv.lock", "version.toml", CATALOG_NAME)
SHA256_LENGTH = 64
_SHA256_CHARACTERS = frozenset("0123456789abcdef")
_CATALOG_KINDS = frozenset({"core", "methodology", "support", "extension", "configuration"})
_CATALOG_VISIBILITIES = frozenset({"public", "private"})
_ROLES = frozenset(
    {
        "engine",
        "dependency",
        "version",
        "catalog",
        "default",
        "skill",
        "methodology",
        "methodology-support",
        "source-admission",
    }
)
_SELECTOR_KEYS = frozenset(
    {
        "schema_version",
        "package_manifest_sha256",
        "release_relpath",
        "framework_version",
        "version_toml_sha256",
        "source_catalog_sha256",
        "full_gate_receipt_sha256",
        "image_digest",
    }
)
_PRIVATE_COMPONENTS = frozenset(
    {
        ".caprmedio_runtime",
        ".caprmedio_tmp",
        ".caprmedio_project",
        ".git",
        "operator_registry",
        "run_records",
        "credentials",
        "secrets",
        "private_settings",
    }
)


class FrameworkPackageError(RuntimeError):
    """Stable refusal from the reusable Framework package boundary."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


@dataclass(frozen=True)
class PackageInventoryRow:
    """One exact manifest row for a regular package member."""

    path: str
    sha256: str
    mode: int
    role: str


@dataclass(frozen=True)
class VerifiedFrameworkPackage:
    """The typed handoff for later gated package-selection and installation."""

    manifest_digest: str
    root: Path
    inventory: tuple[PackageInventoryRow, ...]
    framework_version: str
    version_toml_sha256: str
    source_catalog_sha256: str


@dataclass(frozen=True)
class CurrentPackageSelector:
    """Validated D598 installation-owned package selector data."""

    package_manifest_sha256: str
    release_relpath: str
    framework_version: str
    version_toml_sha256: str
    source_catalog_sha256: str
    full_gate_receipt_sha256: str
    image_digest: str


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _is_sha256(value: object) -> bool:
    return isinstance(value, str) and len(value) == SHA256_LENGTH and set(value) <= _SHA256_CHARACTERS


def _is_immutable_revision(value: object) -> bool:
    return isinstance(value, str) and len(value) in {40, SHA256_LENGTH} and set(value) <= _SHA256_CHARACTERS


def _is_schema_version(value: object) -> bool:
    return type(value) is int and value == SCHEMA_VERSION


def _safe_relative(value: object, field: str, *, code: str = "package-path-invalid") -> Path:
    if not isinstance(value, str) or not value:
        raise FrameworkPackageError(code, f"{field} must be a non-empty relative path")
    candidate = Path(value)
    if candidate.is_absolute() or candidate == Path(".") or any(part in {"", ".", ".."} for part in candidate.parts):
        raise FrameworkPackageError(code, f"{field} is unsafe")
    return candidate


def _lexical_root(value: Path | str, *, field: str, must_exist: bool) -> Path:
    """Return a lexical absolute root only after rejecting every symlink hop.

    ``Path.resolve`` is intentionally delayed until after this check: resolving
    first would erase the fact that a package caller supplied an alias.  A
    caller that intentionally uses macOS's ``/tmp`` alias must pass its own
    already-resolved stable path instead.
    """

    try:
        supplied = Path(value).expanduser()
        if any(part == ".." for part in supplied.parts):
            raise FrameworkPackageError("package-root-invalid", f"{field} must not contain parent traversal")
        root = Path(os.path.abspath(supplied))
        for candidate in (root, *root.parents):
            if candidate.is_symlink():
                raise FrameworkPackageError("package-root-symlink", f"{field} contains a symlink: {candidate}")
        if must_exist and not root.is_dir():
            raise FrameworkPackageError("package-root-invalid", f"{field} is not a regular directory: {root}")
        return root
    except FrameworkPackageError:
        raise
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise FrameworkPackageError("package-root-invalid", f"{field} is unavailable or unsafe") from error


def _contains_private_component(relative: Path) -> bool:
    for component in relative.parts:
        lowered = component.lower()
        if lowered in _PRIVATE_COMPONENTS or lowered.startswith(".env") or lowered.endswith(".env"):
            return True
    return False


def _check_visible_path(relative: Path) -> None:
    if _contains_private_component(relative):
        raise FrameworkPackageError("package-private-member", f"private Project state is not package content: {relative.as_posix()}")


def _read_toml_bytes(payload: bytes, *, code: str, subject: str) -> dict[str, Any]:
    try:
        parsed = tomllib.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise FrameworkPackageError(code, f"{subject} is not valid TOML") from error
    if not isinstance(parsed, dict):  # tomllib currently always returns dict; retain the boundary explicitly.
        raise FrameworkPackageError(code, f"{subject} root must be a table")
    return parsed


def _walk_regular_files(root: Path, *, code_prefix: str) -> tuple[Path, ...]:
    if root.is_symlink():
        raise FrameworkPackageError(f"{code_prefix}-symlink", f"package root is a symlink: {root}")
    if not root.is_dir():
        raise FrameworkPackageError(f"{code_prefix}-missing", f"package root is absent: {root}")
    result: list[Path] = []
    pending = [root]
    while pending:
        directory = pending.pop()
        if directory.is_symlink():
            relative = directory.relative_to(root)
            raise FrameworkPackageError(f"{code_prefix}-symlink", f"package directory is a symlink: {relative.as_posix()}")
        try:
            children = sorted(directory.iterdir(), key=lambda child: child.name)
        except OSError as error:
            raise FrameworkPackageError(f"{code_prefix}-unreadable", f"cannot inspect package directory: {directory}") from error
        for child in children:
            relative = child.relative_to(root)
            if child.is_symlink():
                raise FrameworkPackageError(f"{code_prefix}-symlink", f"package member is a symlink: {relative.as_posix()}")
            if child.is_dir():
                if child.name == "__pycache__":
                    continue
                _check_visible_path(relative)
                pending.append(child)
            elif child.is_file():
                _check_visible_path(relative)
                if child.name == ".DS_Store" or child.suffix in {".pyc", ".pyo"}:
                    continue
                result.append(child)
            else:
                raise FrameworkPackageError(f"{code_prefix}-member-invalid", f"package member is not a regular file: {relative.as_posix()}")
    return tuple(sorted(result, key=lambda path: path.relative_to(root).as_posix()))


def _role_for(relative: Path) -> str:
    if relative == Path(CATALOG_NAME):
        return "catalog"
    if relative == Path("version.toml"):
        return "version"
    if relative in {Path("pyproject.toml"), Path("uv.lock")}:
        return "dependency"
    if relative.is_relative_to(ENGINE_ROOT):
        return "engine"
    if relative.is_relative_to(SKILL_ROOT):
        return "skill"
    if relative.is_relative_to(DEFAULTS_ROOT):
        return "default"
    if relative.is_relative_to(ADMISSIONS_ROOT):
        if relative.parent == ADMISSIONS_ROOT and relative.suffix == ".json" and _is_sha256(relative.stem):
            return "source-admission"
        raise FrameworkPackageError("package-extra-member", f"unadmitted source admission member: {relative.as_posix()}")
    if relative.is_relative_to(METHODOLOGY_ROOT / "support"):
        return "methodology-support"
    if relative.is_relative_to(METHODOLOGY_ROOT):
        return "methodology"
    raise FrameworkPackageError("package-extra-member", f"unadmitted package member: {relative.as_posix()}")


def _version_from_toml(payload: bytes) -> str:
    document = _read_toml_bytes(payload, code="package-version-invalid", subject="version.toml")
    if "framework_version" in document or "version" in document:
        raise FrameworkPackageError("package-version-invalid", "version.toml must use only [framework].version")
    framework = document.get("framework")
    if not isinstance(framework, Mapping):
        raise FrameworkPackageError("package-version-invalid", "version.toml must contain a framework table")
    version = framework.get("version")
    if not isinstance(version, str) or not version:
        raise FrameworkPackageError("package-version-invalid", "version.toml does not carry [framework].version")
    return version


def _path_digest(root: Path, relative: Path, *, code: str) -> str:
    target = root / relative
    cursor = root
    for part in relative.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise FrameworkPackageError(code, f"catalog source is a symlink: {relative.as_posix()}")
    if target.is_file():
        return _sha256(target.read_bytes())
    if not target.is_dir():
        raise FrameworkPackageError(code, f"catalog source is absent: {relative.as_posix()}")
    files = _walk_regular_files(target, code_prefix="package")
    rows = [
        {
            "path": file.relative_to(target).as_posix(),
            "sha256": _sha256(file.read_bytes()),
            "mode": file.stat().st_mode & 0o777,
        }
        for file in files
    ]
    if not rows:
        raise FrameworkPackageError(code, f"catalog source is empty: {relative.as_posix()}")
    return _sha256(json.dumps(rows, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8"))


def read_source_catalog_records(payload: bytes) -> tuple[tuple[str, Mapping[str, Any]], ...]:
    """Read one closed source-catalog descriptor without opening its sources.

    Filesystem consumers retain their own digest and coverage checks.  Sharing
    this descriptor reader keeps package assembly and planned portable rows on
    the same closed schema, type, revision and visible-path boundary.
    """

    document = _read_toml_bytes(payload, code="catalog-invalid", subject=CATALOG_NAME)
    if set(document) != {"schema_version", "source"} or not _is_schema_version(document.get("schema_version")):
        raise FrameworkPackageError("catalog-invalid", "catalog.toml has an invalid closed root schema")
    sources = document.get("source")
    if not isinstance(sources, Mapping) or not sources:
        raise FrameworkPackageError("catalog-invalid", "catalog.toml must contain source records")
    saw_core = saw_methodology = saw_support = False
    records: list[tuple[str, Mapping[str, Any]]] = []
    for identity, raw in sorted(sources.items(), key=lambda entry: entry[0]):
        if not isinstance(identity, str) or not identity or not isinstance(raw, Mapping):
            raise FrameworkPackageError("catalog-invalid", "catalog source identities must name tables")
        expected_keys = {"kind", "revision", "sha256", "admission_receipt_sha256", "visibility", "selection_default", "path"}
        if set(raw) != expected_keys:
            raise FrameworkPackageError("catalog-invalid", f"catalog source has invalid fields: {identity}")
        kind = raw.get("kind")
        revision = raw.get("revision")
        expected_digest = raw.get("sha256")
        receipt = raw.get("admission_receipt_sha256")
        visibility = raw.get("visibility")
        selection_default = raw.get("selection_default")
        if not isinstance(kind, str) or kind not in _CATALOG_KINDS:
            raise FrameworkPackageError("catalog-invalid", f"catalog source kind is invalid: {identity}")
        if not _is_immutable_revision(revision):
            raise FrameworkPackageError("catalog-revision-invalid", f"catalog source revision is not immutable: {identity}")
        if not _is_sha256(expected_digest) or not _is_sha256(receipt):
            raise FrameworkPackageError("catalog-invalid", f"catalog source digest is invalid: {identity}")
        if not isinstance(visibility, str) or visibility not in _CATALOG_VISIBILITIES or not isinstance(selection_default, bool):
            raise FrameworkPackageError("catalog-invalid", f"catalog source selection is invalid: {identity}")
        if visibility == "private" and selection_default:
            raise FrameworkPackageError("catalog-invalid", f"private catalog source cannot be a default: {identity}")
        relative = _safe_relative(raw.get("path"), f"source.{identity}.path", code="catalog-invalid")
        _check_visible_path(relative)
        if (
            relative == Path(CATALOG_NAME)
            or relative.is_relative_to(Path(".caprmedio_install"))
            or relative.is_relative_to(ADMISSIONS_ROOT)
        ):
            raise FrameworkPackageError("catalog-invalid", f"catalog source targets package control state: {identity}")
        saw_core |= kind == "core"
        saw_methodology |= kind == "methodology"
        saw_support |= kind == "support"
        records.append((identity, raw))
    if not (saw_core and saw_methodology and saw_support):
        raise FrameworkPackageError("catalog-incomplete", "catalog must admit Core, active Methodology, and declared support")
    return tuple(records)


def _admission_member_path(receipt_sha256: str) -> Path:
    """Return the one package member designated by a catalog receipt digest."""

    if not _is_sha256(receipt_sha256):
        raise FrameworkPackageError("catalog-invalid", "catalog admission receipt digest is invalid")
    return ADMISSIONS_ROOT / f"{receipt_sha256}.json"


def _read_admission_member(root: Path, receipt_sha256: str) -> bytes:
    """Reopen a designated receipt without following an alias or special node."""

    relative = _admission_member_path(receipt_sha256)
    cursor = root
    for part in relative.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise FrameworkPackageError(
                "catalog-admission-member-invalid",
                f"admission receipt is a symlink: {relative.as_posix()}",
            )
    if not cursor.is_file():
        raise FrameworkPackageError(
            "catalog-admission-missing",
            f"catalog admission receipt is absent: {relative.as_posix()}",
        )
    try:
        return cursor.read_bytes()
    except OSError as error:
        raise FrameworkPackageError(
            "catalog-admission-unreadable",
            f"catalog admission receipt cannot be read: {relative.as_posix()}",
        ) from error


def _read_catalog_admission_receipt(payload: bytes, receipt_sha256: str) -> Any:
    """Use the shared D602 codec without introducing a package/codec import cycle."""

    try:
        from source_catalog_admission import SourceCatalogAdmissionError, read_source_admission_receipt
    except ImportError as error:  # pragma: no cover - installed package composition guard
        raise FrameworkPackageError(
            "catalog-admission-reader-unavailable",
            "the source-admission receipt reader is unavailable",
        ) from error
    try:
        return read_source_admission_receipt(payload, expected_sha256=receipt_sha256)
    except SourceCatalogAdmissionError as error:
        raise FrameworkPackageError(error.code, str(error)) from error


def _catalog_receipt_descriptor(identity: str, record: Mapping[str, Any]) -> dict[str, object]:
    """Normalize the catalog half of a D602 descriptor for exact comparison."""

    return {
        "identity": identity,
        "kind": record["kind"],
        "revision": record["revision"],
        "sha256": record["sha256"],
        "visibility": record["visibility"],
        "selection_default": record["selection_default"],
        "path": _safe_relative(record["path"], f"source.{identity}.path", code="catalog-invalid").as_posix(),
    }


def _validate_methodology_catalog_partition(
    root: Path,
    records: tuple[tuple[str, Mapping[str, Any]], ...],
) -> None:
    """Require the D561v3 disjoint source roots before a package is trusted.

    Selection is intentionally irrelevant here.  A retained optional Extension
    or Configuration remains physical package content and must therefore be
    represented once, while a nested descriptor may never borrow an ancestor's
    coverage.
    """

    expected_singletons = {
        "core": Path("102_FRAMEWORK_ENGINE"),
        "support": METHODOLOGY_ROOT / "support",
        "methodology": METHODOLOGY_ROOT / "active" / "001_CORE_META_MODEL",
    }
    compiler_kinds = frozenset({"methodology", "extension", "configuration"})
    compiler_roots: list[Path] = []
    for kind, expected in expected_singletons.items():
        matching = [
            identity
            for identity, record in records
            if record["kind"] == kind
            and _safe_relative(record["path"], f"source.{identity}.path", code="catalog-invalid") == expected
        ]
        if len(matching) != 1:
            raise FrameworkPackageError(
                "catalog-topology-invalid",
                f"catalog must admit exactly one {kind} root at {expected.as_posix()}",
            )
        if sum(record["kind"] == kind for _identity, record in records) != 1:
            raise FrameworkPackageError("catalog-topology-invalid", f"catalog has an unexpected {kind} root")

    for identity, record in records:
        kind = str(record["kind"])
        relative = _safe_relative(record["path"], f"source.{identity}.path", code="catalog-invalid")
        if kind == "configuration":
            expected = METHODOLOGY_ROOT / "active" / "003_PROJECT_CONFIGURATION"
            if relative != expected:
                raise FrameworkPackageError(
                    "catalog-topology-invalid",
                    f"Configuration root is not {expected.as_posix()}: {identity}",
                )
        elif kind == "extension":
            prefix = METHODOLOGY_ROOT / "active" / "002_INSTALLED_EXTENSIONS"
            if not relative.is_relative_to(prefix) or len(relative.relative_to(prefix).parts) != 2:
                raise FrameworkPackageError(
                    "catalog-topology-invalid",
                    f"Extension root is not identity/revision scoped: {identity}",
                )
        if kind in compiler_kinds:
            compiler_roots.append(relative)

    for index, left in enumerate(compiler_roots):
        for right in compiler_roots[index + 1:]:
            if left == right or left.is_relative_to(right) or right.is_relative_to(left):
                raise FrameworkPackageError(
                    "catalog-methodology-overlap",
                    "catalog Methodology descriptors overlap",
                )

    active = root / METHODOLOGY_ROOT / "active"
    active_rows = _walk_regular_files(active, code_prefix="catalog-source")
    for file in active_rows:
        relative = file.relative_to(root)
        matches = [descriptor for descriptor in compiler_roots if relative.is_relative_to(descriptor)]
        if not matches:
            raise FrameworkPackageError(
                "catalog-methodology-uncovered",
                f"catalog does not admit Methodology member: {relative.as_posix()}",
            )
        if len(matches) != 1:  # Defensive: the topology comparison above should reject this first.
            raise FrameworkPackageError(
                "catalog-methodology-overlap",
                f"catalog admits Methodology member more than once: {relative.as_posix()}",
            )


def _validate_catalog(root: Path, payload: bytes) -> tuple[tuple[str, Mapping[str, Any]], ...]:
    """Validate descriptors, their physical sources, and retained D602 proofs."""

    records = read_source_catalog_records(payload)
    receipts: dict[str, Any] = {}
    expected_sources: dict[str, list[dict[str, object]]] = {}
    for identity, record in records:
        relative = _safe_relative(record["path"], f"source.{identity}.path", code="catalog-invalid")
        if _path_digest(root, relative, code="catalog-source-missing") != record["sha256"]:
            raise FrameworkPackageError("catalog-source-digest-mismatch", f"catalog source digest differs: {identity}")
        receipt_sha256 = record["admission_receipt_sha256"]
        receipt = receipts.get(receipt_sha256)
        if receipt is None:
            receipt = _read_catalog_admission_receipt(
                _read_admission_member(root, receipt_sha256),
                receipt_sha256,
            )
            receipts[receipt_sha256] = receipt
        expected = _catalog_receipt_descriptor(identity, record)
        matches = [source for source in receipt.sources if source.record() == expected]
        if len(matches) != 1:
            raise FrameworkPackageError(
                "catalog-admission-source-mismatch",
                f"catalog source is not admitted by its receipt: {identity}",
            )
        expected_sources.setdefault(receipt_sha256, []).append(expected)
    for receipt_sha256, expected in expected_sources.items():
        receipt = receipts[receipt_sha256]
        actual = tuple(source.record() for source in receipt.sources)
        if actual != tuple(sorted(expected, key=lambda source: str(source["identity"]))):
            raise FrameworkPackageError(
                "catalog-admission-source-mismatch",
                "admission receipt includes a source not named by its catalog references",
            )
    _validate_methodology_catalog_partition(root, records)
    return records


def _catalog_covers(
    relative: Path,
    *,
    kinds: frozenset[str],
    records: tuple[tuple[str, Mapping[str, Any]], ...],
) -> bool:
    for _, record in records:
        if record["kind"] not in kinds:
            continue
        admitted = _safe_relative(record["path"], "catalog source path", code="catalog-invalid")
        if relative == admitted or relative.is_relative_to(admitted):
            return True
    return False


def _validate_complete_layout(
    paths: set[str],
    rows: tuple[PackageInventoryRow, ...],
    catalog_records: tuple[tuple[str, Mapping[str, Any]], ...],
) -> None:
    """Reapply D596 completeness to both source assembly and reopened bytes."""

    missing = [name for name in REQUIRED_TOP_LEVEL_FILES if name not in paths]
    if missing:
        raise FrameworkPackageError("package-incomplete", "required package member is missing: " + ", ".join(missing))
    by_role = {role: [row for row in rows if row.role == role] for role in _ROLES}
    for role, label in (
        ("engine", "complete Framework Engine"),
        ("skill", "ca Skill"),
        ("default", "admitted defaults"),
        ("methodology", "active Methodology"),
        ("methodology-support", "declared Methodology support"),
    ):
        if not by_role[role]:
            raise FrameworkPackageError("package-incomplete", f"{label} is missing")
    expected_admissions = {
        _admission_member_path(str(record["admission_receipt_sha256"])).as_posix()
        for _, record in catalog_records
    }
    actual_admissions = {
        path
        for path in paths
        if Path(path).is_relative_to(ADMISSIONS_ROOT)
    }
    if actual_admissions != expected_admissions:
        if expected_admissions - actual_admissions:
            raise FrameworkPackageError("catalog-admission-missing", "catalog admission receipt is missing from package inventory")
        raise FrameworkPackageError("package-extra-member", "package has unreferenced admission receipt")
    for row in rows:
        relative = Path(row.path)
        if _role_for(relative) != row.role:
            raise FrameworkPackageError("package-manifest-invalid", f"package member role differs: {row.path}")
        catalog_kinds = {
            "engine": frozenset({"core"}),
            # All three D561 compiler source classes are represented by the
            # one package inventory role.  Their target applicability remains
            # explicit in target_methodology_selection; this only proves that
            # every retained active byte has one exact catalog descriptor.
            "methodology": frozenset({"methodology", "extension", "configuration"}),
            "methodology-support": frozenset({"support"}),
        }.get(row.role)
        if catalog_kinds is not None and not _catalog_covers(relative, kinds=catalog_kinds, records=catalog_records):
            raise FrameworkPackageError("catalog-incomplete", f"catalog does not admit package member: {row.path}")


def _source_inventory(root: Path) -> tuple[tuple[PackageInventoryRow, ...], str, str, str]:
    files = _walk_regular_files(root, code_prefix="package")
    by_relative = {file.relative_to(root).as_posix(): file for file in files}
    missing = [name for name in REQUIRED_TOP_LEVEL_FILES if name not in by_relative]
    if missing:
        raise FrameworkPackageError("package-incomplete", "required package member is missing: " + ", ".join(missing))
    catalog_path = by_relative[CATALOG_NAME]
    catalog_records = _validate_catalog(root, catalog_path.read_bytes())
    rows = tuple(
        PackageInventoryRow(
            path=relative,
            sha256=_sha256(file.read_bytes()),
            mode=file.stat().st_mode & 0o777,
            role=_role_for(Path(relative)),
        )
        for relative, file in sorted(by_relative.items())
        if relative != MANIFEST_NAME
    )
    if MANIFEST_NAME in by_relative:
        raise FrameworkPackageError("package-manifest-source", "source package must not carry a self-hashing manifest")
    _validate_complete_layout(set(by_relative), rows, catalog_records)
    version_payload = by_relative["version.toml"].read_bytes()
    return rows, _version_from_toml(version_payload), _sha256(version_payload), _sha256(catalog_path.read_bytes())


def _render_manifest(
    *,
    framework_version: str,
    version_toml_sha256: str,
    source_catalog_sha256: str,
    rows: tuple[PackageInventoryRow, ...],
) -> bytes:
    lines = [
        f"schema_version = {SCHEMA_VERSION}",
        f"package = {_quoted(PACKAGE_NAME)}",
        f"framework_version = {_quoted(framework_version)}",
        f"version_toml_sha256 = {_quoted(version_toml_sha256)}",
        f"source_catalog_sha256 = {_quoted(source_catalog_sha256)}",
        "",
    ]
    for row in rows:
        lines.extend(
            [
                "[[files]]",
                f"path = {_quoted(row.path)}",
                f"sha256 = {_quoted(row.sha256)}",
                f"mode = {row.mode}",
                f"role = {_quoted(row.role)}",
                "",
            ]
        )
    return "\n".join(lines).encode("utf-8")


def _manifest_inventory(payload: bytes) -> tuple[tuple[PackageInventoryRow, ...], str, str, str]:
    document = _read_toml_bytes(payload, code="package-manifest-invalid", subject=MANIFEST_NAME)
    if set(document) != {"schema_version", "package", "framework_version", "version_toml_sha256", "source_catalog_sha256", "files"}:
        raise FrameworkPackageError("package-manifest-invalid", "manifest.toml has an invalid closed root schema")
    if not _is_schema_version(document.get("schema_version")) or document.get("package") != PACKAGE_NAME:
        raise FrameworkPackageError("package-manifest-invalid", "manifest identity is invalid")
    framework_version = document.get("framework_version")
    version_digest = document.get("version_toml_sha256")
    catalog_digest = document.get("source_catalog_sha256")
    if not isinstance(framework_version, str) or not framework_version or not _is_sha256(version_digest) or not _is_sha256(catalog_digest):
        raise FrameworkPackageError("package-manifest-invalid", "manifest version or catalog identity is invalid")
    raw_rows = document.get("files")
    if not isinstance(raw_rows, list) or not raw_rows:
        raise FrameworkPackageError("package-manifest-invalid", "manifest file inventory is missing")
    rows: list[PackageInventoryRow] = []
    for raw in raw_rows:
        if not isinstance(raw, Mapping) or set(raw) != {"path", "sha256", "mode", "role"}:
            raise FrameworkPackageError("package-manifest-invalid", "manifest file row has an invalid closed schema")
        relative = _safe_relative(raw.get("path"), "files.path", code="package-manifest-invalid")
        digest = raw.get("sha256")
        mode = raw.get("mode")
        role = raw.get("role")
        if relative == Path(MANIFEST_NAME) or not _is_sha256(digest) or not isinstance(mode, int) or isinstance(mode, bool) or not 0 <= mode <= 0o777 or role not in _ROLES:
            raise FrameworkPackageError("package-manifest-invalid", "manifest file row is invalid")
        rows.append(PackageInventoryRow(relative.as_posix(), digest, mode, role))
    ordered = tuple(sorted(rows, key=lambda row: row.path))
    if tuple(rows) != ordered or len({row.path for row in rows}) != len(rows):
        raise FrameworkPackageError("package-manifest-invalid", "manifest rows must be path-ordered and unique")
    return ordered, framework_version, version_digest, catalog_digest


def _verify_package_tree(root: Path, *, require_content_addressed_name: bool) -> VerifiedFrameworkPackage:
    if root.is_symlink() or not root.is_dir():
        raise FrameworkPackageError("package-root-invalid", f"package root is unavailable: {root}")
    manifest = root / MANIFEST_NAME
    if manifest.is_symlink() or not manifest.is_file():
        raise FrameworkPackageError("package-manifest-missing", f"package manifest is unavailable: {manifest}")
    manifest_bytes = manifest.read_bytes()
    inventory, framework_version, version_digest, catalog_digest = _manifest_inventory(manifest_bytes)
    manifest_digest = _sha256(manifest_bytes)
    if require_content_addressed_name and root.name != manifest_digest:
        raise FrameworkPackageError("package-digest-mismatch", "release directory name differs from manifest bytes digest")
    actual_files = _walk_regular_files(root, code_prefix="package")
    actual_paths = {path.relative_to(root).as_posix() for path in actual_files}
    expected_paths = {MANIFEST_NAME, *(row.path for row in inventory)}
    extras = actual_paths - expected_paths
    missing = expected_paths - actual_paths
    if extras:
        raise FrameworkPackageError("package-extra-member", "package has undeclared member: " + sorted(extras)[0])
    if missing:
        raise FrameworkPackageError("package-member-missing", "package misses declared member: " + sorted(missing)[0])
    for row in inventory:
        relative = _safe_relative(row.path, "files.path")
        carrier = root / relative
        if carrier.is_symlink() or not carrier.is_file():
            raise FrameworkPackageError("package-member-missing", f"package member is missing: {row.path}")
        if _sha256(carrier.read_bytes()) != row.sha256:
            raise FrameworkPackageError("package-member-digest-mismatch", f"package member bytes differ: {row.path}")
        if carrier.stat().st_mode & 0o777 != row.mode:
            raise FrameworkPackageError("package-member-mode-mismatch", f"package member mode differs: {row.path}")
        if _role_for(relative) != row.role:
            raise FrameworkPackageError("package-manifest-invalid", f"package member role differs: {row.path}")
    if _sha256((root / "version.toml").read_bytes()) != version_digest or _version_from_toml((root / "version.toml").read_bytes()) != framework_version:
        raise FrameworkPackageError("package-version-mismatch", "package version carrier differs from manifest")
    catalog = root / CATALOG_NAME
    if _sha256(catalog.read_bytes()) != catalog_digest:
        raise FrameworkPackageError("package-catalog-mismatch", "package catalog differs from manifest")
    catalog_records = _validate_catalog(root, catalog.read_bytes())
    _validate_complete_layout(actual_paths - {MANIFEST_NAME}, inventory, catalog_records)
    return VerifiedFrameworkPackage(manifest_digest, root, inventory, framework_version, version_digest, catalog_digest)


def assemble_framework_package(source_root: Path | str, releases_root: Path | str) -> VerifiedFrameworkPackage:
    """Copy a closed source assembly into one content-addressed package release.

    ``source_root`` is a preselected, non-checkout payload assembly.  The
    function neither writes the package-current selector nor activates a
    runtime; callers must gate those separate operations.
    """

    source = _lexical_root(source_root, field="source_root", must_exist=True)
    releases = _lexical_root(releases_root, field="releases_root", must_exist=False)
    rows, framework_version, version_digest, catalog_digest = _source_inventory(source)
    manifest = _render_manifest(
        framework_version=framework_version,
        version_toml_sha256=version_digest,
        source_catalog_sha256=catalog_digest,
        rows=rows,
    )
    manifest_digest = _sha256(manifest)
    if releases.is_symlink():
        raise FrameworkPackageError("package-release-root-invalid", f"release root is a symlink: {releases}")
    releases.mkdir(parents=True, exist_ok=True)
    if not releases.is_dir():
        raise FrameworkPackageError("package-release-root-invalid", f"release root is not a directory: {releases}")
    release = releases / manifest_digest
    if release.exists() or release.is_symlink():
        return _verify_package_tree(release, require_content_addressed_name=True)
    staging = Path(tempfile.mkdtemp(prefix=f".package-{manifest_digest[:12]}-", dir=releases))
    try:
        for row in rows:
            source_file = source / row.path
            if source_file.is_symlink() or not source_file.is_file() or _sha256(source_file.read_bytes()) != row.sha256 or source_file.stat().st_mode & 0o777 != row.mode:
                raise FrameworkPackageError("package-source-drift", f"source changed before package copy: {row.path}")
            target = staging / row.path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source_file, target)
            target.chmod(row.mode)
        (staging / MANIFEST_NAME).write_bytes(manifest)
        (staging / MANIFEST_NAME).chmod(0o644)
        _verify_package_tree(staging, require_content_addressed_name=False)
        try:
            os.replace(staging, release)
        except FileExistsError:
            pass
        except PermissionError:
            # Some managed macOS filesystems deny an otherwise local atomic
            # directory rename.  Keep the staging proof and use a guarded
            # copy only when no competing release appeared; the resulting
            # release is still reopened below before it becomes a handoff.
            if release.exists() or release.is_symlink():
                pass
            else:
                try:
                    shutil.copytree(staging, release)
                except FileExistsError:
                    pass
        return _verify_package_tree(release, require_content_addressed_name=True)
    finally:
        if staging.exists():
            try:
                shutil.rmtree(staging)
            except PermissionError:
                # Retain an inspectable fixture/staging root if this host denies
                # cleanup; never convert a cleanup denial into a success claim.
                pass


def verify_framework_package(package_root: Path | str) -> VerifiedFrameworkPackage:
    """Reopen a content-addressed release and verify its exact closed manifest."""

    root = _lexical_root(package_root, field="package_root", must_exist=True)
    return _verify_package_tree(root, require_content_addressed_name=True)


def verify_current_package_selector(payload: bytes | str, package: VerifiedFrameworkPackage) -> CurrentPackageSelector:
    """Validate D598 selector bytes against an already-verified package handoff."""

    if not isinstance(package, VerifiedFrameworkPackage):
        raise FrameworkPackageError("package-selector-invalid", "selector requires a typed verified package")
    reopened = verify_framework_package(package.root)
    if reopened != package:
        raise FrameworkPackageError("package-selector-mismatch", "selector package handoff differs from reopened package bytes")
    raw = payload.encode("utf-8") if isinstance(payload, str) else payload
    if not isinstance(raw, bytes):
        raise FrameworkPackageError("package-selector-invalid", "selector must be TOML bytes")
    document = _read_toml_bytes(raw, code="package-selector-invalid", subject="current selector")
    if set(document) != _SELECTOR_KEYS or not _is_schema_version(document.get("schema_version")):
        raise FrameworkPackageError("package-selector-invalid", "selector has an invalid closed schema")
    fields = {key: document.get(key) for key in _SELECTOR_KEYS if key != "schema_version"}
    if not all(isinstance(value, str) and value for value in fields.values()):
        raise FrameworkPackageError("package-selector-invalid", "selector values must be non-empty strings")
    for key in ("package_manifest_sha256", "version_toml_sha256", "source_catalog_sha256", "full_gate_receipt_sha256", "image_digest"):
        if not _is_sha256(fields[key]):
            raise FrameworkPackageError("package-selector-invalid", f"selector {key} is not a lowercase sha256")
    expected_relpath = f"releases/{package.manifest_digest}"
    if fields["release_relpath"] != expected_relpath:
        raise FrameworkPackageError("package-selector-invalid", "selector release path is not the exact package path")
    if (
        fields["package_manifest_sha256"] != package.manifest_digest
        or fields["framework_version"] != package.framework_version
        or fields["version_toml_sha256"] != package.version_toml_sha256
        or fields["source_catalog_sha256"] != package.source_catalog_sha256
    ):
        raise FrameworkPackageError("package-selector-mismatch", "selector does not bind the verified package")
    return CurrentPackageSelector(
        package_manifest_sha256=fields["package_manifest_sha256"],
        release_relpath=fields["release_relpath"],
        framework_version=fields["framework_version"],
        version_toml_sha256=fields["version_toml_sha256"],
        source_catalog_sha256=fields["source_catalog_sha256"],
        full_gate_receipt_sha256=fields["full_gate_receipt_sha256"],
        image_digest=fields["image_digest"],
    )


def provide_installation_package_evidence(package_root: Path | str) -> object:
    """Reopen a package and derive the target-context evidence from its catalog.

    The returned ``installation_context.VerifiedPackageEvidence`` cannot be
    caller-asserted: this provider first reopens the release, verifies every
    manifest member, and reads its pins from the sealed ``catalog.toml``.  Its
    legacy ``selected_source_identities`` compatibility summary is not target
    applicability; target_methodology_selection binds that separately from
    canonical Framework Instance Settings.
    ``installation_context`` stays imported lazily so this reusable package
    primitive has no import-time dependency on target-control code.
    """

    package = verify_framework_package(package_root)
    records = _validate_catalog(package.root, (package.root / CATALOG_NAME).read_bytes())
    try:
        from installation_context import PackageSourcePin, VerifiedPackageEvidence
    except ImportError as error:  # pragma: no cover - protects use by isolated package tooling.
        raise FrameworkPackageError("package-evidence-unavailable", "target installation evidence types are unavailable") from error
    pins = tuple(
        PackageSourcePin(
            identity=identity,
            kind=str(record["kind"]),
            revision=str(record["revision"]),
            sha256=str(record["sha256"]),
            admission_receipt_sha256=str(record["admission_receipt_sha256"]),
            path=str(record["path"]),
        )
        for identity, record in records
    )
    selected = tuple(
        identity
        for identity, record in records
        if record["kind"] in {"core", "methodology", "support"}
    )
    return VerifiedPackageEvidence(
        package_manifest_sha256=package.manifest_digest,
        catalog_sha256=package.source_catalog_sha256,
        source_pins=pins,
        selected_source_identities=selected,
        verified=True,
    )


__all__ = [
    "CATALOG_NAME",
    "CurrentPackageSelector",
    "FrameworkPackageError",
    "MANIFEST_NAME",
    "PACKAGE_NAME",
    "PackageInventoryRow",
    "SCHEMA_VERSION",
    "VerifiedFrameworkPackage",
    "assemble_framework_package",
    "provide_installation_package_evidence",
    "read_source_catalog_records",
    "verify_current_package_selector",
    "verify_framework_package",
]
