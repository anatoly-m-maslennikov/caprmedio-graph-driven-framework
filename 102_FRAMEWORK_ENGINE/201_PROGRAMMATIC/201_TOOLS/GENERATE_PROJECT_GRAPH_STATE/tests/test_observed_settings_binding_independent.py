"""Settings authority is independent from optional plain log metadata."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

SCRIPT = Path(__file__).resolve().parents[1] / "generate_project_graph_state.py"
SPEC = importlib.util.spec_from_file_location("observed_settings_independent_graph", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
graph = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = graph
SPEC.loader.exec_module(graph)
SCRATCH = SCRIPT.parents[4] / ".caprmedio_tmp/tests/observed-settings-independent"


class ObservedSettingsBindingIndependentTests(unittest.TestCase):
    def setUp(self):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=SCRATCH)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.control = self.root / ".caprmedio_caprmedio"
        self.project = self.root / graph.SETTINGS_PATH
        self.project.parent.mkdir(parents=True)
        self.project.write_text(
            "[project]\nkey='different-key'\nname='independent'\nrepository_slug='fixture'\n"
            "[artifacts.identity]\nproject_prefix='TEST'\n",
            encoding="utf-8",
        )
        self.framework = self.control / "000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"
        self.framework.parent.mkdir()
        self.framework.write_text(
            "[authority_modes]\ndefault='casual'\ngovernance='strict'\n"
            "metamodel='strict'\nproject='strict'\nsemantics='strict'\n",
            encoding="utf-8",
        )
        self.journal = self.control / "_journal"
        self.journal.mkdir()
        patch = mock.patch.multiple(
            graph,
            ROOT=self.root,
            CONTROL=self.control,
            CONFIG=self.framework,
            JOURNAL=self.journal,
        )
        patch.start()
        self.addCleanup(patch.stop)

    def record(self, carrier, **metadata):
        return {
            "result": {
                "path": carrier.relative_to(self.root).as_posix(),
                "sha256": graph.sha(carrier),
            },
            **metadata,
        }

    def write_records(self, records, name="observations.ndjson"):
        carrier = self.journal / name
        carrier.write_text("".join(json.dumps(row) + "\n" for row in records), encoding="utf-8")
        return carrier

    def read(self):
        before = {
            path.relative_to(self.root): path.read_bytes()
            for path in self.root.rglob("*")
            if path.is_file()
        }
        bindings = graph.settings_bindings()
        after = {
            path.relative_to(self.root): path.read_bytes()
            for path in self.root.rglob("*")
            if path.is_file()
        }
        self.assertEqual(before, after)
        for kind, carrier in (
            ("project_settings", self.project),
            ("framework_settings", self.framework),
        ):
            self.assertEqual(carrier.stem, bindings[kind]["identifier"])
            self.assertEqual(carrier.relative_to(self.root).as_posix(), bindings[kind]["carrier"])
            self.assertEqual(graph.sha(carrier), bindings[kind]["sha256"])
        return bindings

    def test_empty_history_remains_unknown_without_blocking_settings(self):
        for binding in self.read().values():
            self.assertEqual("unresolved", binding["status"])
            self.assertEqual("unknown", binding["revision"])
        self.assertEqual("independent", graph.configuration()["project"]["name"])

    def test_unavailable_optional_history_does_not_block_current_authority(self):
        with mock.patch.object(
            graph, "journal_records", side_effect=PermissionError("unavailable")
        ):
            bindings = self.read()
        self.assertTrue(all(item["status"] == "unresolved" for item in bindings.values()))
        self.assertEqual("independent", graph.configuration()["project"]["name"])

    def test_plain_matching_rows_need_no_schema_digest_or_recovery_proof(self):
        records = [
            self.record(self.project, event_id="project-row"),
            self.record(self.framework, event_id="framework-row"),
        ]
        records[0]["result"]["version"] = 7
        records[0]["occurred_at"] = "2026-10-13T18:04:05+04:00"
        location = self.write_records(records)
        bindings = self.read()
        self.assertEqual("7", bindings["project_settings"]["revision"])
        self.assertEqual("2026-10-13 18:04:05", bindings["project_settings"]["updated_at"])
        self.assertEqual("unknown", bindings["framework_settings"]["revision"])
        for line, kind in enumerate(("project_settings", "framework_settings"), 1):
            self.assertEqual("resolved", bindings[kind]["status"])
            self.assertEqual(str(line), bindings[kind]["journal_line"])
            self.assertEqual(
                location.relative_to(self.root).as_posix(), bindings[kind]["journal_carrier"]
            )

    def test_arbitrary_unrelated_rows_do_not_obscure_matching_data(self):
        location = self.write_records(
            [None, [], 5, "text", {"result": []}, {"unknown": True}, self.record(self.framework)]
        )
        location.write_text(location.read_text() + "not-json\n", encoding="utf-8")
        bindings = self.read()
        self.assertEqual("unresolved", bindings["project_settings"]["status"])
        self.assertEqual("resolved", bindings["framework_settings"]["status"])
        self.assertEqual("7", bindings["framework_settings"]["journal_line"])

    def test_log_labels_and_claimed_proofs_do_not_grant_authority(self):
        record = self.record(
            self.framework,
            schema_version="arbitrary",
            event="recovered",
            event_digest="not a proof",
            recovery_evidence=None,
            structural_scope="another-project",
        )
        self.write_records([record])
        binding = self.read()["framework_settings"]
        self.assertEqual("resolved", binding["status"])
        self.assertEqual("unknown", binding["revision"])
        self.assertEqual("", binding["updated_at"])
        self.assertEqual("independent", graph.configuration()["project"]["name"])

    def test_current_path_and_hash_still_select_optional_metadata(self):
        wrong_path = self.record(self.project)
        wrong_path["result"]["path"] = "other/settings.toml"
        wrong_hash = self.record(self.framework)
        wrong_hash["result"]["sha256"] = "0" * 64
        self.write_records([wrong_path, wrong_hash])
        self.assertTrue(all(item["status"] == "unresolved" for item in self.read().values()))

    def test_stale_current_bytes_do_not_acquire_old_history_metadata(self):
        record = self.record(self.framework)
        self.write_records([record])
        self.framework.write_text(self.framework.read_text() + "\n# current drift\n")
        self.assertEqual("unresolved", self.read()["framework_settings"]["status"])
        direct = graph.configuration_binding(record["result"]["sha256"], self.framework)
        self.assertEqual("unresolved", direct["status"])

    def test_duplicate_matches_are_unknown_metadata_not_an_authority_failure(self):
        record = self.record(self.framework)
        self.write_records([record, record])
        binding = self.read()["framework_settings"]
        self.assertEqual("ambiguous", binding["status"])
        self.assertEqual("unknown", binding["revision"])
        self.assertEqual("independent", graph.configuration()["project"]["name"])

    def test_missing_current_file_cannot_be_bound_by_a_log_row(self):
        record = self.record(self.framework)
        self.write_records([record])
        self.framework.unlink()
        binding = graph.configuration_binding(record["result"]["sha256"], self.framework)
        self.assertEqual("unresolved", binding["status"])


if __name__ == "__main__":
    unittest.main()
