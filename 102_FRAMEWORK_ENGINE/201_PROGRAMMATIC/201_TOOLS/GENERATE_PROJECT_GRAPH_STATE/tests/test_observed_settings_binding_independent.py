"""Independent Settings bindings use registered, sealed Journal evidence."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "generate_project_graph_state.py"
SPEC = importlib.util.spec_from_file_location("observed_settings_independent_graph", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
graph = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = graph
SPEC.loader.exec_module(graph)

import work_journal  # noqa: E402


SCRATCH = Path.cwd() / ".caprmedio_tmp/tests/observed-settings-independent"
OBSERVED_AT = "2026-10-13T18:04:05+04:00"


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
            "[artifacts.identity]\nproject_prefix='TEST'\n"
            "[paths]\ncontrol_root='.caprmedio_caprmedio'\n"
            "journal_root='.caprmedio_caprmedio/_journal'\nruntime_root='.caprmedio_runtime'\n",
            encoding="utf-8",
        )
        self.framework = self.control / "000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"
        self.framework.parent.mkdir()
        self.framework.write_text("[authority_modes]\ndefault='casual'\n", encoding="utf-8")
        self.journal = self.control / "_journal"
        self.journal.mkdir()
        original = {key: getattr(graph, key) for key in ("ROOT", "CONTROL", "CONFIG", "JOURNAL")}
        for key, value in dict(ROOT=self.root, CONTROL=self.control,
                               CONFIG=self.framework, JOURNAL=self.journal).items():
            setattr(graph, key, value)
        self.addCleanup(lambda: [setattr(graph, key, value) for key, value in original.items()])
        self.assertEqual("independent", graph.project_identity(self.root)["project"]["name"])

    def event(self, carrier, lifecycle="recovered", event_id="settings-evidence", version=7):
        relative = carrier.relative_to(self.root).as_posix()
        value = {
            "schema_version": 3, "event_id": event_id, "action_id": "action-settings",
            "event": lifecycle,
            "kind": "governed_project_state" if lifecycle == "recovered" else "governed_project_change",
            "subject_kind": "file", "author": "test-user", "occurred_at": OBSERVED_AT,
            "llm_session": {"app": "codex", "uuid": "isolated-settings-test"},
            "structural_scope": "independent",
            "result": {"state": "present", "filename": carrier.name, "version": version,
                       "path": relative, "sha256": graph.sha(carrier)},
        }
        if lifecycle == "recovered":
            value["recovery_evidence"] = {"carrier": {
                "path": relative, "sha256": graph.sha(carrier), "observed_at": OBSERVED_AT,
                "observer_run_id": "isolated-observer-run",
            }}
        else:
            value.update(action_type="UPDATE", sources=[], previous_result_event="prior-settings-evidence")
        sealed = work_journal.with_event_digest(value)
        self.assertEqual(sealed, work_journal.validate_sealed_event(sealed))
        return sealed

    def register(self, events):
        receipts = work_journal.append_sealed_events(
            self.root, events, author="test-user", local_date="2026-10-13", timezone="Asia/Tbilisi",
        )
        for event, receipt in zip(events, receipts, strict=True):
            carrier = self.root / receipt["carrier"]
            line = carrier.read_bytes().splitlines()[receipt["line"] - 1]
            self.assertEqual(work_journal.canonical_json_bytes(event), line)
            self.assertEqual(event, work_journal.validate_sealed_event(json.loads(line)))
            self.assertEqual(event["event_digest"], receipt["event_digest"])
        return receipts

    def write_records(self, records):
        carrier = self.journal / "receipt-not-settings.ndjson"
        carrier.write_bytes(b"\n".join(work_journal.canonical_json_bytes(record) for record in records) + b"\n")
        return carrier

    def read(self, carrier=None, digest=None):
        before = {path.relative_to(self.root): path.read_bytes()
                  for path in self.root.rglob("*") if path.is_file()}
        bindings = graph.settings_bindings()
        requested = self.framework if carrier is None else carrier
        direct = graph.configuration_binding(graph.sha(requested) if digest is None else digest, carrier)
        after = {path.relative_to(self.root): path.read_bytes()
                 for path in self.root.rglob("*") if path.is_file()}
        self.assertEqual(before, after, "Settings binding must not write Settings or Journal evidence")
        for kind, path in (("project_settings", self.project), ("framework_settings", self.framework)):
            self.assertEqual(path.stem, bindings[kind]["identifier"])
            self.assertEqual(path.relative_to(self.root).as_posix(), bindings[kind]["carrier"])
            self.assertEqual(graph.sha(path), bindings[kind]["sha256"])
        self.assertEqual(requested.stem, direct["identifier"])
        return bindings, direct

    def assert_status(self, binding, status):
        self.assertEqual(status, binding["status"])
        if status != "resolved":
            self.assertEqual("unknown", binding["revision"])
            for field in ("journal_carrier", "journal_line", "journal_event_id", "updated_at"):
                self.assertEqual("", binding[field])

    def test_empty_journal_preserves_both_requested_identities(self):
        for carrier in (self.project, self.framework, None):
            with self.subTest(carrier=carrier):
                bindings, direct = self.read(carrier)
                self.assert_status(direct, "unresolved")
                for binding in bindings.values():
                    self.assert_status(binding, "unresolved")

    def test_registered_recovered_and_completed_pairs_preserve_exact_receipts(self):
        for lifecycle in ("recovered", "completed"):
            with self.subTest(lifecycle=lifecycle):
                events = [self.event(path, lifecycle, event_id=f"{lifecycle}-{kind}", version=version)
                          for kind, path, version in (("project", self.project, 7), ("framework", self.framework, 11))]
                receipts = self.register(events)
                bindings, direct = self.read()
                for kind, event, receipt in zip(("project_settings", "framework_settings"), events, receipts, strict=True):
                    binding = bindings[kind]
                    self.assert_status(binding, "resolved")
                    self.assertEqual(str(event["result"]["version"]), binding["revision"])
                    self.assertEqual(receipt["carrier"], binding["journal_carrier"])
                    self.assertEqual(str(receipt["line"]), binding["journal_line"])
                    self.assertEqual(event["event_id"], binding["journal_event_id"])
                    self.assertEqual("2026-10-13 18:04:05", binding["updated_at"])
                self.assertEqual(bindings["framework_settings"]["journal_event_id"], direct["journal_event_id"])
                for carrier in self.journal.glob("*.ndjson"):
                    carrier.unlink()

    def test_duplicate_registered_evidence_is_ambiguous_per_carrier(self):
        project_event = self.event(self.project, event_id="project-observation")
        framework_event = self.event(self.framework, "completed", event_id="framework-change")
        self.register([project_event, framework_event])
        self.write_records([project_event])
        bindings, direct = self.read(self.project)
        self.assert_status(bindings["project_settings"], "ambiguous")
        self.assert_status(direct, "ambiguous")
        self.assert_status(bindings["framework_settings"], "resolved")
        self.write_records([project_event, framework_event])
        bindings, direct = self.read()
        self.assert_status(bindings["framework_settings"], "ambiguous")
        self.assert_status(direct, "ambiguous")

    def test_current_digest_drift_refuses_only_changed_settings(self):
        self.register([self.event(self.project), self.event(self.framework, event_id="framework-observation")])
        self.project.write_text(self.project.read_text(encoding="utf-8") + "\n# current bytes differ\n", encoding="utf-8")
        bindings, direct = self.read(self.project)
        self.assert_status(bindings["project_settings"], "unresolved")
        self.assert_status(direct, "unresolved")
        self.assert_status(bindings["framework_settings"], "resolved")

    def test_matching_record_requires_current_digest_even_for_direct_reader(self):
        event = self.event(self.framework)
        self.register([event])
        self.framework.write_text(self.framework.read_text(encoding="utf-8") + "\n# drift\n", encoding="utf-8")
        bindings, direct = self.read(digest=event["result"]["sha256"])
        self.assert_status(bindings["framework_settings"], "unresolved")
        self.assert_status(direct, "unresolved")

    def test_direct_reader_refuses_missing_or_unreadable_framework_carrier(self):
        event = self.event(self.framework)
        self.register([event])
        self.framework.unlink()
        for unavailable in ("missing", "directory"):
            with self.subTest(carrier=unavailable):
                if unavailable == "directory":
                    self.framework.mkdir()
                before = {path.relative_to(self.root): path.read_bytes()
                          for path in self.root.rglob("*") if path.is_file()}
                for requested in (None, self.framework):
                    binding = graph.configuration_binding(event["result"]["sha256"], requested)
                    self.assertEqual(self.framework.stem, binding["identifier"])
                    self.assert_status(binding, "unresolved")
                self.assertEqual(before, {path.relative_to(self.root): path.read_bytes()
                                          for path in self.root.rglob("*") if path.is_file()})

    def test_wrong_project_path_digest_and_noncanonical_path_refuse(self):
        for lifecycle in ("recovered", "completed"):
            for carrier in (self.project, self.framework):
                event = self.event(carrier, lifecycle)
                relative = event["result"]["path"]
                cases = [(("structural_scope",), value) for value in
                         ("different-key", "INDEPENDENT", " independent ", "another-project", "TOOLS")]
                cases += [(("result", "path"), value) for value in
                          ("other/settings.toml", "./" + relative, relative.replace("/", "//", 1),
                           str(carrier), "../" + relative)]
                cases += [(("result", "sha256"), "0" * 64), (("result", "filename"), "unrelated.toml")]
                for keys, value in cases:
                    with self.subTest(lifecycle=lifecycle, carrier=carrier.name, field=keys, value=value):
                        bad = copy.deepcopy(event)
                        target = bad
                        for key in keys[:-1]:
                            target = target[key]
                        target[keys[-1]] = value
                        self.write_records([work_journal.with_event_digest(bad)])
                        bindings, direct = self.read(carrier)
                        self.assert_status(direct, "unresolved")
                        for binding in bindings.values():
                            self.assert_status(binding, "unresolved")

    def test_invalid_registered_shape_types_revision_and_seal_refuse(self):
        common = [(("schema_version",), value) for value in (2, True, "3", [], None)]
        common += [(("result", "version"), value) for value in (0, -1, True, 7.0, "7", [], None)]
        common += [((field,), value) for field, value in
                   (("event", []), ("kind", {}), ("subject_kind", []), ("author", None),
                    ("event_id", 7), ("structural_scope", []), ("occurred_at", 7),
                    ("occurred_at", "2026-10-13T18:04:05"), ("llm_session", {}))]
        common += [(("result", field), value) for field, value in
                   (("state", "removed"), ("state", []), ("path", []), ("sha256", 7),
                    ("filename", None))]
        for lifecycle in ("recovered", "completed"):
            specific = [(("recovery_evidence", "carrier", field), value) for field, value in
                        (("observed_at", "2026-10-13T19:04:05+04:00"), ("observed_at", 7),
                         ("observed_at", None), ("observer_run_id", ""), ("observer_run_id", []),
                         ("path", "other/settings.toml"), ("sha256", "0" * 64))] if lifecycle == "recovered" else [
                (("action_type",), []), (("previous_result_event",), None), (("sources",), {})]
            for carrier in (self.project, self.framework):
                event = self.event(carrier, lifecycle)
                for keys, value in common + specific:
                    with self.subTest(lifecycle=lifecycle, carrier=carrier.name, field=keys, value=value):
                        bad = copy.deepcopy(event)
                        target = bad
                        for key in keys[:-1]:
                            target = target[key]
                        target[keys[-1]] = value
                        self.write_records([work_journal.with_event_digest(bad)])
                        _, direct = self.read(carrier)
                        self.assert_status(direct, "unresolved")
                for label in ("missing-seal", "tampered", "extra-field", "missing-result"):
                    with self.subTest(lifecycle=lifecycle, carrier=carrier.name, shape=label):
                        bad = copy.deepcopy(event)
                        if label == "missing-seal":
                            bad.pop("event_digest")
                        elif label == "tampered":
                            bad["result"]["version"] += 1
                        elif label == "extra-field":
                            bad["unexpected"] = True
                            bad = work_journal.with_event_digest(bad)
                        else:
                            bad.pop("result")
                            bad = work_journal.with_event_digest(bad)
                        self.write_records([bad])
                        _, direct = self.read(carrier)
                        self.assert_status(direct, "unresolved")

    def test_parseable_unrelated_records_do_not_obscure_registered_evidence(self):
        receipt = self.register([self.event(self.framework)])[0]
        path = self.write_records([None, [], {"kind": "unrelated"}])
        path.write_bytes(path.read_bytes() + b"not-json\n")
        bindings, direct = self.read()
        self.assert_status(bindings["project_settings"], "unresolved")
        self.assert_status(direct, "resolved")
        self.assertEqual(receipt["carrier"], direct["journal_carrier"])


if __name__ == "__main__":
    unittest.main()
