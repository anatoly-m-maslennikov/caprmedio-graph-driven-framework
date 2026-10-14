"""Replacement records observed lineage without manufacturing a predecessor."""

import json
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import test_selected_lifecycle_journal as lifecycle_fixture
from selected_execution import SelectedExecution
from work_journal import append_sealed_events, read_records

sys.path.insert(0, str(lifecycle_fixture.TOOLS / "VALIDATE_ATOMS"))
from replacement import Replacement  # noqa: E402


class FirstRecordedReplacementChangeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.harness = lifecycle_fixture.SelectedLifecycleJournalTest()
        self.harness.setUp()
        self.addCleanup(self.harness.doCleanups)
        self.root, self.path = self.harness.root, self.harness.path

    def test_first_selected_event_preserves_observed_replacement_identity_order(self) -> None:
        selected = SelectedExecution.__new__(SelectedExecution)
        selected.root = self.root
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
        event = selected._replacement_canonical_event(
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

    def replacement_fixture(self):
        self.path.write_bytes(b"---\natom_id: CA-R-100\nversion: 1\nstatus: Active\n---\nbefore\n")
        store = SimpleNamespace(
            root=self.root,
            path=lambda relative: self.root / relative,
            load=lambda run_id: {
                "author": "test-user",
                "session": {"app": "codex", "uuid": "test"},
            },
        )

        def save(path, value):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(value))

        engine = SimpleNamespace(
            store=store, run_directory=lambda run_id: self.root / "runs" / run_id, save=save
        )
        replacement = Replacement(engine, "actual-replacement", 0)
        value = {
            "context": {
                "atom_id": "CA-R-100",
                "source": self.harness.facts(),
                "source_content": self.path.read_text(),
            },
            "candidate_content": self.path.read_text() + "next\n",
        }
        request = SimpleNamespace(author="test-user", scope="CORE_META_MODEL")
        return replacement, value, request

    def test_replacement_logs_again_without_republishing_source_effects(self) -> None:
        historical = {"arbitrary": "history", "previous_result_event": "missing"}
        append_sealed_events(self.root, [historical], **self.harness.context)
        replacement, value, request = self.replacement_fixture()
        with patch.object(replacement, "next_id", return_value="CA-R-101"):
            evidence = replacement.apply(value, request, "new claim")
        rows = read_records(self.root)
        self.assertEqual(3, len(rows))
        self.assertEqual(historical, rows[0])
        self.assertEqual(["MOVE+UPDATE", "ADD"], [row["action_type"] for row in rows[1:]])
        self.assertNotIn("previous_result_event", rows[1])
        self.assertEqual("CA-R-100", rows[1]["predecessor_atom_id"])
        self.assertEqual(["CA-R-101"], rows[1]["successor_atom_ids"])
        with patch("replacement.os.link", side_effect=AssertionError("effects replayed")):
            replacement.apply(value, request, "new claim")
        self.assertEqual(5, len(read_records(self.root)))
        self.assertEqual(2, len(evidence["journal_receipts"]))

    def test_log_failure_reports_actual_replacement_without_source_replay(self) -> None:
        replacement, value, request = self.replacement_fixture()
        with (
            patch.object(replacement, "next_id", return_value="CA-R-101"),
            patch("replacement.append_sealed_events", side_effect=OSError("Journal unavailable")),
        ):
            evidence = replacement.apply(value, request, "new claim")
        self.assertFalse(self.path.exists())
        self.assertTrue((self.root / evidence["archived"]["path"]).is_file())
        self.assertTrue((self.root / evidence["successor"]["path"]).is_file())
        self.assertEqual("Journal unavailable", evidence["recording_error"])
        self.assertEqual([], evidence["journal_receipts"])
        with patch("replacement.os.link", side_effect=AssertionError("effects replayed")):
            repeated = replacement.apply(value, request, "new claim")
        self.assertNotIn("recording_error", repeated)
        self.assertEqual(2, len(read_records(self.root)))

    def test_plan_persistence_failure_is_not_a_log_diagnostic(self) -> None:
        replacement, value, request = self.replacement_fixture()
        save = replacement.engine.save

        def fail_after_reservation(path, plan):
            if path.exists():
                raise OSError("plan unavailable")
            save(path, plan)

        with (
            patch.object(replacement, "next_id", return_value="CA-R-101"),
            patch.object(replacement.engine, "save", side_effect=fail_after_reservation),
        ):
            with self.assertRaisesRegex(OSError, "plan unavailable"):
                replacement.apply(value, request, "new claim")


if __name__ == "__main__":
    unittest.main()
