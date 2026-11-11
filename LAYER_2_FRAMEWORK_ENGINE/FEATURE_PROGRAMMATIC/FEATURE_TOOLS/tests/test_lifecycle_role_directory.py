"""Compiled Role directories derive only from adopted order declarations."""
from pathlib import Path
import json
import tempfile
import sys
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from role_directory_rules import compile_role_folders  # noqa: E402
from ATOM_LIFECYCLE.candidate_schema import compile_candidate_schema, load_candidate_schema  # noqa: E402


def order(role, number):
    return f'Atom/(.Header.Context.Role := {role}) >| (Role Order Number == {number})'


class RoleDirectoryTests(unittest.TestCase):
    def test_source_order_controls_encoding_and_keeps_gaps(self):
        records = [(order('Concern', 4), 'CA-R-887@3'),
                   (order('"Analysis and Advisory"', 2), 'CA-R-90@7'),
                   (order('Operations', 9), 'CA-R-654321@2'),
                   (order('Plan', 13), 'CA-R-5001@1')]
        result = compile_role_folders(records)
        self.assertEqual(('04_concern', 'CA-R-887@3'), result['Concern'])
        self.assertEqual(('02_analysis_and_advisory', 'CA-R-90@7'), result['Analysis and Advisory'])
        self.assertEqual(('09_operations', 'CA-R-654321@2'), result['Operations'])
        self.assertEqual(('13_plan', 'CA-R-5001@1'), result['Plan'])
        self.assertFalse(any(folder.startswith('08_') for folder, _ in result.values()))

    def test_duplicate_and_malformed_order_claims_fail(self):
        for records in [
            [(order('Concern', 1), 'A'), (order('Concern', 2), 'B')],
            [(order('Concern', 1), 'A'), (order('Plan', 1), 'B')],
            [(order('Concern', 'not_a_number'), 'A')],
            [('Atom/(.Header.Context.Role := Concern) >| (Role Order Number = 1)', 'A')],
        ]:
            with self.subTest(records=records), self.assertRaises(ValueError):
                compile_role_folders(records)


class RoleDirectorySourceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.orders = [order('Concern', 4), order('"Analysis and Advisory"', 2),
                       order('Operations', 9), order('Plan', 13)]
        self.generic = 'Atom.Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/<role folder>/<placement>");'
        self.status = '''Atom/(.Header.State.Status := Draft).Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/<role folder>/draft");
Atom/(.Header.State.Status := Archived).Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/<role folder>/archived");
Atom/(.Header.State.Status >| Status Group = Current).Header.Destination.File.Path == PATH_TEMPLATE("<container>/<lowercase status>");
Atom/(.Header.State.Status := Active).Header.Destination.File.Path == PATH_TEMPLATE("<container>");'''

    def write_sources(self, *, orders=None, generic=True):
        declarations = ['Atom.Header.Context.Role :: Concern;',
                        'Atom.Header.Context.Role :: "Analysis and Advisory";',
                        'Atom.Header.Context.Role :: Operations;', 'Atom.Header.Context.Role :: Plan;',
                        'Atom.Header.Form :: Plan;', 'Atom.Header.ID:: [atom id]{::1};',
                        'Atom.Content.Summary:: {::1};']
        statements = self.orders if orders is None else orders
        body = '\n'.join(declarations + [statement + ';' for statement in statements])
        (self.root / 'CA-R-7001.md').write_text(
            '---\natom_id: CA-R-7001\nrole: Requirement\nform: Declaration\nstatus: Active\nversion: 3\n---\n'
            '## Claim\n### Formal Claim\n```CFEL\n' + body + '\n```\n')
        (self.root / 'CA-D-7913.md').write_text(
            '---\natom_id: CA-D-7913\nrole: Delivery\nform: File Layout\nstatus: Active\nversion: 2\n'
            'topics:\n  main_subject: CAPRMEDIO_MODEL <+ Carrier\n---\n'
            '## Claim\n### Formal Claim\n```CFEL\n' + (self.generic if generic else '') + '\n' + self.status + '\n```\n')

    def test_generic_delivery_and_role_orders_compile_from_arbitrary_pins(self):
        self.write_sources()
        payload = json.loads(compile_candidate_schema(self.root))
        asset = self.root.parent / (self.root.name + '-role-schema.json')
        self.addCleanup(asset.unlink, missing_ok=True)
        asset.write_text(json.dumps(payload))
        rules = load_candidate_schema(asset).placement
        self.assertEqual('04_concern', rules.role_folder('Concern'))
        self.assertEqual('02_analysis_and_advisory', rules.role_folder('Analysis and Advisory'))
        self.assertEqual('09_operations', rules.role_folder('Operations'))
        self.assertEqual('13_plan', rules.role_folder('Plan'))
        with self.assertRaises(ValueError):
            rules.role_folder('Delivery')
        self.assertFalse(any(folder.startswith('08_') for folder in rules.role_folders.values()))
        self.assertEqual({('CA-R-7001', 3), ('CA-D-7913', 2)},
                         {(pin['atom_id'], pin['version']) for pin in rules.sources})

    def test_missing_role_order_or_generic_delivery_fails(self):
        for orders, generic in [(self.orders[:-1], True), (self.orders, False)]:
            with self.subTest(orders=orders, generic=generic):
                self.write_sources(orders=orders, generic=generic)
                with self.assertRaises(ValueError):
                    compile_candidate_schema(self.root)


if __name__ == '__main__':
    unittest.main()
