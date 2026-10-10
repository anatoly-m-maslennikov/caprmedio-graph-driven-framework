"""Synthetic D604 native-proof staging coverage with physical package carriers."""

from __future__ import annotations

import hashlib
import json
from dataclasses import replace
from pathlib import Path
import shlex
import shutil
import sys
import tempfile
import tomllib
import unittest


TOOLS = Path(__file__).resolve().parents[1]
RELEASE_ROOT = TOOLS / "RELEASE_VERSION"
RELEASE_TEST_ROOT = RELEASE_ROOT / "tests"
TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
for candidate in (TOOLS, Path(__file__).resolve().parent, RELEASE_ROOT, RELEASE_TEST_ROOT):
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))

import test_portable_runtime_materialization as command_fixture  # noqa: E402
import test_native_proof_delivery as delivery_fixture  # noqa: E402
from framework_installation import PortableInstallationRequest  # noqa: E402
import portable_methodology_installation as methodology  # noqa: E402
from native_installation_proof import (  # noqa: E402
    CandidateNativeInstallationProofRequest,
    NativeInstallationProofError,
    NativeInstallationProofRequest,
    read_candidate_native_installation_proof,
    read_native_installation_proof,
    stage_candidate_native_installation_proof,
    stage_native_installation_proof,
)
from framework_package import provide_installation_package_evidence, verify_framework_package  # noqa: E402
from installation_context import TargetProjectRequest, bind_target_project_context  # noqa: E402
from installation_transaction import InstallationPublicationLock  # noqa: E402
from portable_runtime_materialization import (  # noqa: E402
    CandidateRuntimeCommandStageRequest,
    PortableRuntimeMaterializationError,
    stage_candidate_runtime_command,
    stage_runtime_command,
)
from release_retained_candidate import read_retained_candidate_identity  # noqa: E402
from retained_full_gate_packet import RetainedNativeFullGatePacket  # noqa: E402
import test_detached_native_full_gate as _detached_native_full_gate_fixture  # noqa: E402


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


class NativeInstallationProofTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = delivery_fixture.DeliveryRuntimeFixture("runTest")
        self.fixture.setUp()
        self.target = self.fixture.target
        self.package = self.fixture.package
        self.context = self.fixture.context

    def _stage(self):
        lock = self.fixture._lock()
        self.addCleanup(lambda: lock.active and lock.release("completed"))
        command_stage = stage_runtime_command(self.fixture._request(), lock=lock)
        self.delivery = delivery_fixture.physical_delivery(self.fixture, lock)
        return lock, command_stage

    def _selector(
        self,
        lock,
        *,
        context_sha256: str | None = None,
        image_digest: str | None = None,
        state_generation: object = 1,
    ) -> bytes:
        selected_image = image_digest or "b" * 64
        rendered_generation = str(state_generation).lower() if isinstance(state_generation, bool) else state_generation
        return (
            "\n".join(
                (
                    "schema_version = 1",
                    f'package_manifest_sha256 = "{self.package.manifest_digest}"',
                    f'target_project_context_sha256 = "{context_sha256 or self.context.sha256}"',
                    f"state_generation = {rendered_generation}",
                    f'installation_lock_generation = "{lock.lock_generation}"',
                    f'image_digest = "{selected_image}"',
                    "",
                )
            )
        ).encode("utf-8")

    def _request(self, lock, command_stage, **changes: object) -> NativeInstallationProofRequest:
        values: dict[str, object] = {
            "package": self.package,
            "target_context": self.context,
            "command_stage": command_stage,
            "prospective_selector": self._selector(lock),
            "methodology_delivery": self.delivery,
        }
        values.update(changes)
        return NativeInstallationProofRequest(**values)

    def test_stages_and_reopens_exact_prospective_proof_without_runtime_effects(self) -> None:
        lock, command_stage = self._stage()
        request = self._request(lock, command_stage)
        proof = stage_native_installation_proof(request, lock=lock)

        self.assertEqual(proof.root, self.target / ".caprmedio_tmp" / "installation" / "proofs" / lock.lock_generation)
        self.assertEqual(proof.package_manifest_sha256, self.package.manifest_digest)
        self.assertEqual(proof.target_project_context_sha256, self.context.sha256)
        self.assertEqual(proof.state_generation, 1)
        self.assertEqual(proof.installation_lock_generation, lock.lock_generation)
        self.assertEqual(proof.installation_command_sha256, "c" * 64)
        self.assertEqual(proof.command_sha256, command_stage.command_sha256)
        self.assertEqual(proof.command_stage_manifest_sha256, _sha256(command_stage.manifest_path.read_bytes()))
        self.assertEqual(proof.selector_sha256, _sha256(request.prospective_selector))
        self.assertEqual(proof.selector_path.read_bytes(), request.prospective_selector)
        document = tomllib.loads(proof.proof_path.read_text(encoding="utf-8"))
        self.assertEqual(
            set(document),
            {
                "schema_version", "package_manifest_sha256", "framework_version", "version_toml_sha256",
                "source_catalog_sha256", "full_gate_receipt_sha256", "image_digest", "target_project_context_sha256",
                "state_generation", "installation_lock_generation", "installation_command_sha256", "command_sha256",
                "command_stage_manifest_sha256", "selector_sha256",
                "methodology_delivery_manifest_ref", "methodology_delivery_manifest_sha256",
            },
        )
        self.assertEqual(2, document["schema_version"])
        self.assertEqual(_sha256(self.delivery.delivery_manifest_path.read_bytes()), proof.methodology_delivery_manifest_sha256)
        self.assertNotEqual(self.delivery.delivery_manifest_sha256, proof.methodology_delivery_manifest_sha256)
        self.assertEqual(read_native_installation_proof(request, lock=lock), proof)
        self.assertFalse((self.target / ".caprmedio_runtime" / "installation" / "current.toml").exists())
        self.assertFalse((self.target / ".caprmedio_runtime" / "config.toml").exists())
        self.assertFalse((self.target / ".caprmedio_runtime" / "installation" / "generations" / "1" / "process.toml").exists())
        self.assertEqual(proof.proof_path.stat().st_mode & 0o777, 0o600)
        self.assertEqual(proof.selector_path.stat().st_mode & 0o777, 0o600)

    def test_refuses_mismatched_image_before_proof_stage_write(self) -> None:
        lock, command_stage = self._stage()
        request = self._request(lock, command_stage, prospective_selector=self._selector(lock, image_digest="f" * 64))
        with self.assertRaisesRegex(NativeInstallationProofError, "native-proof-prospective-selector-mismatch"):
            stage_native_installation_proof(request, lock=lock)
        self.assertFalse((self.target / ".caprmedio_tmp" / "installation" / "proofs" / lock.lock_generation).exists())

    def test_refuses_untyped_delivery_before_proof_stage_write(self) -> None:
        lock, command_stage = self._stage()
        request = self._request(lock, command_stage, methodology_delivery=True)
        with self.assertRaisesRegex(NativeInstallationProofError, "native-proof-delivery-untrusted"):
            stage_native_installation_proof(request, lock=lock)
        self.assertFalse((self.target / ".caprmedio_tmp/installation/proofs" / lock.lock_generation).exists())

    def test_refuses_resealed_selection_before_proof_stage_write(self) -> None:
        from installation_transaction import InstallationPublicationLock
        forged = replace(self.context, methodology_source_identities=("core-methodology",))
        carrier = self.target / ".caprmedio_runtime/installation/contexts" / f"{forged.sha256}.toml"
        carrier.write_bytes(forged.with_digest_toml())
        lock = InstallationPublicationLock(self.target, target_context_sha256=forged.sha256,
            owner_run_id="forged-selection-proof", operation="native-proof-stage", command_sha256="c" * 64).acquire()
        self.addCleanup(lambda: lock.active and lock.release("completed"))
        request = NativeInstallationProofRequest(package=self.package, target_context=forged,
            command_stage=None, prospective_selector=self._selector(lock, context_sha256=forged.sha256),
            methodology_delivery=None)
        with self.assertRaisesRegex(NativeInstallationProofError, "native-proof-context-invalid") as refused:
            stage_native_installation_proof(request, lock=lock)
        self.assertIn("target Methodology selection changed", str(refused.exception.__context__))
        self.assertFalse((self.target / ".caprmedio_tmp/installation/proofs" / lock.lock_generation).exists())

    def test_reader_refuses_tampered_command_stage(self) -> None:
        lock, command_stage = self._stage()
        request = self._request(lock, command_stage)
        stage_native_installation_proof(request, lock=lock)
        command_stage.command_path.write_bytes(b"schema_version = 1\n")
        with self.assertRaisesRegex(NativeInstallationProofError, "native-proof-command-stage-invalid"):
            read_native_installation_proof(request, lock=lock)

    def test_refuses_boolean_native_selector_generation(self) -> None:
        lock, command_stage = self._stage()
        request = self._request(lock, command_stage, prospective_selector=self._selector(lock, state_generation=True))
        with self.assertRaisesRegex(NativeInstallationProofError, "native-proof-prospective-selector-invalid"):
            stage_native_installation_proof(request, lock=lock)
        self.assertFalse((self.target / ".caprmedio_tmp" / "installation" / "proofs" / lock.lock_generation).exists())

    def test_refuses_forged_persisted_context_semantics_before_proof_write(self) -> None:
        forged_values = (
            {"mode": "forged"},
            {"settings_sha256": "g" * 64},
            {"control_child_relpath": ".caprmedio_"},
            {"root_locator": "../outside"},
        )
        for number, changes in enumerate(forged_values):
            with self.subTest(changes=changes):
                forged = replace(self.context, **changes)
                context_path = (
                    self.target / ".caprmedio_runtime" / "installation" / "contexts" / f"{forged.sha256}.toml"
                )
                context_path.write_bytes(forged.with_digest_toml())
                lock = InstallationPublicationLock(
                    self.target,
                    target_context_sha256=forged.sha256,
                    owner_run_id=f"native-proof-forged-{number}",
                    operation="native-proof-stage",
                    command_sha256="d" * 64,
                ).acquire()
                try:
                    command_stage = stage_runtime_command(self.fixture._request(target_context=forged), lock=lock)
                    self.delivery = delivery_fixture.physical_delivery(self.fixture, lock)
                    request = self._request(
                        lock,
                        command_stage,
                        target_context=forged,
                        prospective_selector=self._selector(lock, context_sha256=forged.sha256),
                    )
                    with self.assertRaisesRegex(NativeInstallationProofError, "native-proof-context-invalid"):
                        stage_native_installation_proof(request, lock=lock)
                    self.assertFalse(
                        (self.target / ".caprmedio_tmp" / "installation" / "proofs" / lock.lock_generation).exists()
                    )
                finally:
                    if lock.active:
                        lock.release("completed")

    def test_refuses_second_proof_without_overwriting_prior_bytes(self) -> None:
        lock, command_stage = self._stage()
        request = self._request(lock, command_stage)
        proof = stage_native_installation_proof(request, lock=lock)
        original = {path.name: path.read_bytes() for path in (proof.proof_path, proof.selector_path)}
        with self.assertRaisesRegex(NativeInstallationProofError, "native-proof-conflict"):
            stage_native_installation_proof(request, lock=lock)
        self.assertEqual({path.name: path.read_bytes() for path in (proof.proof_path, proof.selector_path)}, original)


