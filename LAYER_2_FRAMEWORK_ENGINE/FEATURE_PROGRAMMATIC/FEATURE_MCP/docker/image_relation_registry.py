"""Private staging of the selected Framework's canonical relation-registry CLI."""

# CA-D-705@1
# CA-M-500@3
# CA-D-704@6
# CA-M-1011@3

from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

try:
    from .image_docker_client import bounded_run
    from .image_reference import IMMUTABLE_IMAGE
except ImportError:
    from image_docker_client import bounded_run
    from image_reference import IMMUTABLE_IMAGE


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
_ATOM_LIFECYCLE = Path("LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/ATOM_LIFECYCLE")


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


def verify_status_workflow_asset(source_root: Path, model_root: Path, *, timeout: float) -> None:
    """Require a shipped Python pilot to match its admitted source and bindings."""
    lifecycle = source_root / _ATOM_LIFECYCLE
    asset = lifecycle / "assets/change_current_status.py"
    verifier = lifecycle / "status_workflow_definition.py"
    sources = asset.with_name("change_current_status_sources.json")
    required = (asset, verifier, sources)
    if (lifecycle.resolve() != source_root.resolve() / _ATOM_LIFECYCLE
            or any(path.is_symlink() for path in (*required, asset.parent))):
        raise ValueError("lifecycle workflow files are unavailable")
    if not any(path.exists() for path in required):
        route = lifecycle / "status_cascade.py"
        if route.is_symlink():
            raise ValueError("lifecycle workflow route is unavailable")
        if route.is_file() and b"assets.change_current_status" in route.read_bytes():
            raise ValueError("lifecycle workflow files are missing from the routed pilot")
        return
    if not all(path.is_file() for path in required):
        raise ValueError("lifecycle workflow files are unavailable")
    result = subprocess.run(
        [sys.executable, "-B", str(verifier), "--model-root", str(model_root)], cwd=source_root,
        env={}, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
        timeout=timeout, check=False,
    )
    if result.returncode != 0:
        raise ValueError("lifecycle workflow verification failed")


def _lifecycle_model(source_root: Path, stage: Path, *, timeout: float) -> Path:
    methodology = source_root / "METHODOLOGY"
    if methodology.exists() or methodology.is_symlink():
        model = methodology / "sources"
        if methodology.is_symlink() or model.is_symlink() or not model.is_dir():
            raise ValueError("packaged lifecycle sources are unavailable")
        return model
    script = source_root / "LAYER_5_FRAMEWORK_DELIVERY/RELEASE_VERSION/release_support.py"
    if script.is_symlink() or not script.is_file():
        raise ValueError("lifecycle source selector is unavailable")
    # Run the checkout's source selector in a clean interpreter.
    selector = """
import shutil
import sys
from pathlib import Path

framework, output = map(Path, sys.argv[1:])
sys.path[:0] = [str(framework / 'LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS'),
                str(framework / 'LAYER_5_FRAMEWORK_DELIVERY/RELEASE_VERSION')]
from release_support import _release_sources

for _, source, files in _release_sources(framework):
    for path in files:
        target = output / source.name / path.relative_to(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)
"""
    model = stage / "model"
    result = subprocess.run([sys.executable, "-B", "-c", selector, str(source_root),
                             str(model)], cwd=source_root, env={},
                            stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                            timeout=timeout, check=False)
    if result.returncode != 0:
        raise ValueError("lifecycle source selection failed")
    return model


def _placement_selection(source_root: Path, model: Path, stage: Path, image: str, *,
                         timeout: float, max_output: int) -> Path:
    if not isinstance(image, str) or IMMUTABLE_IMAGE.fullmatch(image) is None:
        raise ValueError("previous image must be an immutable image ID")
    result = bounded_run(["docker", "image", "inspect", image], cwd=source_root,
                         timeout=timeout, max_output=max_output)
    if result.returncode != 0:
        raise ValueError("previous image is unavailable")
    try:
        records = json.loads(result.stdout)
        value = records[0] if isinstance(records, list) and len(records) == 1 else {}
        if (value.get("Id") != image or value.get("Os") != "linux"
                or not isinstance(value.get("Architecture"), str)
                or value.get("Config", {}).get("Labels", {}).get("org.caprmedio.runtime.schema") != "1"):
            raise ValueError("previous image inspection failed")
    except (ValueError, TypeError, AttributeError) as error:
        raise ValueError("previous image inspection failed") from error
    source = source_root / _ATOM_LIFECYCLE / "placement_sources.py"
    if source.is_symlink() or not source.is_file():
        raise ValueError("placement source selector is unavailable")
    selector = stage / "selector.py"
    shutil.copyfile(source, selector)
    if any("," in str(path) or "\n" in str(path) or "\r" in str(path) for path in (model, selector)):
        raise ValueError("placement selector mount path is invalid")
    result = bounded_run([
        "docker", "run", "--rm", "--pull=never", "--network=none", "--read-only",
        "--mount", f"type=bind,src={model},dst=/model,readonly",
        "--mount", f"type=bind,src={selector},dst=/selector.py,readonly",
        "--entrypoint", "/opt/venv/bin/python", image, "/selector.py", "/model",
    ], cwd=source_root, timeout=timeout, max_output=max_output)
    if result.returncode != 0:
        raise ValueError("previous image placement selection failed")
    try:
        json.loads(result.stdout)
    except (TypeError, ValueError) as error:
        raise ValueError("previous image placement selection is invalid") from error
    output = stage / "placement_selection.json"
    output.write_text(result.stdout, encoding="utf-8")
    return output


def compile_lifecycle_assets(source_root: Path, project_root: Path, *, timeout: float,
                             max_output: int, previous_image: str | None = None) -> tuple[bytes, bytes]:
    """Compile from the same admitted active source layers as local release."""
    temporary = project_root / ".caprmedio_tmp"
    if temporary.is_symlink() or not temporary.is_dir():
        raise ValueError("lifecycle staging root is unavailable")
    with tempfile.TemporaryDirectory(prefix="caprmedio-lifecycle-", dir=temporary) as stage:
        stage = Path(stage)
        model = _lifecycle_model(source_root, stage, timeout=timeout)
        if previous_image is not None and model != stage / "model":
            if any(path.is_symlink() for path in model.rglob("*")):
                raise ValueError("lifecycle model contains a symbolic link")
            shutil.copytree(model, stage / "model")
            model = stage / "model"
        verify_status_workflow_asset(source_root, model, timeout=timeout)
        selection = (_placement_selection(source_root, model, stage, previous_image,
                                          timeout=timeout, max_output=max_output)
                     if previous_image is not None else None)
        assets = []
        for name in ("status_model", "candidate_schema"):
            compiler = source_root / _ATOM_LIFECYCLE / f"{name}.py"
            output = stage / (name + ".json")
            if compiler.is_symlink() or not compiler.is_file():
                raise ValueError("lifecycle compiler is unavailable")
            command = [sys.executable, "-B", str(compiler), "--model-root", str(model), "--output", str(output)]
            if name == "candidate_schema" and selection is not None:
                command.extend(("--placement-selection", str(selection)))
            result = subprocess.run(command, cwd=source_root, env={},
                                    stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                                    timeout=timeout, check=False)
            if result.returncode != 0 or output.is_symlink() or not output.is_file() or output.stat().st_size > max_output:
                raise ValueError("lifecycle asset compilation failed")
            assets.append(output.read_bytes())
        return tuple(assets)
