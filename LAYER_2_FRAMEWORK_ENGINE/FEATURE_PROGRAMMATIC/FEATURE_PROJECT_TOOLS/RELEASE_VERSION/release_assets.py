"""Generate the two Workbench assets that a release package owns."""

# CA-D-705@1
# CA-M-500@3

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


class LocalReleaseError(RuntimeError):
    """A pre-effect refusal from the bounded local-release runner."""


_WORKBENCH_BACKEND = Path(
    "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/"
    "FEATURE_WORKBENCH_BACKEND"
)


def _generate_asset(
    package: Path, project_root: Path, script_name: str, output_name: str, error_name: str,
) -> Path:
    script = package / _WORKBENCH_BACKEND / script_name
    output = script.with_name(output_name)
    unavailable = f"local-release-{error_name}-unavailable"
    if not script.is_file() or script.is_symlink():
        raise LocalReleaseError(unavailable)
    try:
        output.unlink(missing_ok=True)
        result = subprocess.run(
            (
                sys.executable, "-B", str(script), "--project-root", str(project_root),
                "--output", str(output),
            ),
            cwd=package, text=True, capture_output=True, check=False,
        )
    except OSError as error:
        raise LocalReleaseError(unavailable) from error
    if result.returncode != 0 or not output.is_file() or output.is_symlink():
        raise LocalReleaseError(f"local-release-{error_name}-generation-failed")
    return output


def generate_relation_registry(package: Path, project_root: Path) -> Path:
    return _generate_asset(
        package, project_root, "generate_relation_registry.py", "canonical_relation_registry.json",
        "relation-registry",
    )


def generate_workbench_schema(package: Path, project_root: Path) -> Path:
    return _generate_asset(
        package, project_root, "generate_workbench_schema.py", "workbench_schema.json",
        "workbench-schema",
    )
