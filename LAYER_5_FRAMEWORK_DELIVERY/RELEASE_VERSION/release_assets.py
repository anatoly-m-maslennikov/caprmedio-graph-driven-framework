"""Generate the two Workbench assets that a release package owns."""

# CA-D-704@6

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


class LocalReleaseError(RuntimeError):
    """A pre-effect refusal from the bounded local-release runner."""


_WORKBENCH_BACKEND = Path(
    "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/"
    "FEATURE_WORKBENCH_BACKEND"
)
_MCP = Path("LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP")
_ATOM_LIFECYCLE = _MCP.parent / "FEATURE_TOOLS/ATOM_LIFECYCLE"


def _generate_asset(
    package: Path, source_root: Path, script_path: Path, output_name: str, error_name: str,
    *, source_option: str = "--project-root",
) -> Path:
    script = package / script_path
    output = script.with_name(output_name)
    unavailable = f"local-release-{error_name}-unavailable"
    if not script.is_file() or script.is_symlink():
        raise LocalReleaseError(unavailable)
    try:
        output.unlink(missing_ok=True)
        result = subprocess.run(
            (
                sys.executable, "-B", str(script), source_option, str(source_root),
                "--output", str(output),
            ),
            cwd=package, stdout=subprocess.DEVNULL, check=False,
        )
    except OSError as error:
        raise LocalReleaseError(unavailable) from error
    if result.returncode != 0 or not output.is_file() or output.is_symlink():
        raise LocalReleaseError(f"local-release-{error_name}-generation-failed")
    return output


def generate_relation_registry(package: Path, project_root: Path) -> Path:
    return _generate_asset(
        package, project_root, _WORKBENCH_BACKEND / "generate_relation_registry.py", "canonical_relation_registry.json",
        "relation-registry",
    )


def generate_workbench_schema(package: Path, project_root: Path) -> Path:
    return _generate_asset(
        package, project_root, _WORKBENCH_BACKEND / "generate_workbench_schema.py", "workbench_schema.json",
        "workbench-schema",
    )


def generate_lifecycle_status_model(package: Path) -> Path:
    return _generate_asset(
        package, package / "METHODOLOGY/sources", _ATOM_LIFECYCLE / "status_model.py",
        "status_model.json", "lifecycle-status-model", source_option="--model-root",
    )


def generate_lifecycle_candidate_schema(package: Path) -> Path:
    return _generate_asset(
        package, package / "METHODOLOGY/sources", _ATOM_LIFECYCLE / "candidate_schema.py",
        "candidate_schema.json", "lifecycle-candidate-schema", source_option="--model-root",
    )


def generate_tool_registry(package: Path) -> Path:
    """Seal the configured MCP providers into the staged runtime package."""
    script = package / _MCP / "generate_tool_registry.py"
    output = script.with_name("tool_registry.json")
    unavailable = "local-release-tool-registry-unavailable"
    if not script.is_file() or script.is_symlink():
        raise LocalReleaseError(unavailable)
    try:
        output.unlink(missing_ok=True)
        result = subprocess.run(
            (sys.executable, "-B", str(script), "--package-root", str(package)),
            cwd=package, text=True, capture_output=True, check=False,
        )
    except OSError as error:
        raise LocalReleaseError(unavailable) from error
    if result.returncode != 0 or not output.is_file() or output.is_symlink():
        raise LocalReleaseError("local-release-tool-registry-generation-failed")
    try:
        json.loads(output.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise LocalReleaseError("local-release-tool-registry-generation-failed") from error
    return output


def generate_scope_callback(package: Path, raw: bytes, *, selected_pin, release_sources):
    """Build the explicitly selected callback; no selection preserves legacy release."""
    if selected_pin is None:
        return None
    from FEATURE_FORMAL_MODEL_ENGINE.scope_callback_asset import generated_assets, write_package
    generated = generated_assets(raw, pin=selected_pin, release_sources=release_sources)
    return write_package(package / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_FORMAL_MODEL_ENGINE/assets", generated)
