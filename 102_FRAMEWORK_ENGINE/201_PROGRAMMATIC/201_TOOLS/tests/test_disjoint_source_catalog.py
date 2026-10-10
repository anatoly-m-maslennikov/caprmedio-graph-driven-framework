"""Fast D561v3 partition checks for the physical source catalog."""

from __future__ import annotations

import hashlib
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace


TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

import framework_package as package  # noqa: E402
from source_catalog_admission import (  # noqa: E402
    SourceAdmissionDescriptor,
    _descriptors_from_snapshot,
    build_source_admission_receipt,
    render_source_catalog,
)


def _digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _tree_digest(root: Path) -> str:
    rows = [
        {
            "path": file.relative_to(root).as_posix(),
            "sha256": _digest(file.read_bytes()),
            "mode": file.stat().st_mode & 0o777,
        }
        for file in sorted(root.rglob("*"))
        if file.is_file()
    ]
    return _digest(json.dumps(rows, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8"))


def _row(resource: str, destination_path: str, payload: bytes) -> SimpleNamespace:
    return SimpleNamespace(
        resource=resource,
        destination_path=destination_path,
        sha256=_digest(payload),
        mode=0o644,
    )


class DisjointSourceCatalogTests(unittest.TestCase):
    def setUp(self) -> None:
        # Retain synthetic evidence: managed macOS hosts can deny recursive
        # cleanup after a catalog walk, and cleanup must not hide assertions.
        self.root = Path(tempfile.mkdtemp(prefix="caprmedio-disjoint-catalog-", dir="/private/tmp"))
        self._write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", b"tool\n")
        self._write("methodology/active/001_CORE_META_MODEL/04_requirement/core.md", b"core\n")
        self._write("methodology/active/002_INSTALLED_EXTENSIONS/demo/v1/04_requirement/extension.md", b"extension\n")
        self._write("methodology/active/003_PROJECT_CONFIGURATION/05_method/configuration.md", b"configuration\n")
        self._write("methodology/support/support.txt", b"support\n")

    def _write(self, relative: str, payload: bytes) -> None:
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)

    def _descriptors(self, *, duplicate_extension: bool = False, omit_configuration: bool = False) -> tuple[SourceAdmissionDescriptor, ...]:
        descriptors = [
            SourceAdmissionDescriptor(
                "core-meta-model",
                "methodology",
                _tree_digest(self.root / "methodology/active/001_CORE_META_MODEL"),
                _tree_digest(self.root / "methodology/active/001_CORE_META_MODEL"),
                "public",
                False,
                "methodology/active/001_CORE_META_MODEL",
            ),
            SourceAdmissionDescriptor(
                "local-core",
                "core",
                _tree_digest(self.root / "102_FRAMEWORK_ENGINE"),
                _tree_digest(self.root / "102_FRAMEWORK_ENGINE"),
                "public",
                False,
                "102_FRAMEWORK_ENGINE",
            ),
            SourceAdmissionDescriptor(
                "methodology-support",
                "support",
                _tree_digest(self.root / "methodology/support"),
                _tree_digest(self.root / "methodology/support"),
                "public",
                False,
                "methodology/support",
            ),
            SourceAdmissionDescriptor(
                "extension-demo-v1",
                "extension",
                _tree_digest(self.root / "methodology/active/002_INSTALLED_EXTENSIONS/demo/v1"),
                _tree_digest(self.root / "methodology/active/002_INSTALLED_EXTENSIONS/demo/v1"),
                "public",
                False,
                "methodology/active/002_INSTALLED_EXTENSIONS/demo/v1",
            ),
        ]
        if duplicate_extension:
            extension = descriptors[-1]
            descriptors.append(
                SourceAdmissionDescriptor(
                    "extension-demo-v1-copy",
                    extension.kind,
                    extension.revision,
                    extension.sha256,
                    extension.visibility,
                    extension.selection_default,
                    extension.path,
                )
            )
        if not omit_configuration:
            descriptors.append(
                SourceAdmissionDescriptor(
                    "project-configuration",
                    "configuration",
                    _tree_digest(self.root / "methodology/active/003_PROJECT_CONFIGURATION"),
                    _tree_digest(self.root / "methodology/active/003_PROJECT_CONFIGURATION"),
                    "public",
                    False,
                    "methodology/active/003_PROJECT_CONFIGURATION",
                )
            )
        return tuple(sorted(descriptors, key=lambda descriptor: descriptor.identity))

    def _catalog(self, descriptors: tuple[SourceAdmissionDescriptor, ...]) -> bytes:
        receipt_bytes = build_source_admission_receipt(
            operator="test-operator",
            command_ref="test-command",
            action_run_id="test-run",
            sources=descriptors,
        )
        receipt = _digest(receipt_bytes)
        admissions = self.root / "admissions"
        admissions.mkdir(exist_ok=True)
        (admissions / f"{receipt}.json").write_bytes(receipt_bytes)
        return render_source_catalog(descriptors, admission_receipt_sha256=receipt)

    def test_snapshot_partitions_core_extension_and_configuration_without_active_ancestor(self) -> None:
        rows = (
            _row("METHODOLOGY", "methodology/active/001_CORE_META_MODEL/04_requirement/core.md", b"core\n"),
            _row("METHODOLOGY", "methodology/active/002_INSTALLED_EXTENSIONS/demo/v1/04_requirement/extension.md", b"extension\n"),
            _row("METHODOLOGY", "methodology/active/002_INSTALLED_EXTENSIONS/demo/v2/04_requirement/extension.md", b"extension v2\n"),
            _row("METHODOLOGY", "methodology/active/003_PROJECT_CONFIGURATION/05_method/configuration.md", b"configuration\n"),
            _row("FRAMEWORK_ENGINE", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", b"tool\n"),
            _row("METHODOLOGY_SUPPORT", "methodology/support/support.txt", b"support\n"),
        )
        descriptors = _descriptors_from_snapshot(SimpleNamespace(portable_package_rows=rows))
        self.assertEqual(descriptors, _descriptors_from_snapshot(SimpleNamespace(portable_package_rows=rows)))
        by_kind = {descriptor.kind: descriptor for descriptor in descriptors if descriptor.kind != "extension"}
        extensions = tuple(descriptor for descriptor in descriptors if descriptor.kind == "extension")

        self.assertEqual(by_kind["methodology"].path, "methodology/active/001_CORE_META_MODEL")
        self.assertEqual(by_kind["configuration"].path, "methodology/active/003_PROJECT_CONFIGURATION")
        self.assertFalse(by_kind["configuration"].selection_default)
        self.assertEqual(
            {descriptor.path for descriptor in extensions},
            {
                "methodology/active/002_INSTALLED_EXTENSIONS/demo/v1",
                "methodology/active/002_INSTALLED_EXTENSIONS/demo/v2",
            },
        )
        self.assertEqual(len({descriptor.identity for descriptor in extensions}), 2)
        self.assertTrue(all(re.fullmatch(r"[a-z][a-z0-9_-]*", descriptor.identity) for descriptor in extensions))
        self.assertNotIn("methodology/active", {descriptor.path for descriptor in descriptors})

    def test_disjoint_covered_optional_rows_are_allowed(self) -> None:
        catalog = self._catalog(self._descriptors())

        records = package._validate_catalog(self.root, catalog)

        configuration = dict(records)["project-configuration"]
        self.assertFalse(configuration["selection_default"])

    def test_overlapping_or_unadmitted_methodology_rows_are_refused(self) -> None:
        for descriptors, code in (
            (self._descriptors(duplicate_extension=True), "catalog-methodology-overlap"),
            (self._descriptors(omit_configuration=True), "catalog-methodology-uncovered"),
        ):
            with self.subTest(code=code):
                catalog = self._catalog(descriptors)
                with self.assertRaises(package.FrameworkPackageError) as raised:
                    package._validate_catalog(self.root, catalog)
                self.assertEqual(raised.exception.code, code)

    def test_root_digest_and_revision_change_with_its_material_rows(self) -> None:
        rows = list(
            (
                _row("METHODOLOGY", "methodology/active/001_CORE_META_MODEL/04_requirement/core.md", b"core\n"),
                _row("FRAMEWORK_ENGINE", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", b"tool\n"),
                _row("METHODOLOGY_SUPPORT", "methodology/support/support.txt", b"support\n"),
            )
        )
        original = _descriptors_from_snapshot(SimpleNamespace(portable_package_rows=tuple(rows)))
        rows[0] = _row("METHODOLOGY", "methodology/active/001_CORE_META_MODEL/04_requirement/core.md", b"changed core\n")
        changed = _descriptors_from_snapshot(SimpleNamespace(portable_package_rows=tuple(rows)))
        original_core = next(item for item in original if item.kind == "methodology")
        changed_core = next(item for item in changed if item.kind == "methodology")

        self.assertNotEqual(original_core.sha256, changed_core.sha256)
        self.assertNotEqual(original_core.revision, changed_core.revision)
        self.assertEqual(changed_core.sha256, changed_core.revision)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
