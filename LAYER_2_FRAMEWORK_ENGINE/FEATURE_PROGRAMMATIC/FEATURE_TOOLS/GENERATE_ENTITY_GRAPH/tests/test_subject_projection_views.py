"""Focused checks for the first four source-bound primary views."""

from pathlib import Path
import sys
import unittest


TOOL = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOL.parent), str(TOOL)]

from subject_projection_data import build_subject_projection_data  # noqa: E402
import subject_projection_views as views  # noqa: E402


def carrier(atom_id, subject, body, *, role="Requirement", form="Declaration"):
    return {
        "source": {"atom_id": atom_id, "version": 1, "path": f"sources/{atom_id}.md"},
        "subjects": {"active": subject, "passive": []},
        "body": body,
        "read_view": {"content_role": role, "type": form},
    }


def claim(*lines):
    return "## Claim\n\n" + "\n".join(lines) + "\n"


def carriers():
    return [
        carrier(
            "CA-R-NODE", "Node",
            claim("```CFEL", "Node.Status[status]{:1}: [string]{:1+};", "```"),
        ),
        carrier("CA-R-CHILD", "Node/Child", claim("Child declaration.")),
        carrier(
            "CA-R-STATUS", "Node.Status",
            claim("```CFEL", "Node.Status[status]{:1}: [string]{:1+};", "```"),
        ),
        carrier(
            "CA-R-CHILD-STATUS", "Node/Child.Status",
            claim("```CFEL", "Node/Child.Status[child]{:0..1}: [integer]{:2};", "```"),
        ),
        carrier(
            "CA-M-POISON", "Node.Poison",
            claim("```CFEL", "Node.Poison: Poison;", "```"),
            role="Method", form="Policy",
        ),
    ]


def projection(*, namespace=False):
    rows = carriers()
    if namespace:
        rows.append(carrier("CA-R-NS", "CAPRMEDIO <+ MODEL", claim("Namespace declaration.")))
    data = build_subject_projection_data(rows)
    if namespace:
        # ``namespaces`` is the canonical optional namespace record in the
        # projection API; its source is one of the helper input carriers.
        data.setdefault("namespaces", []).append({
            "subject": "CAPRMEDIO <+ MODEL",
            "source": {"atom_id": "CA-R-NS", "version": 1},
        })
    return data


