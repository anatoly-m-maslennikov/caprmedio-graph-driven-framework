"""Typed Aspect hierarchy preserves independently authored facts."""
from pathlib import Path
import sys
import unittest

PROGRAMMATIC = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(PROGRAMMATIC), str(PROGRAMMATIC / 'FEATURE_TOOLS')]
from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import parse_native_model_claim
from FEATURE_FORMAL_MODEL_ENGINE.compiler_claim import compiler_model_statements


class AspectHierarchyTests(unittest.TestCase):
    def test_independent_collections_and_malformed_inputs(self):
        a = 'PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering'
        b = 'PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Product'
        claim = ('from caprmedio.formal_claims import declare_entity\n'
                 f'declare_entity(entity_name="Project Structure", structure_paths=({a!r},), aspect_memberships=({b!r},))')
        parsed = parse_native_model_claim(claim)
        self.assertEqual((a, f'({b}) ((INSTANCE_OF)) Aspect'), compiler_model_statements(parsed))
        for value in (None, 1, 'Node', (), ('Node',), ([],), (a, a), ('Atom <+ Aspects <+ X',)):
            bad = {'kind': 'entity', 'arguments': {'entity_name': 'Project Structure', 'structure_paths': value, 'aspect_memberships': ()}}
            if value == ():
                continue
            with self.subTest(value=value), self.assertRaises(ValueError):
                compiler_model_statements(bad)
        for bad in (claim.replace(repr(a), '"Node"'), claim.replace(repr(b), '["x"]'),
                    claim.replace(repr(b) + ',', repr(b) + ',' + repr(b) + ',')):
            with self.assertRaises(ValueError):
                parse_native_model_claim(bad)

if __name__ == '__main__':
    unittest.main()
