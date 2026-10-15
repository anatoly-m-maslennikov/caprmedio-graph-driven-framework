from __future__ import annotations

import sys
import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOOLS))

from subject_notation import (  # noqa: E402
    GrammarPin,
    SubjectNotationError,
    get_profile,
    parse_initial_atom_selector,
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
        self.assertEqual(
            parse_subject('Atom"Quoted"/Carrier'),
            [('Atom"Quoted"', None), ("Carrier", "/")],
        )

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

    def test_approved_initial_atom_selector_preserves_literal_and_owner_term(self) -> None:
        literal = 'atom( content_role = "Plan/Type: Blue.Green" , type = "Plan" )'
        self.assertEqual(
            parse_subject(f"{literal}.Status", subject_profile="approved"),
            [(literal, None), ("Status", ".")],
        )
        selector = parse_initial_atom_selector(literal, subject_profile="approved")
        self.assertIsNotNone(selector)
        assert selector is not None
        self.assertEqual(literal, selector.literal)
        self.assertEqual(
            {"content_role": "Plan/Type: Blue.Green", "type": "Plan"},
            dict(selector.selector),
        )
        self.assertEqual("Atom", selector.entity_type_term)
        with self.assertRaises(TypeError):
            selector.selector["type"] = "Other"  # type: ignore[index]
        self.assertIsNone(parse_initial_atom_selector("Atom", subject_profile="approved"))

    def test_approved_atom_id_selector_is_initial_only_and_does_not_normalize_atom(self) -> None:
        literal = 'atom(atom_id="CA-O-135")'
        self.assertEqual(
            parse_subject(f"{literal}.Status", subject_profile="approved"),
            [(literal, None), ("Status", ".")],
        )
        self.assertEqual(
            {"atom_id": "CA-O-135"},
            dict(parse_initial_atom_selector(literal, subject_profile="approved").selector),  # type: ignore[union-attr]
        )
        self.assertEqual(
            [("Atom", None), ("Status", ".")],
            parse_subject("Atom.Status", subject_profile="approved"),
        )

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

        sources = get_profile("approved").grammar_pins
        self.assertEqual(["CA-R-1931", "CA-R-1321", "CA-R-1324", "CA-M-228", "CA-E-383"], [source.atom_id for source in sources])
        for source in sources:
            self.assertFalse(hasattr(source, "version"))
            self.assertFalse(hasattr(source, "sha256"))

    def test_evidence_is_exactly_scoped_and_fresh(self) -> None:
        pins = [GrammarPin(source.atom_id, 2, source.path, "1" * 64) for source in get_profile("approved").grammar_pins]
        with self.assertRaises(SubjectNotationError) as unbound:
            profile_evidence("approved")
        self.assertEqual("profile-evidence-unbound", unbound.exception.code)
        first = profile_evidence("approved", grammar_pins=pins)
        second = profile_evidence("approved", grammar_pins=pins)
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

    def test_selector_forms_are_approved_only_and_reject_invalid_syntax(self) -> None:
        accepted = (
            'atom(atom_id="CA-O-135").Status',
            'atom(content_role="Plan").Status',
            'atom(content_role = "Plan" , type = "Plan" ).Status',
        )
        for value in accepted:
            with self.subTest(value=value):
                self.assertEqual("atom", parse_subject(value, subject_profile="approved")[0][0][:4])
                with self.assertRaises(SubjectNotationError) as legacy:
                    parse_subject(value, subject_profile="legacy")
                self.assertEqual("subject-form-unsupported", legacy.exception.code)

        rejected = (
            "atom",
            'Atom(content_role="Plan").Status',
            'ATOM(atom_id="CA-O-135").Status',
            'atom().Status',
            'atom(type="Plan").Status',
            'atom(type="Plan",content_role="Plan").Status',
            'atom(atom_id="CA-O-135",content_role="Plan").Status',
            'atom(content_role="Plan",atom_id="CA-O-135").Status',
            'atom(content_role="Plan",type="Plan",type="Other").Status',
            'atom(content_role="Plan",unknown="Other").Status',
            'atom("Plan").Status',
            'atom(content_role="").Status',
            'atom(content_role="   ").Status',
            'atom(content_role="Plan\\Role").Status',
            'atom(content_role="Plan*").Status',
            'atom(content_role="Plan").atom(atom_id="CA-O-135")',
        )
        for value in rejected:
            with self.subTest(value=value), self.assertRaises(SubjectNotationError):
                parse_subject(value, subject_profile="approved")

        for value in (
            'atom(content_role="Plan*")',
            'atom(content_role="Plan@Current")',
            'atom(content_role="Plan\\Role")',
            'atom(content_role="$PLAN")',
            'atom(content_role="Plan\u0001")',
        ):
            with self.subTest(helper_value=value), self.assertRaises(SubjectNotationError):
                parse_initial_atom_selector(value, subject_profile="approved")


if __name__ == "__main__":
    unittest.main()
