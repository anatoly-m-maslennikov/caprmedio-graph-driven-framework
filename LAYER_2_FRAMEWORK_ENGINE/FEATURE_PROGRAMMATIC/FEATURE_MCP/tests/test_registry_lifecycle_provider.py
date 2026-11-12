"""Private lifecycle provider: corrections, session isolation, and effects."""
from contextlib import contextmanager, nullcontext
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

MCP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(MCP), str(MCP.parent / 'FEATURE_TOOLS')]
from mcp.server.session import ServerSession  # noqa: E402
from mcp.server.connection import Connection  # noqa: E402
from registry_lifecycle_provider import LifecycleProvider, _refresh_selection as refresh_real, tool_descriptors  # noqa: E402


class LifecycleProviderTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.selection = SimpleNamespace(root=Path('/project'), instance_id='project-1', declaration_digest='initial')
        self.provider = LifecycleProvider(SimpleNamespace(selection=self.selection), object())
        refresh = patch('registry_lifecycle_provider._refresh_selection', side_effect=lambda selection: selection)
        refresh.start()
        self.addCleanup(refresh.stop)
        self.a = ServerSession.__new__(ServerSession)
        self.b = ServerSession.__new__(ServerSession)
        self.a._connection = Connection.__new__(Connection)
        self.b._connection = Connection.__new__(Connection)
        self.name = 'atom_lifecycle_create_draft'

    async def invoke(self, session, name, arguments):
        prepared = self.provider.prepare_arguments(name, arguments, SimpleNamespace(session=session))
        return await self.provider.call(name, prepared)

    async def test_runtime_action_uses_shared_workbench_reader(self):
        from ATOM_LIFECYCLE import source

        scope = []

        @contextmanager
        def read_scope():
            scope.append('entered')
            try:
                yield
            finally:
                scope.append('exited')

        reader = SimpleNamespace(lifecycle_read_scope=read_scope)
        self.provider.workbench = SimpleNamespace(lifecycle_reader=lambda: nullcontext(reader))

        def execute(selection, model, name, params):
            self.assertIs(selection, self.selection)
            self.assertIs(source.query_reader(), reader)
            self.assertEqual(scope, ['entered'])
            return {'outcome': 'completed', 'errors': []}

        with (patch('registry_lifecycle_provider._refresh_selection', return_value=self.selection) as refresh,
              patch('registry_lifecycle_provider.backend.execute', side_effect=execute),
              patch('registry_lifecycle_provider.bind_selection', return_value=nullcontext())):
            result = await self.invoke(self.a, self.name, {})
        self.assertEqual(result, {'status': 'completed'})
        self.assertEqual(scope, ['entered', 'exited'])
        refresh.assert_called_once_with(self.selection, reader)

    async def test_corrections_are_scoped_to_session_and_tool(self):
        calls = []
        def execute(selection, model, name, params):
            calls.append((name, params))
            if 'form' not in params.get('newAtom', {}):
                return {'outcome': 'needs_input', 'requested_input': {'form': {'error': 'required'}}, 'effects': []}
            return {'outcome': 'completed', 'effects': [{'operation': 'create'}], 'errors': []}
        with patch('registry_lifecycle_provider.backend.execute', side_effect=execute):
            self.assertEqual('needs_input', (await self.invoke(self.a, self.name, {'newAtom': {'role': 'Method'}}))['status'])
            self.assertEqual('needs_input', (await self.invoke(self.b, self.name, {'newAtom': {'role': 'Requirement'}}))['status'])
            next_request = ServerSession.__new__(ServerSession)
            next_request._connection = self.a._connection
            self.assertEqual({'status': 'completed'}, await self.invoke(next_request, self.name, {'form': 'Declaration'}))
            self.assertEqual({'role': 'Method', 'form': 'Declaration'}, calls[-1][1]['newAtom'])
            self.assertEqual({'status': 'completed'}, await self.invoke(self.b, self.name, {'form': 'Other'}))
            self.assertEqual({'role': 'Requirement', 'form': 'Other'}, calls[-1][1]['newAtom'])
            await self.invoke(self.a, self.name, {'newAtom': {'role': 'Plan'}})
            await self.invoke(self.a, 'atom_lifecycle_archive', {'target': {'ref_id': 'CA-P-1', 'version': 1}})
            self.assertNotIn('newAtom', calls[-1][1])

    async def test_pending_cancellation_is_explicit_and_scoped(self):
        missing = {'outcome': 'needs_input', 'requested_input': {'form': {'error': 'required'}}, 'effects': []}
        with patch('registry_lifecycle_provider.backend.execute', return_value=missing) as execute:
            result = await self.invoke(self.a, self.name, {'newAtom': {'role': 'Method'}})
            self.assertEqual([{'code': 'invalid_input', 'field': 'form', 'message': 'required'}], result['errors'])
            self.assertEqual({'form': {'error': 'required'}}, result['requested_input'])
            self.assertEqual('no_pending_input', (await self.invoke(self.b, self.name, {'cancel': True}))['errors'][0]['code'])
            other_tool = await self.invoke(self.a, 'atom_lifecycle_archive', {'cancel': True})
            self.assertEqual('no_pending_input', other_tool['errors'][0]['code'])
            other_project = LifecycleProvider(SimpleNamespace(selection=SimpleNamespace(
                root=self.selection.root, instance_id='another-project', declaration_digest='initial')), object())
            args = other_project.prepare_arguments(self.name, {'cancel': True}, SimpleNamespace(session=self.a))
            self.assertEqual('no_pending_input', (await other_project.call(self.name, args))['errors'][0]['code'])
            self.assertEqual(1, execute.call_count)
            mixed = await self.invoke(self.a, self.name, {'cancel': True, 'form': 'Declaration'})
            self.assertEqual('invalid_input', mixed['errors'][0]['code'])
            self.assertEqual({'status': 'cancelled'}, await self.invoke(self.a, self.name, {'cancel': True}))
            self.assertEqual('no_pending_input', (await self.invoke(self.a, self.name, {'cancel': True}))['errors'][0]['code'])
            self.assertEqual(1, execute.call_count)
            await self.invoke(self.a, self.name, {'form': 'Declaration'})
            self.assertNotIn('role', execute.call_args.args[3].get('newAtom', {}))

    async def test_all_six_tools_cancel_pending_without_dispatch(self):
        for descriptor in tool_descriptors():
            with self.subTest(tool=descriptor.name):
                self.assertEqual('boolean', descriptor.input_schema['properties']['cancel']['type'])
                missing = {'outcome': 'needs_input', 'requested_input': {
                    next(key for key in descriptor.input_schema['properties'] if key != 'cancel'): {'error': 'required'}},
                    'effects': []}
                with patch('registry_lifecycle_provider.backend.execute', return_value=missing) as execute:
                    self.assertEqual('needs_input', (await self.invoke(self.a, descriptor.name, {}))['status'])
                    self.assertEqual({'status': 'cancelled'}, await self.invoke(self.a, descriptor.name, {'cancel': True}))
                    self.assertEqual(1, execute.call_count)

    async def test_corrected_and_additional_fields_are_retained(self):
        calls = []
        def execute(_selection, _model, _name, params):
            calls.append(params)
            if len(calls) == 1:
                return {'outcome': 'needs_input', 'requested_input': {'form': {'error': 'required'}}, 'effects': []}
            return {'outcome': 'completed', 'errors': []}
        with patch('registry_lifecycle_provider.backend.execute', side_effect=execute):
            await self.invoke(self.a, self.name, {'newAtom': {'role': 'Requirement'}})
            response = await self.invoke(self.a, self.name, {'form': 'Definition', 'summary': 'An extra field'})
        self.assertEqual({'status': 'completed'}, response)
        self.assertEqual({'role': 'Requirement', 'form': 'Definition', 'summary': 'An extra field'}, calls[1]['newAtom'])

    async def test_archive_and_promote_batches_preserve_backend_ledger(self):
        target1 = {'target': {'ref_id': 'CA-R-1', 'version': 1}}
        target2 = {'target': {'ref_id': 'CA-R-2', 'version': 2}}
        for name in ('atom_lifecycle_archive', 'atom_lifecycle_promote_draft'):
            items = [target1, target2] if name.endswith('archive') else [
                {**target1, 'targetStatus': 'Active'}, {**target2, 'targetStatus': 'Done'}]
            cases = [
                {'outcome': 'completed', 'target_results': [{'target': items[0]}, {'target': items[1]}],
                 'remaining_targets': [], 'effects': [{'operation': 'archive'}], 'errors': [], 'warnings': []},
                {'outcome': 'failed', 'target_results': [{'target': items[0]}], 'remaining_targets': [items[1]],
                 'effects': [{'operation': 'archive', 'state': 'known'}, {'operation': 'create', 'state': 'unknown'}],
                 'errors': [{'code': 'failure', 'message': 'Stopped.'}], 'warnings': ['warning']},
            ]
            for value in cases:
                with self.subTest(name=name, outcome=value['outcome']), \
                     patch('registry_lifecycle_provider.backend.execute', return_value=value) as execute:
                    result = await self.invoke(self.a, name, {'targets': items})
                self.assertEqual({'status': value['outcome'], 'results': value['target_results'],
                                  **{key: value[key] for key in ('remaining_targets', 'effects', 'errors', 'warnings')}}, result)
                self.assertEqual({'targets': items}, execute.call_args.args[3])

    async def test_batch_never_resumes_pending_single_or_requests_correction(self):
        name = 'atom_lifecycle_archive'
        target = {'target': {'ref_id': 'CA-R-1', 'version': 1}}
        missing = {'outcome': 'needs_input', 'effects': [], 'requested_input': {'target': {'error': 'required'}}}
        with patch('registry_lifecycle_provider.backend.execute', side_effect=[missing, missing]) as execute:
            self.assertEqual('needs_input', (await self.invoke(self.a, name, {}))['status'])
            response = await self.invoke(self.a, name, {'targets': [target]})
            cancel = await self.invoke(self.a, name, {'cancel': True})
        self.assertEqual('failed', response['status'])
        self.assertEqual('required', response['errors'][0]['message'])
        self.assertEqual({'targets': [target]}, execute.call_args.args[3])
        self.assertEqual('no_pending_input', cancel['errors'][0]['code'])
        self.assertEqual(2, execute.call_count)

    async def test_batch_with_backend_stops_at_first_failure(self):
        from ATOM_LIFECYCLE import backend

        name = 'atom_lifecycle_archive'
        targets = [{'target': {'ref_id': f'CA-R-{number}', 'version': 1}} for number in (1, 2, 3)]
        self.provider.model = SimpleNamespace(candidate_schema=SimpleNamespace(placement=object()))
        def archive(_selection, _model, entry):
            if entry == targets[1]:
                return {'outcome': 'failed', 'effects': [], 'errors': [{'code': 'failure'}], 'warnings': []}
            return {'outcome': 'completed', 'effects': [{'operation': 'archive'}], 'errors': [], 'warnings': []}
        with patch.dict(backend.ROUTES, {name: archive}), \
             patch.object(backend, '_selector', side_effect=lambda _, ref, __: (ref, None, None)), \
             patch.object(backend, 'bind_placement', return_value=nullcontext()), \
             patch.object(backend, '_project_write_lock', return_value=nullcontext()):
            response = await self.invoke(self.a, name, {'targets': targets})
        self.assertEqual('failed', response['status'])
        self.assertEqual([item['target'] for item in targets[:2]],
                         [item['target'] for item in response['results']])
        self.assertEqual([targets[2]], response['remaining_targets'])
        self.assertEqual([{'operation': 'archive'}], response['effects'])

    def test_batch_descriptors_define_archive_and_promotion_entries(self):
        descriptors = {item.name: item.input_schema['properties'] for item in tool_descriptors()}
        archive = descriptors['atom_lifecycle_archive']['targets']
        promote = descriptors['atom_lifecycle_promote_draft']['targets']
        self.assertEqual('array', archive['type'])
        self.assertEqual(['target'], archive['items']['required'])
        self.assertEqual(['target', 'targetStatus'], promote['items']['required'])
        self.assertIn('target', descriptors['atom_lifecycle_archive'])
        self.assertIn('targetStatus', descriptors['atom_lifecycle_promote_draft'])

    async def test_corrections_survive_provider_replacement_but_not_project_change(self):
        calls = []
        def execute(selection, model, name, params):
            calls.append((selection.instance_id, params))
            if 'body' not in params.get('changes', {}):
                return {'outcome': 'needs_input', 'requested_input': {'changes.body': {'error': 'required'}}, 'effects': []}
            return {'outcome': 'completed', 'errors': []}
        name = 'atom_lifecycle_direct_update'
        with patch('registry_lifecycle_provider.backend.execute', side_effect=execute):
            value = await self.invoke(self.a, name, {'target': {'ref_id': 'CA-R-1', 'version': 1}})
            self.assertEqual({'body': {'error': 'required'}}, value['requested_input'])
            await self.provider.close()
            self.provider = LifecycleProvider(SimpleNamespace(selection=self.selection), object())
            other = LifecycleProvider(SimpleNamespace(selection=SimpleNamespace(root=Path('/other'), instance_id='project-2', declaration_digest='initial')), object())
            args = other.prepare_arguments(name, {'body': 'other'}, SimpleNamespace(session=self.a))
            await other.call(name, args)
            self.assertNotIn('target', calls[-1][1])
            self.assertEqual({'status': 'completed'}, await self.invoke(self.a, name, {'body': 'fixed'}))
            self.assertEqual({'ref_id': 'CA-R-1', 'version': 1}, calls[-1][1]['target'])
            self.assertEqual({'body': 'fixed'}, calls[-1][1]['changes'])

    async def test_update_source_switch_does_not_reuse_pending_input_or_pin(self):
        name = 'atom_lifecycle_update'
        old = {'ref_id': 'CA-P-10', 'version': 1}
        new = {'ref_id': 'CA-P-11', 'version': 1}
        scenarios = (
            ({'sourceCurrent': new, 'changes': {'body': 'new body'}},
             {'sourceCurrent': new, 'changes': {'body': 'new body'}}, {}),
            ({'sourceCurrent': old, 'priority': 'High'},
             {'sourceCurrent': old, 'changes': {'summary': 'retained', 'priority': 'High'}},
             {'pending_source': 'old-source-sha'}),
            ({'priority': 'High'},
             {'sourceCurrent': old, 'changes': {'summary': 'retained', 'priority': 'High'}},
             {'pending_source': 'old-source-sha'}),
        )
        for correction, expected_params, expected_kwargs in scenarios:
            calls = []
            def execute(_selection, _model, _name, params, **kwargs):
                calls.append((params, kwargs))
                if len(calls) == 1:
                    return {'outcome': 'needs_input', 'effects': [], 'pending_source': 'old-source-sha',
                            'requested_input': {'priority': {'error': 'required'}}}
                return {'outcome': 'completed', 'errors': []}
            with self.subTest(correction=correction), patch('registry_lifecycle_provider.backend.execute', side_effect=execute):
                first = await self.invoke(self.a, name, {'sourceCurrent': old, 'changes': {'summary': 'retained'}})
                self.assertEqual('needs_input', first['status'])
                self.assertEqual({'status': 'completed'}, await self.invoke(self.a, name, correction))
                self.assertEqual((expected_params, expected_kwargs), calls[-1])

    async def test_create_draft_forwards_source_id_with_optional_version_and_changes(self):
        cases = [
            {'sourceCurrent': 'CA-R-1'},
            {'sourceCurrent': {'ref_id': 'CA-R-1'}},
            {'sourceCurrent': {'ref_id': 'CA-R-1', 'version': 2}},
            {'sourceCurrent': {'ref_id': 'CA-R-1'}, 'changes': {'summary': 'New summary'}},
        ]
        with patch('registry_lifecycle_provider.backend.execute', return_value={
                'outcome': 'completed', 'errors': []}) as execute:
            for arguments in cases:
                with self.subTest(arguments=arguments):
                    self.assertEqual({'status': 'completed'}, await self.invoke(self.a, self.name, arguments))
                    self.assertEqual(arguments, execute.call_args.args[3])

    async def test_create_draft_source_change_does_not_inherit_old_version(self):
        missing = {'outcome': 'needs_input', 'effects': [],
                   'requested_input': {'sourceCurrent': {'error': 'Select a source'}}}
        with patch('registry_lifecycle_provider.backend.execute', side_effect=[missing, {
                'outcome': 'completed', 'errors': []}]) as execute:
            await self.invoke(self.a, self.name, {'sourceCurrent': {'ref_id': 'CA-R-1', 'version': 2}})
            result = await self.invoke(self.a, self.name, {'sourceCurrent': {'ref_id': 'CA-R-2'}})
        self.assertEqual({'status': 'completed'}, result)
        self.assertEqual({'sourceCurrent': {'ref_id': 'CA-R-2'}}, execute.call_args.args[3])

    async def test_create_draft_source_version_correction_keeps_string_id(self):
        missing = {'outcome': 'needs_input', 'effects': [],
                   'requested_input': {'sourceCurrent': {'error': 'Select a source version'}}}
        with patch('registry_lifecycle_provider.backend.execute', side_effect=[missing, {
                'outcome': 'completed', 'errors': []}]) as execute:
            await self.invoke(self.a, self.name, {'sourceCurrent': 'CA-R-1'})
            result = await self.invoke(self.a, self.name, {'sourceCurrent': {'version': 2}})
        self.assertEqual({'status': 'completed'}, result)
        self.assertEqual({'sourceCurrent': {'ref_id': 'CA-R-1', 'version': 2}}, execute.call_args.args[3])

    def test_create_draft_descriptor_documents_optional_source_version(self):
        descriptor = next(item for item in tool_descriptors() if item.name == self.name)
        description = descriptor.input_schema['properties']['sourceCurrent']['description']
        self.assertIn('ref_id', description)
        self.assertIn('optional', description)
        self.assertIn('version', description)

    async def test_changed_declarations_reject_pending_input(self):
        newer = SimpleNamespace(root=self.selection.root, instance_id=self.selection.instance_id,
                                declaration_digest='new')
        name = 'atom_lifecycle_change_status'
        pending = {'outcome': 'needs_input', 'requested_input': {'targetStatus': {'error': 'required'}}}
        with (patch('registry_lifecycle_provider._refresh_selection', side_effect=[self.selection, newer]),
              patch('registry_lifecycle_provider.backend.execute', return_value=pending) as execute):
            self.assertEqual('needs_input', (await self.invoke(self.a, name, {}))['status'])
            result = await self.invoke(self.a, name, {'targetStatus': 'Active'})
        self.assertEqual('failed', result['status'])
        self.assertEqual('source_changed', result['errors'][0]['code'])
        self.assertEqual([], result['effects'])
        execute.assert_called_once()

    async def test_new_scope_is_read_for_each_write_without_restart(self):
        from ATOM_LIFECYCLE import common
        from project_selection import ProjectSelection, rebind_selection, resolve_project
        from scope_unit_declarations import read_scope_unit_declarations
        from scope_declaration_test_support import write_scope_unit_declarations
        sys.path.insert(0, str(MCP.parent / 'FEATURE_TOOLS' / 'tests'))
        from lifecycle_placement_test_support import fixture_rules

        class Model:
            candidate_schema = SimpleNamespace(placement=fixture_rules(), role_form=SimpleNamespace(
                encode=lambda field, value: value, decode=lambda field, value: value))

            def allowed(self, role, form):
                return {'Draft'}

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            control = root / '.caprmedio_test'
            control.mkdir()
            (control / 'caprmedio_project_settings.toml').write_text(
                '[project]\nname="TEST"\n[artifacts.identity]\nproject_prefix="CA"\n'
                '[paths]\ncontrol_root=".caprmedio_test"\n')
            write_scope_unit_declarations(root, control_root=control)
            selection = resolve_project(root)
            host = Path('/unmounted/caprmedio-test')
            host_id = hashlib.sha256(f'{host}\0{selection.control_relative.as_posix()}'.encode()).hexdigest()
            transported = rebind_selection(selection, host_id, host_root=host)
            refreshed = refresh_real(transported)
            self.assertEqual((host_id, host), (refreshed.instance_id, refreshed.host_root))
            self.provider = LifecycleProvider(SimpleNamespace(selection=selection), Model())
            units = write_scope_unit_declarations(root, control_root=control, rows=[
                {'scope_unit_name': 'NEW', 'scope_unit_label': 'FEATURE'},
            ])
            declarations = read_scope_unit_declarations(root, control)
            indexed = SimpleNamespace(lifecycle_declarations=lambda: declarations)
            with (patch.object(ProjectSelection, '_revalidate_boundary', side_effect=AssertionError('boundary scan')),
                  patch('registry_lifecycle_provider.resolve_project', side_effect=AssertionError('Project scan'))):
                indexed_selection = refresh_real(selection, indexed)
                self.assertEqual(declarations.digest, indexed_selection.declaration_digest)
                self.assertIn('NEW', [item['scope_unit_name'] for item in indexed_selection.structure['scope_units']])
                self.assertIs(indexed_selection, refresh_real(indexed_selection, indexed))
                self.assertEqual(selection.instance_id, indexed_selection.instance_id)
            new_atom = {'role': 'Requirement', 'form': 'Declaration', 'scope_unit': 'NEW',
                        'summary': 'New', 'body': '## Summary\n\nNew\n'}
            with patch('registry_lifecycle_provider._refresh_selection', side_effect=refresh_real), \
                    patch.object(common, 'allocate_id', side_effect=['CA-R-9', 'CA-R-10']), \
                    patch('ATOM_LIFECYCLE.validation._validate_declared_schema'):
                self.assertEqual({'status': 'completed'}, await self.invoke(self.a, self.name, {'newAtom': new_atom}))
                self.assertEqual(1, len(list(units['NEW']['authority_path'].rglob('*draft*.md'))))

                # Existing pending inputs cannot silently target a renamed declaration.
                self.assertEqual('needs_input', (await self.invoke(self.a, self.name, {'newAtom': {'role': 'Requirement'}}))['status'])
                units['NEW']['declaration_path'].unlink()
                result = await self.invoke(self.a, self.name, {'form': 'Declaration'})
                self.assertEqual('failed', result['status'])
                self.assertEqual('source_changed', result['errors'][0]['code'])

                renamed = write_scope_unit_declarations(root, control_root=control, rows=[
                    {'scope_unit_name': 'NEWER', 'scope_unit_label': 'FEATURE'},
                ])
                renamed_atom = {**new_atom, 'scope_unit': 'NEWER'}
                self.assertEqual({'status': 'completed'}, await self.invoke(self.a, self.name, {'newAtom': renamed_atom}))
                self.assertEqual(1, len(list(renamed['NEWER']['authority_path'].rglob('*draft*.md'))))

                # Project settings remain bound to the original Project.
                with (control / 'caprmedio_project_settings.toml').open('a') as settings:
                    settings.write('\n[changed]\nvalue=true\n')
                result = await self.invoke(self.a, self.name, {'newAtom': new_atom})
                self.assertEqual('failed', result['status'])
                self.assertEqual('source_selection_failed', result['errors'][0]['code'])

    async def test_post_effect_failure_preserves_effects_and_starts_no_correction(self):
        effects = [{'operation': 'archive'}]
        value = {'outcome': 'needs_input', 'effects': effects, 'warnings': ['prior'],
                 'requested_input': {'target': {'error': 'Draft could not be promoted'}}}
        name = 'atom_lifecycle_update'
        with patch('registry_lifecycle_provider.backend.execute',
                   side_effect=[value, {'outcome': 'completed'}]) as execute:
            result = await self.invoke(self.a, name, {'sourceCurrent': {'ref_id': 'CA-P-1', 'version': 1}})
            self.assertEqual({'status': 'failed', 'effects': effects, 'warnings': ['prior'],
                              'errors': [{'code': 'invalid_input', 'field': 'target',
                                          'message': 'Draft could not be promoted'}]}, result)
            execute.assert_called_once()
            self.assertEqual({'status': 'completed'}, await self.invoke(self.a, name, {}))
            self.assertEqual({}, execute.call_args.args[3])
            self.assertEqual({}, execute.call_args.kwargs)

    async def test_create_draft_corrections_run_real_backend(self):
        from ATOM_LIFECYCLE import common
        from project_selection import resolve_project
        sys.path.insert(0, str(MCP.parent / 'FEATURE_TOOLS' / 'tests'))
        from scope_declaration_test_support import write_scope_unit_declarations
        from lifecycle_placement_test_support import fixture_rules

        class Model:
            candidate_schema = SimpleNamespace(placement=fixture_rules(), role_form=SimpleNamespace(
                encode=lambda field, value: value, decode=lambda field, value: value))

            def allowed(self, role, form):
                return {'Draft'}

        new_atom = {'role': 'Requirement', 'form': 'Declaration', 'scope_unit': 'TEST',
                    'summary': 'New', 'body': '## Summary\n\nNew\n'}
        selector = {'ref_id': 'CA-R-1', 'version': 2}
        cases = [
            ({'newAtom': 'bad'}, {'newAtom': new_atom}, 'newAtom'),
            ({'newAtom': new_atom, 'sourceCurrent': selector}, {'newAtom': new_atom}, 'sourceCurrent'),
            ({'newAtom': new_atom, 'sourceCurrent': selector}, {'sourceCurrent': selector}, 'sourceCurrent'),
            ({'newAtom': new_atom, 'changes': {}}, {'newAtom': new_atom}, 'changes'),
        ]
        for initial, correction, field in cases:
            with self.subTest(initial=initial, correction=correction), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp).resolve()
                control = root / '.caprmedio_test'
                control.mkdir()
                (control / 'caprmedio_project_settings.toml').write_text(
                    '[project]\nname="TEST"\n[artifacts.identity]\nproject_prefix="CA"\n'
                    '[paths]\ncontrol_root=".caprmedio_test"\n')
                write_scope_unit_declarations(root, control_root=control, rows=[])
                source = control / '04_requirement/CA-R-1-DECLARATION--example.md'
                source.parent.mkdir()
                source.write_text('---\nidentity:\n  atom_id: CA-R-1\n  ref_id: CA-R-1\n'
                                  'context:\n  container:\n    scope_unit: TEST\n  role: Requirement\n'
                                  '  form: Declaration\nstate:\n  status: Active\n  version: 2\n'
                                  '  updated_at: 2026-01-01\n---\n## Summary\n\nExample\n\n## Claim\n\nText.\n')
                self.provider = LifecycleProvider(SimpleNamespace(selection=resolve_project(root)), Model())
                before = {p.relative_to(control): p.read_bytes() for p in control.rglob('*') if p.is_file()}
                with patch.object(common, 'allocate_id', return_value='CA-R-9'), \
                        patch('ATOM_LIFECYCLE.validation._validate_declared_schema'):
                    result = await self.invoke(self.a, self.name, initial)
                    self.assertEqual('needs_input', result['status'])
                    self.assertIn(field, result['requested_input'])
                    self.assertEqual(before, {p.relative_to(control): p.read_bytes() for p in control.rglob('*') if p.is_file()})
                    self.assertEqual({'status': 'completed'}, await self.invoke(self.a, self.name, correction))
                    self.assertGreater(len(list(control.rglob('*draft*.md'))), 0)

    async def test_missing_placement_model_refuses_before_write_lock(self):
        from ATOM_LIFECYCLE import backend

        with patch.object(backend, '_project_write_lock') as lock:
            result = await self.invoke(self.a, 'atom_lifecycle_archive',
                                       {'target': {'ref_id': 'CA-R-1', 'version': 1}})
        self.assertEqual('failed', result['status'])
        self.assertEqual('placement_model_unavailable', result['errors'][0]['code'])
        self.assertEqual([], result['effects'])
        lock.assert_not_called()

    async def test_failure_reports_partial_effects_and_clears_pending(self):
        outputs = [
            {'outcome': 'needs_input', 'requested_input': {'targetStatus': {}}, 'effects': []},
            {'outcome': 'failed', 'effects': [{'operation': 'create'}], 'errors': [{'message': 'failed'}], 'warnings': []},
            {'outcome': 'completed', 'errors': []},
        ]
        calls = []
        def execute(selection, model, name, params):
            calls.append(params)
            return outputs.pop(0)
        name = 'atom_lifecycle_change_status'
        with patch('registry_lifecycle_provider.backend.execute', side_effect=execute):
            await self.invoke(self.a, name, {'target': {'ref_id': 'CA-R-1', 'version': 1}})
            result = await self.invoke(self.a, name, {'targetStatus': 'Active'})
            self.assertEqual('failed', result['status'])
            self.assertEqual([{'operation': 'create'}], result['effects'])
            await self.invoke(self.a, name, {})
            self.assertEqual({}, calls[-1])

    async def test_mcp_client_with_elicitation_receives_structured_correction(self):
        from mcp import types
        from mcp.client._memory import InMemoryTransport
        from mcp.client.session import ClientSession
        from mcp.server import Server

        name = 'atom_lifecycle_update'
        target = {'ref_id': 'CA-R-1', 'version': 1}
        requested = {'priority': {'error': 'invalid', 'allowed_values': ['High']}}
        missing = {'outcome': 'needs_input', 'requested_input': requested,
                   'pending_source': 'original', 'effects': []}

        async def call(context, request):
            args = self.provider.prepare_arguments(request.name, request.arguments or {}, context)
            value = await self.provider.call(request.name, args)
            return types.CallToolResult(content=[], structured_content=value)

        async def elicit(_context, _request):
            self.fail('Lifecycle should return input errors to the caller')

        async def list_tools(_context, _request):
            return types.ListToolsResult(tools=list(tool_descriptors()))

        server = Server('lifecycle-input-test', on_call_tool=call, on_list_tools=list_tools)
        async with InMemoryTransport(server, raise_exceptions=True) as streams:
            async with ClientSession(*streams, elicitation_callback=elicit) as client:
                await client.initialize()
                with patch('registry_lifecycle_provider.backend.execute',
                           side_effect=[missing, {'outcome': 'completed'}]) as execute:
                    result = await client.call_tool(name, {'sourceCurrent': target})
                    self.assertEqual({'status': 'needs_input', 'requested_input': requested,
                                      'errors': [{'code': 'invalid_input', 'field': 'priority',
                                                  'message': 'invalid'}]}, result.structured_content)
                    execute.assert_called_once()
                    result = await client.call_tool(name, {'priority': 'High', 'tier': 3})
                    self.assertEqual({'status': 'completed'}, result.structured_content)
                    self.assertEqual({'sourceCurrent': target, 'changes': {'priority': 'High', 'tier': 3}},
                                     execute.call_args.args[3])
                    self.assertEqual({'pending_source': 'original'}, execute.call_args.kwargs)

    async def test_requires_real_session_and_optional_corrections(self):
        with self.assertRaises(ValueError):
            self.provider.prepare_arguments(self.name, {}, SimpleNamespace(session=object()))
        self.assertTrue(all(not tool.input_schema.get('required') for tool in tool_descriptors()))


