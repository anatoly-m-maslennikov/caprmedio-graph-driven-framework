"""Replacement records observed lineage without manufacturing a predecessor."""

import sys
import unittest


import test_selected_lifecycle_journal as lifecycle_fixture
from selected_replacement_journal import canonical_event

sys.path.insert(0, str(lifecycle_fixture.TOOLS / "VALIDATE_ATOMS"))


class FirstRecordedReplacementChangeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.harness = lifecycle_fixture.SelectedLifecycleJournalTest()
        self.harness.setUp()
        self.addCleanup(self.harness.doCleanups)
        self.root, self.path = self.harness.root, self.harness.path

    def test_first_selected_event_preserves_observed_replacement_identity_order(self) -> None:
        original = {
            "atom_id": "CA-R-100",
            "path": "atoms/draft.md",
            "version": 1,
            "digest": "0" * 64,
        }
        observed = {
            **original,
            "filename": "draft.md",
            "path": "archive/draft.md",
            "digest": "1" * 64,
        }
        event = canonical_event(
            parameters={"predecessor": original},
            native_result={
                "history": {"predecessor": original},
                "predecessor": observed,
                "successors": [{"atom_id": "CA-R-102"}, {"atom_id": "CA-R-101"}],
            },
            replacement_binding={"atom_id": "CA-O-051"},
            replacement_action_run_id="actual-run",
            execution_request_id="request",
            author="test-user",
            occurred_at="2026-10-08T00:00:00+04:00",
            structural_scope="CORE_META_MODEL",
        )
        self.assertNotIn("previous_result_event", event)
        self.assertEqual("CA-R-100", event["predecessor_atom_id"])
        self.assertEqual(["CA-R-102", "CA-R-101"], event["successor_atom_ids"])


if __name__ == "__main__":
    unittest.main()
