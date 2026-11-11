"""Formal Status placement uses numbered directories and Current source selection."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE.candidate_schema import compile_candidate_schema, load_candidate_schema  # noqa: E402


def statement(status, template, *, plan=False):
    role = '(.Header.Context.Role := Plan)/' if plan else ''
    return f'Atom/{role}(.Header.State.Status := {status}).Header.Destination.File.Path == PATH_TEMPLATE("{template}");'


class NumberedStatusTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'CA-R-481.md').write_text('''---
atom_id: CA-R-481
role: Requirement
form: Declaration
status: Active
version: 1
---
## Claim
### Formal Claim
```CFEL
Atom.Header.Context.Role :: Plan;
Atom.Header.Form :: Plan;
Atom.Header.ID:: [atom id]{::1};
Atom.Content.Summary:: {::1};
Atom/(.Header.Context.Role := Plan) >| (Role Order Number == 3);
```
''')

    def delivery(self, atom_id, subject, claim, *, directory=None):
        path = (directory or self.root) / f'{atom_id}.md'
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f'---\natom_id: {atom_id}\nrole: Delivery\nform: File Layout\nstatus: Active\nversion: 1\n'
                        f'topics:\n  main_subject: {json.dumps(subject)}\n---\n'
                        f'## Claim\n### Formal Claim\n```CFEL\n{claim}\n```\n')

    def test_exact_numbered_status_rules_and_current_source_boundary(self):
        self.delivery('CA-D-1001', 'CAPRMEDIO_MODEL <+ Carrier',
                      'Atom.Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/<role folder>/<placement>");')
        prefix = 'CAPRMEDIO_MODEL <+ Atom.Header.State.Status >| Status Group := '
        self.delivery('CA-D-1002', prefix + 'Draft', statement('Draft', '<owning scope unit>/<role folder>/000_draft'))
        self.delivery('CA-D-1003', prefix + 'Archived', statement('Archived', '<owning scope unit>/<role folder>/099_archived'))
        self.delivery('CA-D-1004', prefix + 'Current', '\n'.join([
            statement('Active', '<container>'), statement('Done', '<container>/020_done'),
            statement('Resolved', '<container>/021_resolved'), statement('Canceled', '<container>/040_canceled')]))
        self.delivery('CA-D-1005',
                      'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.State.Status >| Status Group := Backlog',
                      statement('Backlog', '<owning scope unit>/<role folder>/001_backlog', plan=True))
        # A copied carrier can still say Active, but its revision folder excludes it.
        self.delivery('CA-D-1006', prefix + 'Draft', statement('Draft', '<owning scope unit>/<role folder>/wrong'),
                      directory=self.root / '000_draft')
        self.delivery('CA-D-1007', prefix + 'Archived', statement('Archived', '<owning scope unit>/<role folder>/wrong'),
                      directory=self.root / '099_archived')
        asset = self.root.parent / (self.root.name + '-status.json')
        self.addCleanup(asset.unlink, missing_ok=True)
        asset.write_bytes(compile_candidate_schema(self.root))
        rules = load_candidate_schema(asset).placement
        for status, expected in {'Draft': ('role', '000_draft'), 'Backlog': ('role', '001_backlog'),
                                 'Active': ('container', ''), 'Done': ('container', '020_done'),
                                 'Resolved': ('container', '021_resolved'), 'Canceled': ('container', '040_canceled'),
                                 'Archived': ('role', '099_archived')}.items():
            with self.subTest(status=status):
                self.assertEqual(expected, rules.placement('Plan', status))
        with self.assertRaises(ValueError):
            rules.placement('Plan', 'Unknown')
        self.assertEqual({'CA-D-1001', 'CA-D-1002', 'CA-D-1003', 'CA-D-1004', 'CA-D-1005', 'CA-R-481'},
                         {pin['atom_id'] for pin in rules.sources})


if __name__ == '__main__':
    unittest.main()
