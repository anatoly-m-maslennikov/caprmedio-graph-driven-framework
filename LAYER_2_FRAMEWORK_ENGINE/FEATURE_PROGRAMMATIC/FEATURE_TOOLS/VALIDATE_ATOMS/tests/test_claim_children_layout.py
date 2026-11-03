"""The new adapter stays dormant until its declaration is reviewed and pinned."""

import unittest
import hashlib
from pathlib import Path
from unittest.mock import patch

import yaml

from test_rmed_sibling_layout import check_body, current_source, rows
from test_schema_extended import run
from validate_atoms_workers.check_sections import _LAYOUT_CLAIMS


SUMMARY = "## Summary\n\nSummary.\n\n## Claim\n"
FORMAL = "\n### Formal Claim\n\n```CFEL\nAtom > Claim\n```\n"
PROSE = "\n### Prose Claim\n\nProse.\n\n#### Context\n\nFirst.\n\n#### Context\n\nSecond.\n"


class ClaimChildrenTests(unittest.TestCase):
    def test_reviewed_candidate_selects_adapter_when_active(self):
        from validate_atoms_workers.check_sections import _headings
        root = Path(__file__).resolve().parents[5]
        candidate = root / (".caprmedio_caprmedio/03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/"
                            "model-header-content-20261103/claim/carriers/"
                            "CA-D-479-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties.md")
        text = candidate.read_text(encoding="utf-8")
        body = text.split("---", 2)[-1]
        lines, headings = body.splitlines(), _headings(body)
        start = next(row[2] for row in headings if row[:2] == (2, "Claim"))
        end = next((row[2] for row in headings if row[2] > start and row[0] <= 2), len(lines))
        claim_hash = hashlib.sha256("\n".join(lines[start + 1:end]).strip().encode()).hexdigest()
        self.assertEqual("claim_children", _LAYOUT_CLAIMS.get(claim_hash))
        # Simulate promotion for the adapter check; do not alter the Draft carrier.
        text = text.replace("status: Draft", "status: Active", 1)
        metadata = yaml.safe_load(text.split("---", 2)[1])
        source = {"binding": {"atom_id": "CA-D-479", "version": metadata["version"],
                              "path": str(candidate), "sha256": hashlib.sha256(text.encode()).hexdigest()},
                  "text": text, "metadata": metadata}
        self.assertEqual("passed", check_body(SUMMARY + PROSE, authority=[source])[0])
        self.assertEqual("failed", check_body(SUMMARY + "\nDirect prose.\n", authority=[source])[0])

    def test_children_layout(self):
        from validate_atoms_workers.check_sections import _headings
        body = current_source()["text"].split("---", 2)[-1]
        headings, lines = _headings(body), body.splitlines()
        start = next(row[2] for row in headings if row[:2] == (2, "Claim"))
        end = next((row[2] for row in headings if row[2] > start and row[0] <= 2), len(lines))
        claim_hash = hashlib.sha256("\n".join(lines[start + 1:end]).strip().encode()).hexdigest()
        with patch.dict(_LAYOUT_CLAIMS, {claim_hash: "claim_children"}):
            for role in ("Requirement", "Method", "Evaluation", "Delivery"):
                for value in (FORMAL, PROSE, FORMAL + PROSE):
                    with self.subTest(role=role, value=value):
                        self.assertEqual("passed", check_body(SUMMARY + value, role)[0])
                        checked = run("body.additional_properties", {"content_role": role},
                                      SUMMARY + value, source_rows=rows())
                        self.assertEqual([], checked.findings)
                        self.assertEqual([], checked.gaps)
                for value in ("", "\nBare text.\n", FORMAL + FORMAL,
                              "\nText.\n" + PROSE, FORMAL.replace("CFEL", "text"),
                              "\n### Prose Claim\n"):
                    with self.subTest(role=role, value=value):
                        self.assertEqual("failed", check_body(SUMMARY + value, role)[0])
            self.assertEqual("failed", check_body("## Summary\n\nSummary.\n")[0])
            reverse = FORMAL.replace("Atom > Claim", "reverseview @Relation//HAS_NARROWER <((HAS_INVERSE)) @Relation//NARROWER_THAN")
            self.assertEqual("passed", check_body(SUMMARY + reverse)[0])
            markdown = (SUMMARY + PROSE + "\n## Dependent Selection\n\nSelection.\n"
                        "\n### Why\n\nReason.\n\n## Another heading\n\nMore.\n"
                        "\n## Semantics\n\nMeaning.\n")
            self.assertEqual("passed", check_body(markdown)[0])
            self.assertEqual([], run("body.additional_properties", {"content_role": "Requirement"},
                                     markdown, source_rows=rows()).findings)
            self.assertEqual("failed", check_body(SUMMARY + PROSE + "\n### Prose Claim\n\nAgain.\n")[0])


if __name__ == "__main__":
    unittest.main()
