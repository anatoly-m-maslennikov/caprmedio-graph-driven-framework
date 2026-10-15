#!/usr/bin/env -S uv run --no-project --isolated --managed-python --python 3.14 --no-env-file python -I
"""Start or reuse one Project's Docker MCP endpoint and print its URL."""

import argparse
import os
from pathlib import Path
import subprocess
import re
import tomllib

LAUNCHER_PATH = Path("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py")


_RELEASE = re.compile(r"releases/[0-9a-f]{64}\Z")


def _source_root(script_path: Path) -> Path | None:
    for candidate in (script_path.parent, *script_path.parents):
        if (candidate / LAUNCHER_PATH).is_file():
            return candidate
    return None


def _installed_source_root(project_root: Path) -> Path:
    selector = project_root / ".caprmedio_install" / "current.toml"
    local_package = project_root / ".caprmedio_runtime" / "simple_local_release" / "package"
    try:
        if any(path.is_symlink() for path in (local_package, local_package.parent, local_package.parent.parent)):
            raise ValueError()
        try:
            local_package.lstat()
        except FileNotFoundError:
            local_present = False
        else:
            local_present = True
        if local_present:
            package = local_package
        elif selector.is_file() and not selector.is_symlink():
            document = tomllib.loads(selector.read_text(encoding="utf-8"))
            release = document.get("release_relpath")
            if not isinstance(release, str) or _RELEASE.fullmatch(release) is None:
                raise ValueError()
            package = project_root / ".caprmedio_install" / release
        elif selector.exists() or selector.is_symlink():
            raise ValueError()
        else:
            package = local_package
        if package.is_symlink() or not package.is_dir() or package.resolve(strict=True) != package:
            raise ValueError()
        launcher = package / LAUNCHER_PATH
        if not launcher.is_file() or launcher.resolve(strict=True) != launcher:
            raise ValueError()
        return package
    except (OSError, UnicodeDecodeError, ValueError):
        raise ValueError("installed Framework package launcher is unavailable") from None


def main(argv=None):
    script_path = Path(__file__).resolve()
    script_source = None if script_path.parent.name == ".caprmedio_runtime" else _source_root(script_path)
    default_root = script_source or script_path.parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=default_root)
    parser.add_argument("--source-root", type=Path,
                        help="Framework source checkout (defaults to the selected installed package)")
    parser.add_argument("--control-root", help="Optional direct .caprmedio_<project> folder")
    parser.add_argument("--port", type=int, help="Assert the Project Settings localhost port")
    parser.add_argument("--no-build", action="store_true", help="Use a matching existing image only")
    args = parser.parse_args(argv)
    if args.port is not None and not 1 <= args.port <= 65535:
        parser.error("--port must be between 1 and 65535")

    project = args.project_root.resolve()
    try:
        if args.source_root is not None:
            source = args.source_root.resolve()
        elif script_source is not None:
            source = script_source
        else:
            source = _installed_source_root(project)
    except ValueError as error:
        parser.error(str(error))
    launcher = source / LAUNCHER_PATH
    if not launcher.is_file():
        parser.error("Framework launcher not found; pass --source-root with the Framework checkout")
    command = [
        "uv", "run", "--project", str(source), "--locked", "--python", "3.14",
        "--managed-python", "--no-env-file", "--group", "rmed-workflow-mcp",
        str(launcher), "--project-root", str(project),
               "--source-root", str(source), "--output", "url"]
    if args.control_root:
        command.extend(["--control-root", args.control_root])
    if args.port is not None:
        command.extend(["--port", str(args.port)])
    if args.no_build:
        command.append("--no-build")
    command.append("project-mcp")
    environment = dict(os.environ)
    for name in ("PYTHONHOME", "PYTHONPATH", "VIRTUAL_ENV", "CONDA_PREFIX",
                 "CAPRMEDIO_MCP_HTTP_SECRET_TOKEN"):
        environment.pop(name, None)
    environment["UV_PROJECT_ENVIRONMENT"] = str(
        project / ".caprmedio_runtime" / "launcher-venv")
    environment["UV_CACHE_DIR"] = str(project / ".caprmedio_tmp" / "cache" / "uv")
    environment["PYTHONNOUSERSITE"] = "1"
    try:
        return subprocess.run(command, check=False, env=environment).returncode
    except FileNotFoundError:
        print("uv is required to run the Project MCP launcher.", file=os.sys.stderr)
        return 2
    except OSError:
        print("Could not run the uv Project MCP launcher.", file=os.sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
