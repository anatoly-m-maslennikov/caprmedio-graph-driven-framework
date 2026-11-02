"""Keep W04 status result labels and terminal outcomes source-compatible."""

from __future__ import annotations

from pathlib import Path
import sys
import unittest


APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

from selected_lifecycle_status_result import status_envelope  # noqa: E402


class SelectedLifecycleStatusOutcomeTests(unittest.TestCase):
    def test_native_outcomes_match_the_old_nested_handler(self) -> None:
        expected = (
            ("applied", "applied", "completed"),
            ("no-op", "no-op", "no_op"),
            ("duplicate", "no-op", "no_op"),
            ("failed", "failed", "interrupted_pending"),
            ("partial", "partial", "interrupted_pending"),
            ("canceled", "canceled", "interrupted_pending"),
            ("blocked", "blocked", "interrupted_pending"),
        )
        for outcome, result_label, terminal_outcome in expected:
            with self.subTest(outcome=outcome):
                envelope = status_envelope(
                    outcome,
                    {"outcome": outcome},
                    ["effect.md"],
                    {"state": "observed"},
                    None,
                    None,
                )
                self.assertEqual(result_label, envelope["result"])
                self.assertEqual(terminal_outcome, envelope["terminal_outcome"])

    def test_pending_keeps_recording_partial_truth(self) -> None:
        envelope = status_envelope(
            "pending",
            {"outcome": "pending"},
            ["effect.md"],
            {"state": "observed"},
            None,
            "OSError",
        )
        self.assertEqual("recording-pending", envelope["result"])
        self.assertEqual("partial", envelope["terminal_outcome"])
        self.assertEqual(["effect.md"], envelope["effect_refs"])
        self.assertEqual("OSError", envelope["recording_error"])


if __name__ == "__main__":
    unittest.main()
