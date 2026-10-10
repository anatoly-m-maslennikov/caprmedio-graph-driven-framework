"""Focused public 16-to-17 manifest publisher coverage.

The fixture copies source authority and never changes the Project's real D572
or D613 carriers.  Its Done status is local and scoped to the positive tests.
"""
from __future__ import annotations

from contextlib import contextmanager
import hashlib
import importlib
from pathlib import Path
import shutil
import sys
import types
import unittest
from unittest.mock import patch


MCP = Path(__file__).resolve().parents[1]
REPOSITORY = MCP.parents[2]
PUBLIC_RELEASE = MCP.parent / "201_TOOLS/PUBLIC_RELEASE"
TOOLS = MCP.parent / "201_TOOLS"
APP_TESTS = MCP.parent / "203_APPS/WORKFLOW_ORCHESTRATOR/tests"
for location in (MCP, MCP / "tests", TOOLS, PUBLIC_RELEASE, APP_TESTS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import selected_admission as public_admission  # noqa: E402
from public_manifest_publisher import (  # noqa: E402
    PublicManifestPublishError,
    plan_public_manifest_publish,
    publish_public_manifest,
    recover_public_manifest_publish,
)
from release_manifest_authorization import (  # noqa: E402
    PublicationAuthorizationContext,
    authorize_operator_public_manifest_publication,
    authorize_operator_public_manifest_recovery,
)
import release_source_admission  # noqa: E402
from selected_routes import load_selected_manifest, selected_manifest_ref  # noqa: E402
import work_journal  # noqa: E402


class PublicManifestPublisherTest(unittest.TestCase):
    def setUp(self) -> None:
        # Reuse the existing copied/resealed D572 fixture rather than changing
        # either source authority or the published fifteen/sixteen projection.
        source_goldens = importlib.import_module("test_release_source_admission")
        authority = REPOSITORY / source_goldens.AUTHORITY_REF
        self.assertEqual(source_goldens.AUTHORITY_REF, release_source_admission.AUTHORITY_PIN["source_path"])
        self.assertEqual(release_source_admission.AUTHORITY_PIN["digest"], hashlib.sha256(authority.read_bytes()).hexdigest())
        source_goldens.AUTHORITY_SHA = release_source_admission.AUTHORITY_PIN["digest"]
        source_goldens.ReleaseSourceAdmissionTest.setUpClass()
        fixture_type = importlib.import_module("test_release_manifest_admission").ReleaseManifestAdmissionTest
        self.fixture = fixture_type()
        self.fixture.setUpClass()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.save(self.fixture.successor())
        self.fixture._copy_public_release_sources()
        self.root = self.fixture.root
        for relative in (
            Path(".caprmedio_caprmedio/operators_registry.toml"),
            Path(".caprmedio_caprmedio/caprmedio_project_settings.toml"),
        ):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPOSITORY / relative, target)
        self.path = self.root / selected_manifest_ref(self.root)
        self.before = self.path.read_bytes()

    @contextmanager
    def _local_d613_authority(self):
        """Expose copied current D613 bytes without changing their Active status."""
        authority = self.root / public_admission.AUTHORITY_REF
        local_pin = {
            **public_admission.AUTHORITY_PIN,
            "digest": hashlib.sha256(authority.read_bytes()).hexdigest(),
        }
        with patch.object(public_admission, "AUTHORITY_PIN", local_pin):
            yield

    def _authorization(self) -> PublicationAuthorizationContext:
        return authorize_operator_public_manifest_publication(
            self.root, plan_public_manifest_publish(self.root),
            operator_name="Anatoly Maslennikov",
            journal_author="anatoly-m-maslennikov",
            llm_session={"app": "test", "uuid": "public-manifest-publisher"},
            authorization_ref="authorization/public-manifest-publisher.md",
        )

    def _recovery_authorization(self, pending_event_id: str) -> PublicationAuthorizationContext:
        return authorize_operator_public_manifest_recovery(
            self.root, pending_event_id,
            operator_name="Anatoly Maslennikov",
            journal_author="anatoly-m-maslennikov",
            llm_session={"app": "test", "uuid": "public-manifest-publisher"},
            authorization_ref="authorization/public-manifest-publisher-recovery.md",
        )

    def _pending_ids(self) -> list[str]:
        pending = self.root / ".caprmedio_runtime/state/work_journal/pending"
        return sorted(path.stem for path in pending.glob("release-manifest:*.json")) if pending.exists() else []

    def test_active_acceptance_refuses_before_any_plan_or_manifest_effect(self) -> None:
        with self._local_d613_authority():
            with self.assertRaisesRegex(PublicManifestPublishError, "public Release source admission is not current"):
                plan_public_manifest_publish(self.root)
        self.assertEqual(self.before, self.path.read_bytes())

    def test_done_fixture_plan_is_read_only_and_exactly_adds_public_release(self) -> None:
        with self.fixture._locally_completed_d613():
            plan = plan_public_manifest_publish(self.root)
        self.assertEqual("plan", plan["mode"])
        self.assertEqual("public", plan["publication_operation"])
        self.assertEqual([*plan["current_route_names"], "public.release"], plan["candidate_route_names"])
        self.assertEqual(self.before, self.path.read_bytes())

    def test_execute_requires_host_capability_then_publishes_and_records_exact_successor(self) -> None:
        with self.fixture._locally_completed_d613():
            with self.assertRaises(PublicManifestPublishError):
                publish_public_manifest(self.root, execute=True, authorization={"authorized": True})
            with patch(
                "release_manifest_lifecycle.subprocess.run",
                return_value=types.SimpleNamespace(returncode=1, stdout=""),
            ):
                result = publish_public_manifest(self.root, execute=True, authorization=self._authorization())
            loaded = load_selected_manifest(self.root)
        self.assertEqual("published", result["disposition"])
        self.assertTrue(result["recording_ref"].startswith("journal:release-manifest:"))
        self.assertEqual(
            [*result["current_route_names"], "public.release"],
            [row["route"] for row in loaded["routes"]],
        )
        self.assertEqual(1, len(loaded["public_release_source_admissions"]))

    def test_source_change_after_opaque_authorization_refuses_before_write(self) -> None:
        with self.fixture._locally_completed_d613():
            context = self._authorization()
            record = public_admission.derive_public_release_source_admission(self.root)
            source = self.root / record["workflow"]["source_path"]
            source.write_bytes(source.read_bytes() + b"\nstale\n")
            with self.assertRaises(PublicManifestPublishError):
                publish_public_manifest(self.root, execute=True, authorization=context)
        self.assertEqual(self.before, self.path.read_bytes())

    def test_finalization_failure_recovers_public_receipt_without_replacing_manifest_again(self) -> None:
        with self.fixture._locally_completed_d613():
            original_context = self._authorization()
            other_prewrite_context = authorize_operator_public_manifest_publication(
                self.root, plan_public_manifest_publish(self.root),
                operator_name="Anatoly Maslennikov",
                journal_author="anatoly-m-maslennikov",
                llm_session={"app": "test", "uuid": "different-prewrite-publication-session"},
                authorization_ref="authorization/other-public-manifest-publisher.md",
            )
            original_append = work_journal.append_sealed_events
            calls = 0

            def fail_final_append(*args: object, **kwargs: object):
                nonlocal calls
                calls += 1
                if calls == 2:
                    raise work_journal.WorkJournalError("injected", "final append failure")
                return original_append(*args, **kwargs)

            with patch(
                "release_manifest_lifecycle.subprocess.run",
                return_value=types.SimpleNamespace(returncode=1, stdout=""),
            ), patch(
                "release_manifest_lifecycle.work_journal.append_sealed_events", side_effect=fail_final_append,
            ):
                result = publish_public_manifest(self.root, execute=True, authorization=original_context)
            self.assertEqual("recording_required", result["disposition"], result)
            pending = self._pending_ids()
            self.assertEqual(1, len(pending))
            before_recovery = self.path.read_bytes()
            wrong_context = recover_public_manifest_publish(
                self.root, pending_event_id=pending[0], authorization=other_prewrite_context,
            )
            self.assertEqual("recording_required", wrong_context["disposition"])
            recovery_context = self._recovery_authorization(pending[0])
            wrong_pending = recover_public_manifest_publish(
                self.root, pending_event_id="release-manifest:" + "0" * 64, authorization=recovery_context,
            )
            self.assertEqual("recording_required", wrong_pending["disposition"])
            self.assertEqual(before_recovery, self.path.read_bytes())
            self.assertEqual(pending, self._pending_ids())
            recovered = recover_public_manifest_publish(
                self.root, pending_event_id=pending[0], authorization=recovery_context,
            )
        self.assertEqual("recovered", recovered["disposition"])
        self.assertEqual(before_recovery, self.path.read_bytes())
        self.assertEqual([], self._pending_ids())


if __name__ == "__main__":
    unittest.main()
