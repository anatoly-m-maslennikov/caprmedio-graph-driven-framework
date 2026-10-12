"""Independent public-wrapper checks for the selected Subject profile."""
from __future__ import annotations

import argparse
import copy
import hashlib
import io
import json
import sys
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from unittest.mock import patch

TESTS = Path(__file__).resolve().parent
TOOLS = TESTS.parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TESTS))
import atom_operations as operations
import test_subject_patch_preview as fixtures


class SubjectProfileWiringTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = fixtures.SubjectPatchPreviewTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root

    def run_preview(self, payload: dict, *, apply: bool = False):
        with patch.object(operations, "_load_payload", return_value=payload):
            with patch.object(operations, "_validate_complete_carrier") as validate:
                result = operations.run_update(self.root, argparse.Namespace(input="-", apply=apply))
        self.assertEqual(validate.call_count, 2)
        return result

    def payload(self, **root_fields):
        return {"atoms": self.fixture._payload([]), **root_fields}

    def test_search_cli_and_description_declare_explicit_profile(self) -> None:
        args = operations.parser("ATOM_SEARCH").parse_args(
            ["run", "--subject", "Artifact/Atom", "--subject-profile", "approved"])
        self.assertEqual(args.subject_profile, "approved")
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            operations.parser("ATOM_SEARCH").parse_args(
                ["run", "--subject", "Atom", "--subject-profile", "guess"])
        search = operations.describe("ATOM_SEARCH")["subject_lookup"]
        self.assertEqual(search["default_profile"], "legacy")
        self.assertEqual(search["profile_prefix_boundaries"],
                         {"legacy": ["/", ":"], "approved": ["/", ".", ":"]})
        self.assertIn("subject_profile_evidence", search["output"])
        preview = operations.describe("ATOM_UPDATE")["subject_preview"]
        self.assertFalse(preview["apply_supported"])
        self.assertEqual(preview["default_profile"], "legacy")

    def test_profile_without_subject_cannot_fall_back_to_generic_search(self) -> None:
        for profile in ("approved", ""):
            with self.subTest(profile=profile), self.assertRaises(operations.ToolError) as caught:
                operations.run_search(self.root, argparse.Namespace(subject=None, subject_profile=profile))
            self.assertEqual(caught.exception.code, "input-invalid")

    def test_closed_root_does_not_silently_ignore_transition_or_unknown_fields(self) -> None:
        for key in ("target_profile", "source_profile", "unexpected"):
            with self.subTest(key=key), self.assertRaises(operations.ToolError) as caught:
                self.run_preview(self.payload(**{key: "approved"}))
            self.assertEqual(caught.exception.code, "input-invalid")

    def test_malformed_supplied_profiles_and_generic_profile_are_rejected(self) -> None:
        for value in (None, "", "guess", [], {}, 1, True):
            with self.subTest(value=value), self.assertRaises(operations.ToolError) as caught:
                self.run_preview(self.payload(subject_profile=value))
            self.assertEqual(caught.exception.code, "subject-profile-invalid")
        payload = {"atoms": [{"selector": self.fixture.selector, "content": "not a Subject patch"}],
                   "subject_profile": "approved"}
        with self.assertRaises(operations.ToolError) as caught:
            self.run_preview(payload)
        self.assertEqual(caught.exception.code, "input-invalid")

    def test_selected_profile_and_five_pin_evidence_are_sealed_for_noop(self) -> None:
        before = self.fixture.path.read_bytes()
        approved = self.run_preview(self.payload(subject_profile="approved"))
        legacy = self.run_preview(self.payload())
        self.assertEqual(approved["subject_profile"], "approved")
        self.assertEqual(legacy["subject_profile"], "legacy")
        self.assertEqual(approved["subject_profile_evidence"]["native_admission"], "not_performed")
        pins = approved["subject_profile_evidence"]["grammar_pins"]
        self.assertEqual({p["atom_id"] for p in pins},
                         {"CA-R-1931", "CA-R-1321", "CA-R-1324", "CA-M-228", "CA-E-383"})
        self.assertEqual(len(pins), 5)
        self.assertTrue(approved["noop"])
        self.assertIsNone(approved["illustrative_updated_at"])
        self.assertEqual(self.fixture.path.read_bytes(), before)
        self.assertNotEqual(approved["preview_sha256"], legacy["preview_sha256"])
        body = copy.deepcopy(approved)
        digest = body.pop("preview_sha256")
        self.assertEqual(digest, hashlib.sha256(operations.canonical_json(body).encode()).hexdigest())
        body["subject_profile_evidence"]["grammar_pins"][0]["version"] += 1
        self.assertNotEqual(digest, hashlib.sha256(operations.canonical_json(body).encode()).hexdigest())

    def test_profile_does_not_open_apply_or_mix_modes(self) -> None:
        before = self.fixture.path.read_bytes()
        with self.assertRaises(operations.ToolError) as caught:
            self.run_preview(self.payload(subject_profile="approved"), apply=True)
        self.assertEqual(caught.exception.code, "subject-apply-not-admitted")
        payload = self.payload(subject_profile="approved")
        payload["atoms"].append({"selector": self.fixture.selector, "content": "not a patch"})
        with self.assertRaises(operations.ToolError) as caught:
            self.run_preview(payload)
        self.assertEqual(caught.exception.code, "input-invalid")
        self.assertEqual(self.fixture.path.read_bytes(), before)

    def test_complete_carrier_refusal_is_not_bypassed_by_profile(self) -> None:
        with patch.object(operations, "_load_payload", return_value=self.payload(subject_profile="approved")):
            with patch.object(operations, "_validate_complete_carrier",
                              side_effect=operations.ToolError("fixture-refusal", "not valid")):
                with self.assertRaises(operations.ToolError) as caught:
                    operations.run_update(self.root, argparse.Namespace(input="-", apply=False))
        self.assertEqual(caught.exception.code, "fixture-refusal")


if __name__ == "__main__":
    unittest.main()
