"""Static direct-container uniqueness; no Python Claim is executed."""
from pathlib import Path
import sys,unittest
P=Path(__file__).resolve().parents[2]
sys.path[:0]=[str(P),str(P/'FEATURE_TOOLS'),str(P/'FEATURE_TOOLS/GENERATE_ENTITY_GRAPH')]
from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import parse_native_model_claim,NativeModelClaimError
from FEATURE_FORMAL_MODEL_ENGINE.native_model_lint import lint_native_model_claim
from FEATURE_FORMAL_MODEL_ENGINE.compiler_claim import compiler_model_statements
from lint_python_model_claim import lint_python_model_claim
from cfel_claim_constraints import _native_constraints
from contract_graph import _clause
PLAN='Atom/(.Header.Context.Role:=Plan)';SEQ='Header.Context.Plan.Work Sequence Number';BASE=PLAN+'.Header.Context.Plan';PROP=PLAN+'.'+SEQ
CLAIM=f'''from caprmedio.formal_claims import Cardinality, declare_entity
declare_entity(entity_name="Work Sequence Number", relation_name="IS_PROPERTY_OF", base_path="{BASE}", value_format=int,
 value_cardinality=Cardinality(minimum=0, maximum=1), minimum_value=1, dependent_property_cardinality=0,
 population_entity_path="{PLAN}", population_unique_constraints=(
 {{"keys": ("Header.Context.Container.atom", "{SEQ}"), "status":"Active", "single_value_paths": ("Header.Context.Container.atom", "{SEQ}")}},
 {{"keys": ("Header.Context.Container.scope_unit", "{SEQ}"), "status":"Active", "single_value_paths": ("Header.Context.Container.scope_unit", "{SEQ}")}},))'''
CATALOG={'Atom','Atom.Header.Context.Role','Atom.Header.Context.Container.atom','Atom.Header.Context.Container.scope_unit','Atom.Header.State.Status',PLAN,BASE,PROP}
class PlanSequenceTests(unittest.TestCase):
 def lint(self,claim=CLAIM,addresses=CATALOG):return lint_python_model_claim(claim,declared_addresses=addresses,relation_names={'IS_PROPERTY_OF'})
 def test_two_direct_containers_and_optional_positive_int(self):
  d=parse_native_model_claim(CLAIM);self.assertEqual((),self.lint());stmts=compiler_model_statements(d)
  self.assertEqual((PROP+' :: [int]{::0..1}',PROP+'.*[]{::0}',PROP+' >= 1'),stmts)
  source={'atom_id':'CA-R-1','version':1,'path':'fixture','sha256':'a'};rows=_native_constraints(d,source,CLAIM)
  rules=[r for r in rows if r['kind']=='population_unique_constraint'];self.assertEqual(2,len(rules))
  self.assertEqual({('Header.Context.Container.atom',SEQ),('Header.Context.Container.scope_unit',SEQ)},{r['keys'] for r in rules})
  for rule in rules:
   self.assertEqual('Active',rule['status']);self.assertEqual(PLAN,rule['population_selector']);self.assertEqual(set(rule['keys']),set(rule['single_value_paths']));self.assertEqual(source,rule['source']);self.assertIn('unique',_clause(rule))
  self.assertTrue(any(r.get('operator')=='>=' and r.get('value')==1 for r in rows))
 def test_malformed_and_unresolved_inputs(self):
  for bad in (CLAIM.replace('"status":"Active"','"status":"Draft"',1), CLAIM.replace('"single_value_paths": ("Header.Context.Container.atom", "'+SEQ+'")','"single_value_paths": ("'+SEQ+'",)'),CLAIM.replace('"Header.Context.Container.atom", "'+SEQ+'"','"../atom", "'+SEQ+'"',1),CLAIM.replace('population_entity_path="'+PLAN+'"','population_entity_path="Other"')):
   with self.subTest(bad=bad),self.assertRaises(NativeModelClaimError):parse_native_model_claim(bad)
  for missing in ('Atom.Header.Context.Container.atom','Atom.Header.Context.Container.scope_unit','Atom.Header.State.Status',PROP):
   with self.subTest(missing=missing):self.assertTrue(self.lint(addresses=CATALOG-{missing}))
if __name__=='__main__':unittest.main()
