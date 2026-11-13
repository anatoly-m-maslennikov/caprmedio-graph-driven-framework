"""Unfiltered uniqueness is distinct from Active Plan uniqueness."""
from pathlib import Path
import sys, unittest
P=Path(__file__).resolve().parents[2];sys.path[:0]=[str(P),str(P/'FEATURE_TOOLS'),str(P/'FEATURE_TOOLS/GENERATE_ENTITY_GRAPH')]
from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import parse_native_model_claim
from cfel_claim_constraints import extract_claim_constraints
from contract_graph import _clause
from lint_python_model_claim import lint_python_model_claim
CLAIM='''from caprmedio.formal_claims import declare_entity
declare_entity(entity_name="ID", relation_name="IS_PROPERTY_OF", base_path="Event Record",
    property_occurrence_cardinality=1, value_format=str, value_cardinality=1,
    dependent_property_cardinality=0, population_entity_path="Event Record",
    population_unique_constraints=({"keys": ("ID",)},))
'''
class EventIDTests(unittest.TestCase):
 def test_unfiltered_rule_and_catalog(self):
  rule=parse_native_model_claim(CLAIM)['arguments']['population_unique_constraints'][0]
  self.assertEqual({'keys':('ID',)},rule)
  self.assertEqual((),lint_python_model_claim(CLAIM,declared_addresses=['Event Record','Event Record.ID'],relation_names=['IS_PROPERTY_OF']))
  self.assertTrue(lint_python_model_claim(CLAIM,declared_addresses=['Event Record'],relation_names=['IS_PROPERTY_OF']))
  row={'source':{'atom_id':'CA-R-1','version':1,'path':'x','sha256':'a'*64},'body':'## Claim\n### Formal Claim\n```python\n'+CLAIM+'```\n','read_view':{'content_role':'Requirement'}}
  records,diags=extract_claim_constraints(row);self.assertEqual([],diags)
  uniq=next(x for x in records if x['kind']=='population_unique_constraint')
  self.assertEqual(('Event Record',('ID',)),(uniq['population_selector'],uniq['keys']))
  self.assertNotIn('status',uniq);self.assertNotIn('single_value_paths',uniq);self.assertIn('unique ID',_clause(uniq))
  for invalid in (CLAIM.replace('{"keys": ("ID",)}','{"keys": ("ID",), "status": "Active"}'), CLAIM.replace('{"keys": ("ID",)}','{"keys": ()}')):
   with self.assertRaises(ValueError):parse_native_model_claim(invalid)
if __name__=='__main__':unittest.main()
