"""Relation cardinalities accept declared single and double colon notation."""
from pathlib import Path
import sys, unittest
TOOL = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOL.parent.parent), str(TOOL.parent), str(TOOL)]
from cfel_claim_constraints import extract_claim_constraints

class RelationCardinalityTests(unittest.TestCase):
    def test_both_spellings_preserve_endpoints_and_bounds(self):
        for colon in (':', '::'):
            expression = f'View {{{colon}1}}((IS_CONTAINED_BY)){{{colon}1+}} Workspace'
            carrier = {'source': {'atom_id':'CA-R-1','version':1,'path':'fixture.md','sha256':'a'*64},
                       'body': f'## Claim\n### Formal Claim\n```CFEL\n# model\n{expression}\n```\n',
                       'read_view': {'content_role':'Requirement'}}
            rows, diagnostics = extract_claim_constraints(carrier)
            self.assertEqual([], diagnostics)
            self.assertEqual(1, len(rows))
            row = rows[0]
            self.assertEqual(('View', 'IS_CONTAINED_BY', 'Workspace', {'minimum':1,'maximum':1}, {'minimum':1,'maximum':None}),
                             tuple(row[k] for k in ('source_selector','relation','target_selector','source_cardinality','target_cardinality')))

if __name__ == '__main__': unittest.main()
