"""Static nearest-container fallback chain; the Claim is never executed."""
from pathlib import Path
import sys, unittest
P=Path(__file__).resolve().parents[2]
sys.path[:0]=[str(P),str(P/'FEATURE_TOOLS'),str(P/'FEATURE_TOOLS/GENERATE_ENTITY_GRAPH')]
from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import parse_native_model_claim,NativeModelClaimError
from FEATURE_FORMAL_MODEL_ENGINE.native_model_lint import lint_native_model_claim
from FEATURE_FORMAL_MODEL_ENGINE.compiler_claim import compiler_model_statements
from lint_python_model_claim import lint_python_model_claim
from cfel_claim_constraints import _native_constraints
from contract_graph import _clause
PLAN='Atom/(.Header.Context.Role:=Plan)'
PROP=PLAN+'.Header.Context.Plan.AI Agent Confidence Threshold'
PROJECT='Project.Settings.AI Agent Confidence Threshold'
CLAIM=f'''from caprmedio.formal_claims import Cardinality, declare_entity
declare_entity(entity_name="AI Agent Confidence Threshold", relation_name="IS_PROPERTY_OF",
 base_path="{PLAN}.Header.Context.Plan", value_format=int,
 value_cardinality=Cardinality(minimum=0, maximum=1), minimum_value=0, maximum_value=100,
 dependent_property_cardinality=0, fallback_chain=(
 {{"lookup_relation":"IS_CONTAINED_BY","lookup_property":"{PROP}"}},
 {{"project_entity":"Project","project_property":"{PROJECT}"}},))'''
CATALOG={'Atom','Atom.Header.Context.Role',PLAN,PLAN+'.Header.Context.Plan',PROP,'Project','Project.Settings',PROJECT}
class FallbackChainTests(unittest.TestCase):
 def lint(self,claim=CLAIM,addresses=CATALOG,relations={'IS_PROPERTY_OF','IS_CONTAINED_BY'}):
  return lint_python_model_claim(claim,declared_addresses=addresses,relation_names=relations,path='fixture')
 def test_chain_and_provenance(self):
  decl=parse_native_model_claim(CLAIM);self.assertEqual((),self.lint())
  source={'atom_id':'CA-R-1','version':1,'path':'fixture','sha256':'fixture'}
  row,=[r for r in _native_constraints(decl,source,CLAIM) if r['kind']=='effective_value_fallback_chain']
  self.assertEqual(source,row['source']);self.assertEqual(('undefined','null',''),row['empty_values']);self.assertEqual(1,row['project_cardinality'])
  self.assertEqual(('IS_CONTAINED_BY',PROP,'Project',PROJECT),(row['branches'][0]['lookup_relation'],row['branches'][0]['lookup_property'],row['branches'][1]['project_entity'],row['branches'][1]['project_property']))
  self.assertIn('via `IS_CONTAINED_BY`',_clause(row))
  self.assertEqual((PROP+' :: [int, 0..100]{::0..1}',PROP+'.*[]{::0}'),compiler_model_statements(decl))
 def test_empty_semantics_preserve_zero_false_and_invalid(self):
  empty = object()
  def is_empty(value):
   return value is empty or value is None or (type(value) is str and value == "")
  self.assertTrue(all(is_empty(v) for v in (empty,None,"")))
  self.assertTrue(all(not is_empty(v) for v in (0,False,101,"invalid")))
  self.assertEqual(0, 0 if not is_empty(0) else 90)
  for value in (False,101,"invalid"):
   self.assertFalse(is_empty(value))
   self.assertTrue(type(value) is not int or not 0 <= value <= 100)
 def test_reject_bad_shapes_and_unresolved_paths(self):
  for bad in (CLAIM.replace('"lookup_relation":"IS_CONTAINED_BY"','"unknown":"IS_CONTAINED_BY"'), CLAIM.replace('"project_entity":"Project"','"project_entity":"Other"'),CLAIM.replace('fallback_chain=(', 'fallback_value=1, fallback_chain=('),CLAIM.replace(f'"project_property":"{PROJECT}"','"project_property":"Other.Threshold"')):
   with self.subTest(bad=bad),self.assertRaises(NativeModelClaimError):parse_native_model_claim(bad)
  for missing in (PROP,PROJECT,'Project'):
   with self.subTest(missing=missing):self.assertTrue(self.lint(addresses=CATALOG-{missing}))
  self.assertTrue(self.lint(relations={'IS_PROPERTY_OF'}))
if __name__=='__main__':unittest.main()
