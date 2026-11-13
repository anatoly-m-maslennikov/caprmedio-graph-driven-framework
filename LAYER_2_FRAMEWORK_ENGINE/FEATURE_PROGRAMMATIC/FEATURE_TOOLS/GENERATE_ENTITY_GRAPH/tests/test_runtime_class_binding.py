from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contract_graph import compose_contract_graph

def carrier(n, subject, cls, base, entity):
    text=f'from caprmedio.formal_claims import declare_entity\nfrom caprmedio.model import {base}\n\nclass {cls}({base}):\n    pass\n\ndeclare_entity(entity_class={cls}, entity_name={entity!r})'
    return {'source':{'atom_id':f'CA-R-{n}','version':1,'path':f'{n}.md'}, 'subjects':{'active':subject,'passive':[]}, 'body':f'## Claim\n\n### Formal Claim\n\n```python\n{text}\n```\n', 'read_view':{'content_role':'Requirement','type':'Declaration'}}
def edge_set(graph):
    nodes={n['id']:n['identity'] for n in graph['nodes']}
    return {(nodes[e['relation_source']],nodes[e['relation_target']]) for e in graph['edges']}

class ClassBinding(unittest.TestCase):
    def test_exact_class_and_competing_binding(self):
        rows=[carrier(1,'Runtime','Runtime','Occurrent','Runtime'),carrier(2,'Workflow/(.Purpose := Runtime)','WorkflowRuntime','Workflow','Runtime'),carrier(3,'Internal Local Runtime','InternalLocalRuntime','Runtime','Internal Local Runtime')]
        tree=compose_contract_graph(rows)['narrowing_tree']
        self.assertIn(('Internal Local Runtime','Runtime'),edge_set(tree))
        rows.append(carrier(4,'Other/Runtime','Runtime','Occurrent','Runtime'))
        tree=compose_contract_graph(rows)['narrowing_tree']
        self.assertNotIn(('Internal Local Runtime','Runtime'),edge_set(tree))
        self.assertTrue(any('native base `Runtime` is unresolved or ambiguous' in d for d in tree['diagnostics']))
    def test_duplicate_same_target_is_ambiguous(self):
        rows=[carrier(1,'Runtime','Runtime','Occurrent','Runtime'),carrier(2,'Runtime','Runtime','Occurrent','Runtime'),carrier(3,'Internal Local Runtime','InternalLocalRuntime','Runtime','Internal Local Runtime')]
        tree=compose_contract_graph(rows)['narrowing_tree']
        self.assertNotIn(('Internal Local Runtime','Runtime'),edge_set(tree))
        self.assertTrue(any('native base `Runtime` is unresolved or ambiguous' in d for d in tree['diagnostics']))

if __name__=='__main__': unittest.main()
