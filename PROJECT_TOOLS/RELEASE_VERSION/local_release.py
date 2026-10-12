"""Direct local replacement workflow for the Project-owned framework release."""

from __future__ import annotations

import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tomllib
from collections.abc import Callable, Mapping, Sequence
from pathlib import Path, PurePosixPath
from typing import Any


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
    collected: list[Path] = []
    for directory, directories, names in os.walk(root, followlinks=False):
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


def run_local_release(project_root: Path | str, *, run_id: str,
                      runner: Callable[[tuple[str, ...], Path], Any] | None = None) -> dict[str, object]:
    """Run the direct local release without candidate selection or recovery state."""

    if not isinstance(run_id, str) or not _RUN_ID.fullmatch(run_id):
        raise LocalReleaseError("local-release-run-id-invalid")
    root = _root(project_root)
    if runner is None:
        runner = lambda argv, cwd: subprocess.run(argv, cwd=cwd, text=True, capture_output=True, check=False)

    product = _target(root, Path(_DEFAULT_PRODUCT), label="product-root")
    installed = _target(root, Path(_DEFAULT_INSTALLED), label="installed-root")
    package = _target(root, Path(".caprmedio_install/simple_local_release/package"), label="simple-package")
    runtime = _target(root, Path(".caprmedio_runtime/simple_local_release/package"), label="simple-runtime")
    if product == installed:
        raise LocalReleaseError("local-release-target-invalid")

    prior_image: str | None = None
    prior_project: str | None = None
    state_root = root / ".caprmedio_install/project_mcp"
    try:
        records: list[tuple[str, str]] = []
        if state_root.is_dir() and not state_root.is_symlink():
            for state in state_root.iterdir():
                record = state / "last_launch.json"
                if (not re.fullmatch(r"[0-9a-f]{64}", state.name) or state.is_symlink()
                        or not state.is_dir() or record.is_symlink() or not record.is_file()):
                    continue
                payload = json.loads(record.read_text(encoding="utf-8"))
                image = payload.get("image_id") if isinstance(payload, dict) else None
                if (
                    isinstance(payload, dict)
                    and payload.get("project_root") == str(root)
                    and payload.get("control_root") == str(root / ".caprmedio_caprmedio")
                    and payload.get("project_id") == state.name
                    and isinstance(image, str)
                    and re.fullmatch(r"sha256:[0-9a-f]{64}", image)
                ):
                    records.append((state.name, image))
        if len(records) == 1:
            prior_project, prior_image = records[0]
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        pass

    failed_step = "tests"
    mcp: Any = None
    receipt_path: str | None = None
    cleanup_note = "No proven superseded Project-owned image identity was available; none was removed."
    cleanup_pending = False
    phases = (
        "tests", "copy active sources", "compile product", "copy product to installed framework",
        "build package", "install project runtime", "start mcp", "final",
    )
    try:
        for phase in phases:
            failed_step = f"git_before_{phase.replace(' ', '_')}"
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

            if phase == "final":
                continue
            if phase == "tests":
                failed_step = "tests"
                try:
                    result = runner((
                        "uv", "run", "--project", str(root), "--locked", "--no-sync", "--python", "3.14",
                        "--managed-python", "--no-env-file", "--group", "rmed-workflow-mcp", "--group",
                        "workflow-orchestrator", "python", "-B", "-m", "unittest",
                        "PROJECT_TOOLS/tests/test_simple_local_release.py",
                        "PROJECT_TOOLS/tests/test_simple_public_release.py",
                        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests/test_simple_local_release_route.py",
                    ), root)
                except OSError as error:
                    raise LocalReleaseError("local-release-command-unavailable") from error
                if getattr(result, "returncode", 0) != 0:
                    raise LocalReleaseError("local-release-command-failed")
            elif phase == "copy active sources":
                failed_step = "copy_active_sources"
                version_path = root / "version.toml"
                try:
                    version_text = version_path.read_text(encoding="utf-8")
                    version = tomllib.loads(version_text)["framework"]["version"]
                except (OSError, KeyError, TypeError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
                    raise LocalReleaseError("local-release-version-invalid") from error
                match = re.fullmatch(r"([0-9]+)\.([0-9]+)\.([0-9]+)(?:\.([0-9]+))?", version) if isinstance(version, str) else None
                if match is None:
                    raise LocalReleaseError("local-release-version-invalid")
                next_version = ".".join((*match.groups()[:3], str(int(match.group(4) or "0") + 1)))
                version_path.write_text(version_text.replace(f'"{version}"', f'"{next_version}"', 1), encoding="utf-8")
                _clear_target(product, root=root, preserve=_PRESERVED_NAMES, label="product-root")
                product_sources = product / "sources"
                product_sources.mkdir(parents=True, exist_ok=False)
                for name, source in _read_structure(root, {}):
                    target_root = product_sources / source.name
                    target_root.mkdir(parents=True, exist_ok=False)
                    for entry in _walk_regular_files(source, excluded_directories=_NON_SOURCE_DIRECTORIES):
                        if entry.suffix == ".md" and not _active_atom(entry):
                            continue
                        target = target_root / entry.relative_to(source)
                        target.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(entry, target)
                    if name == "CORE_META_MODEL" and not any(target_root.rglob("*")):
                        raise LocalReleaseError("local-release-source-empty:CORE_META_MODEL")
            elif phase == "compile product":
                failed_step = "compile_product"
                tools_root = root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS"
                if tools_root.is_symlink() or not tools_root.is_dir():
                    raise LocalReleaseError("local-release-compiler-unavailable")
                if str(tools_root) not in sys.path:
                    sys.path.insert(0, str(tools_root))
                try:
                    from COMPILE_APPLICABLE_METHODOLOGY.compile_applicable_methodology import (
                        CompileError, MethodologyPaths, compile_report, replace_outputs_atomically, stage_outputs,
                    )
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
                _clear_target(installed, root=root, preserve=_PRESERVED_NAMES, label="installed-root")
                _copy_tree(product, installed, preserve=_PRESERVED_NAMES)
            elif phase == "build package":
                failed_step = "build_package"
                _clear_target(package, root=root, preserve=frozenset(), label="simple-package")
                for source, destination in (
                    (root / "102_FRAMEWORK_ENGINE", package / "102_FRAMEWORK_ENGINE"),
                    (product / "sources", package / "METHODOLOGY/sources"),
                    (product / "applicable_methodology", package / "METHODOLOGY/compiled"),
                    (root / "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca", package / "SKILLS/ca"),
                ):
                    if source.is_symlink() or not source.is_dir():
                        raise LocalReleaseError("local-release-package-source-unavailable")
                    destination.mkdir(parents=True, exist_ok=False)
                    for entry in _walk_regular_files(source, excluded_directories=frozenset({
                        ".git", ".caprmedio_tmp", ".pytest_cache", "__pycache__", ".mypy_cache", ".ruff_cache", ".venv",
                    })):
                        target = destination / entry.relative_to(source)
                        target.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(entry, target)
                for name in ("pyproject.toml", "uv.lock", "version.toml"):
                    source = root / name
                    if source.is_symlink() or not source.is_file() or _ignored(source.name):
                        raise LocalReleaseError("local-release-package-source-unavailable")
                    shutil.copy2(source, package / name)
            elif phase == "install project runtime":
                failed_step = "install_project_runtime"
                _clear_target(runtime, root=root, preserve=frozenset(), label="simple-runtime")
                _copy_tree(package, runtime, preserve=frozenset())
                ca = _target(root, Path(".agents/skills/ca"), label="project-ca")
                _clear_target(ca, root=root, preserve=frozenset(), label="project-ca")
                _copy_tree(runtime / "SKILLS/ca", ca, preserve=frozenset())
            else:
                failed_step = "start_mcp"
                launcher = runtime / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py"
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
                                if row["State"]["Running"]:
                                    stopped = runner(("docker", "container", "stop", identifiers[0]), root)
                                    if getattr(stopped, "returncode", 1) != 0:
                                        cleanup_note = "The proven prior Project MCP container was retained because stop failed."
                                        cleanup_pending = True
                                if not cleanup_pending:
                                    removed = runner(("docker", "container", "rm", identifiers[0]), root)
                                    if getattr(removed, "returncode", 1) == 0:
                                        cleanup_note = "Stopped and removed one prior Project MCP container with exact Project labels."
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
                        "--project-root", str(root), "--source-root", str(runtime), "--output", "url", "project-mcp",
                    ), root)
                except OSError as error:
                    raise LocalReleaseError("local-release-command-unavailable") from error
                if getattr(mcp, "returncode", 0) != 0:
                    raise LocalReleaseError("local-release-command-failed")
                try:
                    records = []
                    if state_root.is_dir() and not state_root.is_symlink():
                        for state in state_root.iterdir():
                            record = state / "last_launch.json"
                            if (state.is_symlink() or not state.is_dir() or record.is_symlink() or not record.is_file()):
                                continue
                            payload = json.loads(record.read_text(encoding="utf-8"))
                            image = payload.get("image_id") if isinstance(payload, dict) else None
                            if (
                                isinstance(payload, dict)
                                and payload.get("project_root") == str(root)
                                and payload.get("control_root") == str(root / ".caprmedio_caprmedio")
                                and payload.get("project_id") == state.name
                                and isinstance(image, str)
                                and re.fullmatch(r"sha256:[0-9a-f]{64}", image)
                            ):
                                records.append(image)
                    current_image = records[0] if len(records) == 1 else None
                except (OSError, UnicodeDecodeError, json.JSONDecodeError):
                    current_image = None
                if prior_image is not None and current_image is not None and prior_image != current_image:
                    try:
                        result = runner(("docker", "container", "ls", "--all", "--filter", f"ancestor={prior_image}", "--quiet"), root)
                    except OSError:
                        result = None
                    references = (
                        [value for value in getattr(result, "stdout", "").splitlines() if re.fullmatch(r"[0-9a-f]{12,64}", value)]
                        if getattr(result, "returncode", 1) == 0 and isinstance(getattr(result, "stdout", ""), str) else None
                    )
                    if references == []:
                        try:
                            result = runner(("docker", "image", "rm", prior_image), root)
                        except OSError:
                            result = None
                        if getattr(result, "returncode", 1) == 0:
                            cleanup_note = f"Removed the exact prior Project-owned image `{prior_image}` after replacement."
                        else:
                            cleanup_note = "The proven prior Project-owned image was retained because removal failed."
                            cleanup_pending = True
                    else:
                        cleanup_note = "The proven prior Project-owned image was retained because container use was present or unknown."
                        cleanup_pending = True
                elif prior_image is not None and current_image is None:
                    cleanup_note = "The prior Project-owned image was retained because the new launcher state was unavailable."
                    cleanup_pending = True
                receipt = _project_path(
                    root, Path(".caprmedio_runtime/simple_local_release/reports") / f"{run_id}.md",
                    label="simple-receipt",
                )
                receipt.parent.mkdir(parents=True, exist_ok=True)
                endpoint = getattr(mcp, "stdout", None)
                receipt.write_text(
                    "# Simple local release receipt\n\n"
                    f"Run: `{run_id}`\n\n"
                    f"Endpoint: `{endpoint.strip() if isinstance(endpoint, str) else 'not reported'}`\n\n"
                    f"Image cleanup: {cleanup_note}\n",
                    encoding="utf-8",
                )
                receipt_path = receipt.relative_to(root).as_posix()
    except Exception as error:
        relative = Path(".caprmedio_runtime/simple_local_release/reports") / f"{run_id}.md"
        report_path: str | None = None
        try:
            report = _project_path(root, relative, label="simple-report")
            report.parent.mkdir(parents=True, exist_ok=True)
            report.write_text(
                "# Simple local release failed\n\n"
                f"Run: `{run_id}`\n\nStopped at: `{failed_step}`\n\n"
                f"Error class: `{type(error).__name__}`\n\n"
                "Manual action required: inspect the current project state before any retry.\n",
                encoding="utf-8",
            )
            report_path = relative.as_posix()
        except (LocalReleaseError, OSError):
            pass
        return {"outcome": "failed", "failed_step": failed_step, "report_path": report_path, "endpoint": None}

    endpoint = getattr(mcp, "stdout", None)
    return {
        "outcome": "completed_with_cleanup_pending" if cleanup_pending else "completed",
        "failed_step": None, "report_path": None, "receipt_path": receipt_path,
        "endpoint": endpoint.strip() if isinstance(endpoint, str) else None,
    }
