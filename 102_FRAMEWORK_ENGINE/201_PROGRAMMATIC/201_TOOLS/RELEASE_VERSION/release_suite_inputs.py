"""Read-only native portable inputs for the shared Release Unit-suite runner.

This adapter does not prepare a package or select a runtime.  It reopens the
portable seal and exposes only source rows the existing Unit runner can copy
into its disposable workspace.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from types import SimpleNamespace
from typing import Literal

from release_compilation import PRIVATE_COMPILED_MANIFEST_NAME
from release_contract import ReleaseContractError, ValidatedCandidate
from release_handoff import CANONICAL_SOURCE_RELATIVE, _revalidate
from release_inventory import ReleaseInventoryError, persistent_regular_files, refuse_secret_path
from release_portable_contract import SealedPortableCandidateCompilation, revalidate_sealed_portable_compilation
from release_test_phases import ReleaseTestPhaseMap, derive_test_phase_map_from_rows


_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_RUN_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
_RUNNER_RESOURCES = frozenset({"FRAMEWORK_ENGINE", "METHODOLOGY", "SKILL"})


@dataclass(frozen=True)
class SealedSourcePath:
    """One regular portable source with a physical path and canonical origin."""

    resource: Literal["FRAMEWORK_ENGINE", "METHODOLOGY", "SKILL"]
    source_path: str
    destination_path: str
    sha256: str
    mode: int
    canonical_origin: str
    origin_kind: Literal["candidate", "engine", "skill_projection", "methodology", "support", "compiled"]


@dataclass(frozen=True)
class PortableSuiteInputs:
    """Reopened portable evidence needed before the shared Unit runner starts."""

    input_schema: Literal["portable-1"]
    candidate: ValidatedCandidate
    compilation: SealedPortableCandidateCompilation
    candidate_run_id: str
    input_manifest_sha256: str
    source_catalog_sha256: str
    framework_version: str
    version_toml_sha256: str
    compiled_root: str
    source_paths: tuple[SealedSourcePath, ...]
    phase_map: ReleaseTestPhaseMap


def _error(code: str, message: str) -> ReleaseContractError:
    return ReleaseContractError(code, message)


def _relative(value: object, *, field: str) -> Path:
    if not isinstance(value, str) or not value or "\\" in value:
        raise _error("release-suite-portable-path-invalid", f"{field} must be a safe relative path")
    path = Path(value)
    if path.is_absolute() or path == Path(".") or any(part in {"", ".", ".."} for part in path.parts):
        raise _error("release-suite-portable-path-invalid", f"{field} must be a safe relative path")
    try:
        refuse_secret_path(path)
    except ReleaseInventoryError as error:
        raise _error(error.code, str(error)) from error
    return path


def _regular(root: Path, relative: Path) -> tuple[bytes, int]:
    cursor = root
    for part in relative.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise _error("release-suite-portable-source-symlink", f"portable source is a symlink: {relative.as_posix()}")
    if not cursor.is_file():
        raise _error("release-suite-portable-source-missing", f"portable source is missing: {relative.as_posix()}")
    try:
        cursor.resolve(strict=True).relative_to(root)
        return cursor.read_bytes(), cursor.stat().st_mode & 0o777
    except (OSError, ValueError) as error:
        raise _error("release-suite-portable-source-missing", f"portable source is unavailable: {relative.as_posix()}") from error


def _checked_row(
    root: Path,
    *,
    resource: str,
    source_path: str,
    destination_path: str,
    sha256: str,
    mode: int,
    canonical_origin: str,
    origin_kind: Literal["candidate", "engine", "skill_projection", "methodology", "support", "compiled"],
) -> SealedSourcePath:
    if resource not in _RUNNER_RESOURCES:
        raise _error("release-suite-portable-row-invalid", "portable Unit row has an unsupported resource")
    source = _relative(source_path, field="portable source path")
    destination = _relative(destination_path, field="portable destination path")
    origin = _relative(canonical_origin, field="portable canonical origin")
    if not isinstance(sha256, str) or _SHA256.fullmatch(sha256) is None or type(mode) is not int or not 0 <= mode <= 0o777:
        raise _error("release-suite-portable-row-invalid", "portable Unit row has invalid evidence")
    payload, actual_mode = _regular(root, source)
    if hashlib.sha256(payload).hexdigest() != sha256 or actual_mode != mode:
        raise _error("release-suite-portable-stale", f"portable Unit source changed: {source.as_posix()}")
    return SealedSourcePath(resource, source.as_posix(), destination.as_posix(), sha256, mode, origin.as_posix(), origin_kind)


def _suite_source_precedence(
    prior: SealedSourcePath,
    row: SealedSourcePath,
) -> SealedSourcePath | None:
    """Name the only intentional multi-destination source projections.

    A candidate inventory carries the Unit runner's legacy coverage layout
    (``FRAMEWORK_ENGINE/...``), whereas a portable package retains the native
    package path (``102_FRAMEWORK_ENGINE/...``).  They can name the same
    physical file but must not become two Unit source modules.  The ca source
    has the converse deliberate projection: the Unit runner needs its
    ``SKILLS/ca`` destination, even though the full engine tree also carries
    its original path.  All other duplicate physical sources are evidence
    conflicts rather than a general deduplication rule.
    """

    pair = {prior.origin_kind, row.origin_kind}
    values = (prior, row)
    if pair == {"candidate", "engine"} and all(value.resource == "FRAMEWORK_ENGINE" for value in values):
        return next(value for value in values if value.origin_kind == "candidate")
    if pair == {"engine", "skill_projection"}:
        return next(value for value in values if value.origin_kind == "skill_projection")
    if (
        len(pair) == 2
        and "candidate" in pair
        and pair <= {"candidate", "methodology", "support"}
        and all(value.resource == "METHODOLOGY" for value in values)
    ):
        return next(value for value in values if value.origin_kind == "candidate")
    return None


def _add(rows: dict[str, SealedSourcePath], row: SealedSourcePath) -> None:
    prior = rows.get(row.source_path)
    if prior is None:
        rows[row.source_path] = row
    elif prior.sha256 != row.sha256 or prior.mode != row.mode:
        raise _error("release-suite-portable-row-conflict", "portable source has conflicting sealed evidence")
    elif (prior.resource == row.resource and prior.destination_path == row.destination_path
          and prior.origin_kind == row.origin_kind):
        return
    else:
        selected = _suite_source_precedence(prior, row)
        if selected is None:
            raise _error("release-suite-portable-row-conflict", "portable source has conflicting typed origins")
        rows[row.source_path] = selected


def _portable_origin(compilation: SealedPortableCandidateCompilation, source_path: str, resource: str) -> str:
    source = _relative(source_path, field="portable row source path")
    if resource not in {"METHODOLOGY", "METHODOLOGY_SUPPORT"}:
        return source.as_posix()
    export_root = _relative(compilation.private_compilation.methodology_export.source_export_root, field="portable export root")
    try:
        return (Path(CANONICAL_SOURCE_RELATIVE) / source.relative_to(export_root)).as_posix()
    except ValueError as error:
        raise _error("release-suite-portable-origin-invalid", "portable Methodology source is outside the sealed export") from error


def _compiled_rows(root: Path, compilation: SealedPortableCandidateCompilation) -> list[SealedSourcePath]:
    compiled_root = _relative(compilation.private_compilation.compiled_root, field="portable compiled root")
    directory = root / compiled_root
    if directory.is_symlink() or not directory.is_dir():
        raise _error("release-suite-portable-compiled-missing", "sealed portable compilation has no compiled output root")
    try:
        files = persistent_regular_files(root, directory)
    except ReleaseInventoryError as error:
        raise _error(error.code, str(error)) from error
    result: list[SealedSourcePath] = []
    for file in files:
        relative = file.relative_to(root)
        if file.name == PRIVATE_COMPILED_MANIFEST_NAME:
            continue
        payload, mode = _regular(root, relative)
        result.append(
            SealedSourcePath(
                "METHODOLOGY",
                relative.as_posix(),
                (Path("METHODOLOGY/compiled") / file.relative_to(directory)).as_posix(),
                hashlib.sha256(payload).hexdigest(),
                mode,
                relative.as_posix(),
                "compiled",
            )
        )
    if not result:
        raise _error("release-suite-portable-compiled-missing", "sealed portable compilation has no compiled output rows")
    return result


def collect_portable_suite_inputs(
    candidate: ValidatedCandidate,
    compilation: SealedPortableCandidateCompilation,
) -> PortableSuiteInputs:
    """Reopen actual portable sources without preparing a package or gate run."""

    if not isinstance(candidate, ValidatedCandidate) or not isinstance(compilation, SealedPortableCandidateCompilation):
        raise _error("release-suite-handoff-untrusted", "portable Unit suite requires typed candidate and compilation")
    current_candidate = _revalidate(candidate)
    observed = revalidate_sealed_portable_compilation(compilation)
    if observed.candidate != current_candidate:
        raise _error("release-suite-binding-mismatch", "portable compilation belongs to a different candidate")
    if (
        not isinstance(observed.candidate_run_id, str)
        or _RUN_ID.fullmatch(observed.candidate_run_id) is None
        or any(_SHA256.fullmatch(value) is None for value in (observed.input_manifest_sha256, observed.source_catalog_sha256))
        or observed.framework_version != current_candidate.manifest.framework_version
        or observed.version_toml_sha256 != current_candidate.manifest.version_toml_sha256
    ):
        raise _error("release-suite-portable-binding-invalid", "portable compilation has invalid current bindings")
    root = Path(current_candidate.project_root)
    rows: dict[str, SealedSourcePath] = {}

    for inventory in current_candidate.manifest.source_inventory_rows:
        if inventory.resource not in _RUNNER_RESOURCES:
            continue
        _add(rows, _checked_row(
            root,
            resource=inventory.resource,
            source_path=inventory.source_path,
            destination_path=inventory.destination_path,
            sha256=inventory.source_sha256,
            mode=inventory.source_mode,
            canonical_origin=inventory.source_path,
            origin_kind="skill_projection" if inventory.resource == "SKILL" else "candidate",
        ))

    for portable in observed.portable_package_rows:
        resource = portable.resource
        if resource == "METHODOLOGY_SUPPORT":
            resource = "METHODOLOGY"
        if resource not in _RUNNER_RESOURCES:
            continue
        _add(rows, _checked_row(
            root,
            resource=resource,
            source_path=portable.source_path,
            destination_path=portable.destination_path,
            sha256=portable.sha256,
            mode=portable.mode,
            canonical_origin=_portable_origin(observed, portable.source_path, portable.resource),
            origin_kind={
                "FRAMEWORK_ENGINE": "engine",
                "SKILL": "skill_projection",
                "METHODOLOGY": "methodology",
                "METHODOLOGY_SUPPORT": "support",
            }[portable.resource],
        ))

    for compiled in _compiled_rows(root, observed):
        _add(rows, compiled)
    source_paths = tuple(sorted(rows.values(), key=lambda row: (row.source_path, row.destination_path, row.sha256)))
    phase_origins: dict[str, SealedSourcePath] = {}
    for row in source_paths:
        if row.origin_kind == "skill_projection":
            continue
        prior = phase_origins.get(row.canonical_origin)
        if prior is None:
            phase_origins[row.canonical_origin] = row
            continue
        methodology_twin = {prior.origin_kind, row.origin_kind} <= {"candidate", "methodology", "support"}
        if not methodology_twin or prior.sha256 != row.sha256 or prior.mode != row.mode:
            raise _error("release-suite-portable-origin-conflict", "canonical Unit source has conflicting sealed origins")
    try:
        phase_map = derive_test_phase_map_from_rows(
            SimpleNamespace(source_path=row.canonical_origin, sha256=row.sha256)
            for _origin, row in sorted(phase_origins.items())
        )
    except ReleaseContractError:
        raise
    if not phase_map.unit_paths:
        raise _error("release-test-phase-unit-set-invalid", "portable candidate has no Unit test module")
    return PortableSuiteInputs(
        "portable-1",
        current_candidate,
        observed,
        observed.candidate_run_id,
        observed.input_manifest_sha256,
        observed.source_catalog_sha256,
        observed.framework_version,
        observed.version_toml_sha256,
        observed.private_compilation.compiled_root,
        source_paths,
        phase_map,
    )


__all__ = ["PortableSuiteInputs", "SealedSourcePath", "collect_portable_suite_inputs"]
