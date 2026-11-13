# CA-E-815@2
# CA-E-824@3
"""Live lifecycle Run ownership."""
import asyncio
from pathlib import Path
from types import SimpleNamespace
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch
import sys

MCP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(MCP), str(MCP.parent), str(MCP.parent / 'FEATURE_TOOLS')]
from mcp.server.connection import Connection
from mcp.server.session import ServerSession
from registry_lifecycle_provider import LifecycleProvider, _PROJECT_RUNS
from runtime_request_context import RuntimeRequestContext, bind_request_context
from health_observations import HealthObservations
from workbench_tools import RUN, SYNC_STATUS, WorkbenchTools


class LiveRunsTests(IsolatedAsyncioTestCase):
    def setUp(self):
        _PROJECT_RUNS.clear()
        self.selection = SimpleNamespace(root=Path('/project'), instance_id='one', declaration_digest='initial')
        self.provider = LifecycleProvider(SimpleNamespace(selection=self.selection), object())
        self.session = ServerSession.__new__(ServerSession)
        self.session._connection = Connection.__new__(Connection)
        self.refresh = patch('registry_lifecycle_provider._refresh_selection', side_effect=lambda selection: selection)
        self.refresh.start()
        self.addCleanup(self.refresh.stop)
        self.addCleanup(_PROJECT_RUNS.clear)

    async def call(self, provider, session_id, name, args):
        with bind_request_context(RuntimeRequestContext(session_id=session_id)):
            prepared = provider.prepare_arguments(name, args, SimpleNamespace(session=self.session))
            return await provider.call(name, prepared)

    async def test_project_owner_session_listing_and_cross_session_continuation(self):
        name = 'atom_lifecycle_update'
        missing = {'outcome': 'needs_input', 'requested_input': {'priority': {'error': 'required'}}, 'effects': []}
        with patch('registry_lifecycle_provider.backend.execute', side_effect=[missing, {'outcome': 'completed'}]) as execute:
            first = await self.call(self.provider, 'a', name, {'sourceCurrent': {'ref_id': 'CA-P-1', 'version': 1}})
            run_id = first['run_id']
            other_provider = LifecycleProvider(SimpleNamespace(selection=self.selection), object())
            self.assertEqual([], (await self.call(other_provider, 'b', 'lifecycle_run_list', {}))['runs'])
            listed = (await self.call(other_provider, 'b', 'lifecycle_run_list', {'project_wide': True}))['runs']
            self.assertEqual((run_id, 'a'), (listed[0]['run_id'], listed[0]['session_id']))
            result = await self.call(other_provider, 'b', 'lifecycle_run_continue', {'run_id': run_id, 'inputs': {'priority': 'High'}})
            self.assertEqual({'status': 'completed'}, result)
            self.assertEqual('High', execute.call_args.args[3]['changes']['priority'])
            self.assertEqual([], (await self.call(self.provider, 'a', 'lifecycle_run_list', {}))['runs'])
            self.assertEqual('failed', (await self.call(self.provider, 'a', 'lifecycle_run_cancel', {'run_id': run_id}))['status'])

    async def test_project_isolation_conflict_and_cancel(self):
        missing = {'outcome': 'needs_input', 'requested_input': {'targetStatus': {'error': 'required'}}, 'effects': []}
        with patch('registry_lifecycle_provider.backend.execute', return_value=missing) as execute:
            args = {'target': {'ref_id': 'CA-P-1', 'version': 1}}
            first = await self.call(self.provider, 'a', 'atom_lifecycle_change_status', args)
            blocked = await self.call(self.provider, 'b', 'atom_lifecycle_archive', args)
            self.assertEqual('blocked', blocked['status'])
            execute.assert_called_once()
            other = LifecycleProvider(SimpleNamespace(selection=SimpleNamespace(root=Path('/other'), instance_id='two', declaration_digest='initial')), object())
            self.assertEqual('failed', (await self.call(other, 'a', 'lifecycle_run_cancel', {'run_id': first['run_id']}))['status'])
            self.assertEqual('cancelled', (await self.call(self.provider, 'b', 'lifecycle_run_cancel', {'run_id': first['run_id']}))['status'])
            self.assertEqual('needs_input', (await self.call(self.provider, 'b', 'atom_lifecycle_change_status', args))['status'])

    async def test_unknown_fields_do_not_execute_and_reserve_target(self):
        with patch('registry_lifecycle_provider.backend.execute') as execute:
            first = await self.call(self.provider, 'a', 'atom_lifecycle_archive', {'target': {'ref_id': 'CA-P-1'}, 'bad': 2})
            self.assertEqual('bad', first['errors'][0]['field'])
            self.assertEqual('blocked', (await self.call(self.provider, 'b', 'atom_lifecycle_archive', {'target': {'ref_id': 'CA-P-1'}}))['status'])
            execute.assert_not_called()

    async def test_disconnect_during_project_refresh_releases_the_target(self):
        name = 'atom_lifecycle_archive'
        args = {'target': {'ref_id': 'CA-P-1', 'version': 1}}
        with patch('registry_lifecycle_provider.anyio.to_thread.run_sync', side_effect=asyncio.CancelledError):
            with self.assertRaises(asyncio.CancelledError):
                await self.call(self.provider, 'a', name, args)

        self.assertEqual({'runs': []}, await self.call(self.provider, 'b', 'lifecycle_run_list', {'project_wide': True}))
        with patch('registry_lifecycle_provider.backend.execute', return_value={'outcome': 'completed'}):
            self.assertEqual({'status': 'completed'}, await self.call(self.provider, 'b', name, args))

    async def test_workbench_gets_project_snapshot_at_submission(self):
        project = (self.selection.root, self.selection.instance_id)
        _PROJECT_RUNS[project] = {'r1': {'session_id': 'a', 'name': 'atom_lifecycle_update',
                                       'status': 'running', 'pending': {'secret': 'private'}}}
        _PROJECT_RUNS[(self.selection.root, 'other')] = {'r2': {'session_id': 'b',
                                      'name': 'other', 'status': 'needs_input'}}
        owner = WorkbenchTools(self.selection.root, selection=self.selection)
        service = SimpleNamespace(set_live_runs=lambda rows: captured.extend(rows),
                                  run=lambda *args, **kwargs: {'ok': True})
        owner._service = service
        captured = []

        async def dispatch(fn, *args):
            _PROJECT_RUNS[project].clear()
            return fn(*args)

        with patch('workbench_tools.asyncio.to_thread', side_effect=dispatch):
            self.assertEqual({'ok': True}, await owner.call(RUN, {'sql': 'select 1'}))
        self.assertEqual([{'run_id': 'r1', 'session_id': 'a', 'tool': 'atom_lifecycle_update',
                           'status': 'running'}], captured)

    async def test_workbench_uses_only_bound_safe_diagnostics(self):
        observations, other = HealthObservations(), HealthObservations()
        observations.record('query_run', {'sql': 'private sql'}, {'status': 'completed'})
        other.record('other_project', {}, {'status': 'failed'})
        captured = []
        owner = WorkbenchTools(self.selection.root, diagnostics_snapshot=observations.snapshot)
        owner._service = SimpleNamespace(set_runtime_diagnostics=lambda rows: captured.extend(rows),
                                         run=lambda *args, **kwargs: {'ok': True})
        await owner.call(RUN, {'sql': 'select 1'})
        self.assertEqual(['query_run'], [row['name'] for row in captured])
        self.assertEqual('completed', captured[0]['outcome'])
        self.assertNotIn('private sql', repr(captured))
        owner._service = None
        owner._diagnostics_snapshot = lambda: self.fail('unrelated tool read diagnostics')
        await owner.call(SYNC_STATUS, {})
