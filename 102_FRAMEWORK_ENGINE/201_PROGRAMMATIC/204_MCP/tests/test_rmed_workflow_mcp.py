"""Real stdio protocol with mock Atoms; no live review or Agent dispatch."""
from contextlib import asynccontextmanager, redirect_stderr
import io
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from mcp import Client, StdioServerParameters
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
from frozen_selected_workflows import (  # noqa: E402
    frozen_behavior_bindings,
    frozen_selected_root_paths,
    frozen_source_bytes,
    write_frozen_source,
)


# CA-D-548's eight stable helpers plus its gateway controls remain required.
D548_REQUIRED_TOOLS = frozenset({
    'rmed_atoms_base_revise', 'discover_tools', 'discover_operations',
    'get_execution_context', 'get_execution_status',
    'resume_execution_context', 'watch_execution', 'workflow_orchestrator',
    'reload_mcp_implementation', 'get_mcp_reload_status',
})

# CA-D-547 v5 is the reviewed admission boundary.  This independently fixed
# tuple prevents the registration registry from making its own test pass.
D547_ADMITTED_SELECTED_ROUTES = (
    'create_atom', 'update_atom', 'replace_atom', 'change_atom_status',
    'create_scope_unit', 'rename_scope_unit', 'move_scope_unit', 'remove_scope_unit',
    'run_implementation_workflow', 'revert_changes', 'build_entities_graph',
    'build_terms_graph', 'build_applicable_methodology',
    'find_and_fetch_artifacts', 'find_and_fetch_journal_events',
)
D547_SELECTED_CONTROL_TOOLS = frozenset({
    'get_selected_workflow_run', 'get_selected_action_run',
})
D547_DIRECT_RELEASE_TOOLS = frozenset({'release_version', 'public.release'})

HELPER_DECLARATION_IDS = (
    'CA-D-512', 'CA-D-513', 'CA-D-514', 'CA-D-515', 'CA-D-516', 'CA-D-517',
    'CA-D-518', 'CA-D-551', 'CA-D-557',
)

# The stable gateway first boots an isolated implementation generation.  The
# source tree is intentionally cold in sealed Unit runs, so allow that bounded
# startup before the MCP client's first protocol probe expires.
GATEWAY_STARTUP_TIMEOUT_SECONDS = 30
_STARTUP_TELEMETRY_LINE = re.compile(
    r'^caprmedio_mcp_startup phase=(?:initial_fingerprint|reload_fingerprint|fingerprint_verify|'
    r'child_handshake|list_tools|generation_ready|schema_validation|implementation_import|'
    r'selected_registration|catalog|catalog_registration) '
    r'outcome=(?:completed|failed) elapsed_ms=[0-9]+$')


def _forward_startup_telemetry(stderr):
    """Expose only accepted opt-in timing records after a successful client run."""
    if os.environ.get('CAPRMEDIO_STARTUP_TELEMETRY') != '1':
        return
    stderr.seek(0)
    for line in stderr.read().splitlines():
        if _STARTUP_TELEMETRY_LINE.fullmatch(line):
            print(line, file=sys.stderr, flush=True)


class InstalledLayoutImport(unittest.TestCase):
    def test_startup_telemetry_forwarding_is_opt_in_and_filters_untrusted_stderr(self):
        valid = 'caprmedio_mcp_startup phase=list_tools outcome=completed elapsed_ms=17'
        captured = io.StringIO(f'{valid}\n/secret/path --project-root source-content\n')
        forwarded = io.StringIO()
        with patch.dict(os.environ, {'CAPRMEDIO_STARTUP_TELEMETRY': '1'}), redirect_stderr(forwarded):
            _forward_startup_telemetry(captured)
        self.assertEqual(forwarded.getvalue(), valid + '\n')

        captured = io.StringIO(valid + '\n')
        forwarded = io.StringIO()
        with patch.dict(os.environ, {}, clear=False), redirect_stderr(forwarded):
            os.environ.pop('CAPRMEDIO_STARTUP_TELEMETRY', None)
            _forward_startup_telemetry(captured)
        self.assertEqual(forwarded.getvalue(), '')

    def test_implementation_imports_from_framework_engine_layout(self):
        """The release copies the Engine without the source-tree numeric prefix."""
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as temporary:
            installed = Path(temporary) / 'opt/caprmedio-framework/FRAMEWORK_ENGINE'
            shutil.copytree(ROOT / '102_FRAMEWORK_ENGINE/201_PROGRAMMATIC',
                            installed / '201_PROGRAMMATIC',
                            ignore=shutil.ignore_patterns('__pycache__', '.caprmedio_tmp'))
            shutil.copytree(ROOT / '102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/RMED_ATOM_REVIEW',
                            installed / '202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/RMED_ATOM_REVIEW',
                            ignore=shutil.ignore_patterns('__pycache__', '.mypy_cache'))
            implementation = installed / '201_PROGRAMMATIC/204_MCP/implementation_server.py'
            result = subprocess.run([sys.executable, '-B', '-c',
                                     'import runpy, sys; sys.path.insert(0, ' +
                                     repr(str(implementation.parent)) +
                                     '); runpy.run_path(' + repr(str(implementation)) + ')'],
                                    capture_output=True, text=True)
            self.assertEqual(0, result.returncode, result.stderr)


