"""Independent O211 receiving checks with actual authority and started Sessions."""

from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import sys
import unittest

TOOLS = Path(__file__).resolve().parents[1]
REPOSITORY = TOOLS.parents[2]
sys.path.insert(0, str(TOOLS))

from connector_bindings import capture_source
from connector_toml_parse import render_document
from project_selection import resolve_project
from workflow_run_support import LazyRunTracker, RunExecutionSession, _canonical_digest
import test_project_settings_reader_independent as settings_fixtures


class ScopeQueryReceivingIndependentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = settings_fixtures.ProjectSettingsReaderIndependentTests()
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.setUp()
        self.root = self.fixture.root
        (self.root / ".git").mkdir()
        self.structure = self.fixture.control / "project_structure.toml"
        self.rows = [self.row("BETA", "PROJECT", "Unordered", "FEATURE", 1),
                     self.row("CHILD", "ALPHA", "Ordered", "DETAIL", 2, local_order=0),
                     self.row("ALPHA", "PROJECT", "Unordered", "FEATURE", 1),
                     self.row("UNMATERIALIZED", "PROJECT", "Unordered", "FEATURE", 1)]
        self.structure.write_bytes(render_document({"schema_version": 1, "scope_units": self.rows}))
        self.selection = resolve_project(self.root)
        self.schemas = list(self.fixture.authorities)
        self.sources = {}
        for identity in ("CA-D-625", "CA-D-441", "CA-D-442", "CA-D-626",
                         "CA-R-1937", "CA-M-377", "CA-E-629", "CA-R-1936", "CA-M-376", "CA-E-628",
                         "CA-O-211", "CA-O-212"):
            matches = [p for p in (REPOSITORY / ".caprmedio_caprmedio").rglob(identity + "-*.md")
                       if "archive" not in p.parts and "_projection" not in p.parts
                       and "000_CAPRMEDIO_framework" not in p.parts]
            self.assertEqual(1, len(matches), identity)
            target = self.root / "accepted-authority" / (identity + ".md")
            target.write_bytes(matches[0].read_bytes())
            self.sources[identity] = capture_source(self.root, target.relative_to(self.root))
            if identity not in {"CA-O-211", "CA-O-212"}:
                self.schemas.append(self.sources[identity])
        permission = self.root / "permission.md"
        permission.write_bytes(b"Explicit read-only permission for the selected query.")
        self.permission = capture_source(self.root, "permission.md")
        self.sequence = 0

    @staticmethod
    def row(name, parent, kind, label, level, **optional):
        return {"scope_unit_name": name, "parent": parent, "scope_unit_type": kind,
                "scope_unit_label": label, "structural_level": level, "navigational_order_number": 0,
                "authority_path": ".caprmedio_independent/" + name, "delivery_path": "delivery/" + name,
                **optional}

    def filters(self, identity="independent", *, include_self=True, include_descendants=True,
                predicates=(), fields=("scope_unit_name", "parent", "local_order")):
        return {"frontier": {"identity": identity, "include_self": include_self,
                             "include_descendants": include_descendants},
                "predicates": list(predicates), "result_fields": list(fields)}

    def handler(self, **options):
        from connector_scope_receiver import make_scope_query_receiver
        return make_scope_query_receiver(self.selection, schema_sources=self.schemas,
                                         action_definition=self.sources["CA-O-211"], **options)

    def snapshot(self):
        return {p.relative_to(self.root).as_posix(): p.read_bytes()
                for p in self.root.rglob("*") if p.is_file()}

    def invoke(self, filters=None, *, handler=None, action="CA-O-211", context=None,
               mutate=None, effects=(), expected_state=None, request_changes=None):
        handler = self.handler() if handler is None else handler
        manifest = {"manifest_ref": self.sources["CA-D-625"].relative_path.as_posix(),
                    "manifest_digest": self.sources["CA-D-625"].sha256}
        inner = {"operation": "query", "target": None,
                 "query": {"kind": "Scope Unit", "filters": self.filters() if filters is None else filters},
                 "delta": None, "expected_state": expected_state, "authorization": "permission.md",
                 "context": manifest if context is None else context}
        inner.update(request_changes or {})
        captured = {}
        self.sequence += 1
        def observe(outer):
            return {"selected": outer["operation_route"] == "private-fixture-query",
                    "current": hashlib.sha256((self.root / "permission.md").read_bytes()).hexdigest() == self.permission.sha256,
                    "observed": {"definition_manifest": manifest}}
        def execute(_outer, session):
            self.assertIsInstance(session, RunExecutionSession)
            run = session.start_run("query", run_id=f"actual-query-{self.sequence}")["run_id"]
            if mutate:
                mutate(session, run)
            before = self.snapshot()
            try:
                captured["result"] = handler(session, run)
            except Exception as error:
                captured["exception"] = error
            self.assertEqual(before, self.snapshot(), "Query receiver changed a source or Run evidence.")
            session.tracker.root = self.root
            if "query" not in session.terminal:
                refused = "exception" in captured or bool(captured["result"]["errors"])
                session.finish_run(run, outcome="failed" if refused else "completed",
                                   result_ref="results/query.json", effect_refs=[])
        tracker = LazyRunTracker(self.root, source_observer=observe, executor=execute,
                                 journal_context={"author": "independent-query-operator", "timezone": "UTC"})
        action_source = self.sources[action]
        frontier = [self.fixture.settings.relative_to(self.root).as_posix(), self.structure.relative_to(self.root).as_posix()]
        outer = {"mode": "preview", "request_id": f"query-{self.sequence}", "operation_route": "private-fixture-query",
                 "parameters": inner, "parameters_digest": _canonical_digest(inner),
                 "target_frontier": frontier, "target_frontier_digest": _canonical_digest(frontier),
                 "effects": list(effects), "effects_digest": _canonical_digest(list(effects)),
                 "definition_manifest": manifest,
                 "source_freshness": {"selected_source_registry_ref": manifest["manifest_ref"], "selected_source_registry_version": 2,
                                      "selected_source_registry_digest": manifest["manifest_digest"],
                                      "selected_binding_ref": action_source.relative_path.as_posix(),
                                      "selected_binding_digest": action_source.sha256},
                 "initiative": {"initiative_id": "independent-query", "instruction_summary": "query explicit frontier"},
                 "requested_runs": [{"requested_run_id": "query", "kind": "action", "definition": {
                     "atom_id": action, "version": 3, "path": action_source.relative_path.as_posix(), "digest": action_source.sha256}}]}
        preview = tracker.run_selected_operation(outer)
        outer.update(mode="execute", proposal_receipt=preview["proposal_receipt"],
                     proposal_receipt_digest=preview["proposal_receipt_digest"], assigned_action_id=f"assigned-query-{self.sequence}")
        fields = ("request_id", "operation_route", "proposal_receipt_digest", "parameters_digest",
                  "target_frontier_digest", "effects_digest", "definition_manifest", "source_freshness")
        outer["operator_authorization"] = {
            "authorization_ref": "permission.md", "authorization_freshness": {"state": "current", "digest": self.permission.sha256},
            **{field: copy.deepcopy(outer[field]) for field in fields}}
        outcome = tracker.run_selected_operation(outer)
        self.assertTrue(captured, outcome)
        if "exception" in captured:
            raise captured["exception"]
        result = captured["result"]
        self.assertEqual([], result["effects"])
        return result

    def assert_error(self, result, code):
        self.assertTrue(result["errors"])
        self.assertEqual(code, result["errors"][0]["code"])
        self.assertTrue(result["data"] is None or not result["data"]["coverage"]["complete"])

    def identities(self, result):
        self.assertEqual([], result["errors"])
        self.assertTrue(result["data"]["coverage"]["complete"])
        return [match["identity"] for match in result["data"]["matches"]]

    def test_explicit_root_frontier_exact_projection_order_and_unmaterialized_unit(self):
        result = self.invoke()
        self.assertEqual(["ALPHA", "BETA", "CHILD", "UNMATERIALIZED", "independent"], self.identities(result))
        self.assertEqual({"scope_unit_name": "independent"}, result["data"]["matches"][-1]["facts"])
        self.assertEqual({"scope_unit_name": "CHILD", "parent": "ALPHA", "local_order": 0},
                         result["data"]["matches"][2]["facts"])
        self.assertFalse((self.fixture.control / "UNMATERIALIZED").exists())
        self.assertEqual({"project": "independent", "source_view": "current", "source_evidence": {
            "project_settings": {"sha256": self.fixture.source.sha256},
            "project_structure": {"sha256": hashlib.sha256(self.structure.read_bytes()).hexdigest()}}}, result["current_state"])

    def test_frontier_self_descendants_and_literal_conjunctive_filters(self):
        for self_flag, children_flag, expected in ((True, False, ["ALPHA"]), (False, True, ["CHILD"]), (True, True, ["ALPHA", "CHILD"])):
            with self.subTest(include_self=self_flag, descendants=children_flag):
                self.assertEqual(expected, self.identities(self.invoke(self.filters("ALPHA", include_self=self_flag, include_descendants=children_flag))))
        cases = [("scope_unit_name", "prefix", "AL", ["ALPHA"]), ("scope_unit_name", "suffix", "ILD", ["CHILD"]),
                 ("scope_unit_name", "contains", "ET", ["BETA"]), ("scope_unit_name", "exact", "alpha", []),
                 ("parent", "exact", "independent", ["ALPHA", "BETA", "UNMATERIALIZED"]),
                 ("scope_unit_type", "exact", "Ordered", ["CHILD"])]
        for field, mode, value, expected in cases:
            with self.subTest(field=field, mode=mode, value=value):
                self.assertEqual(expected, self.identities(self.invoke(self.filters(predicates=[{"field": field, "match": mode, "value": value}]))))
        predicates = [{"field": "scope_unit_label", "match": "contains", "value": "FEATURE"},
                      {"field": "scope_unit_name", "match": "suffix", "value": "TA"}]
        self.assertEqual(["BETA"], self.identities(self.invoke(self.filters(predicates=predicates))))
        identities_only = self.invoke(self.filters(fields=()))
        self.assertTrue(all(match["facts"] == {} for match in identities_only["data"]["matches"]))

    def test_exact_expected_state_and_stale_supplied_state(self):
        state = self.invoke()["current_state"]
        self.assertEqual(["ALPHA", "BETA", "CHILD", "UNMATERIALIZED", "independent"], self.identities(self.invoke(expected_state=state)))
        state["source_evidence"]["project_structure"]["sha256"] = "0" * 64
        self.assert_error(self.invoke(expected_state=state), "stale_state")

    def test_closed_query_rejects_paging_invalid_modes_and_omitted_frontier(self):
        cases = []
        filters = self.filters(); filters["page_size"] = 1; cases.append(filters)
        filters = self.filters(); del filters["frontier"]; cases.append(filters)
        filters = self.filters(); filters["frontier"]["include_self"] = 1; cases.append(filters)
        filters = self.filters(); filters["result_fields"] = ["parent", "parent"]; cases.append(filters)
        filters = self.filters(predicates=[{"field": "parent", "match": "prefix", "value": "ind"}]); cases.append(filters)
        for filters in cases:
            with self.subTest(filters=filters):
                self.assert_error(self.invoke(filters), "input_invalid")
        self.assert_error(self.invoke(self.filters("MISSING")), "target_not_found")
        self.assert_error(self.invoke(request_changes={"target": {"kind": "Scope Unit", "identity": "ALPHA"}}), "input_invalid")

    def test_wrong_action_context_and_request_cannot_replace_started_admission(self):
        self.assert_error(self.invoke(action="CA-O-212"), "permission_denied")
        self.assert_error(self.invoke(context={"manifest_ref": "other.md", "manifest_digest": "0" * 64}), "input_invalid")
        def replace(session, _run):
            session.request["parameters"]["query"]["filters"]["frontier"]["identity"] = "BETA"
        self.assert_error(self.invoke(mutate=replace), "permission_denied")

    def test_stale_authorization_terminal_and_absent_start_refuse(self):
        def stale(session, _run):
            session.request["operator_authorization"]["authorization_freshness"]["state"] = "stale"
        self.assert_error(self.invoke(mutate=stale), "stale_state")
        def terminal(session, run):
            session.finish_run(run, outcome="no_op", result_ref="results/already.json", effect_refs=[])
        self.assert_error(self.invoke(mutate=terminal), "permission_denied")
        def missing(session, _run):
            (self.root / session._started_receipts["query"]["carrier"]).unlink()
        self.assert_error(self.invoke(mutate=missing), "permission_denied")

    def test_another_session_root_cannot_supply_query_admission(self):
        def wrong_root(session, _run):
            session.tracker.root = self.root.parent
        self.assert_error(self.invoke(mutate=wrong_root), "permission_denied")

    def test_invalid_declaration_graph_is_not_a_successful_empty_match(self):
        cases = []
        missing = copy.deepcopy(self.rows); missing[1]["parent"] = "MISSING"; cases.append((missing, "schema_invalid"))
        cycle = copy.deepcopy(self.rows); cycle[2]["parent"] = "CHILD"; cases.append((cycle, "schema_invalid"))
        collision = copy.deepcopy(self.rows); collision[0]["scope_unit_name"] = "independent"; cases.append((collision, "target_ambiguous"))
        extra = copy.deepcopy(self.rows); extra[0]["lifecycle"] = "Active"; cases.append((extra, "schema_invalid"))
        for rows, code in cases:
            with self.subTest(code=code, rows=rows):
                self.structure.write_bytes(render_document({"schema_version": 1, "scope_units": rows}))
                self.selection = resolve_project(self.root)
                self.assert_error(self.invoke(self.filters(predicates=[{"field": "scope_unit_name", "match": "exact", "value": "NO_MATCH"}])), code)

    def test_entire_current_settings_schema_is_validated_without_boolean_attestation(self):
        for field, value in (("legacy", True), ("schema_version", 2), ("project.key", "independent"),
                             ("paths.journal_root", ".caprmedio_independent/_journal"),
                             ("artifacts.identity.project_prefix", "test")):
            with self.subTest(field=field):
                document = copy.deepcopy(self.fixture.document)
                keys = field.split("."); target = document
                for key in keys[:-1]:
                    target = target[key]
                target[keys[-1]] = value
                self.fixture.write_document(document)
                self.selection = resolve_project(self.root)
                self.assert_error(self.invoke(), "schema_invalid")

    def test_factory_requires_exact_distinct_complete_source_packet(self):
        from connector_scope_receiver import make_scope_query_receiver
        for sources in (self.schemas[:-1], [*self.schemas, self.schemas[0]], [*self.schemas, self.permission]):
            with self.subTest(count=len(sources)), self.assertRaises(ValueError):
                make_scope_query_receiver(self.selection, schema_sources=sources,
                                          action_definition=self.sources["CA-O-211"])
        original = self.sources["CA-D-441"]
        fake = self.root / "accepted-authority/substitution.md"
        fake.write_bytes(original.read_bytes() + b"\n# same header, different authority\n")
        replacement = capture_source(self.root, fake.relative_to(self.root))
        with self.assertRaises(ValueError):
            make_scope_query_receiver(self.selection,
                                      schema_sources=[replacement if source == original else source for source in self.schemas],
                                      action_definition=self.sources["CA-O-211"])

    def test_every_original_source_and_schema_pin_is_retained(self):
        handler = self.handler()
        paths = [self.fixture.settings, self.structure,
                 *[self.root / pin.relative_path for pin in self.schemas],
                 self.root / self.sources["CA-O-211"].relative_path]
        for path in paths:
            with self.subTest(path=path.name):
                original = path.read_bytes()
                def drift(_session, _run):
                    path.write_bytes(original + b"\n# independently introduced source drift\n")
                try:
                    self.assert_error(self.invoke(handler=handler, mutate=drift), "stale_state")
                finally:
                    path.write_bytes(original)

    def test_query_does_not_admit_requested_effects_or_read_operation(self):
        self.assert_error(self.invoke(effects=[{"type": "modify", "target": "delivery/ALPHA"}]), "input_invalid")
        self.assert_error(self.invoke(request_changes={"operation": "read", "query": None,
                          "target": {"kind": "Scope Unit", "identity": "ALPHA"}}), "unsupported_operation")

    def test_new_project_boundary_in_declared_frontier_is_not_silently_adopted(self):
        self.rows[2]["authority_path"] = ".caprmedio_independent/.caprmedio_foreign/ALPHA"
        self.structure.write_bytes(render_document({"schema_version": 1, "scope_units": self.rows}))
        self.selection = resolve_project(self.root)
        def introduce_boundary(_session, _run):
            nested = self.fixture.control / ".caprmedio_foreign"
            nested.mkdir(parents=True)
            (nested / "caprmedio_project_settings.toml").write_bytes(
                render_document({"project": {"name": "foreign"}, "paths": {"control_root": ".caprmedio_foreign"}}))
        self.assert_error(self.invoke(mutate=introduce_boundary), "schema_invalid")


if __name__ == "__main__":
    unittest.main()
