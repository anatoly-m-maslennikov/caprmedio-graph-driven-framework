"""Physical publication tests for the shared native O200/O169 cut-over.

The fixtures deliberately exercise filesystem carriers only.  They do not
start a runtime, Docker, or a live installation command beyond the direct
Action fixture used to prove recording-pending behavior.
"""

from __future__ import annotations

import errno
import hashlib
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from dataclasses import replace
from types import SimpleNamespace
from unittest.mock import Mock, patch


TOOLS = Path(__file__).resolve().parents[1]
RELEASE_ROOT = TOOLS / "RELEASE_VERSION"
RELEASE_TEST_ROOT = RELEASE_ROOT / "tests"
for _path in (TOOLS, Path(__file__).resolve().parent, RELEASE_ROOT, RELEASE_TEST_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

import portable_runtime_publication as publication_module  # noqa: E402
import test_native_installation_proof as proof_fixture  # noqa: E402
import test_native_selected_installation as selected_native_fixture  # noqa: E402
import test_retained_bootstrap_image as retained_bootstrap_fixture  # noqa: E402
from installation_transaction import InstallationPublicationLock, InstallationTransactionError  # noqa: E402
from framework_installation import install_release, installation_status  # noqa: E402
from legacy_process_coverage import (  # noqa: E402
    LegacyBootstrapSourceProof,
    ProviderCoverageEvidence,
    open_legacy_process_coverage,
)
from portable_runtime_publication import (  # noqa: E402
    PortableRuntimePublicationError,
    _close_process_coverage,
    _prepare_legacy_replacement,
    _revalidate_legacy_replacement,
    publish_replacement_package,
    stage_replacement_package,
)


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


class _TrackingCoverage:
    """Minimal opaque-handle stand-in used only to prove ownership cleanup."""

    def __init__(self) -> None:
        self.close_calls = 0

    def close(self) -> None:
        self.close_calls += 1


class _RootlessNativeCoverageHandle:
    """Fixture provider handle whose evidence is physically re-opened."""

    def __init__(self, provider: "_RootlessNativeCoverageProvider") -> None:
        self._provider = provider
        self.owned_subtree = provider.owned_subtree
        self.provider_namespace = provider.provider_namespace
        self.closed = False

    def snapshot(self) -> ProviderCoverageEvidence:
        if self.closed:
            raise RuntimeError("rootless native fixture provider handle is closed")
        return ProviderCoverageEvidence(
            state=self._provider.state,
            namespace=self.provider_namespace,
            evidence=dict(self._provider.evidence),
            observations=(),
        )

    def close(self) -> None:
        self.closed = True


class _RootlessNativeCoverageProvider:
    """One D607 fixture namespace; it never supplies caller observations."""

    def __init__(self, owned_subtree: str, predecessor_proof: object, *, state: str = "absent") -> None:
        self.owned_subtree = owned_subtree
        self.provider_namespace = f"fixture://rootless-native/{owned_subtree}"
        self.state = state
        evidence_binding = getattr(predecessor_proof, "evidence_binding", None)
        assert callable(evidence_binding)
        self.evidence = {
            "query": "publisher-rootless-native-fixture",
            "matches": [],
            "predecessor_proof": evidence_binding(),
        }

    def open_legacy_process_evidence(self, **_bindings: object) -> _RootlessNativeCoverageHandle:
        return _RootlessNativeCoverageHandle(self)


class CaSkillPublicationFailureDiagnosticsTests(unittest.TestCase):
    """The destructive local Skill boundary records the actual failed OS stage."""

    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        package_root = self.root / "candidate-package"
        source = package_root / "SKILLS" / "ca"
        candidate_payloads = {
            "SKILL.md": b"---\nname: ca\n---\n# candidate\n",
            "agents/openai.yaml": b"interface:\n  display_name: Candidate CA\n",
        }
        members = []
        for relative, payload in candidate_payloads.items():
            carrier = source / relative
            carrier.parent.mkdir(parents=True, exist_ok=True)
            carrier.write_bytes(payload)
            carrier.chmod(0o644)
            members.append(
                SimpleNamespace(
                    path=f"SKILLS/ca/{relative}",
                    sha256=hashlib.sha256(payload).hexdigest(),
                    mode=0o644,
                )
            )
        self.package = SimpleNamespace(root=package_root, manifest_digest="a" * 64)
        self.context = SimpleNamespace(sha256="b" * 64)
        self.binding = SimpleNamespace(package_ca_skill=tuple(members))
        self.target = self.root / ".agents" / "skills" / "ca"
        for relative, payload in {
            "SKILL.md": b"---\nname: ca\n---\n# prior\n",
            "agents/openai.yaml": b"interface:\n  display_name: Prior CA\n",
        }.items():
            carrier = self.target / relative
            carrier.parent.mkdir(parents=True, exist_ok=True)
            carrier.write_bytes(payload)
            carrier.chmod(0o644)
        self.lock = InstallationPublicationLock(
            self.root,
            target_context_sha256=self.context.sha256,
            owner_run_id="ca-skill-diagnostic-fixture",
            operation="install_framework_runtime",
            command_sha256="c" * 64,
        ).acquire()
        self.addCleanup(lambda: self.lock.active and self.lock.release("completed"))

    def _publish(self) -> object:
        return publication_module._prepare_and_publish_ca_skill(
            self.root,
            package=self.package,
            target_context=self.context,
            candidate_mcp_binding=self.binding,
            lock=self.lock,
        )

    def _assert_retained_failure(
        self,
        error: PortableRuntimePublicationError,
        *,
        stage: str,
        os_errno: int,
    ) -> None:
        self.assertEqual("portable-publication-ca-skill-failed", error.code)
        self.assertEqual(stage, error.stage)
        self.assertEqual(os_errno, error.os_errno)
        self.assertEqual(".agents/skills/ca", error.relative_path)
        self.assertIsInstance(error.__cause__, OSError)
        assert isinstance(error.__cause__, OSError)
        self.assertEqual(os_errno, error.__cause__.errno)
        self.assertNotIn(str(self.root), str(error))
        self.assertIn(f"stage={stage}; errno={os_errno}; path=.agents/skills/ca", str(error))
        self.assertEqual(
            f"portable-publication-ca-skill-failed; stage={stage}; errno={os_errno}; path=.agents/skills/ca",
            publication_module.retained_publication_failure_reason(error),
        )
        stage_root = self.root / ".caprmedio_tmp" / "installation" / "ca-skill" / self.lock.lock_generation
        self.assertTrue((stage_root / "candidate").is_dir())
        self.assertTrue((stage_root / "prior").is_dir())
        self.assertTrue((stage_root / "preparation.json").is_file())
        self.assertTrue(self.lock.active)

    def test_remove_prior_skill_eperm_is_not_reported_as_candidate_copy_failure(self) -> None:
        with patch.object(
            publication_module.shutil,
            "rmtree",
            side_effect=PermissionError(errno.EPERM, "operation not permitted", str(self.target)),
        ) as remove_prior:
            with self.assertRaises(PortableRuntimePublicationError) as failed:
                self._publish()

        remove_prior.assert_called_once_with(self.target)
        self._assert_retained_failure(failed.exception, stage="remove_prior_skill", os_errno=errno.EPERM)
        self.assertEqual(b"---\nname: ca\n---\n# prior\n", (self.target / "SKILL.md").read_bytes())

    def test_copy_candidate_skill_error_keeps_its_original_errno_after_prior_removal(self) -> None:
        real_copytree = publication_module.shutil.copytree
        candidate_stage = (
            self.root
            / ".caprmedio_tmp"
            / "installation"
            / "ca-skill"
            / self.lock.lock_generation
            / "candidate"
        )

        def fail_final_copy(source: object, destination: object, *args: object, **kwargs: object) -> object:
            if Path(source) == candidate_stage and Path(destination) == self.target:
                raise OSError(errno.ENOSPC, "no space left on device", str(destination))
            return real_copytree(source, destination, *args, **kwargs)

        with (
            patch.object(publication_module.shutil, "rmtree", return_value=None) as remove_prior,
            patch.object(publication_module.shutil, "copytree", side_effect=fail_final_copy),
        ):
            with self.assertRaises(PortableRuntimePublicationError) as failed:
                self._publish()

        remove_prior.assert_called_once_with(self.target)
        self._assert_retained_failure(failed.exception, stage="copy_candidate_skill", os_errno=errno.ENOSPC)
        self.assertTrue(self.target.is_dir())


class ReplacementPackagePhysicalTests(unittest.TestCase):
    """Bootstrap/native replacement effects stay bounded to exact carriers."""

    @classmethod
    def setUpClass(cls) -> None:
        proof_fixture.CandidateNativeInstallationProofTests.setUpClass()

    def setUp(self) -> None:
        self.fixture = proof_fixture.CandidateNativeInstallationProofTests("runTest")
        self.fixture.setUp()
        # This imported physical Full-Gate fixture intentionally retains its
        # disposable archive; its own package setup may carry open immutable
        # evidence descriptors that make cleanup platform-dependent.
        self.root = self.fixture.target
        self.package = self.fixture.package
        self.context = self.fixture.context
        self.lock = InstallationPublicationLock(
            self.root,
            target_context_sha256=self.context.sha256,
            owner_run_id="portable-publication-fixture",
            operation="install_framework_runtime",
            command_sha256="c" * 64,
        ).acquire()
        self.addCleanup(lambda: self.lock.active and self.lock.release("completed"))

    def _selector(self) -> bytes:
        return self.fixture._package_selector()

    def _stage(self):
        return stage_replacement_package(self.package, lock=self.lock)

    def _install_old_native(self) -> tuple[Path, bytes, bytes]:
        destination = self.root / ".caprmedio_install" / "releases" / self.package.manifest_digest
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(self.package.root, destination)
        selector = self._selector()
        package_current = self.root / ".caprmedio_install" / "current.toml"
        package_current.write_bytes(selector)
        runtime_current = self.root / ".caprmedio_runtime" / "installation" / "current.toml"
        runtime_current.parent.mkdir(parents=True, exist_ok=True)
        runtime = b'native = "old"\n'
        runtime_current.write_bytes(runtime)
        return destination, selector, runtime

    def _seed_owned_runtime_state(self) -> None:
        for name in ("project_mcp", "mcp_hot_reload", "workflow_orchestrator"):
            carrier = self.root / ".caprmedio_install" / name / "state.txt"
            carrier.parent.mkdir(parents=True, exist_ok=True)
            carrier.write_bytes(f"preserve {name} state\n".encode("utf-8"))

    def _install_old_legacy(self) -> tuple[Path, bytes, bytes]:
        """Create an actual schema-2 Framework predecessor and verified tools state."""

        # ``installation_status`` deliberately resolves an actual repository
        # root.  A bare Git directory is sufficient for this filesystem-only
        # fixture; no Git operation or live installation is involved.
        (self.root / ".git").mkdir()
        installed_tools = install_release(self.root, apply=True, source_root=TOOLS)
        self.assertTrue(installed_tools["verified"])
        tools_selector = (self.root / ".caprmedio_runtime" / "tools" / "current.toml").read_bytes()
        # D605 owns the historic package-selector location, while the
        # framework-installation verifier owns the old Tool-runtime location.
        # The exact same closed selector bytes bind both retained surfaces.
        install_current = self.root / ".caprmedio_install" / "current.toml"
        install_current.parent.mkdir(parents=True, exist_ok=True)
        install_current.write_bytes(tools_selector)

        members = {
            "FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/sentinel.py": b"legacy_engine = True\n",
            "METHODOLOGY/sources/sentinel.md": b"# retained legacy methodology\n",
            "SKILLS/ca/SKILL.md": b"---\nname: ca\n---\n",
        }
        rows = []
        for destination, payload in members.items():
            resource = destination.split("/", 1)[0]
            rows.extend(
                (
                    "[[files]]",
                    f'resource = "{resource}"',
                    f'source_path = "source/{destination}"',
                    f'destination = "{destination}"',
                    f'sha256 = "{hashlib.sha256(payload).hexdigest()}"',
                    "mode = 420",
                    "",
                )
            )
        manifest = (
            "schema_version = 2\n"
            f'candidate_snapshot_manifest_sha256 = "{"d" * 64}"\n'
            'package = "caprmedio-framework"\n\n'
            + "\n".join(rows)
        ).encode("utf-8")
        release = hashlib.sha256(manifest).hexdigest()
        legacy_root = self.root / ".caprmedio_runtime" / "framework" / "releases" / release
        for destination, payload in members.items():
            carrier = legacy_root / destination
            carrier.parent.mkdir(parents=True, exist_ok=True)
            carrier.write_bytes(payload)
            carrier.chmod(0o644)
        legacy_root.mkdir(parents=True, exist_ok=True)
        (legacy_root / "manifest.toml").write_bytes(manifest)
        (legacy_root / "manifest.toml").chmod(0o644)
        legacy_relative = f".caprmedio_runtime/framework/releases/{release}"
        legacy_selector = (
            "schema_version = 1\n"
            f'manifest_sha256 = "{release}"\n'
            f'release = "{release}"\n'
            f'selected_release_root = "{legacy_relative}"\n'
            f'framework_engine_root = "{legacy_relative}/FRAMEWORK_ENGINE"\n'
            f'methodology_root = "{legacy_relative}/METHODOLOGY"\n'
            f'image_digest = "sha256:{"b" * 64}"\n'
        ).encode("utf-8")
        execution = self.root / ".caprmedio_runtime" / "framework" / "current.toml"
        execution.parent.mkdir(parents=True, exist_ok=True)
        execution.write_bytes(legacy_selector)
        return legacy_root, tools_selector, legacy_selector

    def test_bootstrap_installs_stage_without_touching_existing_configuration(self) -> None:
        config = self.root / ".caprmedio_runtime" / "config.toml"
        config.parent.mkdir(parents=True, exist_ok=True)
        original_config = b"[runtime]\nuser_value = 'keep'\n"
        config.write_bytes(original_config)

        installed = publish_replacement_package(
            self._stage(), lock=self.lock, old_package_selector=None, old_execution_selector=None
        )

        self.assertEqual(installed.manifest_digest, self.package.manifest_digest)
        self.assertTrue((self.root / ".caprmedio_install" / "releases" / self.package.manifest_digest).is_dir())
        self.assertEqual(original_config, config.read_bytes())
        self.assertFalse((self.root / ".caprmedio_install" / "current.toml").exists())
        self.assertFalse((self.root / ".caprmedio_runtime" / "installation" / "current.toml").exists())

    def test_native_replacement_removes_only_the_exact_selected_old_package(self) -> None:
        old_package, package_selector, runtime_selector = self._install_old_native()
        self._seed_owned_runtime_state()
        journal = self.root / ".control" / "journal.ndjson"
        journal.parent.mkdir(parents=True, exist_ok=True)
        journal.write_bytes(b'{"preserved":true}\n')
        config = self.root / ".caprmedio_runtime" / "config.toml"
        config.write_bytes(b"[runtime]\nkeep = true\n")
        installed = publish_replacement_package(
            self._stage(),
            lock=self.lock,
            old_package_selector=package_selector,
            old_execution_selector=(Path(".caprmedio_runtime/installation/current.toml"), runtime_selector),
        )

        self.assertEqual(installed.root, old_package)
        self.assertFalse((self.root / ".caprmedio_install" / "current.toml").exists())
        self.assertFalse((self.root / ".caprmedio_runtime" / "installation" / "current.toml").exists())
        self.assertEqual(b'{"preserved":true}\n', journal.read_bytes())
        self.assertEqual(b"[runtime]\nkeep = true\n", config.read_bytes())

    def test_failure_after_old_removal_leaves_no_stale_selector_or_package_claim(self) -> None:
        old_package, package_selector, runtime_selector = self._install_old_native()
        stage = self._stage()
        config = self.root / ".caprmedio_runtime" / "config.toml"
        config.write_bytes(b"[runtime]\nkeep = true\n")
        real_replace = publication_module.os.replace
        real_copytree = publication_module.shutil.copytree

        def fail_stage_rename(source, destination):
            if Path(source) == stage.root:
                raise OSError("fixture installation failure")
            return real_replace(source, destination)

        def fail_stage_copy(source, destination, *args, **kwargs):
            if Path(source) == stage.root:
                raise OSError("fixture installation copy failure")
            return real_copytree(source, destination, *args, **kwargs)

        with (
            patch.object(publication_module.os, "replace", side_effect=fail_stage_rename),
            patch.object(publication_module.shutil, "copytree", side_effect=fail_stage_copy),
        ):
            with self.assertRaises(PortableRuntimePublicationError) as failed:
                publish_replacement_package(
                    stage,
                    lock=self.lock,
                    old_package_selector=package_selector,
                    old_execution_selector=(Path(".caprmedio_runtime/installation/current.toml"), runtime_selector),
                )

        self.assertEqual("portable-publication-install-failed", failed.exception.code)
        self.assertFalse((old_package / "manifest.toml").exists())
        self.assertFalse((self.root / ".caprmedio_install" / "current.toml").exists())
        self.assertFalse((self.root / ".caprmedio_runtime" / "installation" / "current.toml").exists())
        self.assertEqual(b"[runtime]\nkeep = true\n", config.read_bytes())

    def test_second_selector_unlink_records_unavailable_after_execution_selection_is_removed(self) -> None:
        """A failed package-selector unlink cannot relabel prior deletion as blocked."""

        import framework_installation_command

        _old_package, package_selector, runtime_selector = self._install_old_native()
        stage = self._stage()
        package_current = self.root / ".caprmedio_install" / "current.toml"
        runtime_current = self.root / ".caprmedio_runtime" / "installation" / "current.toml"
        config = self.root / ".caprmedio_runtime" / "config.toml"
        original_config = b"[runtime]\nkeep = true\n"
        config.write_bytes(original_config)
        prepared = publication_module.PreparedNativePublication(
            package=self.package,
            target_context=self.context,
            candidate_proof_request=SimpleNamespace(full_gate_packet=object()),
            candidate_proof=SimpleNamespace(state_generation=1),
            methodology_delivery=object(),
            candidate_mcp_binding=object(),
            prospective_package_selector=b"candidate package selector",
            prospective_runtime_selector=b"candidate runtime selector",
            old_package_selector=package_selector,
            old_execution_selector=(Path(".caprmedio_runtime/installation/current.toml"), runtime_selector),
        )
        real_unlink = Path.unlink

        def fail_second_selector_unlink(path: Path, *args: object, **kwargs: object) -> None:
            if path == package_current:
                raise OSError("fixture package-selector unlink failure")
            real_unlink(path, *args, **kwargs)

        def publish_once(_command: object, _prepared: object, *, lock: object) -> object:
            return publication_module.publish_replacement_package(
                stage,
                lock=lock,
                old_package_selector=package_selector,
                old_execution_selector=(Path(".caprmedio_runtime/installation/current.toml"), runtime_selector),
            )

        with (
            patch.object(Path, "unlink", new=fail_second_selector_unlink),
            patch.object(
                framework_installation_command,
                "prepare_direct_full_gate_effect_closure",
                return_value=object(),
            ),
            patch.object(publication_module, "publish_direct_native_runtime", side_effect=publish_once) as publish,
            patch.object(
                publication_module,
                "record_direct_publication_result",
                return_value={"state": "recorded"},
            ) as record,
        ):
            result = publication_module.execute_direct_native_runtime(object(), prepared, lock=self.lock)

        self.assertIsNone(result.publication)
        self.assertEqual({"state": "recorded"}, result.recording)
        publish.assert_called_once()
        self.assertEqual("unavailable_after_delete", record.call_args.kwargs["effect_outcome"])
        self.assertEqual("portable-publication-old-selector-removal-failed", record.call_args.kwargs["reason"])
        self.assertFalse(runtime_current.exists())
        self.assertTrue(package_current.exists())
        self.assertEqual(package_selector, package_current.read_bytes())
        self.assertEqual(original_config, config.read_bytes())
        self.assertTrue((self.root / ".caprmedio_install" / "releases" / self.package.manifest_digest / "manifest.toml").is_file())

    def test_legacy_replacement_refuses_without_a_retained_prior_context_proof(self) -> None:
        old_package, tools_selector, legacy_selector = self._install_old_legacy()
        config = self.root / ".caprmedio_runtime" / "config.toml"
        config.parent.mkdir(parents=True, exist_ok=True)
        config.write_bytes(b"[runtime]\nkeep = true\n")
        state = self.root / ".caprmedio_install" / "project_mcp" / "state.txt"
        for name in ("project_mcp", "mcp_hot_reload", "workflow_orchestrator"):
            carrier = self.root / ".caprmedio_install" / name / "state.txt"
            carrier.parent.mkdir(parents=True, exist_ok=True)
            carrier.write_bytes(f"preserve {name} state\n".encode("utf-8"))
        with self.assertRaises(PortableRuntimePublicationError) as unavailable:
            _prepare_legacy_replacement(
                self.root,
                target_context=self.context,
                old_package_selector=tools_selector,
                old_execution_selector=(Path(".caprmedio_runtime/framework/current.toml"), legacy_selector),
                lock=self.lock,
            )

        self.assertEqual("portable-publication-legacy-prior-context-unavailable", unavailable.exception.code)
        self.assertTrue((old_package / "manifest.toml").is_file())
        self.assertTrue((self.root / ".caprmedio_runtime" / "framework" / "current.toml").is_file())
        self.assertTrue((self.root / ".caprmedio_install" / "current.toml").is_file())
        self.assertEqual(b"[runtime]\nkeep = true\n", config.read_bytes())
        self.assertEqual(b"preserve project_mcp state\n", state.read_bytes())
        self.assertTrue(installation_status(self.root)["verified"])


class LegacyBootstrapPredecessorTests(unittest.TestCase):
    """A pre-D600 predecessor retains bootstrap, never prospective, identity."""

    def setUp(self) -> None:
        fixture = retained_bootstrap_fixture.RetainedBootstrapImageTests("runTest")
        fixture.setUp()
        self.fixture = fixture
        self.root = fixture.root
        (self.root / ".git").mkdir()
        installed_tools = install_release(self.root, apply=True, source_root=TOOLS)
        self.assertTrue(installed_tools["verified"])
        self.tools_selector = (self.root / ".caprmedio_runtime" / "tools" / "current.toml").read_bytes()
        install_selector = self.root / ".caprmedio_install" / "current.toml"
        install_selector.parent.mkdir(parents=True, exist_ok=True)
        install_selector.write_bytes(self.tools_selector)

        release = fixture.plan.release
        legacy_relative = f".caprmedio_runtime/framework/releases/{release}"
        self.framework_selector = (
            "schema_version = 1\n"
            f'manifest_sha256 = "{release}"\n'
            f'release = "{release}"\n'
            f'selected_release_root = "{legacy_relative}"\n'
            f'framework_engine_root = "{legacy_relative}/FRAMEWORK_ENGINE"\n'
            f'methodology_root = "{legacy_relative}/METHODOLOGY"\n'
            f'image_digest = "{retained_bootstrap_fixture.OLD_IMAGE}"\n'
        ).encode("utf-8")
        framework_current = self.root / ".caprmedio_runtime" / "framework" / "current.toml"
        framework_current.write_bytes(self.framework_selector)

    def test_bootstrap_reader_binds_raw_framework_tools_and_receipt_bytes(self) -> None:
        proof = publication_module._reopen_legacy_predecessor_context(
            self.root,
            package_selector=self.tools_selector,
            runtime_selector=self.framework_selector,
        )

        self.assertIsInstance(proof, LegacyBootstrapSourceProof)
        assert isinstance(proof, LegacyBootstrapSourceProof)
        receipt = self.root / self.fixture.original.proof_root / "evidence.toml"
        self.assertEqual(self.framework_selector, proof.framework_selector_bytes)
        self.assertEqual(self.tools_selector, proof.tool_selector_bytes)
        self.assertEqual(self.fixture.plan.release, proof.package_manifest_sha256)
        self.assertEqual(self.fixture.original.source_context_sha256, proof.source_context_sha256)
        self.assertEqual(retained_bootstrap_fixture.OLD_IMAGE, proof.image_digest)
        self.assertEqual(self.fixture.original.bootstrap_proof_key, proof.bootstrap_proof_key)
        self.assertEqual(receipt.read_bytes(), proof.raw_receipt_bytes)

    def test_changed_bootstrap_receipt_refuses_before_coverage(self) -> None:
        receipt = self.root / self.fixture.original.proof_root / "evidence.toml"
        original = receipt.read_bytes()
        receipt.write_bytes(original + b"# tampered\n")
        try:
            with self.assertRaises(PortableRuntimePublicationError) as refused:
                publication_module._reopen_legacy_predecessor_context(
                    self.root,
                    package_selector=self.tools_selector,
                    runtime_selector=self.framework_selector,
                )
            self.assertEqual("portable-publication-legacy-prior-context-unavailable", refused.exception.code)
        finally:
            receipt.write_bytes(original)


class NativePredecessorCoverageTests(unittest.TestCase):
    """D607 coverage comes only from a complete installed native predecessor."""

    @classmethod
    def setUpClass(cls) -> None:
        selected_native_fixture.NativeSelectedInstallationTests.setUpClass()

    def setUp(self) -> None:
        # This fixture creates actual D598/D599/D604/D600 carriers plus the
        # target's own Project selection.  Its original publication lock must
        # be released before this test obtains the replacement lock.
        import framework_installation_command as direct_command

        self.fixture = selected_native_fixture.NativeSelectedInstallationTests("runTest")
        captured: dict[str, object] = {}

        def retain_command(request: object):
            command = direct_command.run_framework_installation_command(request)
            captured["command"] = command
            return command

        with patch.object(selected_native_fixture, "run_framework_installation_command", side_effect=retain_command):
            self.fixture.setUp()
        command = captured.get("command")
        self.assertIsNotNone(command)
        closure = direct_command.prepare_direct_full_gate_effect_closure(
            command,
            full_gate_packet=self.fixture.packet,
        )
        recorded = direct_command.record_direct_installation_result(
            command,
            full_gate_effects=closure,
            state_generation=1,
            effect_outcome="completed",
            reason=None,
        )
        self.assertEqual("recorded", recorded["state"])
        self.fixture.doCleanups()
        self.root = self.fixture.target
        self.context = self.fixture.context
        self.package_selector = (self.root / ".caprmedio_install" / "current.toml").read_bytes()
        self.runtime_selector = (self.root / ".caprmedio_runtime" / "installation" / "current.toml").read_bytes()
        self.lock = InstallationPublicationLock(
            self.root,
            target_context_sha256=self.context.sha256,
            owner_run_id="native-predecessor-coverage-fixture",
            operation="install_framework_runtime",
            command_sha256="c" * 64,
        ).acquire()
        self.addCleanup(lambda: self.lock.active and self.lock.release("completed"))

    def _create_legacy_state_roots(self) -> None:
        for name in ("project_mcp", "mcp_hot_reload", "workflow_orchestrator"):
            carrier = self.root / ".caprmedio_install" / name / "state.txt"
            carrier.parent.mkdir(parents=True, exist_ok=True)
            carrier.write_bytes(f"preserve {name} state\n".encode("utf-8"))

    def test_native_predecessor_requires_actual_provider_quiescence_before_copy(self) -> None:
        """A real provider absence may copy; an unavailable query must block first."""

        self._create_legacy_state_roots()
        try:
            evidence = _prepare_legacy_replacement(
                self.root,
                target_context=self.context,
                old_package_selector=self.package_selector,
                old_execution_selector=(Path(".caprmedio_runtime/installation/current.toml"), self.runtime_selector),
                lock=self.lock,
            )
        except PortableRuntimePublicationError as blocked:
            self.assertEqual("portable-publication-native-quiescence-blocked", blocked.code)
            migration = self.root / ".caprmedio_runtime" / "installation" / "migrations" / self.lock.lock_generation
            self.assertTrue((migration / "inventory.toml").is_file())
            self.assertTrue((migration / "quiescence.toml").is_file())
            self.assertFalse((migration / "copy-proof.toml").exists())
            self.assertEqual(self.package_selector, (self.root / ".caprmedio_install" / "current.toml").read_bytes())
            self.assertEqual(
                self.runtime_selector,
                (self.root / ".caprmedio_runtime" / "installation" / "current.toml").read_bytes(),
            )
            return

        self.assertIsNotNone(evidence)
        assert evidence is not None
        self.addCleanup(lambda: _close_process_coverage(evidence.process_coverage, suppress_errors=True))

        migration = self.root / ".caprmedio_runtime" / "installation" / "migrations" / self.lock.lock_generation
        self.assertTrue((migration / "inventory.toml").is_file())
        self.assertTrue((migration / "quiescence.toml").is_file())
        self.assertTrue((migration / "copy-proof.toml").is_file())
        self.assertEqual(self.package_selector, (self.root / ".caprmedio_install" / "current.toml").read_bytes())
        self.assertEqual(
            self.runtime_selector,
            (self.root / ".caprmedio_runtime" / "installation" / "current.toml").read_bytes(),
        )
        self.assertTrue((migration / "staging" / "runtime" / "project_mcp" / "state.txt").is_file())

        prepared = SimpleNamespace(
            old_execution_selector=(Path(".caprmedio_runtime/installation/current.toml"), self.runtime_selector),
            old_package_selector=self.package_selector,
            legacy_replacement=evidence,
            target_context=self.context,
        )
        _revalidate_legacy_replacement(prepared, lock=self.lock)

    def test_native_predecessor_reopens_all_d604_carriers_before_coverage(self) -> None:
        """Digest-shaped D604 values cannot substitute for their physical carriers."""

        proof_path = self.root / ".caprmedio_runtime" / "installation" / "generations" / "1" / "release-proof.toml"
        original = proof_path.read_bytes()
        original_mode = proof_path.stat().st_mode & 0o777

        def changed_field(field: str, value: str) -> bytes:
            prefix = f'{field} = "'.encode("utf-8")
            start = original.index(prefix) + len(prefix)
            end = original.index(b'"', start)
            return original[:start] + value.encode("utf-8") + original[end:]

        def changed_digest(field: str) -> bytes:
            prefix = f'{field} = "'.encode("utf-8")
            start = original.index(prefix) + len(prefix)
            end = original.index(b'"', start)
            current = original[start:end].decode("ascii")
            replacement = ("0" if current[0] != "0" else "1") + current[1:]
            return changed_field(field, replacement)

        mutations = (
            ("missing-methodology-reference", changed_field("methodology_delivery_manifest_ref", "missing/delivery.toml")),
            ("command-digest", changed_digest("installation_command_sha256")),
            ("stage-digest", changed_digest("command_stage_manifest_sha256")),
            ("methodology-proof-digest", changed_digest("methodology_delivery_manifest_sha256")),
        )
        migration = self.root / ".caprmedio_runtime" / "installation" / "migrations" / self.lock.lock_generation
        for label, payload in mutations:
            with self.subTest(label=label):
                proof_path.write_bytes(payload)
                proof_path.chmod(original_mode)
                try:
                    with patch(
                        "legacy_process_coverage.open_legacy_process_coverage",
                        side_effect=AssertionError("coverage must not open after an invalid prior proof"),
                    ):
                        with self.assertRaises(PortableRuntimePublicationError) as refused:
                            _prepare_legacy_replacement(
                                self.root,
                                target_context=self.context,
                                old_package_selector=self.package_selector,
                                old_execution_selector=(
                                    Path(".caprmedio_runtime/installation/current.toml"), self.runtime_selector
                                ),
                                lock=self.lock,
                            )
                    self.assertEqual("portable-publication-native-prior-invalid", refused.exception.code)
                    self.assertFalse((migration / "inventory.toml").exists())
                    self.assertFalse((migration / "copy-proof.toml").exists())
                    self.assertEqual(self.package_selector, (self.root / ".caprmedio_install" / "current.toml").read_bytes())
                    self.assertEqual(
                        self.runtime_selector,
                        (self.root / ".caprmedio_runtime" / "installation" / "current.toml").read_bytes(),
                    )
                finally:
                    proof_path.write_bytes(original)
                    proof_path.chmod(original_mode)

    def test_rootless_native_quiescence_retains_safe_unknown_and_changed_outcomes(self) -> None:
        """D607v4 records each rootless outcome without fabricating D605 state."""

        predecessor_proof, frozen = publication_module._freeze_native_predecessor_handoff(
            self.root,
            package_selector=self.package_selector,
            runtime_selector=self.runtime_selector,
            lock=self.lock,
        )

        def coverage_with(*, first_state: str = "absent"):
            providers = [
                _RootlessNativeCoverageProvider(name, predecessor_proof, state=first_state if index == 0 else "absent")
                for index, name in enumerate(("project_mcp", "mcp_hot_reload", "workflow_orchestrator"))
            ]
            return providers, open_legacy_process_coverage(
                providers,
                target_context_sha256=self.context.sha256,
                predecessor_proof=predecessor_proof,
            )

        providers, coverage = coverage_with()
        try:
            safe_handoff = publication_module._retain_rootless_native_quiescence(
                frozen._with_coverage(predecessor_proof, coverage), target_context=self.context, lock=self.lock
            )
            retained = safe_handoff._native_quiescence
            self.assertIsNotNone(retained)
            assert retained is not None
            self.assertTrue(retained.safe)
            self.assertTrue(retained.path.is_file())
            self.assertFalse((self.root / ".caprmedio_runtime/installation/migrations").exists())
            publication_module._revalidate_rootless_native_quiescence(
                safe_handoff, target_context=self.context, lock=self.lock
            )
        finally:
            coverage.close()

        providers, coverage = coverage_with(first_state="unknown")
        try:
            with self.assertRaises(PortableRuntimePublicationError) as blocked:
                publication_module._retain_rootless_native_quiescence(
                    frozen._with_coverage(predecessor_proof, coverage), target_context=self.context, lock=self.lock
                )
            self.assertEqual("portable-publication-native-quiescence-blocked", blocked.exception.code)
        finally:
            coverage.close()

        providers, coverage = coverage_with()
        try:
            changed_handoff = publication_module._retain_rootless_native_quiescence(
                frozen._with_coverage(predecessor_proof, coverage), target_context=self.context, lock=self.lock
            )
            providers[0].state = "unknown"
            with self.assertRaises(PortableRuntimePublicationError) as changed:
                publication_module._revalidate_rootless_native_quiescence(
                    changed_handoff, target_context=self.context, lock=self.lock
                )
            self.assertEqual("portable-publication-native-quiescence-blocked", changed.exception.code)
        finally:
            coverage.close()

        carriers = list((self.root / ".caprmedio_runtime/installation/quiescence" / self.lock.lock_generation).rglob("quiescence.toml"))
        self.assertGreaterEqual(len(carriers), 3)
        self.assertEqual(self.package_selector, (self.root / ".caprmedio_install/current.toml").read_bytes())
        self.assertEqual(
            self.runtime_selector,
            (self.root / ".caprmedio_runtime/installation/current.toml").read_bytes(),
        )
        for name in ("project_mcp", "mcp_hot_reload", "workflow_orchestrator"):
            self.assertFalse((self.root / ".caprmedio_install" / name).exists())

    def _prepared_native_handoff(self):
        """Freeze the actual old N, with candidate admission as the test seam.

        The fixture has a complete O200 terminal and all final N carriers.  A
        new candidate D604 cannot be staged in this intentionally immutable
        predecessor fixture without creating a second action; the candidate
        reader is therefore the one explicit mock boundary below.  The old
        package/selectors/D600/D601/D604/command/start/detached Full Gate are
        always reopened from physical fixture carriers.
        """

        import native_installation_proof as native_proof
        import portable_methodology_installation as methodology

        predecessor_proof, handoff = publication_module._freeze_native_predecessor_handoff(
            self.root,
            package_selector=self.package_selector,
            runtime_selector=self.runtime_selector,
            lock=self.lock,
        )
        binding = handoff.binding
        candidate_delivery = object.__new__(methodology.CandidatePortableMethodologyDelivery)
        candidate_request = object.__new__(native_proof.CandidateNativeInstallationProofRequest)
        candidate_proof = object.__new__(native_proof.NativeInstallationProof)
        # The function requires identity, not reconstructed delivery facts.
        object.__setattr__(candidate_request, "methodology_delivery", candidate_delivery)
        old_proof = publication_module.tomllib.loads(
            (self.root / ".caprmedio_runtime" / "installation" / "generations" / "1" / "release-proof.toml").read_text(
                encoding="utf-8"
            )
        )
        object.__setattr__(
            candidate_proof,
            "methodology_delivery_manifest_ref",
            old_proof["methodology_delivery_manifest_ref"],
        )
        prepared = publication_module.PreparedNativePublication(
            package=self.fixture.package,
            target_context=self.context,
            candidate_proof_request=candidate_request,
            candidate_proof=candidate_proof,
            methodology_delivery=candidate_delivery,
            candidate_mcp_binding=object(),
            prospective_package_selector=b"candidate-package-selector",
            prospective_runtime_selector=b"candidate-runtime-selector",
            old_package_selector=self.package_selector,
            old_execution_selector=(Path(".caprmedio_runtime/installation/current.toml"), self.runtime_selector),
            native_predecessor=handoff,
            # A normal N->N successor may have no retained D605 state roots.
            # The handoff must remain valid without a migration record.
            legacy_replacement=None,
        )
        return prepared, binding, candidate_proof

    def test_selected_native_handoff_reopens_old_n_then_requires_candidate_d604(self) -> None:
        """Only a typed candidate D604 admission may replace old Methodology."""

        prepared, binding, candidate_proof = self._prepared_native_handoff()
        proof_path = self.root / ".caprmedio_runtime" / "installation" / "generations" / "1" / "release-proof.toml"
        original_proof = proof_path.read_bytes()
        original_mode = proof_path.stat().st_mode & 0o777
        with patch(
            "native_installation_proof.read_candidate_native_installation_proof",
            return_value=candidate_proof,
        ) as candidate_reader:
            reopened = publication_module.revalidate_prepared_native_predecessor(
                prepared, binding, lock=self.lock
            )
        self.assertEqual(binding, reopened)
        candidate_reader.assert_called_once_with(prepared.candidate_proof_request, lock=self.lock)
        self.assertEqual(self.package_selector, (self.root / ".caprmedio_install" / "current.toml").read_bytes())
        self.assertEqual(self.runtime_selector, (self.root / ".caprmedio_runtime" / "installation" / "current.toml").read_bytes())

        object.__setattr__(candidate_proof, "methodology_delivery_manifest_ref", "other/delivery-manifest.json")
        with patch(
            "native_installation_proof.read_candidate_native_installation_proof",
            return_value=candidate_proof,
        ):
            with self.assertRaises(PortableRuntimePublicationError) as wrong_output:
                publication_module.revalidate_prepared_native_predecessor(prepared, binding, lock=self.lock)
        self.assertEqual("portable-publication-native-handoff-candidate-invalid", wrong_output.exception.code)
        object.__setattr__(
            candidate_proof,
            "methodology_delivery_manifest_ref",
            publication_module.tomllib.loads(original_proof.decode("utf-8"))["methodology_delivery_manifest_ref"],
        )

        prefix = b'installation_command_sha256 = "'
        start = original_proof.index(prefix) + len(prefix)
        changed = b"0" if original_proof[start:start + 1] != b"0" else b"1"
        proof_path.write_bytes(original_proof[:start] + changed + original_proof[start + 1:])
        proof_path.chmod(original_mode)
        try:
            with patch(
                "native_installation_proof.read_candidate_native_installation_proof",
                side_effect=AssertionError("candidate D604 must not hide a changed old proof"),
            ):
                with self.assertRaises(PortableRuntimePublicationError) as refused:
                    publication_module.revalidate_prepared_native_predecessor(prepared, binding, lock=self.lock)
            self.assertEqual("portable-publication-native-handoff-stale", refused.exception.code)
            self.assertEqual(self.package_selector, (self.root / ".caprmedio_install" / "current.toml").read_bytes())
            self.assertEqual(self.runtime_selector, (self.root / ".caprmedio_runtime" / "installation" / "current.toml").read_bytes())
        finally:
            proof_path.write_bytes(original_proof)
            proof_path.chmod(original_mode)

    def test_selected_native_handoff_refuses_an_unminted_documentary_shape(self) -> None:
        """Only the physical freeze boundary may mint the Methodology exception."""

        prepared, binding, _candidate_proof = self._prepared_native_handoff()
        forged = object.__new__(publication_module._NativePredecessorHandoff)
        forged_prepared = replace(prepared, native_predecessor=forged)
        with patch(
            "native_installation_proof.read_candidate_native_installation_proof",
            side_effect=AssertionError("unminted handoff must fail before candidate D604"),
        ):
            with self.assertRaises(PortableRuntimePublicationError) as refused:
                publication_module.revalidate_prepared_native_predecessor(
                    forged_prepared, binding, lock=self.lock
                )
        self.assertEqual("portable-publication-native-handoff-unavailable", refused.exception.code)

    def test_coverage_closes_if_handoff_lock_revalidation_fails(self) -> None:
        """A coverage value not returned to the caller remains this frame's responsibility."""

        coverage = _TrackingCoverage()
        handoff_revalidation = False
        real_revalidate = self.lock.revalidate

        def revalidate() -> None:
            if handoff_revalidation:
                raise InstallationTransactionError("fixture-lock-stale", "handoff revalidation failed")
            real_revalidate()

        def open_coverage(*_args: object, **_kwargs: object) -> _TrackingCoverage:
            nonlocal handoff_revalidation
            handoff_revalidation = True
            return coverage

        with (
            patch("legacy_process_coverage.open_legacy_process_coverage", side_effect=open_coverage),
            patch.object(self.lock, "revalidate", side_effect=revalidate),
        ):
            with self.assertRaises(InstallationTransactionError):
                publication_module._open_predecessor_process_coverage(
                    self.root,
                    target_context=self.context,
                    old_package_selector=self.package_selector,
                    old_execution_selector=(Path(".caprmedio_runtime/installation/current.toml"), self.runtime_selector),
                    lock=self.lock,
                )

        self.assertEqual(1, coverage.close_calls)
        self.assertEqual(self.package_selector, (self.root / ".caprmedio_install" / "current.toml").read_bytes())
        self.assertEqual(
            self.runtime_selector,
            (self.root / ".caprmedio_runtime" / "installation" / "current.toml").read_bytes(),
        )

    def test_coverage_closes_if_postcopy_lock_revalidation_fails(self) -> None:
        """A copied migration has no returned owner until its final lock reopen passes."""

        coverage = _TrackingCoverage()
        inventory = {
            "inventory_sha256": "a" * 64,
            "legacy_selector_sha256": publication_module._digest(self.package_selector),
        }
        quiescence = {"quiescence_sha256": "b" * 64, "safe": True}
        copied: list[bool] = []
        predecessor_proof = object()

        def stage_copy(*_args: object, **_kwargs: object) -> dict[str, object]:
            copied.append(True)
            return {"copied": True}

        with (
            patch.object(
                publication_module,
                "_open_predecessor_process_coverage",
                return_value=(self.context.sha256, predecessor_proof, coverage, None),
            ),
            patch("installation_state.build_legacy_inventory", return_value=inventory),
            patch("installation_state.write_inventory"),
            patch("installation_state.read_inventory", return_value=inventory),
            patch("installation_state.prove_quiescence", return_value=quiescence),
            patch("installation_state.write_quiescence"),
            patch("installation_state.read_quiescence", return_value=quiescence),
            patch("installation_state.stage_legacy_copy", side_effect=stage_copy),
            patch("installation_state.verify_staged_copy"),
            patch.object(
                self.lock,
                "revalidate",
                side_effect=InstallationTransactionError("fixture-lock-stale", "post-copy revalidation failed"),
            ),
        ):
            with self.assertRaises(InstallationTransactionError):
                _prepare_legacy_replacement(
                    self.root,
                    target_context=self.context,
                    old_package_selector=self.package_selector,
                    old_execution_selector=(Path(".caprmedio_runtime/installation/current.toml"), self.runtime_selector),
                    lock=self.lock,
                )

        self.assertEqual([True], copied)
        self.assertEqual(1, coverage.close_calls)
        self.assertEqual(self.package_selector, (self.root / ".caprmedio_install" / "current.toml").read_bytes())
        self.assertEqual(
            self.runtime_selector,
            (self.root / ".caprmedio_runtime" / "installation" / "current.toml").read_bytes(),
        )


class MethodologyPublicationRouteTests(unittest.TestCase):
    """O200 and O169 retain distinct pre-delete Methodology facts."""

    def test_direct_target_and_selected_candidate_are_never_relabelled(self) -> None:
        import portable_methodology_installation as methodology

        candidate = object.__new__(methodology.PreparedCandidateMethodologyPublication)
        target = object.__new__(methodology.PreparedTargetMethodologyPublication)

        self.assertEqual(
            "candidate",
            publication_module._methodology_preparation_route(
                candidate,
                candidate_type=methodology.PreparedCandidateMethodologyPublication,
                target_type=methodology.PreparedTargetMethodologyPublication,
            ),
        )
        self.assertEqual(
            "target",
            publication_module._methodology_preparation_route(
                target,
                candidate_type=methodology.PreparedCandidateMethodologyPublication,
                target_type=methodology.PreparedTargetMethodologyPublication,
            ),
        )

    def test_untyped_methodology_preparation_refuses_before_any_effect(self) -> None:
        import portable_methodology_installation as methodology

        with self.assertRaises(PortableRuntimePublicationError) as refused:
            publication_module._methodology_preparation_route(
                object(),
                candidate_type=methodology.PreparedCandidateMethodologyPublication,
                target_type=methodology.PreparedTargetMethodologyPublication,
            )

        self.assertEqual("portable-publication-builder-invalid", refused.exception.code)


class DirectTargetPreparationRefusalTests(unittest.TestCase):
    """O200 target facts are rejected before any lock-owned carrier write."""

    def test_target_preparation_for_another_gate_refuses_before_root_open(self) -> None:
        import framework_installation
        import portable_methodology_installation as methodology
        import portable_runtime_materialization as materialization

        class Request:
            pass

        class Package:
            pass

        class Context:
            pass

        class Stage:
            pass

        class CandidatePreparation:
            pass

        class TargetPreparation:
            gate_receipt_sha256 = "c" * 64

        packet = SimpleNamespace(
            evidence=SimpleNamespace(
                receipt_sha256="a" * 64,
                candidate_image_digest="sha256:" + "b" * 64,
            )
        )
        request = Request()
        request.full_gate_packet = packet

        with (
            patch.object(framework_installation, "PortableInstallationRequest", Request),
            patch.object(materialization, "CandidateRuntimeCommandStageRequest", Stage),
            patch.object(methodology, "PreparedCandidateMethodologyPublication", CandidatePreparation),
            patch.object(methodology, "PreparedTargetMethodologyPublication", TargetPreparation),
            patch.object(publication_module, "VerifiedFrameworkPackage", Package),
            patch.object(publication_module, "TargetProjectContext", Context),
            patch.object(publication_module, "_root", side_effect=AssertionError("must not open the target root")),
        ):
            with self.assertRaises(PortableRuntimePublicationError) as refused:
                publication_module.build_prepared_native_publication(
                    request,
                    package=Package(),
                    target_context=Context(),
                    installation_command_sha256="d" * 64,
                    full_gate_packet=packet,
                    runtime_stage_request=Stage(),
                    methodology_preparation=TargetPreparation(),
                    state_generation=1,
                    old_package_selector=None,
                    old_execution_selector=None,
                    lock=object(),
                )

        self.assertEqual("portable-publication-builder-stale", refused.exception.code)


class RuntimeConfigurationPublicationTests(unittest.TestCase):
    """Configuration migration blocks before any candidate runtime carrier."""

    def test_malformed_existing_configuration_blocks_before_candidate_staging(self) -> None:
        import framework_installation
        import installation_context
        import portable_methodology_installation as methodology
        import portable_runtime_materialization as materialization
        temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)

        class Request:
            runtime_default_member = "defaults/framework.toml"

        class Package:
            pass

        class Context:
            sha256 = "b" * 64

        class Stage:
            pass

        class CandidatePreparation:
            gate_receipt_sha256 = "a" * 64

        class TargetPreparation:
            pass

        packet = SimpleNamespace(
            evidence=SimpleNamespace(
                receipt_sha256="a" * 64,
                candidate_image_digest="sha256:" + "c" * 64,
            )
        )
        request = Request()
        request.target = object()
        request.full_gate_packet = packet
        lock = SimpleNamespace(
            project_root=root,
            target_context_sha256=Context.sha256,
            command_sha256="d" * 64,
            lock_generation="e" * 32,
        )
        configuration = root / ".caprmedio_runtime" / "config.toml"
        configuration.parent.mkdir(parents=True, exist_ok=True)
        malformed = b"[runtime\ndefault =\n"
        configuration.write_bytes(malformed)
        staging = root / ".caprmedio_tmp" / "installation" / "staging" / lock.lock_generation

        with (
            patch.object(framework_installation, "PortableInstallationRequest", Request),
            patch.object(materialization, "CandidateRuntimeCommandStageRequest", Stage),
            patch.object(methodology, "PreparedCandidateMethodologyPublication", CandidatePreparation),
            patch.object(methodology, "PreparedTargetMethodologyPublication", TargetPreparation),
            patch.object(publication_module, "VerifiedFrameworkPackage", Package),
            patch.object(publication_module, "TargetProjectContext", Context),
            patch.object(publication_module, "_root", return_value=(lock, root)),
            patch.object(installation_context, "persist_target_project_context"),
            patch.object(
                materialization,
                "stage_candidate_runtime_command",
                side_effect=AssertionError("blocked configuration must prevent D601 staging"),
            ),
        ):
            with self.assertRaises(PortableRuntimePublicationError) as refused:
                publication_module.build_prepared_native_publication(
                    request,
                    package=Package(),
                    target_context=Context(),
                    installation_command_sha256="d" * 64,
                    full_gate_packet=packet,
                    runtime_stage_request=Stage(),
                    methodology_preparation=CandidatePreparation(),
                    state_generation=1,
                    old_package_selector=None,
                    old_execution_selector=None,
                    lock=lock,
                )

        self.assertEqual("portable-publication-config-invalid", refused.exception.code)
        self.assertEqual(malformed, configuration.read_bytes())
        self.assertFalse(staging.exists())
        self.assertFalse((root / ".caprmedio_install" / "current.toml").exists())
        self.assertFalse((root / ".caprmedio_runtime" / "installation" / "current.toml").exists())


