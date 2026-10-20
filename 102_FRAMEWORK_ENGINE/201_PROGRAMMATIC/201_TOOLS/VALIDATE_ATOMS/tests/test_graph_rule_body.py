"""Focused structural cases for formal Graph Rule body validation."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from validate_atoms_workers.graph_rule_body import (  # noqa: E402
    validate_graph_rule_body,
    validated_graph_rule_payload,
)
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

    def test_extraction_returns_validated_payload_and_exact_carrier_text(self) -> None:
        check = Recorder()
        extracted = validated_graph_rule_payload(WHITELIST, check)  # type: ignore[arg-type]
        self.assertEqual(check.findings, [])
        self.assertIsNotNone(extracted)
        assert extracted is not None
        self.assertEqual(extracted.summary, "Allow evaluation links.\n\n")
        self.assertEqual(extracted.operative_block, "```yaml\n" + WHITELIST.split("```yaml\n", 1)[1])
        self.assertEqual(extracted.operative_yaml, WHITELIST.split("```yaml\n", 1)[1].split("```", 1)[0])
        self.assertEqual(extracted.payload["graph_rule_type"], "whitelist")

    def test_extraction_preserves_crlf_and_opaque_default_value(self) -> None:
        body = WHITELIST.replace("```yaml", "~~~~yaml").replace("```", "~~~~").replace(
            "\n", "\r\n"
        )
        body = body.replace("condition:\r\n", "default_value:\r\n  opaque: 2026-10-20\r\ncondition:\r\n")
        check = Recorder()
        extracted = validated_graph_rule_payload(body, check)  # type: ignore[arg-type]
        self.assertEqual(check.findings, [])
        assert extracted is not None
        self.assertEqual(extracted.summary, "Allow evaluation links.\r\n\r\n")
        self.assertTrue(extracted.operative_block.startswith("~~~~yaml\r\n"))
        self.assertTrue(extracted.operative_block.endswith("~~~~\r\n"))
        self.assertIn("default_value:\r\n  opaque: 2026-10-20\r\n", extracted.operative_yaml)
        self.assertEqual(str(extracted.payload["default_value"]["opaque"]), "2026-10-20")

    def test_optional_support_sections_are_valid_in_either_order_or_empty(self) -> None:
        variants = (
            WHITELIST + "\n## Semantics\nUseful explanation.\n",
            WHITELIST + "\n## Details\nUseful support.\n",
            WHITELIST + "\n## Details\n\n## Semantics\n\n",
            WHITELIST + "\n## Semantics\n\n## Details\n\n",
        )
        for body in variants:
            with self.subTest(body=body):
                check = self.validate(body)
                self.assertEqual(check.findings, [])
                self.assertEqual(check.gaps, [])

    def test_nested_support_headings_and_fenced_examples_are_nonoperative(self) -> None:
        body = WHITELIST + '''
## Details
### Supporting example
```yaml
graph_rule_type: blacklist
applies_to: {}
condition: {}
```
### More support
No operative change.
'''
        check = Recorder()
        extracted = validated_graph_rule_payload(body, check)  # type: ignore[arg-type]
        self.assertEqual(check.findings, [])
        assert extracted is not None
        self.assertEqual(extracted.payload["graph_rule_type"], "whitelist")
        self.assertEqual(extracted.operative_block, "```yaml\n" + WHITELIST.split("```yaml\n", 1)[1])

    def test_crlf_support_docs_do_not_change_extracted_source_slices(self) -> None:
        base = validated_graph_rule_payload(WHITELIST, Recorder())  # type: ignore[arg-type]
        body = WHITELIST.replace("\n", "\r\n") + "\r\n## Semantics\r\nSupport.\r\n"
        documented = validated_graph_rule_payload(body, Recorder())  # type: ignore[arg-type]
        assert base is not None and documented is not None
        self.assertEqual(documented.summary, base.summary.replace("\n", "\r\n"))
        self.assertEqual(documented.operative_yaml, base.operative_yaml.replace("\n", "\r\n"))
        self.assertEqual(documented.operative_block, base.operative_block.replace("\n", "\r\n"))

    def test_forbidden_duplicate_unknown_and_pre_block_sections_fail(self) -> None:
        invalid = (
            WHITELIST + "\n## Scope\nSeparate scope.\n",
            WHITELIST + "\n## Claim\nAnother claim.\n",
            WHITELIST + "\n## Substance\nAnother substance.\n",
            WHITELIST + "\n## Details\nOne.\n## Details\nTwo.\n",
            WHITELIST + "\n## Semantics\nOne.\n## Other\nUnsupported.\n",
            WHITELIST.replace("Allow evaluation links.\n\n```yaml", "Allow evaluation links.\n\n## Details\nPre-block.\n\n```yaml"),
            WHITELIST + "\nUnsectioned trailing prose.\n",
        )
        for body in invalid:
            with self.subTest(body=body):
                check = self.validate(body)
                self.assertTrue(check.findings)

    def test_extra_schema_fields_fail_without_extraction(self) -> None:
        for body in (
            WHITELIST.replace("relation_type: evaluation_for", "relation_type: evaluation_for\n  guessed: true"),
            WHITELIST.replace("condition:\n", "condition:\n  guessed: true\n"),
            WHITELIST.replace("graph_rule_type: whitelist", "graph_rule_type: whitelist\nextra: true"),
        ):
            with self.subTest(body=body):
                check = Recorder()
                self.assertIsNone(validated_graph_rule_payload(body, check))  # type: ignore[arg-type]
                self.assertTrue(check.findings)

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
        for subject in ('"Entity///Atom"', "'atom(type=\"Plan\").Status'"):
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
        extraction_check = Recorder()
        extracted = validated_graph_rule_payload(body, extraction_check)  # type: ignore[arg-type]
        self.assertIsNone(extracted)
        self.assertEqual(extraction_check.findings, [])
        self.assertEqual(len(extraction_check.gaps), 1)


if __name__ == "__main__":
    unittest.main()
