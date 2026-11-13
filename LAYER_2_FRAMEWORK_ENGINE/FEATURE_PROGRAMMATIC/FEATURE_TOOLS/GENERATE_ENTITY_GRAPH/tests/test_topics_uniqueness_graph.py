"""Project the reviewed Topics check without executing it."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cfel_claim_constraints import extract_claim_constraints
from contract_graph import compose_contract_graph

CLAIM = '''from caprmedio.formal_claims import Cardinality, declare_entity
from caprmedio.model import Atom

def dependencies_are_distinct(atom: Atom) -> bool:
    return len(atom.dependencies) == len(set(atom.dependencies))

declare_entity(
    entity_name="Dependencies",
    relation_name="IS_PROPERTY_OF",
    base_path="Atom.Header.Context.Topics",
    property_occurrence_cardinality=Cardinality(minimum=0, maximum=1),
    value_format=str,
    value_cardinality=Cardinality(minimum=0, maximum=None),
    dependent_property_cardinality=0,
    instance_check=dependencies_are_distinct,
)
'''


def carrier(code, label="python", subject="Atom.Header.Context.Topics.Dependencies"):
    return {
        "source": {"atom_id": "CA-R-2708", "version": 2, "path": "source.md", "sha256": "reviewed"},
        "subjects": {"active": subject, "passive": []},
        "read_view": {"content_role": "Requirement", "type": "Declaration"},
        "body": f"## Claim\n\n### Formal Claim\n\n```{label}\n{code}\n```\n",
    }


class TopicsUniquenessGraphTests(unittest.TestCase):
    def test_reviewed_check_keeps_property_bounds_and_provenance(self):
        row = carrier(CLAIM)
        clauses, diagnostics = extract_claim_constraints(row)
        self.assertEqual([], diagnostics)
        check, = [c for c in clauses if c["kind"] == "instance_check"]
        self.assertEqual("instances", check["group"])
        self.assertEqual("dependencies_are_distinct", check["callback"])
        self.assertEqual(row["source"], check["source"])
        prop, = [c for c in clauses if c.get("selection") == "property"]
        self.assertEqual({"minimum": 0, "maximum": 1}, prop["effective_occurrence_cardinality"])
        self.assertEqual({"minimum": 0, "maximum": None}, prop["value_cardinality"])
        self.assertEqual("str", prop["value_format"])
        dependent, = [c for c in clauses if c.get("selection") == "immediate_dependents"]
        self.assertEqual({"minimum": 0, "maximum": 0}, dependent["effective_occurrence_cardinality"])
        old, _ = extract_claim_constraints(carrier('''# model
Atom.Header.Context.Topics.Dependencies{::0..1}:: [string]{::0+};
Atom.Header.Context.Topics.Dependencies.*[]{::0}
''', label="CFEL"))
        legacy_prop, = [c for c in old if c.get("selection") == "property"]
        legacy_dependent, = [c for c in old if c.get("selection") == "immediate_dependents"]
        for field in ("effective_occurrence_cardinality", "value_cardinality"):
            self.assertEqual(legacy_prop[field], prop[field])
        self.assertEqual(legacy_dependent["effective_occurrence_cardinality"], dependent["effective_occurrence_cardinality"])
        self.assertEqual("string", legacy_prop["value_format"])
        graph = compose_contract_graph([row])
        entry, = [e for n in graph["entities"] for e in n["own"] if e["source"]["atom_id"] == "CA-R-2708"]
        self.assertEqual([check], entry["instance_clauses"])

    def test_unknown_callback_shapes_fail_closed(self):
        for code in (
            CLAIM.replace("len(atom.dependencies) == len(set(atom.dependencies))", "True"),
            CLAIM.replace("dependencies_are_distinct", "other_check"),
            CLAIM.replace("base_path=\"Atom.Header.Context.Topics\"", "base_path=\"Atom.Header.Context\""),
            CLAIM.replace("dependent_property_cardinality=0", "dependent_property_cardinality=1"),
            CLAIM.replace("instance_check=dependencies_are_distinct,", "minimum_value=0, instance_check=dependencies_are_distinct,"),
        ):
            with self.subTest(code=code):
                clauses, diagnostics = extract_claim_constraints(carrier(code))
                self.assertEqual([], clauses)
                self.assertTrue(any(d["code"] == "python-formal-claim-invalid" for d in diagnostics))

    def test_existing_scope_check_still_projects(self):
        code = '''from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

def check_structural_level(unit: ScopeUnit) -> bool:
    return True

declare_entity(entity_name="structural_level", relation_name="IS_PROPERTY_OF", base_path="Scope Unit", instance_check=check_structural_level)
'''
        clauses, diagnostics = extract_claim_constraints(carrier(code, subject="Scope Unit.structural_level"))
        self.assertEqual([], diagnostics)
        self.assertEqual(["check_structural_level"], [c["callback"] for c in clauses if c["kind"] == "instance_check"])


if __name__ == "__main__":
    unittest.main()
