"""Independent private Atom receiver checks with actual selected Action Sessions."""

from __future__ import annotations

import copy
import dataclasses
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest


TOOLS = Path(__file__).resolve().parents[1]
REPOSITORY = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(TOOLS))

from connector_atom_read import AtomSourceView  # noqa: E402
from connector_bindings import capture_source  # noqa: E402
from project_selection import resolve_project  # noqa: E402
from subject_notation import get_profile  # noqa: E402
from workflow_run_support import LazyRunTracker, RunExecutionSession, _canonical_digest  # noqa: E402


class AtomReceivingIndependentTests(unittest.TestCase):
    def setUp(self):
        scratch = REPOSITORY / ".caprmedio_tmp/tests/atom-receiving-independent"
        scratch.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        (self.root / ".git").mkdir()
        self.control = self.root / ".caprmedio_fixture"
        self.control.mkdir()
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname="fixture"\nkey="fixture"\nrepository_slug="fixture"\n'
            '[paths]\ncontrol_root=".caprmedio_fixture"\njournal_root=".caprmedio_fixture/_journal"\n'
            'runtime_root=".caprmedio_runtime"\n[artifacts.identity]\nproject_prefix="CA"\n',
        )
        self.owner = self.control / "UNIT"
        self.owner.mkdir()
        (self.control / "project_structure.toml").write_text(
            'schema_version=1\n[[scope_units]]\nscope_unit_name="UNIT"\nparent="PROJECT"\n'
            'scope_unit_type="Unordered"\nscope_unit_label="FEATURE"\nstructural_level=1\n'
            'navigational_order_number=0\nauthority_path=".caprmedio_fixture/UNIT"\ndelivery_path="native/UNIT"\n',
        )
        self.selection = resolve_project(self.root)
        self.first = self.write_atom("CA-R-1", "Thing/Part", ["Atom", 'atom(atom_id="CA-R-1")'], version=4)
        self.second = self.write_atom("CA-R-2", "Other", ["Thing/Part"], version=8, placement="done", status="Done")
        self.third = self.write_atom("CA-R-3", "Thingish", ["Atom"], version=2)
        self.frontier = tuple(capture_source(self.root, path.relative_to(self.root))
                              for path in (self.first, self.second, self.third))
        self.definitions = {}
        canonical = REPOSITORY / ".caprmedio_caprmedio"
        for atom_id in ("CA-D-625", "CA-R-1936", "CA-M-376", "CA-O-047", "CA-O-046"):
            candidates = [path for path in canonical.rglob(atom_id + "-*.md")
                          if "archive" not in path.parts and "_projection" not in path.parts
                          and "000_CAPRMEDIO_framework" not in path.parts]
            self.assertEqual(1, len(candidates), atom_id)
            path = self.root / "definitions" / candidates[0].name
            path.parent.mkdir(exist_ok=True)
            path.write_bytes(candidates[0].read_bytes())
            self.definitions[atom_id] = capture_source(self.root, path.relative_to(self.root))
        self.schemas = tuple(self.definitions[key] for key in ("CA-D-625", "CA-R-1936", "CA-M-376"))
        grammar = []
        for pin in get_profile("approved").grammar_pins:
            raw = (REPOSITORY / pin.path).read_bytes()
            self.assertEqual(pin.sha256, hashlib.sha256(raw).hexdigest())
            path = self.root / "definitions" / Path(pin.path).name
            path.write_bytes(raw)
            grammar.append(capture_source(self.root, path.relative_to(self.root)))
        self.query_schemas = (*self.schemas, *grammar)
        self.manifest_path = self.root / "manifest.json"
        self.manifest_path.write_text(json.dumps({pin.relative_path.as_posix(): pin.sha256
                                                 for pin in (*self.definitions.values(), *grammar)}, sort_keys=True))
        self.manifest = {"manifest_ref": "manifest.json", "manifest_digest": self.digest(self.manifest_path)}
        permission = self.root / "permission.md"
        permission.write_text("Permit the exact selected disposable Atom Read/Query; no modifications.")
        self.permission = capture_source(self.root, permission.relative_to(self.root))
        self.view = AtomSourceView(self.root, self.control, {"UNIT": self.owner}, ("UNIT",),
                                   ("active", "done"), "current", "approved", (), self.manifest)
        self.sequence = 0

    @staticmethod
    def digest(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def write_atom(self, identity, governs, dependencies, *, version=1, placement="", status="Active"):
        directory = self.owner / "04_requirement" / placement
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / (identity + "--exact-independent-fixture.md")
        path.write_text(
            f"---\n# retain this comment\natom_id: {identity}\ncontent_role: Requirement\ntype: Requirement\n"
            f"current_scope_unit: UNIT\nstatus: {status}\nversion: {version}\n"
            'updated_at: "2026-10-13 01:00:00 +0400"\n'
            f"subjects:\n  governs: {governs}\n  depends_on: {dependencies!r}\n"
            "extra_property: preserve this exactly\n---\n# Summary\n\nIndependent fixture.\n\n"
            "## Detail\n\nFull body with `literal` text and unchanged spacing.\n",
        )
        return path

    def snapshot(self):
        return {path.relative_to(self.root).as_posix(): path.read_bytes()
                for path in self.root.rglob("*") if path.is_file() and not path.is_symlink()}

    def filters(self, value="Thing/Part", mode="exact", fields=None):
        return {"scope_units": ["UNIT"], "lifecycles": ["active", "done"],
                "subjects": [{"fields": fields or ["governs", "depends_on"], "match": mode, "value": value}],
                "result_fields": ["status", "subjects"]}

    def inner(self, operation="read"):
        return {"operation": operation,
                "target": {"kind": "Atom", "identity": "CA-R-1"} if operation == "read" else None,
                "query": {"kind": "Atom", "filters": self.filters()} if operation == "query" else None,
                "delta": None, "expected_state": None, "authorization": self.permission.relative_path.as_posix(),
                "context": copy.deepcopy(self.manifest)}

    def receiver(self, operation="read", *, frontier=None, view=None, schemas=None):
        from connector_atom_receiver import make_atom_receiver
        return make_atom_receiver(
            self.selection, source_view=self.view if view is None else view,
            source_frontier=self.frontier if frontier is None else frontier,
            schema_sources=(self.query_schemas if operation == "query" else self.schemas) if schemas is None else schemas,
            action_definition=self.definitions["CA-O-046" if operation == "query" else "CA-O-047"],
            frontier_references=tuple(source.relative_path.as_posix() for source in self.frontier),
        )

    def invoke(self, receiver, inner=None, *, mutate=None, action=None, started=True, effects=None, terminal=False,
               frontier_refs=None, expected_factory_refusal=None):
        request = copy.deepcopy(self.inner() if inner is None else inner)
        atom_id = action or ("CA-O-046" if request["operation"] == "query" else "CA-O-047")
        version = 8 if atom_id == "CA-O-046" else 4
        definition = self.definitions[atom_id]
        self.sequence += 1
        frontier = [source.relative_path.as_posix() for source in self.frontier] if frontier_refs is None else frontier_refs
        effects = [] if effects is None else effects
        outer = {
            "mode": "preview", "request_id": f"independent-atoms-{self.sequence}",
            "operation_route": "fixture.atoms", "parameters": request, "parameters_digest": _canonical_digest(request),
            "target_frontier": frontier, "target_frontier_digest": _canonical_digest(frontier),
            "effects": effects, "effects_digest": _canonical_digest(effects), "definition_manifest": self.manifest,
            "source_freshness": {"selected_source_registry_ref": self.schemas[0].relative_path.as_posix(),
                                 "selected_source_registry_version": 2, "selected_source_registry_digest": self.schemas[0].sha256,
                                 "selected_binding_ref": definition.relative_path.as_posix(), "selected_binding_digest": definition.sha256},
            "initiative": {"initiative_id": "independent-atoms", "instruction_summary": "Observe exact supplied Atom criteria"},
            "requested_runs": [{"requested_run_id": "atom-action", "kind": "action", "definition": {
                "atom_id": atom_id, "version": version, "path": definition.relative_path.as_posix(), "digest": definition.sha256}}],
        }
        observed_pins = (*self.schemas, definition, self.permission, *self.frontier)
        captured = {}

        def observe(value):
            current = (self.digest(self.manifest_path) == self.manifest["manifest_digest"]
                       and all(self.digest(pin.root / pin.relative_path) == pin.sha256 for pin in observed_pins))
            return {"selected": value["operation_route"] == "fixture.atoms", "current": current,
                    "observed": {"manifest_digest": self.digest(self.manifest_path)}}

        def execute(_request, session):
            self.assertIsInstance(session, RunExecutionSession)
            if started:
                session.start_run("atom-action", run_id="actual-atom-action")
            if terminal:
                session.finish_run("actual-atom-action", outcome="no_op", result_ref="results/prior.json", effect_refs=[])
            if mutate:
                mutate(session)
            before = self.snapshot()
            try:
                if expected_factory_refusal is not None:
                    session.read_recorded_action_start("actual-atom-action")
                    with self.assertRaisesRegex(ValueError, expected_factory_refusal):
                        receiver(session, "actual-atom-action")
                    captured["factory_refused"] = True
                else:
                    captured["result"] = receiver(session, "actual-atom-action")
            finally:
                self.assertEqual(before, self.snapshot(), "Receiver changed source or canonical Session/Journal evidence")
                session.tracker.root = self.root
            if started and not terminal:
                failed = expected_factory_refusal is not None or captured["result"]["errors"]
                session.finish_run("actual-atom-action", outcome="failed" if failed else "completed",
                                   result_ref="results/atoms.json", effect_refs=[])

        tracker = LazyRunTracker(self.root, source_observer=observe, executor=execute,
                                 journal_context={"author": "independent-test-operator", "timezone": "UTC"})
        preview = tracker.run_selected_operation(outer)
        outer.update(mode="execute", proposal_receipt=preview["proposal_receipt"],
                     proposal_receipt_digest=preview["proposal_receipt_digest"], assigned_action_id="assigned-atoms")
        fields = ("request_id", "operation_route", "proposal_receipt_digest", "parameters_digest",
                  "target_frontier_digest", "effects_digest", "definition_manifest", "source_freshness")
        outer["operator_authorization"] = {
            "authorization_ref": self.permission.relative_path.as_posix(),
            "authorization_freshness": {"state": "current", "digest": self.permission.sha256},
            **{field: copy.deepcopy(outer[field]) for field in fields},
        }
        outcome = tracker.run_selected_operation(outer)
        if expected_factory_refusal is not None:
            self.assertTrue(captured.get("factory_refused"), outcome)
            self.assertEqual("terminal", outcome["disposition"])
            return outcome
        self.assertIn("result", captured, outcome)
        result = captured["result"]
        self.assertEqual({"data", "current_state", "effects", "errors"}, set(result))
        self.assertEqual([], result["effects"])
        return result

    def assert_refused(self, result, code=None):
        self.assertIsNone(result["data"])
        self.assertTrue(result["errors"])
        self.assertTrue(all(set(error) == {"code", "message", "field"} for error in result["errors"]))
        if code is not None:
            self.assertEqual(code, result["errors"][0]["code"])

    def test_complete_read_is_independent_of_query_and_preserves_full_source_actual_version_and_state(self):
        result = self.invoke(self.receiver())
        self.assertEqual([], result["errors"])
        self.assertEqual(self.first.read_text(), result["data"]["source"])
        self.assertEqual("CA-R-1", result["data"]["atom_id"])
        self.assertEqual(4, result["data"]["version"])
        self.assertEqual("UNIT", result["data"]["current_scope_unit"])
        self.assertIn("extra_property: preserve this exactly", result["data"]["frontmatter"])
        self.assertIn("## Detail", result["data"]["content"])
        self.assertEqual(self.digest(self.first), result["current_state"]["source_token"])
        self.assertEqual(self.manifest, result["current_state"]["source_view"])
        request = self.inner()
        request["expected_state"] = result["current_state"]
        self.assertEqual(result, self.invoke(self.receiver(), request))

    def test_query_returns_complete_empty_singular_multiple_and_exact_requested_values(self):
        for value, fields, identities in (
            ("absent", ["governs", "depends_on"], []), ("Thing/Part", ["governs"], ["CA-R-1"]),
            ("Thing/Part", ["governs", "depends_on"], ["CA-R-1", "CA-R-2"]),
        ):
            with self.subTest(value=value, fields=fields):
                request = self.inner("query")
                request["query"]["filters"] = self.filters(value, fields=fields)
                result = self.invoke(self.receiver("query"), request)
                self.assertEqual([], result["errors"])
                self.assertTrue(result["data"]["complete"])
                self.assertEqual(identities, [row["atom_id"] for row in result["data"]["matches"]])
                self.assertEqual(self.manifest, result["data"]["source_view"])
                for row in result["data"]["matches"]:
                    self.assertEqual({"atom_id", "version", "current_scope_unit", "status", "subjects"}, set(row))
                request["expected_state"] = result["current_state"]
                self.assertEqual(result, self.invoke(self.receiver("query"), request))

    def test_wrong_action_wrong_operation_unstarted_and_terminal_sessions_refuse(self):
        self.assert_refused(self.invoke(self.receiver(), action="CA-O-046"), "permission_denied")
        self.assert_refused(self.invoke(self.receiver("query"), self.inner("query"), action="CA-O-047"), "permission_denied")
        self.assert_refused(self.invoke(self.receiver(), self.inner("query")))
        self.assert_refused(self.invoke(self.receiver(), started=False), "permission_denied")
        self.assert_refused(self.invoke(self.receiver(), terminal=True), "permission_denied")
        self.assert_refused(self.receiver()(True, "actual-atom-action"), "permission_denied")

    def test_mismatched_context_authorization_and_exact_read_pins_refuse(self):
        for field, value, code in (("context", "unresolved", "input_invalid"),
                                   ("authorization", "another-permission", "permission_denied"),
                                   ("expected_state", {"version": 3}, "stale_state")):
            with self.subTest(field=field):
                request = self.inner()
                request[field] = value
                self.assert_refused(self.invoke(self.receiver(), request), code)
        request = self.inner()
        request["target"]["identity"] = "CA-R-999"
        self.assert_refused(self.invoke(self.receiver(), request), "target_not_found")

    def test_session_parameter_and_authorization_drift_refuse(self):
        def stale_authorization(session):
            session.request["operator_authorization"]["authorization_freshness"]["state"] = "stale"
        self.assert_refused(self.invoke(self.receiver(), mutate=stale_authorization), "stale_state")
        def mismatch(session):
            session.request["parameters"]["target"]["identity"] = "CA-R-2"
        self.assert_refused(self.invoke(self.receiver(), mutate=mismatch))

    def test_actual_start_source_and_admitted_frontier_drift_refuse_without_recapture(self):
        for path in (self.first, self.root / self.definitions["CA-O-047"].relative_path,
                     self.root / self.schemas[0].relative_path):
            with self.subTest(path=path.name):
                original = path.read_bytes()
                self.assert_refused(self.invoke(self.receiver(), mutate=lambda _, path=path: path.write_bytes(original + b"\n# drift\n")), "stale_state")
                path.write_bytes(original)
        def remove_start(session):
            (self.root / session._started_receipts["atom-action"]["carrier"]).unlink()
        self.assert_refused(self.invoke(self.receiver(), mutate=remove_start), "permission_denied")

    def test_incomplete_and_late_changed_source_frontiers_refuse_instead_of_complete_results(self):
        self.assert_refused(self.invoke(self.receiver(), frontier_refs=["unrelated-scope-reference"]), "permission_denied")
        self.assert_refused(self.invoke(self.receiver(frontier=self.frontier[:-1])), "stale_state")
        self.assert_refused(self.invoke(self.receiver("query", frontier=self.frontier[:-1]), self.inner("query")), "stale_state")
        created = []
        def introduce(_session):
            created.append(self.write_atom("CA-R-4", "New", []))
        self.assert_refused(self.invoke(self.receiver(), mutate=introduce), "stale_state")
        created[0].unlink()

    def test_missing_query_criteria_wrong_frontier_and_malformed_sources_cannot_report_complete(self):
        for missing in ("scope_units", "lifecycles", "subjects", "result_fields"):
            with self.subTest(missing=missing):
                request = self.inner("query")
                del request["query"]["filters"][missing]
                self.assert_refused(self.invoke(self.receiver("query"), request), "input_invalid")
        request = self.inner("query")
        request["query"]["filters"]["scope_units"] = ["OTHER"]
        self.assert_refused(self.invoke(self.receiver("query"), request), "input_invalid")
        self.first.write_bytes(b"---\natom_id: CA-R-1\natom_id: CA-R-1\n---\n")
        frontier = tuple(capture_source(self.root, path.relative_to(self.root)) for path in (self.first, self.second, self.third))
        self.frontier = frontier
        self.assert_refused(self.invoke(self.receiver("query", frontier=frontier), self.inner("query")), "schema_invalid")

    def test_invalid_private_view_schema_or_boolean_binding_does_not_become_admission(self):
        with self.assertRaises((TypeError, ValueError)):
            self.receiver(view=dataclasses.replace(self.view, owners={}))
        self.assert_refused(self.invoke(self.receiver(view=dataclasses.replace(self.view, attribution="unresolved"))), "input_invalid")
        with self.assertRaises((TypeError, ValueError)):
            self.receiver("query", schemas=self.schemas)
        self.assert_refused(self.invoke(self.receiver(), effects=[{"type": "write", "target": "unrelated.md"}]))

    def replace_definition_bytes(self, identity, raw):
        path = self.root / self.definitions[identity].relative_path
        path.write_bytes(raw)
        self.definitions[identity] = capture_source(self.root, path.relative_to(self.root))
        self.schemas = tuple(self.definitions[key] for key in ("CA-D-625", "CA-R-1936", "CA-M-376"))
        self.query_schemas = (*self.schemas, *self.query_schemas[3:])
        self.manifest_path.write_text(json.dumps(
            {pin.relative_path.as_posix(): pin.sha256
             for pin in (*self.definitions.values(), *self.query_schemas[3:])}, sort_keys=True))
        self.manifest["manifest_digest"] = self.digest(self.manifest_path)

    def test_rehashed_resealed_same_identity_schema_substitution_refuses(self):
        for identity in ("CA-D-625", "CA-R-1936", "CA-M-376"):
            original = (self.root / self.definitions[identity].relative_path).read_bytes()
            for operation in ("read", "query"):
                with self.subTest(identity=identity, operation=operation):
                    self.replace_definition_bytes(identity, original + b"\nAltered contract semantics.\n")
                    try:
                        self.invoke(lambda _session, _run: self.receiver(operation), self.inner(operation),
                                    expected_factory_refusal="accepted connector contract revision")
                    finally:
                        self.replace_definition_bytes(identity, original)

    def test_rehashed_resealed_same_identity_action_substitution_refuses(self):
        for identity, operation in (("CA-O-047", "read"), ("CA-O-046", "query")):
            with self.subTest(identity=identity, operation=operation):
                original = (self.root / self.definitions[identity].relative_path).read_bytes()
                self.replace_definition_bytes(identity, original + b"\nAltered Action semantics.\n")
                try:
                    self.invoke(lambda _session, _run: self.receiver(operation), self.inner(operation),
                                expected_factory_refusal="exact accepted Atom Action revision")
                finally:
                    self.replace_definition_bytes(identity, original)


if __name__ == "__main__":
    unittest.main()