if __name__ == '__main__':
    unittest.main()

class LifecycleRegistryExposureTests(unittest.TestCase):
    def test_generated_registry_exposes_all_lifecycle_tools(self):
        from tool_registry_assets import FEATURE_RELATIVE, read_inventory
        from registry_lifecycle_provider import tool_descriptors

        inventory = read_inventory(MCP)
        entry = next(item for item in inventory.providers if item.provider_id == 'lifecycle')
        self.assertEqual('tool_descriptors', entry.descriptor_factory)
        all_names = {tool.name for tool in tool_descriptors()}
        admitted = {'atom_lifecycle_archive', 'atom_lifecycle_change_status', 'atom_lifecycle_create_draft',
                    'atom_lifecycle_direct_update', 'atom_lifecycle_promote_draft', 'atom_lifecycle_update'}
        self.assertEqual(admitted, all_names)
        self.assertFalse(all_names & set(inventory.blacklist))
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            feature = root / FEATURE_RELATIVE
            feature.mkdir(parents=True)
            for name in ('tool_providers.json', 'registry_lifecycle_provider.py', 'registry_workbench_provider.py'):
                shutil.copy2(MCP / name, feature / name)
            env = dict(os.environ)
            env['PYTHONPATH'] = os.pathsep.join((str(MCP), str(MCP.parent / 'FEATURE_TOOLS'),
                                                  str(MCP.parent / 'FEATURE_APPS')))
            subprocess.run([sys.executable, str(MCP / 'generate_tool_registry.py'), '--package-root', str(root)],
                           env=env, check=True, capture_output=True, text=True)
            generated = json.loads((feature / 'tool_registry.json').read_text())
        lifecycle = next(item for item in generated['providers'] if item['provider_id'] == 'lifecycle')
        self.assertEqual(admitted, {tool['name'] for tool in lifecycle['tools']})
        self.assertEqual(admitted, set(generated['public_tools']) & all_names)


