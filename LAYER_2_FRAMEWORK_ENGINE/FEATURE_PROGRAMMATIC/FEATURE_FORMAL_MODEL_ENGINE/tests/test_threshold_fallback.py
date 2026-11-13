"""Threshold format and literal fallback remain static declaration data."""
from pathlib import Path
import sys
import unittest

PROGRAMMATIC = Path(__file__).resolve().parents[2]
TOOLS = PROGRAMMATIC / "FEATURE_TOOLS"
sys.path[:0] = [str(PROGRAMMATIC), str(TOOLS), str(TOOLS / "GENERATE_ENTITY_GRAPH")]

from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import parse_native_model_claim, NativeModelClaimError
from FEATURE_FORMAL_MODEL_ENGINE.compiler_claim import compiler_model_statements
from cfel_claim_constraints import _native_constraints
CLAIM='''from caprmedio.formal_claims import declare_entity
declare_entity(entity_name="AI Agent Confidence Threshold", relation_name="IS_PROPERTY_OF", base_path="Project.Settings", property_occurrence_cardinality=1, value_format=int, value_cardinality=1, dependent_property_cardinality=0, minimum_value=0, maximum_value=100, fallback_value=90)
'''
class ThresholdTests(unittest.TestCase):
 def test_constraints_and_fallback(self):
  decl=parse_native_model_claim(CLAIM);self.assertEqual(compiler_model_statements(decl),('Project.Settings.AI Agent Confidence Threshold{::1} :: [int, 0..100]{::1} ?== 90','Project.Settings.AI Agent Confidence Threshold.*[]{::0}'))
  rec=_native_constraints(decl,{'atom_id':'fixture'},CLAIM);self.assertEqual({(r['operator'],r['value']) for r in rec if r['kind']=='property_value_bound'},{('>=',0),('<=',100)});self.assertEqual(next(r['fallback_literal'] for r in rec if r['kind']=='effective_value_fallback'),90)
 def test_bad_values(self):
  for bad in (CLAIM.replace('fallback_value=90','fallback_value=101'), CLAIM.replace('maximum_value=100','maximum_value=-1')):
   with self.assertRaises(NativeModelClaimError):parse_native_model_claim(bad)
