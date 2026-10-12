"""Native N consumers reopen final physical installation and retained gates.

These fixture gates retain mocked command observations; they are unit evidence,
never a claim that Docker, an installation, or a repository release was run.
"""

from __future__ import annotations

from dataclasses import replace
import json
import shutil
import sys
import tempfile
from types import SimpleNamespace
import unittest
from pathlib import Path

RELEASE = Path(__file__).resolve().parents[1]
TOOLS = RELEASE.parent
for directory in (RELEASE, RELEASE / "tests", TOOLS, TOOLS / "tests"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import test_native_selected_installation as selected_fixture
from release_contract import ReleaseContractError
from release_handoff import (
    NATIVE_CURRENT_SELECTOR_RELATIVE, _revalidate, bind_native_installed_n,
    build_validated_candidate, reopen_native_installed_n, selected_n_identity,
    CompilerSuccessEvidence, seal_candidate_compilation, validate_source_copy,
    NativeInstalledNBinding,
)
from release_handoff_fixture import COMPILER, MATERIALIZED, ReleaseFixture, digest
from release_image import CANDIDATE_LABEL, CONTEXT_LABEL, DockerCommandResult, _freeze, _observed_rollback_references
from release_suite import _active_n_state
from release_suite_execution import _inspect_bound_n_image, _selector_binding
from release_packaging import _complete_rows


class NativeNAdmissionRefusalTests(unittest.TestCase):
    def setUp(self) -> None:
        # Keep these disposable source carriers available for review.
        self.fixture = ReleaseFixture(Path(tempfile.mkdtemp(prefix="native-n-refusal-")))

    def test_current_native_selector_requires_actual_retained_packet(self) -> None:
        current = self.fixture.root / NATIVE_CURRENT_SELECTOR_RELATIVE
        current.parent.mkdir(parents=True)
        current.write_bytes(b"schema_version = 1\n")
        with self.assertRaises(ReleaseContractError) as failure:
            build_validated_candidate(self.fixture.root, self.fixture.intent)
        self.assertEqual("release-native-n-proof-required", failure.exception.code)

    def test_mapping_and_boolean_cannot_supply_selected_native_n(self) -> None:
        for supplied in (True, {"full_gate_passed": True}, {"selector_sha256": "a" * 64}):
            with self.subTest(supplied=supplied), self.assertRaises(ReleaseContractError) as failure:
                reopen_native_installed_n(self.fixture.root, supplied)
            self.assertEqual("release-native-n-untrusted", failure.exception.code)

    def test_typed_wrapper_does_not_grant_a_pass_to_forged_packet(self) -> None:
        forged = NativeInstalledNBinding(None, False, SimpleNamespace(target_project_context_sha256="a" * 64))
        with self.assertRaises(ReleaseContractError) as failure:
            reopen_native_installed_n(self.fixture.root, forged)
        self.assertEqual("release-native-n-stale", failure.exception.code)

    def test_historical_native_selector_records_exact_prior_immutable_image(self) -> None:
        from release_promotion import PROMOTION_ROOT

        def selector(image: str) -> bytes:
            return ("schema_version = 1\npackage_manifest_sha256 = '" + "c" * 64
                    + "'\ntarget_project_context_sha256 = '" + "d" * 64
                    + "'\nstate_generation = 1\ninstallation_lock_generation = '" + "e" * 32
                    + "'\nimage_digest = '" + image + "'\n").encode()

        current = self.fixture.root / NATIVE_CURRENT_SELECTOR_RELATIVE
        current.parent.mkdir(parents=True)
        current.write_bytes(selector("b" * 64))
        prior = self.fixture.root / PROMOTION_ROOT / "historical-fixture" / "prior-selector.toml"
        prior.parent.mkdir(parents=True)
        prior.write_bytes(selector("a" * 64))
        self.assertEqual((prior.relative_to(self.fixture.root).as_posix(),),
                         _observed_rollback_references(self.fixture.root, "sha256:" + "a" * 64))


class NativeNConsumerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        selected_fixture.NativeSelectedInstallationTests.setUpClass()

    def setUp(self) -> None:
        self.installed = selected_fixture.NativeSelectedInstallationTests("runTest")
        self.installed.setUp()
        self.addCleanup(self.installed.doCleanups)
        self.root = self.installed.target
        structure = self.installed.target_request.project_structure_path
        original_structure = structure.read_bytes()
        self.release = ReleaseFixture(self.root)
        structure.write_bytes(original_structure)
        next_version = self.installed.package.framework_version + "-next"
        self.release.version_toml.write_text(f'[framework]\nversion = "{next_version}"\n', encoding="utf-8")
        self.release.intent["candidate_release"] = next_version
        self.release.intent["candidate_image_reference"] = f"candidate:{next_version}"
        self.release.selection.rename(self.release.selection.with_name("legacy-fixture-evidence.toml"))
        skill = self.root / ".agents/skills/ca"
        skill.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(self.installed.package.root / "SKILLS/ca", skill, dirs_exist_ok=True)
        # The candidate-source fixture creates a legacy public Skill. Keep
        # its extra bytes as separate evidence, and expose the exact native
        # package inventory for admission in this disposable target.
        retained_extra = self.root / "legacy-skill-fixture-evidence"
        for path in sorted(skill.rglob("*")):
            if path.is_file() and not (self.installed.package.root / "SKILLS/ca" / path.relative_to(skill)).is_file():
                retained_extra.mkdir(exist_ok=True)
                path.rename(retained_extra / path.name)
        self.binding = bind_native_installed_n(
            self.root, self.installed.package, self.installed.packet,
            target_context_sha256=self.installed.context.sha256,
        )

    def candidate(self):
        return build_validated_candidate(self.root, self.release.intent, native_installed_n=self.binding)

    def test_native_candidate_uses_version_as_text_and_physical_identity_for_suite(self) -> None:
        candidate = self.candidate()
        self.assertEqual(candidate.authority.executing_release, self.binding.selected.framework_version)
        self.assertEqual(selected_n_identity(candidate), self.installed.packet.retained_candidate.candidate_snapshot_manifest_sha256)
        self.assertNotEqual(selected_n_identity(candidate), candidate.authority.executing_release)
        self.assertEqual(candidate, _revalidate(candidate))
        self.assertEqual(self.binding.selected.selector_sha256, _active_n_state(self.root, candidate)[0])
        self.assertEqual((self.root / NATIVE_CURRENT_SELECTOR_RELATIVE).read_bytes(), _freeze(self.root)[0])

    def test_native_selector_never_admits_without_actual_packet(self) -> None:
        with self.assertRaises(ReleaseContractError) as failure:
            build_validated_candidate(self.root, self.release.intent)
        self.assertEqual("release-native-n-proof-required", failure.exception.code)
        with self.assertRaises(ReleaseContractError):
            reopen_native_installed_n(self.root, {"native": True})

    def test_native_freeze_refuses_final_proof_and_context_tampering(self) -> None:
        candidate = self.candidate()
        proof = self.root / ".caprmedio_runtime/installation/generations/1/release-proof.toml"
        proof.write_bytes(proof.read_bytes().replace(b"full_gate_receipt_sha256 = ", b'full_gate_receipt_sha256 = "forged" # '))
        with self.assertRaises(ReleaseContractError):
            _revalidate(candidate)
        with self.assertRaises(ReleaseContractError):
            _active_n_state(self.root, candidate)

    def test_native_freeze_refuses_forged_retained_receipt(self) -> None:
        candidate = self.candidate()
        packet = self.installed.packet
        receipt = packet.artifact_root / packet.evidence.evidence_root / "receipt.json"
        receipt.write_bytes(receipt.read_bytes() + b" ")
        with self.assertRaises(ReleaseContractError):
            _revalidate(candidate)

    def test_native_freeze_refuses_changed_context(self) -> None:
        candidate = self.candidate()
        context = self.root / ".caprmedio_runtime/installation/contexts" / f"{self.binding.selected.target_project_context_sha256}.toml"
        context.write_bytes(context.read_bytes() + b"forged = true\n")
        with self.assertRaises(ReleaseContractError):
            _revalidate(candidate)

    def test_native_package_handoff_preserves_and_reopens_same_selected_fact(self) -> None:
        candidate = self.candidate()
        self.release.deliver_copy()
        source_copy = validate_source_copy(candidate)
        self.release.materialize_bytes(candidate.manifest.sha256)
        evidence = CompilerSuccessEvidence(
            candidate_snapshot_manifest_sha256=candidate.manifest.sha256, outcome="completed",
            compiler_entrypoint={"path": COMPILER, "sha256": digest((self.root / COMPILER).read_bytes())},
            compiler_frontier_digest=candidate.manifest.source_frontier_digest,
            child_materialization_root=f"{MATERIALIZED}/{candidate.manifest.sha256}",
            actual_compiled_output_sha256=candidate.manifest.expected_compiled_output_sha256,
        )
        compilation = seal_candidate_compilation(source_copy, evidence)
        self.assertEqual(self.binding, compilation.native_installed_n)
        self.assertEqual(candidate.manifest.sha256, _complete_rows(self.root, compilation)[0])
        self.assertNotIn("native_installed_n", compilation.model_dump(mode="json"))
        package_file = self.binding.verified_package.root / "version.toml"
        package_file.write_bytes(package_file.read_bytes() + b"forged = true\n")
        with self.assertRaises(ReleaseContractError):
            _complete_rows(self.root, compilation)

    def test_native_suite_refuses_changed_public_skill(self) -> None:
        candidate = self.candidate()
        (self.root / ".agents/skills/ca/SKILL.md").write_bytes(b"changed")
        with self.assertRaises(ReleaseContractError):
            _active_n_state(self.root, candidate)

    def test_native_image_uses_original_verified_candidate_and_context(self) -> None:
        candidate = self.candidate()
        binding = _selector_binding(self.root, candidate)
        self.assertFalse(binding.bootstrap)
        self.assertEqual(self.binding.selected.package_manifest_sha256, binding.native_package_manifest_sha256)
        self.assertEqual(self.installed.packet.build.context_sha256, binding.source_context_sha256)

        class Inspector:
            def run(inner, argv, **kwargs):
                self.assertEqual(("docker", "image", "inspect", binding.image_digest), argv)
                payload = [{"Id": binding.image_digest, "Config": {
                    "Labels": {CANDIDATE_LABEL: binding.native_candidate_snapshot_manifest_sha256, CONTEXT_LABEL: binding.source_context_sha256},
                    "Env": ["PATH=/usr/local/bin:/usr/bin:/bin"],
                }}]
                return DockerCommandResult(0, json.dumps(payload).encode(), b"")

        self.assertEqual("/usr/local/bin:/usr/bin:/bin", _inspect_bound_n_image(Inspector(), self.root, binding).image_path)
        with self.assertRaises(ReleaseContractError):
            _inspect_bound_n_image(Inspector(), self.root, replace(binding, native_candidate_snapshot_manifest_sha256="forged"))


if __name__ == "__main__":
    unittest.main()
