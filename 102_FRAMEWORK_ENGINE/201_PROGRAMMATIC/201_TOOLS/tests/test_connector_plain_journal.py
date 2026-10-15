"""Actual connector admission is independent of Journal persistence."""

import unittest
from unittest.mock import patch

import test_connector_session_admission as fixtures
from connector_bindings import ConnectorBindings, capture_source


class ConnectorPlainJournalTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ConnectorSessionAdmissionTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)

    def test_connector_read_succeeds_when_journal_append_fails(self):
        fixture = self.fixture

        def check(session, run):
            admission, request = fixture.admission(session, run)
            bindings = ConnectorBindings(
                admission,
                supported_operations={"read"},
                supported_kinds={"Scope Unit"},
                validate_payload=lambda _request: None,
                resolve_sources=lambda _request: [fixture.source],
                authority_sources=[capture_source(fixture.root, "schema.md")],
            )
            bound = bindings.bind(request)
            self.assertEqual(
                bound.sources[0].read_bytes(), (fixture.root / "action.md").read_bytes()
            )
            self.assertTrue(session.recording_errors)
            self.assertTrue(session.read_recorded_action_start(run).event_id)

        with patch.object(
            fixtures.LazyRunTracker,
            "_append_one",
            autospec=True,
            return_value="log unavailable",
        ):
            fixture.invoke(check)

    def test_absent_event_identity_is_not_permission_proof(self):
        def check(session, run):
            session.start_event_ids.clear()
            admission, request = self.fixture.admission(session, run)
            admission.check(request)
            self.assertIsNone(session.read_recorded_action_start(run).event_id)

        self.fixture.invoke(check)

    def test_assigned_action_cannot_change_after_binding(self):
        def check(session, run):
            admission, request = self.fixture.admission(session, run)
            session.request["assigned_action_id"] = "another-assigned-action"
            self.fixture.assert_code("permission_denied", lambda: admission.check(request))

        self.fixture.invoke(check)

    def test_another_actual_action_cannot_be_relabelled_before_binding(self):
        fixture = self.fixture
        checks = []

        def execute(_request, session):
            run = session.start_run("requested-action")
            self.assertEqual(run["definition"]["atom_id"], "CA-O-218")
            session.request["requested_runs"][0]["definition"]["atom_id"] = "CA-O-212"
            self.assertEqual(
                session.actual["requested-action"]["definition"]["atom_id"], "CA-O-218"
            )
            fixture.assert_code(
                "permission_denied", lambda: fixture.admission(session, run["run_id"])
            )
            checks.append(True)
            session.finish_run(
                run["run_id"], outcome="completed", result_ref="results/read.json", effect_refs=[]
            )

        tracker = fixture.make_tracker(execute)
        request = fixture.outer(tracker)
        request["requested_runs"][0]["definition"]["atom_id"] = "CA-O-218"
        result = tracker.run_selected_operation(request)
        self.assertNotIn("execution_error", result)
        self.assertEqual(checks, [True])

    def test_returned_start_does_not_alias_actual_definition(self):
        def check(session, run):
            returned = session.start_run("requested-action")
            returned["definition"]["atom_id"] = "CA-O-218"
            self.assertEqual(
                session.actual["requested-action"]["definition"]["atom_id"], "CA-O-212"
            )
            self.fixture.admission(session, run)

        self.fixture.invoke(check)


if __name__ == "__main__":
    unittest.main()
