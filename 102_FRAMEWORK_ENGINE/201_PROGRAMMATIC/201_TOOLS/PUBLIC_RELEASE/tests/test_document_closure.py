"""Physical public-document closure identity, independent of gate production."""

from __future__ import annotations

from dataclasses import asdict, replace
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

PUBLIC_ROOT = Path(__file__).resolve().parents[1]
for path in (PUBLIC_ROOT, PUBLIC_ROOT.parent):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from native_bindings import NativePublicReleaseBindings
from public_release import PublicReleaseError, SourceProof, _parameters, _read_source_file, _source, document_closure_record


class PublicDocumentClosureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name).resolve()
        self.version = b'[framework]\nversion = "0.4.2"\n'
        (self.root / "version.toml").write_bytes(self.version)
        (self.root / "README.md").write_text("# CAPRMEDIO\n", encoding="utf-8")
        (self.root / "pr-body.md").write_text("## What's new\n\n- Package.\n\n## What's fixed\n\n- Installation.\n", encoding="utf-8")
        (self.root / "VERSION_HISTORY.md").write_text("- Release summary.\n", encoding="utf-8")
        self.release = {"selected_version": "0.4.2", "release_branch": "amm/dev", "target_branch": "main",
                        "remote": {"scope": "personal", "name": "origin", "owner": "example", "repository": "project"}}

    def proof(self, *, url: str | None = None, number: int | None = None) -> SourceProof:
        digest = lambda name: hashlib.sha256((self.root / name).read_bytes()).hexdigest()
        return SourceProof("a" * 64, "0.4.2", digest("version.toml"),
                           "README.md", digest("README.md"), "pr-body.md", digest("pr-body.md"),
                           "VERSION_HISTORY.md", digest("VERSION_HISTORY.md"), "Release summary.", url, number)

    def test_canonical_closed_serialization_has_no_caller_digest_input(self) -> None:
        proof = self.proof()
        record = document_closure_record(proof)
        expected = hashlib.sha256(json.dumps(record, sort_keys=True, separators=(",", ":"),
                                             ensure_ascii=False, allow_nan=False).encode("utf-8")).hexdigest()
        self.assertEqual(13, len(record))
        self.assertEqual(expected, proof.public_document_closure_sha256)
        self.assertEqual(asdict(proof), NativePublicReleaseBindings._source_observation(proof))
        with self.assertRaises(TypeError):
            SourceProof(**asdict(proof))
        parameters = {"release": self.release, "source": {
            "candidate_snapshot_manifest_sha256": proof.candidate_snapshot_manifest_sha256,
            "readme_ref": proof.readme_ref, "pr_body_ref": proof.pr_body_ref,
            "version_history_ref": proof.version_history_ref, "version_history_summary": proof.version_history_summary,
            "public_document_closure_sha256": expected}, "recovery": {"prior_push": "not_started", "prior_pr": "not_started"}}
        with self.assertRaises(PublicReleaseError):
            _parameters(parameters)

    def test_actual_history_link_changes_document_closure_not_package_candidate(self) -> None:
        before = _source(self.proof(), "initial", project_root=self.root, release=self.release)
        url = "https://github.com/example/project/pull/7"
        (self.root / "VERSION_HISTORY.md").write_text(f"- Release summary. [PR #7]({url})\n", encoding="utf-8")
        after = _source(self.proof(url=url, number=7), "history", project_root=self.root, release=self.release)
        self.assertEqual(before.candidate_snapshot_manifest_sha256, after.candidate_snapshot_manifest_sha256)
        self.assertEqual(before.version_toml_sha256, after.version_toml_sha256)
        self.assertNotEqual(before.public_document_closure_sha256, after.public_document_closure_sha256)

    def test_changed_physical_bytes_or_tampered_derived_digest_refuse(self) -> None:
        proof = self.proof()
        object.__setattr__(proof, "public_document_closure_sha256", "0" * 64)
        with self.assertRaises(PublicReleaseError) as forged:
            _source(proof, "forged", project_root=self.root, release=self.release)
        self.assertEqual("source-proof-stale", forged.exception.code)
        current = self.proof()
        (self.root / "README.md").write_text("# Changed\n", encoding="utf-8")
        with self.assertRaises(PublicReleaseError) as stale:
            _source(current, "stale", project_root=self.root, release=self.release)
        self.assertEqual("source-proof-stale", stale.exception.code)

    def test_summary_and_actual_pr_identity_are_part_of_the_closure(self) -> None:
        proof = self.proof()
        self.assertNotEqual(proof.public_document_closure_sha256,
                            replace(proof, version_history_summary="Another summary.").public_document_closure_sha256)
        self.assertNotEqual(proof.public_document_closure_sha256,
                            replace(proof, version_history_pr_url="https://github.com/example/project/pull/8",
                                    version_history_pr_number=8).public_document_closure_sha256)

    def test_environment_reference_is_refused_before_any_read(self) -> None:
        for reference in (".env", ".env.local", "config/credentials.env"):
            with self.subTest(reference=reference), patch.object(Path, "read_bytes", side_effect=AssertionError("must not read")):
                with self.assertRaises(PublicReleaseError):
                    _read_source_file(self.root, reference, "secret")

    def test_aliased_source_ancestor_is_refused_before_any_read(self) -> None:
        (self.root / "real").mkdir()
        (self.root / "real" / "body.md").write_text("not secret", encoding="utf-8")
        (self.root / "alias").symlink_to(self.root / "real", target_is_directory=True)
        with patch.object(Path, "read_bytes", side_effect=AssertionError("must not read")):
            with self.assertRaises(PublicReleaseError):
                _read_source_file(self.root, "alias/body.md", "alias")


if __name__ == "__main__":
    unittest.main()
