"""Fast physical checks for D561 target Methodology selection."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest


TOOLS = Path(__file__).resolve().parents[1]
TESTS = Path(__file__).resolve().parent
TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
if str(TESTS) not in sys.path:
    sys.path.insert(0, str(TESTS))

from framework_package import FrameworkPackageError, assemble_framework_package, provide_installation_package_evidence  # noqa: E402
from installation_context import (  # noqa: E402
    InstallationContextError,
    TargetProjectRequest,
    bind_target_project_context,
    reopen_target_project_context,
)
from source_admission_fixture import write_source_admission_receipt  # noqa: E402
from target_methodology_selection import (  # noqa: E402
    TargetMethodologySelectionError,
    resolve_target_methodology_selection,
)


def _sha(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _tree_sha(path: Path) -> str:
    if path.is_file():
        return _sha(path.read_bytes())
    rows = [
        {
            "path": member.relative_to(path).as_posix(),
            "sha256": _sha(member.read_bytes()),
            "mode": member.stat().st_mode & 0o777,
        }
        for member in sorted(path.rglob("*"))
        if member.is_file() and not member.is_symlink()
    ]
    return _sha(json.dumps(rows, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8"))


class TargetMethodologySelectionTests(unittest.TestCase):
    """Actual package bytes and distinct target controls; no runtime effects."""

    def setUp(self) -> None:
        # Test roots are intentionally retained: macOS can deny cleanup of
        # immutable content-addressed package directories after assertions.
        self.base = Path(tempfile.mkdtemp(dir=TEST_TEMP_ROOT)).resolve()
        self.package = self._package()
        self.evidence = provide_installation_package_evidence(self.package.root)
        self.by_identity = {pin.identity: pin for pin in self.evidence.source_pins}

    def _write(self, root: Path, relative: str, payload: bytes, *, mode: int = 0o644) -> None:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
        path.chmod(mode)

    def _package(self):
        source = self.base / "source"
        releases = self.base / "releases"
        self._write(source, "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", b"tool = 'fixture'\n", mode=0o755)
        self._write(source, "methodology/active/001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", b"# core\n")
        self._write(source, "methodology/active/002_INSTALLED_EXTENSIONS/alpha/label-a/04_requirement/CA-R-002--alpha.md", b"# alpha\n")
        self._write(source, "methodology/active/002_INSTALLED_EXTENSIONS/beta/label-b/04_requirement/CA-R-003--beta.md", b"# beta\n")
        self._write(source, "methodology/active/003_PROJECT_CONFIGURATION/05_method/CA-M-004--configuration.md", b"# configuration\n")
        self._write(source, "methodology/support/CA-D-001--support.md", b"# support\n")
        self._write(source, "SKILLS/ca/SKILL.md", b"# ca\n")
        self._write(source, "defaults/framework.toml", b"[defaults]\nname = 'fixture'\n")
        self._write(source, "pyproject.toml", b"[project]\nname = 'fixture'\nversion = '0.1.0'\n")
        self._write(source, "uv.lock", b"version = 1\n")
        self._write(source, "version.toml", b"[framework]\nversion = '0.1.0'\n")
        source_rows = (
            ("core-engine", "core", "102_FRAMEWORK_ENGINE"),
            ("core-methodology", "methodology", "methodology/active/001_CORE_META_MODEL"),
            ("extension-alpha", "extension", "methodology/active/002_INSTALLED_EXTENSIONS/alpha/label-a"),
            ("extension-beta", "extension", "methodology/active/002_INSTALLED_EXTENSIONS/beta/label-b"),
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
                key=lambda row: row["identity"],
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
                    'visibility = "public"',
                    "selection_default = false",
                    f'path = "{descriptor["path"]}"',
                    "",
                ]
            )
        self._write(source, "catalog.toml", ("\n".join(lines) + "\n").encode("utf-8"))
        return assemble_framework_package(source, releases)

    def _target(self, name: str, instance_settings: str) -> tuple[Path, Path, TargetProjectRequest]:
        root = self.base / name
        control = root / f".caprmedio_{name}"
        control.mkdir(parents=True)
        self._write(
            root,
            f"{control.name}/caprmedio_project_settings.toml",
            ("[project]\n" f'name = "{name}"\n\n' "[paths]\n" f'control_root = "{control.name}"\n').encode(),
        )
        self._write(root, f"{control.name}/project_structure.toml", b"schema_version = 1\nscope_units = []\n")
        self._write(root, f"{control.name}/operators_registry.toml", b"operators = []\n")
        self._write(
            root,
            f"{control.name}/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml",
            instance_settings.encode(),
        )
        request = TargetProjectRequest(
            target_root=root,
            control_child=control.name,
            mode="bootstrap",
            target_project_identity=name,
            settings_path=control / "caprmedio_project_settings.toml",
            project_structure_path=control / "project_structure.toml",
            operators_registry_path=control / "operators_registry.toml",
            repository_identity=False,
            root_locator=f"fixtures/{name}",
            package_root=self.package.root,
            package_evidence=self.evidence,
        )
        return root, control, request

    def test_distinct_target_settings_select_distinct_exact_catalog_identities(self) -> None:
        config = self.by_identity["project-configuration"]
        alpha_root, alpha_control, alpha_request = self._target(
            "alpha",
            "[extension_selections.alpha]\nenabled = true\nrevision = \"label-a\"\n\n"
            "[methodology.configuration]\n"
            f'identity = "project-configuration"\nrevision = "{config.revision}"\n',
        )
        beta_root, beta_control, beta_request = self._target("beta", "# no Extension or Configuration is selected\n")

        alpha = resolve_target_methodology_selection(
            control_root=alpha_control, package_root=self.package.root, package_evidence=self.evidence
        )
        beta = resolve_target_methodology_selection(
            control_root=beta_control, package_root=self.package.root, package_evidence=self.evidence
        )
        context = bind_target_project_context(alpha_request)

        self.assertEqual(
            ("core-methodology", "declared-support", "extension-alpha", "project-configuration"),
            alpha.methodology_source_identities,
        )
        self.assertEqual(("core-methodology", "declared-support"), beta.methodology_source_identities)
        self.assertNotEqual(alpha.framework_instance_settings_sha256, beta.framework_instance_settings_sha256)
        self.assertEqual(self.evidence.catalog_sha256, alpha.source_catalog_sha256)
        self.assertEqual(alpha.methodology_source_identities, context.methodology_source_identities)
        self.assertIn("schema_version = 2", context.toml_bytes().decode("utf-8"))
        self.assertFalse((alpha_root / ".caprmedio_runtime").exists())
        self.assertFalse((beta_root / ".caprmedio_runtime").exists())

    def test_missing_revision_unsafe_carrier_and_configuration_revision_refuse_before_context_write(self) -> None:
        root, control, request = self._target(
            "missing-extension",
            "[extension_selections.alpha]\nenabled = true\nrevision = \"not-admitted\"\n",
        )
        with self.assertRaises(TargetMethodologySelectionError) as missing:
            resolve_target_methodology_selection(
                control_root=control, package_root=self.package.root, package_evidence=self.evidence
            )
        self.assertEqual("target-selection-source-missing", missing.exception.code)
        self.assertFalse((root / ".caprmedio_runtime").exists())

        config_root, config_control, config_request = self._target(
            "bad-config",
            "[methodology.configuration]\nidentity = \"project-configuration\"\nrevision = \"0" + "0" * 63 + "\"\n",
        )
        with self.assertRaisesRegex(InstallationContextError, "selected Configuration"):
            bind_target_project_context(config_request)
        self.assertFalse((config_root / ".caprmedio_runtime").exists())

        unsafe_root, unsafe_control, unsafe_request = self._target("unsafe", "# replacement target\n")
        canonical = unsafe_control / "000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"
        replacement = unsafe_control / "replacement.toml"
        replacement.write_text("# aliased\n", encoding="utf-8")
        canonical.unlink()
        canonical.symlink_to(replacement)
        with self.assertRaises(TargetMethodologySelectionError) as unsafe:
            resolve_target_methodology_selection(
                control_root=unsafe_control, package_root=self.package.root, package_evidence=self.evidence
            )
        self.assertEqual("target-selection-settings-invalid", unsafe.exception.code)
        self.assertFalse((unsafe_root / ".caprmedio_runtime").exists())

    def test_duplicate_overlapping_package_roots_and_context_settings_drift_are_refused(self) -> None:
        source = self.base / "overlap-source"
        self._write(source, "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", b"tool\n")
        self._write(source, "methodology/active/001_CORE_META_MODEL/04_requirement/core.md", b"core\n")
        self._write(source, "methodology/active/002_INSTALLED_EXTENSIONS/duplicate/rev/04_requirement/duplicate.md", b"duplicate\n")
        self._write(source, "methodology/support/support.md", b"support\n")
        self._write(source, "SKILLS/ca/SKILL.md", b"# ca\n")
        self._write(source, "defaults/framework.toml", b"[defaults]\n")
        self._write(source, "pyproject.toml", b"[project]\nname = 'overlap'\nversion = '0.1.0'\n")
        self._write(source, "uv.lock", b"version = 1\n")
        self._write(source, "version.toml", b"[framework]\nversion = '0.1.0'\n")
        rows = (
            ("core", "core", "102_FRAMEWORK_ENGINE"),
            ("methodology", "methodology", "methodology/active/001_CORE_META_MODEL"),
            ("duplicate-one", "extension", "methodology/active/002_INSTALLED_EXTENSIONS/duplicate/rev"),
            ("duplicate-two", "extension", "methodology/active/002_INSTALLED_EXTENSIONS/duplicate/rev"),
            ("support", "support", "methodology/support"),
        )
        descriptors = tuple(
            sorted(
                (
                    {
                        "identity": identity,
                        "kind": kind,
                        "revision": _tree_sha(source / path),
                        "sha256": _tree_sha(source / path),
                        "visibility": "public",
                        "selection_default": False,
                        "path": path,
                    }
                    for identity, kind, path in rows
                ),
                key=lambda row: row["identity"],
            )
        )
        receipt = write_source_admission_receipt(source, descriptors)
        catalog = ["schema_version = 1", ""]
        for descriptor in descriptors:
            catalog.extend(
                [
                    f"[source.{descriptor['identity']}]",
                    f'kind = "{descriptor["kind"]}"',
                    f'revision = "{descriptor["revision"]}"',
                    f'sha256 = "{descriptor["sha256"]}"',
                    f'admission_receipt_sha256 = "{receipt.sha256}"',
                    'visibility = "public"',
                    "selection_default = false",
                    f'path = "{descriptor["path"]}"',
                    "",
                ]
            )
        self._write(source, "catalog.toml", ("\n".join(catalog) + "\n").encode())
        with self.assertRaises(FrameworkPackageError) as overlap:
            assemble_framework_package(source, self.base / "overlap-releases")
        self.assertEqual("catalog-methodology-overlap", overlap.exception.code)

        root, control, request = self._target("drift", "# initial\n")
        context = bind_target_project_context(request)
        carrier = root / ".caprmedio_runtime/installation/contexts" / f"{context.sha256}.toml"
        carrier.parent.mkdir(parents=True)
        carrier.write_bytes(context.with_digest_toml())
        (control / "000_CAPRMEDIO_framework/caprmedio_framework_settings.toml").write_text("# changed\n", encoding="utf-8")
        with self.assertRaisesRegex(InstallationContextError, "differs"):
            reopen_target_project_context(request, expected_sha256=context.sha256)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
