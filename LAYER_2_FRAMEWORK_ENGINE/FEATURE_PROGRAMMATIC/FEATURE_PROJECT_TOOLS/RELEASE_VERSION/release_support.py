"""Filesystem and package support for the direct local-release runner."""

# CA-R-2785@3
# CA-M-473@3
# CA-D-678@4
# CA-D-704@1

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import tomllib
from collections.abc import Mapping, Sequence
from pathlib import Path, PurePosixPath
from typing import Any

from project_selection import active_selection


class LocalReleaseError(RuntimeError):
    """A pre-effect refusal from the bounded local-release runner."""


_SOURCE_UNITS = ("CORE_META_MODEL", "INSTALLED_EXTENSIONS", "PROJECT_CONFIGURATION")
_DEFAULT_PRODUCT = "LAYER_1_FRAMEWORK_METHODOLOGY"
_DEFAULT_INSTALLED = ".caprmedio_caprmedio/000_CAPRMEDIO_framework"
_PRESERVED_NAMES = frozenset(
    {
        "settings.toml",
        "config.toml",
        "project_settings.toml",
        "caprmedio_framework_settings.toml",
        "operators_registry.toml",
        "operator_registry",
    }
)
_RUN_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\Z")
_ACTIVE_STATUS = re.compile(r"^status:\s*[\"']?Active[\"']?\s*$", re.MULTILINE)
_NON_SOURCE_DIRECTORIES = frozenset({"archive", "archived", "draft", "drafts", "journal", "projection", "_journal", "_projection", ".caprmedio_tmp", "__pycache__"})


def _relative(value: object, *, label: str) -> Path:
    if not isinstance(value, str) or not value or "\x00" in value:
        raise LocalReleaseError(f"local-release-{label}-invalid")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise LocalReleaseError(f"local-release-{label}-invalid")
    return Path(*path.parts)


def _root(value: Path | str) -> Path:
    supplied = Path(value)
    try:
        root = supplied.resolve(strict=True)
    except OSError as error:
        raise LocalReleaseError("local-release-project-root-invalid") from error
    if supplied.is_symlink() or not root.is_dir() or root == Path(root.anchor):
        raise LocalReleaseError("local-release-project-root-invalid")
    return root


def _project_path(root: Path, relative: Path, *, label: str, require_exists: bool = False) -> Path:
    candidate = root / relative
    try:
        resolved = candidate.resolve(strict=require_exists)
        resolved.relative_to(root)
    except (OSError, ValueError) as error:
        raise LocalReleaseError(f"local-release-{label}-unsafe") from error
    current = root
    for component in relative.parts:
        current /= component
        if os.path.lexists(current) and current.is_symlink():
            raise LocalReleaseError(f"local-release-{label}-unsafe")
    return candidate


def _ignored(name: str) -> bool:
    return name == ".DS_Store" or name.startswith(".env") or name.endswith(".env")


def _read_structure(root: Path, config: Mapping[str, Any]) -> tuple[tuple[str, Path], ...]:
    if config:
        raise LocalReleaseError("local-release-structure-config-invalid")
    try:
        selection = active_selection(root)
        rows = selection.structure.get("scope_units")
    except (OSError, RuntimeError, ValueError) as error:
        raise LocalReleaseError("local-release-structure-invalid") from error
    if not isinstance(rows, tuple):
        raise LocalReleaseError("local-release-structure-invalid")
    configured = config.get("source_units", _SOURCE_UNITS)
    if not isinstance(configured, Sequence) or isinstance(configured, (str, bytes)):
        raise LocalReleaseError("local-release-source-units-invalid")
    names = tuple(configured)
    if names != _SOURCE_UNITS:
        raise LocalReleaseError("local-release-source-units-invalid")
    selected: list[tuple[str, Path]] = []
    for name in names:
        matches = [row for row in rows if isinstance(row, Mapping) and row.get("scope_unit_name") == name]
        if len(matches) != 1 or not isinstance(matches[0].get("authority_path"), str):
            raise LocalReleaseError("local-release-source-path-missing")
        source_relative = _relative(matches[0]["authority_path"], label="source-path")
        source = _project_path(root, source_relative, label="source-path", require_exists=True)
        if source.is_symlink() or not source.is_dir():
            raise LocalReleaseError("local-release-source-path-unsafe")
        selected.append((name, source))
    return tuple(selected)


