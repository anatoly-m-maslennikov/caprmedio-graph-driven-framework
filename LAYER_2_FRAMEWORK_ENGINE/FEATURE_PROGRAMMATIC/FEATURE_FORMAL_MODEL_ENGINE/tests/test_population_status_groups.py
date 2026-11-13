"""Static Atom Status Group filtering for population dependency records."""
from pathlib import Path
import sys
import unittest
P=Path(__file__).resolve().parents[2]
sys.path[:0]=[str(P),str(P/'FEATURE_TOOLS'),str(P/'FEATURE_TOOLS/GENERATE_ENTITY_GRAPH')]
from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import parse_native_model_claim,NativeModelClaimError
from FEATURE_FORMAL_MODEL_ENGINE.native_model_lint import lint_native_model_claim
from FEATURE_FORMAL_MODEL_ENGINE.compiler_claim import compiler_model_statements
from lint_python_model_claim import lint_python_model_claim
from cfel_claim_constraints import _native_constraints
from contract_graph import _clause
CLAIM='''from caprmedio.formal_claims import declare_entity
declare_entity(entity_name="Summary", relation_name="IS_PROPERTY_OF", base_path="Atom.Content",
 property_occurrence_cardinality=1, value_cardinality=1, dependent_property_cardinality=0,
 population_entity_path="Atom", population_functional_dependencies=(
 {"keys": ("Header.Identity.ID",), "dependents": ("Content.Summary",),
  "status_groups": ("Current", "Backlog", "Archived")},))'''
ADDRESSES={'Atom','Atom.Content','Atom.Content.Summary','Atom.Header.Identity.ID','Atom.Header.State.Status'}
class StatusGroupTests(unittest.TestCase):
 def test_filtered_dependency_and_rendering(self):
  decl=parse_native_model_claim(CLAIM)
  self.assertEqual((),lint_python_model_claim(CLAIM,declared_addresses=ADDRESSES,relation_names={'IS_PROPERTY_OF'}))
  self.assertEqual(('Atom.Content.Summary{::1} ::{::1}','Atom.Content.Summary.*[]{::0}'),compiler_model_statements(decl))
  source={'atom_id':'CA-R-1','version':1,'path':'fixture','sha256':'a'}
  row,=[r for r in _native_constraints(decl,source,CLAIM) if r['kind']=='population_functional_dependency']
  self.assertEqual(('Atom',('Header.Identity.ID',),('Content.Summary',),('Current','Backlog','Archived')),(row['population_selector'],row['keys'],row['dependents'],row['status_groups']))
  self.assertEqual(source,row['source']);self.assertNotIn('Draft',row['status_groups'])
  self.assertIn('Status Group in (Current, Backlog, Archived)',_clause(row))
 def test_invalid_filters_and_missing_paths(self):
  for bad in [CLAIM.replace('"Current", "Backlog", "Archived"','"Current", "NoSuchGroup"'),CLAIM.replace('"Current", "Backlog", "Archived"','"Draft", "Draft"'),CLAIM.replace('"Current", "Backlog", "Archived"','["bad"]'),CLAIM.replace('population_entity_path="Atom"','population_entity_path="Other"'),CLAIM.replace('"status_groups": ("Current", "Backlog", "Archived")','"status_groups": ()')]:
   with self.subTest(bad=bad),self.assertRaises(NativeModelClaimError):parse_native_model_claim(bad)
  for missing in ADDRESSES:
   with self.subTest(missing=missing):
    self.assertTrue(lint_python_model_claim(CLAIM,declared_addresses=ADDRESSES-{missing},relation_names={'IS_PROPERTY_OF'}))
if __name__=='__main__':unittest.main()
