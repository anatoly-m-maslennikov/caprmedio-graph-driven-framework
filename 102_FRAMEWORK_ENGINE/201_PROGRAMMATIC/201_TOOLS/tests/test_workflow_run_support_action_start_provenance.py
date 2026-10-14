"""Read-only provenance tests for recorded selected Action starts."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from workflow_run_support import (  # noqa: E402
    RunExecutionSession,
    RunTracker,
    SelectedRunError,
)


class RecordedActionStartProvenanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.root = Path(self.directory.name)
        (self.root / ".git").mkdir()
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            "[paths]\n"
            'control_root = ".caprmedio_caprmedio"\n'
            'journal_root = ".caprmedio_caprmedio/_journal"\n'
            'runtime_root = ".caprmedio_runtime"\n',
            encoding="utf-8",
        )
        self.tracker = RunTracker(
            self.root,
            source_observer=lambda _request: {"selected": True, "current": True, "observed": {}},
            executor=lambda _request, _runs: {"outcome": "no_op", "result_ref": "results/no-op.json", "effect_refs": []},
            journal_context={"author": "trusted-operator", "timezone": "UTC"},
        )

    def tearDown(self) -> None:
        self.directory.cleanup()

    @staticmethod
    def _definition(kind: str, atom_id: str) -> dict[str, object]:
        return {"atom_id": atom_id, "version": 1, "path": f"operations/{atom_id}.md", "digest": "a" * 64}

    def _session(self) -> tuple[RunExecutionSession, str]:
        request = {
            "request_id": "recorded-action-start",
            "assigned_action_id": "assigned-action-is-not-provenance",
            "initiative": {"initiative_id": "initiative", "instruction_summary": "record the Action start"},
            "requested_runs": [
                {"requested_run_id": "workflow", "kind": "workflow", "definition": self._definition("workflow", "CA-O-1")},
                {
                    "requested_run_id": "step",
                    "kind": "step",
                    "definition": self._definition("step", "CA-O-2"),
                    "parent_requested_run_id": "workflow",
                },
                {
                    "requested_run_id": "action",
                    "kind": "action",
                    "definition": self._definition("action", "CA-O-3"),
                    "parent_requested_run_id": "step",
                },
            ],
        }
        session = RunExecutionSession(self.tracker, request)
        session.start_run("workflow", run_id="actual-workflow")
        session.start_run("step", run_id="actual-step")
        action = session.start_run("action", run_id="actual-action")
        return session, action["run_id"]

    def _carrier(self) -> Path:
        return next((self.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson"))

    def test_reopens_the_same_session_recorded_action_start_without_new_journal_effect(self) -> None:
        session, action_run_id = self._session()
        session.finish_run(
            action_run_id,
            outcome="completed",
            result_ref="results/action.json",
            effect_refs=[],
        )
        carrier = self._carrier()
        before = carrier.read_bytes()
        before_parts = tuple(sorted(carrier.parent.glob("*.ndjson")))

        provenance = session.read_recorded_action_start(action_run_id)

        self.assertEqual("trusted-operator", provenance.author)
        self.assertEqual(action_run_id, provenance.action_run_id)
        self.assertEqual(("actual-step", "actual-workflow"), provenance.parent_lineage)
        self.assertTrue(provenance.event_id.startswith("event-"))
        self.assertFalse(hasattr(provenance, "action_id"))
        self.assertEqual(before, carrier.read_bytes())
        self.assertEqual(before_parts, tuple(sorted(carrier.parent.glob("*.ndjson"))))
        self.assertEqual(["started", "started", "started", "completed"], [
            json.loads(line)["event"] for line in before.decode("utf-8").splitlines()
        ])
        session.start_event_ids.clear()
        self.assertIsNone(session.read_recorded_action_start(action_run_id).event_id)
        self.assertEqual(before, carrier.read_bytes())

    def test_provenance_does_not_follow_a_replaced_journal_root(self) -> None:
        session, action_run_id = self._session()
        expected = session.read_recorded_action_start(action_run_id)
        journal = self._carrier().parent
        retained = journal.with_name("retained-journal")
        journal.rename(retained)
        journal.symlink_to(retained, target_is_directory=True)
        before = {path.name: path.read_bytes() for path in retained.glob("*.ndjson")}
        self.assertEqual(expected, session.read_recorded_action_start(action_run_id))
        self.assertEqual(
            before, {path.name: path.read_bytes() for path in retained.glob("*.ndjson")}
        )

    def test_missing_or_changed_log_does_not_replace_actual_provenance_or_replay(self) -> None:
        cases = (
            ("missing", self._remove_started_event),
            ("tampered", self._tamper_event_bytes),
            ("wrong-parent", self._rewrite_parent),
            ("wrong-run", self._rewrite_run),
        )
        for _name, mutate in cases:
            with self.subTest(case=_name):
                session, action_run_id = self._session()
                expected = session.read_recorded_action_start(action_run_id)
                actual = json.dumps(session.actual, sort_keys=True)
                carrier = self._carrier()
                mutate(carrier)
                before = carrier.read_bytes() if carrier.exists() else b""
                before_parts = (
                    tuple(sorted(carrier.parent.glob("*.ndjson")))
                    if carrier.parent.exists()
                    else ()
                )

                self.assertEqual(expected, session.read_recorded_action_start(action_run_id))
                self.assertEqual(actual, json.dumps(session.actual, sort_keys=True))
                self.assertEqual(before, carrier.read_bytes() if carrier.exists() else b"")
                self.assertEqual(
                    before_parts,
                    tuple(sorted(carrier.parent.glob("*.ndjson")))
                    if carrier.parent.exists()
                    else (),
                )

    def test_only_actual_action_runs_with_complete_acyclic_lineage_are_read(self) -> None:
        for case in ("unknown", "non-action", "missing-parent", "cycle"):
            with self.subTest(case=case):
                session, run = self._session()
                expected = "action-start-lineage-invalid"
                if case == "unknown":
                    run, expected = "never-started", "unknown-run"
                elif case == "non-action":
                    session.actual["action"]["kind"] = "workflow"
                    expected = "action-start-run-invalid"
                elif case == "missing-parent":
                    session.actual.pop("step")
                else:
                    session.actual["action"]["parent_run_id"] = run
                before = self._carrier().read_bytes()
                with self.assertRaises(SelectedRunError) as refused:
                    session.read_recorded_action_start(run)
                self.assertEqual(expected, refused.exception.code)
                self.assertEqual(before, self._carrier().read_bytes())

    @staticmethod
    def _remove_started_event(carrier: Path) -> None:
        carrier.unlink()

    @staticmethod
    def _tamper_event_bytes(carrier: Path) -> None:
        events = [json.loads(line) for line in carrier.read_text(encoding="utf-8").splitlines()]
        events[-1]["author"] = "tampered-author"
        carrier.write_text("\n".join(json.dumps(event, sort_keys=True) for event in events) + "\n", encoding="utf-8")

    @staticmethod
    def _rewrite_parent(carrier: Path) -> None:
        events = [json.loads(line) for line in carrier.read_text(encoding="utf-8").splitlines()]
        events[-1]["run"]["parent_run_id"] = "different-parent"
        carrier.write_text("\n".join(json.dumps(event, sort_keys=True) for event in events) + "\n", encoding="utf-8")

    @staticmethod
    def _rewrite_run(carrier: Path) -> None:
        events = [json.loads(line) for line in carrier.read_text(encoding="utf-8").splitlines()]
        events[-1]["run"]["run_id"] = "different-action-run"
        carrier.write_text("\n".join(json.dumps(event, sort_keys=True) for event in events) + "\n", encoding="utf-8")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
