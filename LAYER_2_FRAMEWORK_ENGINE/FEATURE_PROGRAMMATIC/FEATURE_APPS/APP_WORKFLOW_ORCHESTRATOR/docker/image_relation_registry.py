"""Private staging of the selected Framework's canonical relation-registry CLI."""

# CA-D-705@1
# CA-M-500@3

from __future__ import annotations

from pathlib import Path
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
