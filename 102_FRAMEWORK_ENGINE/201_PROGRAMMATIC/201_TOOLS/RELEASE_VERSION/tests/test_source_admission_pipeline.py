"""D602 admission writes require an explicit trusted invocation."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for _path in (RELEASE_ROOT, TEST_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from portable_package_fixture import PortablePackageFixture  # noqa: E402
from source_catalog_admission import SourceCatalogAdmissionError  # noqa: E402


class SourceAdmissionPipelineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = PortablePackageFixture(admit=False)
        self.addCleanup(self.fixture.cleanup)

    def test_no_invocation_creates_no_catalog_or_admission_state(self) -> None:
        self.assertFalse((self.fixture.root / "catalog.toml").exists())
        self.assertFalse((self.fixture.root / "admissions").exists())

    def test_explicit_matched_invocation_writes_one_receipt_and_catalog(self) -> None:
        admitted = self.fixture.admit_sources()
        self.assertEqual(admitted.snapshot_sha256, admitted.receipt.snapshot_sha256)
        self.assertTrue(admitted.receipt_path.is_file())
        self.assertTrue(admitted.catalog_path.is_file())
        self.assertEqual(len(admitted.sources), 3)
        self.assertEqual({source.kind for source in admitted.sources}, {"core", "methodology", "support"})

    def test_unknown_or_mismatched_invocation_refuses_without_publication(self) -> None:
        with self.assertRaises(SourceCatalogAdmissionError) as unknown:
            self.fixture.admit_sources(admitter=lambda _request: object())
        self.assertEqual(unknown.exception.code, "source-admission-invocation-untrusted")
        self.assertFalse((self.fixture.root / "catalog.toml").exists())
        self.assertFalse((self.fixture.root / "admissions").exists())

    def test_changed_snapshot_refuses_before_catalog_or_receipt_publication(self) -> None:
        tool = self.fixture.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"
        tool.write_bytes(tool.read_bytes() + b"changed\n")

        with self.assertRaises(SourceCatalogAdmissionError) as changed:
            self.fixture.admit_sources()

        self.assertEqual(changed.exception.code, "release-currentness-stale")
        self.assertFalse((self.fixture.root / "catalog.toml").exists())
        self.assertFalse((self.fixture.root / "admissions").exists())


if __name__ == "__main__":
    unittest.main()
