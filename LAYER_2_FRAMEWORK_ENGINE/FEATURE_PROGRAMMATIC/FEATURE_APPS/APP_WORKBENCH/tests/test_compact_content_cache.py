# CA-E-677@17
from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(APP_ROOT)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.content_schema import (  # noqa: E402
    compile_content_schema,
)
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.markdown_content import parse_content  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relations import canonical  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_rows import atom  # noqa: E402


class CompactContentCacheTests(unittest.TestCase):
    @staticmethod
    def schema():
        declaration_body = """## Claim

```CFEL
# model
Atom/(.Header.Role in RMED).Content.Claim{::1}:: []{::0};
Atom/(.Header.Role in RMED).Content.Claim.*[string, in (Formal Claim, Prose Claim)]{::1..2};
Atom.Content.Summary{::1}:: {::1};
```
"""
        return compile_content_schema([{
            "ref": "CA-R-1", "version": 1, "source_path": "model/CA-R-1.md",
            "role": "Requirement", "form": "Declaration", "status_group": "Current",
            "content_markdown": declaration_body,
            "content_properties_json": parse_content(
                declaration_body, tolerate_duplicate_siblings=True,
            ),
        }])

    @staticmethod
    def row(body: str, *, compact: bool) -> dict:
        return {
            "role": "Requirement", "form": "Rule", "content_markdown": body,
            "content_properties_json": parse_content(
                body, tolerate_duplicate_siblings=True, compact=compact,
            ),
        }

    def test_source_rows_omit_section_copies_but_public_parser_keeps_them(self) -> None:
        body = "## Summary\n\nShort.\n"
        public = parse_content(body)
        compact = parse_content(body, compact=True)

        self.assertIn("section_markdown", public[0])
        self.assertIn("direct_markdown", public[0])
        self.assertNotIn("section_markdown", compact[0])
        self.assertNotIn("direct_markdown", compact[0])
        self.assertEqual((0, 1, 3), tuple(compact[0][key] for key in (
            "_start_line", "_body_start_line", "_end_line",
        )))

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "atom.md"
            parsed = atom(path, root, {}, {"atom_id": "CA-R-1", "version": 1}, body, "Current")
        self.assertNotIn("section_markdown", parsed["content_properties_json"][0])
        self.assertNotIn("direct_markdown", parsed["content_properties_json"][0])

    def test_compact_records_match_full_values_and_hash_with_claim_variants(self) -> None:
        body = """## Summary

Short.

## Claim

Legacy prose.

### Formal Claim

```CFEL
Atom.status[string]{1}
```

### Unregistered Heading

Keep this prose.
"""
        schema = self.schema()
        full = schema.values(self.row(body, compact=False))
        compact = schema.values(self.row(body, compact=True))

        self.assertEqual(full, compact)
        self.assertEqual(canonical(full), canonical(compact))
        self.assertIn("Legacy prose.", compact["content.claim.prose_claim"] or "")
        self.assertIn("### Unregistered Heading", compact["content.claim.prose_claim"] or "")
        self.assertEqual("```CFEL\nAtom.status[string]{1}\n```", compact["content.claim.formal_claim"])

        public = {
            "role": "Requirement", "form": "Rule", "content_markdown": body,
            "content_properties_json": parse_content(body),
        }
        self.assertEqual(full, schema.values(public))

    def test_compact_legacy_prose_preserves_parser_newlines_and_fences(self) -> None:
        body = (
            "## Claim\r\n\r\nLegacy\vvertical\fpage.\r\n\r\n"
            "### Formal Claim\r\n\r\n```CFEL\r\nAtom.id[string]{1}\r\n```\r\n\r\n"
            "### Note\r\n\r\nKeep.\r"
        )
        schema = self.schema()
        full = schema.values(self.row(body, compact=False))
        compact = schema.values(self.row(body, compact=True))

        self.assertEqual(full, compact)
        self.assertIn("Legacy\vvertical\fpage.", compact["content.claim.prose_claim"] or "")
        self.assertIn("### Note\r\n\r\nKeep.", compact["content.claim.prose_claim"] or "")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
