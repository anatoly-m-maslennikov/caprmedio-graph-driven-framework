"""Project-bound MCP append checks using the actual Journal writer."""

import copy
import unittest
from pathlib import Path
from unittest.mock import patch

from append_mcp_test_support import AppendMcpFixture, appender, work_journal


class AppendChangeRecordsMcpTest(AppendMcpFixture, unittest.TestCase):
    def test_default_dry_run_preserves_all_bytes_and_creates_no_state(self) -> None:
        context = self._context(replacement=True)
        before = {
            path.relative_to(self.root): path.read_bytes()
            for path in self.root.rglob("*")
            if path.is_file()
        }
        with patch.object(appender, "run", side_effect=AssertionError("legacy run called")):
            result = self.adapter.invoke({"context": context})
        self.assertTrue(result["ok"])
        self.assertEqual("dry-run", result["mode"])
        self.assertEqual(
            context["predictions"]["journal_records"],
            result["result"]["planned_effects"]["journal_records"],
        )
        self.assertEqual(
            before,
            {
                path.relative_to(self.root): path.read_bytes()
                for path in self.root.rglob("*")
                if path.is_file()
            },
        )
        self.assertFalse((self.root / ".caprmedio_runtime").exists())
        self.assertEqual([], self._events())

    def test_two_distinct_actions_append_without_git_lease_index_or_run(self) -> None:
        contexts = [
            self._context(action_id=identity, replacement=True)
            for identity in ("observed-action-one", "observed-action-two")
        ]
        index = (self.root / ".git/index").read_bytes()
        artifact = self.fixture.artifact.read_bytes()
        with (
            patch.object(appender, "run", side_effect=AssertionError("legacy run called")),
            patch.object(
                appender, "acquire_lease", side_effect=AssertionError("Git lease acquired")
            ),
        ):
            results = [self._apply(context) for context in contexts]
        self.assertTrue(all(result["ok"] for result in results))
        self.assertEqual(
            [context["predictions"]["journal_records"][0] for context in contexts], self._events()
        )
        for context, result in zip(contexts, results):
            receipt = result["result"]["receipts"][0]
            self.assertEqual(
                context["predictions"]["journal_records"][0]["event_digest"],
                receipt["event_digest"],
            )
        self.assertEqual(index, (self.root / ".git/index").read_bytes())
        self.assertEqual(artifact, self.fixture.artifact.read_bytes())
        self.assertFalse((self.root / ".caprmedio_runtime/state/commit_change_set").exists())
        self.assertFalse((self.root / ".caprmedio_runtime/state/commit_trigger").exists())

    def test_historical_observations_survive_current_file_and_index_drift(self) -> None:
        context = self._context(replacement=True)
        self.fixture.artifact.write_bytes(b"later current source bytes\n")
        unrelated = self.root / "unrelated.txt"
        unrelated.write_text("unrelated staged change\n")
        self.fixture.run_git("add", "unrelated.txt")
        index = (self.root / ".git/index").read_bytes()
        result = self._apply(context)
        self.assertTrue(result["ok"])
        self.assertEqual(context["predictions"]["journal_records"], self._events())
        self.assertEqual(b"later current source bytes\n", self.fixture.artifact.read_bytes())
        self.assertEqual(index, (self.root / ".git/index").read_bytes())

    def test_exact_replacement_session_digest_and_successor_order_are_retained(self) -> None:
        context = self._context(replacement=True)
        before = copy.deepcopy(context)
        result = self._apply(context)
        self.assertTrue(result["ok"])
        self.assertEqual(before, context)
        event = before["predictions"]["journal_records"][0]
        receipt = result["result"]["receipts"][0]
        self.assertEqual(
            work_journal.canonical_json_bytes(event) + b"\n",
            (self.root / receipt["carrier"]).read_bytes(),
        )
        self.assertEqual(event["event_digest"], receipt["event_digest"])
        self.assertEqual(["CA-D-634", "CA-D-635"], self._events()[0]["successor_atom_ids"])
        self.assertEqual(event["llm_session"], self._events()[0]["llm_session"])

    def test_identical_replay_reuses_receipt_and_conflicting_identity_refuses(self) -> None:
        context = self._context(replacement=True)
        first = self._apply(context)
        second = self._apply(context)
        self.assertTrue(second["ok"])
        self.assertEqual(first["result"]["receipts"], second["result"]["receipts"])
        self.assertEqual(1, len(self._events()))
        changed = copy.deepcopy(context)
        event = changed["predictions"]["journal_records"][0]
        event["successor_atom_ids"] = ["CA-D-635", "CA-D-634"]
        changed["predictions"]["journal_records"] = [work_journal.with_event_digest(event)]
        with self.assertRaises(appender.ToolError) as refused:
            self._apply(changed)
        self.assertEqual("event-identity-mismatch", refused.exception.code)
        self.assertEqual(context["predictions"]["journal_records"], self._events())

    def test_constructor_has_no_io_and_factory_binds_native_module(self) -> None:
        with patch.object(Path, "resolve", side_effect=AssertionError("constructor I/O")):
            adapter = appender.AppendChangeRecordsAdapter(Path("unopened"), appender)
        self.assertEqual(Path("unopened"), adapter.root)
        self.assertIs(appender, self.adapter.native)
        self.assertEqual(self.root, self.adapter.root)


if __name__ == "__main__":
    unittest.main()
