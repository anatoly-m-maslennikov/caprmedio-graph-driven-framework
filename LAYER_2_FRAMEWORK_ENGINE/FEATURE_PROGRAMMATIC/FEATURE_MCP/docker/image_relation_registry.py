"""Private staging of the selected Framework's canonical relation-registry CLI."""

# CA-D-705@1
# CA-M-500@3

from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


RELATION_REGISTRY_COMPILER = (
    "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/"
    "FEATURE_WORKBENCH_BACKEND/generate_relation_registry.py"
)
WORKBENCH_SCHEMA_COMPILER = (
    "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/"
    "FEATURE_WORKBENCH_BACKEND/generate_workbench_schema.py"
)
TOOL_REGISTRY_COMPILER = (
    "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/generate_tool_registry.py"
)
TOOL_PROVIDERS = (
    "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/tool_providers.json"
)
TOOL_REGISTRY = "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/tool_registry.json"


def _compile_generated_asset(source_root: Path, project_root: Path, compiler_path: str,
                             asset_name: str, *, timeout: float, max_output: int) -> bytes:
    """Run one selected-Framework asset compiler in private Project staging."""
    compiler = source_root / compiler_path
    temporary = project_root / ".caprmedio_tmp"
    if (compiler.is_symlink() or not compiler.is_file() or temporary.is_symlink()
            or not temporary.is_dir()):
        raise ValueError("generated asset compiler or staging root is unavailable")
    with tempfile.TemporaryDirectory(prefix="caprmedio-generated-asset-", dir=temporary) as stage:
        output = Path(stage) / asset_name
        result = subprocess.run(
            [sys.executable, "-B", str(compiler), "--project-root", str(project_root), "--output", str(output)],
            cwd=source_root,
            env={},
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=timeout,
            check=False,
        )
        if result.returncode != 0 or output.is_symlink() or not output.is_file():
            raise ValueError("generated asset compilation failed")
        if output.stat().st_size > max_output:
            raise ValueError("generated asset output exceeded its bounded read")
        return output.read_bytes()


def compile_relation_registry(source_root: Path, project_root: Path, *, timeout: float,
                              max_output: int) -> bytes:
    return _compile_generated_asset(
        source_root, project_root, RELATION_REGISTRY_COMPILER, "canonical_relation_registry.json",
        timeout=timeout, max_output=max_output,
    )


def compile_workbench_schema(source_root: Path, project_root: Path, *, timeout: float,
                             max_output: int) -> bytes:
    return _compile_generated_asset(
        source_root, project_root, WORKBENCH_SCHEMA_COMPILER, "workbench_schema.json",
        timeout=timeout, max_output=max_output,
    )


def compile_tool_registry(source_root: Path, *, timeout: float, max_output: int) -> bytes:
    """Generate the registry in private staging, never in the source closure."""
    compiler = source_root / TOOL_REGISTRY_COMPILER
    providers = source_root / TOOL_PROVIDERS
    if (compiler.is_symlink() or not compiler.is_file() or providers.is_symlink()
            or not providers.is_file()):
        raise ValueError("tool registry compiler or providers are unavailable")
    with tempfile.TemporaryDirectory(prefix="caprmedio-tool-registry-") as stage:
        package = Path(stage) / "package"
        shutil.copytree(
            source_root / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC",
            package / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC",
            symlinks=True,
        )
        staged_compiler = package / TOOL_REGISTRY_COMPILER
        output = package / TOOL_REGISTRY
        result = subprocess.run(
            [sys.executable, "-B", str(staged_compiler), "--package-root", str(package)],
            cwd=package,
            env={},
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=timeout,
            check=False,
        )
        if result.returncode != 0 or output.is_symlink() or not output.is_file():
            raise ValueError("tool registry compilation failed")
        if output.stat().st_size > max_output:
            raise ValueError("tool registry output exceeded its bounded read")
        payload = output.read_bytes()
        try:
            json.loads(payload)
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ValueError("tool registry output is invalid") from error
        return payload