class MCPWorkflow(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        # The sealed Unit mounts the repository read-only; the runner supplies
        # a writable per-module TMPDIR for disposable protocol fixtures.
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

    def _copy_declared_selected_manifest(self):
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

    def _server_parameters(self):
        telemetry = ({'CAPRMEDIO_STARTUP_TELEMETRY': '1'}
                     if os.environ.get('CAPRMEDIO_STARTUP_TELEMETRY') == '1' else None)
        return StdioServerParameters(command=sys.executable,
            args=[str(SERVER), '--project-root', str(self.root)], env=telemetry)

    @asynccontextmanager
    async def _server_client(self, *, cache=None):
        """Attach bounded server stderr to an otherwise opaque startup failure."""
        with tempfile.TemporaryFile(mode='w+', encoding='utf-8') as stderr:
            try:
                # ClientSession.send_discover deliberately uses its own ten-second
                # probe constant, rather than Client.read_timeout_seconds.  The
                # gateway's initial child-generation preparation is separately
                # bounded at twenty seconds, so give this cold-start-only probe
                # the existing bounded test startup allowance.
                with (patch.dict(os.environ, {'CAPRMEDIO_STARTUP_TELEMETRY': '1'}),
                      patch('mcp.client.session.DISCOVER_TIMEOUT_SECONDS',
                            GATEWAY_STARTUP_TIMEOUT_SECONDS)):
                    async with Client(stdio_client(self._server_parameters(), errlog=stderr), cache=cache,
                                      read_timeout_seconds=GATEWAY_STARTUP_TIMEOUT_SECONDS) as client:
                        yield client
            except BaseException as error:
                # The complete suite must retain safe phase evidence on a
                # startup failure, even when ordinary successful runs are quiet.
                with patch.dict(os.environ, {'CAPRMEDIO_STARTUP_TELEMETRY': '1'}):
                    _forward_startup_telemetry(stderr)
                stderr.seek(0)
                detail = stderr.read()[-4096:]
                if detail:
                    raise AssertionError(f'MCP stdio startup failed; stderr follows:\n{detail}') from error
                raise
            else:
                _forward_startup_telemetry(stderr)

    async def test_real_server_discovery_marks_registered_query_bindings_mcp_available(self):
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

    async def test_startup_failure_retains_safe_timing_without_global_opt_in(self):
        valid = 'caprmedio_mcp_startup phase=child_handshake outcome=failed elapsed_ms=20000'

        def captured_transport(parameters, *, errlog):
            self.assertEqual(parameters.env['CAPRMEDIO_STARTUP_TELEMETRY'], '1')
            errlog.write(valid + '\nUNTRUSTED_DIAGNOSTIC_CONTENT\n')
            errlog.flush()
            return object()

        forwarded = io.StringIO()
        with (patch.dict(os.environ, {}, clear=False), redirect_stderr(forwarded),
              patch(__name__ + '.stdio_client', captured_transport),
              patch(__name__ + '.Client', side_effect=RuntimeError('mock readiness failure'))):
            os.environ.pop('CAPRMEDIO_STARTUP_TELEMETRY', None)
            with self.assertRaises(AssertionError):
                async with self._server_client():
                    self.fail('failed startup cannot yield a client')
        self.assertEqual(forwarded.getvalue(), valid + '\n')

    async def test_stdio_gather_check_fix_report(self):
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

            async def call(**request):
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

    async def test_protocol_rejects_unknown_fields_and_path_escape(self):
        async with self._server_client() as client:
            for request in ({'operation': 'describe', 'surprise': True},
                            {'operation': 'status', 'run_id': '../escape'}):
                result = await client.call_tool('rmed_atoms_base_revise', {'request': request})
                self.assertTrue(result.is_error)


if __name__ == '__main__':
    unittest.main()
