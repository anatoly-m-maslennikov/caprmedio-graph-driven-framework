# CA-E-681@7
# CA-E-821@2
# CA-E-681@6
"""Isolated Project proof of scoped Archive loading and deferred audits."""
from __future__ import annotations

from contextlib import asynccontextmanager
from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
from pathlib import Path
import sys
import tempfile
import threading
import time
import unittest
from unittest.mock import patch

import httpx2
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamable_http_client
from watchdog.observers.polling import PollingObserver

APP_ROOT = Path(__file__).resolve().parents[2]
PROGRAMMATIC = APP_ROOT.parent
TOOLS = PROGRAMMATIC / 'FEATURE_TOOLS'
MCP = PROGRAMMATIC / 'FEATURE_MCP'
sys.path[:0] = [str(APP_ROOT), str(TOOLS), str(TOOLS / 'tests'), str(MCP), str(Path(__file__).parent)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.audit_tables import TABLES  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.audit_worker import AuditSnapshot  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService  # noqa: E402
from direct_gateway import startup_selection  # noqa: E402
from generate_tool_registry import _provider_payload  # noqa: E402
from http_paths import HEALTH_PATH, MCP_PATH, WORKBENCH_PATH  # noqa: E402
from http_server import create_app  # noqa: E402
from lifecycle_placement_test_support import fixture_rules  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from smalltest_support import built_assets, extension_directory, source_path, write_atom, write_settings  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext  # noqa: E402
from ATOM_LIFECYCLE.source import ArchiveNotLoadedError  # noqa: E402
from workbench_tools import WorkbenchTools  # noqa: E402
import tool_registry_runtime  # noqa: E402


class Fixture:
    def __init__(self, root: Path):
        self.root = root
        control = write_settings(root)
        self.declarations = write_scope_unit_declarations(root, (
            {'scope_unit_name': 'ENGINE', 'scope_unit_type': 'Ordered', 'scope_unit_label': 'LAYER', 'local_order': 1},
            {'scope_unit_name': 'OTHER', 'scope_unit_type': 'Ordered', 'scope_unit_label': 'LAYER', 'local_order': 2},
            {'scope_unit_name': 'ENGINE_CHILD', 'scope_unit_type': 'Unordered', 'scope_unit_label': 'FEATURE',
             'parent': 'ENGINE'},
        ), control_root=control)
        self.atom('ENGINE', '04_requirement', 'CA-R-710-current.md', 'CA-R-710')
        self.atom('ENGINE', '04_requirement/draft', 'CA-R-711@1-draft.md', 'CA-R-711', status='Draft')
        self.atom('ENGINE', '04_requirement/backlog', 'CA-R-712-backlog.md', 'CA-R-712', status='Backlog')
        self.atom('ENGINE', '04_requirement/archive', 'CA-R-713@1-old.md', 'CA-R-713', status='Archived')
        self.atom('ENGINE', '05_method/archive', 'CA-M-714@1-old.md', 'CA-M-714', status='Archived', role='Method')
        self.atom('OTHER', '04_requirement/archive', 'CA-R-715@1-old.md', 'CA-R-715', status='Archived')
        self.atom('ENGINE_CHILD', '04_requirement/archive', 'CA-R-718@1-old.md', 'CA-R-718', status='Archived')

    def atom(self, scope, folder, filename, identity, *, status='Active', role='Requirement'):
        path = source_path(self.declarations, scope, folder, filename)
        write_atom(path, identity, status=status)
        if role != 'Requirement':
            path.write_text(path.read_text().replace('role: "Requirement"', f'role: "{role}"'))
        return path

    def service(self):
        return WorkbenchService(self.root, extension_directory=extension_directory(APP_ROOT.parents[2]),
                                archive_placement=fixture_rules(), **built_assets(self.root))


def rows(service):
    return service.run("SELECT reference, status_group FROM atoms WHERE reference LIKE 'CA-%-71%' ORDER BY reference",
                       result_delivery='inline')['rows']


def idle(service, timeout=10):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        status = service.sync_status()
        if not status['audits_pending'] and status['last_audit_ms'] is not None:
            return status
        time.sleep(.02)
    raise AssertionError(f'audits did not finish: {service.sync_status()!r}')


class ArchiveLoadingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = (Path(self.temp.name) / 'project').resolve()
        root.mkdir()
        self.fixture = Fixture(root)
        observer = patch('APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_watcher.NativeObserver', PollingObserver)
        observer.start()
        self.addCleanup(observer.stop)
        self.service = self.fixture.service()
        self.addCleanup(self.service.close)

    def test_cold_start_loads_active_draft_and_backlog_then_exact_archive_pair(self):
        initial = rows(self.service)
        self.assertEqual(['CA-R-710', 'CA-R-711@1-draft', 'CA-R-712'], [row[0] for row in initial])
        self.assertNotIn('Archived', [row[1] for row in initial])
        request = [{'scope_unit': 'ENGINE', 'role': 'Requirement'}]
        loaded = self.service.load_archives(request)
        self.assertEqual(request, loaded['loaded_archive_scopes'])
        self.assertEqual(['CA-R-710', 'CA-R-711@1-draft', 'CA-R-712', 'CA-R-713@1'],
                         [row[0] for row in rows(self.service)])
        self.assertEqual(loaded['loaded_archive_scopes'], self.service.load_archives(request)['loaded_archive_scopes'])
        self.assertEqual(1, sum(row[0] == 'CA-R-713@1' for row in rows(self.service)))
        self.assertFalse({'CA-M-714@1', 'CA-R-715@1', 'CA-R-718@1'} & {row[0] for row in rows(self.service)})

    def test_load_scope_includes_legacy_archive_folder(self):
        placement = replace(fixture_rules(), _archive_aliases={})
        self.service._archive_placement = placement
        self.service._reader._archive_placement = placement
        legacy = self.fixture.atom('ENGINE', '04_requirement/archive',
                                   'CA-R-719@2-old.md', 'CA-R-719', status='Archived')
        legacy.write_text(legacy.read_text().replace('atom_id: "CA-R-719"', 'atom_id: "CA-R-719@2"')
                          .replace('version: 1', 'version: 2'))
        self.service.run('SELECT count(*) FROM atoms', result_delivery='inline')
        selection = startup_selection(self.fixture.root)
        with self.assertRaises(ArchiveNotLoadedError):
            self.service.lifecycle_archive_candidates(selection, 'CA-R-719')
        self.service.load_archives([{'scope_unit': 'ENGINE', 'role': 'Requirement'}])
        self.assertIn(('CA-R-719@2', legacy), self.service.lifecycle_archive_candidates(selection, 'CA-R-719'))

    def test_cold_start_does_not_read_a_large_archive_inventory(self):
        for index in range(200):
            atom_id = f'CA-R-{800000 + index}'
            self.fixture.atom('OTHER', '04_requirement/archive', f'{atom_id}@1-old.md',
                              atom_id, status='Archived')
        original = ReadContext.read

        def no_archive_reads(reader, path, *args, **kwargs):
            if 'archive' in {part.casefold() for part in Path(path).parts}:
                raise AssertionError('cold start read an Archive carrier')
            return original(reader, path, *args, **kwargs)

        started = time.monotonic()
        with patch.object(ReadContext, 'read', no_archive_reads):
            initial = rows(self.service)
        elapsed = time.monotonic() - started
        self.assertNotIn('Archived', [row[1] for row in initial])
        self.assertLess(elapsed, 15, f'small fixture cold start took {elapsed:.2f}s')
        print(f'cold start with 200 unloaded Archive carriers: {elapsed:.3f}s')

    def test_audit_wait_does_not_block_lifecycle_refresh_and_audit_tables_remain_queryable(self):
        rows(self.service)
        idle(self.service)
        entered, release = threading.Event(), threading.Event()
        self.addCleanup(release.set)
        store = self.service._store
        original = AuditSnapshot.collect

        def slow_audit(snapshot, *args, **kwargs):
            entered.set()
            if not release.wait(10):
                raise RuntimeError('audit fixture was not released')
            return original(snapshot, *args, **kwargs)

        new = source_path(self.fixture.declarations, 'ENGINE', '04_requirement', 'CA-R-716-new.md')
        with store._lock:
            for table in TABLES:
                store._connection.execute(
                    f'INSERT INTO {table} (relative_path, filename, issue_category) VALUES (?, ?, ?)',
                    [new.parent.relative_to(self.fixture.root).as_posix(), new.name, 'fixture_stale'],
                )
        with patch.object(AuditSnapshot, 'collect', new=slow_audit), ThreadPoolExecutor() as executor:
            self.fixture.atom('ENGINE', '04_requirement', new.name, 'CA-R-716')
            self.service.lifecycle_changed(None, new)
            action = executor.submit(self.service._flush_lifecycle_changes)
            try:
                self.assertTrue(entered.wait(5), 'background audit did not start')
                action.result(timeout=2)
                status = self.service.sync_status()
                self.assertTrue(status['audits_pending'])
                self.assertEqual([['CA-R-716']], self.service.run(
                    "SELECT reference FROM atoms WHERE reference = 'CA-R-716'", result_delivery='inline')['rows'])
            finally:
                release.set()
        status = idle(self.service)
        self.assertGreaterEqual(status['last_audit_ms'], 0)
        for table in TABLES:
            self.assertEqual([[0]], self.service.run(
                f"SELECT count(*) FROM {table} WHERE issue_category = 'fixture_stale'",
                result_delivery='inline')['rows'], table)


class FixtureTools(WorkbenchTools):
    def __init__(self, fixture):
        super().__init__(fixture.root)
        self.fixture = fixture

    def _owner(self):
        if self._service is None:
            self._service = self.fixture.service()
        return self._service


class ArchiveTransportTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = (Path(self.temp.name) / 'project').resolve()
        root.mkdir()
        fixture = Fixture(root)
        observer = patch('APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_watcher.NativeObserver', PollingObserver)
        observer.start()
        self.addCleanup(observer.stop)
        self.app = create_app(root, selection=startup_selection(root))
        self.app.gateway.workbench = FixtureTools(fixture)
        self.addAsyncCleanup(self.app.gateway.workbench.close)
        original = tool_registry_runtime._registry

        def generated_registry(asset_root, inventory):
            value = original(asset_root, inventory)
            value['providers'] = [_provider_payload(asset_root, entry)[0] for entry in inventory.providers]
            value['public_tools'] = [tool['name'] for provider in value['providers'] for tool in provider['tools']
                                     if tool['name'] not in inventory.blacklist]
            return value

        registry = patch.object(tool_registry_runtime, '_registry', side_effect=generated_registry)
        registry.start()
        self.addCleanup(registry.stop)

    @asynccontextmanager
    async def session(self):
        async with self.app.starlette_app.router.lifespan_context(self.app.starlette_app):
            async with httpx2.AsyncClient(transport=httpx2.ASGITransport(app=self.app),
                                          base_url='http://127.0.0.1:18093') as client:
                async with streamable_http_client('http://127.0.0.1:18093' + MCP_PATH, http_client=client) as streams:
                    async with ClientSession(*streams) as session:
                        await session.initialize()
                        yield session, client

    async def test_http_and_mcp_load_the_same_project_service(self):
        async with self.session() as (session, client):
            tools = {tool.name for tool in (await session.list_tools()).tools}
            self.assertIn('workbench_archive_load', tools)
            scopes = [{'scope_unit': 'ENGINE', 'role': 'Requirement'}]
            response = await session.call_tool('workbench_archive_load', {'scopes': scopes})
            self.assertFalse(response.is_error, response.structured_content)
            self.assertEqual(scopes, response.structured_content['loaded_archive_scopes'])
            response = await client.post(f'{WORKBENCH_PATH}/fixture/archive-load', json={'scopes': scopes})
            self.assertEqual(200, response.status_code, response.text)
            self.assertEqual(scopes, response.json()['loaded_archive_scopes'])
            query = await session.call_tool('query_run', {
                'sql': "SELECT reference FROM atoms WHERE reference LIKE 'CA-R-71%@1' ORDER BY reference",
                'result_delivery': 'inline',
            })
            self.assertFalse(query.is_error, query.structured_content)
            self.assertEqual([['CA-R-713@1']], query.structured_content['rows'])

    async def test_mcp_and_health_reread_restore_selected_archive_scopes(self):
        scopes = [
            {'scope_unit': 'ENGINE', 'role': 'Requirement'},
            {'scope_unit': 'OTHER', 'role': 'Method'},
        ]
        async with self.session() as (session, client):
            async def assert_archives(expected_scopes, expected_rows):
                status = await session.call_tool('workbench_status', {})
                self.assertFalse(status.is_error, status.structured_content)
                self.assertEqual(expected_scopes, status.structured_content['loaded_archive_scopes'])
                query = await session.call_tool('query_run', {
                    'sql': "SELECT reference FROM atoms WHERE status_group = 'Archived' ORDER BY reference",
                    'result_delivery': 'inline',
                })
                self.assertFalse(query.is_error, query.structured_content)
                self.assertEqual(expected_rows, query.structured_content['rows'])

            await assert_archives([], [])
            loaded = await session.call_tool('workbench_archive_load', {'scopes': scopes})
            self.assertFalse(loaded.is_error, loaded.structured_content)
            await assert_archives(scopes, [['CA-R-713@1']])

            reread = await session.call_tool('workbench_reread', {})
            self.assertFalse(reread.is_error, reread.structured_content)
            self.assertEqual('ready', reread.structured_content['status'])
            await assert_archives(scopes, [['CA-R-713@1']])

            health = await client.post(f'{HEALTH_PATH}/workbench-reread', headers={'accept': 'text/html'})
            self.assertEqual(200, health.status_code, health.text)
            self.assertIn('Workbench is ready.', health.text)
            await assert_archives(scopes, [['CA-R-713@1']])

            restart = await session.call_tool('workbench_restart', {})
            self.assertFalse(restart.is_error, restart.structured_content)
            await assert_archives([], [])
