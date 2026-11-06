# CA-E-675@6
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[2]))

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.markdown_content import parse_content
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.content_columns import content_columns
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.content_schema import compile_content_schema


class ParseContentTest(unittest.TestCase):
    def test_uses_actual_ancestry_for_first_and_skipped_heading_levels(self) -> None:
        body = "## Parent\nintro\n#### Child\nchild\n### Sibling\nsibling\n"

        properties = parse_content(body)

        self.assertEqual(
            [item["property_path"] for item in properties],
            [["parent"], ["parent", "child"], ["parent", "sibling"]],
        )
        self.assertEqual(properties[0]["direct_markdown"], "intro\n")
        self.assertEqual(properties[0]["section_markdown"], body)
        self.assertEqual([item["position"] for item in properties], [1, 2, 3])

    def test_ignores_heading_like_fenced_indented_and_html_content(self) -> None:
        body = "# Real\n```md\n## fenced\n```\n    ## indented\n<h2>html</h2>\nReal text\n"

        self.assertEqual(
            parse_content(body),
            [{
                "property_path": ["real"],
                "heading": "Real",
                "heading_level": 1,
                "position": 1,
                "direct_markdown": "```md\n## fenced\n```\n    ## indented\n<h2>html</h2>\nReal text\n",
                "section_markdown": body,
            }],
        )

    def test_supports_setext_headings_and_preserves_raw_line_breaks(self) -> None:
        body = "Parent\n======\nfirst line\n\nChild\n-----\nchild line\n\nlast line\n"

        properties = parse_content(body)

        self.assertEqual(properties[0]["heading_level"], 1)
        self.assertEqual(properties[0]["direct_markdown"], "first line\n\n")
        self.assertEqual(properties[0]["section_markdown"], body)
        self.assertEqual(properties[1]["property_path"], ["parent", "child"])
        self.assertEqual(properties[1]["section_markdown"], "Child\n-----\nchild line\n\nlast line\n")
        self.assertEqual(properties[1]["direct_markdown"], "child line\n\nlast line\n")

    def test_preserves_unicode_line_separator_as_content_not_a_source_map_line(self) -> None:
        body = "# First\nline\u2028still one CommonMark line\n# Second\ntext\n"

        properties = parse_content(body)

        self.assertEqual(properties[0]["direct_markdown"], "line\u2028still one CommonMark line\n")
        self.assertEqual(properties[0]["section_markdown"], "# First\nline\u2028still one CommonMark line\n")

    def test_rejects_normalized_duplicate_siblings_but_not_different_parents(self) -> None:
        with self.assertRaisesRegex(ValueError, "duplicate normalized heading key: same_name"):
            parse_content("# Same Name\n# same_name\n")
        with self.assertRaisesRegex(ValueError, "empty property key"):
            parse_content("# !!!\n")

        properties = parse_content("# Left\n## Name\n# Right\n## Name\n")

        self.assertEqual(
            [item["property_path"] for item in properties],
            [["left"], ["left", "name"], ["right"], ["right", "name"]],
        )

    def test_can_preserve_duplicate_presentation_headings_for_legacy_rows(self) -> None:
        properties = parse_content(
            "# Claim\n### Prose Claim\n#### Context\nFirst.\n#### Context\nSecond.\n",
            tolerate_duplicate_siblings=True,
        )

        self.assertEqual(4, len(properties))

    def test_returns_none_for_empty_direct_value_without_synthetic_properties(self) -> None:
        properties = parse_content("# Claim\n## Formal Claim\n`x`\n")

        self.assertIsNone(properties[0]["direct_markdown"])
        self.assertEqual(
            [item["property_path"] for item in properties],
            [["claim"], ["claim", "formal_claim"]],
        )


