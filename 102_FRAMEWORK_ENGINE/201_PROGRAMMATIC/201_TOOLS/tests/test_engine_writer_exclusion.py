"""Real alternate writers share the Engine boundary; fixtures are not live Projects."""

from __future__ import annotations

from contextlib import contextmanager, redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import artifact_metadata
import lifecycle_intents
from engine_publication_lock import EnginePublicationLockError, engine_publication_lock
from lifecycle_intents import LifecycleError, carrier_descriptor, change_status_atom_action
from test_engine_publication_lock import read_event, start_child
import test_selected_atom_lifecycle as lifecycle_fixtures


WRITER = r"""
from contextlib import redirect_stdout
import io, json, sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import RELEASE_VERSION.selector_publication_lock as mechanics
original_stdout = sys.stdout
original_flock = mechanics.fcntl.flock
reported = False
def observed_flock(descriptor, operation):
    global reported
    try:
        return original_flock(descriptor, operation)
    except BlockingIOError:
        if not reported:
            print('contended', file=original_stdout, flush=True)
            reported = True
        raise
mechanics.fcntl.flock = observed_flock
root, path, mode = Path(sys.argv[2]), Path(sys.argv[3]), sys.argv[4]
print('ready', file=original_stdout, flush=True)
output = io.StringIO()
try:
    with redirect_stdout(output):
        if mode == 'status':
            from lifecycle_intents import carrier_descriptor, change_status_atom_action
            result = change_status_atom_action(
                root, {'target': carrier_descriptor(root, path.relative_to(root).as_posix()),
                       'status': 'Archived'}, execute=True, authorized=True)
        else:
            import artifact_metadata
            sys.argv = ['artifact_metadata', str(path), '--kind', 'atom']
            if mode == 'apply':
                sys.argv.append('--apply')
            result = artifact_metadata.main()
    response = {'outcome': 'returned', 'result': result, 'output': output.getvalue()}
except BaseException as error:
    response = {'outcome': 'raised', 'type': type(error).__name__,
                'code': getattr(error, 'code', None), 'message': str(error)}
print(json.dumps(response), file=original_stdout, flush=True)
"""


