"""Lifecycle logging is plain append/read; source observations stay checked."""

import hashlib
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
for location in (APP, TOOLS):
    sys.path.insert(0, str(location))

from selected_lifecycle_journal import (  # noqa: E402
    LifecycleJournalError,
    admit_lifecycle_prior,
    prepare_lifecycle_journal,
    record_lifecycle_change,
)
from work_journal import append_sealed_events, read_records  # noqa: E402


class SelectedLifecycleJournalTest(unittest.TestCase):
    def setUp(self) -> None:
        temporary_root = APP.parents[3] / ".caprmedio_tmp/tests/plain-lifecycle-journal"
        temporary_root.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=temporary_root)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / ".git").mkdir()
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
            'journal_root = ".caprmedio_caprmedio/_journal"\n'
            'runtime_root = ".caprmedio_runtime"\n'
        )
        self.path = self.root / "atoms/current.md"
        self.path.parent.mkdir()
        self.path.write_bytes(b"before")
        self.context = {"author": "test-user", "local_date": "2026-10-14", "timezone": "UTC"}
        self.pin = {
            "action_id": "actual-action",
            "structural_scope": "CORE_META_MODEL",
            "occurred_at": "2026-10-14T00:00:00+00:00",
            "llm_session": {"app": "codex", "uuid": "test"},
        }

    def facts(self) -> dict:
        return {
            "filename": self.path.name,
            "version": 1,
            "path": self.path.relative_to(self.root).as_posix(),
            "sha256": hashlib.sha256(self.path.read_bytes()).hexdigest(),
        }

    def admission(self) -> dict:
        prepared = prepare_lifecycle_journal(
            self.root,
            self.facts(),
            self.path.read_bytes(),
            self.pin,
            "observed-run",
            self.context,
        )
        return dict(admit_lifecycle_prior(self.root, prepared, self.context))

    def change(
        self, observed: dict, action_type: str = "UPDATE", run_id: str = "actual-run"
    ) -> dict:
        return dict(
            record_lifecycle_change(
                self.root,
                before_result=observed["before_result"],
                after_facts=self.facts(),
                current_bytes=self.path.read_bytes(),
                action_pin=self.pin,
                run_id=run_id,
                context=self.context,
                action_type=action_type,
                native_effects={"result": {"state": "present", **self.facts()}},
            )
        )

    def test_each_actual_change_appends_one_record_without_baseline(self) -> None:
        for action_type in ("UPDATE", "MOVE", "MOVE+UPDATE"):
            observed = self.admission()
            if action_type != "UPDATE":
                destination = self.path.parent / "moved" / self.path.name
                destination.parent.mkdir()
                self.path.rename(destination)
                self.path = destination
            if action_type != "MOVE":
                self.path.write_bytes(self.path.read_bytes() + b"actual change")
            recorded = self.change(observed, action_type, action_type)
            self.assertEqual("admitted", recorded["state"])
            self.assertNotIn("previous_result_event", recorded["event"])
        rows = read_records(self.root)
        self.assertEqual(["UPDATE", "MOVE", "MOVE+UPDATE"], [row["action_type"] for row in rows])
        self.assertTrue(all(row["event"] == "completed" for row in rows))

    def test_existing_records_are_data_and_do_not_gate_the_next_change(self) -> None:
        historical = {"arbitrary": "historical observation", "previous_result_event": "unknown"}
        append_sealed_events(self.root, [historical, historical], **self.context)
        observed = self.admission()
        self.path.write_bytes(b"after")
        recorded = self.change(observed)
        self.assertEqual([historical, historical, recorded["event"]], read_records(self.root))

    def test_duplicate_logging_appends_again_without_replaying_source_effects(self) -> None:
        observed = self.admission()
        self.path.write_bytes(b"after")
        first = self.change(observed)
        second = self.change(observed)
        self.assertEqual([first["event"], second["event"]], read_records(self.root))
        self.assertEqual(b"after", self.path.read_bytes())

    def test_genuine_noop_creates_no_record(self) -> None:
        self.assertEqual("no_op", self.change(self.admission())["state"])
        self.assertEqual([], read_records(self.root))

    def test_source_readback_drift_is_still_refused(self) -> None:
        prepared = prepare_lifecycle_journal(
            self.root,
            self.facts(),
            self.path.read_bytes(),
            self.pin,
            "observed-run",
            self.context,
        )
        self.path.write_bytes(b"outside change")
        with self.assertRaises(LifecycleJournalError):
            admit_lifecycle_prior(self.root, prepared, self.context)

    def test_append_failure_reports_the_real_error_without_replaying_source(self) -> None:
        observed = self.admission()
        self.path.write_bytes(b"after")
        with patch("selected_lifecycle_journal.append_sealed_events", side_effect=OSError("full")):
            with self.assertRaises(OSError):
                self.change(observed)
        self.assertEqual(b"after", self.path.read_bytes())
        self.assertEqual([], read_records(self.root))


if __name__ == "__main__":
    unittest.main()
