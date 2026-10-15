"""Opt-in local export of derived Subject preview candidates, never sources."""

from __future__ import annotations

import hashlib
import os
import stat
import uuid
from pathlib import Path
from typing import Any

import atom_operations as operations
from atom_subject_patch import _IdentityParseCache, _raw_frontmatter, _validate_complete, preview_subject_patches


def stage_subject_preview(root: Path, items: list[object], *, timestamp: str | None = None,
                          subject_profile: str = "legacy", expected_preview_sha256: str | None = None) -> dict[str, Any]:
    root = Path(root).resolve()
    identity_parse_cache = _IdentityParseCache()
    preview = preview_subject_patches(root, items, timestamp=timestamp, subject_profile=subject_profile,
                                      _identity_parse_cache=identity_parse_cache)
    if expected_preview_sha256 is not None and (
            preview["preview_sha256"] != expected_preview_sha256 or timestamp != preview["illustrative_updated_at"]):
        raise operations.ToolError("subject-stage-preview-mismatch", "Staging requires the same reviewed preview seal and illustrative time")
    base = root / ".caprmedio_tmp" / "subject-preview"
    batch: Path | None = None
    artifacts: dict[Path, tuple[int, int]] = {}
    directories: dict[Path, tuple[int, int]] = {}
    candidates: list[tuple[Path, bytes, tuple[int, ...]]] = []
    try:
        parent = operations._raw_revision_parent(root, base / "_", create=True)
        os.close(parent)
        for directory in (root, base.parent, base):
            directories[directory] = _directory_identity(root, directory)
        generated = base / uuid.uuid4().hex
        directories[generated] = _create_directory(root, generated)
        batch = generated
        artifacts[batch] = directories[batch]
        parents = dict(directories)
        manifest_atoms: list[dict[str, Any]] = []
        for ordinal, atom in enumerate(preview["atoms"], start=1):
            _check_directories(root, parents)
            directory = batch / f"{ordinal:04d}"
            directories[directory] = _create_directory(root, directory)
            artifacts[directory] = directories[directory]
            _check_directories(root, {directory: directories[directory]})
            candidate = directory / Path(atom["selector"]).name
            raw = atom["proposed_carrier"].encode("utf-8")
            fingerprint = _write_candidate(root, candidate, raw)
            artifacts[candidate] = fingerprint[:2]
            reopened, observed = operations.read_raw_atom_revision(root, candidate)
            _check_candidate(raw, fingerprint, reopened, observed)
            measured = hashlib.sha256(reopened).hexdigest()
            if measured != atom["after_sha256"]:
                raise operations.ToolError("subject-stage-readback-mismatch", "staged candidate differs from the original preview hash")
            frontmatter, body = _raw_frontmatter(operations, reopened.decode("utf-8"))
            _validate_complete(operations, root, root / atom["selector"], frontmatter, body)
            candidates.append((candidate, raw, fingerprint))
            manifest_atoms.append({
                "source": {"path": atom["selector"], "atom_id": atom["atom_id"],
                           "version": atom["before_version"], "sha256": atom["before_sha256"]},
                "subject_intent_sha256": atom["subject_intent_sha256"],
                "candidate": {"path": candidate.relative_to(root).as_posix(), "sha256": measured},
                "validation": {"state": "passed", "logical_source_path": atom["selector"]},
            })
        final = preview_subject_patches(root, items, timestamp=preview["illustrative_updated_at"],
                                        subject_profile=subject_profile, _identity_parse_cache=identity_parse_cache)
        if final != preview:
            raise operations.ToolError("subject-stage-currentness-mismatch", "source preview changed during staging")
        _check_directories(root, directories)
        for candidate, raw, fingerprint in candidates:
            reopened, observed = operations.read_raw_atom_revision(root, candidate)
            _check_candidate(raw, fingerprint, reopened, observed)
        manifest = {"schema_version": 1, "preview_sha256": preview["preview_sha256"], "atoms": manifest_atoms}
        manifest_raw = operations.canonical_json(manifest).encode("utf-8")
        manifest_path = batch / "manifest.json"
        fingerprint = _write_candidate(root, manifest_path, manifest_raw)
        artifacts[manifest_path] = fingerprint[:2]
        reopened, observed = operations.read_raw_atom_revision(root, manifest_path)
        _check_candidate(manifest_raw, fingerprint, reopened, observed)
        _check_directories(root, directories)
        for candidate, raw, candidate_fingerprint in candidates:
            candidate_raw, candidate_observed = operations.read_raw_atom_revision(root, candidate)
            _check_candidate(raw, candidate_fingerprint, candidate_raw, candidate_observed)
        return {
            "preview": preview, "staging_only": True, "illustrative": True, "sources_unchanged": True,
            "stage_root": batch.relative_to(root).as_posix(),
            "manifest_path": manifest_path.relative_to(root).as_posix(),
            "manifest_sha256": hashlib.sha256(reopened).hexdigest(),
        }
    except (operations.ToolError, OSError, UnicodeError) as error:
        details = dict(getattr(error, "details", None) or {})
        created = details.pop("created_artifact", None)
        if created:
            created_path = root / created["path"]
            artifacts[created_path] = tuple(created["identity"])
            if created_path.parent == base:
                batch = created_path
        attempted = details.pop("attempted_artifact", None)
        if attempted:
            details["unverified_artifacts"] = [{"path": attempted, "state": "unverified"}]
        details.update({"staging_only": True, "stage_root": batch.relative_to(root).as_posix() if batch else None,
                        "retained_artifacts": _retained_artifacts(root, artifacts)})
        raise operations.ToolError(getattr(error, "code", "subject-stage-write-failed"),
                                   getattr(error, "message", str(error)), details) from error


