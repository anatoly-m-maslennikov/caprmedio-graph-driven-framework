"""Synthetic, read-only target-installation context admission tests."""

from __future__ import annotations

from dataclasses import replace
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest


TOOLS = Path(__file__).resolve().parents[1]
TESTS = Path(__file__).resolve().parent
TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(TOOLS))
if str(TESTS) not in sys.path:
    sys.path.insert(0, str(TESTS))

from installation_context import (  # noqa: E402
    InstallationContextError,
    TargetProjectRequest,
    VerifiedPackageEvidence,
    bind_target_project_context,
)
from framework_package import assemble_framework_package, provide_installation_package_evidence  # noqa: E402
from source_admission_fixture import write_source_admission_receipt  # noqa: E402


def _sha(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _sha_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


class InstallationContextTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.package = self.physical_package("default-package")
        self.package_evidence = provide_installation_package_evidence(self.package.root)

    def physical_package(self, name: str):
        source = self.base / name / "source"
        releases = self.base / name / "releases"

        def write(relative: str, payload: bytes, *, mode: int = 0o644) -> None:
            target = source / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)
            target.chmod(mode)

        write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", b"tool = 'fixture'\n", mode=0o755)
        write("methodology/active/CA-R-001--fixture.md", b"# active methodology\n")
        write("methodology/support/CA-D-001--fixture.md", b"# declared support\n")
        write("SKILLS/ca/SKILL.md", b"# ca\n")
        write("defaults/framework.toml", b"[defaults]\nname = 'fixture'\n")
        write("pyproject.toml", b"[project]\nname = 'fixture'\nversion = '0.1.0'\n")
        write("uv.lock", b"version = 1\n")
        write("version.toml", b"[framework]\nversion = '0.1.0'\n")
        source_rows = (
            ("core", "core", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"),
            ("methodology", "methodology", "methodology/active/CA-R-001--fixture.md"),
            ("support", "support", "methodology/support/CA-D-001--fixture.md"),
        )
        descriptors = tuple(
            {
                "identity": identity,
                "kind": kind,
                "revision": _sha_bytes((source / relative).read_bytes()),
                "sha256": _sha_bytes((source / relative).read_bytes()),
                "visibility": "public",
                "selection_default": False,
                "path": relative,
            }
            for identity, kind, relative in source_rows
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
        write("catalog.toml", ("\n".join(lines) + "\n").encode("utf-8"))
        return assemble_framework_package(source, releases)

    def project(self, name: str, *, identity: str = "project-identity") -> tuple[Path, Path]:
        root = self.base / name
        control = root / f".caprmedio_{name}"
        control.mkdir(parents=True)
        (control / "caprmedio_project_settings.toml").write_text(
            "[project]\n"
            f'name = "{identity}"\n\n'
            "[paths]\n"
            f'control_root = ".caprmedio_{name}"\n',
            encoding="utf-8",
        )
        (control / "project_structure.toml").write_text(
            "schema_version = 1\n"
            "scope_units = []\n",
            encoding="utf-8",
        )
        (control / "operators_registry.toml").write_text("operators = []\n", encoding="utf-8")
        return root, control

    def request(
        self,
        root: Path,
        control: Path,
        *,
        mode: str = "bootstrap",
        identity: str = "project-identity",
        repository_identity: str | bool = False,
        root_locator: str = "fixtures/project",
        relocates_from=None,
        package_root: Path | None = None,
        package_evidence: VerifiedPackageEvidence | None = None,
    ) -> TargetProjectRequest:
        return TargetProjectRequest(
            target_root=root,
            control_child=control.name,
            mode=mode,
            target_project_identity=identity,
            settings_path=control / "caprmedio_project_settings.toml",
            project_structure_path=control / "project_structure.toml",
            operators_registry_path=control / "operators_registry.toml",
            repository_identity=repository_identity,
            root_locator=root_locator,
            package_root=self.package.root if package_root is None else package_root,
            package_evidence=self.package_evidence if package_evidence is None else package_evidence,
            relocates_from=relocates_from,
        )

    def test_bootstrap_binds_exact_controls_and_has_no_runtime_effect(self) -> None:
        root, control = self.project("bootstrap")

        context = bind_target_project_context(self.request(root, control))

        self.assertEqual("bootstrap", context.mode)
        self.assertEqual(control.name, context.control_child_relpath)
        self.assertFalse(context.repository_identity)
        self.assertEqual(self.package_evidence.catalog_sha256, context.package_evidence.catalog_sha256)
        self.assertEqual(_sha((control / "caprmedio_project_settings.toml").read_text()), context.settings_sha256)
        self.assertEqual(_sha((control / "project_structure.toml").read_text()), context.project_structure_sha256)
        self.assertEqual(_sha((control / "operators_registry.toml").read_text()), context.registry_sha256)
        self.assertFalse((root / ".caprmedio_runtime").exists())
        carrier = context.toml_bytes().decode("utf-8")
        self.assertIn('mode = "bootstrap"', carrier)
        self.assertIn(f'target_project_context_sha256 = "{context.sha256}"', context.with_digest_toml().decode("utf-8"))

    def test_persisted_context_keeps_a_self_digest_outside_its_canonical_preimage(self) -> None:
        root, control = self.project("persisted-context")

        context = bind_target_project_context(self.request(root, control))

        expected = context.toml_bytes()
        persisted = context.with_digest_toml()
        self.assertEqual(_sha_bytes(expected), context.sha256)
        self.assertEqual(
            expected + f'target_project_context_sha256 = "{context.sha256}"\n'.encode("utf-8"),
            persisted,
        )

    def test_adopt_preserves_mutable_runtime_config_byte_for_byte(self) -> None:
        root, control = self.project("adopt")
        config = root / ".caprmedio_runtime" / "config.toml"
        config.parent.mkdir()
        original = b"[runtime]\nverbosity = \"quiet\"\n"
        config.write_bytes(original)

        context = bind_target_project_context(self.request(root, control, mode="adopt"))

        self.assertEqual("adopt", context.mode)
        self.assertEqual(original, config.read_bytes())
        self.assertFalse((root / ".caprmedio_runtime/installation").exists())

    def test_adopt_refuses_active_runtime_selector_without_writing_state(self) -> None:
        root, control = self.project("active")
        selector = root / ".caprmedio_runtime/installation/current.toml"
        selector.parent.mkdir(parents=True)
        selector.write_text("schema_version = 1\n", encoding="utf-8")
        before = selector.read_bytes()

        with self.assertRaisesRegex(InstallationContextError, "active"):
            bind_target_project_context(self.request(root, control, mode="adopt"))

        self.assertEqual(before, selector.read_bytes())

    def test_adopt_refuses_an_existing_public_ca_skill(self) -> None:
        root, control = self.project("public-skill")
        public_skill = root / ".agents/skills/ca"
        public_skill.mkdir(parents=True)
        (public_skill / "SKILL.md").write_text("# ca\n", encoding="utf-8")

        with self.assertRaisesRegex(InstallationContextError, "active"):
            bind_target_project_context(self.request(root, control, mode="adopt"))

        self.assertTrue((public_skill / "SKILL.md").is_file())

    def test_refuses_missing_or_replaced_explicit_control_carrier(self) -> None:
        root, control = self.project("missing")
        request = self.request(root, control)
        (control / "operators_registry.toml").unlink()

        with self.assertRaisesRegex(InstallationContextError, "operators registry"):
            bind_target_project_context(request)

        self.assertFalse((root / ".caprmedio_runtime").exists())

    def test_refuses_forged_typed_package_evidence_before_context_effect(self) -> None:
        root, control = self.project("catalog")
        forged = replace(self.package_evidence, package_manifest_sha256="f" * 64, verified=True)

        with self.assertRaisesRegex(InstallationContextError, "differs"):
            bind_target_project_context(self.request(root, control, package_evidence=forged))

        self.assertFalse((root / ".caprmedio_runtime").exists())

    def test_reopened_physical_evidence_not_caller_verified_boolean_controls_admission(self) -> None:
        root, control = self.project("provider-controls-verification")
        caller_assertion = replace(self.package_evidence, verified=False)

        context = bind_target_project_context(self.request(root, control, package_evidence=caller_assertion))

        self.assertTrue(context.package_evidence.verified)
        self.assertEqual(self.package_evidence.source_pins, context.package_evidence.source_pins)

    def test_refuses_tampered_package_after_expected_evidence_was_observed(self) -> None:
        root, control = self.project("tampered-package")
        version = self.package.root / "version.toml"
        version.write_bytes(version.read_bytes() + b"# changed\n")

        with self.assertRaisesRegex(InstallationContextError, "physical package"):
            bind_target_project_context(self.request(root, control))

        self.assertFalse((root / ".caprmedio_runtime").exists())

    def test_accepts_provider_valid_sixty_four_character_revision_without_context_revalidation(self) -> None:
        package = self.physical_package("revision-sixty-four")
        evidence = provide_installation_package_evidence(package.root)
        root, control = self.project("revision-sixty-four")

        context = bind_target_project_context(
            self.request(root, control, package_root=package.root, package_evidence=evidence)
        )

        self.assertEqual(evidence.source_pins, context.package_evidence.source_pins)

    def test_two_projects_with_one_repository_identity_are_isolated(self) -> None:
        first_root, first_control = self.project("first", identity="first-id")
        second_root, second_control = self.project("second", identity="second-id")
        repository_identity = _sha("shared-repository")

        first = bind_target_project_context(
            self.request(
                first_root,
                first_control,
                identity="first-id",
                repository_identity=repository_identity,
                root_locator="projects/first",
            )
        )
        second = bind_target_project_context(
            self.request(
                second_root,
                second_control,
                identity="second-id",
                repository_identity=repository_identity,
                root_locator="projects/second",
            )
        )

        self.assertNotEqual(first.sha256, second.sha256)
        self.assertNotEqual(first.target_project_identity, second.target_project_identity)
        self.assertNotEqual(first.control_child_relpath, second.control_child_relpath)

    def test_relocation_links_a_typed_prior_context_after_identity_revalidation(self) -> None:
        old_root, old_control = self.project("old", identity="same-project")
        previous = bind_target_project_context(
            self.request(old_root, old_control, identity="same-project", root_locator="old/location")
        )
        new_root, new_control = self.project("new", identity="same-project")

        relocated = bind_target_project_context(
            self.request(
                new_root,
                new_control,
                identity="same-project",
                root_locator="new/location",
                relocates_from=previous,
            )
        )

        self.assertEqual(previous.sha256, relocated.relocates_context_sha256)
        self.assertNotEqual(previous.sha256, relocated.sha256)
        self.assertNotIn(str(old_root), relocated.toml_bytes().decode("utf-8"))

    def test_relocation_refuses_a_different_declared_project_identity(self) -> None:
        old_root, old_control = self.project("old-identity", identity="old-project")
        previous = bind_target_project_context(
            self.request(old_root, old_control, identity="old-project", root_locator="old/location")
        )
        new_root, new_control = self.project("new-identity", identity="new-project")

        with self.assertRaisesRegex(InstallationContextError, "identity"):
            bind_target_project_context(
                self.request(
                    new_root,
                    new_control,
                    identity="new-project",
                    root_locator="new/location",
                    relocates_from=previous,
                )
            )


if __name__ == "__main__":
    unittest.main()
