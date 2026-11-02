"""Independent whole-set Subject checks against disposable native Project fixtures."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest


TOOLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import atom_operations as operations  # noqa: E402
import atom_subject_patch as subject_patch  # noqa: E402
import atom_subject_stage as staging  # noqa: E402
import test_subject_patch_by_value_independent as fixtures  # noqa: E402


TIME = "2026-10-14 01:00:00 +0000"
LATER = "2026-10-14 01:01:00 +0000"
CURRENT = ["Atom", "Atom/Revision"]


class SubjectReplaceSetIndependentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.SubjectPatchByValueIndependentTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root, self.path = self.fixture.root, self.fixture.path
        self.assertTrue(self.root.is_relative_to(TOOLS.parents[2] / ".caprmedio_tmp"))

    @staticmethod
    def patch(new=None, *, old=None):
        return {"field": "depends_on", "operation": "replace_set",
                "old": CURRENT.copy() if old is None else old,
                "new": ["Object", "Atom.Version Number"] if new is None else new}

    def source(self, *, newline=b"\n", block=False):
        original = self.fixture.source()
        if block:
            original = original.replace(
                b'  depends_on: [Atom, "Atom/Revision"] # preserve dependency comment',
                b'  # preserve dependency comment\n  depends_on:\n    - Atom\n    - "Atom/Revision"')
        original = original.replace(b"\n", newline)
        self.path.write_bytes(original)
        return original

    def preview(self, patches, *, profile="approved", timestamp=TIME):
        before = self.fixture.ledger()
        try:
            return subject_patch.preview_subject_patches(
                self.root, self.fixture.payload(patches, profile=profile)["atoms"],
                timestamp=timestamp, subject_profile=profile)
        finally:
            self.assertEqual(before, self.fixture.ledger())

    def refused(self, payload, *, stage=False, code=None):
        with self.assertRaises(operations.ToolError) as caught:
            self.fixture.invoke(payload, stage=stage)
        if code is not None:
            self.assertEqual(code, caught.exception.code)
        self.assertFalse((self.root / ".caprmedio_tmp/subject-preview").exists())

    def assert_preserved(self, original, proposed, timestamp=TIME):
        newline = b"\r\n" if b"\r\n" in original else b"\n"
        expected_prefix = (original.split(b"subjects:" + newline, 1)[0]
                           .replace(b"version: 1" + newline, b"version: 2" + newline, 1)
                           .replace(b'updated_at: "2026-01-01 00:00:00 +0000"',
                                    f'updated_at: "{timestamp}"'.encode(), 1))
        self.assertEqual(expected_prefix, proposed.split(b"subjects:" + newline, 1)[0])
        self.assertEqual(original.split(b"relations: {}" + newline, 1)[1],
                         proposed.split(b"relations: {}" + newline, 1)[1])
        self.assertEqual(1, proposed.count(b"# preserve dependency comment"))
        self.assertIn(b"# preserve metadata order" + newline, proposed)
        if newline == b"\r\n":
            self.assertNotIn(b"\n", proposed.replace(b"\r\n", b""))

    def test_exact_current_set_accepts_reordering_and_preserves_unrelated_bytes(self):
        for newline in (b"\n", b"\r\n"):
            for block in (False, True):
                for profile in ("legacy", "approved"):
                    with self.subTest(newline=newline, block=block, profile=profile):
                        original = self.source(newline=newline, block=block)
                        patch = self.patch(old=list(reversed(CURRENT)))
                        atom = self.preview([patch], profile=profile)["atoms"][0]
                        proposed = atom["proposed_carrier"].encode()
                        metadata = operations.parse_carrier(proposed, self.path).metadata
                        self.assertEqual(patch["new"], metadata["subjects"]["depends_on"])
                        self.assertEqual("Atom/Test", metadata["subjects"]["governs"])
                        self.assertEqual(2, atom["after_version"])
                        self.assertFalse(atom["noop"])
                        self.assertEqual([patch], atom["subject_intent"]["subject_patches"])
                        self.assert_preserved(original, proposed)
                        self.assertEqual(original, self.path.read_bytes())

    def test_same_unordered_set_is_an_exact_byte_noop_including_intent(self):
        original = self.source(newline=b"\r\n", block=True)
        patch = self.patch(new=list(reversed(CURRENT)), old=list(reversed(CURRENT)))
        preview = self.preview([patch])
        atom = preview["atoms"][0]
        self.assertTrue(preview["noop"] and atom["noop"])
        self.assertIsNone(preview["illustrative_updated_at"])
        self.assertEqual(original, atom["proposed_carrier"].encode())
        self.assertEqual(1, atom["after_version"])
        self.assertEqual(atom["before_sha256"], atom["after_sha256"])
        self.assertEqual([patch], atom["subject_intent"]["subject_patches"])
        self.assertEqual({"version": 1, "updated_at": "preserve"},
                         atom["subject_intent"]["execution_metadata"])
        self.assertIsNone(atom["subject_intent"]["predecessorArchive"])

    def test_empty_new_set_and_mixed_governs_replacement_are_supported(self):
        original = self.source(newline=b"\r\n")
        patches = [{"field": "governs", "old": "Atom/Test", "new": "Atom.State"},
                   self.patch(new=[])]
        atom = self.preview(patches)["atoms"][0]
        proposed = atom["proposed_carrier"].encode()
        subjects = operations.parse_carrier(proposed, self.path).metadata["subjects"]
        self.assertEqual({"governs": "Atom.State", "depends_on": []}, subjects)
        self.assertEqual(patches, atom["subject_intent"]["subject_patches"])
        self.assert_preserved(original, proposed)

    def test_stale_set_duplicates_invalid_members_and_unknown_shapes_refuse_before_staging(self):
        invalid = [
            self.patch(old=[]), self.patch(old=["Atom"]),
            self.patch(old=CURRENT + ["Object"]), self.patch(old=["Atom", "Atom"]),
            self.patch(new=["Object", "Object"]), self.patch(new=["Atom@State"]),
            self.patch(new=[""]), self.patch(new=[42]), self.patch(new=[["Atom"]]),
            self.patch(new="Atom"), self.patch(old="Atom"),
            {**self.patch(), "index": 0}, {**self.patch(), "operation": "merge"},
            {**self.patch(), "field": "governs"},
        ]
        for patch in invalid:
            for stage in (False, True):
                with self.subTest(patch=patch, stage=stage):
                    self.refused(
                        self.fixture.payload([patch], profile="approved"), stage=stage)
        self.fixture.source(duplicate=True)
        self.refused(self.fixture.payload([self.patch()], profile="approved"))

    def test_entry_and_set_operations_cannot_overlap_in_either_order(self):
        set_patch = self.patch()
        entry = {"field": "depends_on", "old": "Atom", "new": "Object"}
        for patches in ([set_patch, entry], [entry, set_patch], [set_patch, set_patch]):
            with self.subTest(patches=patches):
                self.refused(self.fixture.payload(patches, profile="approved"))

    def test_stale_expected_fields_refuse_before_candidate_exports(self):
        for field, value in (("atom_id", "CA-R-999"), ("version", 2), ("sha256", "0" * 64)):
            with self.subTest(field=field):
                payload = self.fixture.payload([self.patch()], profile="approved")
                payload["atoms"][0]["expected"][field] = value
                self.refused(payload, code="subject-pin-stale", stage=True)

    def test_intent_is_time_independent_retains_operation_and_materializes_without_source_writes(self):
        original = self.source(newline=b"\r\n")
        patches = [self.patch()]
        first = self.preview(patches)["atoms"][0]
        second = self.preview(patches, timestamp=LATER)["atoms"][0]
        self.assertEqual(first["subject_intent_sha256"], second["subject_intent_sha256"])
        self.assertEqual(first["subject_intent"], second["subject_intent"])
        self.assertEqual(patches, first["subject_intent"]["subject_patches"])
        before = self.fixture.ledger()
        prepared = subject_patch.prepare_subject_intent(
            self.root, first["subject_intent"]["target"], patches, subject_profile="approved")
        self.assertEqual(first["subject_intent_sha256"], prepared["subject_intent_sha256"])
        actual = subject_patch.materialize_subject_intent(self.root, prepared, LATER)
        self.assertEqual(second["proposed_carrier"].encode(), actual["carrier_bytes"])
        tampered = copy.deepcopy(prepared)
        tampered["subject_intent"]["subject_patches"][0]["operation"] = "merge"
        with self.assertRaises(operations.ToolError):
            subject_patch.materialize_subject_intent(self.root, tampered, LATER)
        self.assertEqual(before, self.fixture.ledger())
        self.assertEqual(original, self.path.read_bytes())

    def test_stage_readback_matches_changed_and_noop_previews_and_keeps_authority_unchanged(self):
        original = self.source(newline=b"\r\n", block=True)
        for patch in (self.patch(), self.patch(new=list(reversed(CURRENT)))):
            with self.subTest(patch=patch):
                items = self.fixture.payload([patch], profile="approved")["atoms"]
                expected = self.preview([patch])
                before = self.fixture.ledger()
                result = staging.stage_subject_preview(
                    self.root, items, timestamp=TIME, subject_profile="approved")
                self.assertEqual(expected, result["preview"])
                self.assertTrue(result["staging_only"] and result["sources_unchanged"])
                manifest_path = self.root / result["manifest_path"]
                self.assertEqual(hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
                                 result["manifest_sha256"])
                manifest = json.loads(manifest_path.read_bytes())
                self.assertEqual(expected["preview_sha256"], manifest["preview_sha256"])
                candidate = manifest["atoms"][0]["candidate"]
                raw = (self.root / candidate["path"]).read_bytes()
                self.assertEqual(expected["atoms"][0]["proposed_carrier"].encode(), raw)
                self.assertEqual(hashlib.sha256(raw).hexdigest(), candidate["sha256"])
                self.assertEqual(expected["atoms"][0]["subject_intent_sha256"],
                                 manifest["atoms"][0]["subject_intent_sha256"])
                self.assertEqual(before, self.fixture.ledger())
                self.assertEqual(original, self.path.read_bytes())


if __name__ == "__main__":
    unittest.main()
