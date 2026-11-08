"""Private staging of the selected Framework's canonical relation-registry CLI."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import tempfile


RELATION_REGISTRY_COMPILER = (
    "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/"
    "FEATURE_WORKBENCH_BACKEND/generate_relation_registry.py"
)


def compile_relation_registry(source_root: Path, project_root: Path, *, timeout: float,
                              max_output: int) -> bytes:
    """Run the selected Framework compiler in private Project staging."""
    compiler = source_root / RELATION_REGISTRY_COMPILER
    temporary = project_root / ".caprmedio_tmp"
    if (compiler.is_symlink() or not compiler.is_file() or temporary.is_symlink()
            or not temporary.is_dir()):
        raise ValueError("relation registry compiler or staging root is unavailable")
    with tempfile.TemporaryDirectory(prefix="caprmedio-relation-registry-", dir=temporary) as stage:
        output = Path(stage) / "canonical_relation_registry.json"
        result = subprocess.run(
            [sys.executable, str(compiler), "--project-root", str(project_root), "--output", str(output)],
            cwd=source_root,
            env={},
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=timeout,
            check=False,
        )
        if result.returncode != 0 or output.is_symlink() or not output.is_file():
            raise ValueError("relation registry compilation failed")
        if output.stat().st_size > max_output:
            raise ValueError("relation registry output exceeded its bounded read")
        return output.read_bytes()
