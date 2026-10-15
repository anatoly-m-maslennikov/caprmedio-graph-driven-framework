"""Private O211 checks using actual schema bytes and recorded Action Sessions."""

from __future__ import annotations

import copy
import hashlib
import re
from pathlib import Path
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from connector_bindings import capture_source
from connector_scope_receiver import SCOPE_QUERY_IDS, make_scope_query_receiver
from connector_toml_parse import render_document
from project_selection import resolve_project
from project_settings_reader import SCHEMA_IDS
from test_connector_scope_parsing import filters, rows, serialize_project_structure
from workflow_run_support import RunExecutionSession, RunTracker, _canonical_digest


REPOSITORY = TOOLS.parents[2]
CONTROL = REPOSITORY / ".caprmedio_caprmedio"
CORE = CONTROL / "101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL"
ENGINE = CONTROL / "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC"
SETTINGS = {"schema_version": "2.0", "project": {"name": "demo", "obsolete_names": ["old"]},
            "artifacts": {"identity": {"project_prefix": "DEMO"}},
            "paths": {"control_root": ".caprmedio_demo"}}


class ScopeQueryReceiverTests(unittest.TestCase):
    def setUp(self):
        scratch = Path.cwd() / ".caprmedio_tmp/tests/scope-query-receiver"
        scratch.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.control = self.root / ".caprmedio_demo"
        self.control.mkdir()
        self.settings = self.control / "caprmedio_project_settings.toml"
        self.settings.write_bytes(render_document(SETTINGS))
        self.structure = self.control / "project_structure.toml"
        self.structure.write_text(serialize_project_structure([
            {**row, "authority_path": row["authority_path"].rstrip("/")} for row in rows()]), encoding="utf-8")
        authority = self.root / "authority"
        authority.mkdir()
        self.sources = {}
        for identity in SCHEMA_IDS | SCOPE_QUERY_IDS:
            candidates = [path for base in (CORE, ENGINE) for path in base.rglob(identity + "-*.md")
                          if "archive" not in path.parts]
            self.assertEqual(1, len(candidates), identity)
            target = authority / candidates[0].name
            target.write_bytes(candidates[0].read_bytes())
            self.sources[identity] = capture_source(self.root, target.relative_to(self.root))
        self.action = self.sources["CA-O-211"]
        self.action_version = 3
        self.schemas = tuple(source for identity, source in self.sources.items() if identity != "CA-O-211")
        self.selection = resolve_project(self.root)
        self.receiver = make_scope_query_receiver(self.selection, schema_sources=self.schemas,
                                                  action_definition=self.action)
        self.current = True
        self.tracker = RunTracker(self.root,
            source_observer=lambda _request: {"selected": True, "current": self.current, "observed": {}},
            executor=lambda *_args: self.fail("Query must not execute another Run."),
            journal_context={"author": "fixture-operator", "timezone": "UTC"})

    def session(self, selected=None, *, expected=None, effects=None, authorization="permission"):
        manifest = {"manifest_ref": "manifest.json", "manifest_digest": "a" * 64}
        parameters = {"operation": "query", "target": None,
                      "query": {"kind": "Scope Unit", "filters": filters() if selected is None else selected},
                      "delta": None, "expected_state": expected, "authorization": authorization, "context": manifest}
        request = {"mode": "preview", "request_id": "query-" + _canonical_digest(parameters)[:16],
                   "operation_route": "fixture-private-query", "parameters": parameters,
                   "parameters_digest": _canonical_digest(parameters), "target_frontier": ["selected-scope"],
                   "target_frontier_digest": _canonical_digest(["selected-scope"]), "effects": effects or [],
                   "effects_digest": _canonical_digest(effects or []), "definition_manifest": manifest,
                   "source_freshness": {"selected_source_registry_ref": self.sources["CA-D-626"].relative_path.as_posix(),
                       "selected_source_registry_version": 3, "selected_source_registry_digest": self.sources["CA-D-626"].sha256,
                       "selected_binding_ref": "manifest.json", "selected_binding_digest": "a" * 64},
                   "initiative": {"initiative_id": "scope-query-fixture", "instruction_summary": "Query declared Scope Units"}}
        preview = self.tracker.run_selected_operation(request)
        request.update(mode="execute", proposal_receipt=preview["proposal_receipt"],
                       proposal_receipt_digest=preview["proposal_receipt_digest"], assigned_action_id="query-request",
                       requested_runs=[{"requested_run_id": "scope-query-action", "kind": "action", "definition": {
                           "atom_id": "CA-O-211", "version": self.action_version, "path": self.action.relative_path.as_posix(),
                           "digest": self.action.sha256}}])
        fields = ("request_id", "operation_route", "proposal_receipt_digest", "parameters_digest",
                  "target_frontier_digest", "effects_digest", "definition_manifest", "source_freshness")
        request["operator_authorization"] = {"authorization_ref": "permission",
            "authorization_freshness": {"state": "current", "digest": "b" * 64},
            **{field: copy.deepcopy(request[field]) for field in fields}}
        session = RunExecutionSession(self.tracker, request)
        started = session.start_run("scope-query-action", run_id="actual-scope-query-action")
        return session, started["run_id"]

    def snapshot(self):
        return {path.relative_to(self.root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in self.root.rglob("*") if path.is_file()}

    def receive(self, selected=None, *, code=None, **kwargs):
        session, run_id = self.session(selected, **kwargs)
        before = self.snapshot()
        result = self.receiver(session, run_id)
        self.assertEqual(before, self.snapshot())
        self.assertEqual([], result["effects"])
        if code:
            self.assertEqual(code, result["errors"][0]["code"])
        else:
            self.assertEqual([], result["errors"])
            self.assertTrue(result["data"]["coverage"]["complete"])
        return result

    def test_complete_query_preserves_requested_facts_without_a_history_requirement(self):
        result = self.receive()
        self.assertEqual(["ALPHA", "BETA", "CHILD", "demo"], [row["identity"] for row in result["data"]["matches"]])
        self.assertEqual({"scope_unit_name": "CHILD", "parent": "ALPHA", "local_order": 1},
                         result["data"]["matches"][2]["facts"])
        self.assertEqual({"scope_unit_name": "demo"}, result["data"]["matches"][3]["facts"])
        self.assertEqual("current", result["current_state"]["source_view"])
        self.assertNotIn("version", result["current_state"])

    def test_nonroot_frontier_has_no_sibling_or_implicit_read(self):
        result = self.receive(filters("ALPHA", False, True))
        self.assertEqual(["CHILD"], [row["identity"] for row in result["data"]["matches"]])
        self.assertNotIn("declaration", result["data"]["matches"][0])

    def test_empty_and_conjunctive_queries_are_complete(self):
        for wanted, names in (("ALPHA", ["ALPHA"]), ("unknown", [])):
            result = self.receive(filters(predicates=[{"field": "scope_unit_name", "match": "exact", "value": wanted},
                                                       {"field": "parent", "match": "exact", "value": "demo"}]))
            self.assertEqual(names, [row["identity"] for row in result["data"]["matches"]])

    def test_exact_expected_evidence_is_enforced(self):
        state = self.receive()["current_state"]
        self.receive(expected=state)
        state["source_evidence"]["project_structure"]["sha256"] = "0" * 64
        self.receive(expected=state, code="stale_state")

    def test_closed_query_and_unresolved_frontier_refuse(self):
        invalid = filters(); invalid["limit"] = 2
        self.receive(invalid, code="input_invalid")
        self.receive(filters("missing"), code="target_not_found")
        self.receive(authorization="unbound", code="permission_denied")

    def test_complete_settings_unknown_fields_refuse_without_migration(self):
        document = copy.deepcopy(SETTINGS); document["project"]["legacy"] = "preserved"
        self.settings.write_bytes(render_document(document))
        self.selection = resolve_project(self.root)
        self.receiver = make_scope_query_receiver(self.selection, schema_sources=self.schemas, action_definition=self.action)
        self.receive(code="schema_invalid")

    def test_pin_drift_and_terminal_action_refuse(self):
        for path in (self.settings, self.structure, self.root / self.action.relative_path,
                     self.root / self.sources["CA-D-626"].relative_path):
            session, run_id = self.session()
            original = path.read_bytes(); path.write_bytes(original + b"\n# drift\n")
            before = self.snapshot(); result = self.receiver(session, run_id)
            self.assertEqual(before, self.snapshot())
            self.assertEqual("stale_state", result["errors"][0]["code"])
            path.write_bytes(original)
        session, run_id = self.session()
        session.finish_run(run_id, outcome="completed", result_ref="result.json", effect_refs=[])
        self.assertEqual("permission_denied", self.receiver(session, run_id)["errors"][0]["code"])

    def test_missing_or_duplicate_schema_packet_refuses(self):
        for schemas in (self.schemas[:-1], (*self.schemas, self.schemas[0])):
            with self.assertRaises(ValueError):
                make_scope_query_receiver(self.selection, schema_sources=schemas, action_definition=self.action)

    def test_current_rule_and_action_revisions_keep_actual_pins(self):
        old = self.sources["CA-D-626"]
        path = self.root / old.relative_path
        path.write_text(re.sub(r"(?m)^version: .*", "version: 99", path.read_text()) + "\n# Updated rule\n")
        self.receive(filters("ALPHA"), code="stale_state")
        current = capture_source(self.root, old.relative_path)
        self.sources["CA-D-626"] = current
        self.schemas = tuple(current if source == old else source for source in self.schemas)
        path = self.root / self.action.relative_path
        path.write_text(re.sub(r"(?m)^version: .*", "version: 4", path.read_text()))
        self.action = capture_source(self.root, self.action.relative_path)
        self.action_version = 4
        self.receiver = make_scope_query_receiver(self.selection, schema_sources=self.schemas,
                                                  action_definition=self.action)
        self.receive()
        path.write_text(path.read_text() + "\n# Drift after capture\n")
        self.receive(code="stale_state")

    def test_wrong_inactive_or_malformed_current_schema_refuses(self):
        old = self.sources["CA-D-626"]
        path = self.root / old.relative_path
        original = path.read_text()
        for field, value in (("atom_id", "UNKNOWN"), ("status", "Archived"),
                             ("content_role", "Plan"), ("version", "0"),
                             ("version", "true"), ("version", "'1'")):
            with self.subTest(field=field, value=value):
                path.write_text(re.sub(rf"(?m)^{field}: .*", f"{field}: {value}", original))
                current = capture_source(self.root, old.relative_path)
                schemas = tuple(current if source == old else source for source in self.schemas)
                with self.assertRaises(ValueError):
                    make_scope_query_receiver(self.selection, schema_sources=schemas,
                                              action_definition=self.action)

    def test_current_query_action_still_requires_active_action_metadata(self):
        path = self.root / self.action.relative_path
        original = path.read_text()
        for field, value in (("atom_id", "CA-O-212"), ("status", "Archived"),
                             ("type", "Workflow"), ("version", "true")):
            with self.subTest(field=field, value=value):
                path.write_text(re.sub(rf"(?m)^{field}: .*", f"{field}: {value}", original))
                action = capture_source(self.root, self.action.relative_path)
                with self.assertRaises(ValueError):
                    make_scope_query_receiver(self.selection, schema_sources=self.schemas,
                                              action_definition=action)


if __name__ == "__main__":
    unittest.main()
