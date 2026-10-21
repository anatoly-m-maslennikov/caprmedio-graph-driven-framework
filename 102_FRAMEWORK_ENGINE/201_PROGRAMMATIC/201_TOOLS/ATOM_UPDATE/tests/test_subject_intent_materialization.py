from __future__ import annotations

import copy
import hashlib
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOOLS))

import atom_operations as operations  # noqa: E402
import atom_subject_patch as subject_patch  # noqa: E402
from lifecycle_intents import carrier_descriptor  # noqa: E402
from subject_notation import get_profile  # noqa: E402
import test_nonarchived_subject_preview as preview_fixture  # noqa: E402


class SubjectIntentMaterializationTests(unittest.TestCase):
    """Pure planning uses actual source authority, never a mocked validator."""

    def setUp(self) -> None:
        self.fixture = preview_fixture.NonarchivedSubjectPreviewTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.path = self.fixture._plan("Done")
        self.target = carrier_descriptor(self.root, self.path.relative_to(self.root).as_posix())
        self.patches = self.fixture._payload(self.path)[0]["subject_patches"]

    def _prepare(self, *, subject_profile: str = "legacy", patches: list | None = None) -> dict:
        return subject_patch.prepare_subject_intent(
            self.root, self.target, self.patches if patches is None else patches,
            subject_profile=subject_profile,
        )

    def _error(self, code: str, function, *args, **kwargs) -> None:
        with self.assertRaises(operations.ToolError) as raised:
            function(*args, **kwargs)
        self.assertEqual(code, raised.exception.code)

    def test_intent_exact_shape_hash_and_old_metadata_proposal(self) -> None:
        before = self.fixture._snapshot()
        prepared = self._prepare()
        intent = prepared["subject_intent"]
        self.assertEqual({"schema_version", "target", "subject_profile", "subject_profile_evidence",
                          "subject_patches", "proposal", "execution_metadata", "predecessorArchive", "noop"}, set(intent))
        self.assertEqual(self.target, intent["target"])
        self.assertEqual(self.patches, intent["subject_patches"])
        self.assertEqual({"version": 8, "updated_at": "actual_effect_time"}, intent["execution_metadata"])
        original = self.path.read_bytes()
        intended = original.replace(b'governs: "Atom/Status"', b'governs: "Atom/State"')
        self.assertEqual(intended, prepared["intended_carrier"].encode("utf-8"))
        frontmatter, content = subject_patch._raw_frontmatter(operations, intended.decode("utf-8"))
        self.assertEqual({"frontmatter": frontmatter, "content": content}, prepared["proposed"])
        self.assertEqual({"frontmatter_digest": hashlib.sha256(frontmatter.encode()).hexdigest(),
                          "content_digest": hashlib.sha256(content.encode()).hexdigest(),
                          "sha256": hashlib.sha256(intended).hexdigest()}, intent["proposal"])
        archive = self.path.parent.parent / "archived" / f"{self.path.stem}@7.md"
        self.assertEqual({"atom_id": "CA-P-501", "version": 7, "path": archive.relative_to(self.root).as_posix(),
                          "sha256": hashlib.sha256(original).hexdigest(), "lifecycle": "archived"}, intent["predecessorArchive"])
        canonical = json.dumps(intent, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
        self.assertEqual(hashlib.sha256(canonical.encode("utf-8")).hexdigest(), prepared["subject_intent_sha256"])
        self.assertEqual(before, self.fixture._snapshot())

    def test_preview_exposes_same_intent_without_binding_illustrative_time(self) -> None:
        prepared = self._prepare()
        first = subject_patch.preview_subject_patches(self.root, self.fixture._payload(self.path), timestamp="2026-10-12 10:20:30 +0400")
        second = subject_patch.preview_subject_patches(self.root, self.fixture._payload(self.path), timestamp="2026-10-13 11:21:31 +0400")
        for preview in (first, second):
            self.assertEqual(prepared["subject_intent"], preview["atoms"][0]["subject_intent"])
            self.assertEqual(prepared["subject_intent_sha256"], preview["atoms"][0]["subject_intent_sha256"])
        self.assertNotEqual(first["preview_sha256"], second["preview_sha256"])
        self.assertNotEqual(first["atoms"][0]["after_sha256"], second["atoms"][0]["after_sha256"])

    def test_materialization_changes_only_declared_subject_and_effect_metadata(self) -> None:
        before = self.fixture._snapshot()
        prepared = self._prepare()
        for actual_time in ("2026-10-12 10:20:30 +0400", "2026-10-13 11:21:31 +0400"):
            with self.subTest(actual_time=actual_time):
                result = subject_patch.materialize_subject_intent(self.root, prepared, actual_time)
                expected = prepared["intended_carrier"].encode().replace(b"version: 7\r\n", b"version: 8\r\n")
                expected = expected.replace(b'updated_at: "2026-01-01 00:00:00 +0000"', f'updated_at: "{actual_time}"'.encode())
                self.assertEqual(expected, result["carrier_bytes"])
                self.assertEqual({"version": 8, "updated_at": actual_time, "after_sha256": hashlib.sha256(expected).hexdigest()}, result["materialization"])
        self.assertEqual(before, self.fixture._snapshot())

    def test_noop_has_no_history_or_effect_metadata_and_preserves_all_bytes(self) -> None:
        prepared = self._prepare(patches=[])
        intent = prepared["subject_intent"]
        self.assertTrue(intent["noop"])
        self.assertIsNone(intent["predecessorArchive"])
        self.assertEqual({"version": 7, "updated_at": "preserve"}, intent["execution_metadata"])
        result = subject_patch.materialize_subject_intent(self.root, prepared, None)
        self.assertEqual(self.path.read_bytes(), result["carrier_bytes"])
        self.assertEqual({"version": 7, "updated_at": self.target["updated_at"], "after_sha256": self.target["digest"]}, result["materialization"])

    def test_ordered_dependency_patches_and_lowercase_selector_are_literal(self) -> None:
        literal = 'atom(atom_id="CA-P-501").Status'
        patches = [
            {"field": "depends_on", "old": "Atom/Revision", "new": "Atom.Revision"},
            {"field": "governs", "old": "Atom/Status", "new": literal},
            {"field": "depends_on", "old": "Atom", "new": "Atom"},
        ]
        prepared = self._prepare(subject_profile="approved", patches=patches)
        self.assertEqual(patches, prepared["subject_intent"]["subject_patches"])
        metadata = operations.parse_carrier(prepared["intended_carrier"].encode(), self.path).metadata
        self.assertEqual(literal, metadata["subjects"]["governs"])
        self.assertEqual(["Atom", "Atom.Revision"], metadata["subjects"]["depends_on"])
        self.assertEqual("not_performed", prepared["subject_intent"]["subject_profile_evidence"]["native_admission"])
        materialized = subject_patch.materialize_subject_intent(self.root, prepared, "2026-10-14 00:40:00 +0400")
        self.assertEqual(["Atom", "Atom.Revision"], operations.parse_carrier(materialized["carrier_bytes"], self.path).metadata["subjects"]["depends_on"])

    def test_target_descriptor_is_closed_and_all_fields_are_pinned(self) -> None:
        for field in self.target:
            with self.subTest(field=field):
                target = dict(self.target)
                target[field] = 8 if field == "version" else "changed"
                with self.assertRaises(operations.ToolError):
                    subject_patch.prepare_subject_intent(self.root, target, self.patches)
        target = {**self.target, "unknown": True}
        self._error("subject-target-invalid", subject_patch.prepare_subject_intent, self.root, target, self.patches)
        target = dict(self.target, version=7.0)
        self._error("subject-expected-invalid", subject_patch.prepare_subject_intent, self.root, target, self.patches)

    def test_materialization_rejects_unknown_fields_hash_and_proposal_tampering(self) -> None:
        prepared = self._prepare()
        tampered = copy.deepcopy(prepared)
        tampered["subject_intent"]["unknown"] = True
        self._error("subject-intent-invalid", subject_patch.materialize_subject_intent, self.root, tampered, "2026-10-12 10:20:30 +0400")
        for field, value in (("subject_intent_sha256", "0" * 64), ("intended_carrier", "forged"), ("proposed", {"frontmatter": "forged", "content": "forged"})):
            with self.subTest(field=field):
                tampered = copy.deepcopy(prepared)
                tampered[field] = value
                code = "subject-intent-hash-mismatch" if field == "subject_intent_sha256" else "subject-intent-stale"
                self._error(code, subject_patch.materialize_subject_intent, self.root, tampered, "2026-10-12 10:20:30 +0400")
        tampered = copy.deepcopy(prepared)
        tampered["subject_intent"]["execution_metadata"]["updated_at"] = "tomorrow"
        self._error("subject-intent-stale", subject_patch.materialize_subject_intent, self.root, tampered, "2026-10-12 10:20:30 +0400")

    def test_materialization_rejects_stale_source_and_missing_actual_time(self) -> None:
        prepared = self._prepare()
        self._error("subject-preview-time-invalid", subject_patch.materialize_subject_intent, self.root, prepared, None)
        self.path.write_bytes(self.path.read_bytes().replace(b"exact body", b"changed body"))
        self._error("subject-pin-stale", subject_patch.materialize_subject_intent, self.root, prepared, "2026-10-12 10:20:30 +0400")

    def test_profiles_bind_actual_pins_and_reject_each_grammar_source_drift(self) -> None:
        for profile_name in ("legacy", "approved"):
            prepared = self._prepare(subject_profile=profile_name)
            for pin in get_profile(profile_name).grammar_pins:
                with self.subTest(profile=profile_name, pin=pin.atom_id):
                    source = self.root / pin.path
                    original = source.read_bytes()
                    source.write_bytes(original + b"\n")
                    code = "subject-grammar-pin-stale" if profile_name == "legacy" else "subject-intent-stale"
                    self._error(code, subject_patch.materialize_subject_intent, self.root, prepared, "2026-10-12 10:20:30 +0400")
                    source.write_bytes(original)
        self.assertNotEqual(self._prepare()["subject_intent_sha256"], self._prepare(subject_profile="approved")["subject_intent_sha256"])

    def test_grammar_source_is_rechecked_after_real_materialization(self) -> None:
        prepared = self._prepare()
        source = self.root / get_profile().grammar_pins[0].path
        real_materialize = subject_patch._materialize_item

        def mutate_after_materialize(*args):
            result = real_materialize(*args)
            source.write_bytes(source.read_bytes() + b"\n")
            return result

        with patch.object(subject_patch, "_materialize_item", side_effect=mutate_after_materialize):
            self._error("subject-grammar-pin-stale", subject_patch.materialize_subject_intent, self.root, prepared, "2026-10-12 10:20:30 +0400")


if __name__ == "__main__":
    unittest.main()
