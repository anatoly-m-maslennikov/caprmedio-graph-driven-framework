"""Allowed classification values retain the existing source facts."""
from copy import deepcopy
from pathlib import Path
import re
import sys
import unittest

TOOL = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOL.parent), str(TOOL)]

from cfel_claim_constraints import extract_claim_constraints
from current_subject_graph import compose_enhanced_current_graph
from readable_entity_tree import render_model


class AllowedClassificationValuesTests(unittest.TestCase):
    def test_allowed_values_match_across_claim_languages(self):
        old_body = """## Claim
### Formal Claim
```CFEL
# model
Node >| Container: yes;
Node >| Container: no
```
"""
        python = ('from caprmedio.formal_claims import declare_entity\n'
                  'declare_entity(entity_name="Node", allowed_classification_values={"Container": ("yes", "no")})\n')
        new_body = re.sub(r'```CFEL\n.*?```', '```python\n' + python + '```', old_body, count=1, flags=re.S)
        self.assertNotEqual(new_body, old_body)
        row = {'source': {'atom_id': 'CA-R-2484', 'version': 2, 'path': 'R2484.md', 'sha256': 'a'*64},
               'subjects': {'active': 'CAPRMEDIO_MODEL <+ Node >| Container', 'passive': []},
               'read_view': {'content_role': 'Requirement', 'type': 'Rule'}, 'body': old_body}
        changed = deepcopy(row)
        changed['body'] = new_body
        old, old_errors = extract_claim_constraints(row)
        new, new_errors = extract_claim_constraints(changed)
        self.assertEqual(old_errors, [])
        self.assertEqual(new_errors, [])
        self.assertEqual([(r['kind'], r.get('subject_selector'), r.get('axis'), r.get('value')) for r in new],
                         [('classification_allowed_value', 'Node', 'Container', 'yes'),
                          ('classification_allowed_value', 'Node', 'Container', 'no')])
        self.assertEqual(old, new)
        old_graph, _ = compose_enhanced_current_graph([row])
        new_graph, _ = compose_enhanced_current_graph([changed])
        self.assertEqual(old_graph["nodes"], new_graph["nodes"])
        self.assertEqual(old_graph["edges"], new_graph["edges"])
        self.assertFalse(any(r.get('kind') == 'classification_condition' for r in new_graph['constraints']))
        self.assertEqual({r['value'] for r in new_graph['constraints'] if r['kind'] == 'classification_allowed_value'}, {'yes', 'no'})
        graph, provenance = compose_enhanced_current_graph([changed])
        rendered = render_model(graph, provenance, updated_at='2026-11-13 00:00:00 +0000',
                                source_selection='Fixture', projection_identity={'projection_id': 'CA-PROJ-901', 'named_selection': 'Current'})
        self.assertIn('Node >| Container: yes', rendered)
        self.assertIn('Node >| Container: no', rendered)
        from FEATURE_WORKBENCH_BACKEND.relation_registry import compile_relation_registry
        def wb(body):
            return {'id':'CA-R-2484','ref':'CA-R-2484','version':2,'source_path':'R2484.md',
                    'status_group':'Current','role':'Requirement','form':'Rule',
                    '_content_bytes':body.encode(),'content_markdown':body}
        self.assertEqual(compile_relation_registry([wb(old_body)]), compile_relation_registry([wb(new_body)]))


if __name__ == '__main__':
    unittest.main()
