"""Independent actual-Session connector checks; no complete Settings-schema claim."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import tomllib
import unittest

TOOLS = Path(__file__).resolve().parents[1]
REPOSITORY = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(TOOLS))

from connector_bindings import ConnectorBindingError, capture_source
from project_selection import resolve_project
from workflow_run_support import LazyRunTracker, RunExecutionSession, _canonical_digest


class ConnectorReceivingIndependentTests(unittest.TestCase):
    def setUp(self):
        scratch = REPOSITORY / ".caprmedio_tmp"
        scratch.mkdir(exist_ok=True)
        directory = tempfile.TemporaryDirectory(prefix="receiving-independent-", dir=scratch)
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name).resolve()
        (self.root / ".git").mkdir()
        control = self.root / ".caprmedio_fixture"
        control.mkdir()
        self.settings = control / "caprmedio_project_settings.toml"
        self.structure = control / "project_structure.toml"
        self.settings.write_text(
            '[project]\nname="fixture"\nkey="fixture"\nrepository_slug="fixture-repo"\n'
            '[paths]\ncontrol_root=".caprmedio_fixture"\njournal_root=".caprmedio_fixture/_journal"\n'
            'runtime_root=".caprmedio_runtime"\n[artifacts.identity]\nproject_prefix="FIX"\n',
            encoding="utf-8",
        )
        self.structure.write_text(
            '# exact native document\nschema_version=1\n[[scope_units]]\n'
            'scope_unit_name="UNIT"\nparent="PROJECT"\nscope_unit_type="Unordered"\n'
            'scope_unit_label="FEATURE"\nstructural_level=1\nnavigational_order_number=0\n'
            'authority_path=".caprmedio_fixture/UNIT"\ndelivery_path="native/UNIT"\n',
            encoding="utf-8",
        )
        self.selection = resolve_project(self.root)
        self.expected_settings = tomllib.loads(self.settings.read_text())
        self.sources = {}
        for identifier in ("CA-D-625", "CA-D-527", "CA-D-441", "CA-D-442", "CA-O-212", "CA-O-218"):
            candidates = [path for path in (REPOSITORY / ".caprmedio_caprmedio").rglob(identifier + "-*.md")
                          if "/archive/" not in path.as_posix() and "/_projection/" not in path.as_posix()
                          and "/000_CAPRMEDIO_framework/" not in path.as_posix()]
            self.assertEqual(len(candidates), 1, identifier)
            path = self.root / "definitions" / (identifier + ".md")
            path.parent.mkdir(exist_ok=True)
            path.write_bytes(candidates[0].read_bytes())
            self.sources[identifier] = capture_source(self.root, path.relative_to(self.root))
        permission = self.root / "permission.md"
        permission.write_text("Read one exact fixture target through the selected Action.", encoding="utf-8")
        self.permission = capture_source(self.root, "permission.md")
        fixture_schema = self.root / "definitions" / "TEST-D-1.md"
        fixture_schema.write_text('---\natom_id: TEST-D-1\nversion: 1\n---\n' + json.dumps(self.expected_settings), encoding="utf-8")
        self.fixture_schema = capture_source(self.root, fixture_schema.relative_to(self.root))

    def validate_fixture_settings(self, document):
        # This complete closed disposable fixture admission is an injected dependency,
        # not a production validator for unresolved legacy/open Settings fields.
        admitted = json.loads(self.fixture_schema.read_bytes().decode().split("\n---\n", 1)[1])
        if document != admitted:
            raise ConnectorBindingError("schema_invalid", "Entire disposable Settings declaration differs.", "context")

    def handler(self, kind="configuration", *, selection=None):
        schemas = (*[self.sources[key] for key in ("CA-D-625", "CA-D-527", "CA-D-441", "CA-D-442")], self.fixture_schema)
        if kind == "configuration":
            from connector_configuration_receiver import make_configuration_read_receiver
            return make_configuration_read_receiver(
                selection or self.selection, schema_sources=schemas, action_definition=self.sources["CA-O-218"],
                validate_settings=self.validate_fixture_settings,
            )
        from connector_scope_receiver import make_scope_read_receiver
        return make_scope_read_receiver(
            selection or self.selection, validate_settings=self.validate_fixture_settings,
            schema_sources=schemas, action_definition=self.sources["CA-O-212"],
        )

    def snapshot(self):
        return {path.relative_to(self.root).as_posix(): path.read_bytes()
                for path in self.root.rglob("*") if path.is_file()}

    def invoke(self, handler, *, kind="configuration", identity=None, action=None, mutate=None, effects=None):
        atom_id = action or ("CA-O-218" if kind == "configuration" else "CA-O-212")
        action_source = self.sources[atom_id]
        manifest = {"manifest_ref": "definitions/CA-D-625.md", "manifest_digest": self.sources["CA-D-625"].sha256}
        inner = {
            "operation": "read", "target": {"kind": "Configuration" if kind == "configuration" else "Scope Unit",
                                            "identity": identity or ("Project Structure" if kind == "configuration" else "UNIT")},
            "query": None, "delta": None, "expected_state": None,
            "authorization": "permission.md", "context": manifest,
        }
        captured = {}
        pins = tuple(self.sources.values()) + (self.permission, self.fixture_schema)

        def observe(request):
            current = all(hashlib.sha256((pin.root / pin.relative_path).read_bytes()).hexdigest() == pin.sha256 for pin in pins)
            return {"selected": request["operation_route"] == "fixture.read", "current": current,
                    "observed": {"definition_manifest": manifest}}

        def execute(_request, session):
            self.assertIsInstance(session, RunExecutionSession)
            actual = session.start_run("read", run_id="actual-read")
            if mutate:
                mutate(session, actual["run_id"])
            before = self.snapshot()
            try:
                captured["result"] = handler(session, actual["run_id"])
            except Exception as error:
                captured["exception"] = error
            captured["unchanged"] = before == self.snapshot()
            session.tracker.root = self.root
            if "read" not in session.terminal:
                refused = "exception" in captured or bool(captured["result"]["errors"])
                session.finish_run(actual["run_id"], outcome="failed" if refused else "completed",
                                   result_ref="results/read.json", effect_refs=[])

        tracker = LazyRunTracker(self.root, source_observer=observe, executor=execute,
                                 journal_context={"author": "independent-test-operator", "timezone": "UTC"})
        outer = {
            "mode": "preview", "request_id": "read-" + _canonical_digest(inner)[:12],
            "operation_route": "fixture.read", "parameters": inner, "parameters_digest": _canonical_digest(inner),
            "target_frontier": [self.structure.relative_to(self.root).as_posix()],
            "target_frontier_digest": _canonical_digest([self.structure.relative_to(self.root).as_posix()]),
            "effects": effects or [], "effects_digest": _canonical_digest(effects or []), "definition_manifest": manifest,
            "source_freshness": {"selected_source_registry_ref": "definitions/CA-D-625.md", "selected_source_registry_version": 2,
                                 "selected_source_registry_digest": self.sources["CA-D-625"].sha256,
                                 "selected_binding_ref": action_source.relative_path.as_posix(), "selected_binding_digest": action_source.sha256},
            "initiative": {"initiative_id": "independent-read", "instruction_summary": "read one exact selected fixture"},
            "requested_runs": [{"requested_run_id": "read", "kind": "action", "definition": {
                "atom_id": atom_id, "version": 2 if atom_id == "CA-O-218" else 3,
                "path": action_source.relative_path.as_posix(), "digest": action_source.sha256}}],
        }
        preview = tracker.run_selected_operation(outer)
        outer.update(mode="execute", proposal_receipt=preview["proposal_receipt"],
                     proposal_receipt_digest=preview["proposal_receipt_digest"], assigned_action_id="assigned-read")
        outer["operator_authorization"] = {
            "authorization_ref": "permission.md", "authorization_freshness": {"state": "current", "digest": self.permission.sha256},
            **{field: copy.deepcopy(outer[field]) for field in ("request_id", "operation_route", "proposal_receipt_digest", "parameters_digest",
                                                              "target_frontier_digest", "effects_digest", "definition_manifest", "source_freshness")},
        }
        outcome = tracker.run_selected_operation(outer)
        self.assertIn("unchanged", captured, outcome)
        self.assertTrue(captured["unchanged"], "Receiver changed source or canonical Run evidence.")
        if "exception" in captured:
            raise captured["exception"]
        result = captured["result"]
        self.assertEqual(result["effects"], [])
        return result

    def assert_refused(self, result, code=None):
        self.assertIsNone(result["data"])
        self.assertTrue(result["errors"])
        if code:
            self.assertEqual(result["errors"][0]["code"], code)

    def test_structure_read_has_exact_text_complete_document_and_actual_state(self):
        result = self.invoke(self.handler())
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["data"]["source_text"].encode(), self.structure.read_bytes())
        self.assertEqual(result["data"]["document"], tomllib.loads(self.structure.read_text()))
        self.assertEqual(result["current_state"]["sha256"], hashlib.sha256(self.structure.read_bytes()).hexdigest())

    def test_scope_read_uses_supplied_complete_fixture_dependency(self):
        result = self.invoke(self.handler("scope"), kind="scope")
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["data"]["declaration"], self.selection.structure["scope_units"][0])

    def test_wrong_action_is_refused(self):
        self.assert_refused(self.invoke(self.handler(), action="CA-O-212"), "permission_denied")

    def test_terminal_actual_action_is_refused(self):
        def terminal(session, run_id):
            session.finish_run(run_id, outcome="no_op", result_ref="results/earlier.json", effect_refs=[])
        self.assert_refused(self.invoke(self.handler(), mutate=terminal), "permission_denied")

    def test_stale_authorization_is_refused(self):
        def stale(session, _run_id):
            session.request["operator_authorization"]["authorization_freshness"]["state"] = "stale"
        self.assert_refused(self.invoke(self.handler(), mutate=stale), "stale_state")

    def test_source_change_after_selection_cannot_be_recaptured_as_current(self):
        self.structure.write_bytes(self.structure.read_bytes() + b"\n# changed after selection\n")
        self.assert_refused(self.invoke(self.handler()), "stale_state")

    def test_definition_change_after_actual_start_is_refused(self):
        def stale(_session, _run_id):
            path = self.root / self.sources["CA-O-218"].relative_path
            path.write_bytes(path.read_bytes() + b"\nchanged\n")
        self.assert_refused(self.invoke(self.handler(), mutate=stale), "stale_state")

    def test_missing_recorded_start_is_refused(self):
        def remove(session, _run_id):
            path = self.root / session._started_receipts["read"]["carrier"]
            path.unlink()
        self.assert_refused(self.invoke(self.handler(), mutate=remove), "permission_denied")

    def test_other_project_session_root_is_refused(self):
        def wrong_root(session, _run_id):
            session.tracker.root = self.root.parent
        self.assert_refused(self.invoke(self.handler(), mutate=wrong_root), "permission_denied")

    def test_scope_read_refuses_declared_outer_mutation_effect(self):
        self.assert_refused(self.invoke(self.handler("scope"), kind="scope",
                                       effects=[{"type": "modify", "target": "native/UNIT"}]), "input_invalid")

    def test_structure_read_refuses_declared_outer_mutation_effect(self):
        self.assert_refused(self.invoke(self.handler(), effects=[{"type": "modify", "target": "native/UNIT"}]), "permission_denied")

    def test_boolean_settings_attestation_is_not_complete_validation(self):
        from connector_scope_receiver import make_scope_read_receiver
        handler = make_scope_read_receiver(
            self.selection, validate_settings=lambda _document: True,
            schema_sources=(*self.sources.values(), self.fixture_schema), action_definition=self.sources["CA-O-212"],
        )
        self.assert_refused(self.invoke(handler, kind="scope"), "schema_invalid")
