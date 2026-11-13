from pathlib import Path
import re,sys,unittest
P=Path(__file__).resolve().parents[2];sys.path[:0]=[str(P),str(P/'FEATURE_TOOLS'),str(P/'FEATURE_TOOLS/GENERATE_ENTITY_GRAPH')]
from python_model_claim import compile_python_model_claim
from cfel_claim_constraints import extract_claim_constraints
from lint_python_model_claim import lint_python_model_claim
class WorkspaceRelationTests(unittest.TestCase):
 def test_authored_direction_and_cardinality(self):
  claim = """from dataclasses import dataclass, field
from caprmedio.formal_claims import Cardinality, declare_entity

@dataclass
class Workspace:
    native_thread_id: str = field(metadata={"property_occurrence_cardinality": Cardinality(minimum=0, maximum=1), "value_cardinality": Cardinality(minimum=0, maximum=1)})
    project_root: str = field(metadata={"property_occurrence_cardinality": 1, "value_cardinality": 1})

declare_entity(entity_name="Workspace", entity_class=Workspace,
    incoming_model_relations=({"source": "View", "relation": "IS_CONTAINED_BY", "source_cardinality": 1, "target_cardinality": Cardinality(minimum=1, maximum=None)},))
"""
  body = '## Claim\n### Formal Claim\n```python\n' + claim + '```\n'
  self.assertEqual('View {::1}((IS_CONTAINED_BY)){::1+} Workspace',compile_python_model_claim(claim)[-1])
  row={'source':{'atom_id':'R','version':1,'path':'x','sha256':'x'},'body':body,'read_view':{'content_role':'Requirement'}}
  records,errors=extract_claim_constraints(row);self.assertEqual([],errors);rel=records[-1]
  self.assertEqual(('View','Workspace','IS_CONTAINED_BY',{'minimum':1,'maximum':1},{'minimum':1,'maximum':None}),tuple(rel[k] for k in ('source_selector','target_selector','relation','source_cardinality','target_cardinality')))
  good=lint_python_model_claim(claim,declared_addresses=['View','Workspace'],relation_names=['IS_CONTAINED_BY']);self.assertEqual((),good)
  self.assertTrue(lint_python_model_claim(claim,declared_addresses=['Workspace'],relation_names=['IS_CONTAINED_BY']))
  self.assertTrue(lint_python_model_claim(claim,declared_addresses=['View','Workspace'],relation_names=[]))
  with self.assertRaises(ValueError):compile_python_model_claim(claim.replace('"source_cardinality": 1','"source_cardinality": -1'))
 def test_incoming_without_dataclass_contract_fails_closed(self):
  bad = 'from caprmedio.formal_claims import declare_entity\ndeclare_entity(entity_name="Workspace", incoming_model_relations=())'
  with self.assertRaises(ValueError): compile_python_model_claim(bad)
if __name__=='__main__':unittest.main()
