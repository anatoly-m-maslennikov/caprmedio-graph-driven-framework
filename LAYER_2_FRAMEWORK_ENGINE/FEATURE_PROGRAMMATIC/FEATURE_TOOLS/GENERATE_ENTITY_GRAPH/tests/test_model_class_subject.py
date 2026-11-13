from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contract_graph import compose_contract_graph
from FEATURE_FORMAL_MODEL_ENGINE.model_catalog import class_bindings, compile_native
from FEATURE_FORMAL_MODEL_ENGINE.compiler_claim import compiler_model_statements

def carrier(n, subject, entity):
    code=f'from caprmedio.formal_claims import declare_entity\nfrom caprmedio.model import Node\nclass Element(Node):\n    pass\ndeclare_entity(entity_class=Element, entity_name="{entity}")'
    return {'source':{'atom_id':f'CA-R-{n}','version':1,'path':f'{n}.md'},'subjects':{'governs':subject},'body':f'## Claim\n\n### Formal Claim\n\n```python\n{code}\n```\n','read_view':{'content_role':'Requirement','type':'Declaration'}}

def graph_bindings(rows):
    graph=compose_contract_graph(rows)
    return [(n['target'],entry['source']['atom_id']) for k in ('entities','components','namespaces','relations') for n in graph[k] for entry in n['own'] for c in entry['clauses'] if c['kind']=='native_class']

class ModelClassSubjectTests(unittest.TestCase):
    def test_component_qualified_and_entity_agree(self):
        for subject,target in [('CAPRMEDIO_MODEL <+ CFEL <+ Element','Element'),('CAPRMEDIO_MODEL <+ Element','Element'),('CAPRMEDIO_MODEL <+ Node/Element','Node/Element')]:
            with self.subTest(subject=subject):
                rows=[carrier(1,subject,'Element')];bindings=class_bindings(rows)
                self.assertEqual([(target,'CA-R-1')],graph_bindings(rows))
                self.assertEqual([(target,'CA-R-1')],[(x,s['atom_id']) for x,s in bindings['Element']])
    def test_property_mismatched_name_and_wrong_namespace_rejected(self):
        for subject,name in [('CAPRMEDIO_MODEL <+ Atom.Content.Foo','Foo'),('CAPRMEDIO_MODEL <+ CFEL <+ Element','Other'),('CAPRMEDIO_STRUCTURE <+ Element','Element'),('CAPRMEDIO_MODEL <+ Atom.Content.Foo','Element')]:
            with self.subTest(subject=subject,name=name):
                rows=[carrier(1,subject,name)];self.assertEqual({},class_bindings(rows));self.assertEqual([],graph_bindings(rows))
    def test_duplicate_binding_fails_closed(self):
        rows=[carrier(1,'CAPRMEDIO_MODEL <+ CFEL <+ Element','Element'),carrier(2,'CAPRMEDIO_MODEL <+ CFEL <+ Element','Element')]
        bindings=class_bindings(rows);self.assertEqual(2,len(bindings['Element']))
        code='from caprmedio.formal_claims import declare_entity\nfrom caprmedio.model import Element\ndeclare_entity(entity_name="P", relation_name="IS_PROPERTY_OF", base_path="Atom", value_format=Element)'
        with self.assertRaisesRegex(ValueError,'missing or ambiguous Model class binding'):compile_native(code,bindings)

if __name__=='__main__':unittest.main()
