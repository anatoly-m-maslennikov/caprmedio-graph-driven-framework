# implementation of:
# Method: CA-M-405
"""A consumed continuation remains available for safe crash recovery."""

from __future__ import annotations

from pathlib import Path
import sys
import unittest

APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

from selected_integrated_frontier import (  # noqa: E402
    IntegratedFrontierError,
    IntegratedFrontierStore,
)
import test_selected_integrated_frontier as fixtures  # noqa: E402


class IntegratedHistoricalRecordTests(unittest.TestCase):
    # implementation of:
    # Method: CA-M-405
    def test_record_retains_consumed_frontier_and_returns_an_isolated_copy(self) -> None:
        fixture = fixtures.SelectedIntegratedFrontierTests()
        fixture.setUp()
        self.addCleanup(fixture.tearDown)
        with IntegratedFrontierStore(fixture.project, fixture.run_id) as store:
            original = fixture._frontier("first")
            store.save(original)
            store.admit(fixture._submission("first"))
            self.assertIsNone(store.load()["frontier"])
            record = store.record("first")
            self.assertEqual("admitted", record["state"])
            self.assertEqual(original, record["frontier"])
            record["frontier"]["step"]["id"] = "tampered"
            self.assertEqual(original, store.record("first")["frontier"])
            with self.assertRaises(IntegratedFrontierError):
                store.record("absent")
        with self.assertRaises(IntegratedFrontierError):
            store.record("first")


if __name__ == "__main__":
    unittest.main()