class CandidateNativeInstallationProofTests(unittest.TestCase):
    """Use an actual retained D597 Full Gate packet before selector publication."""

    @classmethod
    def setUpClass(cls) -> None:
        fixture = _detached_native_full_gate_fixture.DetachedNativeFullGateTests()
        (
            cls._source_archive,
            cls._source_identity,
            cls._suite,
            cls._build,
            cls._verification,
            cls._e2e,
            cls._full,
        ) = fixture._packet()

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, delete=False)
        self.target = Path(self.temporary.name) / "target"
        self.target.mkdir()
        self.artifact_root = self.target / ".caprmedio_tmp" / "retained-packet"
        shutil.copytree(self._source_archive, self.artifact_root)
        descriptor = self.artifact_root / self._source_identity.descriptor_path.relative_to(self._source_archive)
        sidecar = self.artifact_root / self._source_identity.package_evidence.receipt_path.relative_to(
            self._source_archive
        )
        candidate_root = self.artifact_root / self._source_identity.package_evidence.view.package_root.relative_to(
            self._source_archive
        )
        self.identity = read_retained_candidate_identity(
            descriptor,
            expected_sha256=self._source_identity.descriptor_sha256,
            package_root=candidate_root,
            sidecar_path=sidecar,
            expected_sidecar_sha256=self._source_identity.package_evidence.receipt_sha256,
        )
        self.package = verify_framework_package(candidate_root)
        control_source = self.artifact_root / ".caprmedio_caprmedio"
        self.control = self.target / control_source.name
        self.control.mkdir()
        for name in ("caprmedio_project_settings.toml", "project_structure.toml", "operators_registry.toml"):
            shutil.copy2(control_source / name, self.control / name)
        from target_methodology_selection import FRAMEWORK_INSTANCE_SETTINGS_RELATIVE
        settings_source = control_source / FRAMEWORK_INSTANCE_SETTINGS_RELATIVE
        settings_target = self.control / FRAMEWORK_INSTANCE_SETTINGS_RELATIVE
        settings_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(settings_source, settings_target)
        settings = tomllib.loads((self.control / "caprmedio_project_settings.toml").read_text(encoding="utf-8"))
        project = settings["project"]
        self.assertIsInstance(project, dict)
        self.assertIsInstance(project.get("name"), str)
        self.target_request = TargetProjectRequest(
                target_root=self.target,
                control_child=self.control.name,
                mode="bootstrap",
                target_project_identity=project["name"],
                settings_path=self.control / "caprmedio_project_settings.toml",
                project_structure_path=self.control / "project_structure.toml",
                operators_registry_path=self.control / "operators_registry.toml",
                repository_identity=False,
                root_locator="fixtures/candidate-native-proof",
                package_root=self.package.root,
                package_evidence=provide_installation_package_evidence(self.package.root),
            )
        self.context = bind_target_project_context(self.target_request)
        context_path = self.target / ".caprmedio_runtime" / "installation" / "contexts" / f"{self.context.sha256}.toml"
        context_path.parent.mkdir(parents=True, exist_ok=True)
        context_path.write_bytes(self.context.with_digest_toml())
        self.path = self.target / "bin"
        self.home = self.target / "home"
        self.path.mkdir()
        self.home.mkdir()

    def _package_selector(self, *, image_digest: str | None = None) -> bytes:
        selected_image = self._full.candidate_image_digest.removeprefix("sha256:") if image_digest is None else image_digest
        return (
            "\n".join(
                (
                    "schema_version = 1",
                    f'package_manifest_sha256 = "{self.package.manifest_digest}"',
                    f'release_relpath = "releases/{self.package.manifest_digest}"',
                    f'framework_version = "{self.package.framework_version}"',
                    f'version_toml_sha256 = "{self.package.version_toml_sha256}"',
                    f'source_catalog_sha256 = "{self.package.source_catalog_sha256}"',
                    f'full_gate_receipt_sha256 = "{self._full.receipt_sha256}"',
                    f'image_digest = "{selected_image}"',
                    "",
                )
            )
        ).encode("utf-8")

    def _packet(self) -> RetainedNativeFullGatePacket:
        return RetainedNativeFullGatePacket(
            artifact_root=self.artifact_root,
            retained_candidate=self.identity,
            suite=self._suite,
            build=self._build,
            verification=self._verification,
            e2e=self._e2e,
            evidence=self._full,
        )

    def _entrypoint(self) -> str:
        return next(
            row.path for row in self.package.inventory if row.role == "engine" and row.path.endswith(".py")
        )

    def _publish_delivery(self, lock):
        request = PortableInstallationRequest(target=self.target_request,
            retained_gate_receipt_path=self.artifact_root / self._full.evidence_root / "receipt.json",
            full_gate_packet=self._packet())
        from framework_package import verify_current_package_selector
        selector = verify_current_package_selector(self._package_selector(), self.package)
        prepared = methodology.prepare_candidate_portable_methodology_publication(request,
            package=self.package, target_context=self.context, prospective_selector=selector)
        return methodology.publish_prepared_candidate_portable_methodology(request, prepared,
            package=self.package, target_context=self.context, prospective_selector=selector, lock=lock)

    def _candidate_stage_request(self, **changes: object) -> CandidateRuntimeCommandStageRequest:
        values: dict[str, object] = {
            "package": self.package,
            "target_context": self.context,
            "prospective_package_selector": self._package_selector(),
            "full_gate_packet": self._packet(),
            "state_generation": 1,
            "entrypoint": self._entrypoint(),
            "fixed_arguments": (),
            "invocation_nonce": "candidate-proof-fixture",
            "path_directories": (self.path,),
            "home": self.home,
        }
        values.update(changes)
        return CandidateRuntimeCommandStageRequest(**values)

    def _lock(self) -> InstallationPublicationLock:
        return InstallationPublicationLock(
            self.target,
            target_context_sha256=self.context.sha256,
            owner_run_id="candidate-native-proof-fixture",
            operation="candidate-native-proof-stage",
            command_sha256="c" * 64,
        ).acquire()

    def _runtime_selector(self, lock: InstallationPublicationLock) -> bytes:
        return (
            "\n".join(
                (
                    "schema_version = 1",
                    f'package_manifest_sha256 = "{self.package.manifest_digest}"',
                    f'target_project_context_sha256 = "{self.context.sha256}"',
                    "state_generation = 1",
                    f'installation_lock_generation = "{lock.lock_generation}"',
                    f'image_digest = "{self._full.candidate_image_digest.removeprefix("sha256:")}"',
                    "",
                )
            )
        ).encode("utf-8")

    def test_stages_and_reopens_candidate_proof_without_selector_publication(self) -> None:
        lock = self._lock()
        self.addCleanup(lambda: lock.active and lock.release("completed"))
        command_request = self._candidate_stage_request()
        stage = stage_candidate_runtime_command(command_request, lock=lock)
        prospective_package_root = (
            self.target / ".caprmedio_install" / "releases" / self.package.manifest_digest
        )
        command = tomllib.loads(stage.command_path.read_text(encoding="utf-8"))
        self.assertEqual(
            [
                "uv", "run", "--locked", "--no-sync", "--no-env-file", "--project",
                prospective_package_root.as_posix(), "python", self._entrypoint(),
            ],
            command["argv"],
        )
        wrapper = stage.wrapper_path.read_text(encoding="utf-8")
        self.assertIn(f"cd {shlex.quote(prospective_package_root.as_posix())}\n", wrapper)
        self.assertNotIn(self.package.root.as_posix(), wrapper)
        proof_request = CandidateNativeInstallationProofRequest(
            package=self.package,
            target_context=self.context,
            command_stage=stage,
            prospective_package_selector=command_request.prospective_package_selector,
            prospective_selector=self._runtime_selector(lock),
            full_gate_packet=command_request.full_gate_packet,
            methodology_delivery=self._publish_delivery(lock),
        )

        proof = stage_candidate_native_installation_proof(proof_request, lock=lock)

        self.assertEqual(self.package.manifest_digest, proof.package_manifest_sha256)
        self.assertEqual(self._full.receipt_sha256, proof.full_gate_receipt_sha256)
        self.assertEqual(self._full.candidate_image_digest.removeprefix("sha256:"), proof.image_digest)
        self.assertEqual(proof, read_candidate_native_installation_proof(proof_request, lock=lock))
        self.assertFalse((self.target / ".caprmedio_install" / "current.toml").exists())
        self.assertFalse((self.target / ".caprmedio_runtime" / "installation" / "current.toml").exists())

    def test_refuses_unsealed_or_gate_mismatched_candidate_before_stage_write(self) -> None:
        lock = self._lock()
        self.addCleanup(lambda: lock.active and lock.release("completed"))
        unsealed = replace(self.package, root=self.target / "not-staged" / self.package.manifest_digest)
        with self.assertRaisesRegex(PortableRuntimeMaterializationError, "candidate-package-invalid"):
            stage_candidate_runtime_command(self._candidate_stage_request(package=unsealed), lock=lock)
        with self.assertRaisesRegex(PortableRuntimeMaterializationError, "candidate-full-gate-mismatch"):
            stage_candidate_runtime_command(
                self._candidate_stage_request(prospective_package_selector=self._package_selector(image_digest="f" * 64)),
                lock=lock,
            )
        self.assertFalse((self.target / ".caprmedio_tmp" / "installation" / "staging" / lock.lock_generation).exists())

    def test_candidate_proof_refuses_physically_valid_ungated_legacy_delivery(self) -> None:
        lock = self._lock()
        self.addCleanup(lambda: lock.active and lock.release("completed"))
        command_request = self._candidate_stage_request()
        stage = stage_candidate_runtime_command(command_request, lock=lock)
        installation = PortableInstallationRequest(target=self.target_request,
            retained_gate_receipt_path=self.artifact_root / self._full.evidence_root / "receipt.json",
            full_gate_packet=self._packet())
        from framework_package import verify_current_package_selector
        selector = verify_current_package_selector(self._package_selector(), self.package)
        prepared = methodology.prepare_target_portable_methodology_publication(installation,
            package=self.package, target_context=self.context, prospective_selector=selector)
        delivered = methodology.publish_prepared_target_portable_methodology(installation, prepared,
            package=self.package, target_context=self.context, prospective_selector=selector, lock=lock)
        # Retain exact physically published output, compiler, source members,
        # context and canonical final-package references. Only remove the
        # target preparation's Full Gate binding to model the legacy schema.
        document = json.loads(delivered.delivery_manifest_path.read_bytes())
        document.pop("gate_receipt_sha256")
        document.pop("target_preparation_sha256")
        document["source_view_sha256"] = methodology._digest(methodology._canonical_json([
            methodology.PortableMethodologyFile(source.source_view_path, source.sha256, source.mode).__dict__
            for source in sorted(prepared.source_members, key=lambda source: source.source_view_path)]))
        document.pop("sha256")
        document["sha256"] = methodology._digest(methodology._canonical_json(document))
        delivered.delivery_manifest_path.write_bytes(methodology._canonical_json(document) + b"\n")
        legacy = methodology.PortableMethodologyDelivery(self.package.manifest_digest,
            self.package.source_catalog_sha256, self.context.sha256, prepared.compiler_sha256,
            prepared.compiler_frontier_sha256, document["source_view_sha256"], prepared.authoring_source_sha256,
            delivered.output_tree_sha256, document["sha256"], delivered.output_root,
            delivered.delivery_manifest_path, delivered.files)
        from native_installation_proof import reopen_native_methodology_delivery
        physical = reopen_native_methodology_delivery(self.target, self.package, self.context, legacy,
            full_gate_packet=self._packet())
        self.assertIsNone(physical.gate_receipt_sha256)
        request = CandidateNativeInstallationProofRequest(package=self.package, target_context=self.context,
            command_stage=stage, prospective_package_selector=self._package_selector(),
            prospective_selector=self._runtime_selector(lock), full_gate_packet=self._packet(),
            methodology_delivery=legacy)
        with self.assertRaisesRegex(NativeInstallationProofError, "native-proof-delivery-binding-mismatch"):
            stage_candidate_native_installation_proof(request, lock=lock)
        self.assertFalse((self.target / ".caprmedio_tmp/installation/proofs" / lock.lock_generation).exists())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
