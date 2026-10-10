"""D567/D562 retained-package staging checks using actual temporary bytes.

The compiler receipt is a typed fixture only; no compiler, selector, Skill,
Docker, full-suite, or Journal effect is performed here.
"""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path, PurePosixPath
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TESTS_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TESTS_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from release_handoff import CompilerSuccessEvidence, build_validated_candidate, seal_candidate_compilation, validate_source_copy  # noqa: E402
from release_handoff_fixture import COMPILER, MATERIALIZED, ReleaseFixture, digest  # noqa: E402
from release_packaging import ReleasePackagingError, stage_framework_package  # noqa: E402


class ReleasePackagingTests(unittest.TestCase):
    def setUp(self) -> None:
        # Retain the disposable physical fixture for terminal-evidence review.
        self.fixture = self._new_fixture()

    @staticmethod
    def _new_fixture(*, runtime_parent_symlink: bool = False) -> ReleaseFixture:
        root = Path(tempfile.mkdtemp(prefix="release-packaging-"))
        if runtime_parent_symlink:
            runtime_root = root / ".caprmedio_runtime"
            runtime_root.mkdir()
            outside = root / "outside-runtime"
            outside.mkdir()
            (runtime_root / "framework").symlink_to(outside, target_is_directory=True)
        return ReleaseFixture(root)

    def _sealed_compilation(self, fixture: ReleaseFixture | None = None):
        fixture = self.fixture if fixture is None else fixture
        candidate = build_validated_candidate(fixture.root, fixture.intent)
        fixture.deliver_copy()
        source_copy = validate_source_copy(candidate)
        fixture.materialize_bytes(candidate.manifest.sha256)
        evidence = CompilerSuccessEvidence(
            candidate_snapshot_manifest_sha256=candidate.manifest.sha256,
            outcome="completed",
            compiler_entrypoint={"path": COMPILER, "sha256": digest((fixture.root / COMPILER).read_bytes())},
            compiler_frontier_digest=candidate.manifest.source_frontier_digest,
            child_materialization_root=f"{MATERIALIZED}/{candidate.manifest.sha256}",
            actual_compiled_output_sha256=candidate.manifest.expected_compiled_output_sha256,
        )
        return seal_candidate_compilation(source_copy, evidence)

    def test_stages_actual_complete_package_without_selecting_n_or_public_skill(self) -> None:
        handoff = self._sealed_compilation()
        protected = {relative: (self.fixture.root / relative).read_bytes() for relative in (
            ".caprmedio_runtime/framework/current.toml", ".agents/skills/ca/SKILL.md",
            ".caprmedio_runtime/journal/evidence.jsonl", ".caprmedio_caprmedio/project_structure.toml",
        )}

        result = stage_framework_package(self.fixture.root, handoff)

        release = self.fixture.root / result["release_root"]
        self.assertTrue(result["staged"])
        self.assertEqual(result["candidate_snapshot_manifest_sha256"], handoff.candidate_snapshot_manifest_sha256)
        self.assertEqual(result["file_count"], len(handoff.package_rows))
        self.assertEqual((release / "FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py").read_bytes(), (self.fixture.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py").read_bytes())
        self.assertEqual((release / "METHODOLOGY/compiled/compiled.md").read_bytes(), self.fixture.compiled_payload)
        self.assertEqual((release / "SKILLS/ca/references/usage.md").stat().st_mode & 0o777, 0o600)
        self.assertIn("candidate_snapshot_manifest_sha256", (release / "manifest.toml").read_text(encoding="utf-8"))
        for relative, before in protected.items():
            self.assertEqual((self.fixture.root / relative).read_bytes(), before)

    def test_raw_mapping_and_noncanonical_candidate_are_refused(self) -> None:
        handoff = self._sealed_compilation()
        with self.assertRaises(ReleasePackagingError) as raised:
            stage_framework_package(self.fixture.root, handoff.model_dump())
        self.assertEqual(raised.exception.code, "sealed-compilation-untrusted")
        forged = handoff.model_copy(update={"candidate_snapshot_manifest_sha256": "0" * 64})
        with self.assertRaises(ReleasePackagingError) as raised:
            stage_framework_package(self.fixture.root, forged)
        self.assertEqual(raised.exception.code, "candidate-manifest-unsealed")

    def test_matching_existing_retained_package_is_idempotent_and_changed_bytes_collide(self) -> None:
        handoff = self._sealed_compilation()
        first = stage_framework_package(self.fixture.root, handoff)
        second = stage_framework_package(self.fixture.root, handoff)
        self.assertTrue(first["staged"])
        self.assertFalse(second["staged"])
        self.assertTrue(second["verified"])
        release = self.fixture.root / second["release_root"]
        (release / "METHODOLOGY/compiled/compiled.md").write_bytes(b"tampered\n")
        with self.assertRaises(ReleasePackagingError) as raised:
            stage_framework_package(self.fixture.root, handoff)
        self.assertEqual(raised.exception.code, "release-collision")

    def test_retained_ephemeral_metadata_is_accepted_but_secret_shaped_bytecode_refuses(self) -> None:
        handoff = self._sealed_compilation()
        first = stage_framework_package(self.fixture.root, handoff)
        release = self.fixture.root / first["release_root"]
        metadata = release / ".DS_Store"
        metadata.write_bytes(b"finder metadata\n")

        second = stage_framework_package(self.fixture.root, handoff)

        self.assertFalse(second["staged"])
        self.assertTrue(second["verified"])
        self.assertEqual(metadata.read_bytes(), b"finder metadata\n")

        class SecretShapedEntry:
            def __init__(self) -> None:
                self.read_attempted = False

            def relative_to(self, _root: Path) -> PurePosixPath:
                return PurePosixPath(".env.pyc")

            def is_symlink(self) -> bool:
                return False

            def is_dir(self) -> bool:
                return False

            def is_file(self) -> bool:
                return True

            def read_bytes(self) -> bytes:
                self.read_attempted = True
                raise AssertionError("secret-shaped fixture entry must be refused before bytes are read")

        secret = SecretShapedEntry()
        path_type = type(release)
        original_rglob = path_type.rglob

        def rglob_with_secret(path: Path, pattern: str):
            if path == release and pattern == "*":
                return iter((secret,))
            return original_rglob(path, pattern)

        with patch.object(path_type, "rglob", autospec=True, side_effect=rglob_with_secret):
            with self.assertRaises(ReleasePackagingError) as raised:
                stage_framework_package(self.fixture.root, handoff)
        self.assertEqual(raised.exception.code, "release-collision")
        self.assertFalse(secret.read_attempted)
        self.assertEqual(metadata.read_bytes(), b"finder metadata\n")

    def test_rereads_current_bytes_and_modes_before_copy(self) -> None:
        for mutation in ("bytes", "mode"):
            with self.subTest(mutation=mutation):
                fixture = self._new_fixture()
                handoff = self._sealed_compilation(fixture)
                target = fixture.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py"
                original, mode = target.read_bytes(), target.stat().st_mode & 0o777
                if mutation == "bytes":
                    target.write_bytes(original + b"changed\n")
                    expected = "package-source-digest-mismatch"
                else:
                    target.chmod(0o600)
                    expected = "package-source-mode-mismatch"
                try:
                    with self.assertRaises(ReleasePackagingError) as raised:
                        stage_framework_package(fixture.root, handoff)
                    self.assertEqual(raised.exception.code, expected)
                finally:
                    target.write_bytes(original)
                    target.chmod(mode)

    def test_incomplete_typed_rows_and_runtime_parent_symlink_are_refused(self) -> None:
        handoff = self._sealed_compilation()
        incomplete = handoff.model_copy(update={"package_rows": [row for row in handoff.package_rows if row.resource != "SKILL"]})
        with self.assertRaises(ReleasePackagingError) as raised:
            stage_framework_package(self.fixture.root, incomplete)
        self.assertEqual(raised.exception.code, "package-incomplete")

        symlink_fixture = self._new_fixture(runtime_parent_symlink=True)
        symlink_handoff = self._sealed_compilation(symlink_fixture)
        with self.assertRaises(ReleasePackagingError) as raised:
            stage_framework_package(symlink_fixture.root, symlink_handoff)
        self.assertEqual(raised.exception.code, "runtime-parent-symlink")


if __name__ == "__main__":
    unittest.main()
