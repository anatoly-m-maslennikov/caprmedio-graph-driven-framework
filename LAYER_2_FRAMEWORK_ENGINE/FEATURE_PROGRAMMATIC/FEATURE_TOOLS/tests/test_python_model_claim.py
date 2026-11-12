"""Checks for static Python Formal Claim reading."""

from pathlib import Path
import sys
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOLS), str(TOOLS.parent / "FEATURE_APPS/APP_WORKBENCH")]

from python_model_claim import (  # noqa: E402
    PythonModelClaimError,
    parse_grouped_python_model_claim,
    parse_python_model_claim,
)
from ATOM_LIFECYCLE.content_constraints import compile_content_constraints  # noqa: E402
from ATOM_LIFECYCLE.header_constraints import compile_header_constraints  # noqa: E402


def declaration(text):
    return {
        "status_group": "Current", "role": "Requirement", "form": "Declaration",
        "id": "CA-R-1", "ref": "CA-R-1", "version": 1, "source_path": "CA-R-1.md",
        "_content_bytes": ("## Claim\n### Formal Claim\n```CFEL\n" + text + "\n```\n").encode(),
    }


class PythonModelClaimTests(unittest.TestCase):
    def test_property_constraints_compile_like_existing_claims(self):
        source = '''
property_rule(address="Atom.Header.Tier", value_format="int", occurrences="1", values="1")
property_rule(address="Atom.Header.Context", value_format="", occurrences="1", values="0")
property_rule(address="Atom.Content.Claim", occurrences="1", value_format="", values="0")
allowed_children(address="Atom.Content.Claim", names=("Formal Claim", "Prose Claim"), occurrences="1..2", name_format="string")
'''
        statements = parse_python_model_claim(source)
        expected = '''
Atom.Header.Tier{::1}:: [int]{::1};
Atom.Header.Context{::1}:: []{::0};
Atom.Content.Claim{::1}:: []{::0};
Atom.Content.Claim.*[string, in (Formal Claim, Prose Claim)]{::1..2};
'''
        translated = declaration(";\n".join(statements))
        original = declaration(expected)
        self.assertEqual(compile_header_constraints([original]), compile_header_constraints([translated]))
        self.assertEqual(compile_content_constraints([original]), compile_content_constraints([translated]))

    def test_all_declarations_and_literals(self):
        source = '''
property_rule(address="Atom.Name", occurrences="1")
property_rule(address="Atom.Score", value_format="int, 0..100", values="0..1")
allowed_children(address="Atom.Content", names=("Claim", "Details"), occurrences="1..2")
order_before(first="Atom.Content.Summary", second="Atom.Content.Claim")
allowed_values(address="Atom.Header.Status", values=("Draft", "In Progress"))
allowed_values(address="Atom.Header.Status", values=("Draft", "Active"), occurrences="1")
relation(source="Workflow", name="CONTAINS", target="Step", source_count="1+", target_count="1")
relation(source="Workflow", name="IS_CONTAINED_BY", target="Step", reverse=True)
subject_path(address="Atom/(.Header.Context.Role := Method).Content.Claim")
set_value(address="Scope Unit.ID", value='"CA-SU-02"')
set_value(address="Node.Enabled", value=True)
set_value(address="Node.Count", value=0)
'''
        self.assertEqual(parse_python_model_claim(source), (
            "Atom.Name{::1}",
            "Atom.Score:: [int, 0..100]{::0..1}",
            "Atom.Content.*[in (Claim, Details)]{::1..2}",
            "Atom.Content.Summary ;> Atom.Content.Claim",
            "Atom.Header.Status :: Draft",
            "Atom.Header.Status :: In Progress",
            "Atom.Header.Status:: [in (Draft, Active)]{::1}",
            "Workflow {::1+}((CONTAINS)){::1} Step",
            "Workflow <((IS_CONTAINED_BY)) Step",
            "Atom/(.Header.Context.Role := Method).Content.Claim",
            'Scope Unit.ID == "CA-SU-02"',
            "Node.Enabled == true",
            "Node.Count == 0",
        ))

    def test_groups_follow_only_top_level_comment_markers(self):
        source = '''
subject_path(address="Atom")
# model
property_rule(
    address="Atom.Name",  # instances
    # instances
    value_format="string",
)
# instances
relation(source="Atom//$a", name="HAS_VALUE", target="Atom.Name")
'''
        self.assertEqual(parse_grouped_python_model_claim(source), (
            ("Atom", None),
            ("Atom.Name:: [string]", "model"),
            ("Atom//$a ((HAS_VALUE)) Atom.Name", "instances"),
        ))

    def test_callback_receives_every_reference(self):
        seen = []
        self.assertEqual(parse_python_model_claim(
            'order_before(first="Atom.A", second="Atom.B")',
            validate_reference=lambda ref: seen.append(ref),
        ), ("Atom.A ;> Atom.B",))
        self.assertEqual(seen, ["Atom.A", "Atom.B"])
        with self.assertRaisesRegex(PythonModelClaimError, "line 1.*unknown address"):
            parse_python_model_claim('subject_path(address="Unknown")', validate_reference=lambda _ref: False)

    def test_rejects_code_and_injected_claims(self):
        invalid = (
            "import os",
            'property_rule("Atom.Name", values="1")',
            'property_rule(address=make_address(), values="1")',
            'property_rule(**{"address": "Atom.Name", "values": "1"})',
            'property_rule(address="Atom.Name; Node.X", values="1")',
            'property_rule(address="Atom.Name:: [string]", values="1")',
            'property_rule(address="Atom.Name\\nNode.X", values="1")',
            'property_rule(address="Atom/(.Role := Method", values="1")',
            'property_rule(address="Atom.Name", value_format="string]; Node")',
            'property_rule(address="Atom.Name", occurrences="2..1")',
            'property_rule(address="Atom.Name", occurrences="01")',
            'allowed_children(address="Atom.X", names=("A", "A"), occurrences="1")',
            'relation(source="Node", name="X)) BAD ((Y")',
            'relation(source="Node", name="X", target_count="1")',
            'relation(source="Node", name="X", reverse="yes")',
            'set_value(address="Node.X", value=1.0)',
            'subject_path(address="Node ((RUN)) Action")',
        )
        for source in invalid:
            with self.subTest(source=source), self.assertRaises(PythonModelClaimError):
                parse_python_model_claim(source)

    def test_errors_report_line_and_callback_error(self):
        with self.assertRaisesRegex(PythonModelClaimError, "line 2, column 1"):
            parse_python_model_claim('# model\nunknown(address="Node")')
        with self.assertRaisesRegex(PythonModelClaimError, "line 2"):
            parse_python_model_claim('# model\nsubject_path(address=')
        def reject(_reference):
            raise ValueError("unknown model entity")
        with self.assertRaisesRegex(PythonModelClaimError, "unknown model entity"):
            parse_python_model_claim('subject_path(address="Node")', validate_reference=reject)


if __name__ == "__main__":
    unittest.main()