def _walk_regular_files(root: Path, *, excluded_directories: frozenset[str] = frozenset()) -> list[Path]:
    def fail(error: OSError) -> None:
        raise LocalReleaseError("local-release-source-read-failed") from error

    collected: list[Path] = []
    for directory, directories, names in os.walk(root, followlinks=False, onerror=fail):
        base = Path(directory)
        directories[:] = [name for name in directories if not _ignored(name) and name.casefold() not in excluded_directories]
        for name in directories:
            child = base / name
            if child.is_symlink():
                raise LocalReleaseError("local-release-source-link-unsafe")
        for name in names:
            if _ignored(name):
                continue
            child = base / name
            try:
                mode = child.lstat().st_mode
            except OSError as error:
                raise LocalReleaseError("local-release-source-read-failed") from error
            if stat.S_ISLNK(mode) or not stat.S_ISREG(mode):
                raise LocalReleaseError("local-release-source-entry-unsafe")
            collected.append(child)
    return sorted(collected)


def _active_atom(path: Path) -> bool:
    if path.suffix != ".md":
        return False
    try:
        payload = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        raise LocalReleaseError("local-release-source-read-failed") from error
    if not payload.startswith("---\n"):
        return False
    closing = payload.find("\n---\n", len("---\n"))
    return bool(closing >= 0 and _ACTIVE_STATUS.search(payload[len("---\n"):closing]))


def _release_sources(root: Path) -> list[tuple[str, Path, list[Path]]]:
    selected = []
    for name, source in _read_structure(root, {}):
        files = [entry for entry in _walk_regular_files(source, excluded_directories=_NON_SOURCE_DIRECTORIES)
                 if entry.suffix != ".md" or _active_atom(entry)]
        if name == "CORE_META_MODEL" and not files:
            raise LocalReleaseError("local-release-source-empty:CORE_META_MODEL")
        selected.append((name, source, files))
    return selected


def _clear_target(target: Path, *, root: Path, preserve: frozenset[str], label: str) -> None:
    if target == root or target.parent == target:
        raise LocalReleaseError(f"local-release-{label}-unsafe")
    if target.exists():
        if target.is_symlink() or not target.is_dir():
            raise LocalReleaseError(f"local-release-{label}-unsafe")
    else:
        target.mkdir(parents=True, exist_ok=False)
    for child in target.iterdir():
        if child.name in preserve or _ignored(child.name):
            continue
        _clear_owned(child, label=label)


def _clear_owned(path: Path, *, label: str) -> None:
    """Clear one owned entry while retaining ignored descendants unchanged."""

    try:
        mode = path.lstat().st_mode
    except OSError as error:
        raise LocalReleaseError(f"local-release-{label}-unsafe") from error
    if stat.S_ISLNK(mode):
        raise LocalReleaseError(f"local-release-{label}-unsafe")
    if stat.S_ISREG(mode):
        path.unlink()
        return
    if not stat.S_ISDIR(mode):
        raise LocalReleaseError(f"local-release-{label}-unsafe")
    for child in path.iterdir():
        if _ignored(child.name):
            continue
        _clear_owned(child, label=label)
    try:
        path.rmdir()
    except OSError:
        return


def _target(root: Path, relative: Path, *, label: str) -> Path:
    target = _project_path(root, relative, label=label)
    if target == root or target.parent == target or target == root / ".caprmedio_caprmedio":
        raise LocalReleaseError("local-release-target-invalid")
    if target.exists() and (target.is_symlink() or not target.is_dir()):
        raise LocalReleaseError(f"local-release-{label}-unsafe")
    return target


def _copy_tree(source: Path, destination: Path, *, preserve: frozenset[str]) -> None:
    if source.is_symlink() or not source.is_dir() or destination.is_symlink() or not destination.is_dir():
        raise LocalReleaseError("local-release-copy-unsafe")
    for directory, directories, names in os.walk(source, followlinks=False):
        base = Path(directory)
        relative_directory = base.relative_to(source)
        directories[:] = [
            name for name in directories if not _ignored(name) and not (base == source and name in preserve)
        ]
        for name in directories:
            if (base / name).is_symlink():
                raise LocalReleaseError("local-release-copy-unsafe")
        if relative_directory != Path("."):
            target_directory = destination / relative_directory
            if target_directory.exists() and target_directory.is_symlink():
                raise LocalReleaseError("local-release-copy-unsafe")
            target_directory.mkdir(parents=True, exist_ok=True)
            shutil.copystat(base, target_directory, follow_symlinks=False)
        for name in names:
            if _ignored(name):
                continue
            entry = base / name
            if entry.relative_to(source).parts[0] in preserve:
                continue
            try:
                mode = entry.lstat().st_mode
            except OSError as error:
                raise LocalReleaseError("local-release-copy-unsafe") from error
            if stat.S_ISLNK(mode) or not stat.S_ISREG(mode):
                raise LocalReleaseError("local-release-copy-unsafe")
            relative = entry.relative_to(source)
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists() and target.is_symlink():
                raise LocalReleaseError("local-release-copy-unsafe")
            shutil.copy2(entry, target)


