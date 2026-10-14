"""Plain publication observations are independent of source-effect admission."""
from __future__ import annotations

import datetime as dt
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

MCP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP))
import release_manifest_lifecycle as lifecycle
import source_admission_mcp as admission
import work_journal


class ManifestPlainLoggingTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        settings = self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        settings.parent.mkdir()
        settings.write_text('[paths]\ncontrol_root=".caprmedio_caprmedio"\n'
                            'journal_root=".caprmedio_caprmedio/_journal"\n')
        self.manifest = self.root / "selected.json"
        self.manifest.write_bytes(b'{"actual":"published"}')
        self.plan = {"manifest_ref": "selected.json", "candidate_canonical_manifest_sha256": "a" * 64}
        self.context = SimpleNamespace(journal_author="fixture author", llm_session={"app": "test", "uuid": "actual"})
        self.log = lifecycle.ReleaseManifestLifecycle(self.root, self.context)

    def record(self):
        with patch.object(self.log, "_plan_from_result", return_value=self.plan), patch.object(
            lifecycle, "_canonical_intent", return_value={"plan": self.plan},
        ), patch.object(lifecycle, "_now", return_value=dt.datetime(2026, 10, 14, tzinfo=dt.UTC)):
            return self.log.record_release_manifest_publication({"published": True})

    def test_actual_observation_appends_repeats_without_prior_or_receipt(self):
        self.record()
        self.record()
        rows = work_journal.read_records(self.root)
        self.assertEqual(2, len(rows))
        self.assertEqual(rows[0], rows[1])
        self.assertEqual("selected.json", rows[0]["result"]["path"])
        self.assertFalse({"previous_result_event", "event_digest", "baseline"} & set(rows[0]))
        self.assertFalse((self.root / ".caprmedio_runtime/state/work_journal").exists())

    def test_append_error_is_reported_without_source_mutation_or_retry(self):
        before = self.manifest.read_bytes()
        with patch.object(work_journal, "append_sealed_events", side_effect=OSError("log unavailable")):
            result = self.record()
        self.assertEqual("log unavailable", result["recording_error"])
        self.assertNotIn("recording_ref", result)
        self.assertEqual(before, self.manifest.read_bytes())
        self.assertEqual([], work_journal.read_records(self.root))

    def test_source_admission_terminal_preserves_actual_result_and_log_diagnostic(self):
        terminal = {"disposition": "terminal", "run_id": "actual-run", "outcome": "completed",
                    "result_ref": "admission.json", "effect_refs": ["command.json", "admission.json", "catalog.json"],
                    "recording_errors": ["log unavailable"]}
        result = admission._terminal_transport(self.root, terminal, command_receipt_ref="command.json",
                                              admission_receipt_ref="admission.json", catalog_ref="catalog.json",
                                              action_run_id="actual-run")
        self.assertEqual("completed", result["outcome"])
        self.assertEqual(["log unavailable"], result["recording_errors"])
        with self.assertRaises(admission.SourceAdmissionMcpError):
            admission._terminal_transport(self.root, {**terminal, "effect_refs": []},
                                          command_receipt_ref="command.json", admission_receipt_ref="admission.json",
                                          catalog_ref="catalog.json", action_run_id="actual-run")
