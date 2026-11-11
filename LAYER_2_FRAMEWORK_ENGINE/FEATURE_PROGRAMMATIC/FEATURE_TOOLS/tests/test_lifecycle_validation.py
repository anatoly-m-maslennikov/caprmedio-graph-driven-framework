from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import sys
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE.carrier import render_carrier  # noqa: E402
from ATOM_LIFECYCLE.common import InputError  # noqa: E402
from ATOM_LIFECYCLE.status_model import StatusModel  # noqa: E402
from ATOM_LIFECYCLE.validation import validate_candidate  # noqa: E402


class CandidateValidationTests(unittest.TestCase):
    def test_work_report_resolves_done_plan_in_disposable_project(self):
        import tempfile
        from lifecycle_placement_test_support import bind_placement, fixture_rules
        from project_selection import resolve_project
        from scope_declaration_test_support import write_scope_unit_declarations

        with tempfile.TemporaryDirectory() as directory, bind_placement(fixture_rules()):
            root = Path(directory).resolve()
            control = root / '.caprmedio_test'
            control.mkdir()
            (control / 'caprmedio_project_settings.toml').write_text(
                '[project]\nname="TEST"\n[artifacts.identity]\nproject_prefix="CA"\n'
                '[paths]\ncontrol_root=".caprmedio_test"\n')
            write_scope_unit_declarations(root, control_root=control, rows=[])
            selection = resolve_project(root)
            target = control / '03_plan/done/CA-P-1-TASK--same-work.md'
            target.parent.mkdir(parents=True)
            fields = {'atom_id': 'CA-P-1', 'ref_id': 'CA-P-1', 'role': 'Plan', 'form': 'Plan',
                      'status': 'Done', 'version': 1, 'updated_at': '2026-01-01T00:00:00+00:00',
                      'container.scope_unit': 'TEST'}
            target.write_bytes(render_carrier(None, fields, body='## Summary\n\nSame work\n'))
            report = fields | {'atom_id': 'CA-P-2', 'ref_id': 'CA-P-2', 'form': 'Work Report',
                               'relations': {'IS_WORK_REPORT_FOR': ['CA-P-1']}}
            model = StatusModel(((None, None, 'Done'),))
            validate_candidate(selection, model, render_carrier(None, report, body='## Summary\n\nSame work\n'),
                               control / '03_plan/done/CA-P-2-WORK_REPORT--same-work.md')

    def test_authored_work_report_requires_one_matching_current_plan(self):
        from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier

        selection = SimpleNamespace(settings={'artifacts': {'identity': {'project_prefix': 'CA'}}})
        model = StatusModel(((None, None, 'Active'), ('Plan', None, 'Done'), (None, None, 'Archived')))
        target_fields = {'atom_id': 'CA-P-1', 'ref_id': 'CA-P-1', 'role': 'Plan', 'form': 'Plan',
                         'status': 'Done', 'version': 1, 'updated_at': '2026-01-01T00:00:00+00:00',
                         'container.scope_unit': 'CA-SU-1'}
        target_raw = render_carrier(None, target_fields, body='## Summary\n\nSame work\n')
        target = SimpleNamespace(status='done', raw=target_raw, path=Path('plan.md'),
                                 metadata=parse_carrier(target_raw, Path('plan.md')).metadata)
        fields = target_fields | {'atom_id': 'CA-P-2', 'ref_id': 'CA-P-2', 'form': 'Work Report',
                                  'relations': {'IS_WORK_REPORT_FOR': ['CA-P-1']}}
        def check(values, body='## Summary\n\nSame work\n', **kwargs):
            validate_candidate(selection, model, render_carrier(None, values, body=body), Path('report.md'), **kwargs)

        with patch('ATOM_LIFECYCLE.validation.select_source', return_value=target) as select:
            check(fields)
            check(fields | {'relations': {'is_work_report_for': ['CA-P-1']}})
            self.assertEqual(select.call_args.args[1], 'CA-P-1')
            invalid_relations = ({}, {'IS_WORK_REPORT_FOR': []}, {'IS_WORK_REPORT_FOR': ['CA-P-1@1']},
                                 {'IS_WORK_REPORT_FOR': ['CA-P-2']}, {'IS_WORK_REPORT_FOR': ['CA-P-1', 'CA-P-3']},
                                 {'IS_WORK_REPORT_FOR': ['CA-P-1'], 'is_work_report_for': ['CA-P-3']})
            for relations in invalid_relations:
                with self.subTest(relations=relations), self.assertRaises(InputError):
                    check(fields | {'relations': relations})
            with self.assertRaisesRegex(InputError, 'same Summary'):
                check(fields, body='## Summary\n\nOther work\n')
            with self.assertRaisesRegex(InputError, 'same Container'):
                check(fields | {'container.scope_unit': 'CA-SU-2'})
            with self.assertRaisesRegex(InputError, 'Plan Role'):
                check(fields | {'atom_id': 'CA-M-2', 'ref_id': 'CA-M-2', 'role': 'Method', 'status': 'Active'})
            check(fields | {'relations': {}}, authored=False)
            check(fields | {'relations': {}, 'status': 'Archived'})
            for invalid in (SimpleNamespace(**{**target.__dict__, 'status': 'archived'}),
                            SimpleNamespace(**{**target.__dict__, 'metadata': {'role': 'Plan', 'form': 'Work Report'}})):
                select.return_value = invalid
                with self.assertRaises(InputError):
                    check(fields)

    def test_nonterminal_plan_is_rejected_under_any_terminal_ancestor(self):
        selection = SimpleNamespace(settings={'artifacts': {'identity': {'project_prefix': 'CA'}}})
        model = StatusModel(((None, None, 'Active'), ('Plan', None, 'Done')))
        fields = {'atom_id': 'CA-P-3', 'ref_id': 'CA-P-3', 'role': 'Plan', 'form': 'Plan',
                  'status': 'Active', 'version': 1, 'updated_at': '2026-01-01T00:00:00+00:00',
                  'container.atom': 'CA-P-2'}
        parents = {
            'CA-P-2': SimpleNamespace(status='active', metadata={'container': {'atom': 'CA-P-1'}}),
            'CA-P-1': SimpleNamespace(status='done', metadata={'container': {'scope_unit': 'CA-SU-1'}}),
        }
        with patch('ATOM_LIFECYCLE.validation.select_source', side_effect=lambda _, ref: parents[ref]):
            raw = render_carrier(None, fields, body='## Summary\n\nExample\n')
            with self.assertRaisesRegex(InputError, 'inside a Done or Canceled Plan'):
                validate_candidate(selection, model, raw, Path('candidate.md'))

    def test_required_identity_and_model_status(self):
        selection = SimpleNamespace(settings={'artifacts': {'identity': {'project_prefix': 'CA'}}})
        model = StatusModel(((None, None, 'Proposed'), ('Plan', None, 'Ready')))
        fields = {'atom_id': 'CA-P-1', 'ref_id': 'CA-P-1@1', 'role': 'Plan', 'form': 'Plan',
                  'status': 'Ready', 'version': 1, 'updated_at': '2026-01-01T00:00:00+00:00',
                  'container.scope_unit': 'CA-SU-1'}
        def check(values):
            validate_candidate(selection, model, render_carrier(None, values, body='## Summary\n\nExample\n'), Path('candidate.md'))
        check(fields)
        check(fields | {'status': 'ready'})
        with self.assertRaisesRegex(InputError, 'Role letter'):
            check(fields | {'atom_id': 'CA-R-1', 'ref_id': 'CA-R-1@1'})
        for key, value in (('status', 'Active'), ('version', True), ('ref_id', 'CA-P-2@1'),
                           ('container.scope_unit', ''), ('updated_at', '2026-01-01'), ('atom_id', 'CA-R-1')):
            with self.subTest(key=key), self.assertRaises(InputError):
                check(fields | {key: value})

    def test_global_form_validation_does_not_require_local_pair(self):
        from ATOM_LIFECYCLE.role_form_schema import RoleFormSchema

        selection = SimpleNamespace(
            settings={'artifacts': {'identity': {'project_prefix': 'CA'}}},
            structure={'scope_units': [
                {'parent': 'ROOT', 'scope_unit_name': 'SOURCE', 'scope_unit_id': 'CA-SU-1',
                 'admitted_role_forms': (('Method', 'Solution'), ('Evaluation', 'Direct Policy'))},
            ]},
        )
        roles = RoleFormSchema(frozenset({'Method', 'Evaluation'}),
                               frozenset({'Solution', 'Direct Policy', 'Approach Policy'}), frozenset(),
                               (('Direct Policy', frozenset({'Method'})),))
        noop = SimpleNamespace(validate=lambda _row: None)
        schema = SimpleNamespace(role_form=roles, validate_role_form=roles.validate, header=lambda _mode: noop,
                                 content=noop, content_constraints=noop,
                                 header_constraints=SimpleNamespace(validate=lambda *_args, **_kwargs: []))
        status = StatusModel(((None, None, 'Draft'),))
        model = SimpleNamespace(allowed=status.allowed, candidate_schema=schema)
        fields = {'atom_id': 'CA-M-1', 'ref_id': 'CA-M-1@1-draft', 'role': 'Method', 'form': 'Solution',
                  'status': 'Draft', 'version': 1, 'updated_at': '2026-01-01T00:00:00+00:00',
                  'container.scope_unit': 'CA-SU-1'}

        def check(values):
            validate_candidate(selection, model, render_carrier(None, values, body='## Summary\n\nExample\n'), Path('candidate.md'))

        check(fields)
        check(fields | {'container.scope_unit': 'SOURCE'})
        for form in ('Approach Policy', 'Direct Policy'):
            with self.subTest(form=form):
                check(fields | {'form': form})
        with self.assertRaisesRegex(InputError, 'not permitted'):
            check(fields | {'atom_id': 'CA-E-1', 'ref_id': 'CA-E-1@1-draft', 'role': 'Evaluation', 'form': 'Direct Policy'})


