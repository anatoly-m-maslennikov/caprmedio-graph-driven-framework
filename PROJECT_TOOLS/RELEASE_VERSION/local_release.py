"""Minimal local replacement workflow for the Project-owned framework release.

This module deliberately owns only deterministic filesystem transitions.  The
caller supplies the configured compiler, full-test, Git, runtime, MCP, and
Journal integrations as keyword-only callbacks.  It is not a recovery or
authority framework.
"""

from __future__ import annotations

import hashlib
import os
import re
import shutil
import stat
import tomllib
from collections.abc import Callable, Mapping, Sequence
from pathlib import Path, PurePosixPath
from typing import Any, Protocol


class LocalReleaseError(RuntimeError):
    """A pre-effect refusal from the bounded local-release runner."""


_CONTROL_PATH = ".caprmedio_caprmedio/project_structure.toml"
_SOURCE_UNITS = ("CORE_META_MODEL", "INSTALLED_EXTENSIONS", "PROJECT_CONFIGURATION")
_DEFAULT_PRODUCT = "101_FRAMEWORK_METHODOLOGY"
_DEFAULT_INSTALLED = ".caprmedio_caprmedio/000_CAPRMEDIO_framework"
_PRESERVED_NAMES = frozenset(
    {
        "settings.toml",
        "config.toml",
        "project_structure.toml",
        "project_settings.toml",
        "caprmedio_framework_settings.toml",
        "operators_registry.toml",
        "operator_registry",
    }
)
_RUN_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\Z")
_ACTIVE_STATUS = re.compile(r"^status:\s*[\"']?Active[\"']?\s*$", re.MULTILINE)
_NON_SOURCE_DIRECTORIES = frozenset({"archive", "draft", "drafts", "journal", "projection", "_journal", "_projection", ".caprmedio_tmp", "__pycache__"})


class LocalReleaseHooks(Protocol):
    """The integration boundary; every callback is invoked with keywords."""

    def compile(self, *, source_root: Path, output_root: Path, project_root: Path) -> Any: ...
    def test(self, *, project_root: Path, candidate_root: Path) -> Any: ...
    def commit(self, *, project_root: Path, paths: tuple[str, ...], message: str) -> Any: ...
    def install_engine(self, *, project_root: Path, candidate_root: Path) -> Any: ...
    def start_mcp(self, *, project_root: Path) -> Any: ...
    def journal(self, *, event: Mapping[str, Any]) -> Any: ...


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
        if current.exists() and current.is_symlink():
            raise LocalReleaseError(f"local-release-{label}-unsafe")
    return candidate


def _ignored(name: str) -> bool:
    return name == ".DS_Store" or name.startswith(".env") or name.endswith(".env")


def _require_hooks(value: Mapping[str, Callable[..., Any]] | LocalReleaseHooks) -> Mapping[str, Callable[..., Any]]:
    required = ("compile", "test", "commit", "install_engine", "start_mcp", "journal")
    callbacks = {name: (value.get(name) if isinstance(value, Mapping) else getattr(value, name, None)) for name in required}
    absent = [name for name, callback in callbacks.items() if not callable(callback)]
    if absent:
        raise LocalReleaseError("local-release-hooks-invalid:" + ",".join(absent))
    return callbacks


