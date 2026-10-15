"""Shared connector bindings consume real started selected Action Sessions."""

import copy
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from connector_bindings import ConnectorBindingError, admission_for_started_action, capture_source
from workflow_run_support import LazyRunTracker, _canonical_digest


class ConnectorSessionAdmissionTests(unittest.TestCase):
    def setUp(self):
        scratch = Path(__file__).resolve().parents[4] / ".caprmedio_tmp"
        scratch.mkdir(exist_ok=True)
        temporary = tempfile.TemporaryDirectory(prefix="connector-session-", dir=scratch)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / ".git").mkdir()
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root=".caprmedio_caprmedio"\njournal_root=".caprmedio_caprmedio/_journal"\n'
            'runtime_root=".caprmedio_runtime"\n',
        )
        for name, raw in (("action.md", b"---\natom_id: CA-O-212\ncontent_role: Operations\ntype: Action\nstatus: Active\nversion: 1\n---\n# Action\n"),
                          ("manifest.json", b"exact selected manifest"), ("schema.md", b"exact schema"),
                          ("permission.md", b"explicit read permission")):
            (self.root / name).write_bytes(raw)
        self.source = capture_source(self.root, "action.md")
        self.manifest = {"manifest_ref": "manifest.json", "manifest_digest": self.digest("manifest.json")}
        self.permission_digest = self.digest("permission.md")
        self.request_sequence = 0
        self.request = {
            "operation": "read", "target": {"kind": "Scope Unit", "identity": "TOOLS"},
            "query": None, "delta": None, "expected_state": None,
            "authorization": "permission.md", "context": self.manifest,
        }

    def digest(self, name):
        return hashlib.sha256((self.root / name).read_bytes()).hexdigest()

    def make_tracker(self, executor):
        def observe(outer):
            current = (self.digest("manifest.json") == outer["definition_manifest"]["manifest_digest"]
                       and self.digest("permission.md") == self.permission_digest)
            return {"selected": outer["operation_route"] == "fixture-existing-route", "current": current,
                    "observed": {"manifest_digest": self.digest("manifest.json")}}
        return LazyRunTracker(self.root, source_observer=observe, executor=executor,
                              journal_context={"author": "trusted-operator", "timezone": "UTC"})

    def outer(self, tracker, *, kind="action"):
        self.request_sequence += 1
        parameters = copy.deepcopy(self.request)
        frontier, effects = ["action.md"], []
        outer = {
            "mode": "preview", "request_id": f"connector-session-fixture-{self.request_sequence}", "operation_route": "fixture-existing-route",
            "parameters": parameters, "parameters_digest": _canonical_digest(parameters),
            "target_frontier": frontier, "target_frontier_digest": _canonical_digest(frontier),
            "effects": effects, "effects_digest": _canonical_digest(effects), "definition_manifest": self.manifest,
            "source_freshness": {"selected_source_registry_ref": "schema.md", "selected_source_registry_version": 1,
                                 "selected_source_registry_digest": self.digest("schema.md"),
                                 "selected_binding_ref": "manifest.json", "selected_binding_digest": self.digest("manifest.json")},
            "initiative": {"initiative_id": "fixture", "instruction_summary": "explicit read"},
        }
        preview = tracker.run_selected_operation(outer)
        outer.update(mode="execute", proposal_receipt=preview["proposal_receipt"],
                     proposal_receipt_digest=preview["proposal_receipt_digest"], assigned_action_id="assigned-action",
                     requested_runs=[{"requested_run_id": "requested-action", "kind": kind,
                                      "definition": {"atom_id": "CA-O-212", "version": 1,
                                                     "path": "action.md", "digest": self.source.sha256}}])
        fields = ("request_id", "operation_route", "proposal_receipt_digest", "parameters_digest",
                  "target_frontier_digest", "effects_digest", "definition_manifest", "source_freshness")
        outer["operator_authorization"] = {
            "authorization_ref": "permission.md", "authorization_freshness": {"state": "current", "digest": self.permission_digest},
            **{key: copy.deepcopy(outer[key]) for key in fields},
        }
        return outer

    @staticmethod
    def mapping(outer):
        return outer["parameters"], outer["definition_manifest"]

    def admission(self, session, run_id, **changes):
        options = dict(root=self.root, action_definition=self.source, action_atom_id="CA-O-212", action_version=1,
                       map_request=self.mapping)
        options.update(changes)
        return admission_for_started_action(session, run_id, **options)

    def invoke(self, callback, *, kind="action", start=True):
        values, errors = [], []
        def executor(_outer, session):
            run_id = session.start_run("requested-action", run_id="actual-action")["run_id"] if start else "actual-action"
            try:
                values.append(callback(session, run_id))
            except BaseException as error:
                errors.append(error)
            if start and "requested-action" not in session.terminal:
                session.finish_run(run_id, outcome="completed", result_ref="results/read.json", effect_refs=[])
        tracker = self.make_tracker(executor)
        result = tracker.run_selected_operation(self.outer(tracker, kind=kind))
        if errors:
            raise errors[0]
        self.assertNotIn("execution_error", result)
        self.assertEqual(len(values), 1)
        return values[0]

    def assert_code(self, code, operation):
        with self.assertRaises(ConnectorBindingError) as refused:
            operation()
        self.assertEqual(refused.exception.code, code)

    def test_real_started_session_derives_request_without_new_journal_or_run(self):
        def check(session, run_id):
            before = {path: path.read_bytes() for path in self.root.rglob("*.ndjson")}
            actual = copy.deepcopy(session.actual)
            admission, request = self.admission(session, run_id)
            admission.check(request)
            self.assertEqual(request, self.request)
            self.assertIsNot(request, session.request["parameters"])
            self.assertEqual(session.actual, actual)
            self.assertEqual(before, {path: path.read_bytes() for path in self.root.rglob("*.ndjson")})
        self.invoke(check)

    def test_boolean_or_caller_object_cannot_attest_session(self):
        for session in (True, {"sealed_outer_admission": True}, object()):
            self.assert_code("permission_denied", lambda: self.admission(session, "actual-action"))

    def test_unstarted_or_non_action_run_refuses(self):
        self.invoke(lambda session, run: self.assert_code("permission_denied", lambda: self.admission(session, run)), start=False)
        self.invoke(lambda session, run: self.assert_code("permission_denied", lambda: self.admission(session, run)), kind="workflow")

    def test_wrong_required_action_and_version_refuse(self):
        def check(session, run):
            for options in ({"action_atom_id": "CA-O-218"}, {"action_version": 2}):
                self.assert_code("permission_denied", lambda: self.admission(session, run, **options))
        self.invoke(check)

    def test_another_project_root_refuses(self):
        other = self.root / "other"
        other.mkdir()
        self.invoke(lambda session, run: self.assert_code("permission_denied", lambda: self.admission(session, run, root=other)))

    def test_terminal_action_refuses(self):
        def check(session, run):
            session.finish_run(run, outcome="completed", result_ref="results/first.json", effect_refs=[])
            self.assert_code("permission_denied", lambda: self.admission(session, run))
        self.invoke(check)

    def test_action_pin_is_rechecked_after_binding(self):
        def check(session, run):
            admission, request = self.admission(session, run)
            (self.root / "action.md").write_bytes(b"changed actual definition")
            self.assert_code("stale_state", lambda: admission.check(request))
        self.invoke(check)

    def test_actual_run_remains_admitted_without_a_start_log(self):
        def check(session, run):
            admission, request = self.admission(session, run)
            next(self.root.rglob("*.ndjson")).unlink()
            admission.check(request)
            self.assertEqual(session.read_recorded_action_start(run).action_run_id, run)
        self.invoke(check)

    def test_native_source_and_permission_currentness_are_rechecked(self):
        def check(session, run):
            admission, request = self.admission(session, run)
            (self.root / "permission.md").write_bytes(b"revoked permission")
            self.assert_code("stale_state", lambda: admission.check(request))
        self.invoke(check)

    def test_logical_substitution_context_and_authorization_refuse(self):
        def check(session, run):
            admission, request = self.admission(session, run)
            self.assert_code("permission_denied", lambda: admission.check(dict(request, authorization="another-permission")))
            self.assert_code("permission_denied", lambda: admission.check(dict(request, target={"kind": "Scope Unit", "identity": "OTHER"})))
            self.assert_code("input_invalid", lambda: self.admission(session, run, map_request=lambda outer: (outer["parameters"], "unresolved")))
        self.invoke(check)

    def test_session_request_cannot_change_after_binding(self):
        def check(session, run):
            admission, request = self.admission(session, run)
            session.request["parameters"]["target"]["identity"] = "OTHER"
            self.assert_code("permission_denied", lambda: admission.check(request))
        self.invoke(check)

    def test_recorded_start_cannot_bind_another_assigned_action(self):
        def check(session, run):
            session.request["assigned_action_id"] = "another-assigned-action"
            self.assert_code("permission_denied", lambda: self.admission(session, run))
        self.invoke(check)

    def test_missing_private_mapping_fails_closed(self):
        self.invoke(lambda session, run: self.assert_code("input_invalid", lambda: self.admission(session, run, map_request=None)))


if __name__ == "__main__":
    unittest.main()
