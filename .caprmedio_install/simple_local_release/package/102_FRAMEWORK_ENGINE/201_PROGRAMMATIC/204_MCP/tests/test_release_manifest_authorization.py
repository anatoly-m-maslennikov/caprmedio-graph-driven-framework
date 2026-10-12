"""Focused proof for trusted-host Release manifest publication context."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path, PurePosixPath
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
SCHEMA5_INPUT_SHA256 = "6d1e3aaacf33d4c3cb645f9ed46641dac38b6480773a080074bac51249c143f4"
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
from selected_source_refresh import (  # noqa: E402
    _EXPECTED_V4,
    derive_registered_source_refresh,
    derive_registered_source_successor,
    registered_source_refresh,
)
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


def _frozen_schema5_input() -> bytes:
    """Reconstruct the sealed schema-5 predecessor from frozen schema-4 bytes."""
    schema4_input = json.loads(SCHEMA4_INPUT.read_bytes())
    schema5_input = derive_registered_source_successor(schema4_input, _EXPECTED_V4)
    payload = (
        json.dumps(schema5_input, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode("utf-8")
    if hashlib.sha256(payload).hexdigest() != SCHEMA5_INPUT_SHA256:
        raise AssertionError("frozen schema-5 fixture reconstruction digest differs")
    return payload


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
    """The 17-route repair admits only its closed schema-4 or schema-5 branch."""

    _SCHEMA4_REGISTRATION_ID = "epic1848-exact-three-pin-binding-repair-20261011"
    _SCHEMA5_REGISTRATION_ID = "epic1848-exact-o030-v7-binding-repair-20261011"

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

    def test_o030_seventeen_route_refresh_requires_closed_schema4_or_schema5_registration_metadata(self) -> None:
        incomplete = self._plan(self.names17)
        with self.assertRaises(ReleaseManifestAuthorizationError):
            _normalize_refresh_plan(incomplete, self.root)
        with self.assertRaises(ReleaseManifestLifecycleError):
            _normalized_refresh_plan(incomplete)

        for schema_version, registration_id in (
            (4, self._SCHEMA4_REGISTRATION_ID),
            (5, self._SCHEMA5_REGISTRATION_ID),
        ):
            with self.subTest(schema_version=schema_version):
                plan = self._plan(
                    self.names17,
                    source_refresh_schema_version=schema_version,
                    source_refresh_registration_id=registration_id,
                )
                expected = self._normalized(plan)
                self.assertEqual(expected, _normalize_refresh_plan(plan, self.root))
                self.assertEqual(plan, _normalized_refresh_plan(plan))

    def test_o030_branch_rejects_count_route_and_metadata_broadening(self) -> None:
        valid = self._plan(
            self.names17,
            source_refresh_schema_version=5,
            source_refresh_registration_id=self._SCHEMA5_REGISTRATION_ID,
        )
        variants = (
            {**valid, "candidate_route_names": [*self.names17, "O199"]},
            {**valid, "current_route_names": [*self.names16, "O199"]},
            {**valid, "source_refresh_schema_version": 6},
            {**valid, "source_refresh_schema_version": 4.0},
            {**valid, "source_refresh_schema_version": True},
            {**self._plan(self.names16), "source_refresh_schema_version": 4,
             "source_refresh_registration_id": self._SCHEMA4_REGISTRATION_ID},
        )
        for plan in variants:
            with self.subTest(plan=plan):
                with self.assertRaises(ReleaseManifestAuthorizationError):
                    _normalize_refresh_plan(plan, self.root)
                with self.assertRaises(ReleaseManifestLifecycleError):
                    _normalized_refresh_plan(plan)


class _O030TrustedRefreshFixture:
    """Build one physical D588 input without reading repository state after publish."""

    _REGISTRATION_REF = (
        ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
        "204_FEATURE_MCP/07_delivery/CA-D-588-MCP-DELIVERY--register-the-prepared-successor-binding-refresh.md"
    )
    _REGISTRATION_SOURCE_REF: str
    _EXPECTED_SCHEMA: int
    _EXPECTED_REGISTRATION_ID: str
    _INPUT_FIXTURE: Path | None = None
    _INPUT_BYTES: bytes | None = None

    def setUp(self) -> None:
        temporary = REPOSITORY / ".caprmedio_tmp/tests/o030-trusted-refresh"
        temporary.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temporary, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self._copy(self._REGISTRATION_SOURCE_REF, target_relative=self._REGISTRATION_REF)
        self.registration = registered_source_refresh(self.root)
        self.assertEqual(self._EXPECTED_SCHEMA, self.registration["schema_version"])
        self.assertEqual(self._EXPECTED_REGISTRATION_ID, self.registration["registration_id"])
        self.manifest_ref = self.registration["input_manifest_ref"]
        if self._INPUT_BYTES is not None:
            self.before = self._INPUT_BYTES
        elif self._INPUT_FIXTURE is None:
            self.before = (REPOSITORY / self.manifest_ref).read_bytes()
        else:
            self.before = self._INPUT_FIXTURE.read_bytes()
        self.input_manifest = json.loads(self.before)
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
            self._copy_registered_current_pin(replacement["current_pin"])
            if "prior_archive_path" in replacement:
                self._copy(replacement["prior_archive_path"])
            if "prior_receipt_ref" in replacement:
                self._copy(replacement["prior_receipt_ref"])
        for relative in (
            self.input_manifest["source_freshness"]["selected_source_registry_ref"],
            ".caprmedio_caprmedio/caprmedio_project_settings.toml",
            ".caprmedio_caprmedio/project_structure.toml",
            ".caprmedio_caprmedio/operators_registry.toml",
            AUTHORITY_REF,
        ):
            self._copy(relative)
        self._copy(PUBLIC_AUTHORITY_REF)
        self.path = self.root / self.manifest_ref

    def _copy(self, relative: object, *, target_relative: object | None = None) -> None:
        self.assertIsInstance(relative, str)
        target_reference = relative if target_relative is None else target_relative
        self.assertIsInstance(target_reference, str)
        source, target = REPOSITORY / relative, self.root / target_reference
        self.assertTrue(source.is_file(), relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            shutil.copy2(source, target)

    def _copy_registered_current_pin(self, pin: object) -> None:
        self.assertIsInstance(pin, dict)
        source_path = pin["source_path"]
        version = pin["version"]
        digest = pin["digest"]
        self.assertIsInstance(source_path, str)
        self.assertIsInstance(version, int)
        self.assertIsInstance(digest, str)
        source = REPOSITORY / source_path
        if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest() != digest:
            reference = PurePosixPath(source_path)
            source = REPOSITORY / reference.parent / "archive" / f"{reference.stem}@{version}{reference.suffix}"
        self.assertTrue(source.is_file(), source)
        self.assertEqual(digest, hashlib.sha256(source.read_bytes()).hexdigest())
        target = self.root / source_path
        target.parent.mkdir(parents=True, exist_ok=True)
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

    def _assert_registered_replacements(self, loaded: dict[str, object]) -> None:
        for replacement in self.registration["replacements"]:
            if replacement["target"] == "route":
                route_names = [row["route"] for row in loaded["routes"]]
                actual = loaded["routes"][route_names.index(replacement["route"])]["native_action_calls"][0]
            else:
                occurrence = replacement["occurrences"][0]
                self.assertTrue(occurrence.startswith("rmed_frontier[") and occurrence.endswith("]"))
                index = int(occurrence.removeprefix("rmed_frontier[").removesuffix("]"))
                actual = loaded["release_source_admissions"][replacement["admission_index"]]["rmed_frontier"][index]
            self.assertEqual(replacement["current_pin"], actual)

    def test_exact_authorize_execute_strict_readback_and_journal_finalization(self) -> None:
        expected_current, expected_candidate, expected_payload, _ = derive_registered_source_refresh(self.root)
        plan = plan_release_manifest_refresh(self.root)
        self.assertEqual("plan", plan["mode"])
        self.assertEqual("refresh", plan["publication_operation"])
        self.assertEqual(self._EXPECTED_SCHEMA, plan["source_refresh_schema_version"])
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
        self._assert_registered_replacements(loaded)
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

    def test_recording_failure_finalizes_the_same_event_without_replay(self) -> None:
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


class O030Schema4TrustedRefreshEndToEndTest(_O030TrustedRefreshFixture, unittest.TestCase):
    """Keep the prior v6 repair executable from D588@5 after schema-5 advances it."""

    _REGISTRATION_SOURCE_REF = (
        ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
        "204_FEATURE_MCP/07_delivery/archive/"
        "CA-D-588-MCP-DELIVERY--register-the-prepared-successor-binding-refresh@5.md"
    )
    _EXPECTED_SCHEMA = 4
    _EXPECTED_REGISTRATION_ID = "epic1848-exact-three-pin-binding-repair-20261011"
    _INPUT_FIXTURE = SCHEMA4_INPUT


class O030Schema5TrustedRefreshEndToEndTest(_O030TrustedRefreshFixture, unittest.TestCase):
    """Exercise the current O030 v6-to-v7 registration in a disposable Project."""

    _REGISTRATION_SOURCE_REF = _O030TrustedRefreshFixture._REGISTRATION_REF
    _EXPECTED_SCHEMA = 5
    _EXPECTED_REGISTRATION_ID = "epic1848-exact-o030-v7-binding-repair-20261011"
    _INPUT_BYTES = _frozen_schema5_input()

    def setUp(self) -> None:
        super().setUp()
        self.assertEqual(SCHEMA5_INPUT_SHA256, hashlib.sha256(self.before).hexdigest())

    def test_schema5_replaces_only_o030_v6_with_v7(self) -> None:
        current, expected_candidate, expected_payload, _ = derive_registered_source_refresh(self.root)
        plan = plan_release_manifest_refresh(self.root)
        context = self._authorize(plan)
        with self._git_evidence():
            result = refresh_release_manifest(self.root, execute=True, authorization=context)
        self.assertEqual("published", result["disposition"], result)
        self.assertEqual(expected_payload, self.path.read_bytes())
        loaded = load_selected_manifest(self.root)
        self.assertEqual(expected_candidate, {key: value for key, value in loaded.items() if key != "manifest_ref"})
        self.assertEqual(17, len(current["routes"]))
        self.assertEqual([row["route"] for row in current["routes"]], [row["route"] for row in loaded["routes"]])
        update_index = [row["route"] for row in current["routes"]].index("update_atom")
        before_update = copy.deepcopy(current["routes"][update_index])
        after_update = copy.deepcopy(loaded["routes"][update_index])
        self.assertEqual(6, before_update["native_action_calls"][0]["version"])
        self.assertEqual(7, after_update["native_action_calls"][0]["version"])
        before_update["native_action_calls"][0] = after_update["native_action_calls"][0]
        self.assertEqual(before_update, after_update)
        self.assertEqual(
            current["routes"][:update_index] + current["routes"][update_index + 1:],
            loaded["routes"][:update_index] + loaded["routes"][update_index + 1:],
        )
        self.assertEqual(current["release_source_admissions"], loaded["release_source_admissions"])
        self.assertEqual(current["query_source_admissions"], loaded["query_source_admissions"])
        self.assertEqual(current["public_release_source_admissions"], loaded["public_release_source_admissions"])


if __name__ == "__main__":
    unittest.main()
