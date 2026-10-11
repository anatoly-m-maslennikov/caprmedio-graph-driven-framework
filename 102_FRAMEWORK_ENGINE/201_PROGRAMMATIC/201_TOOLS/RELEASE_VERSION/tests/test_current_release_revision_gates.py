"""Current O164 revision gate coverage without a copied revision pin."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
import re


RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from release_actions import (  # noqa: E402
    ReleaseActionRun,
    SelectedReleaseActionContext,
    _fingerprint,
    _selection,
)
from release_contract import ReleaseContractError  # noqa: E402


class _Request:
    def __init__(self, project_root: str) -> None:
        self.project_root = project_root

    def model_dump(self, **_kwargs):
        return {
            "project_root": self.project_root,
            "operation": "apply",
            "failed_recording_ref": None,
        }


class CurrentReleaseRevisionGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = str(Path(self.temporary.name).resolve())
        self.request = _Request(self.root)
        self.run = ReleaseActionRun(
            self.root, "workflow", _fingerprint(self.request), self.request,
        )

    def context(self, version: int) -> SelectedReleaseActionContext:
        return SelectedReleaseActionContext(
            self.root, "workflow", "step", "action", "workflow", "step",
            "CA-O-170", "CA-O-165", self.run.frozen_parameters_sha256,
            workflow_version=version,
        )

    def test_current_admitted_revision_is_not_a_copied_pin(self) -> None:
        source = RELEASE_ROOT.parents[3] / (
            ".caprmedio_caprmedio/09_operations/CA-O-164-WORKFLOW--release-a-selected-framework-version.md"
        )
        version = int(re.search(
            r"(?m)^version:\s*([1-9][0-9]*)\s*$", source.read_text(encoding="utf-8"),
        ).group(1))
        index, phase = _selection(self.request, self.context(version), self.run)
        self.assertEqual((index, phase), (0, "freeze"))

    def test_non_positive_or_non_integer_revision_is_refused(self) -> None:
        for version in (0, -1, True, "12"):
            with self.subTest(version=version):
                with self.assertRaises(ReleaseContractError):
                    _selection(self.request, self.context(version), self.run)


if __name__ == "__main__":
    unittest.main()
