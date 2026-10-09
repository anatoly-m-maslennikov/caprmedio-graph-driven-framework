"""Producer-specific D596 private package tests with sealed physical inputs."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for candidate in (RELEASE_ROOT, TEST_ROOT):
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))

from portable_package_fixture import PortablePackageFixture  # noqa: E402
from release_handoff import SealedCandidateCompilation  # noqa: E402
from release_portable_package import (  # noqa: E402
    PortableReleasePackageError,
    prepare_portable_release_package,
    reopen_portable_release_package,
)


class PortableReleasePackageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = PortablePackageFixture()
        # Retain generated evidence: a managed host can deny recursive
        # cleanup inside an otherwise writable temporary fixture root.

    def test_private_assembly_reopens_exact_schema_one_package_bytes(self) -> None:
        prepared = prepare_portable_release_package(self.fixture.root, self.fixture.sealed)

        self.assertNotEqual(prepared.candidate_snapshot_manifest_sha256, prepared.package_manifest_sha256)
        self.assertEqual(prepared.input_manifest_sha256, self.fixture.sealed.input_manifest_sha256)
        self.assertEqual(
            prepared.private_package_root,
            self.fixture.root / ".caprmedio_tmp/release_candidates" / self.fixture.run_id / "package" / prepared.package_manifest_sha256,
        )
        self.assertEqual(prepared.package.framework_version, "N+1")
        self.assertEqual(prepared.package.version_toml_sha256, self.fixture.sealed.version_toml_sha256)
        self.assertEqual(prepared.package.source_catalog_sha256, self.fixture.sealed.source_catalog_sha256)
        self.assertEqual(
            (prepared.private_package_root / "defaults/runtime.toml").read_bytes(),
            (self.fixture.root / "defaults/runtime.toml").read_bytes(),
        )
        self.assertEqual(
            (prepared.private_package_root / "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md").read_bytes(),
            (prepared.private_package_root / "SKILLS/ca/SKILL.md").read_bytes(),
        )
        self.assertEqual(
            reopen_portable_release_package(self.fixture.root, self.fixture.run_id, prepared.package_manifest_sha256),
            prepared.package,
        )
        self.assertFalse((self.fixture.root / ".caprmedio_install").exists())
        self.assertFalse((self.fixture.root / ".agents/skills/ca").exists())

    def test_sealed_input_drift_or_missing_source_refuses_without_promotion(self) -> None:
        tool = self.fixture.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"
        tool.write_bytes(tool.read_bytes() + b"changed\n")
        with self.assertRaises(PortableReleasePackageError) as changed:
            prepare_portable_release_package(self.fixture.root, self.fixture.sealed)
        self.assertEqual(changed.exception.code, "release-currentness-stale")
        self.assertFalse((self.fixture.root / ".caprmedio_install").exists())

        missing = PortablePackageFixture()
        missing.support.unlink()
        with self.assertRaises(PortableReleasePackageError) as refused:
            prepare_portable_release_package(missing.root, missing.sealed)
        self.assertEqual(refused.exception.code, "release-currentness-stale")
        self.assertFalse((missing.root / ".caprmedio_install").exists())

    def test_raw_or_legacy_compilation_cannot_enter_schema_one_producer(self) -> None:
        for value in ({"portable_package_rows": []}, SealedCandidateCompilation.model_construct()):
            with self.subTest(value_type=type(value).__name__), self.assertRaises(PortableReleasePackageError) as refused:
                prepare_portable_release_package(self.fixture.root, value)  # type: ignore[arg-type]
            self.assertEqual(refused.exception.code, "portable-package-untrusted")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
