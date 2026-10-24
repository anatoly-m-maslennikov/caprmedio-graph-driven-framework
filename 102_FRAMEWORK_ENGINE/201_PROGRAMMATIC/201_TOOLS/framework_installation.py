"""Shared, non-executable CAPRMEDIO Tool runtime-publication library.

The canonical source is ``102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS`` in the target
repository.  Only the current installed Tool version lives below
``.caprmedio_runtime/tools``; replacement keeps no prior version.  Persistent
configuration and operational state outside that managed Tool surface survive
below ``.caprmedio_runtime``; disposable staging and cache state belongs below
``.caprmedio_tmp``.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import stat
import tempfile
import tomllib
import uuid
from collections.abc import Callable, Mapping, Sequence
from pathlib import Path
from typing import Any

from project_runtime import RUNTIME_DIRECTORY, TEMPORARY_DIRECTORY, atomic_tempfile


SCHEMA_VERSION = 1
PACKAGE = "caprmedio-framework-engine-tools"
SOURCE_DIRECTORY = Path("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS")
TOOLS_RUNTIME_DIRECTORY = RUNTIME_DIRECTORY / "tools"
TEMP_DIRECTORY = TEMPORARY_DIRECTORY
CURRENT_MANIFEST = "current.toml"
RELEASE_MANIFEST = "manifest.toml"
TOOLS_DIRECTORY = "TOOLS"
INSTALL_ENTRYPOINT = "TOOLS/INSTALL_TOOLS/install_tools.py"
TRIGGER_ENTRYPOINT = "TOOLS/COMMIT_TRIGGER/commit_trigger.py"
SERVICE_ENTRYPOINT = "TOOLS/START_BACKGROUND_SERVICES/start_background_services.py"
REQUIRED_FILES = (
    "framework_installation.py",
    "project_runtime.py",
    "atom_operations.py",
    "background_services.toml",
    "INSTALL_TOOLS/install_tools.py",
    "INSTALL_TOOLS/codex_project_context_hook.py",
    "START_BACKGROUND_SERVICES/start_background_services.py",
    "COMMIT_TRIGGER/commit_trigger.py",
    "COMMIT_CONTEXT/commit_context.py",
    "COMMIT_CONTEXT/commit_context_logic.py",
    "APPEND_CHANGE_RECORDS/append_change_records.py",
    "COMMIT_CHANGE_SET/commit_change_set.py",
    "ATOM_SEARCH/atom_search.py",
    "ATOM_READ/atom_read.py",
    "ATOM_CREATE/atom_create.py",
    "ATOM_UPDATE/atom_update.py",
    "ATOM_MOVE/atom_move.py",
    "ATOM_ARCHIVE/atom_archive.py",
    "ATOM_PROMOTE/atom_promote.py",
    "ATOM_UPGRADE/atom_upgrade.py",
    "MIGRATE_ATOM_IDENTITY/migrate_atom_identity.py",
    "REBIND_ATOM_RELATIONS/rebind_atom_relations.py",
    "CLOSE_ATOM/close_atom.py",
    "REPLACE_ATOM/replace_atom.py",
    "caprmedio_relation_types.toml",
    "lifecycle_intents.py",
    "work_journal.py",
)
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
EXCLUDED_DIRECTORY_NAMES = {"__pycache__", "tests"}
EXCLUDED_FILE_NAMES = {".DS_Store", ".gitkeep"}


class InstallationError(RuntimeError):
    """One stable installation or verification failure."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(message)


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value: object) -> str:
    payload = value if isinstance(value, bytes) else canonical_json(value).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def resolve_repository(path: Path | str) -> Path:
    candidate = Path(path).expanduser().resolve()
    for root in (candidate, *candidate.parents):
        if (root / ".git").exists():
            return root
    raise InstallationError("repository-not-found", f"cannot resolve Git repository from {candidate}")