def _deploy_bootstrap(root: Path, package: Path) -> None:
    """Refresh only the copied package bootstrap; never execute it."""
    source = package / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/project_mcp_bootstrap.py"
    try:
        mode = source.lstat().st_mode
        if source.is_symlink() or not stat.S_ISREG(mode):
            raise LocalReleaseError("local-release-bootstrap-unavailable")
        spec = importlib.util.spec_from_file_location("release_project_mcp_bootstrap", source)
        if spec is None or spec.loader is None:
            raise LocalReleaseError("local-release-bootstrap-unavailable")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.deploy_project_mcp_bootstrap(root, package)
    except (ImportError, OSError, RuntimeError) as error:
        raise LocalReleaseError("local-release-bootstrap-unavailable") from error


def _file_identity(path: Path) -> tuple[str, int]:
    return hashlib.sha256(path.read_bytes()).hexdigest(), stat.S_IMODE(path.stat().st_mode)


def _verify_package(package: Path, expected: Mapping[str, tuple[str, int]]) -> None:
    actual = {entry.relative_to(package).as_posix(): _file_identity(entry)
              for entry in _walk_regular_files(package)}
    if actual != expected:
        raise LocalReleaseError("local-release-package-verification-failed")


def _generate_tool_registry(package: Path) -> Path:
    script = package / (
        "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/generate_tool_registry.py"
    )
    output = script.with_name("tool_registry.json")
    if not script.is_file() or script.is_symlink():
        raise LocalReleaseError("local-release-tool-registry-unavailable")
    try:
        output.unlink(missing_ok=True)
        result = subprocess.run(
            (sys.executable, str(script), "--package-root", str(package)),
            cwd=package, text=True, capture_output=True, check=False,
        )
    except OSError as error:
        raise LocalReleaseError("local-release-tool-registry-unavailable") from error
    if result.returncode != 0 or not output.is_file() or output.is_symlink():
        raise LocalReleaseError("local-release-tool-registry-generation-failed")
    return output


