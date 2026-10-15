"""Native direct preparation guards: reviewed seal first, scoped identity claims."""
from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOOLS))

import atom_operations as operations
import atom_subject_patch as subject_patch
import atom_subject_stage as staging
import test_nonarchived_subject_preview as fixtures


STAMP = "2026-10-14 10:20:30 +0400"
OTHER_STAMP = "2026-10-14 10:20:31 +0400"


class DirectPreparationGuardTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.NonarchivedSubjectPreviewTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.source = self.fixture._plan("Active", number=7801)
        self.items = self.fixture._payload(self.source)
        self.original = self.source.read_bytes()

    def preview(self, items=None, timestamp=STAMP):
        return subject_patch.preview_subject_patches(
            self.root, self.items if items is None else items,
            timestamp=timestamp, subject_profile="legacy")

    def ledger(self):
        return {p.relative_to(self.root).as_posix(): p.read_bytes() if p.is_file() else None
                for p in self.root.rglob("*")}

    def excluded(self, header, name="CA-C-7901--unrelated.md"):
        path = self.source.parent.parent / "01_concern" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("---\n" + header + "\n---\nUnrelated legacy content\n")
        return path

    def assert_no_create_refusal(self, *, expected, items=None, timestamp=STAMP):
        before = self.ledger()
        with patch.object(operations, "_raw_revision_parent", wraps=operations._raw_revision_parent) as parent:
            with self.assertRaises(operations.ToolError) as caught:
                staging.stage_subject_preview(
                    self.root, self.items if items is None else items,
                    timestamp=timestamp, subject_profile="legacy", expected_preview_sha256=expected)
        self.assertEqual("subject-stage-preview-mismatch", caught.exception.code)
        self.assertFalse(any(call.kwargs.get("create") is True for call in parent.call_args_list))
        self.assertEqual(before, self.ledger())
        self.assertFalse((self.root / ".caprmedio_tmp/subject-preview").exists())

    def test_mismatched_native_seal_refuses_before_any_scratch_creation(self):
        self.assert_no_create_refusal(expected="0" * 64)

    def test_changed_request_or_illustrative_time_cannot_reuse_reviewed_seal(self):
        reviewed = self.preview()
        changed = copy.deepcopy(self.items)
        changed[0]["subject_patches"][0]["new"] = "Atom/State2"
        self.assert_no_create_refusal(expected=reviewed["preview_sha256"], items=changed)
        self.assert_no_create_refusal(expected=reviewed["preview_sha256"], timestamp=OTHER_STAMP)

    def test_changed_direct_stage_cannot_omit_time_even_if_fresh_clock_matches_seal(self):
        reviewed = self.preview()
        with patch.object(subject_patch, "_preview_timestamp", return_value=STAMP):
            self.assert_no_create_refusal(expected=reviewed["preview_sha256"], timestamp=None)

    def test_stage_uses_own_matching_preview_and_same_time_final_recheck(self):
        reviewed = self.preview()
        before = self.fixture._snapshot()
        with patch.object(staging, "preview_subject_patches", wraps=subject_patch.preview_subject_patches) as planner:
            result = staging.stage_subject_preview(
                self.root, self.items, timestamp=STAMP, subject_profile="legacy",
                expected_preview_sha256=reviewed["preview_sha256"])
        self.assertEqual(reviewed, result["preview"])
        self.assertGreaterEqual(planner.call_count, 2)
        self.assertTrue(all(call.kwargs["timestamp"] == STAMP for call in planner.call_args_list))
        for name, raw in before.items():
            self.assertEqual(raw, (self.root / name).read_bytes())
        self.assertEqual(self.original, self.source.read_bytes())

    def test_all_noop_seal_has_null_time_and_exact_source_candidate(self):
        items = self.fixture._payload(self.source, patches=False)
        reviewed = self.preview(items, timestamp=None)
        result = staging.stage_subject_preview(
            self.root, items, timestamp=None, subject_profile="legacy",
            expected_preview_sha256=reviewed["preview_sha256"])
        self.assertEqual(reviewed, result["preview"])
        self.assertTrue(result["preview"]["noop"])
        self.assertIsNone(result["preview"]["illustrative_updated_at"])
        self.assertEqual(self.original.decode(), result["preview"]["atoms"][0]["proposed_carrier"])
        self.assertEqual(self.original, self.source.read_bytes())

    def test_all_noop_sealed_stage_refuses_nonnull_time_before_creation(self):
        items = self.fixture._payload(self.source, patches=False)
        reviewed = self.preview(items, timestamp=None)
        self.assert_no_create_refusal(expected=reviewed["preview_sha256"], items=items, timestamp=STAMP)

    def test_native_cli_omission_remains_compatible(self):
        result = staging.stage_subject_preview(self.root, self.items, timestamp=STAMP, subject_profile="legacy")
        self.assertEqual(self.preview(), result["preview"])
        self.assertTrue(result["sources_unchanged"])
        noop = self.fixture._payload(self.source, patches=False)
        result = staging.stage_subject_preview(self.root, noop, timestamp=STAMP, subject_profile="legacy")
        self.assertTrue(result["preview"]["noop"])
        self.assertIsNone(result["preview"]["illustrative_updated_at"])

    def test_unrelated_malformed_excluded_identity_headers_do_not_gate_preview(self):
        for header in ("atom_id: [invalid", '"atom_id" : [invalid', "atom_id: CA-C-7901\nbroken: ["):
            with self.subTest(header=header):
                self.excluded(header)
                before = self.ledger()
                result = self.preview()
                self.assertEqual(1, result["count"])
                self.assertEqual(before, self.ledger())

    def test_possible_selected_identity_claims_still_refuse(self):
        cases = (
            ("atom_id: CA-P-7801\nbroken: [", "CA-C-7901--unrelated.md"),
            ('atom_id: "CA-P-\\x37\\x38\\x30\\x31"\nbroken: [', "CA-C-7901--unrelated.md"),
            ('"atom_id" : "CA-P-\\x37\\x38\\x30\\x31"\nbroken: [', "CA-C-7901--unrelated.md"),
            ("atom_id: [invalid", "CA-P-7801--malformed-claim.md"),
        )
        for header, name in cases:
            with self.subTest(header=header):
                created = self.excluded(header, name)
                before = self.ledger()
                with self.assertRaises(operations.ToolError) as caught:
                    self.preview()
                self.assertEqual("subject-identity-inventory-unavailable", caught.exception.code)
                self.assertEqual(before, self.ledger())
                created.unlink()

    def test_terminal_role_directory_symlink_cannot_hide_a_competing_identity(self):
        hidden = self.root / "hidden_competitor"
        hidden.mkdir()
        (hidden / self.source.name).write_bytes(self.original)
        link = self.root / ".caprmedio_caprmedio/other/03_plan"
        link.parent.mkdir(parents=True)
        link.symlink_to(hidden, target_is_directory=True)
        for target_exists in (True, False):
            with self.subTest(target_exists=target_exists):
                if not target_exists:
                    hidden.rename(self.root / "removed_competitor")
                with self.assertRaises(operations.ToolError) as caught:
                    self.preview()
                self.assertEqual("subject-identity-inventory-unavailable", caught.exception.code)
                self.assertEqual(self.original, self.source.read_bytes())
                self.assertFalse((self.root / ".caprmedio_tmp/subject-preview").exists())

    def test_terminal_role_symlink_in_excluded_archive_draft_projection_is_not_an_original(self):
        hidden = self.root / "excluded_competitor"
        hidden.mkdir()
        (hidden / self.source.name).write_bytes(self.original)
        for excluded in ("archive", "draft", "_projection"):
            link = self.root / ".caprmedio_caprmedio/other" / excluded / "03_plan"
            link.parent.mkdir(parents=True, exist_ok=True)
            link.symlink_to(hidden, target_is_directory=True)
        self.assertEqual(1, self.preview()["count"])

    def test_currentness_of_unrelated_excluded_identity_input_is_not_waived(self):
        excluded = self.excluded("atom_id: [invalid")
        original_currentness = subject_patch.ReadContext.currentness
        mutated = False

        def drift(reader):
            nonlocal mutated
            if not mutated and str(excluded) in reader.fingerprints:
                mutated = True
                excluded.write_bytes(excluded.read_bytes() + b"external change\n")
            return original_currentness(reader)

        with patch.object(subject_patch.ReadContext, "currentness", drift):
            with self.assertRaises(operations.ToolError) as caught:
                self.preview()
        self.assertTrue(mutated)
        self.assertEqual("subject-source-changed", caught.exception.code)
        self.assertEqual(self.original, self.source.read_bytes())
        self.assertEqual(hashlib.sha256(self.original).hexdigest(), self.items[0]["expected"]["sha256"])
        self.assertFalse((self.root / ".caprmedio_tmp/subject-preview").exists())


if __name__ == "__main__":
    unittest.main()
