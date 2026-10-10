"""Actual selected O169 Session and shared filesystem publication fixture.

Only disposable package carriers are published. Docker/host command artifact
producers are explicitly mocked by the reused native Full Gate fixture; no
runtime is started and no live Project installation is mutated.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

RELEASE_ROOT = Path(__file__).resolve().parents[1]
for folder in (RELEASE_ROOT, RELEASE_ROOT.parent, Path(__file__).resolve().parent):
    if str(folder) not in sys.path:
        sys.path.insert(0, str(folder))

import test_portable_release_full_gate as gates  # noqa: E402
import bootstrap_image  # noqa: E402
import framework_initialization as initialization  # noqa: E402
import test_bootstrap_image as bootstrap_golden  # noqa: E402
from bootstrap_image import produce_initial_framework_image, read_retained_initial_framework_image  # noqa: E402
from framework_compiler_currentness import CanonicalCompilerCurrentness  # noqa: E402
from framework_initialization import plan_initial_framework_installation  # noqa: E402
from release_actions import begin_release_action_run, SelectedReleaseActionContext  # noqa: E402
from release_contract import canonical_json  # noqa: E402
from release_checkpoint import _NATIVE_STATE_NAMES, _native_state_value, _load_native_state  # noqa: E402
from release_handoff import tree_sha256  # noqa: E402
from framework_installation import install_release, installation_status  # noqa: E402
from legacy_process_coverage import LegacyBootstrapSourceProof  # noqa: E402
import legacy_process_providers as process_providers  # noqa: E402
from release_image import DockerSubprocessExecutor  # noqa: E402
from release_portable_package import PreparedPortableReleasePackage, reopen_portable_release_package  # noqa: E402
import release_promotion as promotion  # noqa: E402
from release_promotion import prepare_and_publish_selected_native_runtime, verify_native_promotion_evidence  # noqa: E402
from operator_registry import parse_operators_registry  # noqa: E402
from portable_runtime_publication import PortableRuntimePublicationError  # noqa: E402
from selected_installation_command import _registered_journal_author  # noqa: E402
from workflow_run_support import RunTracker, RunExecutionSession  # noqa: E402


class _SelectedPhysicalFixture(gates._NativeHappyPathFixture):
    def _candidate(self):
        # An actual compiled prior Framework and Tools installation must be
        # selected before the next candidate snapshots its executing N.
        prior, provisional = gates.build_preflight_validated_candidate(
            self.root, candidate_release="N+1",
            full_suite_environment={"runner": "local-subprocess", "command": list(gates.SUITE_DRIVER_COMMAND), "working_directory": "."},
            candidate_image_reference="mock-only:N+1",
        )
        subprocess.run(["git", "init", "--quiet", str(self.root)], check=True, capture_output=True, timeout=20)
        tools = install_release(self.root, apply=True, source_root=RELEASE_ROOT.parent)
        if tools["verified"] is not True or installation_status(self.root)["verified"] is not True:
            raise AssertionError("disposable prior Tools installation was not verified")
        current = self.root / ".caprmedio_install/current.toml"
        current.parent.mkdir(parents=True, exist_ok=True)
        current.write_bytes((self.root / ".caprmedio_runtime/tools/current.toml").read_bytes())
        # Build a first-N package through the bootstrap producer, rather than
        # inventing a Framework selector whose image/proof carriers cannot be
        # reopened by the legacy predecessor reader.  The candidate output is
        # first installed at the canonical compiled root so the producer's
        # source/compiled-currentness proof is genuine for this fixture.
        prior_compiled = self.root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"
        for relative, contents in prior.output_files.items():
            target = prior_compiled / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(contents)
        skill_markdown = self.root / "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md"
        current_skill = skill_markdown.read_bytes()
        skill_markdown.write_bytes(b"# prior N ca Skill fixture\n")
        # PortablePackageFixture supplies only a pre-bootstrap placeholder;
        # the producer correctly requires an empty Framework-runtime boundary.
        (self.root / ".caprmedio_runtime/framework/current.toml").unlink()
        try:
            compiler_entrypoint = self.root / (
                "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/"
                "COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py"
            )
            source_root = self.root / gates.CANONICAL_SOURCE_RELATIVE
            currentness = CanonicalCompilerCurrentness(
                compiled_root=prior_compiled.relative_to(self.root).as_posix(),
                source_root=gates.CANONICAL_SOURCE_RELATIVE,
                compiler_entrypoint=compiler_entrypoint.relative_to(self.root).as_posix(),
                compiler_entrypoint_sha256=hashlib.sha256(compiler_entrypoint.read_bytes()).hexdigest(),
                source_frontier_digest=prior.compiler_frontier_digest,
                output_tree_digest=prior.expected_compiled_output_sha256,
                output_plan_sha256=hashlib.sha256(prior.child_manifest_bytes).hexdigest(),
                source_snapshot=tuple(
                    (path.relative_to(self.root).as_posix(), hashlib.sha256(path.read_bytes()).hexdigest())
                    for path in sorted(source_root.rglob("*")) if path.is_file()
                ),
            )
            docker = bootstrap_golden.GoldenDocker()
            real_replace = bootstrap_image.os.replace

            def retained_fixture_replace(source, target):
                source_path, target_path = Path(source), Path(target)
                if source_path.is_dir():
                    shutil.copytree(source_path, target_path, dirs_exist_ok=True)
                    return None
                return real_replace(source, target)

            # GoldenDocker and the patched subprocess boundary record a full
            # DockerSubprocess proof without contacting a Docker daemon.
            with (patch.object(initialization, "verify_canonical_compiler_currentness", return_value=currentness),
                  patch.object(DockerSubprocessExecutor, "run", side_effect=docker.run),
                  patch.object(bootstrap_image.os, "replace", side_effect=retained_fixture_replace)):
                plan = plan_initial_framework_installation(self.root)
                evidence = produce_initial_framework_image(plan, executor=DockerSubprocessExecutor())
            if evidence.outcome != "verified" or evidence.image_digest is None:
                raise AssertionError(f"bootstrap legacy predecessor was not verified: {evidence.reason}")
            self.selected_prior_release = plan.release
            package = self.root / ".caprmedio_runtime/framework/releases" / plan.release
            package.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(self.root / evidence.context_root / "PACKAGE", package, copy_function=shutil.copy2)
            self.selected_prior_bootstrap = read_retained_initial_framework_image(
                self.root, plan.release, evidence.image_digest,
            )
            if self.selected_prior_bootstrap != evidence:
                raise AssertionError("bootstrap predecessor proof did not reopen exactly")
            selector = initialization._selector(plan, evidence.image_digest)
        finally:
            skill_markdown.write_bytes(current_skill)
        (self.root / ".caprmedio_runtime/framework/current.toml").write_bytes(selector)
        self._selected_prior_selector_bytes = selector
        self._selected_tool_bytes = (self.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py").read_bytes()
        shutil.copytree(package / "SKILLS/ca", self.root / ".agents/skills/ca")
        self.selected_preflight, candidate = gates.build_preflight_validated_candidate(
            self.root, candidate_release="N+1",
            full_suite_environment={"runner": "local-subprocess", "command": list(gates.SUITE_DRIVER_COMMAND), "working_directory": "."},
            candidate_image_reference="mock-only:N+1",
        )
        return candidate

    def selected_host_capability(self):
        selector_sha, package_sha, skill_sha = gates._active_n_state(self.root, self.candidate)
        driver = self.root / f".caprmedio_runtime/framework/releases/{self.selected_prior_release}/FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_e2e.py"
        python = Path(sys.executable).resolve(strict=True)
        docker = self._host_docker
        if docker.is_symlink() or not docker.is_file() or docker.stat().st_mode & 0o111 == 0:
            raise AssertionError("seeded fixture Docker executable is unavailable")
        identity = lambda kind, path: gates.ExecutableIdentity(kind, str(path), hashlib.sha256(path.read_bytes()).hexdigest())
        return gates.FrozenHostE2ECapability(selector_sha, package_sha, skill_sha, identity("n_host_controller", driver),
                                           identity("python", python), identity("driver", driver), identity("docker", docker), str(docker.parent))

    def _seed_project(self, extra_engine_members):
        super()._seed_project(extra_engine_members)
        # Freeze one fixture-owned Docker carrier before the candidate.  The
        # full-gate path later reopens this identity; recreating it from the
        # mutable candidate workspace would make the retained host proof lie.
        self._host_docker = self.root / ".fixture-host/mock-docker"
        self._host_docker.parent.mkdir(parents=True, exist_ok=True)
        self._host_docker.write_bytes(b"#!/bin/false\n# MOCK DATA ONLY\n")
        self._host_docker.chmod(0o755)
        default = self.root / gates.CANONICAL_SOURCE_RELATIVE / "001_CORE_META_MODEL/caprmedio_framework_default_settings.toml"
        default.write_bytes(default.read_bytes() + (
            "\n[query]\nmax_request_bytes = 4096\nmax_grammar_depth = 20\nmax_filter_tokens = 100\n"
            "max_in_members = 10\nmax_selected_fields = 20\nmax_page_size = 10\nmax_snapshot_members = 20\n"
            "max_file_bytes = 8388608\nmax_total_read_bytes = 33554432\ntimeout_seconds = 5\nmax_findings = 5\n"
        ).encode())


class _SelectedBindingPhysicalFixture(_SelectedPhysicalFixture):
    """The same selected-publication fixture with one frozen Delivery binding."""

    def _seed_project(self, extra_engine_members):
        super()._seed_project(extra_engine_members)
        self.write(
            ".caprmedio_caprmedio/07_delivery/CA-D-901--binding.md",
            b"---\natom_id: CA-D-901\nstatus: Active\ncontent_role: Delivery\n"
            b"version: 1\nupdated_at: 2026-10-10 00:00:00 +0000\nrelations: {}\n---\n"
            b"# CA-D-901\n\n```toml\n[tool_binding]\n"
            b'entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"\n```\n',
        )


class SelectedNativePublicationDiagnosticTests(unittest.TestCase):
    """The selected O169 wrapper retains vetted builder diagnostics unchanged."""

    def test_builder_ca_skill_os_failure_returns_stage_and_errno_without_publication(self):
        temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        settings_path = root / ".caprmedio_caprmedio" / "settings.toml"
        settings_path.parent.mkdir(parents=True)
        settings_path.write_text('[project]\nname = "selected-diagnostic"\n', encoding="utf-8")
        package_selector = root / ".caprmedio_install" / "current.toml"
        package_selector.parent.mkdir(parents=True)
        package_selector.write_bytes(b"prior-package-selector\n")
        prior_selector = root / ".caprmedio_runtime" / "framework" / "current.toml"
        prior_selector.parent.mkdir(parents=True)
        prior_selector.write_bytes(b"prior-framework-selector\n")
        command_path = root / ".caprmedio_runtime" / "installation" / "commands" / ("e" * 64 + ".json")
        command_path.parent.mkdir(parents=True)
        command_path.write_bytes(b"fixture command\n")
        lock_path = root / ".caprmedio_runtime" / "installation" / "lock.toml"
        lock_path.write_bytes(b"fixture lock\n")

        packet = SimpleNamespace(
            evidence=SimpleNamespace(
                receipt_sha256="a" * 64,
                candidate_image_digest="sha256:" + "b" * 64,
                evidence_root=".caprmedio_tmp/selected-diagnostic-gate",
            )
        )
        package = SimpleNamespace(root=root / "package")
        package.root.mkdir()
        active_n = ("c" * 64, "d" * 64, "e" * 64)
        run = SimpleNamespace(
            project_root=str(root),
            candidate=SimpleNamespace(native_installed_n=None),
            portable_suite=SimpleNamespace(
                executing_selector_sha256=active_n[0],
                executing_release_package_sha256=active_n[1],
                executing_skill_sha256=active_n[2],
            ),
            portable_compilation=object(),
            build=object(),
            verification=object(),
            e2e=object(),
            full_gate=object(),
            prepared_portable_package=SimpleNamespace(package=package),
        )
        context = SimpleNamespace(action_run_id="selected-diagnostic-action")
        target_context = SimpleNamespace(sha256="f" * 64)
        command = SimpleNamespace(
            receipt=SimpleNamespace(sha256="e" * 64),
            receipt_path=command_path,
        )
        failure = PortableRuntimePublicationError(
            "portable-publication-ca-skill-failed",
            "local ca Skill replacement stopped with retained preparation",
            stage="copy_candidate_skill",
            os_errno=28,
            relative_path=".agents/skills/ca",
        )

        class Lock:
            def __init__(self, path):
                self.lock_generation = "f" * 32
                self.lock_path = path

        class LockContext:
            def __init__(self, lock):
                self._lock = lock

            def __enter__(self):
                return self._lock

            def __exit__(self, *_args):
                return False

        def physical_file(project_root, relative):
            path = Path(project_root) / Path(relative)
            if not path.is_file():
                raise FileNotFoundError(path)
            return path

        with (
            patch.object(promotion, "admit_selected_native_promotion_start", return_value=object()),
            patch.object(promotion, "retained_native_promotion_packet", return_value=packet),
            patch.object(promotion, "_file", side_effect=physical_file),
            patch("release_suite._active_n_state", return_value=active_n),
            patch("work_journal.resolve_settings_path", return_value=settings_path),
            patch("framework_package.provide_installation_package_evidence", return_value=object()),
            patch("framework_package.verify_current_package_selector", return_value=object()),
            patch("installation_context.TargetProjectRequest", side_effect=lambda **kwargs: SimpleNamespace(**kwargs)),
            patch("installation_context.bind_target_project_context", return_value=target_context),
            patch("framework_installation.PortableInstallationRequest", side_effect=lambda **kwargs: SimpleNamespace(**kwargs)),
            patch("portable_runtime_materialization.CandidateRuntimeCommandStageRequest", side_effect=lambda **kwargs: SimpleNamespace(**kwargs)),
            patch("portable_methodology_installation.prepare_candidate_portable_methodology_publication", return_value=object()),
            patch("portable_runtime_publication.render_package_selector", return_value=b"candidate-selector\n"),
            patch("portable_runtime_publication.build_prepared_native_publication", side_effect=failure) as build,
            patch("selected_installation_command.retain_selected_installation_command", return_value=command),
            patch("installation_transaction.installation_publication_lock", return_value=LockContext(Lock(lock_path))),
            patch.object(promotion.shutil, "which", return_value=str(Path(sys.executable).resolve())),
            patch.object(promotion, "publish_selected_native_runtime") as publish,
        ):
            outcome, reason, refs, promoted = promotion.prepare_and_publish_selected_native_runtime(run, context)

        self.assertEqual("effect_uncertain", outcome)
        self.assertEqual(
            "native preparation/publication stopped: portable-publication-ca-skill-failed; "
            "stage=copy_candidate_skill; errno=28; path=.agents/skills/ca; "
            "exact partial carriers retained, no replay",
            reason,
        )
        self.assertIn(command_path.relative_to(root).as_posix(), refs)
        self.assertIn(lock_path.relative_to(root).as_posix(), refs)
        self.assertIsNone(promoted)
        build.assert_called_once()
        publish.assert_not_called()


class SelectedNativePublicationPhysicalTests(unittest.TestCase):
    fixture_type = _SelectedPhysicalFixture

    @classmethod
    def setUpClass(cls):
        cls.fixture = cls.fixture_type()
        with gates._fixture_authority(cls.fixture._fixture_authority_pin), patch.object(gates, "_install_active_n", return_value=None), patch.object(gates, "_frozen_host_capability", side_effect=lambda fixture: fixture.selected_host_capability()):
            cls.parts = gates.PortableReleaseFullGateBoundaryTests()._run_mock_native_retained_happy_path(cls.fixture)
        # The reused retained-reader fixture deliberately drifts these two
        # disposable carriers after gating. Restore its exact originally
        # observed bytes before exercising current selected publication.
        (cls.fixture.root / ".caprmedio_runtime/framework/current.toml").write_bytes(cls.fixture._selected_prior_selector_bytes)
        (cls.fixture.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py").write_bytes(cls.fixture._selected_tool_bytes)

    def test_same_gated_package_is_published_by_actual_selected_action_without_o200_run(self):
        fixture = self.fixture
        root = fixture.root
        suite, build, verification, e2e, full, _identity = self.parts
        package = reopen_portable_release_package(root, full.candidate_run_id, full.package_manifest_sha256)
        old_skill_bytes = (root / ".agents/skills/ca/SKILL.md").read_bytes()
        self.assertNotEqual(old_skill_bytes, (package.root / "SKILLS/ca/SKILL.md").read_bytes())
        authoring_before = tree_sha256(root, gates.CANONICAL_SOURCE_RELATIVE)
        # Both actual legacy selectors and complete predecessor packages were
        # already selected before candidate freezing and Unit admission.
        for name in ("project_mcp", "mcp_hot_reload", "workflow_orchestrator"):
            state = root / ".caprmedio_install" / name
            state.mkdir()
            (state / "state.txt").write_text("exact disposable prior state", encoding="utf-8")
        # The physical publisher correctly treats an unavailable host process
        # table as ``unknown``.  This disposable fixture must not turn that
        # refusal into a live-host absence claim.  Instead it retains the real
        # three provider-owned fences while substituting their bounded
        # *golden* query results.  The production adapter still parses the
        # exact ``outcome``/``records`` grammar below and revalidates the
        # concrete installation fence around every snapshot.
        receipt = (
            root / bootstrap_image.BOOTSTRAP_IMAGE_RELATIVE
            / fixture.selected_prior_bootstrap.bootstrap_proof_key / "evidence.toml"
        ).read_bytes()
        expected_predecessor = LegacyBootstrapSourceProof(
            framework_selector_bytes=fixture._selected_prior_selector_bytes,
            tool_selector_bytes=(root / ".caprmedio_runtime/tools/current.toml").read_bytes(),
            package_manifest_sha256=fixture.selected_prior_bootstrap.manifest_sha256,
            source_context_sha256=fixture.selected_prior_bootstrap.source_context_sha256,
            image_digest=fixture.selected_prior_bootstrap.image_digest,
            bootstrap_proof_key=fixture.selected_prior_bootstrap.bootstrap_proof_key,
            raw_receipt_bytes=receipt,
        )

        class GoldenHeldProviderFence:
            """Fixture-only process-table response held by the real singleton lock."""

            def __init__(self, provider, physical_fence):
                self.provider = provider
                self._physical_fence = physical_fence
                self.deadlines: list[float] = []
                self.closed = False

            def snapshot(self, deadline):
                if self.closed:
                    raise AssertionError("golden hot-reload fence was queried after close")
                self.deadlines.append(deadline)
                # This is the provider's closed result grammar, not caller
                # observations.  It is intentionally visible in this test as
                # a mocked host query rather than evidence about this machine.
                return {"outcome": "complete", "records": []}

            def close(self):
                self._physical_fence.close()
                self.closed = True

        real_open_provider_fence = process_providers._open_provider_fence
        golden_provider_fences: list[GoldenHeldProviderFence] = []

        def open_fixture_provider_fence(provider, admission, deadline):
            physical_fence = real_open_provider_fence(provider, admission, deadline)
            self.assertIn(provider, process_providers.PROVIDERS)
            self.assertIsInstance(admission.predecessor_proof, LegacyBootstrapSourceProof)
            self.assertEqual(expected_predecessor, admission.predecessor_proof)
            golden = GoldenHeldProviderFence(provider, physical_fence)
            golden_provider_fences.append(golden)
            return golden

        manifest = fixture.candidate.manifest
        parameters = {
            "operation": "apply", "project_root": str(root),
            "candidateSnapshotManifest": manifest.model_dump(mode="json", by_alias=True),
            "expected_executing_release": manifest.executing_release,
            "expected_project_structure_digest": manifest.project_structure_digest,
            "expected_framework_settings_digest": manifest.framework_settings_digest,
            "expected_source_frontier_digest": manifest.source_frontier_digest,
            "run_receipt_refs": ["selected-native-physical-fixture"],
        }
        definitions = {}
        operations = root / gates.CANONICAL_SOURCE_RELATIVE / "003_PROJECT_CONFIGURATION/09_operations"
        for kind, atom_id, version in (("workflow", "CA-O-164", 9), ("step", "CA-O-178", 3), ("action", "CA-O-169", 5)):
            path = next(operations.glob(f"{atom_id}-*.md"))
            definitions[kind] = {"atom_id": atom_id, "version": version,
                                 "path": path.relative_to(root).as_posix(), "digest": hashlib.sha256(path.read_bytes()).hexdigest()}
        requested = [
            {"requested_run_id": fixture.run_id, "kind": "workflow", "definition": definitions["workflow"]},
            {"requested_run_id": "physical-step", "kind": "step", "definition": definitions["step"], "parent_requested_run_id": fixture.run_id},
            {"requested_run_id": "physical-action", "kind": "action", "definition": definitions["action"], "parent_requested_run_id": "physical-step"},
        ]
        request = {
            "mode": "execute", "request_id": "selected-native-physical", "operation_route": "release_version",
            "parameters": parameters, "parameters_digest": hashlib.sha256(canonical_json(parameters)).hexdigest(),
            "target_frontier_digest": "a" * 64, "effects_digest": "b" * 64,
            "definition_manifest": {"manifest_ref": "fixture.json", "manifest_digest": "c" * 64},
            "source_freshness": {}, "assigned_action_id": "physical-selected-assignment",
            "initiative": {"initiative_id": "fixture", "instruction_summary": "selected physical publication"},
            "requested_runs": requested, "proposal_receipt": {"fixture": "exact"}, "proposal_receipt_digest": "d" * 64,
        }
        keys = ("request_id", "operation_route", "proposal_receipt_digest", "parameters_digest",
                "target_frontier_digest", "effects_digest", "definition_manifest", "source_freshness")
        request["operator_authorization"] = {
            **{key: request[key] for key in keys}, "authorization_ref": "fixture/authorization",
            "authorization_freshness": {"state": "current", "digest": "e" * 64},
        }
        records = parse_operators_registry((root / ".caprmedio_caprmedio/operators_registry.toml").read_bytes())
        author = next(_registered_journal_author(record) for record in records if _registered_journal_author(record) is not None)
        tracker = RunTracker(root, source_observer=lambda _request: {"selected": True, "current": True, "observed": {}},
                             executor=lambda _request, _runs: {}, journal_context={"author": author, "timezone": "UTC"})
        session = RunExecutionSession(tracker, request)
        session.start_run(fixture.run_id)
        session.start_run("physical-step")
        session.start_run("physical-action")
        run = begin_release_action_run(parameters, workflow_run_id=fixture.run_id)
        run.selected_action_session = session
        run.candidate = fixture.candidate
        run.preflight = fixture.selected_preflight
        run.methodology_export, run.private_compilation = fixture.export, fixture.private_compilation
        run.portable_source_snapshot, run.portable_compilation = fixture.source_snapshot, fixture.sealed
        run.portable_suite, run.build, run.verification, run.e2e, run.full_gate = suite, build, verification, e2e, full
        run.prepared_portable_package = PreparedPortableReleasePackage(
            full.candidate_run_id, manifest.sha256, full.input_manifest_sha256, package,
        )
        context = SelectedReleaseActionContext(str(root), fixture.run_id, "physical-step", "physical-action",
                                               fixture.run_id, "physical-step", "CA-O-178", "CA-O-169",
                                               run.frozen_parameters_sha256, workflow_version=9)
        with patch.object(process_providers, "_open_provider_fence", side_effect=open_fixture_provider_fence):
            outcome, reason, refs, promoted = prepare_and_publish_selected_native_runtime(run, context)
        self.assertEqual(outcome, "completed", reason)
        self.assertEqual(promoted.outcome, "promoted")
        self.assertEqual(set(process_providers.PROVIDERS), {fence.provider for fence in golden_provider_fences})
        self.assertTrue(all(fence.deadlines for fence in golden_provider_fences))
        self.assertTrue(all(fence.closed for fence in golden_provider_fences))
        self.assertTrue(refs)
        self.assertEqual({item["definition"]["atom_id"] for item in session.actual.values()}, {"CA-O-164", "CA-O-178", "CA-O-169"})
        self.assertEqual(verify_native_promotion_evidence(
            fixture.candidate, fixture.sealed, suite, build, verification, promoted,
            e2e=e2e, full_gate=full, prepared_package=run.prepared_portable_package,
        ), root)
        self.assertEqual(tree_sha256(root, gates.CANONICAL_SOURCE_RELATIVE), authoring_before)
        exported = root / fixture.export.source_export_root
        source_records = {path.relative_to(exported).as_posix(): (hashlib.sha256(path.read_bytes()).hexdigest(), path.stat().st_mode & 0o777)
                          for path in exported.rglob("*") if path.is_file()}
        published = root / "methodology"
        self.assertEqual({path.relative_to(published).as_posix(): (hashlib.sha256(path.read_bytes()).hexdigest(), path.stat().st_mode & 0o777)
                          for path in published.rglob("*") if path.is_file()}, source_records)
        self.assertEqual({path.relative_to(root / ".agents/skills/ca").as_posix(): (hashlib.sha256(path.read_bytes()).hexdigest(), path.stat().st_mode & 0o777)
                          for path in (root / ".agents/skills/ca").rglob("*") if path.is_file()},
                         {row.path.removeprefix("SKILLS/ca/"): (row.sha256, row.mode) for row in package.inventory if row.path.startswith("SKILLS/ca/")})
        self.assertFalse((root / ".caprmedio_runtime/installation/lock.toml").exists())
        # Encode only genuinely observed state: no fabricated predecessor Run
        # results or Journal terminal receipts are needed by this documentary
        # codec check. Runtime Session permission is deliberately not encoded.
        run.promotion = promoted
        state = {name: _native_state_value(run, name) for name in _NATIVE_STATE_NAMES}
        restored = _load_native_state(state, str(root))
        self.assertEqual(restored["promotion"], promoted)
        self.assertEqual(restored["full_gate"], full)
        self.assertEqual(restored["prepared_portable_package"].package_manifest_sha256, package.manifest_digest)
        self._assert_published_binding_frontier(fixture, package, restored)

    def _assert_published_binding_frontier(self, fixture, package, restored) -> None:
        """Keep the existing empty-frontier physical case behavior unchanged."""


class SelectedNativePublicationBindingPhysicalTests(SelectedNativePublicationPhysicalTests):
    """Actual selected publication retains a nonempty package binding frontier."""

    fixture_type = _SelectedBindingPhysicalFixture

    def _assert_published_binding_frontier(self, fixture, package, restored) -> None:
        self.assertTrue(fixture.source_snapshot.binding_atoms)
        self.assertEqual(fixture.source_snapshot.binding_atoms, fixture.sealed.binding_atoms)
        self.assertTrue(package.binding_atoms)
        self.assertEqual(
            tuple(atom.record() for atom in fixture.sealed.binding_atoms),
            tuple(atom.record() for atom in package.binding_atoms),
        )
        self.assertEqual(fixture.source_snapshot.binding_atoms, restored["portable_source_snapshot"].binding_atoms)
        self.assertEqual(fixture.sealed.binding_atoms, restored["portable_compilation"].binding_atoms)
        self.assertEqual(package.binding_atoms, restored["prepared_portable_package"].package.binding_atoms)


if __name__ == "__main__":
    unittest.main()