def _directory_identity(root: Path, path: Path) -> tuple[int, int]:
    descriptor = operations._raw_revision_parent(root, path / "_")
    try:
        value = os.fstat(descriptor)
        return value.st_dev, value.st_ino
    finally:
        os.close(descriptor)


def _create_directory(root: Path, path: Path) -> tuple[int, int]:
    parent = operations._raw_revision_parent(root, path)
    made = False
    created = None
    try:
        try:
            os.mkdir(path.name, mode=0o700, dir_fd=parent)
            made = True
        except FileExistsError as error:
            raise operations.ToolError("subject-stage-destination-occupied", "staged directory already exists") from error
        created = os.stat(path.name, dir_fd=parent, follow_symlinks=False)
        identity = _directory_identity(root, path)
        if identity != (created.st_dev, created.st_ino):
            raise operations.ToolError("subject-stage-destination-changed", "staged directory changed during creation")
        return identity
    except Exception as error:
        details = dict(getattr(error, "details", None) or {})
        if made:
            relative = path.relative_to(root).as_posix()
            if created is not None:
                details["created_artifact"] = {"path": relative, "identity": (created.st_dev, created.st_ino)}
            else:
                details["attempted_artifact"] = relative
        raise operations.ToolError(getattr(error, "code", "subject-stage-write-failed"),
                                   getattr(error, "message", "staged directory creation or verification failed"), details) from error
    finally:
        os.close(parent)


def _check_directories(root: Path, directories: dict[Path, tuple[int, int]]) -> None:
    for path, identity in directories.items():
        if _directory_identity(root, path) != identity:
            raise operations.ToolError("subject-stage-destination-changed", "staging directory was substituted")


def _write_candidate(root: Path, path: Path, raw: bytes) -> tuple[int, ...]:
    parent = operations._raw_revision_parent(root, path)
    identity = None
    try:
        try:
            descriptor = os.open(path.name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                                 0o600, dir_fd=parent)
        except FileExistsError as error:
            raise operations.ToolError("subject-stage-destination-occupied", "staged file already exists") from error
        try:
            created = os.fstat(descriptor)
            identity = created.st_dev, created.st_ino
            remaining = memoryview(raw)
            while remaining:
                written = os.write(descriptor, remaining)
                if written == 0:
                    raise OSError("staged write made no progress")
                remaining = remaining[written:]
            os.fsync(descriptor)
            return operations._raw_revision_fingerprint(os.fstat(descriptor))
        finally:
            os.close(descriptor)
    except OSError as error:
        details = {"created_artifact": {"path": path.relative_to(root).as_posix(), "identity": identity}} if identity else None
        raise operations.ToolError("subject-stage-write-failed", "staged file write failed", details) from error
    finally:
        os.close(parent)


def _check_candidate(expected: bytes, fingerprint: tuple[int, ...], raw: bytes, observed: tuple[int, ...]) -> None:
    if fingerprint != observed:
        raise operations.ToolError("subject-stage-destination-changed", "staged file identity changed after creation")
    if raw != expected:
        raise operations.ToolError("subject-stage-readback-mismatch", "staged file bytes differ from the original preview")


def _retained_artifacts(root: Path, paths: dict[Path, tuple[int, int]]) -> list[dict[str, str]]:
    retained: list[dict[str, str]] = []
    for path, identity in paths.items():
        try:
            parent = operations._raw_revision_parent(root, path)
            try:
                value = os.stat(path.name, dir_fd=parent, follow_symlinks=False)
            finally:
                os.close(parent)
            if (value.st_dev, value.st_ino) != identity or not (stat.S_ISREG(value.st_mode) or stat.S_ISDIR(value.st_mode)):
                continue
            reference = {"path": path.relative_to(root).as_posix()}
            if stat.S_ISREG(value.st_mode):
                try:
                    raw, observed = operations.read_raw_atom_revision(root, path)
                    if observed[:2] != identity:
                        continue
                    reference["sha256"] = hashlib.sha256(raw).hexdigest()
                except (operations.ToolError, OSError):
                    pass
            retained.append(reference)
        except (operations.ToolError, OSError):
            continue
    return retained