def _quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _atomic_write(path: Path, content: str, *, mode: int | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = atomic_tempfile(path, "install_tools")
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        if mode is not None:
            temporary.chmod(mode)
        os.replace(temporary, path)
    except BaseException:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass
        raise


def _source_files(source_root: Path) -> list[Path]:
    if not source_root.is_dir() or source_root.is_symlink():
        raise InstallationError("canonical-source-missing", f"canonical Tool source is missing: {source_root}")
    paths: list[Path] = []
    for path in source_root.rglob("*"):
        relative = path.relative_to(source_root)
        if any(part in EXCLUDED_DIRECTORY_NAMES for part in relative.parts):
            continue
        if not path.is_file() or path.is_symlink():
            continue
        if path.name in EXCLUDED_FILE_NAMES or path.suffix in {".pyc", ".pyo"}:
            continue
        paths.append(path)
    return sorted(paths, key=lambda item: item.relative_to(source_root).as_posix())


def _distribution_sources(canonical: Path) -> dict[str, Path]:
    docker = canonical.parent / "203_APPS/WORKFLOW_ORCHESTRATOR/docker"
    skill = canonical.parents[2] / "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca"
    return {
        "HOST_RUNTIME/shared_mcp_launcher.py": docker / "shared_mcp_launcher.py",
        "HOST_RUNTIME/shared_mcp_launch_support.py": docker / "shared_mcp_launch_support.py",
        "HOST_RUNTIME/shared-mcp.compose.yaml": docker / "shared-mcp.compose.yaml",
        "SKILLS/ca/SKILL.md": skill / "SKILL.md",
        "SKILLS/ca/agents/openai.yaml": skill / "agents/openai.yaml",
    }


def _distribution_inventory(canonical: Path) -> dict[str, Path]:
    distribution = _distribution_sources(canonical)
    present: dict[str, Path] = {}
    for name, path in distribution.items():
        if not path.exists() and not path.is_symlink():
            continue
        if not path.is_file() or path.is_symlink() or path.resolve() != path:
            raise InstallationError("canonical-source-unsafe", "installer distribution asset is unsafe")
        present[name] = path
    if present and len(present) != len(distribution):
        raise InstallationError("canonical-source-incomplete", "installer distribution assets are incomplete")
    return present


def source_inventory(repository: Path | str, *, source_root: Path | None = None) -> tuple[list[dict[str, Any]], str]:
    root = resolve_repository(repository)
    canonical = (source_root or (root / SOURCE_DIRECTORY)).resolve()
    files = _source_files(canonical)
    available = {path.relative_to(canonical).as_posix() for path in files}
    missing = [relative for relative in REQUIRED_FILES if relative not in available]
    if missing:
        raise InstallationError("canonical-source-incomplete", "canonical Tool source is missing: " + ", ".join(missing))
    sources = {f"{TOOLS_DIRECTORY}/{path.relative_to(canonical).as_posix()}": path for path in files}
    sources.update(_distribution_inventory(canonical))
    rows: list[dict[str, Any]] = []
    for relative, path in sources.items():
        rows.append(
            {
                "path": relative,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "mode": path.stat().st_mode & 0o777,
            }
        )
    rows.sort(key=lambda row: str(row["path"]))
    release = digest({"schema_version": SCHEMA_VERSION, "package": PACKAGE, "files": rows})
    return rows, release


def _inventory_source(canonical: Path, relative: Path) -> Path:
    """Map one verified inventory row back to its canonical source carrier."""
    if relative.parts[:1] == (TOOLS_DIRECTORY,):
        return canonical / relative.relative_to(TOOLS_DIRECTORY)
    distribution = _distribution_sources(canonical)
    if relative.as_posix() in distribution:
        return distribution[relative.as_posix()]
    raise InstallationError("install-manifest-invalid", f"release inventory path is unsupported: {relative.as_posix()}")


def _render_release_manifest(release: str, rows: Sequence[Mapping[str, Any]]) -> str:
    lines = [f"schema_version = {SCHEMA_VERSION}", f"package = {_quoted(PACKAGE)}", f"release = {_quoted(release)}", ""]
    for row in rows:
        lines.extend(
            [
                "[[files]]",
                f"path = {_quoted(str(row['path']))}",
                f"sha256 = {_quoted(str(row['sha256']))}",
                f"mode = {int(row['mode'])}",
                "",
            ]
        )
    return "\n".join(lines)


def _render_current_manifest(release: str) -> str:
    return "\n".join(
        [
            f"schema_version = {SCHEMA_VERSION}",
            f"package = {_quoted(PACKAGE)}",
            f"release = {_quoted(release)}",
            f"tools_root = {_quoted(TOOLS_DIRECTORY)}",
            f"entrypoint = {_quoted(INSTALL_ENTRYPOINT)}",
            "",
        ]
    )


def _safe_manifest_path(value: object, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise InstallationError("install-manifest-invalid", f"{field} must be a non-empty relative path")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or path.as_posix() in {"", "."}:
        raise InstallationError("install-manifest-invalid", f"{field} is unsafe")
    return path.as_posix()


def _read_toml(path: Path, code: str) -> dict[str, Any]:
    try:
        document = tomllib.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise InstallationError(code, f"missing manifest: {path}") from error
    except tomllib.TOMLDecodeError as error:
        raise InstallationError(code, f"invalid TOML: {path}") from error
    if not isinstance(document, dict):
        raise InstallationError(code, f"manifest root must be a table: {path}")
    return document


def installation_status(repository: Path | str) -> dict[str, Any]:
    root = resolve_repository(repository)
    tools_runtime_root = root / TOOLS_RUNTIME_DIRECTORY
    current_path = tools_runtime_root / CURRENT_MANIFEST
    if not current_path.is_file():
        return {"installed": False, "tools_runtime_root": TOOLS_RUNTIME_DIRECTORY.as_posix()}
    current = _read_toml(current_path, "current-manifest-invalid")
    release = current.get("release")
    if current.get("schema_version") != SCHEMA_VERSION or current.get("package") != PACKAGE:
        raise InstallationError("current-manifest-invalid", "installed package identity is invalid")
    if not isinstance(release, str) or not SHA256.fullmatch(release):
        raise InstallationError("current-manifest-invalid", "installed release identity is invalid")
    tools_root_name = _safe_manifest_path(current.get("tools_root"), "tools_root")
    entrypoint_name = _safe_manifest_path(current.get("entrypoint"), "entrypoint")
    release_root = tools_runtime_root / "releases" / release
    manifest = _read_toml(release_root / RELEASE_MANIFEST, "release-manifest-invalid")
    if (
        manifest.get("schema_version") != SCHEMA_VERSION
        or manifest.get("package") != PACKAGE
        or manifest.get("release") != release
    ):
        raise InstallationError("release-manifest-invalid", "installed release manifest identity is invalid")
    raw_rows = manifest.get("files")
    if not isinstance(raw_rows, list) or not raw_rows:
        raise InstallationError("release-manifest-invalid", "installed release has no file inventory")
    rows: list[dict[str, Any]] = []
    for raw in raw_rows:
        if not isinstance(raw, Mapping):
            raise InstallationError("release-manifest-invalid", "installed file row must be a table")
        relative = _safe_manifest_path(raw.get("path"), "files.path")
        expected = raw.get("sha256")
        mode = raw.get("mode")
        if not isinstance(expected, str) or not SHA256.fullmatch(expected) or not isinstance(mode, int):
            raise InstallationError("release-manifest-invalid", f"invalid file metadata: {relative}")
        carrier = release_root / relative
        if not carrier.is_file() or carrier.is_symlink():
            raise InstallationError("installed-file-missing", f"installed file is missing: {relative}")
        actual = hashlib.sha256(carrier.read_bytes()).hexdigest()
        if actual != expected:
            raise InstallationError("installed-file-drift", f"installed file digest differs: {relative}")
        actual_mode = carrier.stat().st_mode & 0o777
        if actual_mode != mode:
            raise InstallationError("installed-file-mode-drift", f"installed file mode differs: {relative}")
        rows.append({"path": relative, "sha256": actual, "mode": mode})
    actual_release = digest({"schema_version": SCHEMA_VERSION, "package": PACKAGE, "files": rows})
    if actual_release != release:
        raise InstallationError("release-digest-mismatch", "installed release digest differs from its identity")
    tools_root = release_root / tools_root_name
    entrypoint = release_root / entrypoint_name
    for required in (tools_root, entrypoint, tools_root / "COMMIT_TRIGGER/commit_trigger.py", tools_root / "START_BACKGROUND_SERVICES/start_background_services.py"):
        if not required.exists():
            raise InstallationError("installed-entrypoint-missing", f"installed entrypoint is missing: {required}")
    return {
        "installed": True,
        "verified": True,
        "release": release,
        "tools_runtime_root": TOOLS_RUNTIME_DIRECTORY.as_posix(),
        "release_root": release_root.relative_to(root).as_posix(),
        "package_root": tools_root.relative_to(root).as_posix(),
        "entrypoint": entrypoint.relative_to(root).as_posix(),
        "file_count": len(rows),
    }


def _managed_tools_surface(root: Path) -> Path:
    """Return the one replaceable legacy Tool-version surface.

    This intentionally excludes every other runtime carrier: in particular,
    target configuration, install-state receipts, Project control, and the
    Work Journal do not belong to a Tool-version replacement.
    """

    return root / TOOLS_RUNTIME_DIRECTORY


def _replacement_surface_is_safe(root: Path, surface: Path) -> None:
    """Refuse aliases and protected names before removing a managed version."""

    runtime = root / RUNTIME_DIRECTORY
    try:
        runtime_stat = runtime.lstat()
    except FileNotFoundError:
        return
    if runtime.is_symlink() or not stat.S_ISDIR(runtime_stat.st_mode):
        raise InstallationError("installed-version-surface-unsafe", "runtime root is not a real directory")
    try:
        surface_stat = surface.lstat()
    except FileNotFoundError:
        return
    if surface.is_symlink() or not stat.S_ISDIR(surface_stat.st_mode):
        raise InstallationError("installed-version-surface-unsafe", "managed Tool surface is not a real directory")

    def walk_error(error: OSError) -> None:
        raise InstallationError("installed-version-surface-unsafe", "managed Tool surface cannot be fully inspected") from error

    for directory, directories, files in os.walk(surface, topdown=True, followlinks=False, onerror=walk_error):
        parent = Path(directory)
        for name in (*directories, *files):
            lowered = name.lower()
            if lowered.startswith(".env") or lowered.endswith(".env"):
                raise InstallationError("installed-version-surface-protected", "managed Tool surface contains a protected env path")
            carrier = parent / name
            try:
                observed = carrier.lstat()
            except FileNotFoundError as error:
                raise InstallationError("installed-version-surface-unsafe", "managed Tool surface changed while checking") from error
            if carrier.is_symlink() or not (stat.S_ISDIR(observed.st_mode) or stat.S_ISREG(observed.st_mode)):
                raise InstallationError("installed-version-surface-unsafe", "managed Tool surface contains an unsafe alias")
            if stat.S_ISREG(observed.st_mode) and observed.st_nlink != 1:
                raise InstallationError("installed-version-surface-unsafe", "managed Tool surface contains an aliased file")


def _verify_staged_release(staging: Path, release: str, rows: Sequence[Mapping[str, Any]]) -> None:
    """Prove that the disposable stage is a complete, exact release tree."""

    expected_manifest = _render_release_manifest(release, rows)
    manifest = staging / RELEASE_MANIFEST
    if not manifest.is_file() or manifest.is_symlink() or manifest.read_text(encoding="utf-8") != expected_manifest:
        raise InstallationError("release-stage-invalid", "staged release manifest differs")
    expected_paths = {RELEASE_MANIFEST, *(str(row["path"]) for row in rows)}
    expected_rows = {str(row["path"]): row for row in rows}
    actual_paths: set[str] = set()
    for carrier in staging.rglob("*"):
        if carrier.name == ".DS_Store":
            continue
        if carrier.is_symlink():
            raise InstallationError("release-stage-invalid", "staged release contains an unsafe carrier")
        if carrier.is_dir():
            continue
        if not carrier.is_file():
            raise InstallationError("release-stage-invalid", "staged release contains an unsafe carrier")
        relative = carrier.relative_to(staging).as_posix()
        actual_paths.add(relative)
        if relative == RELEASE_MANIFEST:
            continue
        expected = expected_rows.get(relative)
        if expected is None or (
            hashlib.sha256(carrier.read_bytes()).hexdigest() != expected["sha256"]
            or carrier.stat().st_mode & 0o777 != expected["mode"]
        ):
            raise InstallationError("release-stage-invalid", f"staged release file differs: {relative}")
    if actual_paths != expected_paths:
        raise InstallationError("release-stage-invalid", "staged release inventory differs")


def _wipe_managed_tools_surface(surface: Path) -> None:
    """Remove managed Tool bytes; a sandbox may retain empty directories only."""

    try:
        shutil.rmtree(surface)
        return
    except OSError:
        pass

    def walk_error(error: OSError) -> None:
        raise InstallationError("installed-version-wipe-failed", "managed Tool surface cannot be fully removed") from error

    for directory, _directories, files in os.walk(surface, topdown=False, followlinks=False, onerror=walk_error):
        for name in files:
            try:
                (Path(directory) / name).unlink()
            except OSError as error:
                raise InstallationError("installed-version-wipe-failed", "managed Tool bytes cannot be removed") from error
    for directory, _directories, files in os.walk(surface, topdown=True, followlinks=False, onerror=walk_error):
        if files:
            raise InstallationError("installed-version-wipe-failed", "managed Tool bytes remain after removal")


def _replace_managed_tools_surface(
    root: Path,
    staging: Path,
    release: str,
    rows: Sequence[Mapping[str, Any]],
    *,
    before_activation: Callable[[], None] | None = None,
) -> None:
    """Wipe only the old Tool version after the replacement stage is verified."""

    surface = _managed_tools_surface(root)
    _replacement_surface_is_safe(root, surface)
    selector = surface / CURRENT_MANIFEST
    try:
        selector_stat = selector.lstat()
    except FileNotFoundError:
        pass
    else:
        if selector.is_symlink() or not stat.S_ISREG(selector_stat.st_mode) or selector_stat.st_nlink != 1:
            raise InstallationError("installed-version-surface-unsafe", "managed Tool selector is unsafe")
        selector.unlink()
    if surface.exists():
        _wipe_managed_tools_surface(surface)

    release_root = surface / "releases" / release
    release_root.parent.mkdir(parents=True, exist_ok=True)
    try:
        shutil.copytree(staging, release_root, dirs_exist_ok=True)
    except OSError as error:
        raise InstallationError("release-promotion-failed", f"cannot promote release: {release}") from error
    _verify_staged_release(release_root, release, rows)
    if before_activation is not None:
        before_activation()
    _atomic_write(surface / CURRENT_MANIFEST, _render_current_manifest(release), mode=0o644)


def install_release(
    repository: Path | str,
    *,
    apply: bool,
    source_root: Path | None = None,
    before_activation: Callable[[Mapping[str, Any]], None] | None = None,
) -> dict[str, Any]:
    root = resolve_repository(repository)
    canonical = (source_root or (root / SOURCE_DIRECTORY)).resolve()
    rows, release = source_inventory(root, source_root=canonical)
    tools_runtime_root = root / TOOLS_RUNTIME_DIRECTORY
    release_root = tools_runtime_root / "releases" / release
    result = {
        "installed": apply,
        "verified": False,
        "release": release,
        "tools_runtime_root": TOOLS_RUNTIME_DIRECTORY.as_posix(),
        "release_root": release_root.relative_to(root).as_posix(),
        "package_root": (release_root / TOOLS_DIRECTORY).relative_to(root).as_posix(),
        "entrypoint": (release_root / INSTALL_ENTRYPOINT).relative_to(root).as_posix(),
        "file_count": len(rows),
        "planned_effect": "replace-managed-installed-tool-version",
    }
    if not apply:
        return result
    staging_root = root / TEMP_DIRECTORY / "install_tools"
    staging_root.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".staging-{uuid.uuid4().hex}-", dir=staging_root))
    try:
        for row in rows:
            relative = Path(str(row["path"]))
            source = _inventory_source(canonical, relative)
            if not source.is_file() or source.is_symlink():
                raise InstallationError("canonical-source-incomplete", f"canonical release source is unavailable: {relative.as_posix()}")
            if (hashlib.sha256(source.read_bytes()).hexdigest() != row["sha256"]
                    or source.stat().st_mode & 0o777 != row["mode"]):
                raise InstallationError("canonical-source-drift", f"canonical release source changed: {relative.as_posix()}")
            target = staging / relative
            if not target.parent.is_dir():
                target.parent.mkdir(parents=True, exist_ok=True)
            try:
                with source.open("rb") as source_handle, target.open("wb") as target_handle:
                    shutil.copyfileobj(source_handle, target_handle)
            except OSError as error:
                raise InstallationError("release-copy-failed", f"cannot copy release file: {relative}") from error
            target.chmod(int(row["mode"]))
            if (hashlib.sha256(target.read_bytes()).hexdigest() != row["sha256"]
                    or target.stat().st_mode & 0o777 != row["mode"]):
                raise InstallationError("release-copy-failed", f"copied release file differs: {relative.as_posix()}")
        _atomic_write(staging / RELEASE_MANIFEST, _render_release_manifest(release, rows), mode=0o644)
        _verify_staged_release(staging, release, rows)
        activation = None if before_activation is None else lambda: before_activation(result)
        _replace_managed_tools_surface(root, staging, release, rows, before_activation=activation)
    finally:
        if staging.exists():
            try:
                shutil.rmtree(staging)
            except PermissionError:
                # Some sandboxed hosts permit file cleanup but prohibit
                # directory removal. Reclaim the disposable bytes and leave
                # only empty cleanup remnants in Project Temporary State.
                for carrier in staging.rglob("*"):
                    if carrier.is_file() or carrier.is_symlink():
                        try:
                            carrier.unlink()
                        except (FileNotFoundError, PermissionError):
                            pass
    return installation_status(root)


__all__ = [
    "InstallationError",
    "PACKAGE",
    "RUNTIME_DIRECTORY",
    "TEMP_DIRECTORY",
    "TOOLS_RUNTIME_DIRECTORY",
    "SCHEMA_VERSION",
    "SERVICE_ENTRYPOINT",
    "SOURCE_DIRECTORY",
    "TRIGGER_ENTRYPOINT",
    "canonical_json",
    "digest",
    "install_release",
    "installation_status",
    "resolve_repository",
    "source_inventory",
]
