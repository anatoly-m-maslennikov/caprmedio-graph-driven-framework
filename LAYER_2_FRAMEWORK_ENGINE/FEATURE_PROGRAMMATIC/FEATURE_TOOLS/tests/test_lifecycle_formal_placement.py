"""Formal Delivery claims alone determine the compiled placement policy."""
from pathlib import Path
import json
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE.candidate_schema import compile_candidate_schema, load_candidate_schema  # noqa: E402
from ATOM_LIFECYCLE.placement_model import active_placement  # noqa: E402


def carrier(atom_id, role, status, body, subject=None):
    topics = f'topics:\n  main_subject: {json.dumps(subject)}\n' if subject else ''
    return (f'---\natom_id: {atom_id}\nrole: {role}\nform: Declaration\n'
            f'status: {status}\nversion: 1\n{topics}---\n{body}\n')


RULES = '''Atom/(.Header.Context.Role := Concern).Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/01_concern/<placement>");
Atom/(.Header.Context.Role := Plan).Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/03_plan/<placement>");
Atom/(.Header.State.Status := Draft).Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/<role folder>/draft");
Atom/(.Header.State.Status := Archived).Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/<role folder>/archived");
Atom/(.Header.State.Status >| Status Group = Current).Header.Destination.File.Path == PATH_TEMPLATE("<container>/<lowercase status>");
Atom/(.Header.State.Status := Active).Header.Destination.File.Path == PATH_TEMPLATE("<container>");
Atom/(.Header.Context.Role := Plan)/(.Header.State.Status := Backlog).Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/<role folder>/Backlog");'''


class FormalPlacementTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'CA-R-1.md').write_text(carrier('CA-R-1', 'Requirement', 'Active', '''## Claim
### Formal Claim
```CFEL
Atom.Header.Role :: Plan;
Atom.Header.Form :: Plan;
Atom.Header.ID:: [atom id]{::1};
Atom.Content.Summary:: {::1};
```
'''))

    def delivery(self, rules=RULES, atom_id='CA-D-747', subject='CAPRMEDIO_MODEL <+ Carrier', status='Active'):
        (self.root / f'{atom_id}.md').write_text(carrier(atom_id, 'Delivery', status,
            '## Claim\n### Prose Claim\n```CFEL\n' + RULES.splitlines()[0].replace('01_concern', '99_prose') + '\n```\n### Formal Claim\n```CFEL\n' + rules + '\n```', subject))

    def compile(self):
        output = self.root.parent / (self.root.name + '-schema.json')
        self.addCleanup(output.unlink, missing_ok=True)
        output.write_bytes(compile_candidate_schema(self.root))
        return load_candidate_schema(output)

    def test_formal_rules_compile_and_ignore_prose_comments_and_archived(self):
        lines = RULES.replace('01_concern', '77_issues').splitlines()
        self.delivery('\n'.join(lines[:2]) + '\n# ' + RULES.splitlines()[0], 'CA-D-747',
                      'CAPRMEDIO_MODEL <+ Atom.Header.Context.Role')
        self.delivery('\n'.join(lines[2:6]), 'CA-D-9123', 'CAPRMEDIO_MODEL <+ Atom.Header.State.Status')
        self.delivery(lines[6], 'CA-D-98236', 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.State.Status >| Status Group := Backlog')
        self.delivery(lines[6], 'CA-D-8890', 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.State.Status >| Status Group := Other')
        self.delivery(RULES, 'CA-D-8888', 'CAPRMEDIO_MODEL <+ Unrelated')
        self.delivery(RULES, 'CA-D-8889', 'CAPRMEDIO_MODEL <+ Carrier <+ Unrelated')
        (self.root / 'CA-D-2.md').write_text(carrier('CA-D-2', 'Delivery', 'Archived',
            '## Claim\n### Formal Claim\n```CFEL\n' + RULES + '\n```'))
        (self.root / 'CA-D-3.md').write_text(carrier('CA-D-3', 'Delivery', 'Draft',
            '## Claim\n### Formal Claim\n```CFEL\n' + RULES + '\n```'))
        schema = self.compile()
        rules = schema.placement
        self.assertEqual('77_issues', rules.role_folder('Concern'))
        self.assertEqual(('container', ''), rules.placement('Plan', 'Active'))
        self.assertEqual(('role', 'Backlog'), rules.placement('Plan', 'Backlog'))
        self.assertEqual(('container', 'resolved'), rules.placement('Concern', 'Resolved'))
        self.assertEqual(('role', 'draft'), rules.placement('Plan', 'Draft'))
        self.assertEqual(('role', 'archived'), rules.placement('Plan', 'Archived'))
        self.assertEqual({'CA-D-747', 'CA-D-9123', 'CA-D-98236'},
                         {row['atom_id'] for row in rules.sources})

    def test_duplicate_formal_binding_fails(self):
        self.delivery(RULES + '\n' + RULES.splitlines()[0])
        with self.assertRaisesRegex(ValueError, '[Dd]uplicate'):
            self.compile()

    def test_missing_placement_cannot_be_used_as_a_model(self):
        self.assertIsNone(self.compile().placement)
        with self.assertRaisesRegex(ValueError, 'not bound'):
            active_placement()


if __name__ == '__main__':
    unittest.main()
