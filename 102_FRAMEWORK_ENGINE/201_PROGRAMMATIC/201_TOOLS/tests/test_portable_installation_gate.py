"""Detached native Full Gate transport coverage for portable installation readiness."""

from __future__ import annotations

from dataclasses import replace
from pathlib import Path
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
for path in (str(TOOLS), str(RELEASE_ROOT), str(RELEASE_TEST_ROOT)):
    if path not in sys.path:
        sys.path.insert(0, path)

from framework_installation import (  # noqa: E402
    InstallationError,
    PortableFullGatePacket,
    PortableInstallationRequest,
    initialize_portable_runtime_configuration,
    prepare_portable_installation,
)
from framework_package import provide_installation_package_evidence  # noqa: E402
from installation_context import TargetProjectRequest  # noqa: E402
from release_retained_candidate import read_retained_candidate_identity  # noqa: E402
from target_methodology_selection import FRAMEWORK_INSTANCE_SETTINGS_RELATIVE  # noqa: E402
import test_detached_native_full_gate as _detached_native_full_gate_fixture  # noqa: E402


_RUNTIME_DEFAULT = (
    b"schema_version = 1\n\n"
    b"[project_mcp]\n"
    b"startup_timeout_seconds = 60\n"
    b"build_timeout_seconds = 600\n"
    b"build_if_missing = true\n"
)


class _BridgeNativeHappyPathFixture(_detached_native_full_gate_fixture.packet_fixtures._NativeHappyPathFixture):
    """Add the production-shaped default before the candidate is sealed."""

    def _seed_project(self, extra_engine_members: dict[str, bytes]) -> None:
        super()._seed_project(extra_engine_members)
        self.write("defaults/runtime-config.toml", _RUNTIME_DEFAULT)


