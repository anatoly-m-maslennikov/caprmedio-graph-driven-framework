# CA-E-675@4

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[2]))

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.markdown_content import parse_content


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

    def test_returns_none_for_empty_direct_value_without_synthetic_properties(self) -> None:
        properties = parse_content("# Claim\n## Formal Claim\n`x`\n")

        self.assertIsNone(properties[0]["direct_markdown"])
        self.assertEqual(
            [item["property_path"] for item in properties],
            [["claim"], ["claim", "formal_claim"]],
        )
