from __future__ import annotations

import sys
import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOOLS))

from subject_notation import (  # noqa: E402
    SubjectNotationError,
    get_profile,
    parse_subject,
    profile_evidence,
)


class SubjectNotationTest(unittest.TestCase):
    def test_default_legacy_preserves_literal_dots(self) -> None:
        self.assertEqual(
            parse_subject(" Atom.Content / Carrier : Delivery.Policy "),
            [("Atom.Content", None), ("Carrier", "/"), ("Delivery.Policy", ":")],
        )
        self.assertEqual(parse_subject("Atom..Content"), [("Atom..Content", None)])

    def test_approved_mixed_operators_remain_distinct(self) -> None:
        self.assertEqual(
            parse_subject("Atom/Carrier.DeliveryPolicy:Required" , subject_profile="approved"),
            [
                ("Atom", None),
                ("Carrier", "/"),
                ("DeliveryPolicy", "."),
                ("Required", ":"),
            ],
        )
        approved = get_profile("approved")
        self.assertEqual(approved.separators, ("/", ".", ":"))
        self.assertEqual(approved.bearer_separator, ".")

    def test_profiles_and_pins_are_immutable(self) -> None:
        legacy = get_profile()
        self.assertEqual(legacy.name, "legacy")
        self.assertEqual(legacy.separators, ("/", ":"))
        self.assertEqual(legacy.bearer_separator, "/")
        self.assertEqual(len(legacy.grammar_pins), 5)
        self.assertEqual(
            [(pin.atom_id, pin.version) for pin in legacy.grammar_pins],
            [("CA-R-1204", 14), ("CA-R-1321", 12), ("CA-R-1324", 10), ("CA-M-228", 14), ("CA-E-383", 13)],
        )
        with self.assertRaises(FrozenInstanceError):
            legacy.name = "approved"  # type: ignore[misc]
        with self.assertRaises(FrozenInstanceError):
            legacy.grammar_pins[0].version = 0  # type: ignore[misc]

    def test_evidence_is_exactly_scoped_and_fresh(self) -> None:
        first = profile_evidence("approved")
        second = profile_evidence("approved")
        self.assertEqual(set(first), {"grammar_pins", "native_admission"})
        self.assertEqual(first["native_admission"], "not_performed")
        self.assertEqual(len(first["grammar_pins"]), 5)
        self.assertIsNot(first, second)
        self.assertIsNot(first["grammar_pins"], second["grammar_pins"])
        self.assertIsNot(first["grammar_pins"][0], second["grammar_pins"][0])
        first["grammar_pins"][0]["atom_id"] = "altered"
        self.assertEqual(second["grammar_pins"][0]["atom_id"], "CA-R-1931")

    def test_unknown_or_malformed_profiles_fail_without_inference(self) -> None:
        for profile, code in (("legacy ", "profile-unknown"), ("", "profile-invalid"), (None, "profile-invalid")):
            with self.subTest(profile=profile), self.assertRaises(SubjectNotationError) as context:
                parse_subject("Atom", subject_profile=profile)  # type: ignore[arg-type]
            self.assertEqual(context.exception.code, code)

    def test_malformed_separators_fail(self) -> None:
        for value in ("", " ", "/Atom", "Atom/", "Atom//Carrier", "Atom/:Value", "Atom::Value"):
            with self.subTest(value=value), self.assertRaises(SubjectNotationError) as context:
                parse_subject(value)
            self.assertIn(context.exception.code, {"subject-empty", "subject-malformed"})
        with self.assertRaises(SubjectNotationError) as context:
            parse_subject("Atom..Property", subject_profile="approved")
        self.assertEqual(context.exception.code, "subject-malformed")

    def test_unsupported_forms_reject_in_both_profiles(self) -> None:
        for profile in ("legacy", "approved"):
            with self.subTest(profile=profile), self.assertRaises(SubjectNotationError) as context:
                parse_subject("Atom@3", subject_profile=profile)
            self.assertEqual(context.exception.code, "subject-at-unsupported")
            for value in (r"Atom\\Property", "Atom[selector]", "Atom,Carrier", "Atom&Carrier"):
                with self.subTest(profile=profile, value=value), self.assertRaises(SubjectNotationError) as context:
                    parse_subject(value, subject_profile=profile)
                self.assertEqual(context.exception.code, "subject-form-unsupported")


if __name__ == "__main__":
    unittest.main()
