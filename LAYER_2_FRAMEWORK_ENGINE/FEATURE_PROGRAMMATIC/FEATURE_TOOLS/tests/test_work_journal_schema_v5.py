"""Workflow-shaped metadata remains plain data at the Journal boundary."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import work_journal  # noqa: E402


class WorkJournalSchemaV5Test(unittest.TestCase):
    def setUp(self) -> None:
        temporary_root = TOOLS.parents[2] / ".caprmedio_tmp/tests/work_journal_metadata"
        temporary_root.mkdir(parents=True, exist_ok=True)
        self.directory = tempfile.TemporaryDirectory(dir=temporary_root)
        self.root = Path(self.directory.name)
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            "[paths]\n"
            'control_root = ".caprmedio_caprmedio"\n'
            'journal_root = ".caprmedio_caprmedio/_journal"\n'
            'runtime_root = ".caprmedio_runtime"\n',
            encoding="utf-8",
        )
        self.event = self._event()

    def tearDown(self) -> None:
        self.directory.cleanup()

    def _event(self) -> dict[str, object]:
        event: dict[str, object] = {
            "schema_version": 5,
            "kind": "workflow_execution",
            "event_id": "event-1510",
            "action_id": "action-1510",
            "event": "completed",
            "author": "test-user",
            "occurred_at": "2026-10-04T19:15:00+04:00",
            "llm_session": {"app": "codex", "uuid": "session-1510"},
            "structural_scope": "TOOLS",
            "initiative": {
                "initiative_id": "initiative-1510",
                "instruction_summary": "record one selected run",
                "initiative_ref": "03_plan/CA-P-1510.md",
            },
            "run": {
                "run_id": "run-1510",
                "kind": "action",
                "definition": {
                    "atom_id": "CA-O-1510",
                    "version": 1,
                    "path": "operations/CA-O-1510.md",
                    "digest": "a" * 64,
                },
            },
            "definition_bindings": [
                {
                    "kind": "action",
                    "atom_id": "CA-O-1510",
                    "version": 1,
                    "path": "operations/CA-O-1510.md",
                    "digest": "a" * 64,
                }
            ],
            "input_ref": "inputs/CA-I-1510.json",
            "outcome": "completed",
            "result_ref": "results/CA-R-1510.json",
            "effect_refs": ["03_plan/result.md"],
            "report_ref": "reports/CA-R-1510.md",
            "redaction": {"redacted": False, "fields": []},
        }
        return work_journal.with_event_digest(event)

    def test_configured_root_defaults_to_exact_generic_control_journal(self) -> None:
        (self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").unlink()
        control = self.root / ".caprmedio_example"
        control.mkdir()
        settings = control / "caprmedio_project_settings.toml"
        settings.write_text(
            '[paths]\ncontrol_root = ".caprmedio_example"\nruntime_root = ".caprmedio_runtime"\n',
            encoding="utf-8",
        )

        self.assertEqual(
            Path(".caprmedio_example/_journal"),
            work_journal.configured_journal_root(self.root),
        )

        settings.write_text(
            "[paths]\n"
            'control_root = ".caprmedio_example"\n'
            'journal_root = ".caprmedio_example/work_journal"\n'
            'runtime_root = ".caprmedio_runtime"\n',
            encoding="utf-8",
        )
        with self.assertRaisesRegex(RuntimeError, "exactly"):
            work_journal.configured_journal_root(self.root)

    def test_workflow_metadata_is_not_validated_or_rewritten(self) -> None:
        changed = {**self.event, "event_digest": "caller supplied", "outcome": "unknown"}
        rows = [self.event, changed]
        work_journal.append_sealed_events(
            self.root, rows, author="test-user", local_date="2026-10-04", timezone="UTC"
        )
        self.assertEqual(rows, work_journal.read_records(self.root))

    def test_legacy_directory_bytes_do_not_gate_current_append(self) -> None:
        legacy = self.root / ".caprmedio_caprmedio/work_journal"
        legacy.mkdir()
        path = legacy / "historical.ndjson"
        original = b"existing historical bytes\n"
        path.write_bytes(original)
        work_journal.append_sealed_events(
            self.root, [self.event], author="test-user", local_date="2026-10-04", timezone="UTC"
        )
        self.assertEqual([self.event], work_journal.read_records(self.root))
        self.assertEqual(original, path.read_bytes())
        self.assertFalse((self.root / ".caprmedio_runtime").exists())


if __name__ == "__main__":
    unittest.main()
