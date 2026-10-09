"""Detached D597 candidate-descriptor retention and reopening.

This carrier retains only an already sealed candidate manifest beside immutable
package evidence.  It never reconstructs a live candidate, source admission,
authorization, request intent, gate result, or permission to execute work.
"""

from __future__ import annotations

from dataclasses import dataclass
import errno
import hashlib
import json
import os
from pathlib import Path
import stat
import tempfile
from typing import Mapping

from release_contract import (
    CandidateSnapshotManifest,
    ReleaseContractError,
    ValidatedCandidate,
    canonical_json,
)
from release_inventory import ReleaseInventoryError, refuse_secret_path
from release_portable_contract import SealedPortableCandidateCompilation
from release_portable_package import PreparedPortableReleasePackage
from release_retained_package import (
    RetainedNativePackageEvidence,
    RetainedNativePackageError,
    read_retained_native_package_evidence,
    retain_native_package_evidence,
)


DESCRIPTOR_NAME = "candidate-snapshot.json"
_SHA256 = frozenset("0123456789abcdef")
_MAX_DESCRIPTOR_BYTES = 8 * 1024 * 1024


class RetainedCandidateError(ReleaseContractError):
    """Stable refusal from the detached D597 candidate-descriptor boundary."""


@dataclass(frozen=True)
class RetainedCandidateIdentity:
    """A reopened descriptor plus its independently reopened package evidence."""

    descriptor: CandidateSnapshotManifest
    descriptor_sha256: str
    descriptor_path: Path
    package_evidence: RetainedNativePackageEvidence

    @property
    def candidate_snapshot_manifest_sha256(self) -> str:
        """D566 self-excluding manifest identity; not descriptor raw bytes."""

        return self.descriptor.sha256

    @property
    def framework_version(self) -> str:
        return self.descriptor.framework_version

    @property
    def version_toml_sha256(self) -> str:
        return self.descriptor.version_toml_sha256


def _error(code: str, message: str) -> RetainedCandidateError:
    return RetainedCandidateError(code, message)


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _require_sha256(value: object, *, field: str, code: str) -> str:
    if not isinstance(value, str) or len(value) != 64 or set(value) - _SHA256:
        raise _error(code, f"{field} must be a lowercase SHA-256")
    return value


def _reject_duplicate_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise _error("retained-candidate-descriptor-invalid", "descriptor has duplicate JSON members")
        result[key] = value
    return result


def _reject_json_constant(value: str) -> object:
    raise _error("retained-candidate-descriptor-invalid", f"descriptor has non-JSON constant: {value}")


def _inspect_descriptor_path(path: Path) -> None:
    """Refuse unsafe descriptor paths before opening any descriptor bytes."""

    if not path.is_absolute() or any(part == ".." for part in path.parts):
        raise _error("retained-candidate-descriptor-path-invalid", "descriptor path must be absolute and lexical")
    try:
        refuse_secret_path(path)
    except ReleaseInventoryError as error:
        raise _error(error.code, str(error)) from error
    if path.name != DESCRIPTOR_NAME:
        raise _error("retained-candidate-descriptor-path-invalid", "descriptor path must be candidate-snapshot.json")


