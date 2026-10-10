"""Explicit local-source admission for one reusable Framework package.

This module retains the D602 proof carrier and its matching ``catalog.toml``.
It has no release-selection, runtime, image, Skill, gate, Journal, or workflow
effect.  A caller must provide both a sealed physical source snapshot and a
trusted invocation-admitter callback; neither a caller boolean nor this module
can approve an admission by itself.

``framework_package`` imports the receipt codec lazily while reopening a
package.  Consequently this module must not import ``framework_package`` at
module import time.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import tempfile
from typing import Any


SCHEMA_VERSION = 1
OPERATION = "admit_package_sources"
CATALOG_NAME = "catalog.toml"
ADMISSIONS_DIRECTORY = PurePosixPath("admissions")
SHA256_LENGTH = 64

_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_IDENTITY = re.compile(r"[a-z][a-z0-9_-]*\Z")
_KINDS = frozenset({"core", "methodology", "support", "extension", "configuration", "binding"})
_VISIBILITIES = frozenset({"public", "private"})
_DESCRIPTOR_KEYS = frozenset(
    {"identity", "kind", "revision", "sha256", "visibility", "selection_default", "path"}
)
_RECEIPT_KEYS = frozenset(
    {"schema_version", "operation", "operator", "command_ref", "action_run_id", "snapshot_sha256", "sources"}
)


class SourceCatalogAdmissionError(RuntimeError):
    """Stable refusal from the D602 local-source admission boundary."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


def _refuse(code: str, message: str) -> None:
    raise SourceCatalogAdmissionError(code, message)


