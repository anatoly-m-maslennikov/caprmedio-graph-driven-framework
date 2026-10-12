"""Read-only provenance tests for recorded selected Action starts."""

from __future__ import annotations

import json
import os
import stat
import sys
import tempfile
import unittest
from contextlib import nullcontext
from pathlib import Path
from unittest import mock


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import work_journal  # noqa: E402
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

    def test_symlinked_journal_root_or_carrier_ancestor_refuses_before_carrier_read(self) -> None:
        for case in ("root", "ancestor"):
            with self.subTest(case=case):
                session, action_run_id = self._session()
                carrier = self._carrier()
                if case == "root":
                    journal = carrier.parent.resolve()
                    original_lstat = os.lstat

                    def swapped_journal_root(path, *args, **kwargs):
                        if Path(path) == journal:
                            return mock.Mock(st_mode=stat.S_IFLNK | 0o777)
                        return original_lstat(path, *args, **kwargs)

                    lstat_guard = mock.patch("workflow_run_support.os.lstat", side_effect=swapped_journal_root)
                else:
                    alias = carrier.parent / "carrier-alias"
                    alias.symlink_to(carrier.parent, target_is_directory=True)
                    session._started_receipts["action"]["carrier"] = (
                        f".caprmedio_caprmedio/_journal/carrier-alias/{carrier.name}"
                    )
                    lstat_guard = nullcontext()
                with lstat_guard, mock.patch("workflow_run_support.work_journal._carrier_records", side_effect=AssertionError("reader invoked")):
                    with self.assertRaises(SelectedRunError) as refused:
                        session.read_recorded_action_start(action_run_id)
                self.assertEqual("action-start-evidence-invalid", refused.exception.code)

    def test_missing_tampered_wrong_parent_and_wrong_run_refuse_without_replay(self) -> None:
        cases = (
            ("missing", self._remove_started_event, "action-start-evidence-missing"),
            ("tampered", self._tamper_event_bytes, "action-start-evidence-invalid"),
            ("wrong-parent", self._rewrite_parent, "action-start-evidence-mismatch"),
            ("wrong-run", self._rewrite_run, "action-start-evidence-mismatch"),
        )
        for _name, mutate, code in cases:
            with self.subTest(case=_name):
                session, action_run_id = self._session()
                carrier = self._carrier()
                mutate(carrier)
                before = carrier.read_bytes() if carrier.exists() else b""
                before_parts = tuple(sorted(carrier.parent.glob("*.ndjson"))) if carrier.parent.exists() else ()

                with self.assertRaises(SelectedRunError) as refused:
                    session.read_recorded_action_start(action_run_id)

                self.assertEqual(code, refused.exception.code)
                self.assertEqual(before, carrier.read_bytes() if carrier.exists() else b"")
                self.assertEqual(before_parts, tuple(sorted(carrier.parent.glob("*.ndjson"))) if carrier.parent.exists() else ())

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
        events[-1] = work_journal.with_event_digest(events[-1])
        carrier.write_text("\n".join(json.dumps(event, sort_keys=True) for event in events) + "\n", encoding="utf-8")

    @staticmethod
    def _rewrite_run(carrier: Path) -> None:
        events = [json.loads(line) for line in carrier.read_text(encoding="utf-8").splitlines()]
        events[-1]["run"]["run_id"] = "different-action-run"
        events[-1] = work_journal.with_event_digest(events[-1])
        carrier.write_text("\n".join(json.dumps(event, sort_keys=True) for event in events) + "\n", encoding="utf-8")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