def _read_structure(root: Path, config: Mapping[str, Any]) -> tuple[tuple[str, Path], ...]:
    control_relative = _relative(config.get("project_structure_path", _CONTROL_PATH), label="structure-path")
    control = _project_path(root, control_relative, label="structure-path", require_exists=True)
    if control.is_symlink() or not control.is_file():
        raise LocalReleaseError("local-release-structure-path-unsafe")
    try:
        document = tomllib.loads(control.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise LocalReleaseError("local-release-structure-invalid") from error
    rows = document.get("scope_units")
    if not isinstance(rows, list):
        raise LocalReleaseError("local-release-structure-invalid")
    configured = config.get("source_units", _SOURCE_UNITS)
    if not isinstance(configured, Sequence) or isinstance(configured, (str, bytes)):
        raise LocalReleaseError("local-release-source-units-invalid")
    names = tuple(configured)
    if names != _SOURCE_UNITS:
        raise LocalReleaseError("local-release-source-units-invalid")
    selected: list[tuple[str, Path]] = []
    for name in names:
        matches = [row for row in rows if isinstance(row, dict) and row.get("scope_unit_name") == name]
        if len(matches) != 1 or not isinstance(matches[0].get("authority_path"), str):
            raise LocalReleaseError("local-release-source-path-missing")
        source_relative = _relative(matches[0]["authority_path"], label="source-path")
        source = _project_path(root, source_relative, label="source-path", require_exists=True)
        if source.is_symlink() or not source.is_dir():
            raise LocalReleaseError("local-release-source-path-unsafe")
        selected.append((name, source))
    return tuple(selected)


def _walk_regular_files(root: Path) -> list[Path]:
    collected: list[Path] = []
    for directory, directories, names in os.walk(root, followlinks=False):
        base = Path(directory)
        directories[:] = [name for name in directories if not _ignored(name)]
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
    return collected


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


def _copy_active_sources(sources: tuple[tuple[str, Path], ...], destination: Path) -> int:
    copied = 0
    for name, source in sources:
        target_root = destination / source.name
        target_root.mkdir(parents=True, exist_ok=False)
        unit_copied = 0
        for entry in _walk_regular_files(source):
            if any(part.casefold() in _NON_SOURCE_DIRECTORIES for part in entry.relative_to(source).parts[:-1]):
                continue
            if not _active_atom(entry):
                continue
            target = target_root / entry.relative_to(source)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(entry, target)
            copied += 1
            unit_copied += 1
        if name == "CORE_META_MODEL" and not unit_copied:
            raise LocalReleaseError(f"local-release-source-empty:{name}")
    return copied


def _protected_paths(config: Mapping[str, Any], key: str) -> frozenset[str]:
    value = config.get(key, tuple(sorted(_PRESERVED_NAMES)))
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
        raise LocalReleaseError(f"local-release-{key}-invalid")
    protected: set[str] = set()
    for item in value:
        path = _relative(item, label=key)
        protected.add(path.parts[0])
    return frozenset(protected)


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
        # An ignored descendant deliberately retains its otherwise-empty
        # parent directory.  It is not a failed release transition.
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


def _snapshot(target: Path, *, root: Path, preserve: frozenset[str]) -> dict[str, tuple[int, str]]:
    """Observe owned regular files only; protected and secret paths stay unread."""

    if not target.exists():
        return {}
    observed: dict[str, tuple[int, str]] = {}
    for entry in _walk_regular_files(target):
        relative = entry.relative_to(target)
        if relative.parts[0] in preserve:
            continue
        try:
            payload = entry.read_bytes()
            mode = stat.S_IMODE(entry.stat().st_mode)
        except OSError as error:
            raise LocalReleaseError("local-release-snapshot-failed") from error
        observed[entry.relative_to(root).as_posix()] = (mode, hashlib.sha256(payload).hexdigest())
    return observed


def _compiled_snapshot(root: Path) -> dict[str, str]:
    if root.is_symlink() or not root.is_dir():
        raise LocalReleaseError("local-release-compiled-output-invalid")
    observed: dict[str, str] = {}
    for entry in _walk_regular_files(root):
        try:
            observed[entry.relative_to(root).as_posix()] = hashlib.sha256(entry.read_bytes()).hexdigest()
        except OSError as error:
            raise LocalReleaseError("local-release-compiled-output-invalid") from error
    return observed


def _require_matching_compiled_output(candidate_output: Path, product_output: Path) -> None:
    if _compiled_snapshot(candidate_output) != _compiled_snapshot(product_output):
        raise LocalReleaseError("local-release-compiled-output-mismatch")


def _checkpoint(hooks: Mapping[str, Callable[..., Any]], *, project_root: Path, message: str,
                before: Mapping[str, tuple[int, str]], after: Mapping[str, tuple[int, str]]) -> tuple[str, ...]:
    paths = tuple(sorted(path for path in set(before) | set(after) if before.get(path) != after.get(path)))
    if paths:
        _invoke(hooks, "commit", project_root=project_root, paths=paths, message=message)
    return paths


def _invoke(hooks: Mapping[str, Callable[..., Any]], name: str, **kwargs: Any) -> None:
    result = hooks[name](**kwargs)
    if result is False or (isinstance(result, Mapping) and result.get("passed") is False):
        raise RuntimeError(f"{name} returned false")


def _event(run_id: str, phase: str, outcome: str, **details: Any) -> dict[str, Any]:
    return {"run_id": run_id, "phase": phase, "outcome": outcome, **details}


def run_local_release(project_root: Path | str, *, run_id: str, hooks: Mapping[str, Callable[..., Any]] | LocalReleaseHooks,
                      config: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Run the five local filesystem transitions after private compile and test.

    The ``test`` hook is the configured full test command.  It runs on the
    private candidate before this function clears either target tree.
    """

    if not isinstance(run_id, str) or not _RUN_ID.fullmatch(run_id):
        raise LocalReleaseError("local-release-run-id-invalid")
    if config is None:
        config = {}
    if not isinstance(config, Mapping):
        raise LocalReleaseError("local-release-config-invalid")
    root = _root(project_root)
    callbacks = _require_hooks(hooks)
    sources = _read_structure(root, config)
    product_relative = _relative(config.get("product_root", _DEFAULT_PRODUCT), label="product-root")
    installed_relative = _relative(config.get("installed_root", _DEFAULT_INSTALLED), label="installed-root")
    product_root = _target(root, product_relative, label="product-root")
    installed_root = _target(root, installed_relative, label="installed-root")
    if product_root == installed_root:
        raise LocalReleaseError("local-release-target-invalid")
    product_preserve = _protected_paths(config, "preserve_product_paths")
    installed_preserve = _protected_paths(config, "preserve_installed_paths")
    candidate_root = _project_path(
        root,
        Path(".caprmedio_tmp") / "local_release" / run_id / "candidate",
        label="candidate-root",
    )
    if candidate_root.exists():
        raise LocalReleaseError("local-release-candidate-exists")
    phase = "private_copy"
    try:
        _invoke(callbacks, "journal", event=_event(run_id, phase, "started"))
        candidate_sources = candidate_root / "sources"
        candidate_sources.mkdir(parents=True, exist_ok=False)
        active_atoms = _copy_active_sources(sources, candidate_sources)
        _invoke(callbacks, "journal", event=_event(run_id, phase, "completed", active_atoms=active_atoms))

        phase = "private_compile"
        candidate_output = candidate_root / "applicable_methodology"
        _invoke(callbacks, "compile", source_root=candidate_sources, output_root=candidate_output, project_root=root)
        _invoke(callbacks, "journal", event=_event(run_id, phase, "completed"))

        phase = "full_test"
        _invoke(callbacks, "test", project_root=root, candidate_root=candidate_root)
        _invoke(callbacks, "journal", event=_event(run_id, phase, "completed"))

        phase = "clear_product"
        before = _snapshot(product_root, root=root, preserve=product_preserve)
        _clear_target(product_root, root=root, preserve=product_preserve, label="product-root")
        paths = _checkpoint(callbacks, project_root=root, message=f"local release {run_id}: clear product", before=before,
                            after=_snapshot(product_root, root=root, preserve=product_preserve))
        _invoke(callbacks, "journal", event=_event(run_id, phase, "completed", paths=paths))

        phase = "copy_product_sources"
        before = _snapshot(product_root, root=root, preserve=product_preserve)
        product_sources = product_root / "sources"
        product_sources.mkdir(parents=True, exist_ok=False)
        _copy_tree(candidate_sources, product_sources, preserve=frozenset())
        active_atoms = len(_walk_regular_files(candidate_sources))
        paths = _checkpoint(callbacks, project_root=root, message=f"local release {run_id}: copy active sources", before=before,
                            after=_snapshot(product_root, root=root, preserve=product_preserve))
        _invoke(callbacks, "journal", event=_event(run_id, phase, "completed", active_atoms=active_atoms, paths=paths))

        phase = "compile_product"
        before = _snapshot(product_root, root=root, preserve=product_preserve)
        product_output = product_root / "applicable_methodology"
        _invoke(callbacks, "compile", source_root=product_sources, output_root=product_output, project_root=root)
        _require_matching_compiled_output(candidate_output, product_output)
        paths = _checkpoint(callbacks, project_root=root, message=f"local release {run_id}: compile product", before=before,
                            after=_snapshot(product_root, root=root, preserve=product_preserve))
        _invoke(callbacks, "journal", event=_event(run_id, phase, "completed", paths=paths))

        phase = "clear_installed"
        before = _snapshot(installed_root, root=root, preserve=installed_preserve)
        _clear_target(installed_root, root=root, preserve=installed_preserve, label="installed-root")
        paths = _checkpoint(callbacks, project_root=root, message=f"local release {run_id}: clear installed framework", before=before,
                            after=_snapshot(installed_root, root=root, preserve=installed_preserve))
        _invoke(callbacks, "journal", event=_event(run_id, phase, "completed", paths=paths))

        phase = "copy_installed"
        before = _snapshot(installed_root, root=root, preserve=installed_preserve)
        _copy_tree(product_root, installed_root, preserve=installed_preserve)
        paths = _checkpoint(callbacks, project_root=root, message=f"local release {run_id}: copy product to installed framework", before=before,
                            after=_snapshot(installed_root, root=root, preserve=installed_preserve))
        _invoke(callbacks, "journal", event=_event(run_id, phase, "completed", paths=paths))

        phase = "install_engine"
        _invoke(callbacks, "install_engine", project_root=root, candidate_root=candidate_root)
        _invoke(callbacks, "journal", event=_event(run_id, phase, "completed"))

        phase = "start_mcp"
        _invoke(callbacks, "start_mcp", project_root=root)
        _invoke(callbacks, "journal", event=_event(run_id, phase, "completed"))
    except Exception as error:
        failure = _event(run_id, phase, "failed", error=str(error))
        try:
            _invoke(callbacks, "journal", event=failure)
        except Exception:
            pass
        return {"run_id": run_id, "outcome": "failed", "phase": phase, "error": str(error),
                "candidate_root": str(candidate_root)}
    return {"run_id": run_id, "outcome": "completed", "candidate_root": str(candidate_root),
            "product_root": str(product_root), "installed_root": str(installed_root), "active_atoms": active_atoms}