def _canonical_json(value: object) -> bytes:
    try:
        return json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        _refuse("source-admission-receipt-invalid", "receipt cannot be canonicalized")
        raise AssertionError("unreachable") from error


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _require_sha256(value: object, *, field: str, code: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        _refuse(code, f"{field} must be a lowercase SHA-256")
    return value


def _require_immutable_revision(value: object, *, field: str, code: str) -> str:
    if not isinstance(value, str) or len(value) not in {40, SHA256_LENGTH} or any(character not in "0123456789abcdef" for character in value):
        _refuse(code, f"{field} must be an immutable lowercase revision")
    return value


def _safe_relative(value: object, *, field: str, code: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value:
        _refuse(code, f"{field} must be a non-empty normalized relative path")
    path = PurePosixPath(value)
    if path.is_absolute() or path == PurePosixPath(".") or any(part in {"", ".", ".."} for part in path.parts):
        _refuse(code, f"{field} is unsafe")
    if any(part.startswith(".env") or part.endswith(".env") for part in path.parts):
        _refuse(code, f"{field} names protected source state")
    return path.as_posix()


def _reference(value: object, *, field: str, code: str) -> str:
    if not isinstance(value, str) or not value or len(value) > 512 or any(character in value for character in "\x00\r\n"):
        _refuse(code, f"{field} must be a non-empty reference")
    return value


@dataclass(frozen=True)
class SourceAdmissionDescriptor:
    """One closed catalog/receipt descriptor for an admitted logical source."""

    identity: str
    kind: str
    revision: str
    sha256: str
    visibility: str
    selection_default: bool
    path: str

    def record(self) -> dict[str, object]:
        return {
            "identity": self.identity,
            "kind": self.kind,
            "revision": self.revision,
            "sha256": self.sha256,
            "visibility": self.visibility,
            "selection_default": self.selection_default,
            "path": self.path,
        }


@dataclass(frozen=True)
class SourceAdmissionReceipt:
    """One reopened canonical D602 receipt, including its byte identity."""

    operator: str
    command_ref: str
    action_run_id: str
    snapshot_sha256: str
    sources: tuple[SourceAdmissionDescriptor, ...]
    sha256: str
    payload: bytes


@dataclass(frozen=True)
class AdmissionInvocationRequest:
    """The source snapshot that a trusted host callback must bind to its Run."""

    snapshot_sha256: str
    sources: tuple[SourceAdmissionDescriptor, ...]


@dataclass(frozen=True)
class TrustedSourceAdmissionInvocation:
    """Typed host evidence returned only through ``invocation_admitter``.

    This data value is intentionally insufficient on its own: the writer never
    accepts it as a direct argument and always invokes the supplied trusted
    boundary after re-observing the sealed snapshot.
    """

    snapshot_sha256: str
    operator: str
    command_ref: str
    action_run_id: str


@dataclass(frozen=True)
class SourceCatalogAdmission:
    """Reopened result of one retained receipt/catalog publication."""

    snapshot_sha256: str
    receipt: SourceAdmissionReceipt
    receipt_path: Path
    catalog_sha256: str
    catalog_path: Path
    sources: tuple[SourceAdmissionDescriptor, ...]


def _descriptor(value: object, *, code: str) -> SourceAdmissionDescriptor:
    if isinstance(value, SourceAdmissionDescriptor):
        raw = value.record()
    elif isinstance(value, Mapping):
        raw = dict(value)
    else:
        _refuse(code, "receipt source descriptor is not an object")
    if set(raw) != _DESCRIPTOR_KEYS:
        _refuse(code, "receipt source descriptor has an invalid closed schema")
    identity = raw.get("identity")
    kind = raw.get("kind")
    visibility = raw.get("visibility")
    default = raw.get("selection_default")
    if not isinstance(identity, str) or _IDENTITY.fullmatch(identity) is None:
        _refuse(code, "receipt source identity is invalid")
    if not isinstance(kind, str) or kind not in _KINDS:
        _refuse(code, f"receipt source kind is invalid: {identity}")
    if not isinstance(visibility, str) or visibility not in _VISIBILITIES or type(default) is not bool:
        _refuse(code, f"receipt source visibility is invalid: {identity}")
    if visibility == "private" and default:
        _refuse(code, f"private receipt source cannot be a default: {identity}")
    digest = _require_sha256(raw.get("sha256"), field=f"receipt source digest {identity}", code=code)
    revision = _require_immutable_revision(raw.get("revision"), field=f"receipt source revision {identity}", code=code)
    path = _safe_relative(raw.get("path"), field=f"receipt source path {identity}", code=code)
    if kind == "binding" and (default or path != "methodology/bindings"):
        _refuse(code, f"binding receipt source must be non-selectable discovery metadata: {identity}")
    if path in {CATALOG_NAME, ADMISSIONS_DIRECTORY.as_posix()} or path.startswith(f"{ADMISSIONS_DIRECTORY.as_posix()}/"):
        _refuse(code, f"receipt source cannot name admission control state: {identity}")
    return SourceAdmissionDescriptor(identity, kind, revision, digest, visibility, default, path)


def _ordered_descriptors(values: Iterable[object], *, code: str) -> tuple[SourceAdmissionDescriptor, ...]:
    descriptors = tuple(_descriptor(value, code=code) for value in values)
    if not descriptors:
        _refuse(code, "receipt must admit at least one source")
    identities = tuple(descriptor.identity for descriptor in descriptors)
    if len(set(identities)) != len(identities):
        _refuse(code, "receipt source identities must be unique")
    if identities != tuple(sorted(identities)):
        _refuse(code, "receipt source identities must be sorted")
    return descriptors


def source_snapshot_sha256(sources: Iterable[object]) -> str:
    """Return the D602 checksum of an identity-ordered descriptor array."""

    descriptors = _ordered_descriptors(sources, code="source-admission-descriptor-invalid")
    return _sha256(_canonical_json([descriptor.record() for descriptor in descriptors]))


def build_source_admission_receipt(
    *,
    operator: str,
    command_ref: str,
    action_run_id: str,
    sources: Iterable[object],
) -> bytes:
    """Build canonical receipt bytes for already-typed trusted invocation data."""

    descriptors = _ordered_descriptors(sources, code="source-admission-descriptor-invalid")
    document = {
        "schema_version": SCHEMA_VERSION,
        "operation": OPERATION,
        "operator": _reference(operator, field="operator", code="source-admission-receipt-invalid"),
        "command_ref": _reference(command_ref, field="command_ref", code="source-admission-receipt-invalid"),
        "action_run_id": _reference(action_run_id, field="action_run_id", code="source-admission-receipt-invalid"),
        "snapshot_sha256": _sha256(_canonical_json([descriptor.record() for descriptor in descriptors])),
        "sources": [descriptor.record() for descriptor in descriptors],
    }
    return _canonical_json(document)


def _reject_duplicate_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            _refuse("source-admission-receipt-invalid", "receipt contains duplicate object keys")
        result[key] = value
    return result


def _reject_json_constant(value: str) -> object:
    _refuse("source-admission-receipt-invalid", f"receipt contains non-JSON value: {value}")
    raise AssertionError("unreachable")


def read_source_admission_receipt(
    payload: bytes | bytearray | memoryview,
    *,
    expected_sha256: str | None = None,
) -> SourceAdmissionReceipt:
    """Reopen a canonical D602 receipt and optionally bind its byte checksum."""

    if not isinstance(payload, (bytes, bytearray, memoryview)):
        _refuse("source-admission-receipt-invalid", "receipt payload must be bytes")
    raw = bytes(payload)
    if expected_sha256 is not None and _sha256(raw) != _require_sha256(
        expected_sha256,
        field="expected admission receipt",
        code="source-admission-receipt-digest-mismatch",
    ):
        _refuse("source-admission-receipt-digest-mismatch", "receipt bytes differ from their catalog identity")
    try:
        decoded = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_reject_duplicate_pairs,
            parse_constant=_reject_json_constant,
        )
    except SourceCatalogAdmissionError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise SourceCatalogAdmissionError("source-admission-receipt-invalid", "receipt is not valid UTF-8 JSON") from error
    if not isinstance(decoded, dict) or set(decoded) != _RECEIPT_KEYS:
        _refuse("source-admission-receipt-invalid", "receipt has an invalid closed schema")
    if decoded.get("schema_version") != SCHEMA_VERSION or type(decoded.get("schema_version")) is not int:
        _refuse("source-admission-receipt-invalid", "receipt schema version is invalid")
    if decoded.get("operation") != OPERATION:
        _refuse("source-admission-receipt-invalid", "receipt operation is invalid")
    sources = decoded.get("sources")
    if not isinstance(sources, list):
        _refuse("source-admission-receipt-invalid", "receipt sources must be an array")
    descriptors = _ordered_descriptors(sources, code="source-admission-receipt-invalid")
    snapshot_sha256 = _require_sha256(
        decoded.get("snapshot_sha256"),
        field="receipt snapshot",
        code="source-admission-receipt-invalid",
    )
    expected_snapshot = _sha256(_canonical_json([descriptor.record() for descriptor in descriptors]))
    if snapshot_sha256 != expected_snapshot:
        _refuse("source-admission-receipt-snapshot-mismatch", "receipt snapshot does not bind its sources")
    operator = _reference(decoded.get("operator"), field="operator", code="source-admission-receipt-invalid")
    command_ref = _reference(decoded.get("command_ref"), field="command_ref", code="source-admission-receipt-invalid")
    action_run_id = _reference(decoded.get("action_run_id"), field="action_run_id", code="source-admission-receipt-invalid")
    if raw != _canonical_json(decoded):
        _refuse("source-admission-receipt-noncanonical", "receipt bytes are not canonical JSON")
    return SourceAdmissionReceipt(operator, command_ref, action_run_id, snapshot_sha256, descriptors, _sha256(raw), raw)


def render_source_catalog(
    sources: Iterable[object],
    *,
    admission_receipt_sha256: str,
) -> bytes:
    """Render the matching closed catalog with one retained receipt reference."""

    descriptors = _ordered_descriptors(sources, code="source-admission-descriptor-invalid")
    receipt = _require_sha256(
        admission_receipt_sha256,
        field="admission receipt",
        code="source-admission-descriptor-invalid",
    )
    lines = ["schema_version = 1", ""]
    for descriptor in descriptors:
        lines.extend(
            [
                f"[source.{descriptor.identity}]",
                f"kind = {json.dumps(descriptor.kind, ensure_ascii=False)}",
                f"revision = {json.dumps(descriptor.revision, ensure_ascii=False)}",
                f"sha256 = {json.dumps(descriptor.sha256, ensure_ascii=False)}",
                f"admission_receipt_sha256 = {json.dumps(receipt, ensure_ascii=False)}",
                f"visibility = {json.dumps(descriptor.visibility, ensure_ascii=False)}",
                f"selection_default = {'true' if descriptor.selection_default else 'false'}",
                f"path = {json.dumps(descriptor.path, ensure_ascii=False)}",
                "",
            ]
        )
    return "\n".join(lines).encode("utf-8")


def _snapshot_api() -> tuple[type[Any], Callable[[Any], Any]]:
    """Import the shared pre-catalog snapshot only at writer invocation time."""

    try:
        from release_portable_contract import (
            SealedPortableSourceSnapshot,
            revalidate_portable_source_snapshot,
        )
    except ImportError as error:
        raise SourceCatalogAdmissionError(
            "source-admission-snapshot-unavailable",
            "the sealed portable source snapshot API is unavailable",
        ) from error
    return SealedPortableSourceSnapshot, revalidate_portable_source_snapshot


def _snapshot_rows(snapshot: Any) -> tuple[object, ...]:
    for field in ("logical_package_rows", "portable_package_rows", "source_rows"):
        rows = getattr(snapshot, field, None)
        if isinstance(rows, tuple) and rows:
            return rows
    _refuse("source-admission-snapshot-invalid", "sealed source snapshot has no logical package rows")


def _logical_digest(rows: tuple[object, ...], *, resource: str, root: PurePosixPath) -> str:
    values: list[tuple[PurePosixPath, str, int]] = []
    for row in rows:
        if getattr(row, "resource", None) != resource:
            continue
        destination = _safe_relative(
            getattr(row, "destination_path", None),
            field="logical package row destination",
            code="source-admission-snapshot-invalid",
        )
        path = PurePosixPath(destination)
        if path == root or root in path.parents:
            digest = _require_sha256(
                getattr(row, "sha256", None),
                field="logical package row digest",
                code="source-admission-snapshot-invalid",
            )
            mode = getattr(row, "mode", None)
            if type(mode) is not int or not 0 <= mode <= 0o777:
                _refuse("source-admission-snapshot-invalid", "logical package row mode is invalid")
            values.append((path, digest, mode))
    if not values:
        _refuse("source-admission-snapshot-incomplete", f"sealed source snapshot lacks {resource} rows")
    if len({path for path, _digest_value, _mode in values}) != len(values):
        _refuse("source-admission-snapshot-invalid", "logical package rows repeat a destination")
    if len(values) == 1 and values[0][0] == root:
        return values[0][1]
    records = [
        {
            "path": path.relative_to(root).as_posix(),
            "sha256": digest,
            "mode": mode,
        }
        for path, digest, mode in sorted(values, key=lambda item: item[0].as_posix())
    ]
    return _sha256(_canonical_json(records))


def _extension_identity(root: PurePosixPath) -> str:
    """Return one stable lawful catalog identity for an Extension root.

    Extension directory labels are source data, not catalog identifiers: they
    may contain characters that the closed descriptor schema deliberately does
    not permit.  The digest suffix therefore gives every observed physical
    root a stable, collision-free identity without rewriting or interpreting
    that source label.
    """

    return f"extension-{_sha256(root.as_posix().encode('utf-8'))[:24]}"


def _methodology_descriptor_roots(rows: tuple[object, ...]) -> tuple[tuple[str, str, PurePosixPath], ...]:
    """Classify every material Methodology row by its one D561v3 root.

    The sealed snapshot is the only input here.  In particular, no checkout
    directory is reopened to discover absent Extensions or Configuration.
    """

    active = PurePosixPath("methodology/active")
    roots: dict[PurePosixPath, tuple[str, str]] = {}
    for row in rows:
        if getattr(row, "resource", None) != "METHODOLOGY":
            continue
        destination = _safe_relative(
            getattr(row, "destination_path", None),
            field="logical Methodology row destination",
            code="source-admission-snapshot-invalid",
        )
        path = PurePosixPath(destination)
        if not path.is_relative_to(active):
            _refuse("source-admission-snapshot-invalid", "Methodology row is outside methodology/active")
        tail = path.relative_to(active).parts
        if not tail:
            _refuse("source-admission-snapshot-invalid", "Methodology row cannot name the active root")
        if tail[0] == "001_CORE_META_MODEL":
            root = active / "001_CORE_META_MODEL"
            classified = ("core-meta-model", "methodology")
        elif tail[0] == "003_PROJECT_CONFIGURATION":
            root = active / "003_PROJECT_CONFIGURATION"
            classified = ("project-configuration", "configuration")
        elif tail[0] == "002_INSTALLED_EXTENSIONS":
            if len(tail) < 4 or not tail[1] or not tail[2]:
                _refuse(
                    "source-admission-snapshot-invalid",
                    "Extension Methodology row does not name an identity and label revision root",
                )
            root = active / tail[0] / tail[1] / tail[2]
            classified = (_extension_identity(root), "extension")
        else:
            _refuse("source-admission-snapshot-invalid", "Methodology row is outside the governed source topology")
        previous = roots.setdefault(root, classified)
        if previous != classified:  # pragma: no cover - one root has one structural classification.
            _refuse("source-admission-snapshot-invalid", "Methodology root has ambiguous catalog classification")
    if not roots:
        _refuse("source-admission-snapshot-incomplete", "sealed source snapshot lacks METHODOLOGY rows")
    core = active / "001_CORE_META_MODEL"
    if core not in roots:
        _refuse("source-admission-snapshot-incomplete", "sealed source snapshot lacks Core Meta-model Methodology rows")
    return tuple(
        (identity, kind, root)
        for root, (identity, kind) in sorted(roots.items(), key=lambda item: item[1][0])
    )


def _binding_descriptor(snapshot: Any, rows: tuple[object, ...]) -> SourceAdmissionDescriptor | None:
    """Derive the one non-selectable binding descriptor from a frozen frontier.

    Bindings are a package projection, so their catalog identity describes the
    projection root rather than any individual Delivery Atom.  The snapshot
    normally has already been revalidated by the writer, but this helper also
    closes the frontier-to-row cardinality boundary itself: callers cannot
    silently admit an unaccounted projection by invoking descriptor derivation
    directly.
    """

    atoms = getattr(snapshot, "binding_atoms", None)
    if not isinstance(atoms, tuple):
        _refuse("source-admission-snapshot-invalid", "sealed source snapshot has an invalid binding frontier")
    root = PurePosixPath("methodology/bindings")
    binding_rows = tuple(row for row in rows if getattr(row, "resource", None) == "BINDING_PROJECTION")
    if not atoms:
        if binding_rows:
            _refuse(
                "source-admission-snapshot-invalid",
                "sealed source snapshot has binding projections without a frozen frontier",
            )
        return None

    expected_destinations: set[str] = set()
    atom_pairs: set[tuple[str, int]] = set()
    for atom in atoms:
        atom_id = getattr(atom, "atom_id", None)
        version = getattr(atom, "version", None)
        if not isinstance(atom_id, str) or not atom_id or type(version) is not int or version < 1:
            _refuse("source-admission-snapshot-invalid", "frozen binding frontier has an invalid Atom identity")
        _require_sha256(
            getattr(atom, "sha256", None),
            field="frozen binding Atom digest",
            code="source-admission-snapshot-invalid",
        )
        source = _safe_relative(
            getattr(atom, "source_path", None),
            field="frozen binding Atom source path",
            code="source-admission-snapshot-invalid",
        )
        destination = (root / source).as_posix()
        if destination in expected_destinations or (atom_id, version) in atom_pairs:
            _refuse("source-admission-snapshot-invalid", "frozen binding frontier is not canonical")
        expected_destinations.add(destination)
        atom_pairs.add((atom_id, version))

    observed_destinations: set[str] = set()
    for row in binding_rows:
        destination = _safe_relative(
            getattr(row, "destination_path", None),
            field="binding projection destination",
            code="source-admission-snapshot-invalid",
        )
        if destination not in expected_destinations or destination in observed_destinations:
            _refuse(
                "source-admission-snapshot-invalid",
                "binding projections differ from the frozen binding frontier",
            )
        observed_destinations.add(destination)
    if len(binding_rows) != len(atoms) or observed_destinations != expected_destinations:
        _refuse(
            "source-admission-snapshot-invalid",
            "binding projections do not cover the frozen binding frontier",
        )

    digest = _logical_digest(rows, resource="BINDING_PROJECTION", root=root)
    return SourceAdmissionDescriptor(
        "delivery-bindings",
        "binding",
        digest,
        digest,
        "public",
        False,
        root.as_posix(),
    )


def _descriptors_from_snapshot(snapshot: Any) -> tuple[SourceAdmissionDescriptor, ...]:
    rows = _snapshot_rows(snapshot)
    methodology = tuple(
        SourceAdmissionDescriptor(
            identity,
            kind,
            _logical_digest(rows, resource="METHODOLOGY", root=root),
            _logical_digest(rows, resource="METHODOLOGY", root=root),
            "public",
            False,
            root.as_posix(),
        )
        for identity, kind, root in _methodology_descriptor_roots(rows)
    )
    binding = _binding_descriptor(snapshot, rows)
    values = (
        *methodology,
        SourceAdmissionDescriptor(
            "local-core",
            "core",
            _logical_digest(rows, resource="FRAMEWORK_ENGINE", root=PurePosixPath("102_FRAMEWORK_ENGINE")),
            _logical_digest(rows, resource="FRAMEWORK_ENGINE", root=PurePosixPath("102_FRAMEWORK_ENGINE")),
            "public",
            False,
            "102_FRAMEWORK_ENGINE",
        ),
        SourceAdmissionDescriptor(
            "methodology-support",
            "support",
            _logical_digest(rows, resource="METHODOLOGY_SUPPORT", root=PurePosixPath("methodology/support")),
            _logical_digest(rows, resource="METHODOLOGY_SUPPORT", root=PurePosixPath("methodology/support")),
            "public",
            False,
            "methodology/support",
        ),
        *((binding,) if binding is not None else ()),
    )
    return _ordered_descriptors(
        tuple(sorted(values, key=lambda descriptor: descriptor.identity)),
        code="source-admission-snapshot-invalid",
    )


def _project_root(value: Path | str) -> Path:
    try:
        supplied = Path(value)
        if not supplied.is_absolute() or supplied.is_symlink() or not supplied.is_dir() or supplied.resolve(strict=True) != supplied:
            _refuse("source-admission-project-invalid", "project root must be a canonical regular directory")
        return supplied
    except SourceCatalogAdmissionError:
        raise
    except (OSError, TypeError, ValueError) as error:
        raise SourceCatalogAdmissionError("source-admission-project-invalid", "project root is unavailable") from error


def _snapshot_project_root(snapshot: Any) -> Path:
    candidate = getattr(snapshot, "candidate", None)
    value = getattr(candidate, "project_root", None) if candidate is not None else getattr(snapshot, "project_root", None)
    if not isinstance(value, (str, Path)):
        _refuse("source-admission-snapshot-invalid", "sealed source snapshot has no project root")
    return _project_root(value)


def _checked_snapshot(snapshot: object) -> Any:
    snapshot_type, revalidate = _snapshot_api()
    if not isinstance(snapshot, snapshot_type):
        _refuse("source-admission-snapshot-untrusted", "source admission requires a typed sealed portable source snapshot")
    try:
        observed = revalidate(snapshot)
    except Exception as error:
        code = getattr(error, "code", "source-admission-snapshot-stale")
        raise SourceCatalogAdmissionError(str(code), "sealed portable source snapshot is not current") from error
    if observed != snapshot:
        _refuse("source-admission-snapshot-stale", "sealed portable source snapshot changed during revalidation")
    return observed


def _trusted_invocation(
    callback: object,
    request: AdmissionInvocationRequest,
) -> TrustedSourceAdmissionInvocation:
    if not callable(callback):
        _refuse("source-admission-invocation-required", "source admission requires an explicit trusted invocation callback")
    try:
        invocation = callback(request)
    except SourceCatalogAdmissionError:
        raise
    except Exception as error:
        raise SourceCatalogAdmissionError(
            "source-admission-invocation-rejected",
            "trusted source admission callback rejected the request",
        ) from error
    if not isinstance(invocation, TrustedSourceAdmissionInvocation):
        _refuse("source-admission-invocation-untrusted", "source admission callback must return typed invocation evidence")
    if invocation.snapshot_sha256 != request.snapshot_sha256:
        _refuse("source-admission-invocation-mismatch", "invocation evidence binds a different source snapshot")
    return TrustedSourceAdmissionInvocation(
        _require_sha256(
            invocation.snapshot_sha256,
            field="invocation snapshot",
            code="source-admission-invocation-invalid",
        ),
        _reference(invocation.operator, field="invocation operator", code="source-admission-invocation-invalid"),
        _reference(invocation.command_ref, field="invocation command_ref", code="source-admission-invocation-invalid"),
        _reference(invocation.action_run_id, field="invocation action_run_id", code="source-admission-invocation-invalid"),
    )


def _regular_existing(path: Path, *, code: str, label: str) -> bytes | None:
    if not path.exists() and not path.is_symlink():
        return None
    try:
        metadata = os.lstat(path)
    except OSError as error:
        raise SourceCatalogAdmissionError(code, f"{label} cannot be inspected") from error
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        _refuse(code, f"{label} is not a regular file")
    try:
        return path.read_bytes()
    except OSError as error:
        raise SourceCatalogAdmissionError(code, f"{label} cannot be read") from error


def _existing_matches(path: Path, expected: bytes, *, code: str, label: str) -> bool:
    actual = _regular_existing(path, code=code, label=label)
    if actual is None:
        return False
    if actual != expected:
        _refuse(code, f"existing {label} differs from the admitted request")
    return True


def _ensure_regular_directory(path: Path, *, label: str) -> None:
    if path.exists() or path.is_symlink():
        try:
            metadata = os.lstat(path)
        except OSError as error:
            raise SourceCatalogAdmissionError("source-admission-publish-unsafe", f"{label} cannot be inspected") from error
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
            _refuse("source-admission-publish-unsafe", f"{label} is not a regular directory")
        return
    try:
        path.mkdir(mode=0o755)
    except FileExistsError:
        _ensure_regular_directory(path, label=label)
    except OSError as error:
        raise SourceCatalogAdmissionError("source-admission-publish-failed", f"cannot create {label}") from error


def _publish_exact(directory: Path, name: str, payload: bytes, *, label: str) -> bool:
    """Publish one payload through an exclusive link without overwriting it."""

    target = directory / name
    if _existing_matches(target, payload, code="source-admission-publication-conflict", label=label):
        return False
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{name}.", suffix=".next", dir=directory)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb", closefd=True) as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        try:
            os.link(temporary, target)
        except FileExistsError:
            if not _existing_matches(target, payload, code="source-admission-publication-conflict", label=label):
                _refuse("source-admission-publication-conflict", f"concurrent {label} publication differs")
        except OSError as error:
            raise SourceCatalogAdmissionError("source-admission-publish-failed", f"cannot atomically publish {label}") from error
        return True
    finally:
        try:
            temporary.unlink(missing_ok=True)
        except OSError:
            # The final target, not this disposable private staging file, is
            # the receipt/catalog evidence.  A cleanup failure never claims a
            # second publication or a successful replacement.
            pass


