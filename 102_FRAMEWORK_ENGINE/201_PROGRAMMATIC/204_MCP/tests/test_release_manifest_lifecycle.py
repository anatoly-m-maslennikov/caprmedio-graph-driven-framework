"""Focused retained-fixture proof for the Release publication lifecycle."""

from __future__ import annotations

from pathlib import Path
import shutil
import sys
import unittest
from unittest.mock import patch


MCP = Path(__file__).resolve().parents[1]
REPOSITORY = MCP.parents[2]
APP_TESTS = MCP.parent / "203_APPS/WORKFLOW_ORCHESTRATOR/tests"
for location in (MCP, MCP / "tests", APP_TESTS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import test_release_source_admission as source_goldens  # noqa: E402
from release_manifest_authorization import authorize_operator_publication  # noqa: E402
from release_manifest_lifecycle import ReleaseManifestLifecycle, ReleaseManifestLifecycleError  # noqa: E402
from release_manifest_publisher import _candidate, plan_release_manifest_publish  # noqa: E402
from selected_routes import selected_manifest_ref  # noqa: E402
from selected_workflows_docker_fixture import GoldenCase, GoldenProject  # noqa: E402
import work_journal  # noqa: E402


class ReleaseManifestLifecycleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        source_goldens.ReleaseSourceAdmissionTest.setUpClass()

    def setUp(self) -> None:
        self.fixture = source_goldens.ReleaseSourceAdmissionTest()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        project = GoldenProject(REPOSITORY, self.root, GoldenCase("W04", "change_atom_status"))
        project._copy_reviewed_manifest()
        for relative in (
            Path(".caprmedio_caprmedio/operators_registry.toml"),
            Path(".caprmedio_caprmedio/caprmedio_project_settings.toml"),
        ):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPOSITORY / relative, target)
        self.path = self.root / selected_manifest_ref(self.root)
        self.before = self.path.read_bytes()
        self.plan = plan_release_manifest_publish(self.root)
        self.assertEqual("plan", self.plan.pop("mode"))
        _, _, self.payload, _ = _candidate(self.root)
        context = authorize_operator_publication(
            self.root,
            self.plan,
            operator_name="Anatoly Maslennikov",
            journal_author="anatoly-m-maslennikov",
            llm_session={"app": "test", "uuid": "release-lifecycle"},
            authorization_ref="authorization/release-manifest.md",
        )
        self.lifecycle = ReleaseManifestLifecycle(self.root, context)

    def test_authorization_and_prepare_change_no_carrier_or_journal(self) -> None:
        self.assertTrue(
            self.lifecycle.authorize_release_manifest_publication(self.plan, self.lifecycle.context)
        )
        event_id = self.lifecycle.prepare_release_manifest_publication(self.plan, self.payload)
        self.assertTrue(event_id.startswith("release-manifest:"))
        self.assertEqual(self.before, self.path.read_bytes())
        self.assertEqual([], work_journal.read_records(self.root))

    def test_exact_published_observation_appends_without_baseline_or_dedup(self) -> None:
        event_id = self.lifecycle.prepare_release_manifest_publication(self.plan, self.payload)
        self.path.write_bytes(self.payload)
        result = {"mode": "execute", "published": True, **self.plan}
        first = self.lifecycle.record_release_manifest_publication(result)
        second = self.lifecycle.record_release_manifest_publication(result)
        self.assertEqual("journal:" + event_id, first["recording_ref"])
        self.assertEqual(first, second)
        records = work_journal.read_records(self.root)
        self.assertEqual(2, len(records))
        self.assertEqual(["completed", "completed"], [record["event"] for record in records])
        self.assertTrue(all("previous_result_event" not in record for record in records))
        self.assertEqual(self.plan["manifest_ref"], records[0]["result"]["path"])

    def test_append_failure_reports_logging_error_without_pending_recovery(self) -> None:
        self.lifecycle.prepare_release_manifest_publication(self.plan, self.payload)
        self.path.write_bytes(self.payload)
        with patch(
            "release_manifest_lifecycle.work_journal.append_sealed_events",
            side_effect=OSError("fixture append failed"),
        ):
            result = self.lifecycle.record_release_manifest_publication(
                {"mode": "execute", "published": True, **self.plan}
            )
        self.assertIn("fixture append failed", result["recording_error"])
        self.assertEqual(self.payload, self.path.read_bytes())
        self.assertFalse((self.root / ".caprmedio_runtime/state/work_journal/pending").exists())

    def test_arbitrary_history_does_not_gate_source_prepare(self) -> None:
        journal = self.root / ".caprmedio_caprmedio/_journal/arbitrary.ndjson"
        journal.parent.mkdir(parents=True, exist_ok=True)
        journal.write_text(
            'null\nnot-json\n{"result":{"path":"' + self.plan["manifest_ref"] + '"}}\n',
            encoding="utf-8",
        )
        before = journal.read_bytes()
        self.assertTrue(
            self.lifecycle.prepare_release_manifest_publication(self.plan, self.payload)
        )
        self.assertEqual(before, journal.read_bytes())
        self.assertEqual(self.before, self.path.read_bytes())

    def test_non_context_authority_is_refused(self) -> None:
        self.assertFalse(self.lifecycle.authorize_release_manifest_publication(self.plan, True))
        self.assertFalse(
            self.lifecycle.authorize_release_manifest_publication(
                {"bad": "plan"}, self.lifecycle.context
            )
        )

    def test_lifecycle_owned_effect_lock_is_not_reentrant(self) -> None:
        with self.lifecycle.release_manifest_publication_lock(self.plan):
            with self.assertRaisesRegex(ReleaseManifestLifecycleError, "already held"):
                with self.lifecycle.release_manifest_publication_lock(self.plan):
                    pass

    def test_effect_lock_preserves_failure_and_has_no_bypass_flag(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "publisher body failed"):
            with self.lifecycle.release_manifest_publication_lock(self.plan):
                raise RuntimeError("publisher body failed")
        with self.assertRaises(TypeError):
            self.lifecycle.prepare_release_manifest_publication(
                self.plan, self.payload, publication_lock_held=True
            )


if __name__ == "__main__":
    unittest.main()
