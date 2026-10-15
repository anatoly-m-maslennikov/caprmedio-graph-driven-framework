"""Genuine selected Action tests for the private Structure Read receiver."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from connector_bindings import capture_source
from connector_configuration_receiver import make_configuration_read_receiver
from project_selection import resolve_project
from workflow_run_support import LazyRunTracker, _canonical_digest


STRUCTURE = '''# preserve complete source text
schema_version = 1

[[scope_units]]
scope_unit_name = "ALPHA"
parent = "PROJECT"
scope_unit_type = "Unordered"
scope_unit_label = "UNIT"
structural_level = 1
navigational_order_number = 0
authority_path = ".caprmedio_demo/alpha"
delivery_path = "implementation/alpha"
'''


class ConfigurationReadReceiverTests(unittest.TestCase):
    def setUp(self):
        scratch = Path.cwd() / ".caprmedio_tmp" / "tests"
        scratch.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=scratch, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.control = self.root / ".caprmedio_demo"
        self.control.mkdir()
        self.settings = self.control / "caprmedio_project_settings.toml"
        self.settings.write_text('[project]\nname="demo"\nkey="different-key"\n'
                                 '[paths]\ncontrol_root=".caprmedio_demo"\n'
                                 'journal_root=".caprmedio_demo/_journal"\n', encoding="utf-8")
        self.structure = self.control / "project_structure.toml"
        self.structure.write_text(STRUCTURE, encoding="utf-8")
        self.action = self.root / "action.md"
        self.action.write_text('---\natom_id: CA-O-218\nversion: 2\ncontent_role: Operations\n'
                               'type: Action\nstatus: Active\n---\n# Read one complete TOML configuration\n', encoding="utf-8")
        self.schema = self.root / "structure-schema.md"
        self.schema.write_text("---\natom_id: CA-D-441\nversion: 5\n---\nFixture document schema.\n", encoding="utf-8")
        self.row_schema = self.root / "row-schema.md"
        self.row_schema.write_text("---\natom_id: CA-D-442\nversion: 6\n---\nFixture declaration schema.\n", encoding="utf-8")
        self.manifest = self.root / "manifest.json"
        self.manifest.write_text(json.dumps({"action": self.digest(self.action), "schema": self.digest(self.schema)}), encoding="utf-8")
        self.selection = resolve_project(self.root)
        self.action_pin = capture_source(self.root, "action.md")
        self.schema_pin = capture_source(self.root, "structure-schema.md")
        self.schema_pins = [self.schema_pin, capture_source(self.root, "row-schema.md")]
        self.receiver = make_configuration_read_receiver(self.selection, validate_settings=self.validate_settings,
                                                        schema_sources=self.schema_pins,
                                                        action_definition=self.action_pin)
        self.sequence = 0

    @staticmethod
    def digest(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()

    @staticmethod
    def validate_settings(document):
        if (set(document) != {"project", "paths"}
                or document["project"] != {"name": "demo", "key": "different-key"}
                or document["paths"] != {"control_root": ".caprmedio_demo", "journal_root": ".caprmedio_demo/_journal"}):
            raise ValueError("Complete explicit fixture Settings schema is invalid.")

    def snapshot(self):
        return {path.relative_to(self.root).as_posix(): path.read_bytes()
                for path in self.root.rglob("*") if path.is_file()}

    def inner(self):
        return {"operation": "read", "target": {"kind": "Configuration", "identity": "Project Structure"},
                "query": None, "delta": None, "expected_state": None, "authorization": "read-permission",
                "context": {"manifest_ref": "manifest.json", "manifest_digest": self.digest(self.manifest)}}

    def invoke(self, inner=None, *, before=None, action_id="CA-O-218", version=2, finish_first=False,
               started=True, effects=None):
        inner = copy.deepcopy(self.inner() if inner is None else inner)
        self.sequence += 1
        frontier = [self.structure.relative_to(self.root).as_posix()]
        effects = [] if effects is None else effects
        outer = {"mode": "preview", "request_id": f"configuration-read-{self.sequence}",
                 "operation_route": "fixture.configuration-read", "parameters": inner,
                 "parameters_digest": _canonical_digest(inner), "target_frontier": frontier,
                 "target_frontier_digest": _canonical_digest(frontier), "effects": effects,
                 "effects_digest": _canonical_digest(effects),
                 "definition_manifest": {"manifest_ref": "manifest.json", "manifest_digest": self.digest(self.manifest)},
                 "source_freshness": {"selected_source_registry_ref": "structure-schema.md",
                    "selected_source_registry_version": 1, "selected_source_registry_digest": self.digest(self.schema),
                    "selected_binding_ref": "manifest.json", "selected_binding_digest": self.digest(self.manifest)},
                 "initiative": {"initiative_id": "fixture", "instruction_summary": "read complete selected Structure"}}
        captured = {}

        def executor(request, session):
            if started:
                session.start_run("action", run_id="actual-action")
            if finish_first:
                session.finish_run("actual-action", outcome="completed", result_ref="results/read.json", effect_refs=[])
            if before:
                before(session)
            prior = self.snapshot()
            captured["result"] = self.receiver(session, "actual-action")
            self.assertEqual(prior, self.snapshot(), "receiver changed source or Journal bytes")
            if started and not finish_first:
                session.finish_run("actual-action", outcome="completed" if not captured["result"]["errors"] else "failed",
                                   result_ref="results/read.json", effect_refs=[])

        tracker = LazyRunTracker(self.root, source_observer=lambda request: {
            "selected": request["operation_route"] == "fixture.configuration-read",
            "current": self.digest(self.manifest) == request["definition_manifest"]["manifest_digest"],
            "observed": {"manifest_digest": self.digest(self.manifest)}}, executor=executor,
            journal_context={"author": "trusted-operator", "timezone": "UTC"})
        preview = tracker.run_selected_operation(outer)
        outer.update(mode="execute", proposal_receipt=preview["proposal_receipt"],
                     proposal_receipt_digest=preview["proposal_receipt_digest"], assigned_action_id="assigned-action",
                     requested_runs=[{"requested_run_id": "action", "kind": "action", "definition": {
                         "atom_id": action_id, "version": version, "path": "action.md", "digest": self.digest(self.action)}}])
        fields = ("request_id", "operation_route", "proposal_receipt_digest", "parameters_digest",
                  "target_frontier_digest", "effects_digest", "definition_manifest", "source_freshness")
        outer["operator_authorization"] = {"authorization_ref": "read-permission",
            "authorization_freshness": {"state": "current", "digest": "a" * 64},
            **{key: copy.deepcopy(outer[key]) for key in fields}}
        terminal = tracker.run_selected_operation(outer)
        self.assertNotIn("execution_error", terminal, terminal)
        return captured["result"]

    def assert_refused(self, result, code):
        self.assertEqual([], result["effects"])
        self.assertIsNone(result["data"])
        self.assertEqual(code, result["errors"][0]["code"])

    def test_complete_structure_text_document_state_and_exact_pin(self):
        result = self.invoke()
        self.assertEqual([], result["errors"])
        self.assertEqual([], result["effects"])
        self.assertEqual(STRUCTURE, result["data"]["source_text"])
        self.assertNotIn("authority_mode", result["data"]["document"]["scope_units"][0])
        self.assertEqual({"identity": "Project Structure", "project": "demo", "source_view": "current",
                          "sha256": self.digest(self.structure)}, result["current_state"])
        pinned = self.inner(); pinned["expected_state"] = result["current_state"]
        self.assertEqual(result, self.invoke(pinned))

    def test_stale_expected_state_is_refused(self):
        inner = self.inner()
        inner["expected_state"] = {"sha256": "0" * 64}
        self.assert_refused(self.invoke(inner), "stale_state")

    def test_selection_schema_and_action_drift_are_not_recaptured(self):
        for path in (self.settings, self.structure, self.schema, self.row_schema, self.action):
            with self.subTest(path=path.name):
                original = path.read_bytes()
                self.assert_refused(self.invoke(before=lambda _, path=path: path.write_bytes(original + b"\n# drift\n")), "stale_state")
                path.write_bytes(original)

    def test_unresolved_context_and_denied_permission(self):
        inner = self.inner(); inner["context"] = "unresolved"
        self.assert_refused(self.invoke(inner), "input_invalid")
        inner = self.inner(); inner["authorization"] = "other-permission"
        self.assert_refused(self.invoke(inner), "permission_denied")

    def test_real_started_correct_nonterminal_action_is_required(self):
        self.assert_refused(self.invoke(action_id="CA-O-212"), "permission_denied")
        self.assert_refused(self.invoke(version=1), "permission_denied")
        self.assert_refused(self.invoke(finish_first=True), "permission_denied")
        self.assert_refused(self.invoke(started=False), "permission_denied")
        self.assert_refused(self.receiver(True, "actual-action"), "permission_denied")

    def test_settings_capability_remains_explicitly_unsupported(self):
        inner = self.inner(); inner["target"]["identity"] = "Project Settings"
        self.assert_refused(self.invoke(inner), "unsupported_operation")

    def test_read_does_not_admit_requested_effects(self):
        self.assert_refused(self.invoke(effects=[{"type": "write", "target": "unrelated.txt"}]), "permission_denied")

    def test_complete_schema_is_checked_beyond_selection_subset(self):
        original = self.structure.read_text(encoding="utf-8")
        self.structure.write_text(original + '\nunknown = "invalid row field"\n', encoding="utf-8")
        # Project selection intentionally provides boundary evidence, not full
        # declaration-schema acceptance; the receiver performs that check.
        selected = resolve_project(self.root)
        self.receiver = make_configuration_read_receiver(selected, validate_settings=self.validate_settings,
                                                        schema_sources=self.schema_pins,
                                                        action_definition=self.action_pin)
        self.assert_refused(self.invoke(), "schema_invalid")

    def test_settings_validator_cannot_return_flags_or_repair_source(self):
        def repair(document):
            document["paths"]["journal_root"] = "changed"
        for validator in (lambda _: True, repair):
            with self.subTest(validator=validator):
                self.receiver = make_configuration_read_receiver(self.selection, validate_settings=validator,
                    schema_sources=self.schema_pins, action_definition=self.action_pin)
                self.assert_refused(self.invoke(), "schema_invalid")

    def test_missing_or_duplicate_schema_authority_is_not_bound(self):
        for sources in ([], [self.schema_pin], [*self.schema_pins, self.schema_pin]):
            with self.subTest(sources=sources):
                with self.assertRaises(ValueError):
                    make_configuration_read_receiver(self.selection, validate_settings=self.validate_settings,
                        schema_sources=sources, action_definition=self.action_pin)
        duplicate = self.root / "duplicate-document-schema.md"
        duplicate.write_bytes(self.schema.read_bytes())
        with self.assertRaises(ValueError):
            make_configuration_read_receiver(self.selection, validate_settings=self.validate_settings,
                schema_sources=[*self.schema_pins, capture_source(self.root, duplicate.name)],
                action_definition=self.action_pin)


if __name__ == "__main__":
    unittest.main()
