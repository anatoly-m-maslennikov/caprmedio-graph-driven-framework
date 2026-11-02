"""Independent parse-reuse checks with real reads and on-disk drift."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOLS), str(TOOLS / "ATOM_UPDATE/tests")]

import atom_operations as operations
import atom_subject_patch as subjects
import atom_subject_stage as staging
import test_direct_preparation_guards as guards


class SubjectIdentityReuseIndependentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = guards.DirectPreparationGuardTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.source = self.fixture.source
        self.other = self.fixture.fixture._plan("Active", number=7802)
        self.other_raw = self.other.read_bytes()

    def stage(self, preview):
        return staging.stage_subject_preview(
            self.root, self.fixture.items, timestamp=guards.STAMP,
            subject_profile="legacy", expected_preview_sha256=preview["preview_sha256"])

    def test_stage_parses_unchanged_original_once_but_rereads_at_each_audit(self):
        reviewed = self.fixture.preview()
        parses, reads = Counter(), Counter()
        real_parse, real_read = operations.parse_carrier, subjects.ReadContext.read

        def parse(raw, path):
            if Path(path) == self.other:
                parses[raw] += 1
            return real_parse(raw, path)

        def read(reader, path, **kwargs):
            if Path(path) == self.other:
                reads[str(path)] += 1
            return real_read(reader, path, **kwargs)

        with patch.object(operations, "parse_carrier", parse), patch.object(subjects.ReadContext, "read", read):
            first = self.stage(reviewed)
            self.assertEqual({self.other_raw: 1}, dict(parses))
            self.assertGreaterEqual(reads[str(self.other)], 4)
            second = self.stage(reviewed)
            self.assertEqual({self.other_raw: 2}, dict(parses), "reuse must be invocation-local")
            self.assertGreaterEqual(reads[str(self.other)], 8)
        self.assertEqual(reviewed, first["preview"])
        self.assertEqual(reviewed, second["preview"])
        self.assertNotEqual(first["stage_root"], second["stage_root"])
        self.assertEqual(self.fixture.original, self.source.read_bytes())

    def test_changed_original_bytes_are_reparsed_and_competing_identity_refuses_stage(self):
        reviewed = self.fixture.preview()
        changed = self.other_raw.replace(b"CA-P-7802", b"CA-P-7801")
        parsed = Counter()
        real_parse, real_write = operations.parse_carrier, staging._write_candidate
        injected = False

        def parse(raw, path):
            if Path(path) == self.other:
                parsed[raw] += 1
            return real_parse(raw, path)

        def write(root, path, raw):
            nonlocal injected
            result = real_write(root, path, raw)
            if not injected:
                injected = True
                self.other.write_bytes(changed)
            return result

        with patch.object(operations, "parse_carrier", parse), patch.object(staging, "_write_candidate", write):
            with self.assertRaises(operations.ToolError) as caught:
                self.stage(reviewed)
        self.assertTrue(injected)
        self.assertEqual("subject-identity-duplicate", caught.exception.code)
        self.assertEqual({self.other_raw: 1, changed: 1}, dict(parsed))
        self.assertTrue(caught.exception.details["retained_artifacts"])
        self.assertFalse(list((self.root / ".caprmedio_tmp/subject-preview").rglob("manifest.json")))
        self.assertEqual(self.fixture.original, self.source.read_bytes())

    def test_fresh_currentness_still_detects_changed_bytes_during_read_audit(self):
        real_read = subjects.ReadContext.read
        injected = False

        def read(reader, path, **kwargs):
            nonlocal injected
            raw = real_read(reader, path, **kwargs)
            if Path(path) == self.other and not injected:
                injected = True
                self.other.write_bytes(raw + b"\nExternal change.\n")
            return raw

        with patch.object(subjects.ReadContext, "read", read):
            with self.assertRaises(operations.ToolError) as caught:
                self.fixture.preview()
        self.assertTrue(injected)
        self.assertEqual("subject-source-changed", caught.exception.code)
        self.assertFalse((self.root / ".caprmedio_tmp/subject-preview").exists())

    def test_new_duplicate_after_initial_preview_is_not_hidden_by_parse_reuse(self):
        reviewed = self.fixture.preview()
        duplicate = self.other.with_name("CA-P-7801--new-claim.md")
        real_write = staging._write_candidate
        injected = False

        def write(root, path, raw):
            nonlocal injected
            result = real_write(root, path, raw)
            if not injected:
                injected = True
                duplicate.write_bytes(self.fixture.original)
            return result

        with patch.object(staging, "_write_candidate", write):
            with self.assertRaises(operations.ToolError) as caught:
                self.stage(reviewed)
        self.assertTrue(injected)
        self.assertEqual("subject-identity-duplicate", caught.exception.code)
        self.assertTrue(caught.exception.details["retained_artifacts"])
        self.assertEqual(self.fixture.original, self.source.read_bytes())

    def test_ignored_symlink_becoming_regular_selected_claim_is_reexamined(self):
        link = self.fixture.excluded("atom_id: CA-C-7901\nstatus: Active")
        link.unlink()
        link.symlink_to(self.root / "missing-unrelated-target")
        reviewed = self.fixture.preview()
        real_write = staging._write_candidate
        injected = False

        def write(root, path, raw):
            nonlocal injected
            result = real_write(root, path, raw)
            if not injected:
                injected = True
                link.unlink()
                link.write_bytes(self.fixture.original)
            return result

        with patch.object(staging, "_write_candidate", write):
            with self.assertRaises(operations.ToolError) as caught:
                self.stage(reviewed)
        self.assertTrue(injected)
        self.assertEqual("subject-identity-duplicate", caught.exception.code)
        self.assertTrue(caught.exception.details["retained_artifacts"])

    def test_next_invocation_does_not_reuse_success_after_new_role_symlink(self):
        self.assertEqual(1, self.fixture.preview()["count"])
        link = self.root / ".caprmedio_caprmedio/new_owner/03_plan"
        link.parent.mkdir()
        link.symlink_to(self.root / "missing-role-target", target_is_directory=True)
        with self.assertRaises(operations.ToolError) as caught:
            self.fixture.preview()
        self.assertEqual("subject-identity-inventory-unavailable", caught.exception.code)
        self.assertFalse((self.root / ".caprmedio_tmp/subject-preview").exists())


if __name__ == "__main__":
    unittest.main()