class LifecycleHTTPTests(unittest.TestCase):
    def test_stateful_http_keeps_corrections_with_the_right_connection(self):
        from mcp.server.lowlevel import Server
        from mcp import types
        from starlette.testclient import TestClient

        provider = LifecycleProvider(SimpleNamespace(selection=SimpleNamespace(
            root=Path('/project'), instance_id='project-1', declaration_digest='initial')), object())
        seen = []
        def execute(_selection, _model, _name, params):
            seen.append(params)
            if 'form' not in params.get('newAtom', {}):
                return {'outcome': 'needs_input', 'requested_input': {'form': {}}, 'effects': []}
            return {'outcome': 'completed', 'errors': []}
        async def call(context, params):
            args = provider.prepare_arguments(params.name, params.arguments or {}, context)
            value = await provider.call(params.name, args)
            return types.CallToolResult(content=[], structured_content=value)
        server = Server('test', on_call_tool=call)
        app = server.streamable_http_app(streamable_http_path='/mcp', json_response=True)
        with patch('registry_lifecycle_provider._refresh_selection', side_effect=lambda selection: selection), \
                patch('registry_lifecycle_provider.backend.execute', side_effect=execute), TestClient(app, base_url="http://localhost:8000") as client:
            def send(method, params, session=None, ident=1):
                headers = {'accept': 'application/json, text/event-stream'}
                if session:
                    headers['mcp-session-id'] = session
                return client.post('/mcp', headers=headers, json={'jsonrpc': '2.0', 'id': ident, 'method': method, 'params': params})
            init = {'protocolVersion': '2025-06-18', 'capabilities': {}, 'clientInfo': {'name': 'test', 'version': '1'}}
            a, b = send('initialize', init), send('initialize', init)
            self.assertEqual(200, a.status_code)
            self.assertEqual(200, b.status_code)
            sa, sb = a.headers['mcp-session-id'], b.headers['mcp-session-id']
            for session in (sa, sb):
                client.post('/mcp', headers={'mcp-session-id': session, 'accept': 'application/json, text/event-stream'},
                            json={'jsonrpc': '2.0', 'method': 'notifications/initialized'})
            name = 'atom_lifecycle_create_draft'
            for session, role in ((sa, 'Method'), (sb, 'Requirement')):
                response = send('tools/call', {'name': name, 'arguments': {'newAtom': {'role': role}}}, session)
                self.assertEqual('needs_input', response.json()['result']['structuredContent']['status'])
            for session, role in ((sa, 'Method'), (sb, 'Requirement')):
                response = send('tools/call', {'name': name, 'arguments': {'form': 'Declaration'}}, session)
                self.assertEqual('completed', response.json()['result']['structuredContent']['status'])
                self.assertEqual(role, seen[-1]['newAtom']['role'])
