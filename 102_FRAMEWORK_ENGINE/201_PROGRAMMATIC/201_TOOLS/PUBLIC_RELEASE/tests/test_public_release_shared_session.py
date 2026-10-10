"""Shared-session lineage coverage for the public-release executor."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


TOOLS = Path(__file__).resolve().parents[2]
PUBLIC_RELEASE = TOOLS / "PUBLIC_RELEASE"
for path in (str(TOOLS), str(PUBLIC_RELEASE), str(PUBLIC_RELEASE / "tests")):
    if path not in sys.path:
        sys.path.insert(0, path)

from public_release import PublicReleaseError, _run_evidence_ref, run, run_execution_session  # noqa: E402
from test_public_release import PublicReleaseTests  # noqa: E402
from workflow_run_support import RunTracker  # noqa: E402


class PublicReleaseSharedSessionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = PublicReleaseTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)

    def _execute_request(self) -> dict[str, object]:
        request = self.fixture.request()
        preview = run(self.fixture.root, request, bindings=self.fixture.bindings,
                      source_observer=self.fixture.observer)
        return {
            **request,
            "mode": "execute",
            "proposal_receipt": preview["proposal_receipt"],
            "proposal_receipt_digest": preview["proposal_receipt_digest"],
            "assigned_action_id": "CA-O-198",
            "operator_authorization": self.fixture.authorization(preview, request),
        }

    def test_reuses_admitted_session_without_an_inner_tracker(self) -> None:
        request = self._execute_request()
        observed = {}
        trace: list[dict[str, object]] = []

        def executor(_request, session) -> None:
            observed["session"] = session
            with mock.patch("public_release.RunTracker", side_effect=AssertionError("inner tracker")):
                trace.extend(run_execution_session(self.fixture.root, session, bindings=self.fixture.bindings))

        tracker = RunTracker(self.fixture.root, source_observer=self.fixture.observer, executor=executor)
        result = tracker.run_selected_operation(request)

        session = observed["session"]
        self.assertEqual(result["run_ids"], [run["run_id"] for run in session.actual.values()])
        self.assertEqual(9, len(trace))
        journal = next((self.fixture.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson"))
        terminal_events = [json.loads(line) for line in journal.read_text(encoding="utf-8").splitlines()
                           if json.loads(line)["event"] != "started"]
        self.assertEqual(11, len(terminal_events))
        for event in terminal_events:
            self.assertFalse(event["result_ref"].startswith("results/"))
            self.assertTrue((self.fixture.root / event["result_ref"]).is_file())

    def test_compatibility_wrapper_retains_the_complete_lineage(self) -> None:
        result = self.fixture.execute()

        self.assertEqual("terminal", result["disposition"])
        self.assertEqual(11, len(result["run_ids"]))
        self.assertEqual("CA-O-188", result["workflow"])
        self.assertEqual(9, len(result["tool_calls"]))

    def test_terminal_recording_failure_stops_before_the_next_binding(self) -> None:
        import workflow_run_support

        original = workflow_run_support.work_journal.append_sealed_events

        def fail_first_terminal(*args, **kwargs):
            if args[1][0]["event"] == "completed":
                raise OSError("simulated terminal append failure")
            return original(*args, **kwargs)

        with mock.patch("workflow_run_support.work_journal.append_sealed_events", side_effect=fail_first_terminal):
            result = self.fixture.execute()

        self.assertEqual("recording_pending", result["disposition"])
        self.assertEqual(["discover"], self.fixture.bindings.calls)
        self.assertEqual("inspect-or-recover-only", result["retry_disposition"])

    def test_run_evidence_refuses_symlinked_parent_or_existing_file(self) -> None:
        session = SimpleNamespace(tracker=SimpleNamespace(root=self.fixture.root), request={"request_id": "evidence-test"})
        run_record = {"run_id": "run-evidence", "kind": "action", "definition": {"atom_id": "CA-O-190"}}
        selected_runs = self.fixture.root / ".caprmedio_runtime/state/work_journal/selected_runs"
        selected_runs.parent.mkdir(parents=True)
        outside = self.fixture.root / "outside"
        outside.mkdir()
        selected_runs.symlink_to(outside, target_is_directory=True)
        with self.assertRaises(PublicReleaseError) as parent_error:
            _run_evidence_ref(session, run_record, outcome="completed")
        self.assertEqual("run-evidence-unavailable", parent_error.exception.code)
        selected_runs.unlink()

        reference = _run_evidence_ref(session, run_record, outcome="completed")
        evidence = self.fixture.root / reference
        payload = evidence.read_bytes()
        target = outside / "existing.json"
        target.write_bytes(payload)
        evidence.unlink()
        evidence.symlink_to(target)
        with self.assertRaises(PublicReleaseError) as file_error:
            _run_evidence_ref(session, run_record, outcome="completed")
        self.assertEqual("run-evidence-unavailable", file_error.exception.code)
        self.assertEqual(payload, target.read_bytes())

    def test_interrupted_or_failed_later_binding_retains_known_push_effect(self) -> None:
        def fail_upsert(*_args, **_kwargs):
            raise RuntimeError("simulated upsert failure")

        self.fixture.bindings.upsert_main_pr = fail_upsert
        result = self.fixture.execute()

        action_rows = [row for row in result["terminal_runs"] if "effects/push-initial.json" in row["effect_refs"]]
        self.assertTrue(action_rows)
        journal = next((self.fixture.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson"))
        terminal_by_atom = {
            event["run"]["definition"]["atom_id"]: event
            for event in (json.loads(line) for line in journal.read_text(encoding="utf-8").splitlines())
            if event["event"] != "started"
        }
        for atom_id in ("CA-O-188", "CA-O-195", "CA-O-196"):
            self.assertIn("effects/push-initial.json", terminal_by_atom[atom_id]["effect_refs"])
        self.assertEqual("started", result["disposition"])

    def test_interrupted_call_retains_its_partial_effect_reference(self) -> None:
        self.fixture.bindings.interrupt_push = True
        result = self.fixture.execute()

        action_rows = [row for row in result["terminal_runs"] if "effects/push-initial.json" in row["effect_refs"]]
        self.assertTrue(action_rows)
        self.assertEqual("started", result["disposition"])


if __name__ == "__main__":
    unittest.main()
