# CA-M-504@2
"""Small durable-state boundary retained after AI Agent retirement."""

import hashlib
from pathlib import Path
import sys

from runtime_config import control_directory

TOOLS = Path(__file__).resolve().parents[2] / "FEATURE_TOOLS"
EVIDENCE = (
    Path(__file__).resolve().parents[3]
    / "FEATURE_AGENTIC"
    / "FEATURE_PROMPTS"
    / "ACTION_PROMPTS"
    / "RMED_ATOM_REVIEW"
)
for path in (TOOLS, EVIDENCE):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))
from workflow_evidence import RunEvidence, encoded  # noqa: E402


def runtime_fingerprint(root=None):
    """Fingerprint the deterministic worker implementation used for readiness."""
    app = Path(__file__).resolve().parent
    paths = [
        app / name
        for name in (
            "contracts.py",
            "engine.py",
            "backend.py",
            "orchestrator.py",
            "runtime_config.py",
        )
    ]
    paths.extend(sorted(app.glob("selected_*.py")))
    paths.extend(
        TOOLS / name
        for name in (
            "operation_error_boundary.py",
            "runtime_failure_diagnostics.py",
            "runtime_process_boundary.py",
            "technical_diagnostics.py",
            "project_selection.py",
            "project_settings_schema.py",
            "COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py",
        )
    )
    paths.extend(app / "docker" / name for name in ("entrypoint.py", "Dockerfile", "compose.yaml"))
    paths.extend(app.parents[3] / name for name in ("pyproject.toml", "uv.lock"))
    observations = [
        {
            "path": str(path.relative_to(app.parents[3])),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }
        for path in paths
    ]
    return hashlib.sha256(encoded(observations)).hexdigest()


class Coordinator:
    """Compatibility facade for durable Run paths and historical observations.

    It intentionally has no Agent dispatch or Base Revise execution methods.
    """

    def __init__(self, root):
        self.root = Path(root).resolve(strict=True)
        self.store = RunEvidence(self.root)

    def run_directory(self, run_id):
        self.store._directory(run_id)
        return self.store.path(f"{control_directory()}/runs/{run_id}")

    def save(self, path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.store._atomic(path, encoded(value))
