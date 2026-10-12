"""Synthetic portable Framework-package installation preparation tests."""

from __future__ import annotations

from dataclasses import replace
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
for path in (str(TOOLS), str(Path(__file__).resolve().parent)):
    if path not in sys.path:
        sys.path.insert(0, path)

import framework_installation  # noqa: E402
from framework_installation import (  # noqa: E402
    InstallationError,
    PortableInstallationRequest,
    initialize_portable_runtime_configuration,
    prepare_portable_installation,
)
from framework_package import CurrentPackageSelector, assemble_framework_package, provide_installation_package_evidence  # noqa: E402
from installation_context import TargetProjectRequest  # noqa: E402
from source_admission_fixture import write_source_admission_receipt  # noqa: E402


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _tree_sha(path: Path) -> str:
    rows = [
        {
            "path": member.relative_to(path).as_posix(),
            "sha256": _sha256(member.read_bytes()),
            "mode": member.stat().st_mode & 0o777,
        }
        for member in sorted(path.rglob("*"))
        if member.is_file() and not member.is_symlink()
    ]
    return _sha256(json.dumps(rows, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8"))


class PortableInstallationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.package = self._package()
        self.target, self.control = self._project()
        self.gate = self.target / "retained" / "full-gate.receipt"
        self.gate.parent.mkdir()
        self.gate.write_bytes(b"retained full gate receipt\n")
        self._write_current_selector(_sha256(self.gate.read_bytes()))

    def _write(self, root: Path, relative: str, payload: bytes, *, mode: int = 0o644) -> None:
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
        target.chmod(mode)

    def _seed_package_compiler_closure(self, source: Path) -> None:
        """Seal the actual compiler and every locally imported dependency."""

        for relative in (
            "COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py",
            "project_runtime.py",
            "project_selection.py",
            "artifact_metadata.py",
            "VALIDATE_ATOMS/validate_atoms_workers/__init__.py",
            "VALIDATE_ATOMS/validate_atoms_workers/read_io.py",
            "VALIDATE_ATOMS/validate_atoms_workers/settings.py",
        ):
            canonical = TOOLS / relative
            self._write(
                source,
                f"102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/{relative}",
                canonical.read_bytes(),
                mode=canonical.stat().st_mode & 0o777,
            )

    def _package(
        self,
        *,
        source_name: str = "package-source",
        releases_name: str = "package-releases",
        default_startup_timeout: int = 60,
    ):
        source = self.base / source_name
        releases = self.base / releases_name
        self._seed_package_compiler_closure(source)
        self._write(source, "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", b"tool = 'fixture'\n", mode=0o755)
        self._write(source, "methodology/active/001_CORE_META_MODEL/04_requirement/CA-R-001--fixture.md", b"# active methodology\n")
        self._write(
            source,
            "methodology/active/003_PROJECT_CONFIGURATION/05_method/CA-M-001--fixture.md",
            b"# configuration methodology\n",
        )
        self._write(source, "methodology/support/CA-D-001--fixture.md", b"# declared support\n")
        self._write(source, "SKILLS/ca/SKILL.md", b"# ca\n")
        self._write(
            source,
            "defaults/runtime-config.toml",
            b"".join(
                (
                    b"schema_version = 1\n\n",
                    b"[project_mcp]\n",
                    f"startup_timeout_seconds = {default_startup_timeout}\n".encode("utf-8"),
                    b"build_timeout_seconds = 600\n",
                    b"build_if_missing = true\n",
                )
            ),
        )
        self._write(source, "pyproject.toml", b"[project]\nname = 'fixture'\nversion = '0.1.0'\n")
        self._write(source, "uv.lock", b"version = 1\n")
        self._write(source, "version.toml", b"[framework]\nversion = '0.1.0'\n")
        source_rows = (
            ("core-engine", "core", "102_FRAMEWORK_ENGINE"),
            ("core-methodology", "methodology", "methodology/active/001_CORE_META_MODEL"),
            ("project-configuration", "configuration", "methodology/active/003_PROJECT_CONFIGURATION"),
            ("declared-support", "support", "methodology/support"),
        )
        descriptors = tuple(
            sorted(
                (
                    {
                        "identity": identity,
                        "kind": kind,
                        "revision": _tree_sha(source / relative),
                        "sha256": _tree_sha(source / relative),
                        "visibility": "public",
                        "selection_default": False,
                        "path": relative,
                    }
                    for identity, kind, relative in source_rows
                ),
                key=lambda descriptor: descriptor["identity"],
            )
        )
        receipt = write_source_admission_receipt(source, descriptors)
        lines = ["schema_version = 1", ""]
        for descriptor in descriptors:
            lines.extend(
                [
                    f"[source.{descriptor['identity']}]",
                    f'kind = "{descriptor["kind"]}"',
                    f'revision = "{descriptor["revision"]}"',
                    f'sha256 = "{descriptor["sha256"]}"',
                    f'admission_receipt_sha256 = "{receipt.sha256}"',
                    f'visibility = "{descriptor["visibility"]}"',
                    "selection_default = false",
                    f'path = "{descriptor["path"]}"',
                    "",
                ]
            )
        self._write(source, "catalog.toml", ("\n".join(lines) + "\n").encode("utf-8"))
        return assemble_framework_package(source, releases)

    def _project(self) -> tuple[Path, Path]:
        root = self.base / "target"
        control = root / ".caprmedio_target"
        control.mkdir(parents=True)
        (control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname = "target-project"\n\n[paths]\ncontrol_root = ".caprmedio_target"\n',
            encoding="utf-8",
        )
        (control / "project_structure.toml").write_text("schema_version = 1\nscope_units = []\n", encoding="utf-8")
        (control / "operators_registry.toml").write_text("operators = []\n", encoding="utf-8")
        configuration = next(
            pin
            for pin in provide_installation_package_evidence(self.package.root).source_pins
            if pin.identity == "project-configuration"
        )
        framework_settings = control / "000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"
        framework_settings.parent.mkdir()
        framework_settings.write_text(
            "[methodology.configuration]\n"
            "identity = \"project-configuration\"\n"
            f"revision = \"{configuration.revision}\"\n",
            encoding="utf-8",
        )
        return root, control

    def _write_current_selector(self, gate_sha256: str, *, package=None) -> None:
        selected_package = self.package if package is None else package
        selector = self.target / ".caprmedio_install" / "current.toml"
        selector.parent.mkdir(parents=True, exist_ok=True)
        selector.write_text(
            "\n".join(
                (
                    "schema_version = 1",
                    f'package_manifest_sha256 = "{selected_package.manifest_digest}"',
                    f'release_relpath = "releases/{selected_package.manifest_digest}"',
                    f'framework_version = "{selected_package.framework_version}"',
                    f'version_toml_sha256 = "{selected_package.version_toml_sha256}"',
                    f'source_catalog_sha256 = "{selected_package.source_catalog_sha256}"',
                    f'full_gate_receipt_sha256 = "{gate_sha256}"',
                    f'image_digest = "{"c" * 64}"',
                    "",
                )
            ),
            encoding="utf-8",
        )

    def request(self, *, package=None) -> PortableInstallationRequest:
        selected_package = self.package if package is None else package
        evidence = provide_installation_package_evidence(selected_package.root)
        target = TargetProjectRequest(
            target_root=self.target,
            control_child=self.control.name,
            # The fixture intentionally publishes D598 before preparation so
            # every refusal can exercise the selected-package reader.  That
            # is an adoption context, not an empty-bootstrap context.
            mode="adopt",
            target_project_identity="target-project",
            settings_path=self.control / "caprmedio_project_settings.toml",
            project_structure_path=self.control / "project_structure.toml",
            operators_registry_path=self.control / "operators_registry.toml",
            repository_identity=False,
            root_locator="fixtures/target",
            package_root=selected_package.root,
            package_evidence=evidence,
        )
        return PortableInstallationRequest(
            target=target,
            retained_gate_receipt_path=self.gate,
        )

    def test_prepare_reopens_admitted_inputs_and_preserves_existing_target_config(self) -> None:
        config = self.target / ".caprmedio_runtime" / "config.toml"
        config.parent.mkdir()
        original = (
            b"schema_version = 1\n\n"
            b"[project_mcp]\n"
            b"startup_timeout_seconds = 12\n"
            b"build_timeout_seconds = 34\n"
            b"build_if_missing = false\n"
            b"port = 8199\n"
        )
        config.write_bytes(original)

        preparation = prepare_portable_installation(self.request())

        self.assertEqual(self.package.manifest_digest, preparation.package.manifest_digest)
        self.assertEqual(_sha256(self.gate.read_bytes()), preparation.selector.full_gate_receipt_sha256)
        self.assertEqual("preserved", preparation.configuration.state)
        self.assertEqual("blocked", preparation.status)
        self.assertEqual("full-gate-verifier-unavailable", preparation.blocker)
        self.assertEqual(original, config.read_bytes())
        self.assertFalse((self.target / ".caprmedio_runtime/installation/current.toml").exists())

    def test_prepare_refuses_missing_gate_or_selector_before_any_runtime_effect(self) -> None:
        (self.target / ".caprmedio_install/current.toml").unlink()

        with self.assertRaisesRegex(InstallationError, "selector"):
            prepare_portable_installation(self.request())

        self.assertFalse((self.target / ".caprmedio_runtime").exists())

    def test_prepare_refuses_gate_digest_mismatch_before_any_runtime_effect(self) -> None:
        self._write_current_selector("d" * 64)

        with self.assertRaisesRegex(InstallationError, "gate"):
            prepare_portable_installation(self.request())

        self.assertFalse((self.target / ".caprmedio_runtime").exists())

    def test_prepare_refuses_a_missing_retained_gate_receipt_before_any_runtime_effect(self) -> None:
        self.gate.unlink()

        with self.assertRaisesRegex(InstallationError, "gate receipt"):
            prepare_portable_installation(self.request())

        self.assertFalse((self.target / ".caprmedio_runtime").exists())

    def test_prepare_refuses_a_retained_gate_receipt_routed_through_a_symlink(self) -> None:
        payload = self.gate.read_bytes()
        external = self.base / "external-gate"
        external.mkdir()
        (external / self.gate.name).write_bytes(payload)
        linked = self.gate.parent / "linked"
        linked.symlink_to(external, target_is_directory=True)
        request = replace(self.request(), retained_gate_receipt_path=linked / self.gate.name)

        with self.assertRaisesRegex(InstallationError, "unsafe Project ancestor"):
            prepare_portable_installation(request)

        self.assertFalse((self.target / ".caprmedio_runtime").exists())

    def test_protected_retained_receipt_paths_are_rejected_before_any_reader_or_open(self) -> None:
        root = framework_installation._portable_root(self.request())
        selector = CurrentPackageSelector(
            package_manifest_sha256="a" * 64,
            release_relpath="releases/fixture",
            framework_version="0.1.0",
            version_toml_sha256="b" * 64,
            source_catalog_sha256="c" * 64,
            full_gate_receipt_sha256="d" * 64,
            image_digest="e" * 64,
        )
        protected = (".env-receipt", "receipt.env", "secrets/receipt", "credentials/receipt", "private_settings/receipt")

        with (
            patch("framework_installation._read_target_regular_carrier") as reader,
            patch("framework_installation.os.open") as opener,
        ):
            for relative in protected:
                with self.subTest(relative=relative), self.assertRaisesRegex(InstallationError, "path is protected"):
                    framework_installation._retained_gate_receipt(root, self.target / relative, selector)

        reader.assert_not_called()
        opener.assert_not_called()

    def test_prepare_refuses_a_default_not_admitted_by_the_reopened_package(self) -> None:
        request = replace(self.request(), runtime_default_member="defaults/other.toml")

        with self.assertRaisesRegex(InstallationError, "not an admitted"):
            prepare_portable_installation(request)

        self.assertFalse((self.target / ".caprmedio_runtime").exists())

    def test_prepare_blocks_an_incompatible_target_config_without_replacing_its_bytes(self) -> None:
        config = self.target / ".caprmedio_runtime" / "config.toml"
        config.parent.mkdir()
        original = b"[runtime]\nmode = 'legacy'\n"
        config.write_bytes(original)

        preparation = prepare_portable_installation(self.request())

        self.assertEqual("blocked", preparation.status)
        self.assertEqual("runtime-configuration-migration-needed", preparation.blocker)
        self.assertEqual("blocked", preparation.configuration.state)
        self.assertEqual(original, config.read_bytes())
        self.assertFalse((self.target / ".caprmedio_runtime/installation").exists())

    def test_prepare_upgrade_reopens_a_second_package_and_preserves_commented_target_config(self) -> None:
        config = self.target / ".caprmedio_runtime" / "config.toml"
        config.parent.mkdir()
        original = (
            b"# Project operator override; installation must retain every byte.\n"
            b"schema_version = 1\n\n"
            b"[project_mcp]\n"
            b"startup_timeout_seconds = 8 # configured by the Project\n"
            b"build_timeout_seconds = 15\n"
            b"build_if_missing = false\n"
        )
        config.write_bytes(original)
        upgrade = self._package(
            source_name="package-source-upgrade",
            releases_name="package-releases-upgrade",
            default_startup_timeout=45,
        )
        self.assertNotEqual(self.package.manifest_digest, upgrade.manifest_digest)
        self._write_current_selector(_sha256(self.gate.read_bytes()), package=upgrade)

        preparation = prepare_portable_installation(self.request(package=upgrade))

        self.assertEqual(upgrade.manifest_digest, preparation.package.manifest_digest)
        self.assertEqual(
            _sha256((upgrade.root / "defaults/runtime-config.toml").read_bytes()),
            preparation.runtime_default_sha256,
        )
        self.assertEqual("preserved", preparation.configuration.state)
        self.assertEqual("full-gate-verifier-unavailable", preparation.blocker)
        self.assertEqual(original, config.read_bytes())
        self.assertFalse((self.target / ".caprmedio_runtime/installation").exists())

    def test_explicit_configuration_initialization_stops_without_a_full_gate_verifier(self) -> None:
        with self.assertRaisesRegex(InstallationError, "full gate verifier"):
            initialize_portable_runtime_configuration(
                self.request(),
                owner_run_id="portable-config-fixture",
                command_sha256="e" * 64,
            )

        config = self.target / ".caprmedio_runtime" / "config.toml"
        self.assertFalse(config.exists())
        self.assertFalse((self.target / ".caprmedio_runtime/installation/current.toml").exists())
        self.assertFalse((self.target / ".caprmedio_runtime/installation").exists())


if __name__ == "__main__":
    unittest.main()
