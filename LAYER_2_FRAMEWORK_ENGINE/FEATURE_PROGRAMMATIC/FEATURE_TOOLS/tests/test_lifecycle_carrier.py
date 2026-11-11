from pathlib import Path
import sys
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE.carrier import render_carrier  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier  # noqa: E402


def metadata(raw):
    return parse_carrier(raw, Path('test.md')).metadata


class CarrierTest(unittest.TestCase):
    def test_flat_aliases_and_unrelated_data(self):
        raw = b'---\nrole: Method\ncontent_role: Method\nstatus: Draft\nextra:\n  nested: [1, 2]\n---\n\nBody\n'
        result = render_carrier(raw, {'role': 'Plan'})
        self.assertEqual(metadata(result), {'role': 'Plan', 'content_role': 'Plan', 'status': 'Draft', 'extra': {'nested': [1, 2]}})
        self.assertTrue(result.endswith(b'\nBody\n'))

    def test_grouped_and_destination_aliases(self):
        raw = b'---\nidentity:\n  id: CA-R-1\nstate:\n  status: Draft\ndestination:\n  path: old\ncarrier_destination:\n  path: old\n---\nbody\n'
        data = metadata(render_carrier(raw, {'status': 'Active', 'destination.path': 'new'}))
        self.assertEqual(data['identity'], {'id': 'CA-R-1'})
        self.assertEqual(data['state'], {'status': 'Active'})
        self.assertEqual(data['destination'], {'path': 'new'})
        self.assertEqual(data['carrier_destination'], {'path': 'new'})

    def test_crlf_body_and_omitted_fields(self):
        raw = b'---\r\nstatus: Draft\r\n---\r\n\r\nText\r\n\xff'
        # Non-UTF-8 is rejected even when body is untouched.
        with self.assertRaises(ValueError):
            render_carrier(raw, {'status': 'Active'})
        raw = raw[:-1] + 'ñ'.encode()
        self.assertTrue(render_carrier(raw, {'status': 'Active'}).endswith(b'\r\nText\r\n' + 'ñ'.encode()))
        self.assertEqual(render_carrier(raw, {}), raw)
        self.assertTrue(render_carrier(raw, {}, body='literal\n').endswith(b'---\r\nliteral\n'))

    def test_new_grouped_header_and_literal_body(self):
        result = render_carrier(None, {'atom_id': 'CA-P-1', 'role': 'Plan', 'status': 'Draft', 'work_sequence_number': 2}, body='\nNew\n')
        data = metadata(result)
        self.assertEqual(data['identity']['atom_id'], 'CA-P-1')
        self.assertEqual(data['context']['plan']['work_sequence_number'], 2)
        self.assertEqual(data['state']['status'], 'Draft')
        self.assertTrue(result.endswith(b'---\n\nNew\n'))

    def test_conflicts_and_non_mapping_parents_fail(self):
        with self.assertRaises(ValueError):
            render_carrier(b'---\nrole: Plan\ncontent_role: Method\n---\n', {'role': 'Plan'})
        with self.assertRaises(ValueError):
            render_carrier(b'---\nextra: text\n---\n', {'extra.child': 2})
        with self.assertRaises(ValueError):
            render_carrier(b'---\nstatus: Draft\n---\n', {'status': 'Active', 'state.status': 'Draft'})


if __name__ == '__main__':
    unittest.main()
