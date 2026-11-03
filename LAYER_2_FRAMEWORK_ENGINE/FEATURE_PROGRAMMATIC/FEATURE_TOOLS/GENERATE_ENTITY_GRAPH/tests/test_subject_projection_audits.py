"""Focused checks for the additive Subject audit layer."""

from pathlib import Path
import sys
import unittest


TOOL = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOL.parent), str(TOOL)]

from subject_projection_audits import build_subject_audits, render_subject_audit, select_model_subjects  # noqa: E402
from subject_projection_data import build_subject_projection_data  # noqa: E402


def carrier(atom_id, active, passive=(), *, role="Requirement", form="Declaration"):
    return {"source": {"atom_id": atom_id, "version": 1, "path": f"sources/{atom_id}.md"},
            "subjects": {"active": active, "passive": list(passive)}, "body": "## Claim\n",
            "read_view": {"content_role": role, "type": form}}


class SubjectProjectionAuditTests(unittest.TestCase):
    def test_model_scope_excludes_structure_and_concrete_instances_but_keeps_descriptors(self):
        sources = [
            carrier("CA-R-1", "CAPRMEDIO_MODEL <+ Node", [
                "CAPRMEDIO_STRUCTURE <+ Project", "CAPRMEDIO_MODEL <+ Node//Example",
                "CAPRMEDIO_MODEL <+ Node//Example.Name", "CAPRMEDIO_MODEL <+ CFEL <+ Relation//RUN",
                "CAPRMEDIO_MODEL <+ CFEL <+ Operator//Alias", "CAPRMEDIO_MODEL <+ CFEL <+ Format//markdown",
                "CAPRMEDIO_MODEL <+ Term//Word", "Legacy Node",
            ]),
            carrier("CA-R-2", "CAPRMEDIO_STRUCTURE <+ Project", ["CAPRMEDIO_MODEL <+ Node"]),
            carrier("CA-R-3", "CAPRMEDIO_STRUCTURE <+ Project", [{"legacy": "not a Subject"}]),
        ]
        selected, diagnostics = select_model_subjects(sources)
        self.assertEqual(3, len(selected))
        self.assertEqual(["Legacy Node", "{'legacy': 'not a Subject'}"], [row["raw_value"] for row in diagnostics])
        passive = selected[0]["subjects"]["passive"]
        self.assertEqual(4, len(passive))
        self.assertTrue(any("Relation//RUN" in row for row in passive))
        self.assertTrue(any("Operator//Alias" in row for row in passive))
        self.assertTrue(any("Format//markdown" in row for row in passive))
        self.assertTrue(any("Term//Word" in row for row in passive))
        self.assertNotIn("active", selected[1]["subjects"])
        data = build_subject_projection_data([selected[0]])
        audits = build_subject_audits(selected, data, scope_diagnostics=diagnostics)
        identities = {row["identity"] for row in audits["entity_definition_summary"]["entities"]}
        self.assertNotIn("Project", identities)
        self.assertFalse(any("Example" in identity for identity in identities))
        self.assertTrue({"RUN", "Operator//Alias", "Format//markdown", "Term//Word"} <= identities)
        self.assertIn("Legacy Node", [row["subject"] for row in audits["subjects_without_declaration_coverage"]["unresolved"]])
        self.assertEqual("CAPRMEDIO_STRUCTURE <+ Project", sources[1]["subjects"]["active"])

    def test_selection_groups_keep_model_scope_and_exclude_instance_scope(self):
        model = "CAPRMEDIO <+ MODEL <+ (Node, Node.**)"
        instance = "CAPRMEDIO <+ MODEL <+ (Node//,(Node//).**)"
        selected, diagnostics = select_model_subjects([
            carrier("CA-R-1", model, [instance], form="Rule"),
            carrier("CA-R-2", instance, form="Rule"),
            carrier("CA-R-3", "CAPRMEDIO_STRUCTURE", form="Rule"),
        ])
        self.assertEqual(model, selected[0]["subjects"]["active"])
        self.assertNotIn("passive", selected[0]["subjects"])
        self.assertEqual({}, selected[1]["subjects"])
        self.assertEqual({}, selected[2]["subjects"])
        self.assertEqual([], diagnostics)
        audits = build_subject_audits(selected)
        unresolved = audits["subjects_without_declaration_coverage"]["unresolved"]
        self.assertTrue(any(row["subject"] == "CAPRMEDIO <+ MODEL <+ (Node,Node.**)" for row in unresolved))

    def test_passive_set_difference_does_not_confuse_owner_active_subjects(self):
        audits = build_subject_audits([
            carrier("CA-R-1", "OwnerA", ["Shared", "Passive Only"]),
            carrier("CA-R-2", "OwnerB", ["Shared"]),
            carrier("CA-R-3", "Shared"),
        ])
        rows = audits["passive_only_subjects"]["subjects"]
        self.assertEqual(["Passive Only"], [row["subject"] for row in rows])
        self.assertEqual("passive", rows[0]["occurrences"][0]["source_key"])

    def test_exact_requirement_declaration_excludes_rules_and_entity_definitions_are_informational(self):
        audits = build_subject_audits([
            carrier("CA-R-1", "Node"),
            carrier("CA-R-2", "Rule Only", form="Rule"),
            carrier("CA-R-3", "CFEL", form="Entity Definition"),
        ])
        report = audits["subjects_without_declaration_coverage"]
        self.assertEqual(["Rule Only"], [row["subject"] for row in report["subjects"]])
        self.assertEqual(["CFEL"], [row["subject"] for row in report["informational"]])

    def test_inherited_property_is_covered_by_its_original_declaration(self):
        audits = build_subject_audits([
            carrier("CA-R-1", "Node"), carrier("CA-R-2", "Node/Child"),
            carrier("CA-R-3", "Node.Status"),
            carrier("CA-R-4", "Node/Child.Status", ["Node/Child.Status"]),
        ])
        report = audits["subjects_without_declaration_coverage"]
        self.assertNotIn("Node/Child.Status", [row["subject"] for row in report["subjects"]])

    def test_namespaced_subject_and_unsupported_subject_keep_provenance_and_review_state(self):
        legacy = carrier("CA-R-1", "Node", ["CAPRMEDIO <+ MODEL <+ Node"])
        legacy["subjects"] = {"governs": "Node", "depends_on": ["CAPRMEDIO <+ MODEL <+ Node", "not valid ("]}
        audits = build_subject_audits([legacy])
        row = audits["passive_only_subjects"]["subjects"][0]
        self.assertEqual("depends_on", row["occurrences"][0]["source_key"])
        report = audits["subjects_without_declaration_coverage"]
        self.assertTrue(report["unresolved"])
        self.assertEqual("not valid (", audits["passive_only_subjects"]["subjects"][1]["subject"])
        self.assertTrue(audits["passive_only_subjects"]["subjects"][1]["unresolved"])
        self.assertIn("# Subjects Used Only Passively", render_subject_audit(audits, "passive_only_subjects"))

    def test_entity_summary_keeps_definition_and_active_flags_orthogonal(self):
        scope = carrier("CA-R-1", "Scope Unit//Alpha", form="Scope Unit Declaration")
        term = carrier("CA-M-2", "Term//Word", role="Method", form="Term Definition")
        entity = carrier("CA-R-3", "CFEL", form="Entity Definition")
        rule = carrier("CA-R-4", "Rule Only", form="Rule")
        passive = carrier("CA-R-5", "Owner", ["Passive Only"])
        report = build_subject_audits([scope, term, entity, rule, passive])["entity_definition_summary"]
        rows = {row["identity"]: row for row in report["entities"]}
        self.assertFalse(rows["Scope Unit//Alpha"]["missing_definition"])
        self.assertFalse(rows["Term//Word"]["missing_definition"])
        self.assertFalse(rows["CFEL"]["missing_definition"])
        self.assertTrue(rows["Rule Only"]["missing_definition"])
        self.assertFalse(rows["Rule Only"]["missing_active"])
        self.assertTrue(rows["Passive Only"]["missing_active"])
        self.assertIn("| Entity |", render_subject_audit({"entity_definition_summary": report}, "entity_definition_summary"))

    def test_term_definition_is_informational_only_for_its_exact_term(self):
        audits = build_subject_audits([
            carrier("CA-M-1", "CAPRMEDIO <+ MODEL <+ Term//Word", role="Method", form="Term Definition"),
            carrier("CA-M-2", "Term//Wrong.Name", role="Method", form="Term Definition"),
            carrier("CA-M-3", "Format//markdown", role="Method", form="Term Definition"),
            carrier("CA-R-4", "Owner", ["Term//Word", "Term//Unregistered", "Term//Wrong", "Format//markdown"]),
        ])
        report = audits["subjects_without_declaration_coverage"]
        info = {row["subject"]: row for row in report["informational"]}
        missing = {row["subject"] for row in report["subjects"]}
        self.assertEqual(["CA-M-1@1"], info["Term//Word"]["term_definition_refs"])
        self.assertIn("Term Definition: CA-M-1@1", render_subject_audit(audits, "subjects_without_declaration_coverage"))
        self.assertTrue({"Term//Unregistered", "Term//Wrong", "Format//markdown"} <= missing)
        summary = {row["identity"]: row for row in audits["entity_definition_summary"]["entities"]}
        self.assertFalse(summary["Term//Word"]["missing_definition"])
        self.assertFalse(summary["Term//Word"]["missing_active"])
        self.assertTrue(summary["Term//Unregistered"]["missing_definition"])
        self.assertTrue(summary["Term//Unregistered"]["missing_active"])
        self.assertTrue(summary["Term//Wrong.Name"]["missing_definition"])
        self.assertTrue(summary["Format//markdown"]["missing_definition"])

    def test_exact_relation_and_instance_declarations_cover_their_own_targets(self):
        audits = build_subject_audits([
            carrier("CA-R-1", "Relation//RUN"),
            carrier("CA-R-2", "Node"),
            carrier("CA-R-3", "Node//Example"),
        ])
        missing = audits["subjects_without_declaration_coverage"]["subjects"]
        self.assertNotIn("Relation//RUN", [row["subject"] for row in missing])
        self.assertNotIn("Node//Example", [row["subject"] for row in missing])

    def test_prefixed_cfel_relation_and_known_qualified_selector_are_covered(self):
        audits = build_subject_audits([
            carrier("CA-R-1", "CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//IS_PROPERTY_OF"),
            carrier("CA-R-2", "Atom"), carrier("CA-R-3", "Atom.Role"),
            carrier("CA-R-4", "Atom.Form"),
            carrier("CA-R-5", "Owner", ["Atom/(.Role:=Analysis)/(.Form:=Report)"]),
        ])
        missing = audits["subjects_without_declaration_coverage"]["subjects"]
        self.assertNotIn("CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//IS_PROPERTY_OF", [row["subject"] for row in missing])
        self.assertNotIn("Atom/(.Role := Analysis)/(.Form := Report)", [row["subject"] for row in missing])

    def test_prefixed_allowed_value_selector_binds_existing_property_without_a_value_node(self):
        audits = build_subject_audits([
            carrier("CA-R-1", "CAPRMEDIO <+ MODEL <+ Atom"),
            carrier("CA-R-2", "CAPRMEDIO <+ MODEL <+ Atom.Status"),
            carrier("CA-R-3", "Owner", ["CAPRMEDIO <+ MODEL <+ Atom.Status: Draft"]),
        ])
        missing = audits["subjects_without_declaration_coverage"]["subjects"]
        self.assertNotIn("CAPRMEDIO <+ MODEL <+ Atom.Status: Draft", [row["subject"] for row in missing])

    def test_entity_summary_uses_original_inherited_property_declaration(self):
        audits = build_subject_audits([
            carrier("CA-R-1", "Node"), carrier("CA-R-2", "Node/Child"),
            carrier("CA-R-3", "Node.Status"),
            carrier("CA-R-4", "Owner", ["Node/Child.Status"]),
        ])
        row = next(row for row in audits["entity_definition_summary"]["entities"]
                   if row["identity"] == "Node/Child.Status")
        self.assertEqual(["CA-R-3@1"], row["defining_refs"])
        self.assertTrue(row["missing_active"])

    def test_invalid_passive_values_render_as_diagnostics(self):
        audits = build_subject_audits([carrier("CA-R-1", "Node", [None, "", 3])])
        rendered = render_subject_audit(audits, "passive_only_subjects")
        self.assertIn("## Diagnostics (3)", rendered)
        self.assertIn("CA-R-1@1", rendered)

    def test_metadata_subject_keys_win_over_alias_normalized_read_view(self):
        source = carrier("CA-R-1", "wrong", ["wrong"])
        source["metadata"] = {"subjects": {"active": "Owner", "passive": ["Dependency"]}}
        source["subjects"] = {"active": "Owner", "governs": "Owner", "passive": ["Dependency"], "depends_on": ["Dependency"]}
        audits = build_subject_audits([source])
        report = audits["passive_only_subjects"]
        self.assertEqual(2, report["coverage"]["subject_occurrences"])
        self.assertEqual(["Dependency"], [row["subject"] for row in report["subjects"]])
        self.assertEqual("passive", report["subjects"][0]["occurrences"][0]["source_key"])


if __name__ == "__main__":
    unittest.main()