def _prepare_package(root: Path, product: Path, package: Path) -> dict[str, tuple[str, int]]:
    excluded = frozenset({".git", ".caprmedio_tmp", ".pytest_cache", "__pycache__", ".mypy_cache", ".ruff_cache", ".venv", "node_modules"})
    trees = (
        (root / "LAYER_2_FRAMEWORK_ENGINE", Path("LAYER_2_FRAMEWORK_ENGINE")),
        (product / "SUPERLAYER_1_METHODOLOGY_SOURCES", Path("METHODOLOGY/sources")),
        (product / "applicable_methodology", Path("METHODOLOGY/compiled")),
        (root / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_AGENTIC/FEATURE_SKILLS/ca", Path("SKILLS/ca")),
    )
    sources: list[tuple[Path, Path]] = []
    inventories: list[tuple[Path, list[Path]]] = []
    for source, destination in trees:
        if source.is_symlink() or not source.is_dir():
            raise LocalReleaseError("local-release-package-source-unavailable")
        members = _walk_regular_files(source, excluded_directories=excluded)
        if not members:
            raise LocalReleaseError("local-release-package-source-unavailable")
        inventories.append((source, members))
        (package / destination).mkdir(parents=True, exist_ok=True)
        sources.extend((entry, destination / entry.relative_to(source)) for entry in members)
    for name in ("pyproject.toml", "uv.lock", "version.toml"):
        source = root / name
        if source.is_symlink() or not source.is_file():
            raise LocalReleaseError("local-release-package-source-unavailable")
        sources.append((source, Path(name)))
    expected = {}
    for source, relative in sources:
        expected[relative.as_posix()] = _file_identity(source)
        destination = package / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    for source, members in inventories:
        if _walk_regular_files(source, excluded_directories=excluded) != members:
            raise LocalReleaseError("local-release-package-source-changed")
    for source, relative in sources:
        if _file_identity(source) != expected[relative.as_posix()]:
            raise LocalReleaseError("local-release-package-source-changed")
    registry = _generate_tool_registry(package)
    expected[registry.relative_to(package).as_posix()] = _file_identity(registry)
    for relative in (
        "SKILLS/ca/SKILL.md",
        "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/project_mcp_bootstrap.py",
        "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/docker/start_mcp.py",
        "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/docker/runtime.py",
        "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/generate_tools_catalog.py",
        "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/generate_tool_registry.py",
    ):
        if relative not in expected:
            raise LocalReleaseError("local-release-package-source-unavailable")
    _verify_package(package, expected)
    return expected


def _generate_tools_catalog(root: Path, runtime: Path, endpoint: str | None, runner: Any) -> None:
    script = runtime / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/generate_tools_catalog.py"
    launcher_python = root / ".caprmedio_runtime/launcher-venv/bin/python"
    if not script.is_file() or script.is_symlink() or not launcher_python.is_file():
        raise LocalReleaseError("local-release-tools-catalog-unavailable")
    try:
        result = runner((
            str(launcher_python), str(script),
            "--project-root", str(root), "--mcp-url", endpoint or "",
        ), root)
    except OSError as error:
        raise LocalReleaseError("local-release-tools-catalog-unavailable") from error
    if getattr(result, "returncode", 0) != 0:
        raise LocalReleaseError("local-release-tools-catalog-failed")


def _cleanup_staging(root: Path, staging: Path | None) -> str:
    if staging is None:
        return ""
    try:
        _clear_owned(staging, label="temporary-package")
    except (LocalReleaseError, OSError):
        pass
    return f"Retained temporary staging: `{staging.relative_to(root).as_posix()}`.\n" if os.path.lexists(staging) else ""


def _image_manager(source: Path, temporary: Path | None = None, *, build_provenance: dict[str, str] | None = None):
    docker = Path(__file__).resolve().parents[4] / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/docker"
    if str(docker) not in sys.path:
        sys.path.insert(0, str(docker))
    from runtime_images import ImageManager
    from image_provenance import ImageBuildProvenance
    provenance = ImageBuildProvenance(**build_provenance) if build_provenance is not None else None
    return ImageManager(source, build_temp_root=temporary, build_provenance=provenance)


def _launcher_image(selection) -> str | None:
    """Read only this selected instance's observation; never scan legacy state."""
    try:
        record = _project_path(selection.root, selection.launcher_state.relative_to(selection.root) / "last_launch.json",
                               label="project-launch-state")
        if not record.is_file():
            return None
        payload = json.loads(record.read_text(encoding="utf-8"))
        image = payload.get("image_id") if isinstance(payload, dict) else None
        if (isinstance(payload, dict) and payload.get("project_root") == str(selection.root)
                and payload.get("control_root") == str(selection.control_root)
                and payload.get("project_id") == selection.instance_id
                and isinstance(image, str) and re.fullmatch(r"sha256:[0-9a-f]{64}", image)):
            return image
    except (LocalReleaseError, OSError, UnicodeDecodeError, json.JSONDecodeError):
        pass
    return None


def _read_version(root: Path) -> tuple[Path, str]:
    version_path = _project_path(root, Path("version.toml"), label="version-path", require_exists=True)
    if not version_path.is_file():
        raise LocalReleaseError("local-release-version-invalid")
    try:
        version_text = version_path.read_text(encoding="utf-8")
        version = tomllib.loads(version_text)["framework"]["version"]
    except (OSError, KeyError, TypeError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise LocalReleaseError("local-release-version-invalid") from error
    match = re.fullmatch(r"([0-9]+)\.([0-9]+)\.([0-9]+)(?:\.([0-9]+))?", version) if isinstance(version, str) else None
    if match is None:
        raise LocalReleaseError("local-release-version-invalid")
    next_version = ".".join((*match.groups()[:3], str(int(match.group(4) or "0") + 1)))
    return version_path, version_text.replace(f'"{version}"', f'"{next_version}"', 1)


def _failed_test_output(
    root: Path,
    run_id: str,
    result: Any,
    *,
    log_path: str | None = None,
    named_temporary_file: Any = tempfile.NamedTemporaryFile,
) -> str:
    """Retain complete failed-suite output separately from the bounded report."""
    streams = {name: str(getattr(result, name, "") or "") for name in ("stdout", "stderr")}
    if log_path is not None:
        return f"Complete test output: `{log_path}`\n{streams['stdout'][-8000:]}"
    try:
        temporary = _target(root, Path(".caprmedio_tmp/simple_local_release"), label="test-log")
        temporary.mkdir(parents=True, exist_ok=True)
        with named_temporary_file(
            mode="w", encoding="utf-8", prefix=f"{run_id}-tests-", suffix=".log",
            dir=temporary, delete=False,
        ) as log:
            log.write("\n".join(f"{name}:\n{value}" for name, value in streams.items()))
            location = Path(log.name).relative_to(root).as_posix()
        note = f"Complete test output: `{location}`"
    except (LocalReleaseError, OSError) as error:
        note = f"Complete test output could not be saved ({type(error).__name__})"
    detail = "\n".join(f"{name}:\n{value[-4000:]}" for name, value in streams.items())
    return f"{note}\n{detail}"
