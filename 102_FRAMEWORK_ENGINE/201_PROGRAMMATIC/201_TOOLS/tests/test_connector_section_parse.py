from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from connector_section_parse import SectionError, edit_section, parse_sections, resolve_section


SOURCE = (b"---\r\natom_id: CA-R-1\r\nversion: 7\r\n---\r\n# Summary\r\n\r\nStable summary\r\n\r\n"
          b"## Scope\r\n\r\nCurrent scope\r\n\r\n## Claim\r\n\r\nClaim text\r\n\r\n"
          b"## Details\r\n\r\nLiteral examples:\r\n````markdown\r\n## False section\r\n```\r\n"
          b"## Still false\r\n````\r\n\r\n### First\r\n\r\nFirst value\r\n\r\n"
          b"#### Nested\r\n\r\nNested value\r\n\r\n### Last\r\n\r\nLast value\r\n")


def identity(title, level=3):
    return {"level": level, "title": title}


class SectionTransformTests(unittest.TestCase):
    def test_fences_and_exact_spans(self):
        sections = parse_sections(SOURCE)
        self.assertEqual([section.title for section in sections], ["Summary", "Scope", "Claim", "Details", "First", "Nested", "Last"])
        first = resolve_section(sections, identity("First"))
        self.assertEqual(SOURCE[first.start:first.end], b"### First\r\n\r\nFirst value\r\n\r\n#### Nested\r\n\r\nNested value\r\n\r\n")

    def test_replace_preserves_every_unrelated_byte(self):
        sections = parse_sections(SOURCE)
        section = resolve_section(sections, identity("First"))
        content = "\r\nNew content\r\n\r\n#### Nested\r\n\r\nPreserved nested heading\r\n\r\n"
        output = edit_section(SOURCE, {"operation": "replace", "section": identity("First"), "content": content})
        self.assertEqual(output, SOURCE[:section.body_start] + content.encode() + SOURCE[section.end:])

    def test_title_changes_only_title_including_nested_content(self):
        output = edit_section(SOURCE, {"operation": "title", "section": identity("First"), "title": "Renamed"})
        self.assertEqual(output, SOURCE.replace(b"### First\r\n", b"### Renamed\r\n"))

    def test_add_remove_are_one_family_and_reversible(self):
        delta = {"operation": "add", "section": identity("Added"), "content": "\r\nNew value\r\n\r\n", "position": {"before": identity("Last")}}
        output = edit_section(SOURCE, delta)
        self.assertEqual(output, SOURCE.replace(b"### Last\r\n", b"### Added\r\n\r\nNew value\r\n\r\n### Last\r\n"))
        self.assertEqual(edit_section(output, {"operation": "remove", "section": identity("Added")}), SOURCE)

    def test_move_preserves_complete_nested_section_and_other_bytes(self):
        first = resolve_section(parse_sections(SOURCE), identity("First"))
        last = resolve_section(parse_sections(SOURCE), identity("Last"))
        output = edit_section(SOURCE, {"operation": "position", "section": identity("First"), "position": {"after": identity("Last")}})
        self.assertEqual(output, SOURCE[:first.start] + SOURCE[last.start:last.end] + SOURCE[first.start:first.end])
        self.assertEqual(edit_section(output, {"operation": "position", "section": identity("First"), "position": {"before": identity("Last")}}), SOURCE)

    def test_exact_noops(self):
        section = resolve_section(parse_sections(SOURCE), identity("First"))
        deltas = [
            {"operation": "replace", "section": identity("First"), "content": SOURCE[section.body_start:section.end].decode()},
            {"operation": "title", "section": identity("First"), "title": "First"},
            {"operation": "position", "section": identity("First"), "position": {"before": identity("Last")}},
        ]
        for delta in deltas:
            self.assertEqual(edit_section(SOURCE, delta), SOURCE)

    def test_missing_ambiguous_and_conflicting_selection(self):
        cases = [
            (SOURCE, {"operation": "remove", "section": identity("Missing")}, "target_not_found"),
            (SOURCE.replace(b"### Last", b"### First"), {"operation": "remove", "section": identity("First")}, "target_ambiguous"),
            (SOURCE, {"operation": "title", "section": identity("First"), "title": "Last"}, "target_ambiguous"),
            (SOURCE, {"operation": "position", "section": identity("First"), "position": {"before": identity("Nested", 4)}}, "schema_invalid"),
            (SOURCE, {"operation": "position", "section": identity("First"), "position": 0}, "input_invalid"),
        ]
        for raw, delta, code in cases:
            with self.subTest(delta=delta), self.assertRaises(SectionError) as error:
                edit_section(raw, delta)
            self.assertEqual(error.exception.code, code)

    def test_summary_replacement_refusal_and_exact_noop(self):
        summary = resolve_section(parse_sections(SOURCE), identity("Summary", 1))
        content = SOURCE[summary.body_start:summary.end].decode()
        self.assertEqual(edit_section(SOURCE, {"operation": "replace", "section": identity("Summary", 1), "content": content}), SOURCE)
        self.assertEqual(edit_section(SOURCE, {"operation": "title", "section": identity("Summary", 1), "title": "Summary"}), SOURCE)
        for delta in (
            {"operation": "replace", "section": identity("Summary", 1), "content": "Changed summary\r\n"},
            {"operation": "remove", "section": identity("Summary", 1)},
            {"operation": "title", "section": identity("Summary", 1), "title": "Renamed"},
        ):
            with self.assertRaisesRegex(SectionError, "replacement Workflow"):
                edit_section(SOURCE, delta)

    def test_invalid_input_and_injected_sibling_refuse(self):
        for delta in (None, [], {}, {"operation": [], "section": identity("First")},
                      {"operation": "remove", "section": identity("First"), "extra": True},
                      {"operation": "replace", "section": identity("First"), "content": "\r\n### Injected\r\nvalue\r\n"},
                      {"operation": "title", "section": identity("First"), "title": "Bad\nTitle"}):
            with self.assertRaises(SectionError):
                edit_section(SOURCE, delta)
        for raw in (None, "source", b"no frontmatter", SOURCE + b"```\r\n", SOURCE + b"\xff"):
            with self.assertRaises(SectionError):
                parse_sections(raw)

    def test_position_cannot_merge_eof_content_without_newline(self):
        with self.assertRaises(SectionError):
            edit_section(SOURCE.rstrip(b"\r\n"), {"operation": "position", "section": identity("Last"), "position": {"before": identity("First")}})

    def test_surrogate_titles_and_content_have_structured_refusals(self):
        deltas = (
            {"operation": "title", "section": identity("First"), "title": "\ud800"},
            {"operation": "remove", "section": identity("\ud800")},
            {"operation": "replace", "section": identity("First"), "content": "\ud800"},
            {"operation": "replace", "section": identity("Summary", 1), "content": "\ud800"},
            {"operation": "add", "section": identity("New"), "content": "\ud800", "position": {"before": identity("Last")}},
        )
        for delta in deltas:
            with self.subTest(delta=delta), self.assertRaises(SectionError) as error:
                edit_section(SOURCE, delta)
            self.assertEqual(error.exception.code, "input_invalid")

    def test_lf_and_literal_tilde_fence(self):
        raw = SOURCE.replace(b"\r\n", b"\n").replace(b"````markdown", b"~~~markdown").replace(b"````", b"~~~")
        self.assertEqual(len(parse_sections(raw)), 7)
        output = edit_section(raw, {"operation": "title", "section": identity("Last"), "title": "End"})
        self.assertEqual(output, raw.replace(b"### Last\n", b"### End\n"))


if __name__ == "__main__":
    unittest.main()
