"""Synthetic Current workflow fixture for legacy Coordinator tests."""

from pathlib import Path


WORKFLOW_PATH = Path(
    ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/"
    "CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/"
    "CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/"
    "CA-O-104-PROJECT_CONFIGURATION-WORKFLOW--review-and-repair-a-bounded-rmed-atom-batch.md"
)


def write_workflow_fixture(root: Path) -> Path:
    path = root / WORKFLOW_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\natom_id: CA-O-104\nversion: 1\nstatus: Active\n---\n"
        "# Synthetic Workflow Fixture\n"
    )
    return path
