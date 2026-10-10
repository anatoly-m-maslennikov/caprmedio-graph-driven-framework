"""Focused proof for trusted-host Release manifest publication context."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch


MCP = Path(__file__).resolve().parents[1]
REPOSITORY = MCP.parents[2]
APP_TESTS = MCP.parent / "203_APPS/WORKFLOW_ORCHESTRATOR/tests"
PUBLIC_RELEASE = MCP.parent / "201_TOOLS/PUBLIC_RELEASE"
SCHEMA4_INPUT = MCP / "tests/selected_source_refresh_golden/input_manifest.schema4.v1.json"
for location in (MCP, APP_TESTS, PUBLIC_RELEASE):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import release_source_admission as admission_module  # noqa: E402
from release_manifest_authorization import (  # noqa: E402
    PublicationAuthorizationContext,
    ReleaseManifestAuthorizationError,
    _normalize_refresh_plan,
    authorize_operator_publication,
    authorize_operator_publication_recovery,
    authorize_operator_refresh,
    validate_candidate_payload,
    validate_publication_context,
    validate_refresh_context,
)
from release_manifest_lifecycle import ReleaseManifestLifecycle, ReleaseManifestLifecycleError, _normalized_refresh_plan  # noqa: E402
from release_manifest_publisher import (  # noqa: E402
    ReleaseManifestPublishError,
    _candidate,
    plan_release_manifest_publish,
    plan_release_manifest_refresh,
    refresh_release_manifest,
)
from release_source_admission import (  # noqa: E402
    AUTHORITY_REF,
    derive_release_graph_admission,
)
from selected_routes import SELECTED_ROUTE_NAMES, load_selected_manifest, selected_manifest_ref  # noqa: E402
from selected_source_refresh import derive_registered_source_refresh, registered_source_refresh  # noqa: E402
from selected_admission import AUTHORITY_REF as PUBLIC_AUTHORITY_REF  # noqa: E402
from selected_workflows_docker_fixture import GoldenCase, GoldenProject  # noqa: E402


def _paths(value: object) -> set[str]:
    if isinstance(value, dict):
        result = {value["source_path"]} if isinstance(value.get("source_path"), str) else set()
        for child in value.values():
            result |= _paths(child)
        return result
    if isinstance(value, list):
        return set().union(*(_paths(item) for item in value)) if value else set()
    return set()


class ReleaseManifestAuthorizationTest(unittest.TestCase):
    def setUp(self) -> None:
        temporary = REPOSITORY / ".caprmedio_tmp/tests/release-manifest-authorization"
        temporary.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="context-", dir=temporary, ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        # This historical authorization corpus is deliberately the closed
        # fifteen-route predecessor.  Its fixture helper copies every pin that
        # predecessor admits; do not reopen the current Release-only private
        # package inventory while preparing it.
        raw = GoldenProject(REPOSITORY, self.root, GoldenCase("W04", "change_atom_status"))._copy_reviewed_manifest()
        _, admission = derive_release_graph_admission(REPOSITORY)
        manifest_ref = selected_manifest_ref(REPOSITORY)
        source_registry_ref = raw["source_freshness"]["selected_source_registry_ref"]
        operators_registry_ref = ".caprmedio_caprmedio/operators_registry.toml"
        project_settings_ref = ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        project_structure_ref = ".caprmedio_caprmedio/project_structure.toml"
        for relative in _paths(admission) | {
            AUTHORITY_REF, manifest_ref, source_registry_ref, operators_registry_ref, project_settings_ref,
            project_structure_ref,
        }:
            source, target = REPOSITORY / relative, self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists():
                shutil.copyfile(source, target)
        # Preserve the historical authorization contract independently from
        # the current live Operator record.
        (self.root / operators_registry_ref).write_text(
            '[[operators]]\nname = "Anatoly Maslennikov"\nrole = "project owner"\n'
            'journal_author = "anatoly-m"\n',
            encoding="utf-8",
        )
        # The current-source resolver scans both registered Project and TOOLS
        # roots for every RMED role.  The frozen predecessor has no source in
        # every fallback root, but each checked root must still exist.
        for relative in (
            ".caprmedio_caprmedio/09_operations",
            ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
            "205_FEATURE_PROJECT_TOOLS",
            ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
            "201_FEATURE_TOOLS",
        ):
            for role_directory in ("04_requirement", "05_method", "06_evaluation", "07_delivery"):
                (self.root / relative / role_directory).mkdir(parents=True, exist_ok=True)
        self.path = self.root / manifest_ref
        self.before = self.path.read_bytes()
        self.plan = plan_release_manifest_publish(self.root)

    def authorize(self, **overrides: object) -> PublicationAuthorizationContext:
        values: dict[str, object] = {
            "operator_name": "Anatoly Maslennikov",
            "journal_author": "anatoly-m",
            "llm_session": {"app": "codex", "uuid": "fixture-release-manifest"},
            "authorization_ref": "operator_authorization/release_manifest_fixture",
        }
        values.update(overrides)
        return authorize_operator_publication(self.root, self.plan, **values)  # type: ignore[arg-type]

    def assert_refused(self, context: object, *, root: Path | None = None, plan: object | None = None, **kwargs: object) -> None:
        with self.assertRaises(ReleaseManifestAuthorizationError):
            validate_publication_context(
                context, self.root if root is None else root, self.plan if plan is None else plan, **kwargs  # type: ignore[arg-type]
            )

    def test_registered_operator_context_is_fresh_and_opaque(self) -> None:
        context = self.authorize()
        self.assertEqual("Anatoly Maslennikov", context.operator_name)
        self.assertEqual("anatoly-m", context.journal_author)
        self.assertEqual({"app": "codex", "uuid": "fixture-release-manifest"}, dict(context.llm_session))
        self.assertEqual(context, validate_publication_context(context, self.root, self.plan))
        self.assertEqual(self.before, self.path.read_bytes())
        with self.assertRaises(TypeError):
            PublicationAuthorizationContext()
        with self.assertRaises(TypeError):
            context.__reduce__()

    def test_unregistered_operator_and_declared_journal_mapping_refuse(self) -> None:
        with self.assertRaises(ReleaseManifestAuthorizationError):
            self.authorize(operator_name="Unregistered Operator")
        registry = self.root / ".caprmedio_caprmedio/operators_registry.toml"
        registry.write_text(
            '[[operators]]\nname = "Anatoly Maslennikov"\nrole = "project owner"\njournal_author = "another-author"\n',
            encoding="utf-8",
        )
        with self.assertRaises(ReleaseManifestAuthorizationError):
            self.authorize()
        self.assertEqual(self.before, self.path.read_bytes())

    def test_stale_input_bytes_and_source_refuse_without_publication(self) -> None:
        context = self.authorize()
        self.path.write_bytes(self.before + b"\n")
        self.assert_refused(context)
        self.path.write_bytes(self.before)
        _, admission = derive_release_graph_admission(self.root)
        source = self.root / admission["workflow"]["source_path"]
        source.write_bytes(source.read_bytes() + b"\nstale\n")
        self.assert_refused(context)
        self.assertEqual(self.before, self.path.read_bytes())

    def test_root_plan_dict_callback_and_forged_or_altered_context_refuse(self) -> None:
        context = self.authorize()
        other = Path(tempfile.mkdtemp(prefix="other-release-root-", dir=self.root.parent))
        self.addCleanup(shutil.rmtree, other, ignore_errors=True)
        self.assert_refused(context, root=other)
        changed = dict(self.plan)
        changed["candidate_byte_count"] += 1
        self.assert_refused(context, plan=changed)
        self.assert_refused({"authorization": "remote-json"})
        self.assert_refused(lambda: True)
        forged = object.__new__(PublicationAuthorizationContext)
        self.assert_refused(forged)
        object.__setattr__(context, "_operator_name", "Altered Operator")
        self.assert_refused(context)
        self.assertEqual(self.before, self.path.read_bytes())

    def test_candidate_readback_requires_the_exact_sealed_candidate(self) -> None:
        context = self.authorize()
        _, _, payload, _ = _candidate(self.root)
        self.path.write_bytes(payload)
        self.assertEqual(context, validate_publication_context(context, self.root, self.plan, manifest_state="candidate"))
        self.path.write_bytes(payload + b"\n")
        self.assert_refused(context, manifest_state="candidate")

    def test_normal_context_seals_candidate_payload_without_disclosing_its_digest(self) -> None:
        context = self.authorize()
        _, _, payload, _ = _candidate(self.root)
        self.assertIsNone(validate_candidate_payload(context, self.root, self.plan, payload))
        with self.assertRaises(ReleaseManifestAuthorizationError):
            validate_candidate_payload(context, self.root, self.plan, payload + b"\n")
        self.assertEqual(self.before, self.path.read_bytes())

    def _seal_existing_candidate(self) -> tuple[str, bytes]:
        context = self.authorize()
        lifecycle = ReleaseManifestLifecycle(self.root, context)
        _, _, payload, _ = _candidate(self.root)
        lifecycle_plan = {key: value for key, value in self.plan.items() if key != "mode"}
        with patch("release_manifest_lifecycle.subprocess.run") as git:
            git.return_value.returncode, git.return_value.stdout = 0, "a" * 40 + "\n"
            event_id = lifecycle.prepare_release_manifest_publication(lifecycle_plan, payload)
        self.path.write_bytes(payload)
        return event_id, payload

    def test_cold_restart_reissues_finalization_only_context_from_sealed_pending_evidence(self) -> None:
        event_id, payload = self._seal_existing_candidate()
        import release_manifest_authorization as authorization
        authorization._issued.clear()
        recovery = authorize_operator_publication_recovery(
            self.root, event_id, operator_name="Anatoly Maslennikov", journal_author="anatoly-m",
            llm_session={"app": "codex", "uuid": "fixture-release-manifest"},
            authorization_ref="operator_authorization/release_manifest_recovery_fixture",
        )
        self.assertEqual(
            recovery,
            validate_publication_context(recovery, self.root, self.plan, manifest_state="candidate"),
        )
        with self.assertRaises(ReleaseManifestAuthorizationError):
            validate_publication_context(recovery, self.root, self.plan)
        with self.assertRaises(ReleaseManifestAuthorizationError):
            validate_candidate_payload(recovery, self.root, self.plan, payload)
        recovered = ReleaseManifestLifecycle(self.root, recovery).recover_release_manifest_publication(event_id)
        self.assertEqual("recovered", recovered["disposition"])
        self.assertEqual(payload, self.path.read_bytes())

    def test_recovery_refuses_changed_target_source_or_actor_binding(self) -> None:
        event_id, payload = self._seal_existing_candidate()
        self.path.write_bytes(payload + b"\n")
        with self.assertRaises(ReleaseManifestAuthorizationError):
            authorize_operator_publication_recovery(
                self.root, event_id, operator_name="Anatoly Maslennikov", journal_author="anatoly-m",
                llm_session={"app": "codex", "uuid": "fixture-release-manifest"},
                authorization_ref="operator_authorization/release_manifest_recovery_fixture",
            )
        self.path.write_bytes(payload)
        with self.assertRaises(ReleaseManifestAuthorizationError):
            authorize_operator_publication_recovery(
                self.root, event_id, operator_name="Anatoly Maslennikov", journal_author="other-author",
                llm_session={"app": "codex", "uuid": "fixture-release-manifest"},
                authorization_ref="operator_authorization/release_manifest_recovery_fixture",
            )
        _, admission = derive_release_graph_admission(self.root)
        source = self.root / admission["workflow"]["source_path"]
        source.write_bytes(source.read_bytes() + b"\nstale\n")
        with self.assertRaises(ReleaseManifestAuthorizationError):
            authorize_operator_publication_recovery(
                self.root, event_id, operator_name="Anatoly Maslennikov", journal_author="anatoly-m",
                llm_session={"app": "codex", "uuid": "fixture-release-manifest"},
                authorization_ref="operator_authorization/release_manifest_recovery_fixture",
            )

    def test_plan_or_context_from_another_source_frontier_refuses(self) -> None:
        context = self.authorize()
        authority = self.root / AUTHORITY_REF
        authority.write_bytes(authority.read_bytes() + b"\nsource changed\n")
        self.assert_refused(context)
        self.assertEqual(self.before, self.path.read_bytes())
        self.assertEqual(self.plan["observed_input_sha256"], hashlib.sha256(self.before).hexdigest())


class O030RefreshPlanShapeTest(unittest.TestCase):
    """The 17-route repair remains an exact schema-4 branch, never a count range."""

    def setUp(self) -> None:
        self.root = REPOSITORY
        self.names16 = [*SELECTED_ROUTE_NAMES, "release_version"]
        self.names17 = [*self.names16, "public.release"]

    def _plan(self, names: list[str], **overrides: object) -> dict[str, object]:
        plan: dict[str, object] = {
            "publication_operation": "refresh",
            "manifest_ref": selected_manifest_ref(self.root),
            "observed_input_sha256": "a" * 64,
            "current_route_names": list(names),
            "candidate_route_names": list(names),
            "candidate_canonical_manifest_sha256": "b" * 64,
            "added_route": "release_version",
            "added_admission_route": "release_version",
            "candidate_byte_count": 1,
        }
        plan.update(overrides)
        return plan

    @staticmethod
    def _normalized(plan: dict[str, object]) -> dict[str, object]:
        return {
            **plan,
            "current_route_names": tuple(plan["current_route_names"]),
            "candidate_route_names": tuple(plan["candidate_route_names"]),
        }

    def test_historical_sixteen_route_refresh_remains_exact(self) -> None:
        plan = self._plan(self.names16)
        expected = self._normalized(plan)
        self.assertEqual(expected, _normalize_refresh_plan(plan, self.root))
        self.assertEqual(plan, _normalized_refresh_plan(plan))

    def test_o030_seventeen_route_refresh_requires_exact_schema4_registration_metadata(self) -> None:
        incomplete = self._plan(self.names17)
        with self.assertRaises(ReleaseManifestAuthorizationError):
            _normalize_refresh_plan(incomplete, self.root)
        with self.assertRaises(ReleaseManifestLifecycleError):
            _normalized_refresh_plan(incomplete)

        plan = self._plan(
            self.names17,
            source_refresh_schema_version=4,
            source_refresh_registration_id="o030-v6-three-pin-repair",
        )
        expected = self._normalized(plan)
        self.assertEqual(expected, _normalize_refresh_plan(plan, self.root))
        self.assertEqual(plan, _normalized_refresh_plan(plan))

    def test_o030_branch_rejects_count_route_and_metadata_broadening(self) -> None:
        valid = self._plan(
            self.names17,
            source_refresh_schema_version=4,
            source_refresh_registration_id="o030-v6-three-pin-repair",
        )
        variants = (
            {**valid, "candidate_route_names": [*self.names17, "O199"]},
            {**valid, "current_route_names": [*self.names16, "O199"]},
            {**valid, "source_refresh_schema_version": 5},
            {**valid, "source_refresh_schema_version": 4.0},
            {**valid, "source_refresh_schema_version": True},
            {**self._plan(self.names16), "source_refresh_schema_version": 4,
             "source_refresh_registration_id": "o030-v6-three-pin-repair"},
        )
        for plan in variants:
            with self.subTest(plan=plan):
                with self.assertRaises(ReleaseManifestAuthorizationError):
                    _normalize_refresh_plan(plan, self.root)
                with self.assertRaises(ReleaseManifestLifecycleError):
                    _normalized_refresh_plan(plan)


class O030TrustedRefreshEndToEndTest(unittest.TestCase):
    """Run D588's exact schema-4 repair through the trusted lifecycle in isolation."""

    _REGISTRATION_REF = (
        ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
        "204_FEATURE_MCP/07_delivery/CA-D-588-MCP-DELIVERY--register-the-prepared-successor-binding-refresh.md"
    )

    def setUp(self) -> None:
        temporary = REPOSITORY / ".caprmedio_tmp/tests/o030-trusted-refresh"
        temporary.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temporary, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.registration = registered_source_refresh(REPOSITORY)
        self.manifest_ref = selected_manifest_ref(REPOSITORY)
        self.before = SCHEMA4_INPUT.read_bytes()
        self.input_manifest = json.loads(self.before)
        self.assertEqual(4, self.registration["schema_version"])
        self.assertEqual(17, len(self.input_manifest["routes"]))
        self.assertEqual(
            self.registration["input_manifest_sha256"], hashlib.sha256(self.before).hexdigest(),
        )
        for source_root in (*admission_module._RMED_ROOTS.values(), *admission_module._TOOLS_RMED_ROOTS.values()):
            (self.root / source_root).mkdir(parents=True, exist_ok=True)
        target = self.root / self.manifest_ref
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(self.before)
        for source_path in _paths(self.input_manifest):
            self._copy(source_path)
        for replacement in self.registration["replacements"]:
            self._copy(replacement["current_pin"]["source_path"])
            if "prior_archive_path" in replacement:
                self._copy(replacement["prior_archive_path"])
            if "prior_receipt_ref" in replacement:
                self._copy(replacement["prior_receipt_ref"])
        for relative in (
            self._REGISTRATION_REF,
            self.input_manifest["source_freshness"]["selected_source_registry_ref"],
            ".caprmedio_caprmedio/caprmedio_project_settings.toml",
            ".caprmedio_caprmedio/project_structure.toml",
            ".caprmedio_caprmedio/operators_registry.toml",
            AUTHORITY_REF,
        ):
            self._copy(relative)
        self._copy(PUBLIC_AUTHORITY_REF)
        self.path = self.root / self.manifest_ref

    def _copy(self, relative: object) -> None:
        self.assertIsInstance(relative, str)
        source, target = REPOSITORY / relative, self.root / relative
        self.assertTrue(source.is_file(), relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            shutil.copy2(source, target)

    def _authorize(self, plan: dict[str, object]) -> PublicationAuthorizationContext:
        return authorize_operator_refresh(
            self.root,
            plan,
            operator_name="Anatoly Maslennikov",
            journal_author="anatoly-m-maslennikov",
            llm_session={"app": "codex", "uuid": "o030-trusted-refresh-fixture"},
            authorization_ref=self.registration["authorization_ref"],
        )

    @staticmethod
    def _git_evidence() -> object:
        return patch(
            "release_manifest_lifecycle.subprocess.run",
            return_value=type("GitEvidence", (), {"returncode": 0, "stdout": "a" * 40 + "\n"})(),
        )

    def _assert_unchanged(self, expected: bytes) -> None:
        self.assertEqual(expected, self.path.read_bytes())

    def test_exact_authorize_execute_strict_readback_and_journal_finalization(self) -> None:
        expected_current, expected_candidate, expected_payload, _ = derive_registered_source_refresh(self.root)
        plan = plan_release_manifest_refresh(self.root)
        self.assertEqual("plan", plan["mode"])
        self.assertEqual("refresh", plan["publication_operation"])
        self.assertEqual(4, plan["source_refresh_schema_version"])
        self.assertEqual(self.registration["registration_id"], plan["source_refresh_registration_id"])
        self.assertEqual([*SELECTED_ROUTE_NAMES, "release_version", "public.release"], plan["current_route_names"])
        self.assertEqual(plan["current_route_names"], plan["candidate_route_names"])
        context = self._authorize(plan)
        self.assertIs(context, validate_refresh_context(context, self.root, plan))

        forged = object.__new__(PublicationAuthorizationContext)
        with self.assertRaises(ReleaseManifestPublishError):
            refresh_release_manifest(self.root, execute=True, authorization=forged)
        self._assert_unchanged(self.before)

        o030_source = self.root / self.registration["replacements"][0]["current_pin"]["source_path"]
        source_before = o030_source.read_bytes()
        o030_source.write_bytes(source_before + b"\nsource drift\n")
        with self.assertRaises(ReleaseManifestPublishError):
            refresh_release_manifest(self.root, execute=True, authorization=context)
        self._assert_unchanged(self.before)
        o030_source.write_bytes(source_before)

        input_drift = self.before + b"\ninput drift\n"
        self.path.write_bytes(input_drift)
        with self.assertRaises(ReleaseManifestPublishError):
            refresh_release_manifest(self.root, execute=True, authorization=context)
        self._assert_unchanged(input_drift)
        self.path.write_bytes(self.before)

        with self._git_evidence():
            result = refresh_release_manifest(self.root, execute=True, authorization=context)
        self.assertEqual("published", result["disposition"], result)
        self.assertTrue(result["recording_ref"].startswith("journal:release-manifest:"))
        self.assertEqual(expected_payload, self.path.read_bytes())
        loaded = load_selected_manifest(self.root)
        self.assertEqual(expected_candidate, {key: value for key, value in loaded.items() if key != "manifest_ref"})
        self.assertEqual(expected_current["routes"][:1], loaded["routes"][:1])
        self.assertEqual(expected_current["routes"][2:], loaded["routes"][2:])
        self.assertEqual(
            self.registration["replacements"][0]["current_pin"],
            loaded["routes"][1]["native_action_calls"][0],
        )
        self.assertEqual(
            self.registration["replacements"][1]["current_pin"],
            loaded["release_source_admissions"][0]["rmed_frontier"][11],
        )
        self.assertEqual(
            self.registration["replacements"][2]["current_pin"],
            loaded["release_source_admissions"][0]["rmed_frontier"][31],
        )
        self.assertEqual(self.input_manifest["query_source_admissions"], loaded["query_source_admissions"])
        self.assertEqual(
            self.input_manifest["public_release_source_admissions"], loaded["public_release_source_admissions"],
        )
        pending = self.root / ".caprmedio_runtime/state/work_journal/pending"
        self.assertEqual([], list(pending.glob("release-manifest:*.json")) if pending.exists() else [])

        published = self.path.read_bytes()
        with self.assertRaises(ReleaseManifestPublishError):
            refresh_release_manifest(self.root, execute=True, authorization=context)
        self._assert_unchanged(published)

    def test_schema4_recording_failure_finalizes_the_same_event_without_replay(self) -> None:
        plan = plan_release_manifest_refresh(self.root)
        context = self._authorize(plan)
        with self._git_evidence(), patch.object(
            ReleaseManifestLifecycle,
            "record_release_manifest_publication",
            side_effect=RuntimeError("injected final recording failure"),
        ):
            result = refresh_release_manifest(self.root, execute=True, authorization=context)
        self.assertEqual("recording_required", result["disposition"], result)
        pending_root = self.root / ".caprmedio_runtime/state/work_journal/pending"
        pending = sorted(path.stem for path in pending_root.glob("release-manifest:*.json"))
        self.assertEqual(1, len(pending))
        published = self.path.read_bytes()
        with patch(
            "release_manifest_publisher._atomic_write",
            side_effect=AssertionError("recording finalization rewrote the manifest"),
        ):
            recovered = ReleaseManifestLifecycle(self.root, context).recover_release_manifest_publication(pending[0])
        self.assertEqual("recovered", recovered["disposition"])
        self.assertEqual(pending[0], recovered["event_id"])
        self.assertEqual(published, self.path.read_bytes())
        self.assertEqual([], list(pending_root.glob("release-manifest:*.json")))


if __name__ == "__main__":
    unittest.main()