def _read_bounded_regular_file(
    path: Path,
    *,
    label: str,
    invalid_code: str,
    unavailable_code: str,
    oversized_code: str,
    missing_ok: bool = False,
) -> bytes | None:
    """Read one bounded regular file by no-follow descriptors, never by path."""

    if not path.is_absolute():
        raise _error(invalid_code, f"{label} path must be absolute")
    required = ("O_NOFOLLOW", "O_DIRECTORY", "O_NONBLOCK")
    if any(not hasattr(os, flag) for flag in required) or not os.supports_dir_fd:
        raise _error(unavailable_code, f"host cannot safely reopen {label}")
    root_fd = parent_fd = file_fd = None
    try:
        root_fd = os.open(path.anchor, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        parent_fd = root_fd
        for part in path.parts[1:-1]:
            try:
                next_fd = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=parent_fd)
            except OSError as error:
                code = invalid_code if error.errno in {errno.ELOOP, errno.ENOTDIR} else unavailable_code
                raise _error(code, f"{label} ancestor cannot be safely reopened") from error
            metadata = os.fstat(next_fd)
            if not stat.S_ISDIR(metadata.st_mode):
                os.close(next_fd)
                raise _error(invalid_code, f"{label} ancestor is not a regular directory")
            if parent_fd != root_fd:
                os.close(parent_fd)
            parent_fd = next_fd
        try:
            file_fd = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent_fd)
        except FileNotFoundError:
            if missing_ok:
                return None
            raise _error(unavailable_code, f"{label} is unavailable") from None
        except OSError as error:
            code = invalid_code if error.errno in {errno.ELOOP, errno.ENOTDIR} else unavailable_code
            raise _error(code, f"{label} cannot be safely reopened") from error
        before = os.fstat(file_fd)
        if not stat.S_ISREG(before.st_mode):
            raise _error(invalid_code, f"{label} must be a regular file")
        if before.st_size > _MAX_DESCRIPTOR_BYTES:
            raise _error(oversized_code, f"{label} exceeds the bounded read")
        chunks: list[bytes] = []
        total = 0
        while total <= _MAX_DESCRIPTOR_BYTES:
            chunk = os.read(file_fd, min(64 * 1024, _MAX_DESCRIPTOR_BYTES + 1 - total))
            if not chunk:
                break
            chunks.append(chunk)
            total += len(chunk)
        if total > _MAX_DESCRIPTOR_BYTES:
            raise _error(oversized_code, f"{label} grew beyond the bounded read")
        after = os.fstat(file_fd)
        try:
            named = os.stat(path.name, dir_fd=parent_fd, follow_symlinks=False)
        except OSError as error:
            raise _error(invalid_code, f"{label} changed while it was read") from error
        if (
            (before.st_dev, before.st_ino, before.st_mode, before.st_size, before.st_mtime_ns)
            != (after.st_dev, after.st_ino, after.st_mode, after.st_size, after.st_mtime_ns)
            or (named.st_dev, named.st_ino, named.st_mode) != (before.st_dev, before.st_ino, before.st_mode)
        ):
            raise _error(invalid_code, f"{label} changed while it was read")
        return b"".join(chunks)
    finally:
        for descriptor in (file_fd, parent_fd, root_fd):
            if descriptor is not None:
                try:
                    os.close(descriptor)
                except OSError:
                    pass


def _inspect_regular_directory_chain(path: Path, *, code: str) -> None:
    if not path.is_absolute():
        raise _error(code, "candidate directory must be absolute")
    for ancestor in reversed((path, *path.parents)):
        try:
            metadata = os.lstat(ancestor)
        except OSError as error:
            raise _error(code, "candidate directory ancestor cannot be inspected") from error
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
            raise _error(code, "candidate directory ancestor is not a regular directory")


def encode_retained_candidate_descriptor(manifest: CandidateSnapshotManifest) -> bytes:
    """Encode one existing D566 manifest as canonical raw descriptor bytes."""

    if not isinstance(manifest, CandidateSnapshotManifest):
        raise _error("retained-candidate-descriptor-untrusted", "descriptor requires a typed candidate manifest")
    try:
        # Re-validating the serialized model verifies the self-excluding D566
        # identity while retaining the sha256 member in the raw descriptor.
        normalized = CandidateSnapshotManifest.model_validate(manifest.model_dump(mode="json", by_alias=True))
        return canonical_json(normalized.model_dump(mode="json", by_alias=True))
    except (TypeError, ValueError) as error:
        raise _error("retained-candidate-descriptor-invalid", "candidate manifest cannot be canonically encoded") from error


