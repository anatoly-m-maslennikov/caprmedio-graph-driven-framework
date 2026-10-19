"""Focused structural cases for formal Graph Rule body validation."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from validate_atoms_workers.graph_rule_body import validate_graph_rule_body  # noqa: E402
from validate_atoms_workers.settings import CEILINGS  # noqa: E402


class Recorder:
    def __init__(self) -> None:
        self.findings: list[tuple[str, str, str]] = []
        self.gaps: list[tuple[str, str]] = []

    def fail(self, code: str, field: str, reason: str) -> None:
        self.findings.append((code, field, reason))

    def gap(self, field: str, reason: str) -> None:
        self.gaps.append((field, reason))


class EncodeTrap(str):
    def encode(self, encoding: str = "utf-8", errors: str = "strict") -> bytes:
        raise AssertionError("oversized body must be rejected before encoding")


WHITELIST = '''# Summary
Allow evaluation links.

```yaml
graph_rule_type: whitelist
applies_to:
  relation_type: evaluation_for
condition:
  source:
    - "Entity/Node/Continuant/Atom/Content Role: Evaluation"
  target:
    - "Entity/Node/Continuant/Atom/Content Role: Requirement"
```
'''


class GraphRuleBodyTests(unittest.TestCase):
    def validate(self, body: str) -> Recorder:
        check = Recorder()
        validate_graph_rule_body(body, check)  # type: ignore[arg-type]
        return check

    def test_declared_whitelist_shape_passes(self) -> None:
        check = self.validate(WHITELIST)
        self.assertEqual(check.findings, [])
        self.assertEqual(check.gaps, [])

    def test_approved_dot_path_and_atom_selector_pass(self) -> None:
        body = WHITELIST.replace(
            '"Entity/Node/Continuant/Atom/Content Role: Evaluation"',
            "'atom(content_role=\"Plan\").Status'",
        )
        check = self.validate(body)
        self.assertEqual(check.findings, [])

    def test_empty_endpoint_lists_are_structurally_allowed(self) -> None:
        body = WHITELIST.replace(
            '    - "Entity/Node/Continuant/Atom/Content Role: Evaluation"', "    []"
        ).replace(
            '    - "Entity/Node/Continuant/Atom/Content Role: Requirement"', "    []"
        )
        check = self.validate(body)
        self.assertEqual(check.findings, [])

    def test_malformed_yaml_and_non_string_endpoint_members_fail(self) -> None:
        malformed = WHITELIST.replace("relation_type: evaluation_for", "relation_type: [")
        typed_list = WHITELIST.replace(
            '"Entity/Node/Continuant/Atom/Content Role: Evaluation"', "7"
        )
        for body in (malformed, typed_list):
            with self.subTest(body=body):
                self.assertTrue(self.validate(body).findings)

    def test_malformed_subject_notation_fails(self) -> None:
        for subject in ('"Entity//Atom"', "'atom(type=\"Plan\").Status'"):
            body = WHITELIST.replace(
                '"Entity/Node/Continuant/Atom/Content Role: Evaluation"', subject
            )
            with self.subTest(subject=subject):
                self.assertTrue(self.validate(body).findings)

    def test_extra_sections_and_trailing_prose_fail(self) -> None:
        for body in (
            WHITELIST.replace("```yaml", "## Claim\nDuplicate.\n\n```yaml"),
            WHITELIST + "Trailing prose.\n",
            WHITELIST.replace("```yaml", "```text", 1),
        ):
            with self.subTest(body=body):
                self.assertTrue(self.validate(body).findings)

    def test_commonmark_fences_and_leading_blank_lines_pass(self) -> None:
        bodies = (
            "\n\n" + WHITELIST,
            WHITELIST.replace("```yaml", "  ````yaml").replace("\n```\n", "\n  ````   \n"),
            WHITELIST.replace("```yaml", "~~~yaml").replace("\n```\n", "\n~~~\n"),
        )
        for body in bodies:
            with self.subTest(body=body):
                check = self.validate(body)
                self.assertEqual(check.findings, [])
                self.assertEqual(check.gaps, [])

    def test_body_byte_limit_accepts_exact_boundary_and_counts_utf8_bytes(self) -> None:
        body = WHITELIST.replace("Allow evaluation links.", "Allow evaluation 🌉.")
        byte_size = len(body.encode("utf-8"))
        self.assertGreater(byte_size, len(body))
        with patch.dict(CEILINGS, {"max_file_bytes": byte_size}):
            self.assertEqual(self.validate(body).findings, [])
        with patch.dict(CEILINGS, {"max_file_bytes": len(body)}):
            check = self.validate(body)
        self.assertEqual(check.findings[0][1], "body")
        self.assertIn("byte ceiling", check.findings[0][2])

    def test_oversized_character_count_is_rejected_before_encoding(self) -> None:
        with patch.dict(CEILINGS, {"max_file_bytes": 1}):
            check = self.validate(EncodeTrap(WHITELIST))
        self.assertIn("byte ceiling", check.findings[0][2])

    def test_unencodable_body_fails_with_sanitized_diagnostic(self) -> None:
        check = self.validate(WHITELIST + "\ud800")
        self.assertEqual(check.findings[0][1], "body")
        self.assertNotIn("\ud800", check.findings[0][2])

    def test_other_declared_type_is_a_gap_not_a_guessed_schema(self) -> None:
        body = WHITELIST.replace("graph_rule_type: whitelist", "graph_rule_type: cardinality")
        check = self.validate(body)
        self.assertEqual(check.findings, [])
        self.assertEqual(len(check.gaps), 1)


if __name__ == "__main__":
    unittest.main()
