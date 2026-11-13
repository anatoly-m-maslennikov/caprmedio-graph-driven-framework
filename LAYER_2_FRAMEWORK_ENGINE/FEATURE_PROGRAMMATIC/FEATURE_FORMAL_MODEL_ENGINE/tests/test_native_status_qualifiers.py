"""Regressions for Role- and Form-qualified native Status declarations."""
from pathlib import Path
import sys
import unittest
from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import NativeModelClaimError, parse_native_model_claim
from FEATURE_FORMAL_MODEL_ENGINE.compiler_claim import compiler_model_statements
from FEATURE_WORKBENCH_BACKEND.workbench_schema_asset import compile_status_groups
from ATOM_LIFECYCLE.status_model import _DECL, _STATUS_ORDER

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "FEATURE_TOOLS" / "GENERATE_ENTITY_GRAPH"))
from cfel_claim_constraints import _native_constraints

PLAN = '''from caprmedio.model import Plan
from caprmedio.formal_claims import declare_entity
declare_entity(entity_name="Status", relation_name="IS_PROPERTY_OF", base_path="Atom.Header.State", applies_to_entity_classes=(Plan,), allowed_values=("Backlog", "Done", "Canceled"), status_order_numbers={"Backlog": 1, "Done": 20, "Canceled": 40}, status_groups={"Backlog": "Backlog"})'''
ANALYSIS = '''from caprmedio.formal_claims import declare_entity
declare_entity(entity_name="Status", relation_name="IS_PROPERTY_OF", base_path="Atom.Header.State", applies_to_role="Analysis and Advisory", applies_to_forms=("Analysis Report", "Rationale"), allowed_values=("Done",))'''

class NativeStatusQualifiers(unittest.TestCase):
    def test_explicit_none_rejected(self):
        for name in ("status_groups", "applies_to_role", "applies_to_forms"):
            with self.subTest(name=name), self.assertRaises(NativeModelClaimError):
                parse_native_model_claim(PLAN.replace('status_groups={"Backlog": "Backlog"}', name + '=None'))

    def test_plan_group_order_and_graph(self):
        declaration = parse_native_model_claim(PLAN)
        statements = compiler_model_statements(declaration)
        self.assertEqual(compile_status_groups([(s, 'CA-R-1539') for s in statements]), (('Plan', 'Backlog', 'Backlog'),))
        self.assertEqual({(_STATUS_ORDER.fullmatch(s)['status'], int(_STATUS_ORDER.fullmatch(s)['order'])) for s in statements if _STATUS_ORDER.fullmatch(s)}, {('Backlog', 1), ('Done', 20), ('Canceled', 40)})
        rows = _native_constraints(declaration, {'atom_id': 'CA-R-1539'}, PLAN)
        self.assertTrue(any(r.get('axis') == 'Status Group' and r.get('value') == 'Backlog' and 'Role := Plan' in r.get('subject_selector', '') for r in rows))

    def test_analysis_only_two_forms(self):
        declaration = parse_native_model_claim(ANALYSIS)
        statements = compiler_model_statements(declaration)
        decoded = {(_DECL.fullmatch(s)['role'].strip('"'), _DECL.fullmatch(s)['form'], _DECL.fullmatch(s)['value']) for s in statements}
        self.assertEqual(decoded, {('Analysis and Advisory', 'Analysis Report', 'Done'), ('Analysis and Advisory', 'Rationale', 'Done')})
        rows = _native_constraints(declaration, {'atom_id': 'CA-R-1875'}, ANALYSIS)
        self.assertEqual(len([r for r in rows if r.get('kind') == 'allowed_literal']), 2)
        self.assertTrue(all('Header.Context.Form in (' in r['property_selector'] for r in rows))

if __name__ == '__main__':
    unittest.main()
