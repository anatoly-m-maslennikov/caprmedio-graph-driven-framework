"""Functional temporary-state boundaries for selected Run evidence writes."""

from __future__ import annotations

import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
PROJECT_ROOT = APP.parents[3]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

import selected_evidence_io as evidence  # noqa: E402
from selected_execution_contracts import canonical_json  # noqa: E402


class SelectedEvidenceAtomicTests(unittest.TestCase):
    def setUp(self) -> None:
        parent = PROJECT_ROOT / ".caprmedio_tmp" / "selected-evidence-tests"
        parent.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        self.destination = evidence.run_directory(self.root, "atomic-test") / "result.json"

    def test_canonical_replacement_stages_only_under_project_temporary_state(self) -> None:
        observed: list[Path] = []
        replace = os.replace

        def observe(source: Path, target: Path) -> None:
            observed.append(source)
            self.assertEqual(self.destination, target)
            replace(source, target)

        value = {"z": "result", "a": [1, 2]}
        with patch.object(os, "replace", side_effect=observe):
            evidence.atomic_write(self.destination, value)
        self.assertEqual(canonical_json(value), self.destination.read_bytes())
        self.assertEqual(value, json.loads(self.destination.read_bytes()))
        self.assertTrue(observed[0].is_relative_to(self.root / ".caprmedio_tmp"))
        self.assertFalse(observed[0].exists())
        self.assertEqual(["result.json"], [p.name for p in self.destination.parent.iterdir()])

    def test_failed_replace_preserves_previous_bytes_and_cleans_owned_stage(self) -> None:
        evidence.atomic_write(self.destination, {"previous": True})
        previous = self.destination.read_bytes()
        with patch.object(os, "replace", side_effect=OSError("replacement failed")):
            with self.assertRaisesRegex(OSError, "replacement failed"):
                evidence.atomic_write(self.destination, {"next": True})
        self.assertEqual(previous, self.destination.read_bytes())
        stages = self.root / ".caprmedio_tmp" / "workflow_orchestrator" / "atomic"
        self.assertEqual([], list(stages.iterdir()))


if __name__ == "__main__":
    unittest.main()