class SubjectProjectionViewTests(unittest.TestCase):
    def test_qualified_leaf_and_empty_structural_domain_keep_inherited_format(self):
        data = build_subject_projection_data([
            carrier("CA-R-1", "Node", claim("Node.")),
            carrier("CA-R-2", "Node.Section", claim("```CFEL", "Node.Section.**: [markdown];", "```")),
            carrier("CA-R-3", "Node.Section.Group", claim("```CFEL", "Node.Section.Group{:1}: []{:0};", "```")),
            carrier("CA-R-4", "Node.Section.Group.Summary", claim("```CFEL", "Node/(.Header.Role in RMED).Section.Group.Summary: {:0..1};", "```")),
        ])
        properties = next(row for row in data["entities"] if row["identity"] == "Node")["direct_properties"]
        group = next(row for row in properties if row["identity"] == "Node.Section.Group")
        summary = next(row for row in properties if row["identity"] == "Node.Section.Group.Summary")
        self.assertEqual("markdown", group["effective_value_format"])
        self.assertEqual("markdown", summary["effective_value_format"])
        self.assertEqual("Node/(.Header.Role in RMED).Section.Group.Summary", summary["contracts"][0]["property_selector"])
        self.assertEqual({"minimum": 0, "maximum": 1}, summary["contracts"][0]["value_cardinality"])
        self.assertFalse(any(row.get("code") == "conflicting_property_value_formats" for row in data["diagnostics"]))

    def test_recursive_format_inheritance_keeps_local_count_and_source(self):
        rows = [
            carrier("CA-R-1", "Node", claim("Node.")),
            carrier("CA-R-2", "Node.Section", claim("```CFEL", "Node.Section.**: [markdown];", "```")),
            carrier("CA-R-3", "Node.Section.Summary", claim("```CFEL", "Node.Section.Summary: {:0..1};", "```")),
            carrier("CA-R-4", "Node.Section.Nested.Detail", claim("```CFEL", "Node.Section.Nested.Detail: {:0..1};", "```")),
            carrier("CA-M-5", "Node.Section", claim("```CFEL", "Node.Section.**: [integer];", "```"), role="Method", form="Policy"),
        ]
        data = build_subject_projection_data(rows)
        properties = next(row for row in data["entities"] if row["identity"] == "Node")["direct_properties"]
        summary = next(row for row in properties if row["identity"] == "Node.Section.Summary")
        self.assertEqual({"minimum": 0, "maximum": 1}, summary["contracts"][0]["value_cardinality"])
        self.assertIsNone(summary["contracts"][0]["value_format"])
        self.assertEqual(["CA-R-2"], [row["atom_id"] for row in summary["effective_value_format_sources"]])
        document = views.render_primary_projection(data, 3)
        self.assertEqual(2, document.count("effective value format: `markdown` — CA-R-2@1"))
        self.assertIn("value cardinality: `0..1`", document)
        self.assertNotIn("integer", document)
        self.assertFalse(any(row.get("code") == "conflicting_property_value_formats" for row in data["diagnostics"]))

    def test_conflicting_local_and_recursive_formats_are_diagnostic(self):
        data = build_subject_projection_data([
            carrier("CA-R-1", "Node", claim("Node.")),
            carrier("CA-R-2", "Node.Section", claim("```CFEL", "Node.Section.**: [markdown];", "```")),
            carrier("CA-R-3", "Node.Section.Summary", claim("```CFEL", "Node.Section.Summary: [integer]{:0..1};", "```")),
        ])
        document = views.render_primary_projection(data, 3)
        self.assertNotIn("effective value format:", document)
        self.assertIn("Conflicting applicable value formats for Node.Section.Summary", document)
        self.assertIn("CA-R-2@1, CA-R-3@1", document)

    def test_level_three_shows_effective_occurrence_and_population_scopes(self):
        data = build_subject_projection_data([
            carrier("CA-R-1", "Node", claim("Node.")),
            carrier("CA-R-2", "Node.Name", claim(
                "```CFEL", "# model", "Node.Name{:0..1}: [string]{:0..1};",
                "# instances", "Node.**//{:1};", "Node//$node{:1}", "```")),
        ])
        document = views.render_primary_projection(data, 3)
        self.assertIn("occurrence cardinality: `0..1`", document)
        self.assertIn("effective occurrence cardinality: `0..1`", document)
        self.assertIn("value cardinality: `0..1`", document)
        self.assertIn("scope: each Property schema per bearer", document)
        self.assertIn("scope: project population", document)

    def test_explicit_new_namespace_roots_render_without_invented_parent(self):
        data = projection()
        data["namespaces"] = [
            {"subject": "CAPRMEDIO_MODEL", "source": {"atom_id": "CA-R-1", "version": 1}},
            {"subject": "CAPRMEDIO_STRUCTURE <+ Project", "source": {"atom_id": "CA-R-2", "version": 1}},
        ]
        document = views.render_primary_projection(data, 1)
        self.assertIn("\nCAPRMEDIO_MODEL\n", document)
        self.assertIn("\nCAPRMEDIO_STRUCTURE\n  <+ Project", document)
        self.assertNotIn("\nCAPRMEDIO\n", document)

    def test_level_one_keeps_primary_tree_and_source_backed_namespace(self):
        document = views.render_primary_projection(projection(namespace=True), 1)
        self.assertIn("NARROWER_THAN: `/`", document)
        self.assertIn("Node", document)
        self.assertIn("\t/ Child", document)
        self.assertIn("## Namespace context", document)
        self.assertIn("<+ MODEL [CA-R-NS@1]", document)
        self.assertNotIn("Node.Status", document)

    def test_level_two_lists_direct_properties_only(self):
        document = views.render_primary_projection(projection(), 2)
        self.assertIn("## Direct properties", document)
        self.assertIn("property: `Node/Child.Status`", document)
        self.assertNotIn("[inherited]", document)
        child_section = document.split("### `Node/Child`", 1)[1]
        self.assertNotIn("property: `Node.Status`", child_section)

    def test_namespace_context_is_not_invented_without_source_evidence(self):
        document = views.render_primary_projection(projection(), 1)
        self.assertNotIn("## Namespace context", document)

    def test_level_three_keeps_inherited_origin_and_all_constraint_channels(self):
        document = views.render_primary_projection(projection(), 3)
        self.assertIn("## Effective properties", document)
        self.assertIn("property: `Node.Status` (relative `Status`) [inherited]", document)
        self.assertIn("origin: `Node`", document)
        self.assertIn("Node/Child.Status[child]{:0..1}: [integer]{:2}", document)
        self.assertIn("nesting: `property`", document)
        self.assertIn("name format: `child`", document)
        self.assertIn("occurrence cardinality: `0..1`", document)
        self.assertIn("value format: `integer`", document)
        self.assertIn("value cardinality: `2`", document)
        self.assertIn("CA-R-CHILD-STATUS@1", document)
        self.assertIn("CA-R-STATUS@1", document)

    def test_level_four_copies_formal_claim_blocks_verbatim_without_prose(self):
        document = views.render_primary_projection(projection(), 4)
        self.assertIn("## Primary Declaration CFEL", document)
        self.assertIn("Node.Status[status]{:1}: [string]{:1+};", document)
        self.assertIn("Node/Child.Status[child]{:0..1}: [integer]{:2};", document)
        self.assertIn("ancestor Declaration `Node`", document)
        self.assertIn("Property Declaration CFEL", document)
        self.assertNotIn("Child declaration.", document)
        self.assertNotIn("Semantics", document)
        self.assertNotIn("Details", document)

    def test_non_declaration_source_is_not_rendered(self):
        document = views.render_primary_projection(projection(), 4)
        self.assertNotIn("Poison", document)
        self.assertNotIn("CA-M-POISON", document)

    def test_invalid_level_is_rejected(self):
        with self.assertRaises(ValueError):
            views.render_primary_projection(projection(), 5)


if __name__ == "__main__":
    unittest.main()
