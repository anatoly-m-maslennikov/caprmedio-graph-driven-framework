"""Status order declarations and Delivery templates compile into placement."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE.candidate_schema import compile_candidate_schema, load_candidate_schema  # noqa: E402


def status_order(name, number):
    return f'Atom/(.Header.State.Status := {name}).Header.State.Status >| (Status Order Number == {number});'


def status_path(name, path, *, plan=False):
    role = '(.Header.Context.Role := Plan)/' if plan else ''
    return f'Atom/{role}(.Header.State.Status := {name}).Header.Destination.File.Path == PATH_TEMPLATE("{path}");'


class StatusOrderPlacementTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.orders = {'Draft': 7, 'Active': 12, 'Backlog': 14, 'Done': 31, 'Archived': 115}
        self.write_requirements()
        self.delivery('CA-D-881', 'CAPRMEDIO_MODEL <+ Carrier',
                      'Atom.Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/<role folder>/<placement>");')
        prefix = 'CAPRMEDIO_MODEL <+ Atom.Header.State.Status >| Status Group := '
        self.delivery('CA-D-882', prefix + 'Draft', status_path('Draft', '<owning scope unit>/<role folder>/<status folder>'))
        self.delivery('CA-D-883', prefix + 'Archived', status_path('Archived', '<owning scope unit>/<role folder>/<status folder>'))
        self.delivery('CA-D-884', prefix + 'Current', '\n'.join([
            'Atom/(.Header.State.Status >| Status Group = Current).Header.Destination.File.Path == PATH_TEMPLATE("<container>/<status folder>");',
            status_path('Active', '<container>')]))
        self.delivery('CA-D-885',
                      'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.State.Status >| Status Group := Backlog',
                      status_path('Backlog', '<owning scope unit>/<role folder>/<status folder>', plan=True))

    def write_requirements(self, orders=None):
        orders = self.orders if orders is None else orders
        statements = ['Atom.Header.Context.Role :: Plan;', 'Atom.Header.Form :: Plan;',
                      'Atom.Header.ID:: [atom id]{::1};', 'Atom.Content.Summary:: {::1};',
                      'Atom/(.Header.Context.Role := Plan) >| (Role Order Number == 3);']
        statements.extend(f'Atom.Header.State.Status :: {name};' for name in ('Draft', 'Active', 'Done', 'Archived'))
        statements.append('Atom/(.Header.Context.Role in (Plan)).Header.State.Status :: Backlog;')
        statements.extend(status_order(name, number) for name, number in orders.items())
        (self.root / 'CA-R-71591.md').write_text(
            '---\natom_id: CA-R-71591\nrole: Requirement\nform: Declaration\nstatus: Active\nversion: 4\n---\n'
            '## Claim\n### Formal Claim\n```CFEL\n' + '\n'.join(statements) + '\n```\n')

    def delivery(self, atom_id, subject, claim):
        (self.root / f'{atom_id}.md').write_text(
            f'---\natom_id: {atom_id}\nrole: Delivery\nform: File Layout\nstatus: Active\nversion: 2\n'
            f'topics:\n  main_subject: {json.dumps(subject)}\n---\n'
            f'## Claim\n### Formal Claim\n```CFEL\n{claim}\n```\n')

    def compile(self):
        asset = self.root.parent / (self.root.name + '-status-order.json')
        self.addCleanup(asset.unlink, missing_ok=True)
        asset.write_bytes(compile_candidate_schema(self.root))
        return load_candidate_schema(asset).placement

    def test_order_numbers_derive_role_and_container_folders(self):
        rules = self.compile()
        for status, expected in {'Draft': ('role', '007_draft'), 'Backlog': ('role', '014_backlog'),
                                 'Active': ('container', ''), 'Done': ('container', '031_done'),
                                 'Archived': ('role', '115_archived')}.items():
            with self.subTest(status=status):
                self.assertEqual(expected, rules.placement('Plan', status))
        self.assertIn('CA-R-71591', {pin['atom_id'] for pin in rules.sources})

    def test_missing_or_duplicate_status_number_fails(self):
        for orders in [{key: value for key, value in self.orders.items() if key != 'Backlog'},
                       {**self.orders, 'Done': self.orders['Draft']}]:
            with self.subTest(orders=orders):
                self.write_requirements(orders)
                with self.assertRaises(ValueError):
                    self.compile()


if __name__ == '__main__':
    unittest.main()
