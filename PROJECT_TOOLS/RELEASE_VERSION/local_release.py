"""Direct local replacement workflow for the Project-owned framework release."""

from __future__ import annotations

import importlib.util
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import tomllib
from collections.abc import Callable, Mapping, Sequence
from pathlib import Path, PurePosixPath
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from release_cleanup import cleanup_obsolete_images, cleanup_stopped_containers  # noqa: E402
from release_cleanup_identity import image_labels  # noqa: E402
from release_image_provenance import release_image_provenance  # noqa: E402
from PROJECT_TOOLS.local_release_test_process import run_logged_test_process  # noqa: E402


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


def _deploy_bootstrap(root: Path, package: Path) -> None:
    """Refresh only the copied package bootstrap; never execute it."""
    source = package / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/project_mcp_bootstrap.py"
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


def _prepare_package(root: Path, product: Path, package: Path) -> dict[str, tuple[str, int]]:
    excluded = frozenset({".git", ".caprmedio_tmp", ".pytest_cache", "__pycache__", ".mypy_cache", ".ruff_cache", ".venv"})
    trees = (
        (root / "102_FRAMEWORK_ENGINE", Path("102_FRAMEWORK_ENGINE")),
        (product / "sources", Path("METHODOLOGY/sources")),
        (product / "applicable_methodology", Path("METHODOLOGY/compiled")),
        (root / "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca", Path("SKILLS/ca")),
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
    for relative in (
        "SKILLS/ca/SKILL.md",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/project_mcp_bootstrap.py",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/start_mcp.py",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py",
    ):
        if relative not in expected:
            raise LocalReleaseError("local-release-package-source-unavailable")
    _verify_package(package, expected)
    return expected


def _cleanup_staging(root: Path, staging: Path | None) -> str:
    if staging is None:
        return ""
    try:
        _clear_owned(staging, label="temporary-package")
    except (LocalReleaseError, OSError):
        pass
    return f"Retained temporary staging: `{staging.relative_to(root).as_posix()}`.\n" if os.path.lexists(staging) else ""


def _image_manager(source: Path, temporary: Path | None = None, *, build_provenance: dict[str, str] | None = None):
    docker = Path(__file__).resolve().parents[2] / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker"
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


def _failed_test_output(root: Path, run_id: str, result: Any, *, log_path: str | None = None) -> str:
    """Retain complete failed-suite output separately from the bounded report."""
    streams = {name: str(getattr(result, name, "") or "") for name in ("stdout", "stderr")}
    if log_path is not None:
        return f"Complete test output: `{log_path}`\n{streams['stdout'][-8000:]}"
    try:
        temporary = _target(root, Path(".caprmedio_tmp/simple_local_release"), label="test-log")
        temporary.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(
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


def run_local_release(
    project_root: Path | str,
    *,
    run_id: str,
    runner: Callable[[tuple[str, ...], Path], Any] | None = None,
    test_modules: tuple[str, ...] | None = None,
) -> dict[str, object]:
    """Run the direct local release without candidate selection or recovery state."""

    if not isinstance(run_id, str) or not _RUN_ID.fullmatch(run_id):
        raise LocalReleaseError("local-release-run-id-invalid")
    if test_modules is not None and not isinstance(test_modules, tuple):
        raise LocalReleaseError("local-release-test-modules-invalid")
    if test_modules == ():
        raise LocalReleaseError("local-release-test-modules-empty")
    if test_modules is not None and any(not isinstance(module, str) for module in test_modules):
        raise LocalReleaseError("local-release-test-modules-invalid")
    root = _root(project_root)
    from project_selection import ProjectSelectionError, resolve_project
    try:
        selection = resolve_project(root)
    except ProjectSelectionError as error:
        raise LocalReleaseError("local-release-project-selection-invalid") from error
    cleanup_runner = runner
    default_runner = runner is None
    if runner is None:
        runner = lambda argv, cwd: subprocess.run(argv, cwd=cwd, text=True, capture_output=True, check=False)

    product = _target(root, Path(_DEFAULT_PRODUCT), label="product-root")
    installed = _target(root, Path(_DEFAULT_INSTALLED), label="installed-root")
    package: Path | None = None
    prepared_product: Path | None = None
    staging: Path | None = None
    package_identity: dict[str, tuple[str, int]] = {}
    product_identity: dict[str, tuple[str, int]] = {}
    candidate_image: str | None = None
    candidate_fingerprint: str | None = None
    runtime = _target(root, Path(".caprmedio_runtime/simple_local_release/package"), label="simple-runtime")
    if product == installed:
        raise LocalReleaseError("local-release-target-invalid")

    prior_image = _launcher_image(selection)
    prior_project = selection.instance_id if prior_image is not None else None

    failed_step = "validate_inputs"
    mcp: Any = None
    receipt_path: str | None = None
    test_log_path: str | None = None
    cleanup_note = "No proven superseded Project-owned image identity was available; none was removed."
    cleanup_pending = False
    cleanup = None
    test_scope = "focused" if test_modules is not None else "full"
    selected_test_modules = list(test_modules) if test_modules is not None else None
    test_selection = (
        ", ".join(test_modules) if test_modules is not None else "all discovered modules"
    )
    phases = (
        "validate inputs", "tests", "copy active sources", "compile product", "build package", "prepare candidate image",
        "copy product to installed framework", "install project runtime", "start mcp", "final",
    )
    try:
        for phase in phases:
            print(f"Local release phase START: {phase}", file=sys.stderr, flush=True)
            failed_step = f"git_before_{phase.replace(' ', '_')}"
            sensitive = runner((
                "git", "diff", "--cached", "--name-only", "--", ":(glob)**/.env*", ":(glob)**/*.env",
            ), root)
            if (getattr(sensitive, "returncode", 1) != 0 or not isinstance(getattr(sensitive, "stdout", None), str)
                    or sensitive.stdout.strip()):
                raise LocalReleaseError("local-release-staged-environment-file-or-check-unavailable")
            try:
                result = runner((
                    "git", "add", "-A", "--", ".", ":(exclude,glob)**/.env*", ":(exclude,glob)**/*.env",
                ), root)
            except OSError as error:
                raise LocalReleaseError("local-release-git-failed") from error
            if getattr(result, "returncode", 0) != 0:
                raise LocalReleaseError("local-release-git-failed")
            try:
                result = runner(("git", "diff", "--cached", "--quiet"), root)
            except OSError as error:
                raise LocalReleaseError("local-release-git-failed") from error
            if getattr(result, "returncode", 0) == 1:
                try:
                    result = runner(("git", "commit", "-m", f"chore(release): simple local {phase}"), root)
                except OSError as error:
                    raise LocalReleaseError("local-release-git-failed") from error
                if getattr(result, "returncode", 0) != 0:
                    raise LocalReleaseError("local-release-git-failed")
            elif getattr(result, "returncode", 0) != 0:
                raise LocalReleaseError("local-release-git-failed")
            result = runner(("git", "status", "--porcelain", "--untracked-files=all"), root)
            if (getattr(result, "returncode", 1) != 0 or not isinstance(getattr(result, "stdout", None), str)
                    or result.stdout.strip()):
                raise LocalReleaseError("local-release-worktree-not-clean")

            if phase == "final":
                continue
            if phase == "validate inputs":
                failed_step = "validate_inputs"
                _release_sources(root)
                ca = _target(root, Path(".agents/skills/ca"), label="project-ca")
                for target in (product, installed, runtime, ca):
                    if target.exists():
                        _walk_regular_files(target)
                _read_version(root)
                tools_root = _project_path(
                    root, Path("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS"),
                    label="compiler-path", require_exists=True,
                )
                if not tools_root.is_dir():
                    raise LocalReleaseError("local-release-compiler-unavailable")
                if str(tools_root) not in sys.path:
                    sys.path.insert(0, str(tools_root))
                try:
                    from COMPILE_APPLICABLE_METHODOLOGY.compile_applicable_methodology import (
                        CompileError, MethodologyPaths, compile_report, replace_outputs_atomically, stage_outputs,
                    )
                except ImportError as error:
                    raise LocalReleaseError("local-release-compiler-unavailable") from error
            elif phase == "tests":
                failed_step = "tests"
                argv = (
                    "uv", "run", "--project", str(root), "--locked", "--no-sync", "--python", "3.14",
                    "--managed-python", "--no-env-file", "--all-groups", "python", "-B", "-u",
                    str(Path(__file__).resolve().parents[1] / "run_full_test_suite.py"), "--project-root", str(root),
                )
                if test_modules is not None:
                    argv += tuple(
                        argument
                        for module in test_modules
                        for argument in ("--test-module", module)
                    )
                if default_runner:
                    temporary = _target(root, Path(".caprmedio_tmp/simple_local_release"), label="test-log")
                    temporary.mkdir(parents=True, exist_ok=True)
                    with tempfile.NamedTemporaryFile(
                        mode="w+b", prefix=f"{run_id}-tests-", suffix=".log", dir=temporary, delete=False,
                    ) as log:
                        test_log_path = Path(log.name).relative_to(root).as_posix()
                        print(f"Local release tests; output log: {test_log_path}", file=sys.stderr, flush=True)
                        result = run_logged_test_process(argv, root, log)
                else:
                    try:
                        result = runner(argv, root)
                    except OSError as error:
                        raise LocalReleaseError("local-release-command-unavailable") from error
                if getattr(result, "returncode", 0) != 0:
                    detail = _failed_test_output(root, run_id, result, log_path=test_log_path)
                    raise LocalReleaseError(f"local-release-command-failed: {detail}")
            elif phase == "copy active sources":
                failed_step = "copy_active_sources"
                sources = _release_sources(root)
                version_path, next_version_text = _read_version(root)
                version_path.write_text(next_version_text, encoding="utf-8")
                _clear_target(product, root=root, preserve=_PRESERVED_NAMES, label="product-root")
                product_sources = product / "sources"
                product_sources.mkdir(parents=True, exist_ok=True)
                for _, source, files in sources:
                    target_root = product_sources / source.name
                    target_root.mkdir(parents=True, exist_ok=True)
                    for entry in files:
                        target = target_root / entry.relative_to(source)
                        target.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(entry, target)
            elif phase == "compile product":
                failed_step = "compile_product"
                try:
                    places = MethodologyPaths(
                        source=Path("101_FRAMEWORK_METHODOLOGY/sources"),
                        output=Path("101_FRAMEWORK_METHODOLOGY/applicable_methodology"),
                        control_root=Path(".caprmedio_caprmedio"),
                    )
                    report, candidates, snapshot = compile_report(root, places)
                    if report.get("can_apply") is not True:
                        raise LocalReleaseError("local-release-product-compile-blocked")
                    replace_outputs_atomically(root, stage_outputs(root, candidates, snapshot, places), places)
                except ImportError as error:
                    raise LocalReleaseError("local-release-compiler-unavailable") from error
                except CompileError as error:
                    raise LocalReleaseError("local-release-product-compile-blocked") from error
            elif phase == "copy product to installed framework":
                failed_step = "copy_product_to_installed_framework"
                _verify_package(package, package_identity)
                _verify_package(prepared_product, product_identity)
                _clear_target(installed, root=root, preserve=_PRESERVED_NAMES, label="installed-root")
                _copy_tree(prepared_product, installed, preserve=_PRESERVED_NAMES)
            elif phase == "build package":
                failed_step = "build_package"
                from project_runtime import owned_temporary_root, repository_root
                temporary = _target(root, Path(".caprmedio_tmp/simple_local_release"), label="temporary-package")
                if repository_root(root) != root:
                    raise LocalReleaseError("local-release-temporary-project-mismatch")
                owned_temporary_root(root, "simple_local_release")
                staging = Path(tempfile.mkdtemp(prefix=f"{run_id}-", dir=temporary))
                prepared_product = staging / "framework"
                prepared_product.mkdir()
                product_identity = {
                    entry.relative_to(product).as_posix(): _file_identity(entry)
                    for entry in _walk_regular_files(product)
                    if entry.relative_to(product).parts[0] not in _PRESERVED_NAMES
                }
                _copy_tree(product, prepared_product, preserve=_PRESERVED_NAMES)
                _verify_package(prepared_product, product_identity)
                package = staging / "package"
                package.mkdir()
                package_identity = _prepare_package(root, prepared_product, package)
            elif phase == "prepare candidate image":
                failed_step = "prepare_candidate_image"
                _verify_package(package, package_identity)
                _verify_package(prepared_product, product_identity)
                image_temporary = staging / "image_builds"
                image_temporary.mkdir(mode=0o700)
                manager = _image_manager(
                    package, image_temporary,
                    build_provenance=release_image_provenance(root, selection, cleanup_runner),
                )
                candidate_image = manager.resolve()
                candidate_fingerprint = manager.identity().fingerprint
                if (not isinstance(candidate_image, str) or not re.fullmatch(r"sha256:[0-9a-f]{64}", candidate_image)
                        or not isinstance(candidate_fingerprint, str) or not re.fullmatch(r"[0-9a-f]{64}", candidate_fingerprint)):
                    raise LocalReleaseError("local-release-candidate-image-invalid")
                _verify_package(package, package_identity)
            elif phase == "install project runtime":
                failed_step = "install_project_runtime"
                _verify_package(package, package_identity)
                _clear_target(runtime, root=root, preserve=frozenset(), label="simple-runtime")
                _copy_tree(package, runtime, preserve=frozenset())
                _verify_package(runtime, package_identity)
                manager = _image_manager(runtime)
                if (manager.resolve(explicit_id=candidate_image, build_if_missing=False) != candidate_image
                        or manager.identity().fingerprint != candidate_fingerprint):
                    raise LocalReleaseError("local-release-installed-image-mismatch")
                ca = _target(root, Path(".agents/skills/ca"), label="project-ca")
                _clear_target(ca, root=root, preserve=frozenset(), label="project-ca")
                _copy_tree(runtime / "SKILLS/ca", ca, preserve=frozenset())
                _deploy_bootstrap(root, runtime)
            else:
                failed_step = "start_mcp"
                launcher = runtime / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py"
                cleanup = cleanup_stopped_containers(
                    root, selection.instance_id, selection.control_relative.as_posix(),
                    candidate_image, candidate_fingerprint, cleanup_runner,
                )
                if prior_image is not None:
                    cleanup.images.add(prior_image)
                if prior_project is not None:
                    try:
                        result = runner((
                            "docker", "ps", "--all", "--filter", f"label=org.caprmedio.project={prior_project}",
                            "--format", "{{.ID}}",
                        ), root)
                    except OSError:
                        result = None
                    identifiers = (
                        [value for value in getattr(result, "stdout", "").splitlines() if re.fullmatch(r"[0-9a-f]{12,64}", value)]
                        if getattr(result, "returncode", 1) == 0 and isinstance(getattr(result, "stdout", ""), str) else []
                    )
                    if getattr(result, "returncode", 1) != 0:
                        cleanup_note = "A prior Project MCP container was retained because discovery was unavailable."
                        cleanup_pending = True
                    elif len(identifiers) > 1:
                        cleanup_note = "Prior Project MCP containers were retained because ownership was ambiguous."
                        cleanup_pending = True
                    elif identifiers and identifiers[0] in cleanup.attempted:
                        cleanup_note = f"Prior container {identifiers[0]} retained after its earlier removal attempt; no retry."
                        cleanup_pending = True
                    elif len(identifiers) == 1:
                        try:
                            inspected = runner((
                                "docker", "container", "inspect", "--format",
                                '{"Image":{{json .Image}},"State":{"Running":{{json .State.Running}}},'
                                '"Config":{"Labels":{{json .Config.Labels}}}}', identifiers[0],
                            ), root)
                            row = json.loads(getattr(inspected, "stdout", ""))
                            labels = row.get("Config", {}).get("Labels") if isinstance(row, dict) else None
                            if (
                                getattr(inspected, "returncode", 1) == 0
                                and isinstance(labels, dict)
                                and labels.get("org.caprmedio.project") == prior_project
                                and labels.get("org.caprmedio.service") == "mcp-http"
                                and labels.get("org.caprmedio.control_root") == ".caprmedio_caprmedio"
                                and labels.get("org.caprmedio.host_project_root") == str(root)
                                and isinstance(row.get("State"), dict)
                                and isinstance(row["State"].get("Running"), bool)
                            ):
                                prior_id = row.get("Image", "")
                                protected = prior_id == candidate_image
                                if protected:
                                    cleanup_note = "Retained the exact candidate Project MCP container for canonical reuse."
                                else:
                                    image_labels(root, cleanup_runner, prior_id)
                                    cleanup.attempted.add(identifiers[0])
                                if row["State"]["Running"] and not protected:
                                    stopped = runner(("docker", "container", "stop", identifiers[0]), root)
                                    if getattr(stopped, "returncode", 1) != 0:
                                        cleanup_note = "The proven prior Project MCP container was retained because stop failed."
                                        cleanup_pending = True
                                if not cleanup_pending and not protected:
                                    removed = runner(("docker", "container", "rm", identifiers[0]), root)
                                    if getattr(removed, "returncode", 1) == 0:
                                        cleanup_note = f"Stopped and removed prior Project MCP container {identifiers[0]} with exact Project labels."
                                    else:
                                        cleanup_note = "A proven prior Project MCP container was retained because removal failed."
                                        cleanup_pending = True
                            else:
                                cleanup_note = "A prior Project MCP container was retained because its exact stopped ownership was not proven."
                                cleanup_pending = True
                        except (OSError, TypeError, ValueError, json.JSONDecodeError):
                            cleanup_note = "A prior Project MCP container was retained because inspection was unavailable."
                            cleanup_pending = True
                try:
                    mcp = runner((
                        "uv", "run", "--project", str(runtime), "--locked", "--no-sync", "--python", "3.14",
                        "--managed-python", "--no-env-file", "--group", "rmed-workflow-mcp", "python", str(launcher),
                        "--project-root", str(root), "--source-root", str(runtime), "--image", candidate_image,
                        "--no-build", "--output", "url", "project-mcp",
                    ), root)
                except OSError as error:
                    raise LocalReleaseError("local-release-command-unavailable") from error
                if getattr(mcp, "returncode", 0) != 0:
                    raise LocalReleaseError("local-release-command-failed")
                current_image = _launcher_image(selection)
                cleanup_stopped_containers(
                    root, selection.instance_id, selection.control_relative.as_posix(),
                    candidate_image, candidate_fingerprint, cleanup_runner, cleanup=cleanup,
                )
                if current_image != candidate_image:
                    cleanup.notes.append("Image cleanup skipped: replacement launcher image was not verified.")
                    cleanup.pending = True
                else:
                    cleanup_obsolete_images(root, candidate_image, candidate_fingerprint, cleanup, cleanup_runner)
                cleanup_pending |= cleanup.pending
                cleanup_note = "\n".join([cleanup_note, *cleanup.notes])
                receipt = _project_path(
                    root, Path(".caprmedio_runtime/simple_local_release/reports") / f"{run_id}.md",
                    label="simple-receipt",
                )
                receipt.parent.mkdir(parents=True, exist_ok=True)
                endpoint = getattr(mcp, "stdout", None)
                staging_note = _cleanup_staging(root, staging)
                staging = None
                receipt.write_text(
                    "# Simple local release receipt\n\n"
                    f"Run: `{run_id}`\n\n"
                    f"Test scope: `{test_scope}`\n\n"
                    f"Selected test modules: {test_selection}\n\n"
                    f"Endpoint: `{endpoint.strip() if isinstance(endpoint, str) else 'not reported'}`\n\n"
                    + (f"Complete test output: `{test_log_path}`\n\n" if test_log_path is not None else "")
                    +
                    f"Image cleanup: {cleanup_note}\n\n{staging_note}",
                    encoding="utf-8",
                )
                receipt_path = receipt.relative_to(root).as_posix()
    except (Exception, KeyboardInterrupt) as error:
        staging_note = _cleanup_staging(root, staging)
        relative = Path(".caprmedio_runtime/simple_local_release/reports") / f"{run_id}.md"
        report_path: str | None = None
        try:
            report = _project_path(root, relative, label="simple-report")
            report.parent.mkdir(parents=True, exist_ok=True)
            report.write_text(
                "# Simple local release failed\n\n"
                f"Run: `{run_id}`\n\nStopped at: `{failed_step}`\n\n"
                f"Test scope: `{test_scope}`\n\n"
                f"Selected test modules: {test_selection}\n\n"
                f"Error class: `{type(error).__name__}`\n\n"
                + (f"{str(error)[:8500]}\n\n" if failed_step == "tests" else "")
                + (f"Complete test output: `{test_log_path}`\n\n" if test_log_path is not None else "")
                + ("\n".join(getattr(error, "__notes__", ())) + "\n\n" if getattr(error, "__notes__", ()) else "")
                +
                "Manual action required: inspect the current project state before any retry.\n\n"
                + ("Docker cleanup:\n" + "\n".join([cleanup_note, *cleanup.notes]) + "\n\n" if cleanup is not None else "")
                +
                f"{staging_note}",
                encoding="utf-8",
            )
            report_path = relative.as_posix()
        except (LocalReleaseError, OSError):
            pass
        return {
            "outcome": "failed",
            "failed_step": failed_step,
            "report_path": report_path,
            "error_type": type(error).__name__,
            "test_log_path": test_log_path,
            "endpoint": None,
            "test_scope": test_scope,
            "test_modules": selected_test_modules,
        }

    endpoint = getattr(mcp, "stdout", None)
    return {
        "outcome": "completed_with_cleanup_pending" if cleanup_pending else "completed",
        "failed_step": None, "report_path": None, "receipt_path": receipt_path,
        "test_log_path": test_log_path,
        "endpoint": endpoint.strip() if isinstance(endpoint, str) else None,
        "test_scope": test_scope,
        "test_modules": selected_test_modules,
    }
