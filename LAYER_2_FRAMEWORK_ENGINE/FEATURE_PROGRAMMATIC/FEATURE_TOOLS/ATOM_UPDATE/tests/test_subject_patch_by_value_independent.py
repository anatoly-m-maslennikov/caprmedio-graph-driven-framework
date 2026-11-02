"""Actual native Subject preview/staging, selected by exact old values only."""

from __future__ import annotations

import argparse
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
import test_nonarchived_subject_preview as fixtures  # noqa: E402
from atom_subject_patch import prepare_subject_intent, materialize_subject_intent  # noqa: E402
from subject_notation import SubjectNotationError, parse_subject  # noqa: E402


class SubjectPatchByValueIndependentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.NonarchivedSubjectPreviewTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.path = self.fixture.fixture.target
        self.base = self.path.read_bytes()
        self.input = self.root / ".caprmedio_tmp" / "independent-input.json"
        self.input.parent.mkdir()
        self.source()

    def source(self, *, newline=b"\n", reverse=False, duplicate=False):
        values = b'["Atom/Revision", Atom]' if reverse else b'[Atom, "Atom/Revision"]'
        if duplicate:
            values = b'["Atom/Revision", "Atom/Revision"]'
        raw = self.base.replace(b"  depends_on: []", b"  depends_on: " + values + b" # preserve dependency comment")
        raw = raw.replace(b"version: 1\n", b"# preserve metadata order\nversion: 1\n\n")
        raw = raw.replace(b"Fixture details.\n", "Fixture details.  \n\nLiteral Atom/Revision and café stay unchanged.\n\n".encode())
        self.path.write_bytes(raw.replace(b"\n", newline))
        return self.path.read_bytes()

    def payload(self, patches, *, profile="legacy"):
        raw = self.path.read_bytes()
        return {"subject_profile": profile, "atoms": [{
            "selector": self.path.relative_to(self.root).as_posix(),
            "expected": {"atom_id": "CA-R-100", "version": 1, "sha256": hashlib.sha256(raw).hexdigest()},
            "subject_patches": copy.deepcopy(patches),
        }]}

    def ledger(self):
        control = self.root / ".caprmedio_caprmedio"
        return {path.relative_to(self.root).as_posix(): (path.read_bytes(), path.stat().st_mode & 0o777)
                for path in control.rglob("*") if path.is_file()}

    def invoke(self, payload, *, stage=False, apply=False):
        self.input.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        before = self.ledger()
        try:
            return operations.run_update(self.root, argparse.Namespace(
                input=str(self.input), apply=apply, stage_preview=stage))
        finally:
            self.assertEqual(before, self.ledger(), "Native preview/staging changed authoritative evidence")
            self.assertFalse((self.path.parent / "archive" / (self.path.stem + "@1.md")).exists())
            self.assertFalse((self.root / ".caprmedio_caprmedio/_journal").exists())
            self.assertFalse((self.root / ".caprmedio_runtime").exists())

    @staticmethod
    def patch(old="Atom/Revision", new="Atom/Revision/State"):
        return {"field": "depends_on", "old": old, "new": new}

    def assert_refused(self, payload, code, *, stage=False, apply=False):
        with self.assertRaises(operations.ToolError) as caught:
            self.invoke(payload, stage=stage, apply=apply)
        self.assertEqual(code, caught.exception.code)
        self.assertFalse((self.root / ".caprmedio_tmp/subject-preview").exists())

    def assert_preview(self, preview, original, patches, *, noop=False):
        atom = preview["atoms"][0]
        expected = original
        if not noop:
            for patch in patches:
                old = json.dumps(patch["old"], ensure_ascii=False).encode()
                new = json.dumps(patch["new"], ensure_ascii=False).encode()
                self.assertEqual(1, expected.count(old))
                expected = expected.replace(old, new, 1)
            newline = b"\r\n" if b"\r\n" in original else b"\n"
            expected = expected.replace(b"version: 1" + newline, b"version: 2" + newline, 1)
            expected = expected.replace(b'updated_at: "2026-01-01 00:00:00 +0000"',
                                        f'updated_at: "{preview["illustrative_updated_at"]}"'.encode(), 1)
        self.assertEqual(expected, atom["proposed_carrier"].encode())
        self.assertEqual(hashlib.sha256(original).hexdigest(), atom["before_sha256"])
        self.assertEqual(hashlib.sha256(expected).hexdigest(), atom["after_sha256"])
        self.assertEqual(1 if noop else 2, atom["after_version"])
        self.assertEqual(noop, atom["noop"])
        self.assertEqual(patches, atom["subject_intent"]["subject_patches"])
        self.assertTrue(all(set(patch) == {"field", "old", "new"}
                            for patch in atom["subject_intent"]["subject_patches"]))
        unsigned = {key: value for key, value in preview.items() if key != "preview_sha256"}
        canonical = json.dumps(unsigned, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
        self.assertEqual(hashlib.sha256(canonical.encode()).hexdigest(), preview["preview_sha256"])
        if noop:
            self.assertIsNone(preview["illustrative_updated_at"])
            self.assertIsNone(atom["subject_intent"]["predecessorArchive"])
        return expected

    def test_reordered_lists_lf_crlf_and_both_profiles_replace_only_the_exact_scalar(self):
        patches = [self.patch()]
        for newline in (b"\n", b"\r\n"):
            for reverse in (False, True):
                for profile in ("legacy", "approved"):
                    with self.subTest(newline=newline, reverse=reverse, profile=profile):
                        original = self.source(newline=newline, reverse=reverse)
                        preview = self.invoke(self.payload(patches, profile=profile))
                        self.assert_preview(preview, original, patches)
                        record = preview["atoms"][0]["patches"][0]
                        self.assertEqual(0 if reverse else 1, record["index"])
                        text = original.decode()
                        nl = newline.decode()
                        frontmatter = text.split(nl, 1)[1].split(nl + "---" + nl, 1)[0]
                        start = frontmatter.index('"Atom/Revision"')
                        self.assertEqual({"start": start, "end": start + len('"Atom/Revision"')}, record["span"])
                        self.assertFalse((self.root / ".caprmedio_tmp/subject-preview").exists())

    def test_public_staging_exports_exact_bytes_and_closed_by_value_intent(self):
        original = self.source(newline=b"\r\n", reverse=True)
        patches = [self.patch()]
        result = self.invoke(self.payload(patches, profile="approved"), stage=True)
        expected = self.assert_preview(result["preview"], original, patches)
        self.assertTrue(result["staging_only"] and result["illustrative"] and result["sources_unchanged"])
        manifest_path = self.root / result["manifest_path"]
        self.assertEqual(hashlib.sha256(manifest_path.read_bytes()).hexdigest(), result["manifest_sha256"])
        manifest = json.loads(manifest_path.read_bytes())
        self.assertEqual(result["preview"]["preview_sha256"], manifest["preview_sha256"])
        candidate = manifest["atoms"][0]["candidate"]
        self.assertEqual(expected, (self.root / candidate["path"]).read_bytes())
        self.assertEqual(hashlib.sha256(expected).hexdigest(), candidate["sha256"])
        self.assertEqual(Path(".caprmedio_tmp/subject-preview"), Path(result["stage_root"]).parent)
        self.assertEqual(original, self.path.read_bytes())

    def test_missing_prefix_case_and_duplicate_old_values_refuse(self):
        for old in ("Missing", "Atom/Rev", "atom/Revision"):
            for stage in (False, True):
                with self.subTest(old=old, stage=stage):
                    self.assert_refused(self.payload([self.patch(old=old)]), "subject-old-stale", stage=stage)
        self.source(duplicate=True)
        for stage in (False, True):
            with self.subTest(duplicate=True, stage=stage):
                self.assert_refused(self.payload([self.patch()]), "subject-dependency-duplicate", stage=stage)

    def test_every_caller_index_is_refused_even_if_it_would_select_the_correct_value(self):
        for index in (0, 1, True, -1, "1"):
            for stage in (False, True):
                with self.subTest(index=index, stage=stage):
                    self.assert_refused(self.payload([{**self.patch(), "index": index}]), "subject-patch-invalid", stage=stage)

    def test_duplicate_occurrence_result_and_chained_old_resolution_refuse(self):
        for patches, code in (
            ([self.patch(), self.patch(new="Atom/Revision/Other")], "subject-occurrence-duplicate"),
            ([self.patch(new="Atom")], "subject-dependency-duplicate"),
            ([self.patch(), self.patch(old="Atom/Revision/State", new="Atom/Revision/Other")], "subject-old-stale"),
        ):
            for stage in (False, True):
                with self.subTest(patches=patches, stage=stage):
                    self.assert_refused(self.payload(patches), code, stage=stage)

    def test_exact_noops_preserve_original_bytes_metadata_and_no_history_even_when_staged(self):
        original = self.source(newline=b"\r\n")
        for patches in ([], [self.patch(new="Atom/Revision")]):
            with self.subTest(patches=patches):
                self.assert_preview(self.invoke(self.payload(patches)), original, patches, noop=True)
                staged = self.invoke(self.payload(patches), stage=True)
                self.assert_preview(staged["preview"], original, patches, noop=True)
                manifest = json.loads((self.root / staged["manifest_path"]).read_bytes())
                self.assertEqual(original, (self.root / manifest["atoms"][0]["candidate"]["path"]).read_bytes())

    def test_invalid_notation_stale_expected_state_and_standalone_apply_guards_remain(self):
        with self.assertRaises(SubjectNotationError) as expected:
            parse_subject("Atom@State", subject_profile="approved")
        self.assert_refused(self.payload([self.patch(new="Atom@State")], profile="approved"), expected.exception.code)
        for field, value in (("sha256", "0" * 64), ("version", 2), ("atom_id", "CA-R-999")):
            with self.subTest(field=field):
                payload = self.payload([self.patch()])
                payload["atoms"][0]["expected"][field] = value
                self.assert_refused(payload, "subject-pin-stale", stage=True)
        self.assert_refused(self.payload([self.patch()]), "subject-apply-not-admitted", apply=True)
        self.assert_refused(self.payload([self.patch()]), "subject-stage-apply-rejected", stage=True, apply=True)

    def test_native_describe_has_no_public_index_selector(self):
        description = operations.describe("ATOM_UPDATE")["subject_preview"]
        self.assertEqual(["field", "old", "new"], description["patch_fields"])
        self.assertFalse(description["apply_supported"])
        self.assertTrue(description["staging_only"])

    def test_public_pure_intent_replay_remains_by_value_and_rejects_an_indexed_prepared_request(self):
        original = self.source(newline=b"\r\n", reverse=True)
        patches = [self.patch()]
        preview = self.invoke(self.payload(patches, profile="approved"))
        target = preview["atoms"][0]["subject_intent"]["target"]
        before = self.ledger()
        prepared = prepare_subject_intent(self.root, target, patches, subject_profile="approved")
        self.assertEqual(patches, prepared["subject_intent"]["subject_patches"])
        requested_time = "2026-10-14 00:45:00 +0000"
        materialized = materialize_subject_intent(self.root, prepared, requested_time)
        expected = (original.replace(b'"Atom/Revision"', b'"Atom/Revision/State"', 1)
                    .replace(b"version: 1\r\n", b"version: 2\r\n", 1)
                    .replace(b'updated_at: "2026-01-01 00:00:00 +0000"',
                             f'updated_at: "{requested_time}"'.encode(), 1))
        self.assertEqual(expected, materialized["carrier_bytes"])
        indexed = copy.deepcopy(prepared)
        indexed["subject_intent"]["subject_patches"][0]["index"] = 0
        with self.assertRaises(operations.ToolError) as refused:
            materialize_subject_intent(self.root, indexed, requested_time)
        self.assertEqual("subject-patch-invalid", refused.exception.code)
        self.assertEqual(before, self.ledger())
        self.assertEqual(original, self.path.read_bytes())


if __name__ == "__main__":
    unittest.main()
