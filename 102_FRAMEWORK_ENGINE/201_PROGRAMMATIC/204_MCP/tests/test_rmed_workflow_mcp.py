# implementation of:
# Method: CA-M-395, CA-M-431
# Evaluation: CA-E-567
from contextlib import asynccontextmanager, redirect_stderr
import io
import os
from pathlib import Path
import sys
import tempfile
import unittest
from typing import Any
from unittest.mock import patch
from mcp import Client
from mcp.client.stdio import stdio_client
ROOT = Path(__file__).resolve().parents[4]
SERVER = ROOT / '102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py'
MCP = SERVER.parent
MCP_TESTS = MCP / 'tests'
WORKFLOW_TESTS = MCP.parent / '203_APPS/WORKFLOW_ORCHESTRATOR/tests'
sys.path.insert(0, str(MCP))
sys.path.insert(0, str(MCP_TESTS))
sys.path.insert(0, str(WORKFLOW_TESTS))
from selected_routes import QUERY_ROUTE_NAMES, SELECTED_ROUTE_NAMES  # noqa: E402
from test_selected_routes_mcp import copy_complete_selected_guard_fixture  # noqa: E402
from frozen_selected_workflows import (  # type: ignore[import-not-found]  # noqa: E402
    frozen_behavior_bindings,
    frozen_selected_root_paths,
    frozen_source_bytes,
    write_frozen_source,
)
from rmed_workflow_mcp_support import (  # noqa: E402
    D547_ADMITTED_SELECTED_ROUTES,
    D547_DIRECT_RELEASE_TOOLS,
    D547_SELECTED_CONTROL_TOOLS,
    D548_REQUIRED_TOOLS,
    HELPER_DECLARATION_IDS,
    InstalledLayoutImport,  # noqa: F401
    _forward_startup_telemetry,
    bounded_server_client,
)
class MCPWorkflow(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        (self.root / '.git').mkdir()
        control = self.root / '.caprmedio_caprmedio'
        control.mkdir()
        (control / 'caprmedio_project_settings.toml').write_text(
            '[project]\nname="caprmedio"\n[paths]\ncontrol_root=".caprmedio_caprmedio"\n'
            'journal_root=".caprmedio_caprmedio/_journal"\nruntime_root=".caprmedio_runtime"\n')
        (control / 'project_structure.toml').write_text(
            'schema_version=1\n[[scope_units]]\nscope_unit_name="CORE_META_MODEL"\n'
            'authority_path=".caprmedio_caprmedio/core"\ndelivery_path=".caprmedio_caprmedio/output"\n')
        self._copy_declared_selected_manifest()
        (self.root / 'atom.md').write_text('mock original atom')
        (self.root / 'rules.md').write_text('mock applicable criteria')

    def _copy_declared_selected_manifest(self) -> None:
        """Copy admitted route pins and the actual helper registration sources."""
        settings = self.root / '.caprmedio_caprmedio/caprmedio_project_settings.toml'
        fixture_settings = settings.read_bytes()
        try:
            copy_complete_selected_guard_fixture(self.root)
        finally:
            settings.write_bytes(fixture_settings)
        bindings = frozen_behavior_bindings()
        for atom_id in HELPER_DECLARATION_IDS:
            pin = bindings[atom_id]
            write_frozen_source(self.root, pin['source_path'], pin['sha256'])
        supplemental = bindings['CA-D-625']
        self.assertNotIn(supplemental['source_path'], frozen_selected_root_paths())
        self.assertTrue(frozen_source_bytes(supplemental['source_path'], supplemental['sha256']))
        self.assertFalse((self.root / supplemental['source_path']).exists())

    @asynccontextmanager
    async def _server_client(self, *, cache: Any | None = None) -> Any:
        async with bounded_server_client(
            self.root,
            cache=cache,
            stdio_client_factory=stdio_client,
            client_factory=Client,
            telemetry_forwarder=_forward_startup_telemetry,
        ) as client:
            yield client

    async def test_real_server_discovery_marks_registered_query_bindings_mcp_available(self) -> None:
        async with self._server_client(cache=None) as client:
            registered = {tool.name: tool for tool in (await client.list_tools()).tools}
            self.assertTrue(set(QUERY_ROUTE_NAMES) <= set(registered))
            self.assertTrue(all(registered[name].annotations.read_only_hint for name in QUERY_ROUTE_NAMES))
            discovered = await client.call_tool('discover_tools', {'request': {
                'query': 'find_and_fetch', 'availability': 'mcp'}})
            self.assertFalse(discovered.is_error, str(discovered))
            matches = discovered.structured_content['matches']
            self.assertEqual(set(QUERY_ROUTE_NAMES), {row['mcp_name'] for row in matches})
            self.assertTrue(all(row['availability'] == 'mcp' for row in matches))

    async def test_startup_failure_retains_safe_timing_without_global_opt_in(self) -> None:
        valid = 'caprmedio_mcp_startup phase=child_handshake outcome=failed elapsed_ms=20000'

        def captured_transport(parameters: Any, *, errlog: Any) -> object:
            self.assertEqual(parameters.env['CAPRMEDIO_STARTUP_TELEMETRY'], '1')
            errlog.write(valid + '\nUNTRUSTED_DIAGNOSTIC_CONTENT\n')
            errlog.flush()
            return object()

        forwarded = io.StringIO()
        with (patch.dict(os.environ, {}, clear=False), redirect_stderr(forwarded),
              patch.object(sys.modules[__name__], 'stdio_client', captured_transport),
              patch.object(sys.modules[__name__], 'Client', side_effect=RuntimeError('mock readiness failure'))):
            os.environ.pop('CAPRMEDIO_STARTUP_TELEMETRY', None)
            with self.assertRaises(AssertionError):
                async with self._server_client():
                    self.fail('failed startup cannot yield a client')
        self.assertEqual(forwarded.getvalue(), valid + '\n')

    async def test_stdio_gather_check_fix_report(self) -> None:
        async with self._server_client() as client:
            tools = await client.list_tools()
            actual_tool_names = {tool.name for tool in tools.tools}
            self.assertEqual(D547_ADMITTED_SELECTED_ROUTES, SELECTED_ROUTE_NAMES)
            self.assertTrue(D548_REQUIRED_TOOLS <= actual_tool_names)
            self.assertTrue(set(D547_ADMITTED_SELECTED_ROUTES) <= actual_tool_names)
            self.assertTrue(D547_SELECTED_CONTROL_TOOLS <= actual_tool_names)
            self.assertTrue(next(tool for tool in tools.tools if tool.name == 'find_and_fetch_artifacts').annotations.read_only_hint)
            self.assertTrue(next(tool for tool in tools.tools if tool.name == 'find_and_fetch_journal_events').annotations.read_only_hint)
            self.assertEqual(
                D548_REQUIRED_TOOLS | set(SELECTED_ROUTE_NAMES) | D547_SELECTED_CONTROL_TOOLS |
                D547_DIRECT_RELEASE_TOOLS,
                actual_tool_names,
            )
            schema = next(tool for tool in tools.tools if tool.name == 'workflow_orchestrator').input_schema
            encoded_schema = __import__('json').dumps(schema)
            self.assertIn('allow_replacements', encoded_schema)
            self.assertFalse(schema['$defs']['Enqueue']['properties']['allow_replacements']['default'])
            discovered = await client.call_tool('discover_tools', {'request': {'query': 'missing'}})
            self.assertFalse(discovered.is_error)
            self.assertEqual(discovered.structured_content['matches'], [])

            async def call(**request: Any) -> Any:
                result = await client.call_tool('rmed_atoms_base_revise', {'request': request})
                self.assertFalse(result.is_error, str(result))
                return result.structured_content

            help_result = await call(operation='describe')
            self.assertIn('gather', help_result['steps'])
            started = await call(operation='start', run_id='mcp-mock', request={'scope': 'MOCK'},
                author='mock-operator', session={'app': 'test', 'uuid': 'mock-session'}, scope='MOCK')
            self.assertEqual(started['outcome'], 'running')
            await call(operation='gather', run_id='mcp-mock',
                selection=[{'atom_id': 'MOCK-R-1', 'path': 'atom.md'}], criteria_paths=['rules.md'])
            context = await call(operation='context', run_id='mcp-mock', ordinal=0, stage='check')
            self.assertEqual(context['source_content'], 'mock original atom')
            report = {'workflow_run_id': 'mcp-mock', 'atom_id': 'MOCK-R-1',
                'source': context['source'], 'criteria_sha256': context['criteria_sha256'],
                'checks': {name: {'status': 'passed', 'evidence': 'mock quotation'} for name in
                           ('properties', 'cce', 'scope', 'claim', 'details', 'summary')},
                'findings': [{'id': 'f1', 'check': 'cce', 'evidence': 'mock quote'}],
                'blockers': [], 'corrections': [], 'unresolved_findings': [{'finding_id': 'f1'}],
                'rejected_findings': [], 'fix_blockers': [], 'result': 'issues'}
            report['checks']['cce']['status'] = 'failed'
            submitted = await call(operation='submit', run_id='mcp-mock', ordinal=0,
                                   stage='check', report=report)
            self.assertEqual(submitted['progress']['checked'], 1)
            self.assertEqual(submitted['progress']['completed'], 0)
            await call(operation='context', run_id='mcp-mock', ordinal=0, stage='fix')
            (self.root / 'atom.md').write_text('authorized mock correction')
            report.update(result='fixed_not_rechecked',
                corrections=[{'finding_id': 'f1', 'change': 'mock correction'}], unresolved_findings=[])
            await call(operation='submit', run_id='mcp-mock', ordinal=0, stage='fix',
                       report=report, after_paths=['atom.md'])
            final = await call(operation='finish', run_id='mcp-mock', outcome='completed')
            self.assertEqual(final['progress']['completed'], 1)
            self.assertEqual(final['recording_blockers'], [])
            rendered = await call(operation='report', run_id='mcp-mock')
            self.assertIn('mock quotation', rendered['markdown'])
            self.assertIn('fixed_not_rechecked', rendered['markdown'])
            self.assertTrue((self.root / final['report_path']).is_file())
            observed = await client.call_tool('get_execution_status', {'request': {
                'run_id': 'mcp-mock', 'include_results': True}})
            self.assertFalse(observed.is_error)
            self.assertEqual(observed.structured_content['outcome'], 'completed')
            self.assertEqual(observed.structured_content['results'][0]['result'], 'fixed_not_rechecked')
            watched = await client.call_tool('watch_execution', {'request': {'run_id': 'mcp-mock'}})
            self.assertFalse(watched.is_error)
            self.assertTrue(watched.structured_content['terminal'])
            replay = await client.call_tool('watch_execution', {'request': {
                'run_id': 'mcp-mock', 'cursor': watched.structured_content['cursor']}})
            self.assertEqual(replay.structured_content['notifications'], [])

    async def test_protocol_rejects_unknown_fields_and_path_escape(self) -> None:
        async with self._server_client() as client:
            for request in ({'operation': 'describe', 'surprise': True},
                            {'operation': 'status', 'run_id': '../escape'}):
                result = await client.call_tool('rmed_atoms_base_revise', {'request': request})
                self.assertTrue(result.is_error)

if __name__ == '__main__':
    unittest.main()
