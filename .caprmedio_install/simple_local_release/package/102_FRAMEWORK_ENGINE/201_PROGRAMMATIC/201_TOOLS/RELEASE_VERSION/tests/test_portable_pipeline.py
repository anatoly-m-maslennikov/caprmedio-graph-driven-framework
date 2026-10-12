"""D596/D602 private portable package preparation from real sealed inputs."""

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
from release_portable_package import (  # noqa: E402
    PortableReleasePackageError,
    prepare_portable_release_package,
    reopen_portable_release_package,
)


class PortablePipelineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = PortablePackageFixture()
        self.addCleanup(self.fixture.cleanup)

    def test_prepares_and_reopens_a_distinct_private_physical_package(self) -> None:
        selector = self.fixture.root / ".caprmedio_runtime/framework/current.toml"
        selector_before = selector.read_bytes()
        prepared = prepare_portable_release_package(self.fixture.root, self.fixture.sealed)

        self.assertNotEqual(prepared.candidate_snapshot_manifest_sha256, prepared.package_manifest_sha256)
        self.assertEqual(prepared.candidate_run_id, self.fixture.run_id)
        self.assertEqual(prepared.package.framework_version, "N+1")
        self.assertEqual(prepared.package.source_catalog_sha256, self.fixture.sealed.source_catalog_sha256)
        self.assertEqual(
            reopen_portable_release_package(self.fixture.root, self.fixture.run_id, prepared.package_manifest_sha256),
            prepared.package,
        )
        self.assertEqual(selector.read_bytes(), selector_before)
        self.assertFalse((self.fixture.root / ".caprmedio_install").exists())
        self.assertFalse((self.fixture.root / ".agents/skills/ca").exists())

    def test_changed_or_missing_physical_inputs_refuse_without_selector_or_promotion(self) -> None:
        selector = self.fixture.root / ".caprmedio_runtime/framework/current.toml"
        selector_before = selector.read_bytes()
        tool = self.fixture.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"
        tool.write_bytes(tool.read_bytes() + b"changed\n")
        with self.assertRaises(PortableReleasePackageError) as changed:
            prepare_portable_release_package(self.fixture.root, self.fixture.sealed)
        self.assertEqual(changed.exception.code, "release-currentness-stale")
        self.assertEqual(selector.read_bytes(), selector_before)
        self.assertFalse((self.fixture.root / ".caprmedio_install").exists())

        fixture = PortablePackageFixture()
        self.addCleanup(fixture.cleanup)
        fixture.support.unlink()
        with self.assertRaises(PortableReleasePackageError) as missing:
            prepare_portable_release_package(fixture.root, fixture.sealed)
        self.assertEqual(missing.exception.code, "release-currentness-stale")
        self.assertFalse((fixture.root / ".caprmedio_install").exists())


if __name__ == "__main__":
    unittest.main()
