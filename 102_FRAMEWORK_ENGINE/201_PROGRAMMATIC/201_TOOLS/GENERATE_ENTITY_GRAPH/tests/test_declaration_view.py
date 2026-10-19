"""Focused tests for the pure declaration-view Markdown renderer."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

import yaml


SCRIPT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPT_DIR))

import declaration_view  # noqa: E402


FENCE = chr(96) * 3
PROJECTION = {
    "projection_id": "CA-PROJ-901",
    "named_selection": "Relation-Types-and-Graph-Rules",
    "source_of_truth": ["CORE_META_MODEL selected authority", "current active source set"],
}


def source(atom_id: str, version: int) -> dict[str, object]:
    return {"atom_id": atom_id, "version": version}


def metadata(**overrides: object) -> dict[str, object]:
    values = {
        "meaning": "a supplied relation meaning",
        "direction": "source to target",
        "inverse": "target to source",
        "authority_effect": "direct",
        "transitivity": "not transitive",
        "applicability": "selected graph",
        "status": "Active",
        "exclusive_purpose": "one purpose",
    }
    values.update(overrides)
    return values


def relation_type(
    graph_kind: str,
    canonical_name: str,
    *,
    relation_metadata: dict[str, object] | None = None,
    sources: list[dict[str, object]] | None = None,
    evidence: list[dict[str, object]] | None = None,
) -> dict[str, object]:
    row: dict[str, object] = {
        "graph_kind": graph_kind,
        "canonical_name": canonical_name,
        "metadata": relation_metadata if relation_metadata is not None else metadata(),
        "sources": sources if sources is not None else [source("CA-R-100", 2)],
    }
    if evidence is not None:
        row["evidence"] = evidence
    return row


def render(
    catalog: dict[str, object],
    *,
    owners: list[dict[str, object]] | None = None,
    projection_identity: dict[str, object] | None = None,
) -> str:
    return declaration_view.render_declarations(
        catalog,
        {"owners": owners if owners is not None else [{"source": source("CA-R-100", 2)}]},
        updated_at="2026-10-20 02:30:00 +0400",
        source_selection="CORE_META_MODEL only",
        projection_identity=projection_identity or PROJECTION,
    )


class DeclarationViewTests(unittest.TestCase):
    def test_good_view_has_identity_sections_and_no_atom_relation_map(self) -> None:
        raw_yaml = (
            FENCE
            + "yaml\n"
            + "graph_rule_type: whitelist\n"
            + "applies_to:\n"
            + "  relation_type: IS_CONTAINED_BY\n"
            + "condition:\n"
            + "  source: [Child]\n"
            + "  target: [Parent]\n"
            + FENCE
        )
        document = render(
            {
                "relation_types": [
                    relation_type(
                        "Entities Graph",
                        "IS_CONTAINED_BY",
                        evidence=[
                            {
                                "source": source("CA-R-1368", 14),
                                "subject": "Entity/Plan",
                                "body": "The source Claim establishes the direct containment direction.",
                            }
                        ],
                    )
                ],
                "graph_rules": [
                    {
                        "source": source("CA-R-200", 4),
                        "subject": "Entity/Plan",
                        "summary": "Plan containment rule.",
                        "yaml_block": raw_yaml,
                    }
                ],
                "limitations": ["Project selection is not included."],
                "unresolved": [],
            },
            owners=[
                {"source": source("CA-R-200", 4)},
                {"source": source("CA-R-100", 2)},
                {"source": source("CA-R-100", 2)},
            ],
        )

        frontmatter = yaml.safe_load(document.split("---\n", 2)[1])
        self.assertEqual("Projection", frontmatter["artifact_form"])
        self.assertEqual("Entities Graph", frontmatter["type"])
        self.assertEqual("CA-PROJ-901", frontmatter["projection_id"])
        self.assertEqual(
            ["CORE_META_MODEL selected authority", "current active source set"],
            frontmatter["source_of_truth"],
        )
        self.assertEqual(["CA-R-100@2", "CA-R-200@4"], frontmatter["sources"])
        self.assertLess(document.index("## Relation Types"), document.index("## Graph Rules"))
        self.assertLess(document.index("## Graph Rules"), document.index("## Source limitations"))
        self.assertIn("\tMeaning: a supplied relation meaning", document)
        self.assertIn("#### Evidence: CA-R-1368@14", document)
        self.assertIn("Subject: Entity/Plan", document)
        self.assertIn("The source Claim establishes the direct containment direction.", document)
        self.assertIn(raw_yaml, document)
        self.assertNotIn("relations:", document)

    def test_empty_catalog_is_explicit_and_does_not_claim_complete_authority(self) -> None:
        document = render({"relation_types": [], "graph_rules": [], "limitations": [], "unresolved": []})

        self.assertIn("- No Relation Type declarations supplied for the selected source set.", document)
        self.assertIn("- Concrete Graph Rule catalogue: empty for the selected source set.", document)
        self.assertIn("does not establish completeness outside the selection", document)

    def test_graph_kind_and_name_are_sorted_without_merging_same_names(self) -> None:
        document = render(
            {
                "relation_types": [
                    relation_type("Z Graph", "SAME"),
                    relation_type("A Graph", "SAME"),
                    relation_type("A Graph", "FIRST"),
                ],
                "graph_rules": [],
                "limitations": [],
                "unresolved": [],
            }
        )

        first = document.index("Relation Type: A Graph / FIRST")
        second = document.index("Relation Type: A Graph / SAME")
        third = document.index("Relation Type: Z Graph / SAME")
        self.assertLess(first, second)
        self.assertLess(second, third)
        self.assertEqual(3, document.count("Relation Type: "))

    def test_rule_yaml_is_opaque_and_keeps_date_and_default_text(self) -> None:
        raw_yaml = (
            FENCE
            + "yaml\n"
            + "graph_rule_type: value_constraint\n"
            + "default_value: 2026-10-20\n"
            + "condition:\n"
            + "  literal: '01:02'\n"
            + FENCE
        )
        document = render(
            {
                "relation_types": [],
                "graph_rules": [
                    {
                        "source": source("CA-R-300", 1),
                        "subject": "Property/Status",
                        "summary": "Do not evaluate this.",
                        "yaml_block": raw_yaml,
                    }
                ],
                "limitations": [],
                "unresolved": [],
            }
        )

        self.assertIn(raw_yaml, document)
        self.assertIn("default_value: 2026-10-20", document)
        self.assertIn("literal: '01:02'", document)
        self.assertIn("Do not evaluate this.", document)

    def test_duplicate_relation_sources_are_deduplicated_and_sorted(self) -> None:
        document = render(
            {
                "relation_types": [
                    relation_type(
                        "Entities Graph",
                        "IS_BORNE_BY",
                        sources=[source("CA-R-9", 3), source("CA-R-9", 3), source("CA-R-2", 8)],
                    )
                ],
                "graph_rules": [],
                "limitations": [],
                "unresolved": [],
            },
            owners=[
                {"source": source("CA-R-9", 3)},
                {"source": source("CA-R-2", 8)},
                {"source": source("CA-R-9", 3)},
            ],
        )

        self.assertEqual(["CA-R-2@8", "CA-R-9@3"], yaml.safe_load(document.split("---\n", 2)[1])["sources"])
        self.assertEqual(1, document.count("\t\tCA-R-9@3"))
        self.assertEqual(1, document.count("\t\tCA-R-2@8"))

    def test_metadata_fence_is_wider_than_untrusted_backticks_and_fields_are_tabbed(self) -> None:
        document = render(
            {
                "relation_types": [
                    relation_type(
                        "Entities Graph",
                        "UNTRUSTED",
                        relation_metadata=metadata(meaning="text with " + chr(96) * 4 + " inside"),
                    )
                ],
                "graph_rules": [],
                "limitations": [],
                "unresolved": [],
            }
        )

        self.assertIn(chr(96) * 5 + "text", document)
        self.assertIn("\tMeaning: text with " + chr(96) * 4 + " inside", document)
        text_block = document[document.index(chr(96) * 5 + "text") :]
        self.assertIn("\tOwning graph kind:", text_block)
        self.assertIn("\tCanonical name:", text_block)

    def test_missing_metadata_is_an_honest_gap_and_unresolved_evidence_is_visible(self) -> None:
        evidence = "governing prose with " + chr(96) * 3 + " fence"
        document = render(
            {
                "relation_types": [
                    relation_type(
                        "Entities Graph",
                        "INCOMPLETE",
                        relation_metadata={"meaning": "only supplied meaning"},
                    )
                ],
                "graph_rules": [],
                "limitations": ["unknown candidate remains outside admission"],
                "unresolved": [
                    {
                        "source": source("CA-R-999", 2),
                        "subject": "Entity/Unknown",
                        "reason": "qualified identity is unresolved",
                        "body": evidence,
                    }
                ],
            }
        )

        self.assertIn("\tMeaning: only supplied meaning", document)
        self.assertIn("\tDeclared direct direction: unavailable (not evidenced in selected authority)", document)
        self.assertIn("unknown candidate remains outside admission", document)
        self.assertIn("qualified identity is unresolved", document)
        self.assertIn(evidence, document)

    def test_invalid_provenance_version_fails_through_existing_source_helper(self) -> None:
        with self.assertRaisesRegex(ValueError, "Invalid source Version"):
            render(
                {"relation_types": [], "graph_rules": [], "limitations": [], "unresolved": []},
                owners=[{"source": {"atom_id": "CA-R-100", "version": 0}}],
            )


if __name__ == "__main__":
    unittest.main()