def _read_descriptor(path: Path, *, expected_sha256: object) -> tuple[CandidateSnapshotManifest, bytes, str]:
    expected = _require_sha256(
        expected_sha256,
        field="expected descriptor digest",
        code="retained-candidate-descriptor-digest-mismatch",
    )
    _inspect_descriptor_path(path)
    raw = _read_bounded_regular_file(
        path,
        label="descriptor",
        invalid_code="retained-candidate-descriptor-path-invalid",
        unavailable_code="retained-candidate-descriptor-unavailable",
        oversized_code="retained-candidate-descriptor-oversized",
    )
    if raw is None:  # pragma: no cover - descriptor reads never permit absence
        raise _error("retained-candidate-descriptor-unavailable", "descriptor is unavailable")
    raw_sha256 = _sha256(raw)
    if raw_sha256 != expected:
        raise _error("retained-candidate-descriptor-digest-mismatch", "descriptor bytes differ from the expected digest")
    try:
        document = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_reject_duplicate_pairs,
            parse_constant=_reject_json_constant,
        )
    except RetainedCandidateError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise _error("retained-candidate-descriptor-invalid", "descriptor is not valid UTF-8 JSON") from error
    if not isinstance(document, Mapping) or raw != canonical_json(document):
        raise _error("retained-candidate-descriptor-noncanonical", "descriptor bytes are not canonical JSON")
    try:
        manifest = CandidateSnapshotManifest.model_validate(document)
    except (TypeError, ValueError) as error:
        raise _error("retained-candidate-descriptor-invalid", "descriptor does not satisfy the closed candidate schema") from error
    if raw != encode_retained_candidate_descriptor(manifest):
        raise _error("retained-candidate-descriptor-noncanonical", "descriptor differs from normalized candidate bytes")
    if raw_sha256 == manifest.sha256:
        raise _error("retained-candidate-identity-collision", "raw descriptor and self-excluding identities must remain distinct")
    return manifest, raw, raw_sha256


def _reopen_package(
    package_root: Path | str,
    sidecar_path: Path | str,
    expected_sidecar_sha256: object,
) -> RetainedNativePackageEvidence:
    try:
        return read_retained_native_package_evidence(
            package_root,
            sidecar_path,
            expected_sha256=_require_sha256(
                expected_sidecar_sha256,
                field="expected package sidecar digest",
                code="retained-candidate-package-mismatch",
            ),
        )
    except RetainedNativePackageError as error:
        raise _error(error.code, str(error)) from error


def _assert_descriptor_matches_package(
    manifest: CandidateSnapshotManifest,
    package: RetainedNativePackageEvidence,
) -> None:
    view = package.view
    if (
        manifest.sha256 != view.candidate_snapshot_manifest_sha256
        or manifest.framework_version != view.framework_version
        or manifest.version_toml_sha256 != view.version_toml_sha256
    ):
        raise _error(
            "retained-candidate-package-mismatch",
            "descriptor candidate identity differs from the reopened package sidecar",
        )


def read_retained_candidate_identity(
    descriptor_path: Path | str,
    *,
    expected_sha256: str,
    package_root: Path | str,
    sidecar_path: Path | str,
    expected_sidecar_sha256: str,
) -> RetainedCandidateIdentity:
    """Reopen a descriptor beside ``package_evidence/`` without checkout authority."""

    descriptor = Path(descriptor_path)
    sidecar = Path(sidecar_path)
    if descriptor.parent != sidecar.parent.parent:
        raise _error("retained-candidate-descriptor-path-invalid", "descriptor must be beside package evidence")
    manifest, _raw, descriptor_sha256 = _read_descriptor(descriptor, expected_sha256=expected_sha256)
    package = _reopen_package(package_root, sidecar_path, expected_sidecar_sha256)
    _assert_descriptor_matches_package(manifest, package)
    return RetainedCandidateIdentity(manifest, descriptor_sha256, descriptor, package)