class ContentColumnsTest(unittest.TestCase):
    @staticmethod
    def _schema():
        body = """## Claim

```CFEL
# model
Atom.Content.Summary{::1}:: {::1};
Atom/(.Header.Role in RMED).Content.Claim{::1}:: []{::0};
Atom/(.Header.Role in RMED).Content.Claim.*[string, in (Formal Claim, Prose Claim)]{::1..2};
Atom.Content.Semantics{::0..1}:: {::0..1};
Atom.Content.Details{::0..1}:: {::0..1};
Atom/(.Header.Role := Plan).Content.Objective{::1}:: {::1};
Atom/(.Header.Role := Plan).Content.Details.Definition of Done{::0..1}:: {::0..1};
```
"""
        declaration = {
            "ref": "CA-R-500", "id": "CA-R-500", "version": 1,
            "source_path": "model/CA-R-500.md", "role": "Requirement",
            "form": "Declaration", "status_group": "Current",
            "content_markdown": body,
            "content_properties_json": parse_content(body, tolerate_duplicate_siblings=True),
        }
        return compile_content_schema([declaration])

    @staticmethod
    def _row(*, role: str, form: str, content_markdown: str) -> dict:
        return {
            "role": role,
            "form": form,
            "content_markdown": content_markdown,
            "content_properties_json": parse_content(
                content_markdown, tolerate_duplicate_siblings=True,
            ),
        }

    def test_rmed_claim_children_are_columns_and_keep_nested_prose_markdown(self) -> None:
        row = self._row(role="Requirement", form="Rule", content_markdown="""## Summary

Short summary.

## Claim

### Formal Claim

```CFEL
Atom.status[string]{1}
```

### Prose Claim

Plain prose.

#### Context

This heading remains prose.

#### Context

Repeated presentation heading remains prose too.

## Semantics

Meaning.
""")

        values = content_columns(row, self._schema())

        self.assertEqual(set(self._schema().names), set(values))
        self.assertEqual("Short summary.", values["content.summary"])
        self.assertEqual("```CFEL\nAtom.status[string]{1}\n```", values["content.claim.formal_claim"])
        self.assertEqual(
            "Plain prose.\n\n#### Context\n\nThis heading remains prose.\n\n#### Context\n\nRepeated presentation heading remains prose too.",
            values["content.claim.prose_claim"],
        )
        self.assertEqual("Meaning.", values["content.semantics"])
        self.assertNotIn("content.context", values)

    def test_legacy_direct_claim_remains_available_as_prose(self) -> None:
        values = content_columns(
            self._row(
                role="Method", form="Policy",
                content_markdown="## Summary\n\nSummary.\n\n## Claim\n\nLegacy prose.\n",
            ), self._schema(),
        )

        self.assertEqual("Legacy prose.", values["content.claim.prose_claim"])

    def test_known_canonical_sections_do_not_require_summary(self) -> None:
        values = content_columns(
            self._row(
                role="Requirement", form="Rule",
                content_markdown="## Claim\n\n### Prose Claim\n\nKnown claim.\n",
            ), self._schema(),
        )

        self.assertIsNone(values["content.summary"])
        self.assertEqual("Known claim.", values["content.claim.prose_claim"])

    def test_nested_declared_name_inside_prose_claim_is_not_a_content_column(self) -> None:
        values = content_columns(
            self._row(role="Delivery", form="Decision", content_markdown="""## Summary

Summary.

## Claim

### Prose Claim

Prose.

#### Details

Presentation detail.

## Semantics

Meaning.
"""), self._schema(),
        )

        self.assertIn("#### Details\n\nPresentation detail.", values["content.claim.prose_claim"])
        self.assertIsNone(values["content.details"])

    def test_duplicate_declared_sections_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "duplicate declared content property: summary"):
            content_columns(
                self._row(
                    role="Requirement", form="Rule",
                    content_markdown="## Summary\n\nFirst.\n\n## Summary\n\nSecond.\n",
                ), self._schema(),
            )
        with self.assertRaisesRegex(ValueError, "duplicate declared content property: claim.prose_claim"):
            content_columns(
                self._row(
                    role="Requirement", form="Rule",
                    content_markdown="## Summary\n\nSummary.\n\n## Claim\n\n### Prose Claim\n\nFirst.\n\n### Prose Claim\n\nSecond.\n",
                ), self._schema(),
            )

    def test_plan_definition_of_done_is_a_declared_nested_property(self) -> None:
        values = content_columns(
            self._row(
                role="Plan", form="Plan",
                content_markdown="## Summary\n\nPlan.\n\n## Objective\n\nShip it.\n\n## Details\n\nContext.\n\n### Definition of Done\n\nTests pass.\n",
            ), self._schema(),
        )

        self.assertEqual("Plan.", values["content.summary"])
        self.assertEqual("Ship it.", values["content.objective"])
        self.assertEqual("Context.", values["content.details"])
        self.assertEqual("Tests pass.", values["content.details.definition_of_done"])