class DeclaredSchemaValidationTests(unittest.TestCase):
    def test_header_format_and_duplicate_declared_content(self):
        workbench = TOOLS.parents[0] / 'FEATURE_APPS/APP_WORKBENCH'
        sys.path.insert(0, str(workbench))
        from FEATURE_WORKBENCH_BACKEND.content_schema import (  # noqa: PLC0415
            ContentRule, DeclarationSource, _schema_from_rules,
        )
        from FEATURE_WORKBENCH_BACKEND.header_columns import HeaderColumn, HeaderSchema  # noqa: PLC0415
        from FEATURE_WORKBENCH_BACKEND.workbench_schema_asset import SchemaCompilation  # noqa: PLC0415
        from ATOM_LIFECYCLE.candidate_schema import CandidateSchema  # noqa: PLC0415
        from ATOM_LIFECYCLE.content_constraints import ContentConstraints  # noqa: PLC0415
        from ATOM_LIFECYCLE.header_constraints import HeaderConstraints  # noqa: PLC0415
        from ATOM_LIFECYCLE.role_form_schema import RoleFormSchema  # noqa: PLC0415

        header = HeaderSchema((HeaderColumn(('context', 'tier'), 'header.context.tier', 'BIGINT', True),))
        source = DeclarationSource(None, None, None)
        content = _schema_from_rules([ContentRule(('summary',), None, None, True, source)])
        role_form = RoleFormSchema(frozenset({'Plan'}), frozenset(), frozenset(), ())
        schema = CandidateSchema(SchemaCompilation(header, header, content), role_form,
                                 HeaderConstraints((), ()), ContentConstraints(()))
        selection = SimpleNamespace(settings={'artifacts': {'identity': {'project_prefix': 'CA'}}})
        status = StatusModel(((None, None, 'Proposed'),))
        model = SimpleNamespace(allowed=status.allowed, candidate_schema=schema)
        fields = {'atom_id': 'CA-P-1', 'ref_id': 'CA-P-1@1', 'role': 'Plan', 'form': 'Plan',
                  'status': 'Proposed', 'version': 1, 'updated_at': '2026-01-01T00:00:00+00:00',
                  'container.scope_unit': 'CA-SU-1', 'tier': 2}
        raw = render_carrier(None, fields, body='## Summary\n\nExample\n')
        validate_candidate(selection, model, raw, Path('candidate.md'))
        with self.assertRaises(InputError) as invalid_header:
            raw = render_carrier(None, fields | {'tier': 'bad'}, body='## Summary\n\nExample\n')
            validate_candidate(selection, model, raw, Path('candidate.md'))
        self.assertEqual(invalid_header.exception.field, 'tier')
        with self.assertRaises(InputError) as duplicate:
            raw = render_carrier(None, fields, body='## Summary\n\nOne\n\n## Summary\n\nTwo\n')
            validate_candidate(selection, model, raw, Path('candidate.md'))
        self.assertEqual(duplicate.exception.field, 'body')


if __name__ == '__main__':
    unittest.main()
