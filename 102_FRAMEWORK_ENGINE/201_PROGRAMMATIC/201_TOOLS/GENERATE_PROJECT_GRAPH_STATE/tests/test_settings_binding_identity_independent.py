"""Independent regression: Settings identity and Journal receipt identity differ."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock


SCRIPT = Path(__file__).resolve().parents[1] / "generate_project_graph_state.py"
SPEC = importlib.util.spec_from_file_location("settings_identity_independent_graph", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
graph = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = graph
SPEC.loader.exec_module(graph)
SCRATCH = Path.cwd() / ".caprmedio_tmp" / "tests" / "settings-identity-independent"


class SettingsBindingIdentityIndependentTests(unittest.TestCase):
    def setUp(self):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=SCRATCH)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.control = self.root / ".caprmedio_caprmedio"
        self.project = self.root / graph.SETTINGS_PATH
        self.project.parent.mkdir(parents=True)
        self.project.write_text("[project]\nkey='caprmedio'\nname='caprmedio'\nrepository_slug='fixture'\n"
                                "[artifacts.identity]\nproject_prefix='TEST'\n", encoding="utf-8")
        self.framework = self.control / "000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"
        self.framework.parent.mkdir()
        self.framework.write_text("[authority_modes]\ndefault='casual'\ngovernance='strict'\n"
                                  "metamodel='strict'\nproject='strict'\nsemantics='strict'\n", encoding="utf-8")
        self.journal = self.control / "_journal"
        self.journal.mkdir()
        patch = mock.patch.multiple(graph, ROOT=self.root, CONTROL=self.control,
                                    CONFIG=self.framework, JOURNAL=self.journal)
        patch.start()
        self.addCleanup(patch.stop)
        self.assertEqual(graph.configuration()["project"]["name"], "caprmedio")

    def record(self, path, version, event_id):
        return {"kind": "governed_project_change", "event": "completed", "subject_kind": "file",
                "occurred_at": "2026-10-13 05:00:00 +0400", "event_id": event_id,
                "result": {"path": path.relative_to(self.root).as_posix(), "sha256": graph.sha(path),
                           "version": version}}

    def write_journal(self, name, records):
        path = self.journal / name
        path.write_text("\n".join(json.dumps(record) for record in records) + "\n", encoding="utf-8")
        return path

    def read_bindings(self):
        paths = [self.project, self.framework, *self.journal.glob("*.ndjson")]
        before = {path: path.read_bytes() for path in paths}
        bindings = graph.settings_bindings()
        self.assertEqual(before, {path: path.read_bytes() for path in paths})
        for kind, path in (("project_settings", self.project), ("framework_settings", self.framework)):
            self.assertEqual(bindings[kind]["carrier"], path.relative_to(self.root).as_posix())
            self.assertEqual(bindings[kind]["sha256"], graph.sha(path))
        return bindings

    def assert_identity(self, binding, path, status):
        self.assertEqual(binding["identifier"], path.stem)
        self.assertEqual(binding["status"], status)
        if status != "resolved":
            self.assertEqual(binding["revision"], "unknown")
            for field in ("journal_carrier", "journal_line", "journal_event_id", "updated_at"):
                self.assertEqual(binding[field], "")

    def test_empty_journal_keeps_explicit_and_default_requested_identities(self):
        bindings = self.read_bindings()
        for kind, path in (("project_settings", self.project), ("framework_settings", self.framework)):
            self.assert_identity(bindings[kind], path, "unresolved")
        self.assert_identity(graph.configuration_binding(graph.sha(self.project), self.project),
                             self.project, "unresolved")
        self.assert_identity(graph.configuration_binding(graph.sha(self.framework)), self.framework, "unresolved")

    def test_unrelated_multiple_journals_do_not_replace_settings_identities(self):
        self.write_journal("aa-empty.ndjson", [])
        wrong_path = self.record(self.project, 7, "unrelated-path")
        wrong_path["result"]["path"] = "some/other/settings.toml"
        wrong_digest = self.record(self.framework, 8, "unrelated-digest")
        wrong_digest["result"]["sha256"] = "0" * 64
        self.write_journal("zz-unrelated.ndjson", [None, [], wrong_path, wrong_digest])
        bindings = self.read_bindings()
        self.assert_identity(bindings["project_settings"], self.project, "unresolved")
        self.assert_identity(bindings["framework_settings"], self.framework, "unresolved")

    def test_resolved_pair_preserves_requested_identity_and_exact_receipt_evidence(self):
        receipt = self.write_journal("receipt-not-settings.ndjson", [
            None, self.record(self.project, 7, "project-receipt"),
            self.record(self.framework, 11, "framework-receipt"),
        ])
        self.write_journal("zz-later-empty.ndjson", [])
        bindings = self.read_bindings()
        for kind, path, version, line, event in (
            ("project_settings", self.project, 7, 2, "project-receipt"),
            ("framework_settings", self.framework, 11, 3, "framework-receipt"),
        ):
            item = bindings[kind]
            self.assert_identity(item, path, "resolved")
            self.assertEqual(item["revision"], str(version))
            self.assertEqual(item["journal_carrier"], receipt.relative_to(self.root).as_posix())
            self.assertEqual(item["journal_line"], str(line))
            self.assertEqual(item["journal_event_id"], event)
            self.assertEqual(item["updated_at"], "2026-10-13 05:00:00")
        direct = graph.configuration_binding(graph.sha(self.framework))
        self.assert_identity(direct, self.framework, "resolved")
        self.assertEqual(direct["journal_event_id"], "framework-receipt")

    def test_ambiguous_project_receipts_do_not_affect_framework_identity_or_receipt(self):
        first = self.write_journal("aa-first.ndjson", [
            self.record(self.project, 7, "project-first"), self.record(self.framework, 11, "framework-only"),
        ])
        self.write_journal("zz-second.ndjson", [self.record(self.project, 7, "project-second")])
        bindings = self.read_bindings()
        self.assert_identity(bindings["project_settings"], self.project, "ambiguous")
        self.assert_identity(bindings["framework_settings"], self.framework, "resolved")
        self.assertEqual(bindings["framework_settings"]["journal_carrier"], first.relative_to(self.root).as_posix())
        self.assertEqual(bindings["framework_settings"]["journal_line"], "2")
        self.assertEqual(bindings["framework_settings"]["journal_event_id"], "framework-only")

    def test_default_framework_identity_is_retained_for_ambiguous_receipts(self):
        self.write_journal("aa-one.ndjson", [self.record(self.framework, 11, "one")])
        self.write_journal("zz-two.ndjson", [self.record(self.framework, 11, "two")])
        self.assert_identity(graph.configuration_binding(graph.sha(self.framework)), self.framework, "ambiguous")
        bindings = self.read_bindings()
        self.assert_identity(bindings["framework_settings"], self.framework, "ambiguous")
        self.assert_identity(bindings["project_settings"], self.project, "unresolved")

    def test_current_digest_drift_does_not_change_requested_identity(self):
        self.write_journal("old-settings-receipts.ndjson", [
            self.record(self.project, 7, "old-project"), self.record(self.framework, 11, "current-framework"),
        ])
        self.project.write_text(self.project.read_text(encoding="utf-8") + "\n# changed source\n", encoding="utf-8")
        bindings = self.read_bindings()
        self.assert_identity(bindings["project_settings"], self.project, "unresolved")
        self.assert_identity(bindings["framework_settings"], self.framework, "resolved")
        self.assertEqual(bindings["framework_settings"]["journal_event_id"], "current-framework")


if __name__ == "__main__":
    unittest.main()
