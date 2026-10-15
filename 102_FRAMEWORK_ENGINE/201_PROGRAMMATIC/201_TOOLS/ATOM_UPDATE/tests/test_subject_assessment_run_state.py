"""Completed source assessment is bound to Run state and its persisted result."""

import json
from pathlib import Path
from types import SimpleNamespace
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOOLS))

import atom_subject_apply as native  # noqa: E402
from lifecycle_intents import LifecycleError  # noqa: E402


class SubjectAssessmentRunStateTests(unittest.TestCase):
    def setUp(self):
        scratch = TOOLS.parents[2] / ".caprmedio_tmp/tests/assessment-run-state"
        scratch.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.assessment = {"actual": "assessment"}
        self.action = {
            "run_id": "assessment-action",
            "kind": "action",
            "parent_run_id": "assessment-step",
            "definition": {"atom_id": "CA-O-067"},
        }
        self.session = SimpleNamespace(
            actual={
                "workflow": {
                    "run_id": "workflow",
                    "kind": "workflow",
                    "definition": {"atom_id": "CA-O-127"},
                },
                "step": {
                    "run_id": "assessment-step",
                    "kind": "step",
                    "parent_run_id": "workflow",
                    "definition": {"atom_id": "CA-O-145"},
                },
                "action": self.action,
            },
            terminal={
                "step": {
                    "run_id": "assessment-step",
                    "disposition": "terminal",
                    "outcome": "completed",
                    "effect_refs": [],
                },
                "action": {
                    "run_id": "assessment-action",
                    "disposition": "terminal",
                    "outcome": "completed",
                    "effect_refs": [],
                    "result_ref": "assessment.json",
                },
            },
            _parent_lineage=lambda record: ("workflow",),
        )
        self.result = {
            "result": "identity-preserving",
            "action_run_id": "assessment-action",
            "native_result": {"assessment": self.assessment},
        }

    def check(self):
        (self.root / "assessment.json").write_text(json.dumps(self.result))
        native._completed_assessment(
            self.root, self.session, self.assessment, {"run_id": "mutation"}
        )

    def test_persisted_actual_assessment_needs_no_journal_receipt(self):
        self.check()

    def test_mismatched_actual_assessment_result_is_still_refused(self):
        self.result["action_run_id"] = "different-action"
        with self.assertRaises(LifecycleError):
            self.check()


if __name__ == "__main__":
    unittest.main()
