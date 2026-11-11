"""Private lifecycle provider: corrections, session isolation, and effects."""
import asyncio
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
from registry_lifecycle_provider import LifecycleProvider, tool_descriptors  # noqa: E402


class LifecycleProviderTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.selection = SimpleNamespace(root=Path('/project'), instance_id='project-1')
        self.provider = LifecycleProvider(SimpleNamespace(selection=self.selection), object())
        self.a = ServerSession.__new__(ServerSession)
        self.b = ServerSession.__new__(ServerSession)
        self.a._connection = Connection.__new__(Connection)
        self.b._connection = Connection.__new__(Connection)
        self.name = 'atom_lifecycle_create_draft'

    async def invoke(self, session, name, arguments):
        prepared = self.provider.prepare_arguments(name, arguments, SimpleNamespace(session=session))
        return await self.provider.call(name, prepared)

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
            other = LifecycleProvider(SimpleNamespace(selection=SimpleNamespace(root=Path('/other'), instance_id='project-2')), object())
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

    async def test_pending_promotion_is_scoped_and_resumes_with_only_correction(self):
        token = object()
        effects = [{'operation': 'create', 'target': 'draft'}]
        warnings = ['prior warning']
        calls = []
        def execute(_selection, _model, _name, params, **kwargs):
            calls.append((params, kwargs))
            if kwargs.get('pending_promotion') is token:
                if params == {'targetStatus': 'Wrong'}:
                    return {'outcome': 'needs_input', 'pending_promotion': token, 'effects': effects,
                            'warnings': warnings, 'requested_input': {'target': {'error': 'external repair'}}}
                return {'outcome': 'completed', 'errors': []}
            return {'outcome': 'needs_input', 'pending_promotion': token, 'effects': effects,
                    'warnings': warnings, 'requested_input': {'target': {'error': 'external repair'}}}
        name = 'atom_lifecycle_update'
        with patch('registry_lifecycle_provider.backend.execute', side_effect=execute):
            first = await self.invoke(self.a, name, {'sourceCurrent': {'ref_id': 'CA-P-10', 'version': 1}})
            self.assertEqual({'status': 'needs_input', 'requested_input': {'target': {'error': 'external repair'}},
                              'effects': effects, 'warnings': warnings}, first)
            await self.invoke(self.b, name, {})
            self.assertEqual(({}, {}), calls[-1])
            second = await self.invoke(self.a, name, {'targetStatus': 'Wrong'})
            self.assertEqual('needs_input', second['status'])
            self.assertEqual(({'targetStatus': 'Wrong'}, {'pending_promotion': token}), calls[-1])
            self.assertEqual({'status': 'completed'}, await self.invoke(self.a, name, {}))
            self.assertEqual(({}, {'pending_promotion': token}), calls[-1])

    async def test_cancelled_promotion_form_does_not_leak_token_to_next_call(self):
        token, calls, waiting = object(), [], asyncio.Event()
        def execute(_selection, _model, _name, params, **kwargs):
            calls.append((params, kwargs))
            if len(calls) == 1:
                return {'outcome': 'needs_input', 'pending_promotion': token,
                        'effects': [{'operation': 'archive'}],
                        'requested_input': {'targetStatus': {'error': 'select status'}}}
            return {'outcome': 'completed', 'errors': []}
        async def wait_for_form(*_args):
            waiting.set()
            await asyncio.Event().wait()
        name = 'atom_lifecycle_update'
        with patch('registry_lifecycle_provider.backend.execute', side_effect=execute), \
                patch('registry_lifecycle_provider._request_correction', side_effect=wait_for_form):
            task = asyncio.create_task(self.invoke(self.a, name, {'sourceCurrent': {'ref_id': 'CA-P-1', 'version': 1}}))
            await asyncio.wait_for(waiting.wait(), 5)
            task.cancel()
            with self.assertRaises(asyncio.CancelledError):
                await task
            other = {'sourceCurrent': {'ref_id': 'CA-P-2', 'version': 1}}
            self.assertEqual({'status': 'completed'}, await self.invoke(self.a, name, other))
            self.assertEqual((other, {}), calls[-1])

    async def test_promotion_unbound_fields_are_reported_as_target(self):
        token = object()
        value = {'outcome': 'needs_input', 'pending_promotion': token, 'effects': [{'operation': 'archive'}],
                 'requested_input': {'relations.is_replacement_for': {'error': 'predecessor missing'},
                                     'target': {'error': 'draft needs repair'}}}
        with patch('registry_lifecycle_provider.backend.execute', return_value=value):
            result = await self.invoke(self.a, 'atom_lifecycle_update', {})
        self.assertEqual({'target'}, set(result['requested_input']))
        message = result['requested_input']['target']['error']
        self.assertIn('predecessor missing', message)
        self.assertIn('draft needs repair', message)

    async def test_failed_promotion_reports_prior_effects_and_does_not_retry(self):
        token = object()
        effects = [{'operation': 'archive'}]
        calls = []
        def execute(_selection, _model, _name, params, **kwargs):
            calls.append((params, kwargs))
            if len(calls) == 1:
                return {'outcome': 'needs_input', 'pending_promotion': token, 'effects': effects,
                        'requested_input': {'target': {'error': 'repair'}}}
            return {'outcome': 'failed', 'effects': effects, 'warnings': ['prior'],
                    'errors': [{'code': 'source_changed'}]}
        with patch('registry_lifecycle_provider.backend.execute', side_effect=execute):
            await self.invoke(self.a, 'atom_lifecycle_update', {'sourceCurrent': {'ref_id': 'CA-P-1', 'version': 1}})
            result = await self.invoke(self.a, 'atom_lifecycle_update', {})
            self.assertEqual('failed', result['status'])
            self.assertEqual(effects, result['effects'])
            self.assertEqual(['prior'], result['warnings'])
            self.assertEqual(({}, {'pending_promotion': token}), calls[-1])
            self.assertEqual(2, len(calls))

    async def test_pending_promotion_form_accept_and_cancel_preserve_effects(self):
        from mcp import types
        from mcp.client._memory import InMemoryTransport
        from mcp.client.session import ClientSession
        from mcp.server import Server

        for action in ('accept', 'cancel'):
            token, calls = object(), []
            effects, warnings = [{'operation': 'archive'}], ['warning']
            def execute(_selection, _model, _name, params, **kwargs):
                calls.append((params, kwargs))
                if len(calls) == 1:
                    return {'outcome': 'needs_input', 'pending_promotion': token, 'effects': effects,
                            'warnings': warnings, 'requested_input': {'targetStatus': {'error': 'select status'}}}
                return {'outcome': 'completed', 'errors': []}
            async def call(context, request):
                args = self.provider.prepare_arguments(request.name, request.arguments or {}, context)
                return types.CallToolResult(content=[], structured_content=await self.provider.call(request.name, args))
            async def elicit(_context, _request):
                return types.ElicitResult(action=action, content={'targetStatus': 'Active'} if action == 'accept' else None)
            async def list_tools(_context, _request):
                return types.ListToolsResult(tools=list(tool_descriptors()))
            server = Server('promotion-form-test', on_call_tool=call, on_list_tools=list_tools)
            async with InMemoryTransport(server, raise_exceptions=True) as streams:
                async with ClientSession(*streams, elicitation_callback=elicit) as client:
                    await client.initialize()
                    with patch('registry_lifecycle_provider.backend.execute', side_effect=execute):
                        result = (await client.call_tool('atom_lifecycle_update', {'sourceCurrent': {}})).structured_content
                        if action == 'accept':
                            self.assertEqual({'status': 'completed'}, result)
                            self.assertEqual(({'targetStatus': 'Active'}, {'pending_promotion': token}), calls[-1])
                        else:
                            self.assertEqual({'status': 'cancelled', 'effects': effects, 'warnings': warnings}, result)
                            self.assertEqual(1, len(calls))

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

    async def test_native_form_accept_cancel_and_fallback(self):
        from mcp import types
        from mcp.client._memory import InMemoryTransport
        from mcp.client.session import ClientSession
        from mcp.server import Server

        for case in ('accept', 'integer', 'cancel', 'unsupported', 'object'):
            calls, forms = [], []
            name = 'atom_lifecycle_update'
            def execute(_selection, _model, _name, params, **kwargs):
                calls.append((params, kwargs))
                if len(calls) == 1:
                    field = {'object': 'sourceCurrent', 'integer': 'tier'}.get(case, 'priority')
                    return {'outcome': 'needs_input', 'requested_input': {
                        field: {'error': 'invalid'}}, 'pending_source': 'original', 'effects': []}
                return {'outcome': 'completed', 'errors': []}
            async def call(context, request):
                args = self.provider.prepare_arguments(request.name, request.arguments or {}, context)
                return types.CallToolResult(content=[], structured_content=await self.provider.call(request.name, args))
            async def elicit(_context, request):
                forms.append(request.requested_schema)
                self.assertEqual(1, len(calls))
                correction = {'accept': {'priority': 'High'}, 'integer': {'tier': 3}}.get(case)
                return types.ElicitResult(action='accept' if correction else 'cancel', content=correction)
            async def list_tools(_context, _request):
                return types.ListToolsResult(tools=list(tool_descriptors()))
            server = Server('lifecycle-form-test', on_call_tool=call, on_list_tools=list_tools)
            async with InMemoryTransport(server, raise_exceptions=True) as streams:
                callback = None if case == 'unsupported' else elicit
                async with ClientSession(*streams, elicitation_callback=callback) as client:
                    await client.initialize()
                    with patch('registry_lifecycle_provider.backend.execute', side_effect=execute):
                        result = await client.call_tool(name, {'sourceCurrent': {'ref_id': 'CA-R-1', 'version': 1}})
                        self.assertEqual({'accept': 'completed', 'integer': 'completed', 'cancel': 'cancelled',
                                          'unsupported': 'needs_input', 'object': 'needs_input'}[case],
                                         result.structured_content['status'])
                        self.assertEqual(1 if case in ('accept', 'integer', 'cancel') else 0, len(forms))
                        if case in ('accept', 'integer'):
                            expected = {'tier': 3} if case == 'integer' else {'priority': 'High'}
                            self.assertEqual(expected, calls[1][0]['changes'])
                            self.assertEqual({'pending_source': 'original'}, calls[1][1])
                        else:
                            self.assertEqual(1, len(calls))

    async def test_transport_cancellation_interrupts_form_wait(self):
        from mcp import types
        from mcp.client._memory import InMemoryTransport
        from mcp.client.session import ClientSession
        from mcp.server import Server

        waiting, interrupted = asyncio.Event(), asyncio.Event()
        seen = []
        def execute(*args, **kwargs):
            seen.append(1)
            return {'outcome': 'needs_input', 'requested_input': {'form': {'error': 'required'}}, 'effects': []}
        async def call(context, request):
            seen.append(context.request_id)
            try:
                args = self.provider.prepare_arguments(request.name, request.arguments or {}, context)
                value = await self.provider.call(request.name, args)
                return types.CallToolResult(content=[], structured_content=value)
            except asyncio.CancelledError:
                interrupted.set()
                raise
        async def elicit(_context, _request):
            waiting.set()
            await asyncio.Event().wait()
        server = Server('lifecycle-cancel-test', on_call_tool=call)
        async with InMemoryTransport(server, raise_exceptions=True) as streams:
            async with ClientSession(*streams, elicitation_callback=elicit) as client:
                await client.initialize()
                with patch('registry_lifecycle_provider.backend.execute', side_effect=execute):
                    task = asyncio.create_task(client.call_tool(self.name, {}))
                    await asyncio.wait_for(waiting.wait(), 5)
                    await client.send_notification(types.CancelledNotification(
                        params=types.CancelledNotificationParams(requestId=seen[0], reason='cancel')))
                    await asyncio.wait_for(interrupted.wait(), 5)
                    self.assertEqual(2, len(seen))
                    task.cancel()
                    try:
                        await task
                    except asyncio.CancelledError:
                        pass

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

        provider = LifecycleProvider(SimpleNamespace(selection=SimpleNamespace(root=Path('/project'), instance_id='project-1')), object())
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
        with patch('registry_lifecycle_provider.backend.execute', side_effect=execute), TestClient(app, base_url="http://localhost:8000") as client:
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