def reopen_retained_candidate_identity(identity: RetainedCandidateIdentity) -> RetainedCandidateIdentity:
    """Physically reopen one caller-supplied detached candidate identity.

    A typed identity is only a transport carrier.  Detached consumers must
    reopen both the canonical descriptor and the content-addressed package
    sidecar before treating any of its fields as evidence.
    """

    if not isinstance(identity, RetainedCandidateIdentity):
        raise _error(
            "retained-candidate-identity-untrusted",
            "detached reopening requires a typed retained candidate identity",
        )
    if not isinstance(identity.package_evidence, RetainedNativePackageEvidence):
        raise _error(
            "retained-candidate-identity-untrusted",
            "detached reopening requires typed retained package evidence",
        )
    package = identity.package_evidence
    if (
        not isinstance(package.receipt_path, Path)
        or not isinstance(package.receipt_sha256, str)
        or not isinstance(getattr(package.view, "package_root", None), Path)
    ):
        raise _error(
            "retained-candidate-identity-untrusted",
            "detached reopening requires complete retained package evidence",
        )
    reopened = read_retained_candidate_identity(
        identity.descriptor_path,
        expected_sha256=identity.descriptor_sha256,
        package_root=package.view.package_root,
        sidecar_path=package.receipt_path,
        expected_sidecar_sha256=package.receipt_sha256,
    )
    if reopened != identity:
        raise _error(
            "retained-candidate-identity-mismatch",
            "caller-provided retained candidate identity differs from physical evidence",
        )
    return reopened


def _read_existing_descriptor(path: Path, *, code: str) -> bytes | None:
    return _read_bounded_regular_file(
        path,
        label="descriptor target",
        invalid_code=code,
        unavailable_code=code,
        oversized_code=code,
        missing_ok=True,
    )


def _publish_exact(directory: Path, name: str, payload: bytes) -> None:
    if len(payload) > _MAX_DESCRIPTOR_BYTES:
        raise _error("retained-candidate-descriptor-publish-failed", "descriptor exceeds the bounded write")
    _inspect_regular_directory_chain(directory, code="retained-candidate-descriptor-publish-failed")
    target = directory / name
    existing = _read_existing_descriptor(target, code="retained-candidate-descriptor-publish-failed")
    if existing is not None:
        if existing != payload:
            raise _error("retained-candidate-descriptor-conflict", "existing descriptor differs from the sealed candidate")
        return
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
            if _read_existing_descriptor(target, code="retained-candidate-descriptor-conflict") != payload:
                raise _error("retained-candidate-descriptor-conflict", "concurrent descriptor differs from the sealed candidate")
        except OSError as error:
            raise _error("retained-candidate-descriptor-publish-failed", "descriptor cannot be atomically published") from error
    finally:
        try:
            temporary.unlink(missing_ok=True)
        except OSError:
            pass


def retain_retained_candidate_identity(
    candidate: ValidatedCandidate,
    compilation: SealedPortableCandidateCompilation,
    prepared_package: PreparedPortableReleasePackage,
) -> RetainedCandidateIdentity:
    """Explicitly retain a descriptor after existing package retention revalidation."""

    if not isinstance(candidate, ValidatedCandidate):
        raise _error("retained-candidate-descriptor-untrusted", "retention requires a typed live candidate")
    package = retain_native_package_evidence(candidate, compilation, prepared_package)
    if package.view.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256:
        raise _error("retained-candidate-package-mismatch", "retained package differs from the supplied candidate")
    payload = encode_retained_candidate_descriptor(candidate.manifest)
    descriptor_path = package.receipt_path.parent.parent / DESCRIPTOR_NAME
    _inspect_retention_directory(descriptor_path.parent)
    _publish_exact(descriptor_path.parent, descriptor_path.name, payload)
    return read_retained_candidate_identity(
        descriptor_path,
        expected_sha256=_sha256(payload),
        package_root=package.view.package_root,
        sidecar_path=package.receipt_path,
        expected_sidecar_sha256=package.receipt_sha256,
    )


def _inspect_retention_directory(path: Path) -> None:
    _inspect_regular_directory_chain(path, code="retained-candidate-descriptor-publish-failed")


__all__ = [
    "DESCRIPTOR_NAME",
    "RetainedCandidateError",
    "RetainedCandidateIdentity",
    "encode_retained_candidate_descriptor",
    "read_retained_candidate_identity",
    "reopen_retained_candidate_identity",
    "retain_retained_candidate_identity",
]
