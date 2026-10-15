"""Full dependency-set replacement through actual pinned Subject preparation."""
from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import sys
import unittest

TOOLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOOLS))

import atom_operations as operations
import atom_subject_patch as subject_patch
from lifecycle_intents import carrier_descriptor
import test_nonarchived_subject_preview as fixtures


class SubjectReplaceSetTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.NonarchivedSubjectPreviewTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.path = self.fixture._plan("Active")
        self.original = self.path.read_bytes()

    def payload(self, patches):
        item = self.fixture._payload(self.path)[0]
        item["subject_patches"] = patches
        return [item]

    @staticmethod
    def patch(new, old=None):
        return {"field": "depends_on", "operation": "replace_set",
                "old": ["Atom/Revision", "Atom"] if old is None else old, "new": new}

    def preview(self, patches, profile="legacy"):
        before = self.fixture._snapshot()
        result = subject_patch.preview_subject_patches(
            self.root, self.payload(patches), timestamp="2026-10-14 10:20:30 +0400", subject_profile=profile)
        self.assertEqual(before, self.fixture._snapshot())
        return result

    def test_changed_sets_use_explicit_membership_and_preserve_comments_crlf_body(self):
        layouts = [
            '  depends_on: [Atom, # café first\r\n    "Atom/Revision"] # trailing\r\n',
            '  depends_on:\r\n    - Atom # café first\r\n    # middle\r\n    - "Atom/Revision" # trailing\r\n',
        ]
        for layout in layouts:
            for new in (["Atom"], ["Atom", "Atom/Status", "Atom/Scope"], []):
                with self.subTest(layout=layout, new=new):
                    self.path.write_bytes(self.original.replace(b'  depends_on: [Atom, "Atom/Revision"]\r\n', layout.encode()))
                    source = self.path.read_bytes()
                    preview = self.preview([self.patch(new)])
                    atom = preview["atoms"][0]
                    proposed = atom["proposed_carrier"].encode()
                    metadata = operations.parse_carrier(proposed, self.path).metadata
                    self.assertEqual(new, metadata["subjects"]["depends_on"])
                    self.assertEqual(8, metadata["version"])
                    self.assertEqual(source.split(b"---\r\n", 2)[2], proposed.split(b"---\r\n", 2)[2])
                    self.assertEqual(source[:source.index(b"  depends_on:")], proposed[:proposed.index(b"  depends_on:")].replace(
                        b"version: 8\r\n", b"version: 7\r\n").replace(
                        b'updated_at: "2026-10-14 10:20:30 +0400"', b'updated_at: "2026-01-01 00:00:00 +0000"'))
                    for comment in ("# café first", "# trailing"):
                        self.assertIn(comment.encode(), proposed)
                    if "# middle" in layout:
                        self.assertIn(b"# middle", proposed)
                    self.assertNotIn(b"\n", proposed.replace(b"\r\n", b""))
                    self.assertEqual(hashlib.sha256(proposed).hexdigest(), atom["after_sha256"])

    def test_permuted_equal_sets_are_byte_exact_noops_in_both_profiles(self):
        for profile in ("legacy", "approved"):
            result = self.preview([self.patch(["Atom/Revision", "Atom"], old=["Atom", "Atom/Revision"])], profile)
            atom = result["atoms"][0]
            self.assertTrue(result["noop"])
            self.assertEqual(self.original, atom["proposed_carrier"].encode())
            self.assertEqual(7, atom["after_version"])
            self.assertIsNone(result["illustrative_updated_at"])
            self.assertIsNone(atom["subject_intent"]["predecessorArchive"])
            self.assertEqual({"version": 7, "updated_at": "preserve"}, atom["subject_intent"]["execution_metadata"])

    def test_empty_flow_collection_accepts_an_explicit_new_set(self):
        self.path.write_bytes(self.original.replace(b'[Atom, "Atom/Revision"]', b'[]'))
        result = self.preview([self.patch(["Atom"], old=[])])
        proposed = result["atoms"][0]["proposed_carrier"].encode()
        self.assertEqual(["Atom"], operations.parse_carrier(proposed, self.path).metadata["subjects"]["depends_on"])

    def test_independent_governs_patch_and_intent_materialization_retain_operation(self):
        patches = [self.patch(["Atom.Status", "Atom"]), {"field": "governs", "old": "Atom/Status", "new": "Atom.Status"}]
        preview = self.preview(patches, "approved")
        atom = preview["atoms"][0]
        self.assertEqual(patches, atom["subject_intent"]["subject_patches"])
        target = carrier_descriptor(self.root, self.path.relative_to(self.root).as_posix())
        prepared = subject_patch.prepare_subject_intent(self.root, target, patches, subject_profile="approved")
        self.assertEqual(atom["subject_intent_sha256"], prepared["subject_intent_sha256"])
        materialized = subject_patch.materialize_subject_intent(self.root, prepared, "2026-10-14 10:20:30 +0400")
        self.assertEqual(atom["proposed_carrier"].encode(), materialized["carrier_bytes"])
        self.assertEqual(self.original, self.path.read_bytes())

    def test_invalid_requests_fail_before_writes(self):
        good = self.patch(["Atom"])
        invalid = [
            ({**good, "old": ["Atom"]}, "subject-old-stale"),
            ({**good, "old": "Atom"}, "subject-set-invalid"),
            ({**good, "new": None}, "subject-set-invalid"),
            ({**good, "old": ["Atom", "Atom"]}, "subject-dependency-duplicate"),
            ({**good, "new": ["Atom", "Atom"]}, "subject-dependency-duplicate"),
            ({**good, "new": ["Atom", 1]}, "subject-value-invalid"),
            ({**good, "new": [""]}, "subject-value-invalid"),
            ({**good, "index": 0}, "subject-patch-invalid"),
            ({**good, "field": "governs"}, "subject-patch-invalid"),
        ]
        for patch, code in invalid:
            with self.subTest(patch=patch):
                before = self.fixture._snapshot()
                with self.assertRaises(operations.ToolError) as caught:
                    self.preview([patch])
                self.assertEqual(code, caught.exception.code)
                self.assertEqual(before, self.fixture._snapshot())

    def test_full_set_cannot_overlap_dependency_entry_edits_in_either_order(self):
        full = self.patch(["Atom"])
        entry = {"field": "depends_on", "old": "Atom/Revision", "new": "Atom/Status"}
        for patches in ([full, entry], [entry, full], [full, copy.deepcopy(full)]):
            with self.assertRaises(operations.ToolError) as caught:
                self.preview(patches)
            self.assertEqual("subject-occurrence-duplicate", caught.exception.code)

    def test_missing_list_is_not_implicitly_added(self):
        self.path.write_bytes(self.original.replace(b'  depends_on: [Atom, "Atom/Revision"]\r\n', b''))
        with self.assertRaises(operations.ToolError) as caught:
            self.preview([self.patch(["Atom"], old=[])])
        self.assertEqual("subject-shape-invalid", caught.exception.code)


if __name__ == "__main__":
    unittest.main()
