from pathlib import Path
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from ATOM_LIFECYCLE.candidate_schema import CandidateSchema  # noqa: E402
from ATOM_LIFECYCLE.carrier import effective_header, logical_view, render_carrier  # noqa: E402
from ATOM_LIFECYCLE.common import InputError, logical_container  # noqa: E402
from ATOM_LIFECYCLE.content_constraints import ContentConstraints  # noqa: E402
from ATOM_LIFECYCLE.header_constraints import HeaderConstraints  # noqa: E402
from ATOM_LIFECYCLE.role_form_schema import RoleFormSchema  # noqa: E402
from ATOM_LIFECYCLE.status_model import StatusModel  # noqa: E402
from ATOM_LIFECYCLE.validation import validate_candidate  # noqa: E402
from FEATURE_WORKBENCH_BACKEND.content_schema import ContentSchema  # noqa: E402
from FEATURE_WORKBENCH_BACKEND.header_columns import HeaderColumn, HeaderSchema  # noqa: E402
from FEATURE_WORKBENCH_BACKEND.workbench_schema_asset import SchemaCompilation  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier  # noqa: E402
from header_groups import header_value  # noqa: E402
from project_selection import resolve_project  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402


class LifecycleRootContainerTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name).resolve()
        self.control = self.root / '.caprmedio_test'
        self.control.mkdir()
        (self.control / 'caprmedio_project_settings.toml').write_text(
            '[project]\nname="TEST"\n[artifacts.identity]\nproject_prefix="CA"\n'
            '[paths]\ncontrol_root=".caprmedio_test"\n', encoding='utf-8',
        )
        rows = write_scope_unit_declarations(self.root, rows=({'scope_unit_name': 'CHILD'},),
                                             control_root=self.control)
        self.root_carrier = rows['TEST']['declaration_path']
        self.child_carrier = rows['CHILD']['declaration_path']
        self.root_body = parse_carrier(self.root_carrier.read_bytes(), self.root_carrier).body
        self.fields = {
            'atom_id': rows['TEST']['atom_id'], 'ref_id': rows['TEST']['atom_id'], 'role': 'Requirement',
            'form': 'Scope Unit Declaration', 'status': 'Active', 'version': 1,
            'updated_at': '2026-01-01T00:00:00+00:00',
        }
        header = HeaderSchema((HeaderColumn(
            ('context', 'container', 'scope_unit'), 'header.context.container.scope_unit', 'VARCHAR', True,
            reader='container.scope_unit',
        ),))
        rules = HeaderConstraints(
            (('container', '', '', '1', 'CA-R-2779'),), (),
            (('context', '', '', (3, 3, 'container', 'form', 'role'), 'CA-R-3070'),),
        )
        forms = RoleFormSchema(frozenset({'Requirement'}), frozenset({'Scope Unit Declaration', 'Declaration'}),
                               frozenset(), ())
        schema = CandidateSchema(SchemaCompilation(header, header, ContentSchema((), (), ())), forms, rules,
                                 ContentConstraints(()))
        self.model = StatusModel(((None, None, 'Active'),), candidate_schema=schema)

    def pin_root(self, extra_fields=None):
        raw = render_carrier(None, self.fields | (extra_fields or {}), body=self.root_body)
        self.root_carrier.write_bytes(raw)
        return resolve_project(self.root), raw

    def test_selected_root_omission_passes_logical_and_schema_checks_without_persisting_default(self):
        selection, raw = self.pin_root()
        parsed = parse_carrier(raw, self.root_carrier)
        effective = effective_header(selection, parsed.metadata, raw, self.root_carrier)
        self.assertEqual({'scope_unit': 'CA-SU--1'}, logical_container({}, logical_view(effective, self.model)))
        validate_candidate(selection, self.model, raw, self.root_carrier)
        self.assertEqual((False, None), header_value(parsed.metadata, 'container'))
        self.assertEqual(raw, self.root_carrier.read_bytes())

    def test_explicit_root_container_overrides_default_and_malformed_values_are_rejected(self):
        for container in ({'scope_unit': 'CA-SU--1'}, {'scope_unit': 'TEST-SU-1'}, {'atom': 'CA-R-1'}):
            with self.subTest(container=container):
                selection, raw = self.pin_root({'container': container})
                parsed = parse_carrier(raw, self.root_carrier)
                effective = effective_header(selection, parsed.metadata, raw, self.root_carrier)
                self.assertIs(parsed.metadata, effective)
                self.assertEqual(container, logical_container({}, logical_view(effective, self.model)))
                validate_candidate(selection, self.model, raw, self.root_carrier)
        for malformed in (None, {}, {'scope_unit': ''}, {'scope_unit': 'CA-SU--1', 'atom': 'CA-R-1'},
                          {'scope_unit': 'CA-SU--1', 'extra': 'value'}):
            with self.subTest(malformed=malformed):
                selection, raw = self.pin_root({'container': malformed})
                with self.assertRaisesRegex(InputError, 'Supply one Scope Unit or containing Atom'):
                    validate_candidate(selection, self.model, raw, self.root_carrier, authored=False)

    def test_default_requires_exact_selected_root_carrier(self):
        selection, raw = self.pin_root()
        cases = (
            (self.root_carrier, raw + b'\n'),
            (self.root_carrier.with_name('CA-R-990000-copy.md'), raw),
            (self.child_carrier, render_carrier(self.child_carrier.read_bytes(), {'ref_id': 'CA-R-990001'})),
            (self.control / '04_requirement/CA-R-4-ordinary.md',
             render_carrier(None, self.fields | {
                 'atom_id': 'CA-R-4', 'ref_id': 'CA-R-4', 'form': 'Declaration', 'current_scope_unit': 'TEST',
             }, body='## Summary\n\nOrdinary\n')),
        )
        for path, carrier in cases:
            with self.subTest(path=path), self.assertRaisesRegex(InputError, 'Supply one Scope Unit or containing Atom'):
                validate_candidate(selection, self.model, carrier, path)


if __name__ == '__main__':
    unittest.main()
