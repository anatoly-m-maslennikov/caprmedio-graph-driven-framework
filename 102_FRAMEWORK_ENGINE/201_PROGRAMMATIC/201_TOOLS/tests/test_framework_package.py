"""Synthetic fixtures for the reusable Framework package boundary.

The fixtures intentionally retain their temporary roots.  A managed host can
deny directory cleanup, and cleanup failures must never hide a failed package
assertion or discard its evidence.
"""

from __future__ import annotations

import hashlib
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch


TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from framework_package import (  # noqa: E402
    FrameworkPackageError,
    assemble_framework_package,
    provide_installation_package_evidence,
    verify_current_package_selector,
    verify_framework_package,
)
import framework_package as package_library  # noqa: E402


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


class FrameworkPackageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="caprmedio-framework-package-")).resolve()
        self.source = self.root / "source"
        self.releases = self.root / "releases"
        self._write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", b"tool = 'fixture'\n", mode=0o755)
        self._write("methodology/active/CA-R-001--fixture.md", b"# active methodology\n")
        self._write("methodology/support/CA-D-001--fixture.md", b"# declared support\n")
        self._write("SKILLS/ca/SKILL.md", b"# ca\n")
        self._write("defaults/framework.toml", b"[defaults]\nname = 'fixture'\n")
        self._write("pyproject.toml", b"[project]\nname = 'fixture'\nversion = '0.1.0'\n")
        self._write("uv.lock", b"version = 1\n")
        self._write("version.toml", b"[framework]\nversion = '0.1.0'\n")
        self._write_catalog()

    def _write(self, relative: str, payload: bytes, *, mode: int = 0o644) -> Path:
        target = self.source / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
        target.chmod(mode)
        return target

    def _write_catalog(self, *, revision: str | None = None) -> None:
        source_rows = (
            ("core", "core", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"),
            ("methodology", "methodology", "methodology/active/CA-R-001--fixture.md"),
            ("support", "support", "methodology/support/CA-D-001--fixture.md"),
        )
        lines = ["schema_version = 1", ""]
        for identity, kind, relative in source_rows:
            digest = _sha256((self.source / relative).read_bytes())
            lines.extend(
                [
                    f"[source.{identity}]",
                    f'kind = "{kind}"',
                    f'revision = "{revision or "a" * 40}"',
                    f'sha256 = "{digest}"',
                    f'admission_receipt_sha256 = "{"b" * 64}"',
                    'visibility = "public"',
                    "selection_default = false",
                    f'path = "{relative}"',
                    "",
                ]
            )
        self._write("catalog.toml", ("\n".join(lines) + "\n").encode("utf-8"))

    def test_assembles_and_reopens_a_complete_content_addressed_package(self) -> None:
        package = assemble_framework_package(self.source, self.releases)

        self.assertEqual(package.root, self.releases.resolve() / package.manifest_digest)
        self.assertEqual(package.root.name, package.manifest_digest)
        self.assertEqual(package.manifest_digest, _sha256((package.root / "manifest.toml").read_bytes()))
        self.assertEqual(package.framework_version, "0.1.0")
        self.assertEqual(package.source_catalog_sha256, _sha256((package.root / "catalog.toml").read_bytes()))
        self.assertNotIn("manifest.toml", {row.path for row in package.inventory})
        self.assertEqual(
            [(row.path, row.role) for row in package.inventory],
            sorted((row.path, row.role) for row in package.inventory),
        )
        self.assertEqual(verify_framework_package(package.root), package)
        evidence = provide_installation_package_evidence(package.root)
        self.assertTrue(evidence.verified)
        self.assertEqual(evidence.package_manifest_sha256, package.manifest_digest)
        self.assertEqual(evidence.catalog_sha256, package.source_catalog_sha256)
        self.assertEqual(evidence.selected_source_identities, ("core", "methodology", "support"))

    def test_ignores_finder_metadata_but_refuses_substantive_extra_members(self) -> None:
        self._write(".DS_Store", b"finder")
        package = assemble_framework_package(self.source, self.releases)
        self.assertNotIn(".DS_Store", {row.path for row in package.inventory})

        (package.root / "undeclared.txt").write_text("extra\n", encoding="utf-8")
        with self.assertRaises(FrameworkPackageError) as raised:
            verify_framework_package(package.root)
        self.assertEqual(raised.exception.code, "package-extra-member")

    def test_refuses_source_symlink_and_private_settings(self) -> None:
        target = self.root / "outside.txt"
        target.write_bytes(b"outside\n")
        link = self.source / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/link.py"
        try:
            link.symlink_to(target)
        except OSError as error:  # pragma: no cover - host capability guard
            self.skipTest(f"symlinks unavailable in this synthetic fixture: {error}")
        with self.assertRaises(FrameworkPackageError) as raised:
            assemble_framework_package(self.source, self.releases)
        self.assertEqual(raised.exception.code, "package-symlink")

        link.unlink()
        self._write(".caprmedio_project/settings.toml", b"private = true\n")
        with self.assertRaises(FrameworkPackageError) as raised:
            assemble_framework_package(self.source, self.releases)
        self.assertEqual(raised.exception.code, "package-private-member")

    def test_refuses_mutable_and_noncanonical_catalog_revisions(self) -> None:
        for revision in ("main", "a" * 41):
            with self.subTest(revision=revision):
                self._write_catalog(revision=revision)
                with self.assertRaises(FrameworkPackageError) as raised:
                    assemble_framework_package(self.source, self.releases)
                self.assertEqual(raised.exception.code, "catalog-revision-invalid")

    def test_refuses_boolean_schema_versions_in_all_closed_toml_carriers(self) -> None:
        catalog = self.source / "catalog.toml"
        catalog.write_bytes(catalog.read_bytes().replace(b"schema_version = 1", b"schema_version = true"))
        with self.assertRaises(FrameworkPackageError) as raised:
            assemble_framework_package(self.source, self.releases)
        self.assertEqual(raised.exception.code, "catalog-invalid")

        self._write_catalog()
        package = assemble_framework_package(self.source, self.releases)
        manifest = package.root / "manifest.toml"
        manifest_bytes = manifest.read_bytes()
        manifest.write_bytes(manifest_bytes.replace(b"schema_version = 1", b"schema_version = true"))
        with self.assertRaises(FrameworkPackageError) as raised:
            verify_framework_package(package.root)
        self.assertEqual(raised.exception.code, "package-manifest-invalid")
        manifest.write_bytes(manifest_bytes)

        with self.assertRaises(FrameworkPackageError) as raised:
            verify_current_package_selector(b"schema_version = true\n", package)
        self.assertEqual(raised.exception.code, "package-selector-invalid")

    def test_refuses_forbidden_env_names_from_path_metadata_without_opening_them(self) -> None:
        for name in (".env", ".envrc", "production.env", ".env.pyc"):
            with self.subTest(name=name):
                forbidden = MagicMock()
                forbidden.name = name
                forbidden.suffix = Path(name).suffix
                forbidden.relative_to.return_value = Path(name)
                forbidden.is_symlink.return_value = False
                forbidden.is_dir.return_value = False
                forbidden.is_file.return_value = True
                with patch.object(Path, "iterdir", return_value=iter((forbidden,))):
                    with self.assertRaises(FrameworkPackageError) as raised:
                        package_library._walk_regular_files(self.source, code_prefix="package")
                self.assertEqual(raised.exception.code, "package-private-member")
                forbidden.read_bytes.assert_not_called()

    def test_refuses_tampered_dependency_and_version_carriers(self) -> None:
        self._write("version.toml", b"version = '0.1.0'\n")
        with self.assertRaises(FrameworkPackageError) as raised:
            assemble_framework_package(self.source, self.releases)
        self.assertEqual(raised.exception.code, "package-version-invalid")
        self._write("version.toml", b"[framework]\nversion = '0.1.0'\n")
        package = assemble_framework_package(self.source, self.releases)
        for relative in ("pyproject.toml", "uv.lock", "version.toml"):
            carrier = package.root / relative
            original = carrier.read_bytes()
            carrier.write_bytes(original + b"# tampered\n")
            with self.assertRaises(FrameworkPackageError) as raised:
                verify_framework_package(package.root)
            self.assertIn(raised.exception.code, {"package-member-digest-mismatch", "package-version-mismatch"})
            with self.assertRaises(FrameworkPackageError) as selector_raised:
                verify_current_package_selector(b"schema_version = 1\n", package)
            self.assertIn(selector_raised.exception.code, {"package-member-digest-mismatch", "package-version-mismatch"})
            carrier.write_bytes(original)

    def test_reopen_refuses_a_self_consistent_manifest_without_required_defaults(self) -> None:
        package = assemble_framework_package(self.source, self.releases)
        rows = tuple(row for row in package.inventory if row.role != "default")
        manifest = package_library._render_manifest(
            framework_version=package.framework_version,
            version_toml_sha256=package.version_toml_sha256,
            source_catalog_sha256=package.source_catalog_sha256,
            rows=rows,
        )
        incomplete = package.root.parent / _sha256(manifest)
        shutil.copytree(package.root, incomplete)
        (incomplete / "defaults/framework.toml").unlink()
        (incomplete / "manifest.toml").write_bytes(manifest)
        with self.assertRaises(FrameworkPackageError) as raised:
            verify_framework_package(incomplete)
        self.assertEqual(raised.exception.code, "package-incomplete")

    def test_refuses_lexical_source_release_and_package_symlink_paths(self) -> None:
        try:
            source_alias = self.root / "source-alias"
            source_alias.symlink_to(self.source, target_is_directory=True)
            with self.assertRaises(FrameworkPackageError) as raised:
                assemble_framework_package(source_alias, self.releases)
            self.assertEqual(raised.exception.code, "package-root-symlink")

            ancestor_alias = self.root.parent / f"{self.root.name}-ancestor-alias"
            ancestor_alias.symlink_to(self.root, target_is_directory=True)
            with self.assertRaises(FrameworkPackageError) as raised:
                assemble_framework_package(ancestor_alias / "source", self.releases)
            self.assertEqual(raised.exception.code, "package-root-symlink")

            self.releases.mkdir()
            releases_alias = self.root / "releases-alias"
            releases_alias.symlink_to(self.releases, target_is_directory=True)
            with self.assertRaises(FrameworkPackageError) as raised:
                assemble_framework_package(self.source, releases_alias)
            self.assertEqual(raised.exception.code, "package-root-symlink")

            package = assemble_framework_package(self.source, self.releases)
            package_alias = self.root / "package-alias"
            package_alias.symlink_to(package.root, target_is_directory=True)
            with self.assertRaises(FrameworkPackageError) as raised:
                verify_framework_package(package_alias)
            self.assertEqual(raised.exception.code, "package-root-symlink")
        except OSError as error:  # pragma: no cover - host capability guard
            self.skipTest(f"symlinks unavailable in this synthetic fixture: {error}")

    def test_refuses_manifest_tampering_and_invalid_current_selector(self) -> None:
        package = assemble_framework_package(self.source, self.releases)
        valid_selector = "\n".join(
            [
                "schema_version = 1",
                f'package_manifest_sha256 = "{package.manifest_digest}"',
                f'release_relpath = "releases/{package.manifest_digest}"',
                'framework_version = "0.1.0"',
                f'version_toml_sha256 = "{package.version_toml_sha256}"',
                f'source_catalog_sha256 = "{package.source_catalog_sha256}"',
                f'full_gate_receipt_sha256 = "{"c" * 64}"',
                f'image_digest = "{"d" * 64}"',
                "",
            ]
        )
        selector = verify_current_package_selector(valid_selector.encode("utf-8"), package)
        self.assertEqual(selector.package_manifest_sha256, package.manifest_digest)

        with self.assertRaises(FrameworkPackageError) as raised:
            verify_current_package_selector((valid_selector + 'checkout = "main"\n').encode("utf-8"), package)
        self.assertEqual(raised.exception.code, "package-selector-invalid")

        manifest = package.root / "manifest.toml"
        manifest.write_text(manifest.read_text(encoding="utf-8").replace('role = "engine"', 'role = "tampered"'), encoding="utf-8")
        with self.assertRaises(FrameworkPackageError) as raised:
            verify_framework_package(package.root)
        self.assertEqual(raised.exception.code, "package-manifest-invalid")
        with self.assertRaises(FrameworkPackageError) as raised:
            verify_current_package_selector(valid_selector.encode("utf-8"), package)
        self.assertEqual(raised.exception.code, "package-manifest-invalid")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