def admit_package_sources(
    project_root: Path | str,
    sealed_source_snapshot: object,
    *,
    invocation_admitter: Callable[[AdmissionInvocationRequest], TrustedSourceAdmissionInvocation],
) -> SourceCatalogAdmission:
    """Explicitly retain one D602 receipt and matching catalog for a snapshot.

    The source snapshot is observed before invocation, invocation is bound to
    the exact descriptor checksum, and the snapshot is re-observed before any
    output effect.  Existing different catalog/receipt bytes refuse; identical
    bytes only reopen and are never overwritten.
    """

    root = _project_root(project_root)
    observed = _checked_snapshot(sealed_source_snapshot)
    if _snapshot_project_root(observed) != root:
        _refuse("source-admission-project-mismatch", "caller project root differs from the sealed source snapshot")
    sources = _descriptors_from_snapshot(observed)
    snapshot = source_snapshot_sha256(sources)
    request = AdmissionInvocationRequest(snapshot, sources)

    # Observe any prior output before asking the host to bind an Action Run.
    # The receipt fields depend on trusted callback evidence, so only a
    # pre-existing catalog can be checked before the callback.
    catalog_path = root / CATALOG_NAME
    existing_catalog = _regular_existing(
        catalog_path,
        code="source-admission-catalog-conflict",
        label="catalog",
    )

    invocation = _trusted_invocation(invocation_admitter, request)
    current = _checked_snapshot(observed)
    current_sources = _descriptors_from_snapshot(current)
    if source_snapshot_sha256(current_sources) != snapshot or current_sources != sources:
        _refuse("source-admission-snapshot-stale", "sealed source snapshot changed before publication")
    receipt_bytes = build_source_admission_receipt(
        operator=invocation.operator,
        command_ref=invocation.command_ref,
        action_run_id=invocation.action_run_id,
        sources=sources,
    )
    receipt = read_source_admission_receipt(receipt_bytes)
    if receipt.snapshot_sha256 != snapshot:
        _refuse("source-admission-receipt-snapshot-mismatch", "receipt does not bind the observed source snapshot")
    catalog_bytes = render_source_catalog(sources, admission_receipt_sha256=receipt.sha256)
    if existing_catalog is not None and existing_catalog != catalog_bytes:
        _refuse("source-admission-catalog-conflict", "existing catalog differs from the admitted request")

    admissions = root.joinpath(*ADMISSIONS_DIRECTORY.parts)
    _ensure_regular_directory(admissions, label="admissions directory")
    receipt_path = admissions / f"{receipt.sha256}.json"
    _publish_exact(admissions, receipt_path.name, receipt_bytes, label="admission receipt")
    _publish_exact(root, CATALOG_NAME, catalog_bytes, label="catalog")

    reopened_receipt_bytes = _regular_existing(
        receipt_path,
        code="source-admission-publication-invalid",
        label="admission receipt",
    )
    reopened_catalog = _regular_existing(
        catalog_path,
        code="source-admission-publication-invalid",
        label="catalog",
    )
    if reopened_receipt_bytes != receipt_bytes or reopened_catalog != catalog_bytes:
        _refuse("source-admission-publication-invalid", "published admission bytes cannot be reopened")
    reopened = read_source_admission_receipt(reopened_receipt_bytes, expected_sha256=receipt.sha256)
    if reopened != receipt:
        _refuse("source-admission-publication-invalid", "published receipt differs from the admission handoff")
    return SourceCatalogAdmission(snapshot, reopened, receipt_path, _sha256(catalog_bytes), catalog_path, sources)


write_source_catalog_admission = admit_package_sources


__all__ = [
    "ADMISSIONS_DIRECTORY",
    "AdmissionInvocationRequest",
    "CATALOG_NAME",
    "OPERATION",
    "SCHEMA_VERSION",
    "SourceAdmissionDescriptor",
    "SourceAdmissionReceipt",
    "SourceCatalogAdmission",
    "SourceCatalogAdmissionError",
    "TrustedSourceAdmissionInvocation",
    "admit_package_sources",
    "build_source_admission_receipt",
    "read_source_admission_receipt",
    "render_source_catalog",
    "source_snapshot_sha256",
    "write_source_catalog_admission",
]