class PortableInstallationGateTests(unittest.TestCase):
    """Use only the physical D597 packet fixture; never mock gate success."""

    @classmethod
    def setUpClass(cls) -> None:
        fixture = _BridgeNativeHappyPathFixture()
        (
            cls._source_archive,
            cls._source_identity,
            cls._suite,
            cls._build,
            cls._verification,
            cls._e2e,
            cls._full,
        ) = _detached_native_full_gate_fixture.DetachedNativeFullGateTests()._packet(fixture)

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, delete=False)
        self.target_root = Path(self.temporary.name) / "target"
        self.target_root.mkdir()
        self.artifact_root = self.target_root / ".caprmedio_tmp" / "retained-packet"
        shutil.copytree(self._source_archive, self.artifact_root)
        descriptor = self.artifact_root / self._source_identity.descriptor_path.relative_to(self._source_archive)
        sidecar = self.artifact_root / self._source_identity.package_evidence.receipt_path.relative_to(self._source_archive)
        retained_package_root = self.artifact_root / self._source_identity.package_evidence.view.package_root.relative_to(self._source_archive)
        self.identity = read_retained_candidate_identity(
            descriptor,
            expected_sha256=self._source_identity.descriptor_sha256,
            package_root=retained_package_root,
            sidecar_path=sidecar,
            expected_sidecar_sha256=self._source_identity.package_evidence.receipt_sha256,
        )
        self.gate_receipt = self.artifact_root / self._full.evidence_root / "receipt.json"
        control_source = self.artifact_root / ".caprmedio_caprmedio"
        self.control = self.target_root / control_source.name
        self.control.mkdir()
        for name in ("caprmedio_project_settings.toml", "project_structure.toml", "operators_registry.toml"):
            shutil.copy2(control_source / name, self.control / name)
        # Preserve the canonical selected instance settings before D600 is
        # bound.  Its bytes—not catalog presence—determine the selected
        # configuration roots for this target.
        framework_settings = control_source.joinpath(*FRAMEWORK_INSTANCE_SETTINGS_RELATIVE.parts)
        copied_settings = self.control.joinpath(*FRAMEWORK_INSTANCE_SETTINGS_RELATIVE.parts)
        copied_settings.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(framework_settings, copied_settings)
        self.package_root = self.target_root / ".caprmedio_install" / "releases" / self.identity.package_evidence.view.actual_package_manifest_sha256
        shutil.copytree(retained_package_root, self.package_root)
        selected_evidence = provide_installation_package_evidence(self.package_root)
        self.assertEqual(
            self.identity.package_evidence.view.actual_package_manifest_sha256,
            selected_evidence.package_manifest_sha256,
        )
        self._write_selector(self.package_root)

    def _write_selector(self, package_root: Path, *, image_digest: str | None = None) -> None:
        evidence = provide_installation_package_evidence(package_root)
        selector = self.target_root / ".caprmedio_install" / "current.toml"
        selector.parent.mkdir(parents=True, exist_ok=True)
        selected_image_digest = self._full.candidate_image_digest.removeprefix("sha256:") if image_digest is None else image_digest
        selector.write_text(
            "\n".join(
                (
                    "schema_version = 1",
                    f'package_manifest_sha256 = "{evidence.package_manifest_sha256}"',
                    f'release_relpath = "releases/{evidence.package_manifest_sha256}"',
                    f'framework_version = "{self.identity.framework_version}"',
                    f'version_toml_sha256 = "{self.identity.version_toml_sha256}"',
                    f'source_catalog_sha256 = "{self.identity.package_evidence.view.source_catalog_sha256}"',
                    f'full_gate_receipt_sha256 = "{self._full.receipt_sha256}"',
                    f'image_digest = "{selected_image_digest}"',
                    "",
                )
            ),
            encoding="utf-8",
        )

    def _request(self) -> PortableInstallationRequest:
        settings = tomllib.loads((self.control / "caprmedio_project_settings.toml").read_text(encoding="utf-8"))
        project = settings["project"]
        self.assertIsInstance(project, dict)
        self.assertIsInstance(project.get("name"), str)
        target = TargetProjectRequest(
            target_root=self.target_root,
            control_child=self.control.name,
            mode="adopt",
            target_project_identity=project["name"],
            settings_path=self.control / "caprmedio_project_settings.toml",
            project_structure_path=self.control / "project_structure.toml",
            operators_registry_path=self.control / "operators_registry.toml",
            repository_identity=False,
            root_locator="fixtures/portable-gate",
            package_root=self.package_root,
            package_evidence=provide_installation_package_evidence(self.package_root),
        )
        return PortableInstallationRequest(
            target=target,
            retained_gate_receipt_path=self.gate_receipt,
            full_gate_packet=PortableFullGatePacket(
                artifact_root=self.artifact_root,
                retained_candidate=self.identity,
                suite=self._suite,
                build=self._build,
                verification=self._verification,
                e2e=self._e2e,
                evidence=self._full,
            ),
        )

    def test_verified_detached_packet_is_ready_but_publication_remains_blocked(self) -> None:
        before = list(sys.path)
        preparation = prepare_portable_installation(self._request())

        self.assertEqual("ready", preparation.status)
        self.assertIsNone(preparation.blocker)
        self.assertEqual(self._full.receipt_sha256, preparation.gate_receipt_sha256)
        self.assertEqual(self.identity.package_evidence.view.actual_package_manifest_sha256, preparation.package.manifest_digest)
        self.assertFalse((self.target_root / ".caprmedio_runtime/config.toml").exists())
        self.assertEqual(before, sys.path)
        with self.assertRaisesRegex(InstallationError, "publication adapter is unavailable"):
            initialize_portable_runtime_configuration(
                self._request(),
                owner_run_id="portable-gate-fixture",
                command_sha256="a" * 64,
            )
        self.assertFalse((self.target_root / ".caprmedio_runtime/config.toml").exists())

    def test_packet_receipt_path_mismatch_is_refused_before_runtime_writes(self) -> None:
        before = list(sys.path)
        request = replace(self._request(), retained_gate_receipt_path=self.artifact_root / "other-receipt.json")

        with self.assertRaisesRegex(InstallationError, "does not name the reopened Full Gate receipt"):
            prepare_portable_installation(request)

        self.assertFalse((self.target_root / ".caprmedio_runtime/config.toml").exists())
        self.assertEqual(before, sys.path)

    def test_packet_image_digest_mismatch_is_refused_before_runtime_writes(self) -> None:
        self._write_selector(self.package_root, image_digest="f" * 64)

        with self.assertRaisesRegex(InstallationError, "image differs from the selected package image"):
            prepare_portable_installation(self._request())

        self.assertFalse((self.target_root / ".caprmedio_runtime/config.toml").exists())

    def test_malformed_typed_packet_evidence_is_refused_without_attribute_error(self) -> None:
        request = self._request()
        self.assertIsNotNone(request.full_gate_packet)
        malformed_identity = replace(self.identity, package_evidence=object())
        malformed_packet = replace(request.full_gate_packet, retained_candidate=malformed_identity)

        with self.assertRaisesRegex(InstallationError, "retained package sidecar must be target-contained"):
            prepare_portable_installation(replace(request, full_gate_packet=malformed_packet))

        self.assertFalse((self.target_root / ".caprmedio_runtime/config.toml").exists())

    def test_external_packet_artifact_root_is_refused_before_runtime_writes(self) -> None:
        request = self._request()
        self.assertIsNotNone(request.full_gate_packet)
        packet = replace(request.full_gate_packet, artifact_root=Path(self.temporary.name) / "external-packet")

        with self.assertRaisesRegex(InstallationError, "artifact root must be target-contained"):
            prepare_portable_installation(replace(request, full_gate_packet=packet))

        self.assertFalse((self.target_root / ".caprmedio_runtime/config.toml").exists())

    def test_verified_packet_preserves_incompatible_configuration_and_stays_blocked(self) -> None:
        config = self.target_root / ".caprmedio_runtime/config.toml"
        config.parent.mkdir(parents=True, exist_ok=True)
        original = b"[legacy]\nmode = 'unsupported'\n"
        config.write_bytes(original)

        preparation = prepare_portable_installation(self._request())

        self.assertEqual("blocked", preparation.status)
        self.assertEqual("runtime-configuration-migration-needed", preparation.blocker)
        self.assertEqual(original, config.read_bytes())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
