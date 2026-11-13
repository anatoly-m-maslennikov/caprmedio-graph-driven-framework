from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contract_graph import compose_contract_graph, render_contract_graph
from cfel_claim_constraints import extract_claim_constraints
from subject_projection_data import _relation_declarations, _relation_records

def carrier(name, subject, code, label='CFEL', form='Declaration'):
    return {'source':{'atom_id':name,'version':1,'path':name+'.md'},'subjects':{'active':subject,'passive':[]},'read_view':{'content_role':'Requirement','type':form},'body':f'## Claim\n\n### Formal Claim\n\n```{label}\n{code}\n```\n\n## Semantics\n\nA relation.\n'}

class GraphParity(unittest.TestCase):
    def test_typed_step_check_and_relation_permissions_project_together(self):
        step = carrier('CA-R-2465', 'Atom/(.Header.Context.Role:=Operations)/Step', '''from caprmedio.formal_claims import declare_entity
from caprmedio.model import Operations

class Step(Operations):
    pass

def step_has_one_execution_form(step: Step) -> bool:
    return (len(step.runs) == 1 and not step.contains) or (not step.runs and bool(step.contains))

declare_entity(
    entity_name="Step",
    entity_class=Step,
    instance_check=step_has_one_execution_form,
    instance_relation_constraints={
        "RUNS": {"target_entity_paths": ("Action", "Workflow")},
        "CONTAINS": {"target_entity_paths": ("Step",)},
    },
)
''', 'python')
        clauses, diagnostics = extract_claim_constraints(step)
        self.assertEqual([], diagnostics)
        check, = [clause for clause in clauses if clause['kind'] == 'instance_check']
        self.assertEqual('step_has_one_execution_form', check['callback'])
        self.assertEqual(step['source'], check['source'])
        node, = compose_contract_graph([step])['entities']
        self.assertIn(check, node['own'][0]['instance_clauses'])
        rules = _relation_records(node['target'], node['own'], {}, {})
        self.assertEqual({'RUNS': ('Action', 'Workflow'), 'CONTAINS': ('Step',)}, {
            rule['relation']: rule['contract']['target_entity_paths'] for rule in rules
        })

    def test_instance_property_old_and_native(self):
        old=carrier('CA-R-2524','Project','# instances\nProject//$project_3.order.number:: []{::0}')
        native=carrier('CA-R-2524','Project', '''from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit
class Project(ScopeUnit):
    pass
declare_entity(entity_class=Project, entity_name="Project", instance_property_constraints={"order.number": {"value_cardinality": 0}})''','python')
        graphs=[compose_contract_graph([row]) for row in (old,native)]
        clauses=[next(c for c in g['entities'][0]['own'][0]['instance_clauses'] if c['kind']=='property_constraint') for g in graphs]
        fields=('selection','name_format','occurrence_cardinality','effective_occurrence_cardinality','value_format','value_cardinality','group')
        self.assertEqual([clauses[0][k] for k in fields],[clauses[1][k] for k in fields])
        for c in clauses: self.assertTrue(c['property_selector'].endswith('.order.number'))
        for graph in graphs:
            rendered=render_contract_graph(graph)
            self.assertIn('Instance constraints:',rendered);self.assertIn('order.number` values',rendered);self.assertIn('values count=0',rendered)
    def test_model_inverse_alias_keeps_derived_reverse_view(self):
        c=carrier('CA-R-2965','CFEL <+ Relation//AFTER','''from caprmedio.formal_claims import declare_relation, Cardinality
declare_relation(relation_name="AFTER", source_endpoint={"level": "model_entities", "entity_paths": ("Host",)}, target_endpoint={"level": "model_entities", "entity_paths": ("Target",)}, inverse_alias="BEFORE", targets_per_source=Cardinality(minimum=0, maximum=1), sources_per_target=Cardinality(minimum=0, maximum=2))''','python','Relation Declaration')
        old=carrier('CA-R-2965','CFEL <+ Relation//AFTER','Relation//BEFORE ((IS_INVERSE_ALIAS_FOR)) Relation//AFTER',form='Relation Declaration')
        old_clauses,old_diag=extract_claim_constraints(old); self.assertFalse(old_diag)
        clauses,diag=extract_claim_constraints(c);self.assertFalse(diag)
        inverse=next(x for x in clauses if x.get('relation')=='IS_INVERSE_ALIAS_FOR')
        self.assertEqual((inverse['source_selector'],inverse['target_selector']),('Relation//BEFORE','Relation//AFTER'))
        self.assertEqual(tuple(inverse[k] for k in ('source_selector','relation','target_selector','source_cardinality','target_cardinality','written_direction')),tuple(old_clauses[0][k] for k in ('source_selector','relation','target_selector','source_cardinality','target_cardinality','written_direction')))
        self.assertFalse(any(x.get('relation')=='HAS_INVERSE' for x in clauses))
        graph=compose_contract_graph([c]);self.assertEqual([r['target'] for r in graph['relations']],['AFTER'])
        alias=graph['relations'][0]['derived_aliases'][0];self.assertEqual((alias['name'],alias['classification'],alias['direct_relation']),('BEFORE','Derived','AFTER'))
        endpoint=alias['endpoints'][0];self.assertEqual(endpoint['host']['entity_paths'],('Target',));self.assertEqual(endpoint['target']['entity_paths'],('Host',));self.assertEqual(endpoint['targets_per_source'],{'minimum':0,'maximum':2});self.assertEqual(endpoint['sources_per_target'],{'minimum':0,'maximum':1})
        rendered=render_contract_graph(graph); self.assertIn('Derived Relation `((BEFORE))`',rendered); self.assertIn('IS_INVERSE_ALIAS_FOR bindings',rendered); self.assertNotIn('HAS_INVERSE bindings',rendered)
        aliases=_relation_declarations(graph['relations']);self.assertTrue(any(r['name']=='BEFORE' and r['derivation']=='Derived' and r['direct_relations']==['AFTER'] for r in aliases))

    def test_native_relation_keeps_endpoint_pairs_and_reverses_each_pair(self):
        declaration = carrier('CA-R-2245', 'CFEL <+ Relation//IS_EXECUTION_OF', '''from caprmedio.formal_claims import declare_relation

declare_relation(
    relation_name="IS_EXECUTION_OF",
    endpoint_pairs=(
        {"source_endpoint": {"level": "instances", "entity_paths": ("Workflow Run",)},
         "target_endpoint": {"level": "instances", "entity_paths": ("Workflow",)}},
        {"source_endpoint": {"level": "instances", "entity_paths": ("Step Run",)},
         "target_endpoint": {"level": "instances", "entity_paths": ("Step",)}},
    ),
    inverse_alias="HAS_EXECUTION",
    targets_per_source=1,
)
''', 'python')
        graph = compose_contract_graph([declaration])
        relation, = graph['relations']
        pairs = relation['host_target']
        self.assertEqual(
            [(('Workflow Run',), ('Workflow',)), (('Step Run',), ('Step',))],
            [(p['source_endpoint']['entity_paths'], p['target_endpoint']['entity_paths']) for p in pairs],
        )
        inverse, = relation['derived_aliases']
        self.assertEqual('HAS_EXECUTION', inverse['name'])
        self.assertEqual(
            [(('Workflow',), ('Workflow Run',)), (('Step',), ('Step Run',))],
            [(p['host']['entity_paths'], p['target']['entity_paths']) for p in inverse['endpoints']],
        )
        self.assertTrue(all(p['sources_per_target'] == {'minimum': 1, 'maximum': 1}
                            for p in inverse['endpoints']))
        rendered = render_contract_graph(graph)
        _, _, contracts = rendered.partition('- Host / Target contracts:\n')
        pair_lines = contracts.split('\n- ', 1)[0].splitlines()
        self.assertEqual(2, len(pair_lines))
        self.assertIn('Workflow Run', pair_lines[0])
        self.assertIn('Step Run', pair_lines[1])
        self.assertTrue(all('targets per source=1' in line for line in pair_lines))


if __name__=='__main__':unittest.main()
