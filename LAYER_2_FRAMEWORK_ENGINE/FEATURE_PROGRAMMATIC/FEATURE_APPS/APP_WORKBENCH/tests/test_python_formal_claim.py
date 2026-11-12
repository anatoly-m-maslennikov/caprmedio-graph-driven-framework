"""Parity for Python Formal Claims at the shared compiler entry point."""

from pathlib import Path
import sys
import unittest


PROGRAMMATIC = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(PROGRAMMATIC / 'FEATURE_TOOLS'), str(PROGRAMMATIC / 'FEATURE_APPS')]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.content_schema import compile_content_schema
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.declaration_cfel import formal_claim_blocks
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relation_registry import compile_relation_registry


def declaration(language, claim):
    body = f'## Claim\n\n### Formal Claim\n\n```{language}\n{claim}\n```\n'
    return {'id': 'CA-R-2500', 'ref': 'CA-R-2500', 'version': 6, 'source_path': 'claim.md',
            'role': 'Requirement', 'form': 'Declaration', 'status_group': 'Current',
            '_content_bytes': body.encode()}


class PythonFormalClaimTest(unittest.TestCase):
    def test_content_schema_keeps_constraints_and_source(self):
        prefix = 'Atom/(.Header.Context.Role in RMED).Content.Claim'
        cfel = (f'{prefix}{{::1}}:: []{{::0}};\n'
                f'{prefix}.*[string, in (Formal Claim, Prose Claim)]{{::1..2}};')
        python = (f'property_rule(address={prefix!r}, value_format="", occurrences="1", values="0")\n'
                  f'allowed_children(address={prefix!r}, names=("Formal Claim", "Prose Claim"), '
                  'occurrences="1..2", name_format="string")')
        baseline = compile_content_schema([declaration('CFEL', cfel)])
        self.assertTrue(baseline.rules)
        self.assertEqual(baseline, compile_content_schema([declaration('python', python)]))

    def test_relation_inverse_is_visible_to_registry(self):
        cfel = 'Relation//PRECEDES ((HAS_INVERSE)) Relation//FOLLOWS'
        python = 'relation(source="Relation//PRECEDES", name="HAS_INVERSE", target="Relation//FOLLOWS")'
        baseline = compile_relation_registry([declaration('CFEL', cfel)])
        self.assertEqual(baseline.inverse, {'PRECEDES': 'FOLLOWS'})
        self.assertEqual(baseline, compile_relation_registry([declaration('python', python)]))

    def test_python_example_in_prose_is_not_a_model_claim(self):
        self.assertEqual((), formal_claim_blocks('## Claim\n### Prose Claim\n```python\nprint(1)\n```\n'))
