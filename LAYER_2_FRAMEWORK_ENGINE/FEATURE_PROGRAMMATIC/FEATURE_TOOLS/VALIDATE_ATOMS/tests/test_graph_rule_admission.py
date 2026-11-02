"""Runtime admission for the source-governed Requirement/Graph Rule form."""

from copy import deepcopy
from pathlib import Path
import sys
import unittest

TOOL = Path(__file__).resolve().parents[1]
TOOLS = TOOL.parent
sys.path[:0] = [str(TOOLS), str(TOOL)]

from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.check_dispatch import ADAPTERS  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.check_schema_extended import ADAPTERS as SCHEMA_ADAPTERS  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.authority import Obligation  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.check_support import Check  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.check_sections import GRAPH_RULE_SOURCES  # noqa: E402
from project_selection import bind_selection  # noqa: E402
import test_proposed_carrier_admission_regressions as fixtures  # noqa: E402


SOURCE_IDS = GRAPH_RULE_SOURCES
WHITELIST = '''# Summary

Permit evaluation links to requirements.

```yaml
graph_rule_type: whitelist
applies_to:
  relation_type: evaluation_for
condition:
  source:
    - "Entity/Node/Continuant/Atom/Content Role: Evaluation"
  target:
    - "Entity/Node/Continuant/Atom/Content Role: Requirement"
```
'''
CARDINALITY = '''# Summary

Cardinality source fixture.

```yaml
graph_rule_type: cardinality
applies_to:
  node: "Entity/Node/Continuant/Selection//Dependent Entity Occurrences"
  relation_type: IS_BORNE_BY
  direction: outgoing
condition:
  other_endpoint:
    - Entity
  minimum: 0
  maximum: null
```
'''
REQUIREMENT_BODY = """# Summary

Ordinary requirement.

## Scope

The applicable graph cases.

## Claim

The required condition.

## Details

Additional explanation.
"""


class GraphRuleAdmissionTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ProposedCarrierAdmissionRegressions()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.selection = self.fixture.project(source_ids=(*SOURCE_IDS, "CA-R-1309"))
        self.context = proposed_carrier.source_context_from_project(self.selection.root)
        self.rule_inputs = proposed_carrier._type_inputs(
            self.context, self.graph_rule_metadata()
        )

    def check(self, inputs=None):
        return Check(
            Obligation("test", [], True, "verified selected authority"),
            self.context.authority,
            deepcopy(self.rule_inputs if inputs is None else inputs),
        )

    @staticmethod
    def graph_rule_metadata(**changes):
        metadata = {
            "atom_id": "CA-R-999901",
            "content_role": "Requirement",
            "type": "Graph Rule",
            "subjects": {"governs": "Entity/Node/Continuant/Atom.Relations", "depends_on": []},
            "relations": {},
        }
        metadata.update(changes)
        return metadata

    def test_current_requirement_type_authority_admits_graph_rule(self):
        check = self.check()
        SCHEMA_ADAPTERS["model.domains"](self.graph_rule_metadata(), WHITELIST, check)
        self.assertEqual((check.findings, check.gaps), ([], []))

    def test_missing_changed_or_ambiguous_type_authority_cannot_admit(self):
        for mode in ("missing", "changed", "ambiguous"):
            with self.subTest(mode=mode):
                inputs = deepcopy(self.rule_inputs)
                rows = inputs["sources"]
                source = next(row for row in rows if row["binding"]["atom_id"] == "CA-R-2001")
                if mode == "missing":
                    rows.remove(source)
                elif mode == "changed":
                    source["text"] += "\nChanged after observation.\n"
                else:
                    rows.append(deepcopy(source))
                check = self.check(inputs)
                SCHEMA_ADAPTERS["model.domains"](self.graph_rule_metadata(), WHITELIST, check)
                self.assertTrue(check.findings or check.gaps)

    def test_graph_rule_body_requires_current_delivery_and_schema_authority(self):
        for identifier in ("CA-R-2001", "CA-D-637", "CA-R-1996"):
            for mode in ("missing", "changed", "ambiguous"):
                with self.subTest(identifier=identifier, mode=mode):
                    inputs = deepcopy(self.rule_inputs)
                    rows = inputs["sources"]
                    source = next(row for row in rows if row["binding"]["atom_id"] == identifier)
                    if mode == "missing":
                        rows.remove(source)
                    elif mode == "changed":
                        source["text"] += "\nChanged after observation.\n"
                    else:
                        rows.append(deepcopy(source))
                    check = self.check(inputs)
                    ADAPTERS["body.sections"](
                        self.graph_rule_metadata(), WHITELIST, check
                    )
                    self.assertTrue(check.findings or check.gaps)

    def test_graph_rule_body_accepts_precise_subject_without_entity_graph_rule_marker(self):
        metadata = self.graph_rule_metadata(
            subjects={
                "governs": "Entity/Node/Continuant/Atom.Status",
                "depends_on": ["Entity/Node/Continuant/Atom.Relations"],
            }
        )
        check = self.check()
        ADAPTERS["body.sections"](metadata, WHITELIST, check)
        self.assertEqual((check.findings, check.gaps), ([], []))

    def test_cardinality_body_is_structurally_admitted_without_evaluation(self):
        check = self.check()
        ADAPTERS["body.sections"](self.graph_rule_metadata(), CARDINALITY, check)
        self.assertEqual((check.findings, check.gaps), ([], []))

    def test_cardinality_body_keeps_current_source_authority_gate(self):
        for identifier in SOURCE_IDS:
            for mode in ("missing", "changed", "ambiguous"):
                with self.subTest(identifier=identifier, mode=mode):
                    inputs = deepcopy(self.rule_inputs)
                    rows = inputs["sources"]
                    source = next(row for row in rows if row["binding"]["atom_id"] == identifier)
                    if mode == "missing":
                        rows.remove(source)
                    elif mode == "changed":
                        source["text"] += "\nChanged after observation.\n"
                    else:
                        rows.append(deepcopy(source))
                    check = self.check(inputs)
                    ADAPTERS["body.sections"](
                        self.graph_rule_metadata(), CARDINALITY, check
                    )
                    self.assertTrue(check.findings or check.gaps)

    def test_ordinary_requirement_and_generic_rule_keep_prose_layout(self):
        untyped = self.check()
        SCHEMA_ADAPTERS["model.domains"](
            {"content_role": "Requirement"}, REQUIREMENT_BODY, untyped
        )
        self.assertEqual((untyped.findings, untyped.gaps), ([], []))

        generic_rule = self.check()
        ADAPTERS["body.sections"](
            {"content_role": "Requirement", "type": "Rule"},
            REQUIREMENT_BODY,
            generic_rule,
        )
        self.assertEqual((generic_rule.findings, generic_rule.gaps), ([], []))

    def test_graph_rule_rejects_malformed_and_noncanonical_body_carriers(self):
        malformed = (
            WHITELIST.replace("relation_type: evaluation_for", "relation_type: ["),
            WHITELIST.replace("```yaml", "## Claim\nDuplicate prose.\n\n```yaml"),
            WHITELIST + "```yaml\nother: block\n```\n",
            WHITELIST.replace("graph_rule_type: whitelist", "type: whitelist"),
        )
        for body in malformed:
            with self.subTest(body=body[:70]):
                check = self.check()
                ADAPTERS["body.sections"](self.graph_rule_metadata(), body, check)
                self.assertTrue(check.findings or check.gaps)

        wrong_role = self.check()
        SCHEMA_ADAPTERS["model.domains"](
            self.graph_rule_metadata(content_role="Delivery"), WHITELIST, wrong_role
        )
        self.assertTrue(wrong_role.findings or wrong_role.gaps)

    def test_declared_forms_without_complete_schemas_remain_gaps(self):
        for rule_type in (
            "blacklist",
            "value_constraint",
            "topology_constraint",
            "endpoint_constraint",
        ):
            with self.subTest(rule_type=rule_type):
                check = self.check()
                body = WHITELIST.replace("graph_rule_type: whitelist", f"graph_rule_type: {rule_type}")
                ADAPTERS["body.sections"](self.graph_rule_metadata(), body, check)
                self.assertFalse(check.findings)
                self.assertTrue(check.gaps)

    def test_complete_graph_rule_carrier_passes_the_public_admission_path(self):
        metadata = self.fixture.metadata(
            "amber",
            atom_id="CA-R-999901",
            content_role="Requirement",
            type="Graph Rule",
            subjects={
                "governs": "Entity/Node/Continuant/Atom.Relations",
                "depends_on": [],
            },
            relations={},
        )
        with bind_selection(self.selection):
            result = proposed_carrier.validate_proposed_carrier(
                metadata,
                WHITELIST,
                self.context,
                Path("04_requirement/CA-R-999901--graph-rule.md"),
                allow_existing_relations=True,
            )
        self.assertEqual((result["findings"], result["gaps"]), ([], []))

    def test_ordinary_plan_still_validates_without_graph_rule_sources(self):
        fixture = fixtures.ProposedCarrierAdmissionRegressions()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        selection = fixture.project()
        context = proposed_carrier.source_context_from_project(selection.root)
        selected = {row["binding"]["atom_id"] for row in context.inputs["sources"]}
        self.assertTrue(set(SOURCE_IDS).isdisjoint(selected))
        with bind_selection(selection):
            result = proposed_carrier.validate_proposed_carrier(
                fixture.metadata(),
                fixtures.PLAN_BODY,
                context,
                Path("03_plan/CA-P-701--independent-plan.md"),
                allow_existing_relations=True,
            )
        self.assertEqual((result["findings"], result["gaps"]), ([], []))


if __name__ == "__main__":
    unittest.main()
