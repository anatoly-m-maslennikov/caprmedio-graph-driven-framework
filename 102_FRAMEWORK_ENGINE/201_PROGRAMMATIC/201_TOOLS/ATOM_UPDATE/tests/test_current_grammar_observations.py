"""Current approved grammar observations survive metadata updates between calls."""

import hashlib
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

import yaml

TOOLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOOLS))
import atom_operations as operations  # noqa: E402
import atom_subject_patch as subjects  # noqa: E402
from subject_notation import get_profile  # noqa: E402
import test_subject_intent_materialization as intent_fixture  # noqa: E402


class CurrentGrammarObservationTests(unittest.TestCase):
    def setUp(self):
        self.fixture = intent_fixture.SubjectIntentMaterializationTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.source = get_profile("approved").grammar_pins[0]
        self.path = self.root / self.source.path

    def prepare(self):
        return self.fixture._prepare(subject_profile="approved")

    def update_grammar_subjects(self):
        parsed = operations.parse_carrier(self.path.read_bytes(), self.path)
        metadata = dict(parsed.metadata)
        metadata["version"] += 1
        metadata["subjects"] = {**metadata["subjects"], "governs": "Subject.Expression"}
        self.path.write_text(
            "---\n" + yaml.safe_dump(metadata, sort_keys=False) + "---\n" + parsed.body
        )
        return metadata["version"]

    def test_next_operation_reads_updated_subjects_and_version_without_reload(self):
        first = self.prepare()
        target_before = self.fixture.path.read_bytes()
        version = self.update_grammar_subjects()
        second = self.prepare()
        evidence = second["subject_intent"]["subject_profile_evidence"]["grammar_pins"]
        observed = next(row for row in evidence if row["atom_id"] == self.source.atom_id)
        self.assertEqual(version, observed["version"])
        self.assertEqual(hashlib.sha256(self.path.read_bytes()).hexdigest(), observed["sha256"])
        self.assertNotEqual(first["subject_intent_sha256"], second["subject_intent_sha256"])
        self.assertEqual(target_before, self.fixture.path.read_bytes())
        with self.assertRaises(operations.ToolError) as stale:
            subjects.materialize_subject_intent(self.root, first, "2026-10-15 10:00:00 +0400")
        self.assertEqual("subject-intent-stale", stale.exception.code)

    def test_change_after_capture_still_rejects_and_does_not_refresh_the_observation(self):
        profile = get_profile("approved")
        captured = subjects._capture_grammar(operations, self.root, profile)
        evidence = subjects._captured_profile_evidence(operations, profile, captured)
        self.update_grammar_subjects()
        self.assertNotEqual(
            evidence["grammar_pins"][0]["sha256"],
            hashlib.sha256(self.path.read_bytes()).hexdigest(),
        )
        with self.assertRaises(operations.ToolError) as stale:
            subjects._assert_grammar_current(operations, self.root, captured)
        self.assertEqual("subject-grammar-pin-stale", stale.exception.code)

    def test_wrong_identity_inactive_and_invalid_version_are_not_current_rules(self):
        original = self.path.read_bytes()
        for field, value in (("atom_id", "CA-R-99999"), ("status", "Draft"), ("version", True)):
            parsed = operations.parse_carrier(original, self.path)
            metadata = {**parsed.metadata, field: value}
            self.path.write_text(
                "---\n" + yaml.safe_dump(metadata, sort_keys=False) + "---\n" + parsed.body
            )
            with self.subTest(field=field), self.assertRaises(operations.ToolError):
                subjects._capture_grammar(operations, self.root, get_profile("approved"))
            self.path.write_bytes(original)

    def test_preview_rechecks_captured_grammar_after_target_validation(self):
        original = subjects._materialize_item

        def materialize_then_change(*args, **kwargs):
            result = original(*args, **kwargs)
            self.update_grammar_subjects()
            return result

        with patch.object(subjects, "_materialize_item", side_effect=materialize_then_change):
            with self.assertRaises(operations.ToolError) as stale:
                subjects.preview_subject_patches(
                    self.root,
                    self.fixture.fixture._payload(self.fixture.path),
                    timestamp="2026-10-15 10:00:00 +0400",
                    subject_profile="approved",
                )
        self.assertEqual("subject-grammar-pin-stale", stale.exception.code)


if __name__ == "__main__":
    unittest.main()
