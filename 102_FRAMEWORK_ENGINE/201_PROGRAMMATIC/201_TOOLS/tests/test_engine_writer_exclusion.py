"""Alternate writer errors, previews and authorization use disposable Projects."""

from __future__ import annotations

from contextlib import redirect_stdout
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import artifact_metadata  # noqa: E402
from lifecycle_intents import LifecycleError, carrier_descriptor, change_status_atom_action  # noqa: E402
import test_selected_atom_lifecycle as lifecycle_fixtures  # noqa: E402


class AlternateWriterBehaviorTests(unittest.TestCase):
    def setUp(self):
        scratch = TOOLS.parents[2] / ".caprmedio_tmp" / "tests"
        scratch.mkdir(parents=True, exist_ok=True)
        self.fixture = tempfile.TemporaryDirectory(prefix="alternate-writers-", dir=scratch)
        self.addCleanup(self.fixture.cleanup)
        self.root = Path(self.fixture.name)
        settings = self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        settings.parent.mkdir()
        settings.write_text('[artifact_timestamps]\ntimezone = "UTC"\n', encoding="utf-8")
        self.path = self.root / "CA-R-42--fixture.md"
        self.before = b'---\natom_id: CA-R-42\nversion: 1\nupdated_at: "2026-01-01 00:00:00 +0000"\n---\nExact initial body\n'
        self.path.write_bytes(self.before)
        self.assertEqual(artifact_metadata.repository_root(self.path), self.root)

    def metadata(self, *, apply):
        argv = ["artifact_metadata", str(self.path), "--kind", "atom"]
        if apply:
            argv.append("--apply")
        output = io.StringIO()
        with patch.object(sys, "argv", argv), redirect_stdout(output):
            result = artifact_metadata.main()
        return result, output.getvalue()

    def test_metadata_preview_does_not_write(self):
        result, output = self.metadata(apply=False)
        self.assertEqual(result, 0)
        self.assertIn("apply=False", output)
        self.assertEqual(self.path.read_bytes(), self.before)

    def test_metadata_apply_updates_revision(self):
        result, _ = self.metadata(apply=True)
        self.assertEqual(result, 0)
        self.assertIn(b"version: 2\n", self.path.read_bytes())

    def test_metadata_raw_error_is_not_rewritten_or_followed_by_a_write(self):
        invalid = self.before.replace(b"version: 1", b"version: 1\nversion: 2")
        self.path.write_bytes(invalid)
        with self.assertRaisesRegex(RuntimeError, "^duplicate version property$"):
            self.metadata(apply=True)
        self.assertEqual(self.path.read_bytes(), invalid)

    def lifecycle_fixture(self):
        fixture = lifecycle_fixtures.SelectedAtomLifecycleTest(
            "test_source_model_status_noop_and_archive_relation_diagnostics"
        )
        fixture.setUp()
        self.addCleanup(fixture.tearDown)
        return fixture

    def test_status_authorization_error_remains_raw_and_effect_free(self):
        fixture = self.lifecycle_fixture()
        before = fixture.target.read_bytes()
        request = {"target": carrier_descriptor(fixture.root, "CA-R-100"), "status": "Archived"}
        with self.assertRaises(LifecycleError) as refused:
            change_status_atom_action(fixture.root, request, execute=True, authorized=False)
        self.assertEqual(refused.exception.code, "authorization-required")
        self.assertEqual(
            str(refused.exception),
            "authorization-required: the caller has not admitted an authorized mutation",
        )
        self.assertEqual(fixture.target.read_bytes(), before)

    def test_default_selected_host_requires_publication_permission(self):
        sys.path.insert(0, str(TOOLS / "ATOM_UPDATE/tests"))
        from test_subject_apply_portfolio import SubjectApplyProject
        from workflow_run_support import RunExecutionSession
        import atom_subject_apply as subject

        root = self.root / "subject"
        root.mkdir()
        fixture = SubjectApplyProject(root)
        runner, frozen = fixture.execution("default-publication-permission-required")
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


if __name__ == "__main__":
    unittest.main()