class FinalNativePublicationReopenTests(unittest.TestCase):
    """The common publisher never returns on a failed final native reopen."""

    def test_final_proof_or_methodology_tamper_is_final_invalid_after_selection(self) -> None:
        import installed_mcp_binding
        import native_selected_installation

        class Package:
            manifest_digest = "a" * 64

        class Context:
            sha256 = "b" * 64

        class Binding:
            pass

        package = Package()
        context = Context()
        binding = Binding()
        selector = SimpleNamespace(
            package_manifest_sha256=package.manifest_digest,
            full_gate_receipt_sha256="c" * 64,
        )
        proof_request = SimpleNamespace(full_gate_packet=object())
        prepared = publication_module.PreparedNativePublication(
            package=package,
            target_context=context,
            candidate_proof_request=proof_request,
            candidate_proof=object(),
            methodology_delivery=object(),
            candidate_mcp_binding=binding,
            prospective_package_selector=b"candidate package selector",
            prospective_runtime_selector=b"candidate runtime selector",
            old_package_selector=None,
            old_execution_selector=None,
        )
        lock = SimpleNamespace(
            project_root=Path("/fixture"),
            target_context_sha256=context.sha256,
            revalidate=Mock(),
        )

        for rejected_code in (
            "native-selected-proof-invalid",
            "native-selected-methodology-delivery-invalid",
        ):
            with (
                self.subTest(rejected_code=rejected_code),
                patch.object(publication_module, "VerifiedFrameworkPackage", Package),
                patch.object(publication_module, "TargetProjectContext", Context),
                patch.object(publication_module, "_root", return_value=(lock, Path("/fixture"))),
                patch.object(publication_module, "verify_current_package_selector", return_value=selector),
                patch.object(publication_module, "stage_replacement_package", return_value=object()),
                patch.object(publication_module, "publish_final_generation_proof", return_value=Path("/fixture/proof.toml")),
                patch.object(publication_module, "_revalidate_legacy_replacement"),
                patch.object(publication_module, "_revalidate_ca_skill_publication"),
                patch.object(publication_module, "publish_replacement_package", return_value=package),
                patch.object(publication_module, "publish_selectors", return_value=("d" * 64, "e" * 64)) as publish_selectors,
                patch.object(installed_mcp_binding, "InstalledMcpBinding", Binding),
                patch.object(installed_mcp_binding, "admit_candidate_mcp_binding", return_value=binding),
                patch.object(installed_mcp_binding, "admit_installed_mcp_binding", return_value=binding),
                patch.object(
                    native_selected_installation,
                    "reopen_current_native_installation",
                    side_effect=native_selected_installation.NativeSelectedInstallationError(
                        rejected_code, "final carrier was tampered"
                    ),
                ) as reopen,
            ):
                with self.assertRaises(PortableRuntimePublicationError) as refused:
                    publication_module._publish_prepared_native_runtime(prepared, lock=lock)

            self.assertEqual("portable-publication-final-invalid", refused.exception.code)
            publish_selectors.assert_called_once()
            reopen.assert_called_once_with(
                lock.project_root,
                package,
                proof_request.full_gate_packet,
                target_context_sha256=context.sha256,
            )
            lock.revalidate.assert_not_called()

    def test_final_invalid_is_recorded_uncertain_not_completed(self) -> None:
        import framework_installation_command

        temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        package_selector = root / ".caprmedio_install" / "current.toml"
        runtime_selector = root / ".caprmedio_runtime" / "installation" / "current.toml"
        package_selector.parent.mkdir(parents=True)
        runtime_selector.parent.mkdir(parents=True)
        package_selector.write_bytes(b"selected package")
        runtime_selector.write_bytes(b"selected runtime")
        prepared = publication_module.PreparedNativePublication(
            package=SimpleNamespace(manifest_digest="a" * 64),
            target_context=object(),
            candidate_proof_request=SimpleNamespace(full_gate_packet=object()),
            candidate_proof=SimpleNamespace(state_generation=1),
            methodology_delivery=object(),
            candidate_mcp_binding=object(),
            prospective_package_selector=b"candidate package selector",
            prospective_runtime_selector=b"candidate runtime selector",
            old_package_selector=b"old package selector",
            old_execution_selector=None,
        )
        lock = SimpleNamespace(release=Mock())
        failure = PortableRuntimePublicationError(
            "portable-publication-final-invalid", "final proof was tampered"
        )

        with (
            patch.object(
                framework_installation_command,
                "prepare_direct_full_gate_effect_closure",
                return_value=object(),
            ),
            patch.object(publication_module, "publish_direct_native_runtime", side_effect=failure),
            patch.object(publication_module, "_root", return_value=(lock, root)),
            patch.object(
                publication_module,
                "record_direct_publication_result",
                return_value={"state": "recorded"},
            ) as record,
        ):
            result = publication_module.execute_direct_native_runtime(object(), prepared, lock=lock)

        self.assertIsNone(result.publication)
        self.assertEqual({"state": "recorded"}, result.recording)
        self.assertEqual("effect_uncertain", record.call_args.kwargs["effect_outcome"])
        self.assertEqual("portable-publication-final-invalid", record.call_args.kwargs["reason"])
        lock.release.assert_called_once_with("blocked")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
