"""Focused checks for the pure Subject-inventory renderers."""

from __future__ import annotations

import sys
import unittest
import importlib.util
from pathlib import Path

import yaml


TOOL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL))
import subject_inventory_views as views  # noqa: E402


STAGE_SCRIPT = TOOL.parents[3] / ".caprmedio_caprmedio/02_analysis/draft/role-projection-completion-20261102/projection-preparation/scripts/stage_official_views.py"
_stage_spec = importlib.util.spec_from_file_location("stage_official_views", STAGE_SCRIPT)
assert _stage_spec and _stage_spec.loader
stage_official_views = importlib.util.module_from_spec(_stage_spec)
_stage_spec.loader.exec_module(stage_official_views)


def row(identity: str, subject: str | None = None) -> dict:
    return {"identity": identity, "subject": subject or identity,
            "source": {"atom_id": "CA-R-100", "version": 2}}


MODEL = {
    "primary_nodes": [row("Node")], "properties": [row("Node.Name")],
    "instances": [], "relations": [row("Relation//CONTAINS")],
    "selected_subject_expressions": [
        {"expression": "Node", "source": row("Node")["source"], "subject_role": "governs"},
        {"expression": "Aspect <+ Engineering", "source": {"atom_id": "CA-R-101", "version": 1}, "subject_role": "depends_on"},
    ],
}


class SubjectInventoryViewsTests(unittest.TestCase):
    def test_primary_view_keeps_non_admitted_subjects_as_observations(self) -> None:
        document = views._primary_document(
            views._frontmatter("CA-PROJ-014", "Current", ["CA-R-100@2"], "now"), MODEL, []
        )
        self.assertIn("Node [CA-R-100@2]", document)
        self.assertIn("`Aspect <+ Engineering` — CA-R-101@1", document)
        self.assertNotIn("Aspect <+ Engineering [", document)
        self.assertEqual("CA-PROJ-014", yaml.safe_load(document.split("---\n", 2)[1])["projection_id"])

    def test_relation_view_does_not_promote_constraints_or_instances(self) -> None:
        document = views._instances_document(
            views._frontmatter("CA-PROJ-016", "Current", ["CA-R-100@2"], "now"), MODEL,
            [{"kind": "relation_cardinality", "expression": "invented"}],
        )
        self.assertIn("Relation//CONTAINS [CA-R-100@2]", document)
        self.assertNotIn("invented", document)

    def test_aspect_containment_requires_the_explicit_namespace_and_keeps_all_facts(self) -> None:
        occurrence = {"subject": "CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering",
                      "source": {"atom_id": "CA-R-101", "version": 1}}
        rows = stage_official_views.aspect_containment_rows({"occurrences": [occurrence]})
        self.assertIn("STRUCTURE IS_CONTAINED_BY CAPRMEDIO [CA-R-101@1]", rows)
        self.assertIn("Engineering IS_CONTAINED_BY Aspects [CA-R-101@1]", rows)
        with self.assertRaisesRegex(ValueError, "No bare Aspect"):
            stage_official_views.aspect_containment_rows({"occurrences": [{
                **occurrence, "subject": "Aspects <+ Engineering",
            }]})

    def test_aspect_containment_skips_an_unparseable_subject(self) -> None:
        occurrence = {"subject": "CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering",
                      "source": {"atom_id": "CA-R-101", "version": 1}}
        rows = stage_official_views.aspect_containment_rows({"occurrences": [
            occurrence, {**occurrence, "subject": "not valid ( subject"},
        ]})
        self.assertIn("Engineering IS_CONTAINED_BY Aspects [CA-R-101@1]", rows)

    def test_namespace_context_has_no_default_branch(self) -> None:
        graph = {"nodes": [
            {"id": "root", "identity": "CAPRMEDIO"}, {"id": "model", "identity": "MODEL"},
            {"id": "structure", "identity": "STRUCTURE"},
        ], "edges": [{"kind": "IS_CONTAINED_BY", "relation_source": "model", "relation_target": "root"}]}
        self.assertEqual("## Namespace context\n\n```text\nCAPRMEDIO\n  <+ MODEL\n```\n", stage_official_views.namespace_context(graph))
        self.assertEqual("", stage_official_views.namespace_context({**graph, "edges": []}))


if __name__ == "__main__":
    unittest.main()
