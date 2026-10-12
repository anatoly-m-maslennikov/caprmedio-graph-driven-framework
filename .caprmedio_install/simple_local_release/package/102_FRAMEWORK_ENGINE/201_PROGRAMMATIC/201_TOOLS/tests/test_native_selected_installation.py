"""Physical final-carrier coverage for the selected-native reader."""

from __future__ import annotations

import shutil
import sys
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1]
RELEASE_ROOT = TOOLS / "RELEASE_VERSION"
RELEASE_TEST_ROOT = RELEASE_ROOT / "tests"
for path in (TOOLS, Path(__file__).resolve().parent, RELEASE_ROOT, RELEASE_TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import test_native_installation_proof as proof_fixture  # noqa: E402
import test_portable_release_full_gate as full_gate_fixture  # noqa: E402
from framework_installation_command import (  # noqa: E402
    FrameworkInstallationCommandRequest,
    run_framework_installation_command,
)
from framework_installation import PortableInstallationRequest  # noqa: E402
from framework_package import (  # noqa: E402
    provide_installation_package_evidence,
    verify_current_package_selector,
    verify_framework_package,
)
from installation_context import (  # noqa: E402
    TargetProjectRequest,
    bind_target_project_context,
    persist_target_project_context,
)
from installation_transaction import InstallationPublicationLock  # noqa: E402
from portable_package_fixture import exporter  # noqa: E402
from release_handoff import CANONICAL_SOURCE_RELATIVE  # noqa: E402
from release_retained_candidate import read_retained_candidate_identity  # noqa: E402
from retained_full_gate_packet import RetainedNativeFullGatePacket  # noqa: E402
from native_installation_proof import (  # noqa: E402
    CandidateNativeInstallationProofRequest,
    stage_candidate_native_installation_proof,
)
from native_selected_installation import (  # noqa: E402
    NativeSelectedInstallationError,
    reopen_current_native_installation,
)
from portable_runtime_materialization import (  # noqa: E402
    CandidateRuntimeCommandStageRequest,
    stage_candidate_runtime_command,
)
import portable_methodology_installation as methodology  # noqa: E402


_O200_SOURCE_RELATIVE = (
    Path(CANONICAL_SOURCE_RELATIVE)
    / "003_PROJECT_CONFIGURATION"
    / "09_operations"
    / "CA-O-200-PROJECT_CONFIGURATION-ACTION--install-one-admitted-project-runtime.md"
)
_DEFAULT_SETTINGS_RELATIVE = Path(
    "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/"
    "caprmedio_framework_default_settings.toml"
)


class _O200NativeHappyPathFixture(full_gate_fixture._NativeHappyPathFixture):
    """Retain the canonical O200 Methodology source before package sealing."""

    def _seed_project(self, extra_engine_members: dict[str, bytes]) -> None:
        super()._seed_project(extra_engine_members)
        source = full_gate_fixture.PROJECT_ROOT / _O200_SOURCE_RELATIVE
        self.write(_O200_SOURCE_RELATIVE.as_posix(), source.read_bytes(), source.stat().st_mode & 0o777)

    def _export(self) -> None:
        manifest = exporter.freeze_methodology_manifest(
            source_root=self.source,
            selected_atoms=[
                {"atom_id": "CA-R-001", "version": 1},
                {"atom_id": "CA-M-002", "version": 1},
                {"atom_id": "CA-O-200", "version": 1},
            ],
            support_inventory=[{
                "path": self.support.relative_to(self.source).as_posix(),
                "sha256": proof_fixture._sha256(self.support.read_bytes()),
            }],
            catalog_pins=[],
            project_root=self.root,
        )
        frozen = self.write("freeze/manifest.json", exporter.frozen_manifest_bytes(manifest))
        exporter.export_selected_methodology(
            source_root=self.source,
            frozen_manifest_path=frozen,
            release_candidate_root=self.candidate_root,
            project_root=self.root,
        )


class NativeSelectedInstallationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        fixture = _O200NativeHappyPathFixture()
        packet_fixture = proof_fixture._detached_native_full_gate_fixture.DetachedNativeFullGateTests()
        (
            proof_fixture.CandidateNativeInstallationProofTests._source_archive,
            proof_fixture.CandidateNativeInstallationProofTests._source_identity,
            proof_fixture.CandidateNativeInstallationProofTests._suite,
            proof_fixture.CandidateNativeInstallationProofTests._build,
            proof_fixture.CandidateNativeInstallationProofTests._verification,
            proof_fixture.CandidateNativeInstallationProofTests._e2e,
            proof_fixture.CandidateNativeInstallationProofTests._full,
        ) = packet_fixture._packet(fixture)

    def setUp(self) -> None:
        self.fixture = proof_fixture.CandidateNativeInstallationProofTests("runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.target, self.target_request = self._alpha_target()
        self.context = bind_target_project_context(self.target_request)
        command = run_framework_installation_command(
            FrameworkInstallationCommandRequest(
                target=self.target_request,
                target_context=self.context,
                package=self.candidate_package,
                full_gate_receipt_sha256=self.packet.evidence.receipt_sha256,
                command_id="native-selected-installation-fixture",
                operator="Anatoly Maslennikov",
            )
        )
        self.addCleanup(command.action_session.close)
        run_id = command.action_start.get("run_id")
        self.assertIsInstance(run_id, str)
        self.assertEqual(run_id, command.action_provenance.action_run_id)
        self.assertEqual(command.command_receipt.sha256, command.action_session.actual[run_id]["intent"]["installation_command_sha256"])
        lock = InstallationPublicationLock(
            self.target,
            target_context_sha256=command.target_context.sha256,
            owner_run_id=run_id,
            operation="install-framework-runtime",
            command_sha256=command.command_receipt.sha256,
        ).acquire()
        self.addCleanup(lambda: lock.active and lock.release("completed"))
        self.context = command.target_context
        context_path = persist_target_project_context(self.target_request, self.context, lock=lock)
        self.assertEqual(
            self.target / ".caprmedio_runtime/installation/contexts" / f"{self.context.sha256}.toml",
            context_path,
        )
        request = self._candidate_stage_request()
        stage = stage_candidate_runtime_command(request, lock=lock)
        delivery = self._publish_candidate_methodology_delivery(
            lock=lock,
            prospective_package_selector=request.prospective_package_selector,
        )
        proof_request = CandidateNativeInstallationProofRequest(
            package=self.candidate_package, target_context=self.context, command_stage=stage,
            prospective_package_selector=request.prospective_package_selector,
            prospective_selector=self._runtime_selector(lock), full_gate_packet=request.full_gate_packet,
            methodology_delivery=delivery,
        )
        self.proof = stage_candidate_native_installation_proof(proof_request, lock=lock)
        self.assertEqual(command.command_receipt.sha256, self.proof.installation_command_sha256)
        release = self.target / ".caprmedio_install/releases" / self.candidate_package.manifest_digest
        release.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(self.candidate_package.root, release)
        (self.target / ".caprmedio_install/current.toml").write_bytes(request.prospective_package_selector)
        current = self.target / ".caprmedio_runtime/installation/current.toml"
        current.parent.mkdir(parents=True, exist_ok=True)
        current.write_bytes(proof_request.prospective_selector)
        final = self.target / ".caprmedio_runtime/installation/generations/1"
        final.mkdir(parents=True)
        shutil.copyfile(self.proof.proof_path, final / "release-proof.toml")
        for name in ("command.toml", "environment.toml", "wrapper", "stage-manifest.toml"):
            shutil.copyfile(stage.root / name, final / name)
        for name in ("command.toml", "environment.toml", "stage-manifest.toml", "release-proof.toml"):
            (final / name).chmod(0o600)
        (final / "wrapper").chmod(0o700)
        self.package = verify_framework_package(release)

    def _alpha_target(self) -> tuple[Path, TargetProjectRequest]:
        """Bind the final reader fixture to a distinct, actual target control."""

        target = self.fixture.target.parent / "alpha-target"
        target.mkdir()
        artifact_root = target / ".caprmedio_tmp" / "retained-packet"
        shutil.copytree(self.fixture.artifact_root, artifact_root)
        descriptor = artifact_root / self.fixture.identity.descriptor_path.relative_to(self.fixture.artifact_root)
        sidecar = artifact_root / self.fixture.identity.package_evidence.receipt_path.relative_to(
            self.fixture.artifact_root
        )
        candidate_root = artifact_root / self.fixture.identity.package_evidence.view.package_root.relative_to(
            self.fixture.artifact_root
        )
        identity = read_retained_candidate_identity(
            descriptor,
            expected_sha256=self.fixture.identity.descriptor_sha256,
            package_root=candidate_root,
            sidecar_path=sidecar,
            expected_sidecar_sha256=self.fixture.identity.package_evidence.receipt_sha256,
        )
        self.candidate_package = verify_framework_package(candidate_root)
        self.packet = RetainedNativeFullGatePacket(
            artifact_root=artifact_root,
            retained_candidate=identity,
            suite=self.fixture._suite,
            build=self.fixture._build,
            verification=self.fixture._verification,
            e2e=self.fixture._e2e,
            evidence=self.fixture._full,
        )
        self.path = target / "bin"
        self.home = target / "home"
        self.path.mkdir()
        self.home.mkdir()
        control = target / ".caprmedio_alpha"
        control.mkdir()
        package_evidence = provide_installation_package_evidence(self.candidate_package.root)
        configurations = tuple(pin for pin in package_evidence.source_pins if pin.kind == "configuration")
        self.assertEqual(1, len(configurations), "the retained candidate must admit one selected Project Configuration")
        configuration = configurations[0]
        (control / "caprmedio_project_settings.toml").write_text(
            "[project]\n"
            'name = "alpha"\n\n'
            "[paths]\n"
            'control_root = ".caprmedio_alpha"\n'
            'journal_root = ".caprmedio_alpha/_journal"\n'
            'runtime_root = ".caprmedio_runtime"\n',
            encoding="utf-8",
        )
        (control / "project_structure.toml").write_text(
            "schema_version = 1\n"
            "\n"
            "[[scope_units]]\n"
            'scope_unit_name = "METHODOLOGY_SOURCES"\n'
            'authority_path = ".caprmedio_alpha/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources"\n'
            'delivery_path = ".caprmedio_alpha/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"\n',
            encoding="utf-8",
        )
        shutil.copy2(
            self.fixture.control / "operators_registry.toml",
            control / "operators_registry.toml",
        )
        # This is the target's own D359 control input, created before D600
        # binding from the actual retained package pin.  It never changes the
        # sealed candidate package, catalog, or authoring source.
        framework = control / "000_CAPRMEDIO_framework"
        framework.mkdir()
        default_source = (
            full_gate_fixture.PROJECT_ROOT
            / ".caprmedio_caprmedio"
            / _DEFAULT_SETTINGS_RELATIVE
        )
        default_target = control / _DEFAULT_SETTINGS_RELATIVE
        default_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(default_source, default_target)
        (framework / "caprmedio_framework_settings.toml").write_text(
            "[methodology.configuration]\n"
            f'identity = "{configuration.identity}"\n'
            f'revision = "{configuration.revision}"\n',
            encoding="utf-8",
        )
        request = TargetProjectRequest(
            target_root=target,
            control_child=control.name,
            mode="bootstrap",
            target_project_identity="alpha",
            settings_path=control / "caprmedio_project_settings.toml",
            project_structure_path=control / "project_structure.toml",
            operators_registry_path=control / "operators_registry.toml",
            repository_identity=False,
            root_locator="fixtures/native-selected-alpha",
            package_root=self.candidate_package.root,
            package_evidence=package_evidence,
        )
        return target, request

    def _publish_candidate_methodology_delivery(self, *, lock: InstallationPublicationLock,
                                                prospective_package_selector: bytes):
        """Publish the actual retained candidate Methodology for Alpha before D604 proofing."""

        request = PortableInstallationRequest(
            target=self.target_request,
            retained_gate_receipt_path=self.packet.artifact_root / self.packet.evidence.evidence_root / "receipt.json",
            full_gate_packet=self.packet,
        )
        selector = verify_current_package_selector(
            prospective_package_selector,
            self.candidate_package,
        )
        prepared = methodology.prepare_candidate_portable_methodology_publication(
            request,
            package=self.candidate_package,
            target_context=self.context,
            prospective_selector=selector,
        )
        return methodology.publish_prepared_candidate_portable_methodology(
            request,
            prepared,
            package=self.candidate_package,
            target_context=self.context,
            prospective_selector=selector,
            lock=lock,
        )

    def _candidate_stage_request(self) -> CandidateRuntimeCommandStageRequest:
        return CandidateRuntimeCommandStageRequest(
            package=self.candidate_package,
            target_context=self.context,
            prospective_package_selector=self._package_selector(),
            full_gate_packet=self.packet,
            state_generation=1,
            entrypoint=next(
                row.path
                for row in self.candidate_package.inventory
                if row.role == "engine" and row.path.endswith(".py")
            ),
            fixed_arguments=(),
            invocation_nonce="native-selected-installation-fixture",
            path_directories=(self.path,),
            home=self.home,
        )

    def _package_selector(self) -> bytes:
        return (
            "\n".join(
                (
                    "schema_version = 1",
                    f'package_manifest_sha256 = "{self.candidate_package.manifest_digest}"',
                    f'release_relpath = "releases/{self.candidate_package.manifest_digest}"',
                    f'framework_version = "{self.candidate_package.framework_version}"',
                    f'version_toml_sha256 = "{self.candidate_package.version_toml_sha256}"',
                    f'source_catalog_sha256 = "{self.candidate_package.source_catalog_sha256}"',
                    f'full_gate_receipt_sha256 = "{self.packet.evidence.receipt_sha256}"',
                    f'image_digest = "{self.packet.evidence.candidate_image_digest.removeprefix("sha256:")}"',
                    "",
                )
            )
        ).encode("utf-8")

    def _runtime_selector(self, lock: InstallationPublicationLock) -> bytes:
        return (
            "\n".join(
                (
                    "schema_version = 1",
                    f'package_manifest_sha256 = "{self.candidate_package.manifest_digest}"',
                    f'target_project_context_sha256 = "{self.context.sha256}"',
                    "state_generation = 1",
                    f'installation_lock_generation = "{lock.lock_generation}"',
                    f'image_digest = "{self.packet.evidence.candidate_image_digest.removeprefix("sha256:")}"',
                    "",
                )
            )
        ).encode("utf-8")

    def _read(self):
        return reopen_current_native_installation(
            self.target, self.package, self.packet,
            target_context_sha256=self.context.sha256,
        )

    def test_reopens_complete_final_native_carriers(self) -> None:
        selected = self._read()
        self.assertEqual(self.package.manifest_digest, selected.package_manifest_sha256)
        self.assertEqual(1, selected.state_generation)

    def test_refuses_tampered_final_proof(self) -> None:
        proof = self.target / ".caprmedio_runtime/installation/generations/1/release-proof.toml"
        proof.write_bytes(proof.read_bytes().replace(b'framework_version = ', b'framework_version = "forged" # '))
        with self.assertRaises(NativeSelectedInstallationError):
            self._read()

    def test_refuses_tampered_context_or_selector(self) -> None:
        context = self.target / ".caprmedio_runtime/installation/contexts" / f"{self.context.sha256}.toml"
        context.write_bytes(context.read_bytes() + b"forged = true\n")
        with self.assertRaises(NativeSelectedInstallationError):
            self._read()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
