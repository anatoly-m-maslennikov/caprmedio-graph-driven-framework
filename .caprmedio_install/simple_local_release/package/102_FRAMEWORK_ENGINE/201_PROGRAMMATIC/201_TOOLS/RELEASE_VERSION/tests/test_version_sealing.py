"""Exact root ``version.toml`` sealing checks with disposable local bytes."""

from __future__ import annotations

import hashlib
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TESTS_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TESTS_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from release_contract import ReleaseContractError  # noqa: E402
from release_handoff import (  # noqa: E402
    CompilerSuccessEvidence,
    build_validated_candidate,
    seal_candidate_compilation,
    validate_source_copy,
)
from release_handoff_fixture import COMPILER, MATERIALIZED, ReleaseFixture, digest  # noqa: E402
from release_packaging import stage_framework_package  # noqa: E402


class VersionSealingTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.fixture = ReleaseFixture(Path(temporary.name))
        self.version_toml = self.fixture.write("version.toml", b'[framework]\nversion = "N+1"\n')

    def _candidate(self):
        return build_validated_candidate(self.fixture.root, self.fixture.intent)

    def _sealed_compilation(self):
        candidate = self._candidate()
        self.fixture.deliver_copy()
        source_copy = validate_source_copy(candidate)
        self.fixture.materialize_bytes(candidate.manifest.sha256)
        evidence = CompilerSuccessEvidence(
            candidate_snapshot_manifest_sha256=candidate.manifest.sha256,
            outcome="completed",
            compiler_entrypoint={"path": COMPILER, "sha256": digest((self.fixture.root / COMPILER).read_bytes())},
            compiler_frontier_digest=candidate.manifest.source_frontier_digest,
            child_materialization_root=f"{MATERIALIZED}/{candidate.manifest.sha256}",
            actual_compiled_output_sha256=candidate.manifest.expected_compiled_output_sha256,
        )
        return candidate, seal_candidate_compilation(source_copy, evidence)

    def test_candidate_seals_root_version_value_hash_and_control_row(self) -> None:
        candidate = self._candidate()

        self.assertEqual(candidate.manifest.framework_version, "N+1")
        self.assertEqual(candidate.authority.framework_version, "N+1")
        self.assertEqual(
            candidate.manifest.version_toml_sha256,
            hashlib.sha256(self.version_toml.read_bytes()).hexdigest(),
        )
        controls = [row for row in candidate.manifest.source_inventory_rows if row.resource == "PACKAGE_CONTROL"]
        self.assertEqual(1, len(controls))
        self.assertEqual(("version.toml", "version.toml"), (controls[0].source_path, controls[0].destination_path))
        self.assertEqual(candidate.manifest.version_toml_sha256, controls[0].source_sha256)

    def test_mismatched_root_version_refuses_candidate_construction(self) -> None:
        self.version_toml.write_bytes(b'[framework]\nversion = "N+2"\n')

        with self.assertRaises(ReleaseContractError) as raised:
            self._candidate()

        self.assertEqual("release-version-mismatch", raised.exception.code)

    def test_changed_version_bytes_invalidate_the_candidate_even_when_value_stays_equal(self) -> None:
        candidate = self._candidate()
        self.fixture.deliver_copy()
        self.version_toml.write_bytes(b'# same semantic version, changed sealed bytes\n[framework]\nversion = "N+1"\n')

        with self.assertRaises(ReleaseContractError) as raised:
            validate_source_copy(candidate)

        self.assertEqual("release-currentness-stale", raised.exception.code)

    def test_staged_package_retains_the_exact_root_version_file_and_manifest_binding(self) -> None:
        candidate, compilation = self._sealed_compilation()
        result = stage_framework_package(self.fixture.root, compilation)
        release = self.fixture.root / result["release_root"]
        manifest = tomllib.loads((release / "manifest.toml").read_text(encoding="utf-8"))

        self.assertEqual(self.version_toml.read_bytes(), (release / "version.toml").read_bytes())
        self.assertEqual("N+1", manifest["framework_version"])
        self.assertEqual(candidate.manifest.version_toml_sha256, manifest["version_toml_sha256"])
        rows = [row for row in manifest["files"] if row["destination"] == "version.toml"]
        self.assertEqual(1, len(rows))
        self.assertEqual(candidate.manifest.version_toml_sha256, rows[0]["sha256"])
        self.assertEqual("N+1", result["framework_version"])


if __name__ == "__main__":
    unittest.main()
