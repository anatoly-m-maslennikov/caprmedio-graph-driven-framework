"""O212 receiver checks with real selected admission and recorded Action starts."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

import yaml

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from connector_bindings import ConnectorBindingError, capture_source
from connector_scope_receiver import make_scope_read_receiver
from header_groups import nested_header  # noqa: E402
from project_selection import resolve_project
from scope_declaration_test_support import write_scope_unit_declarations
from workflow_run_support import RunExecutionSession, RunTracker, _canonical_digest


def rows():
    return [
        {"scope_unit_name": "ALPHA", "parent": "PROJECT", "scope_unit_type": "Unordered",
         "scope_unit_label": "FEATURE"},
        {"scope_unit_name": "BETA", "parent": "PROJECT", "scope_unit_type": "Unordered",
         "scope_unit_label": "FEATURE"},
        {"scope_unit_name": "CHILD", "parent": "ALPHA", "scope_unit_type": "Ordered",
         "scope_unit_label": "FEATURE", "local_order": 1},
    ]


FIXTURE_SETTINGS = {"project": {"name": "demo", "key": "demo", "obsolete_names": ["old"]},
                    "paths": {"control_root": ".caprmedio_demo", "journal_root": ".caprmedio_demo/_journal",
                              "runtime_root": ".caprmedio_runtime"}}


class ScopeReceiverTests(unittest.TestCase):
    def setUp(self):
        scratch = Path.cwd() / ".caprmedio_tmp/tests/scope-receiver"
        scratch.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.control = self.root / ".caprmedio_demo"
        self.control.mkdir()
        self.settings = self.control / "caprmedio_project_settings.toml"
        self.settings.write_text('[project]\nname = "demo"\nkey = "demo"\nobsolete_names = ["old"]\n'
                                 '[paths]\ncontrol_root = ".caprmedio_demo"\n'
                                 'journal_root = ".caprmedio_demo/_journal"\n'
                                 'runtime_root = ".caprmedio_runtime"\n', encoding="utf-8")
        declared = write_scope_unit_declarations(self.root, tuple(rows()), control_root=self.control)
        self.declaration_paths = tuple(row["declaration_path"] for row in declared.values())
        self.selection = resolve_project(self.root)
        self.action = self.authority("CA-O-212", role="Operations", kind="Action", version=3)
        self.schemas = tuple(self.authority(identity) for identity in ("CA-D-442", "TEST-D-1"))
        self.checked_settings = []
        self.receiver = make_scope_read_receiver(self.selection, self.validate_settings, self.schemas, self.action)
        self.current = True
        self.tracker = RunTracker(self.root,
            source_observer=lambda _request: {"selected": True, "current": self.current, "observed": {}},
            executor=lambda *_args: self.fail("Receiver must not execute another Run."),
            journal_context={"author": "fixture-operator", "timezone": "UTC"})

    def authority(self, atom_id, *, role="Delivery", kind="Delivery", version=1):
        path = self.root / f"{atom_id}.md"
        path.write_text(f"---\natom_id: {atom_id}\ncontent_role: {role}\ntype: {kind}\n"
                        f"version: {version}\nstatus: Active\n---\n"
                        + (json.dumps(FIXTURE_SETTINGS) if atom_id == "TEST-D-1"
                           else "Complete schema for this disposable test Project.") + "\n", encoding="utf-8")
        return capture_source(self.root, path.relative_to(self.root))

    def validate_settings(self, settings):
        """Complete source-bound disposable schema, not production Settings policy."""
        self.checked_settings.append(copy.deepcopy(settings))
        schema = json.loads(self.schemas[-1].read_bytes().decode("utf-8").split("\n---\n", 1)[1])
        if settings != schema:
            raise ConnectorBindingError("schema_invalid", "Fixture complete Settings schema refused.", "context")

    def session(self, identity="ALPHA", *, action=None, context=None, authorization="permission"):
        manifest = {"manifest_ref": "manifest.json", "manifest_digest": "a" * 64}
        parameters = {"operation": "read", "target": {"kind": "Scope Unit", "identity": identity},
                      "query": None, "delta": None, "expected_state": None,
                      "authorization": authorization, "context": manifest if context is None else context}
        request = {"mode": "preview", "request_id": "read-" + _canonical_digest(parameters)[:16],
                   "operation_route": "fixture-private-read", "parameters": parameters,
                   "parameters_digest": _canonical_digest(parameters), "target_frontier": ["selected-scope"],
                   "target_frontier_digest": _canonical_digest(["selected-scope"]), "effects": [], "effects_digest": _canonical_digest([]),
                   "definition_manifest": manifest, "source_freshness": {
                       "selected_source_registry_ref": "TEST-D-1.md", "selected_source_registry_version": 1,
                       "selected_source_registry_digest": self.schemas[-1].sha256,
                       "selected_binding_ref": "manifest.json", "selected_binding_digest": "a" * 64},
                   "initiative": {"initiative_id": "scope-fixture", "instruction_summary": "Read one Scope declaration"}}
        preview = self.tracker.run_selected_operation(request)
        source = self.action if action is None else action
        action_id = "CA-O-212" if action is None else source.relative_path.stem
        request.update(mode="execute", proposal_receipt=preview["proposal_receipt"],
                       proposal_receipt_digest=preview["proposal_receipt_digest"], assigned_action_id="receiver-request",
                       requested_runs=[{"requested_run_id": "scope-action", "kind": "action", "definition": {
                           "atom_id": action_id, "version": 3, "path": source.relative_path.as_posix(), "digest": source.sha256}}])
        fields = ("request_id", "operation_route", "proposal_receipt_digest", "parameters_digest",
                  "target_frontier_digest", "effects_digest", "definition_manifest", "source_freshness")
        request["operator_authorization"] = {"authorization_ref": "permission",
            "authorization_freshness": {"state": "current", "digest": "b" * 64},
            **{field: copy.deepcopy(request[field]) for field in fields}}
        session = RunExecutionSession(self.tracker, request)
        started = session.start_run("scope-action", run_id="actual-scope-action")
        return session, started["run_id"]

    def snapshot(self):
        return {path.relative_to(self.root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in self.root.rglob("*") if path.is_file()}

    def check(self, session, run_id, code=None):
        before = self.snapshot()
        result = self.receiver(session, run_id)
        self.assertEqual(before, self.snapshot())
        self.assertEqual([], result["effects"])
        if code is not None:
            self.assertIsNone(result["data"])
            self.assertEqual(code, result["errors"][0]["code"])
        return result

    def test_complete_root_and_child_reads_use_entire_settings_and_same_session(self):
        for identity, declaration in (("demo", {"scope_unit_name": "demo", "parent": "PROJECT",
                                                "scope_unit_type": "Unordered"}),
                                      ("ALPHA", {"scope_unit_name": "ALPHA", "parent": "PROJECT",
                                                  "scope_unit_id": "TEST-SU-1", "scope_unit_type": "Unordered",
                                                  "label": "FEATURE"})):
            with self.subTest(identity=identity):
                session, run_id = self.session(identity)
                result = self.check(session, run_id)
                self.assertEqual([], result["errors"])
                self.assertEqual({"identity": identity, "declaration": declaration}, result["data"])
                self.assertEqual("current", result["current_state"]["source_view"])
                self.assertTrue(self.checked_settings)
                self.assertFalse(session.terminal)

    def test_nested_action_and_schema_authorities_allow_read(self):
        def grouped(source):
            path = self.root / source.relative_path
            header, body = path.read_text(encoding="utf-8")[4:].split("\n---\n", 1)
            path.write_text("---\n" + yaml.safe_dump(nested_header(yaml.safe_load(header)), sort_keys=False)
                            + "---\n" + body, encoding="utf-8")
            return capture_source(self.root, source.relative_path)

        self.action = grouped(self.action)
        self.schemas = tuple(grouped(source) for source in self.schemas)
        self.receiver = make_scope_read_receiver(self.selection, self.validate_settings, self.schemas, self.action)
        result = self.check(*self.session())
        self.assertEqual([], result["errors"])
        self.assertEqual("ALPHA", result["data"]["identity"])

    def test_missing_target_and_context_and_denied_permission_refuse_without_effects(self):
        for arguments, code in (({"identity": "MISSING"}, "target_not_found"),
                                ({"context": "unresolved"}, "input_invalid"),
                                ({"authorization": "unbound"}, "permission_denied")):
            with self.subTest(arguments=arguments):
                self.check(*self.session(**arguments), code)

    def test_wrong_or_unstarted_or_completed_action_refuses(self):
        other = self.authority("CA-O-218", role="Operations", kind="Action", version=3)
        self.check(*self.session(action=other), "permission_denied")
        session, run_id = self.session()
        self.check(session, "not-started", "permission_denied")
        session.finish_run(run_id, outcome="completed", result_ref="result.json", effect_refs=[])
        self.check(session, run_id, "permission_denied")

    def test_each_original_pin_and_selected_currentness_are_retained(self):
        for path in (self.settings, *self.declaration_paths, self.root / self.action.relative_path,
                     *(self.root / source.relative_path for source in self.schemas)):
            with self.subTest(path=path.name):
                session, run_id = self.session()
                original = path.read_bytes()
                path.write_bytes(original + b"\n# drift\n")
                self.check(session, run_id, "stale_state")
                path.write_bytes(original)
        session, run_id = self.session()
        self.current = False
        self.check(session, run_id, "stale_state")

    def test_missing_complete_validator_or_schema_and_boolean_attestation_refuse(self):
        with self.assertRaises(TypeError):
            make_scope_read_receiver(self.selection, None, self.schemas, self.action)
        with self.assertRaises(ValueError):
            make_scope_read_receiver(self.selection, self.validate_settings, self.schemas[2:], self.action)
        self.receiver = make_scope_read_receiver(self.selection, lambda _settings: True, self.schemas, self.action)
        self.check(*self.session(), "schema_invalid")


if __name__ == "__main__":
    unittest.main()
