"""Focused native creation result-label compatibility checks."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

from selected_creation_result import complete_creation  # noqa: E402


class _Session:
    def finish_run(self, run_id: str, **result: object) -> dict[str, object]:
        return {"run_id": run_id, "disposition": "terminal", **result}

    def note_effects(self, run_id: str, *, result_ref: str, effect_refs: list[str]) -> None:
        del run_id, result_ref, effect_refs


class SelectedCreationOutcomeTests(unittest.TestCase):
    def test_legacy_result_labels_and_terminal_outcomes(self) -> None:
        cases = (
            ("applied", "applied", "completed"),
            ("no-op", "no-op", "no_op"),
            ("duplicate", "no-op", "no_op"),
            ("failed", "failed", "failed"),
            ("partial", "partial", "partial"),
            ("canceled", "canceled", "cancelled"),
            ("blocked", "blocked", "interrupted_pending"),
            ("unexpected", "unexpected", "interrupted_pending"),
        )
        for native, expected_result, expected_terminal in cases:
            with self.subTest(native=native):
                output = complete_creation(
                    _Session(),
                    "requested-child",
                    "actual-child",
                    native,
                    [],
                    "result.json",
                    {"outcome": native},
                    None,
                    None,
                )
                self.assertEqual(expected_result, output["result"])
                self.assertEqual(expected_terminal, output["terminal_outcome"])


if __name__ == "__main__":
    unittest.main()