class EngineWriterExclusionTests(unittest.TestCase):
    def setUp(self):
        scratch = TOOLS.parents[2] / ".caprmedio_tmp" / "tests"
        scratch.mkdir(parents=True, exist_ok=True)
        self.fixture = tempfile.TemporaryDirectory(prefix="engine-writers-", dir=scratch)
        self.addCleanup(self.fixture.cleanup)
        self.root = Path(self.fixture.name)
        settings = self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        settings.parent.mkdir()
        settings.write_text('[artifact_timestamps]\ntimezone = "UTC"\n', encoding="utf-8")
        self.path = self.root / "CA-R-42--fixture.md"
        self.before = b'---\natom_id: CA-R-42\nversion: 1\nupdated_at: "2026-01-01 00:00:00 +0000"\n---\nExact initial body\n'
        self.path.write_bytes(self.before)
        self.assertEqual(artifact_metadata.repository_root(self.path), self.root)

    def writer(self, mode, *, root=None, path=None):
        child = start_child(self, WRITER, root or self.root, path or self.path, mode)
        self.assertEqual(read_event(self, child), "ready")
        return child

    def returned(self, child):
        response = json.loads(read_event(self, child))
        self.assertEqual(response["outcome"], "returned", response)
        child.communicate(timeout=5)
        self.assertEqual(child.returncode, 0)
        return response

    def test_metadata_apply_cannot_read_or_mutate_carrier_before_shared_owner_releases(self):
        with engine_publication_lock(self.root, timeout_seconds=0):
            child = self.writer("apply")
            self.assertEqual(read_event(self, child), "contended")
            self.assertEqual(self.path.read_bytes(), self.before)
            reviewed = self.before.replace(b"version: 1", b"version: 4").replace(
                b"Exact initial body", b"Exact body retained by the current owner")
            self.path.write_bytes(reviewed)
        response = self.returned(child)
        self.assertEqual(response["result"], 0)
        result = self.path.read_bytes()
        self.assertIn(b"version: 5\n", result)
        self.assertTrue(result.endswith(b"Exact body retained by the current owner\n"))

    def test_metadata_preview_does_not_wait_for_mutating_lock_or_write(self):
        with engine_publication_lock(self.root, timeout_seconds=0):
            response = self.returned(self.writer("preview"))
            self.assertEqual(response["result"], 0)
            self.assertIn("apply=False", response["output"])
        self.assertEqual(self.path.read_bytes(), self.before)

    def test_metadata_apply_is_reentrant_inside_existing_owner(self):
        with engine_publication_lock(self.root, timeout_seconds=0):
            with patch.object(sys, "argv", ["artifact_metadata", str(self.path), "--kind", "atom", "--apply"]):
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(artifact_metadata.main(), 0)
        self.assertIn(b"version: 2\n", self.path.read_bytes())

    def test_metadata_raw_error_is_not_rewritten_or_followed_by_a_write(self):
        invalid = self.before.replace(b"version: 1", b"version: 1\nversion: 2")
        self.path.write_bytes(invalid)
        child = self.writer("apply")
        response = json.loads(read_event(self, child))
        self.assertEqual(response["outcome"], "raised")
        self.assertEqual(response["type"], "RuntimeError")
        self.assertEqual(response["message"], "duplicate version property")
        self.assertEqual(self.path.read_bytes(), invalid)
        child.communicate(timeout=5)
        self.assertEqual(child.returncode, 0)

    def lifecycle_fixture(self):
        fixture = lifecycle_fixtures.SelectedAtomLifecycleTest("test_source_model_status_noop_and_archive_relation_diagnostics")
        fixture.setUp()
        self.addCleanup(fixture.tearDown)
        return fixture

    def test_status_writer_waits_for_shared_owner_before_carrier_effect(self):
        fixture = self.lifecycle_fixture()
        before = fixture.target.read_bytes()
        unrelated = fixture.successor_one.read_bytes()
        with engine_publication_lock(fixture.root, timeout_seconds=0):
            child = self.writer("status", root=fixture.root, path=fixture.target)
            self.assertEqual(read_event(self, child), "contended")
            self.assertEqual(fixture.target.read_bytes(), before)
            self.assertEqual(fixture.successor_one.read_bytes(), unrelated)
        response = self.returned(child)
        self.assertEqual(response["result"]["outcome"], "applied")
        output = fixture.root / response["result"]["observed"]["path"]
        self.assertIn(b"status: Archived\n", output.read_bytes())
        self.assertEqual(fixture.successor_one.read_bytes(), unrelated)

    def test_status_authorization_error_remains_raw_and_effect_free(self):
        fixture = self.lifecycle_fixture()
        before = fixture.target.read_bytes()
        request = {"target": carrier_descriptor(fixture.root, "CA-R-100"), "status": "Archived"}
        with engine_publication_lock(fixture.root, timeout_seconds=0):
            with self.assertRaises(LifecycleError) as refused:
                change_status_atom_action(fixture.root, request, execute=True, authorized=False)
        self.assertEqual(refused.exception.code, "authorization-required")
        self.assertEqual(str(refused.exception), "authorization-required: the caller has not admitted an authorized mutation")
        self.assertEqual(fixture.target.read_bytes(), before)

    def test_default_selected_host_cannot_use_lock_ownership_as_publication_permission(self):
        sys.path.insert(0, str(TOOLS / "ATOM_UPDATE/tests"))
        from test_subject_apply_portfolio import SubjectApplyProject
        from workflow_run_support import RunExecutionSession
        import atom_subject_apply as subject

        root = self.root / "subject"
        root.mkdir()
        fixture = SubjectApplyProject(root)
        runner, frozen = fixture.execution("default-lock-is-not-permission")
        original = subject.subject_update_action
        calls, errors = [], []
        def observe(actual_root, parameters, **kwargs):
            if kwargs.get("execute") is True:
                calls.append(kwargs)
            try:
                return original(actual_root, parameters, **kwargs)
            except LifecycleError as error:
                errors.append(error.code)
                raise
        with engine_publication_lock(root, timeout_seconds=0):
            with patch.object(subject, "subject_update_action", side_effect=observe):
                result = runner.dispatch(frozen)
        self.assertEqual(errors, ["subject-publication-window-unconfirmed"])
        self.assertEqual(len(calls), 1)
        session = calls[0]["session"]
        self.assertIsInstance(session, RunExecutionSession)
        action = session._actual_by_id(calls[0]["action_run_id"])[1]
        self.assertEqual(action["definition"]["atom_id"], "CA-O-030")
        session.read_recorded_action_start(calls[0]["action_run_id"])
        self.assertNotEqual(result.get("outcome"), "completed")
        fixture.assert_unchanged(self)

    def unsafe_lock_carrier(self, root):
        carrier = root / ".caprmedio_runtime/framework/selector-publication.lock"
        carrier.parent.mkdir(parents=True, exist_ok=True)
        unrelated = root / "untouched-lock-target"
        unrelated.write_bytes(b"exact unrelated lock target")
        carrier.symlink_to(unrelated)
        return unrelated

    @staticmethod
    @contextmanager
    def changed_on_lock_exit(root, **kwargs):
        with engine_publication_lock(root, **kwargs):
            yield
        raise EnginePublicationLockError("selector-publication-lock-unsafe", "isolated exit failure after real body")

    def structural_fixture(self):
        from WORKFLOW_OPERATIONS.PROJECT_STRUCTURE import project_structure as structure
        settings = self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        settings.write_text(
            '[project]\nname = "engine-fixture"\n'
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
            '[authority_modes]\ndefault = "casual"\n',
            encoding="utf-8",
        )
        parent = {"scope_unit_name": "PARENT", "parent": "PROJECT", "scope_unit_type": "Ordered",
                  "scope_unit_label": "LAYER", "structural_level": 1, "local_order": 1,
                  "navigational_order_number": 0, "authority_path": ".caprmedio_caprmedio/PARENT",
                  "delivery_path": "delivery/PARENT"}
        toml = self.root / ".caprmedio_caprmedio/project_structure.toml"
        toml.write_text(structure.serialize_project_structure([parent]), encoding="utf-8")
        child = {**parent, "scope_unit_name": "CHILD", "parent": "PARENT", "scope_unit_label": "FEATURE",
                 "structural_level": 2, "authority_path": ".caprmedio_caprmedio/CHILD", "delivery_path": "delivery/CHILD"}
        request = {"operation": "Create", "declaration": child,
                   "expected_toml_revision": hashlib.sha256(toml.read_bytes()).hexdigest(), "reference_frontier": [],
                   "goal_coverage_disposition": {"state": "missing", "parent": "PARENT", "gap_ref": "fixture-gap",
                                                 "authorized_disposition": "report-only"},
                   "preservation_disposition": {"preserved": [self.path.name]},
                   "recovery_disposition": {"authorized": True, "boundary": "toml-and-listed-references"}}
        return structure, toml, request

    def test_structure_unsafe_lock_refuses_in_domain_before_any_effect(self):
        structure, toml, request = self.structural_fixture()
        before = toml.read_bytes()
        unrelated = self.unsafe_lock_carrier(self.root)
        result = structure.apply_scope_unit_action(self.root, request)
        self.assertEqual(result["state"], "conflict")
        self.assertEqual(result["actual_effects"], [])
        self.assertTrue(result["validation_errors"])
        self.assertEqual(toml.read_bytes(), before)
        self.assertEqual(self.path.read_bytes(), self.before)
        self.assertEqual(unrelated.read_bytes(), b"exact unrelated lock target")

    def test_structure_exit_failure_retains_real_effects_as_partial(self):
        structure, toml, request = self.structural_fixture()
        before = toml.read_bytes()
        with patch.object(structure, "engine_publication_lock", self.changed_on_lock_exit):
            result = structure.apply_scope_unit_action(self.root, request)
        after = toml.read_bytes()
        self.assertNotEqual(after, before)
        self.assertIn(b'"CHILD"', after)
        self.assertEqual(result["state"], "partial")
        self.assertEqual(result["actual_effects"], [{"path": ".caprmedio_caprmedio/project_structure.toml",
                                                    "before_sha256": hashlib.sha256(before).hexdigest(),
                                                    "after_sha256": hashlib.sha256(after).hexdigest()}])
        self.assertEqual(result["post_toml_revision"], hashlib.sha256(after).hexdigest())
        self.assertTrue(result["validation_errors"])
        self.assertEqual(self.path.read_bytes(), self.before)

    def test_status_unsafe_lock_refuses_in_native_domain_before_effect(self):
        fixture = self.lifecycle_fixture()
        request = {"target": carrier_descriptor(fixture.root, "CA-R-100"), "status": "Archived"}
        before = fixture.target.read_bytes()
        unrelated = self.unsafe_lock_carrier(fixture.root)
        with self.assertRaises(LifecycleError) as refused:
            change_status_atom_action(fixture.root, request, execute=True, authorized=True)
        self.assertEqual(refused.exception.code, "selector-publication-lock-unavailable")
        self.assertEqual(fixture.target.read_bytes(), before)
        self.assertEqual(unrelated.read_bytes(), b"exact unrelated lock target")

    def test_status_exit_failure_reports_uncertainty_without_erasing_real_body_evidence(self):
        fixture = self.lifecycle_fixture()
        request = {"target": carrier_descriptor(fixture.root, "CA-R-100"), "status": "Archived"}
        before = fixture.target.read_bytes()
        with patch.object(lifecycle_intents, "engine_publication_lock", self.changed_on_lock_exit):
            result = change_status_atom_action(fixture.root, request, execute=True, authorized=True)
        self.assertEqual(result["outcome"], "partial")
        self.assertEqual(result["failure"]["phase"], "lock-exit")
        self.assertEqual(result["failure"]["code"], "selector-publication-lock-unsafe")
        original = result["failure"]["observed_result"]
        self.assertEqual(original["outcome"], "applied")
        self.assertTrue(original["effects"])
        self.assertEqual({effect["state"] for effect in original["effects"]}, {"changed"})
        for field, value in original.items():
            if field not in {"outcome", "observed", "effects", "recovery"}:
                self.assertEqual(result[field], value)
        self.assertEqual(result["observed"]["verification"], "unknown")
        self.assertEqual(len(result["effects"]), len(original["effects"]))
        for effect, observed in zip(result["effects"], original["effects"]):
            self.assertEqual(effect["state"], "unknown")
            self.assertEqual({key: value for key, value in effect.items() if key != "state"},
                             {key: value for key, value in observed.items() if key != "state"})
        output = fixture.root / original["observed"]["path"]
        self.assertNotEqual(output.read_bytes(), before)
        self.assertIn(b"status: Archived\n", output.read_bytes())
        self.assertEqual(result["recovery"]["automatic_retry"], False)


if __name__ == "__main__":
    unittest.main()
