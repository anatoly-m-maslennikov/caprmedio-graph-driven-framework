"""Independent Project-bound append tests using the actual Journal writer."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

from pydantic import ValidationError

TESTS = Path(__file__).resolve().parent
sys.path.insert(0, str(TESTS))
import test_append_change_records as native_tests  # noqa: E402
import append_change_records as appender  # noqa: E402
import work_journal  # noqa: E402


class AppendChangeRecordsMcpTest(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = native_tests.AppendChangeRecordsTest("test_dry_run_is_mutation_free")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root.resolve()
        self.adapter = appender.create_adapter(self.root)

    def _context(self, *, action_id: str = "observed-action-one", replacement: bool = False) -> dict:
        context = self.fixture.context(action="MOVE+UPDATE" if replacement else "ADD")
        context["action_id"] = action_id
        event = context["predictions"]["journal_records"][0]
        event["action_id"] = action_id
        if replacement:
            context["previous_result_event"] = event["previous_result_event"]
            event.update(predecessor_atom_id="CA-D-562", successor_atom_ids=["CA-D-634", "CA-D-635"])
        event["event_id"] = appender._expected_event_id(event)
        context["predictions"]["journal_records"] = [work_journal.with_event_digest(event)]
        context["context_id"] = appender._expected_context_id(context)
        return context

    def _events(self) -> list[dict]:
        journal = self.root / ".caprmedio_caprmedio/_journal"
        return [json.loads(line) for path in sorted(journal.glob("*.ndjson"))
                for line in path.read_text().splitlines()]

    def _apply(self, context: dict) -> dict:
        return self.adapter.invoke({"context": context, "apply": True})

    def test_default_dry_run_preserves_all_bytes_and_creates_no_state(self) -> None:
        context = self._context(replacement=True)
        before = {path.relative_to(self.root): path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
        with patch.object(appender, "run", side_effect=AssertionError("legacy run called")):
            result = self.adapter.invoke({"context": context})
        self.assertTrue(result["ok"])
        self.assertEqual("dry-run", result["mode"])
        self.assertEqual(context["predictions"]["journal_records"], result["result"]["planned_effects"]["journal_records"])
        self.assertEqual(before, {path.relative_to(self.root): path.read_bytes() for path in self.root.rglob("*") if path.is_file()})
        self.assertFalse((self.root / ".caprmedio_runtime").exists())
        self.assertEqual([], self._events())

    def test_two_distinct_actions_append_without_git_lease_index_or_run(self) -> None:
        contexts = [self._context(action_id=identity, replacement=True)
                    for identity in ("observed-action-one", "observed-action-two")]
        index = (self.root / ".git/index").read_bytes()
        artifact = self.fixture.artifact.read_bytes()
        with patch.object(appender, "run", side_effect=AssertionError("legacy run called")), \
             patch.object(appender, "acquire_lease", side_effect=AssertionError("Git lease acquired")):
            results = [self._apply(context) for context in contexts]
        self.assertTrue(all(result["ok"] for result in results))
        self.assertEqual([context["predictions"]["journal_records"][0] for context in contexts], self._events())
        for context, result in zip(contexts, results):
            receipt = result["result"]["receipts"][0]
            self.assertEqual(context["predictions"]["journal_records"][0]["event_digest"], receipt["event_digest"])
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
        self.assertEqual(work_journal.canonical_json_bytes(event) + b"\n", (self.root / receipt["carrier"]).read_bytes())
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

    def test_actual_stored_event_identity_collision_refuses_without_rewriting_history(self) -> None:
        context = self._context(replacement=True)
        original = context["predictions"]["journal_records"][0]
        conflicting = copy.deepcopy(original)
        conflicting["successor_atom_ids"] = ["CA-D-633"]
        conflicting = work_journal.with_event_digest(conflicting)
        work_journal.append_sealed_events(self.root, [conflicting], author=context["author"],
                                         local_date=context["local_date"], timezone=context["timezone"])
        with self.assertRaises(work_journal.WorkJournalError) as refused:
            self._apply(context)
        self.assertEqual("identity-collision", refused.exception.code)
        self.assertEqual([conflicting], self._events())

    def _recovery_context(self) -> dict:
        context = self._context(replacement=True)
        result = copy.deepcopy(context["result"])
        evidence = {"git": {"base_commit": context["git_base"]["commit"]},
                    "carrier": {"path": result["path"], "sha256": result["sha256"]}}
        recovered = {key: context[key] for key in ("schema_version", "action_id", "author", "occurred_at", "llm_session", "structural_scope")}
        recovered.update(event="recovered", kind="governed_project_state", subject_kind="file", result=result, recovery_evidence=evidence)
        recovered["event_id"] = appender._expected_event_id(recovered)
        recovered = work_journal.with_event_digest(recovered)
        completed = context["predictions"]["journal_records"][0]
        completed["previous_result_event"] = recovered["event_id"]
        completed["event_id"] = appender._expected_event_id(completed)
        context["predictions"]["journal_records"] = [recovered, work_journal.with_event_digest(completed)]
        context["previous_result_event"] = recovered["event_id"]
        context["recovery"] = {"event_id": recovered["event_id"], "result": result, "evidence": evidence,
                               "evidence_digest": work_journal.canonical_json_digest(evidence), "contradictions": []}
        context["context_id"] = appender._expected_context_id(context)
        return context

    def test_actual_partial_append_is_pending_and_retry_does_not_replay_source(self) -> None:
        context = self._recovery_context()
        events = context["predictions"]["journal_records"]
        original = work_journal._append_locked
        artifact = self.fixture.artifact.read_bytes()

        def fail_second(root, event, *args, **kwargs):
            if event["event_id"] == events[1]["event_id"]:
                raise OSError("injected second-event storage failure")
            return original(root, event, *args, **kwargs)

        with patch.object(work_journal, "_append_locked", side_effect=fail_second):
            result = self._apply(context)
        self.assertFalse(result["ok"])
        self.assertEqual("recording_pending", result["result"]["state"])
        self.assertEqual([events[0]], self._events())
        self.assertEqual(events[0]["event_digest"], result["result"]["receipts"][0]["event_digest"])
        pending = list((self.root / ".caprmedio_runtime/state/work_journal/pending").glob("*.json"))
        self.assertTrue(pending)
        self.assertIn(events[1], [json.loads(json.loads(path.read_text())["event_bytes"]) for path in pending])
        with patch.object(appender, "run", side_effect=AssertionError("source workflow replayed")):
            retried = self._apply(context)
        self.assertTrue(retried["ok"])
        self.assertEqual(events, self._events())
        self.assertEqual(artifact, self.fixture.artifact.read_bytes())
        self.assertEqual([], list((self.root / ".caprmedio_runtime/state/work_journal/pending").glob("*.json")))

    def test_receipt_write_failure_retains_observed_append_and_retry_clears_pending(self) -> None:
        context = self._context(replacement=True)
        event = context["predictions"]["journal_records"][0]
        receipt_path = work_journal._receipt_path(self.root, event["event_id"])
        original = work_journal._atomic_json
        artifact = self.fixture.artifact.read_bytes()

        def fail_receipt(path, value):
            if path == receipt_path:
                raise OSError("injected receipt write failure after carrier append")
            return original(path, value)

        with patch.object(work_journal, "_atomic_json", side_effect=fail_receipt):
            result = self._apply(context)
        self.assertFalse(result["ok"])
        self.assertEqual("recording_pending", result["result"]["state"])
        self.assertEqual([event], self._events())
        receipts = result["result"]["receipts"]
        self.assertEqual(1, len(receipts))
        payload = work_journal.canonical_json_bytes(event) + b"\n"
        self.assertEqual({"event_id": event["event_id"], "action_id": event["action_id"],
                          "event_digest": event["event_digest"],
                          "carrier": ".caprmedio_caprmedio/_journal/test-user-2026-08-20-part-1.ndjson",
                          "line": 1, "previous_carrier_digest": hashlib.sha256(b"").hexdigest(),
                          "appended_carrier_digest": hashlib.sha256(payload).hexdigest()}, receipts[0])
        self.assertEqual(payload, (self.root / receipts[0]["carrier"]).read_bytes())
        self.assertEqual(event["event_digest"], result["result"]["pending_events"][0]["event_digest"])
        pending_dir = self.root / ".caprmedio_runtime/state/work_journal/pending"
        self.assertEqual(1, len(list(pending_dir.glob("*.json"))))
        with patch.object(appender, "run", side_effect=AssertionError("source workflow replayed")):
            retried = self._apply(context)
        self.assertTrue(retried["ok"])
        self.assertEqual([event], self._events())
        self.assertEqual(artifact, self.fixture.artifact.read_bytes())
        self.assertEqual([], list(pending_dir.glob("*.json")))

    def test_unsafe_settings_after_first_append_preserve_partial_receipt_and_refuse_outside_write(self) -> None:
        context = self._recovery_context()
        events = context["predictions"]["journal_records"]
        settings = self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        original_settings = settings.read_bytes()
        original_recover = appender.recover_pending_event
        first_receipts = []
        outside = self.root.parent / "outside"
        self.assertFalse(outside.exists())
        artifact = self.fixture.artifact.read_bytes()

        def invalidate_settings_after_first(root, event_id):
            receipt = original_recover(root, event_id)
            if event_id == events[0]["event_id"]:
                first_receipts.append(receipt)
                settings.write_bytes(original_settings.replace(
                    b'journal_root = ".caprmedio_caprmedio/_journal"', b'journal_root = "../outside"'))
            return receipt

        with patch.object(appender, "recover_pending_event", side_effect=invalidate_settings_after_first):
            result = self._apply(context)
        self.assertFalse(result["ok"])
        self.assertEqual("recording_pending", result["result"]["state"])
        self.assertEqual(first_receipts, result["result"]["receipts"])
        self.assertEqual(1, len(first_receipts))
        self.assertEqual(events[0]["event_digest"], first_receipts[0]["event_digest"])
        self.assertTrue(result["result"]["inspection_required"])
        self.assertTrue(result["result"]["pending_errors"])
        self.assertEqual([events[0]], self._events())
        self.assertFalse(outside.exists())
        settings.write_bytes(original_settings)
        with patch.object(appender, "run", side_effect=AssertionError("source workflow replayed")):
            retried = self._apply(context)
        self.assertTrue(retried["ok"])
        self.assertEqual(events, self._events())
        self.assertEqual(artifact, self.fixture.artifact.read_bytes())
        self.assertFalse(outside.exists())
        self.assertEqual([], list((self.root / ".caprmedio_runtime/state/work_journal/pending").glob("*.json")))

    def test_foreign_project_context_is_refused_before_any_append(self) -> None:
        foreign = native_tests.AppendChangeRecordsTest("test_dry_run_is_mutation_free")
        foreign.setUp()
        self.addCleanup(foreign.tearDown)
        context = foreign.context()
        with self.assertRaises(appender.ToolError) as refused:
            self._apply(context)
        self.assertEqual("descriptor-root-mismatch", refused.exception.code)
        self.assertEqual([], self._events())
        self.assertFalse((foreign.root / ".caprmedio_caprmedio/_journal").exists())
        self.assertFalse((self.root / ".caprmedio_runtime").exists())

    def test_closed_request_and_strict_apply_reject_before_writes(self) -> None:
        for request in ({}, {"context": self._context(), "root": str(self.root)},
                        {"context": self._context(), "wait_seconds": 0},
                        {"context": self._context(), "event": {}},
                        *({"context": self._context(), "apply": value} for value in (1, 0, "true", None))):
            with self.subTest(request=request):
                with self.assertRaises(ValidationError):
                    appender.AppendChangeRecordsRequest.model_validate(request)
        self.assertEqual([], self._events())
        self.assertFalse((self.root / ".caprmedio_runtime").exists())

    def test_event_digest_tamper_refuses_without_pending_or_append(self) -> None:
        context = self._context(replacement=True)
        context["predictions"]["journal_records"][0]["successor_atom_ids"] = ["CA-D-633"]
        with self.assertRaises(work_journal.WorkJournalError) as refused:
            self._apply(context)
        self.assertEqual("event-digest-mismatch", refused.exception.code)
        self.assertEqual([], self._events())
        self.assertFalse((self.root / ".caprmedio_runtime").exists())


if __name__ == "__main__":
    unittest.main()
