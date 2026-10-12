"""Mock evidence tests; no real Workflow execution."""
import asyncio
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / 'VALIDATE_ATOMS'))
sys.path.insert(0, str(TOOLS.parent / '204_MCP'))
TESTS_ROOT = TOOLS / 'tests'
sys.path.insert(0, str(TESTS_ROOT))
from capability_discovery.service import Service, Query, Observation, Watch
from framework_package import assemble_framework_package
import framework_package as package_library
from framework_runtime_installation_mcp import input_schema as runtime_installation_input_schema
from source_admission_fixture import write_source_admission_receipt
from unittest.mock import patch


REPOSITORY_ROOT = TOOLS.parents[2]
D602_RELATIVE = Path(
    '.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/'
    '201_FEATURE_TOOLS/07_delivery/'
    'CA-D-602-TOOLS-DELIVERY--encode-admitted-package-source-catalog.md'
)
O199_RELATIVE = Path(
    '.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/'
    '003_PROJECT_CONFIGURATION/09_operations/'
    'CA-O-199-PROJECT_CONFIGURATION-ACTION--admit-local-package-sources.md'
)
O199_SOURCE = Path(
    '.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/'
    '000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/'
    'CA-O-199-PROJECT_CONFIGURATION-ACTION--admit-local-package-sources.md'
)
SOURCE_ADMISSION_ENTRYPOINT = Path(
    '102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/source_admission_mcp.py'
)
RUNTIME_INSTALLATION_DELIVERY = Path(
    '.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/'
    '204_FEATURE_MCP/07_delivery/'
    'CA-D-620-MCP-DELIVERY--expose-direct-framework-runtime-installation.md'
)
RUNTIME_INSTALLATION_ACTION = Path(
    '.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/'
    '003_PROJECT_CONFIGURATION/09_operations/'
    'CA-O-200-PROJECT_CONFIGURATION-ACTION--install-one-admitted-project-runtime.md'
)
RUNTIME_INSTALLATION_ENTRYPOINT = Path(
    '102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/framework_runtime_installation_mcp.py'
)


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _tree_digest(root: Path) -> str:
    rows = [
        {
            'path': path.relative_to(root).as_posix(),
            'sha256': _sha256(path.read_bytes()),
            'mode': path.stat().st_mode & 0o777,
        }
        for path in sorted(root.rglob('*'))
        if path.is_file() and not path.is_symlink()
    ]
    return _sha256(json.dumps(rows, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8'))


def seed_selected_runtime_binding_package(root: Path) -> object:
    """Create one physical selected package without copying a control source.

    The package contains the derived D620 binding projection and a regular
    package Engine member.  Its temporary source assembly deliberately lives
    outside the Project control root so discovery can prove it is not using a
    checkout/control declaration as fallback evidence.
    """

    root = root.resolve(strict=True)
    # Keep the source assembly outside the Project fixture.  Apart from proving
    # no control-source fallback, this avoids cleanup traversing a retained
    # canonical projection path on managed macOS filesystems.
    source = Path(tempfile.mkdtemp(prefix='caprmedio-package-binding-')).resolve()
    releases = root / '.caprmedio_install' / 'releases'

    def write(relative: str, payload: bytes) -> None:
        path = source / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)

    write(RUNTIME_INSTALLATION_ENTRYPOINT.as_posix(), b'# package-owned runtime adapter fixture\n')
    write('methodology/active/001_CORE_META_MODEL/04_requirement/CA-R-001--fixture.md', b'# core\n')
    write('methodology/support/CA-D-001--fixture.md', b'# support\n')
    write('SKILLS/ca/SKILL.md', b'# ca\n')
    write('defaults/framework.toml', b'[defaults]\nname = "fixture"\n')
    write('pyproject.toml', b'[project]\nname = "fixture"\nversion = "0.1.0"\n')
    write('uv.lock', b'version = 1\n')
    write('version.toml', b'[framework]\nversion = "0.1.0"\n')

    source_payload = (REPOSITORY_ROOT / RUNTIME_INSTALLATION_DELIVERY).read_bytes()
    source_path = RUNTIME_INSTALLATION_DELIVERY.as_posix()
    atom = {
        'atom_id': 'CA-D-620',
        'version': 1,
        'source_path': source_path,
        'sha256': _sha256(source_payload),
    }
    codec = package_library._methodology_export_module()
    binding = codec.BindingAtom(source_path, atom['atom_id'], atom['version'], atom['sha256'])
    write(f'methodology/bindings/{source_path}', codec.binding_projection_bytes(source_payload, binding))

    source_rows = (
        ('local-core', 'core', '102_FRAMEWORK_ENGINE'),
        ('core-meta-model', 'methodology', 'methodology/active/001_CORE_META_MODEL'),
        ('methodology-support', 'support', 'methodology/support'),
        ('tool-bindings', 'binding', 'methodology/bindings'),
    )
    descriptors = tuple(sorted((
        {
            'identity': identity,
            'kind': kind,
            'revision': _tree_digest(source / relative),
            'sha256': _tree_digest(source / relative),
            'visibility': 'public',
            'selection_default': False,
            'path': relative,
        }
        for identity, kind, relative in source_rows
    ), key=lambda row: str(row['identity'])))
    receipt = write_source_admission_receipt(source, descriptors)
    catalog = ['schema_version = 1', '']
    for row in descriptors:
        catalog.extend((
            f'[source.{row["identity"]}]',
            f'kind = "{row["kind"]}"',
            f'revision = "{row["revision"]}"',
            f'sha256 = "{row["sha256"]}"',
            f'admission_receipt_sha256 = "{receipt.sha256}"',
            f'visibility = "{row["visibility"]}"',
            'selection_default = false',
            f'path = "{row["path"]}"',
            '',
        ))
    write('catalog.toml', ('\n'.join(catalog) + '\n').encode('utf-8'))
    package = assemble_framework_package(source, releases, binding_atoms=(atom,))
    selector = root / '.caprmedio_install' / 'current.toml'
    selector.parent.mkdir(parents=True, exist_ok=True)
    selector.write_text(
        '\n'.join((
            'schema_version = 1',
            f'package_manifest_sha256 = "{package.manifest_digest}"',
            f'release_relpath = "releases/{package.manifest_digest}"',
            f'framework_version = "{package.framework_version}"',
            f'version_toml_sha256 = "{package.version_toml_sha256}"',
            f'source_catalog_sha256 = "{package.source_catalog_sha256}"',
            f'full_gate_receipt_sha256 = "{"a" * 64}"',
            f'image_digest = "{"b" * 64}"',
            '',
        )),
        encoding='utf-8',
    )
    return package


class ServiceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self._retain_fixture = False
        self.addCleanup(self._cleanup_fixture)
        self.root = Path(self.temp.name)
        control = self.root / '.caprmedio_caprmedio'
        control.mkdir()
        (control / 'caprmedio_project_settings.toml').write_text('[paths]\ncontrol_root=".caprmedio_caprmedio"\n')
        self.service = Service(self.root)

    def _cleanup_fixture(self) -> None:
        if self._retain_fixture:
            # The verified release carries a deeply nested projection source
            # path.  Managed macOS cleanup can block while removing it; retain
            # the disposable evidence root rather than turning that host quirk
            # into a false test failure or stalled suite.
            self.temp._finalizer.detach()
            return
        self.temp.cleanup()

    def _seed_source_admission_binding(self, *, delivery_payload: bytes | None = None) -> Path:
        """Install the actual D602/O199 source pair without an executable adapter."""

        for relative in (O199_RELATIVE,):
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPOSITORY_ROOT / O199_SOURCE, destination)
        if delivery_payload is not None:
            delivery = self.root / D602_RELATIVE
            delivery.parent.mkdir(parents=True, exist_ok=True)
            delivery.write_bytes(delivery_payload)
        entrypoint = self.root / SOURCE_ADMISSION_ENTRYPOINT
        entrypoint.parent.mkdir(parents=True, exist_ok=True)
        entrypoint.write_text('raise AssertionError("discovery must not execute source entrypoints")\n', encoding='utf-8')
        return self.root / D602_RELATIVE

    def _seed_runtime_installation_binding(self, *, delivery_payload: bytes | None = None) -> Path:
        destination = self.root / RUNTIME_INSTALLATION_ACTION
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPOSITORY_ROOT / RUNTIME_INSTALLATION_ACTION, destination)
        if delivery_payload is not None:
            delivery = self.root / RUNTIME_INSTALLATION_DELIVERY
            delivery.parent.mkdir(parents=True, exist_ok=True)
            delivery.write_bytes(delivery_payload)
        entrypoint = self.root / RUNTIME_INSTALLATION_ENTRYPOINT
        entrypoint.parent.mkdir(parents=True, exist_ok=True)
        entrypoint.write_text('raise AssertionError("discovery must not execute source entrypoints")\n', encoding='utf-8')
        return self.root / RUNTIME_INSTALLATION_DELIVERY

    @staticmethod
    def _files(root: Path) -> tuple[tuple[str, bytes], ...]:
        return tuple(
            (path.relative_to(root).as_posix(), path.read_bytes())
            for path in sorted(root.rglob('*')) if path.is_file() and not path.is_symlink()
        )

    @staticmethod
    def _operation(service: Service) -> dict:
        operations = service.discover(Query(query='CA-O-199'), operations=True)
        return next(row for row in operations['matches'] if row['id'] == 'CA-O-199')

    @staticmethod
    def _context(service: Service) -> dict:
        return service.context(type('Request', (), {'id': 'CA-O-199'})())

    @staticmethod
    def _runtime_operation(service: Service) -> dict:
        operations = service.discover(Query(query='CA-O-200'), operations=True)
        return next(row for row in operations['matches'] if row['id'] == 'CA-O-200')

    @staticmethod
    def _runtime_context(service: Service) -> dict:
        return service.context(type('Request', (), {'id': 'CA-O-200'})())

    def test_active_operations_only(self):
        for status in ('Active', 'Draft'):
            (self.root / '.caprmedio_caprmedio' / f'{status}.md').write_text(
                f'---\natom_id: CA-O-{status}\nstatus: {status}\ncontent_role: Operations\ntype: Action\n---\n# Summary\nFind things\n')
        result = self.service.discover(Query(), operations=True)
        self.assertEqual(result['total'], 1)

    def test_catalog_excludes_persistent_journal_and_projection_carriers(self):
        control = self.root / '.caprmedio_caprmedio'
        for relative, identity in (
            ('visible.md', 'CA-O-visible'),
            ('_journal/hidden.md', 'CA-O-journal'),
            ('_projection/hidden.md', 'CA-O-projection'),
        ):
            path = control / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                f'---\natom_id: {identity}\nstatus: Active\ncontent_role: Operations\ntype: Action\n---\n# Summary\nFixture\n'
            )

        result = self.service.discover(Query(), operations=True)

        self.assertEqual(['CA-O-visible'], [row['id'] for row in result['matches']])

    def test_catalog_prunes_excluded_trees_before_descending(self):
        control = (self.root / '.caprmedio_caprmedio').resolve()
        methodology = control / '101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES'
        canonical = methodology / '003_PROJECT_CONFIGURATION/active.md'
        canonical.parent.mkdir(parents=True)
        canonical.write_text('---\natom_id: CA-O-999\nstatus: Active\ncontent_role: Operations\n---\n# Summary\nCanonical\n')
        excluded = [control / name for name in ('archive', 'ARCHIVED', 'draft', 'done',
                    'resolved', 'canceled', 'cancelled', '_journal', '_projection', control.name)]
        excluded.append(methodology / '_release_materialized')
        for directory in excluded:
            directory.mkdir(parents=True)
            (directory / 'copy.md').write_text(canonical.read_text())
        scandir = os.scandir
        def guarded_scandir(path):
            self.assertNotIn(Path(path), excluded, 'Excluded tree was traversed')
            return scandir(path)
        with patch('os.scandir', side_effect=guarded_scandir):
            atoms, _tools, issues = self.service.catalog()
        self.assertEqual(['CA-O-999'], list(atoms))
        self.assertNotIn('incomplete: catalog limit reached', issues)
        self.assertNotIn('ambiguous Atom ID: CA-O-999', issues)

    def test_catalog_prunes_installed_framework_tree_but_keeps_project_and_authoring_sources(self):
        control = (self.root / '.caprmedio_caprmedio').resolve()
        project_operation = control / '09_operations/current.md'
        authoring_source = (
            control / '101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/'
            '003_PROJECT_CONFIGURATION/09_operations/authoring.md'
        )
        installed_copy = (
            control / '000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/'
            '000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/installed.md'
        )
        operation = ('---\natom_id: CA-O-999\nstatus: Active\ncontent_role: Operations\n'
                     '---\n# Summary\nProject operation\n')
        authoring = ('---\natom_id: CA-M-999\nstatus: Active\ncontent_role: Method\n'
                     '---\n# Summary\nAuthoring source\n')
        for path, text in ((project_operation, operation), (authoring_source, authoring),
                           (installed_copy, operation)):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)

        scandir = os.scandir
        def guarded_scandir(path):
            self.assertNotEqual(Path(path), control / '000_CAPRMEDIO_framework',
                                'Installed framework tree was traversed')
            return scandir(path)
        with patch('os.scandir', side_effect=guarded_scandir):
            atoms, _tools, issues = self.service.catalog()

        self.assertEqual({
            'CA-O-999': str(project_operation.relative_to(self.root.resolve())),
            'CA-M-999': str(authoring_source.relative_to(self.root.resolve())),
        }, {identity: row['source_path'] for identity, row in atoms.items()})
        self.assertNotIn('ambiguous Atom ID: CA-O-999', issues)

    def test_catalog_does_not_descend_into_symlink_directories(self):
        control = self.root / '.caprmedio_caprmedio'
        target = self.root / 'outside-control'
        target.mkdir()
        (target / 'active.md').write_text(
            '---\natom_id: CA-O-hidden\nstatus: Active\ncontent_role: Operations\n---\n# Summary\nHidden\n')
        link = control / 'linked-sources'
        link.symlink_to(target, target_is_directory=True)
        scandir = os.scandir
        def guarded_scandir(path):
            self.assertNotEqual(Path(path), link, 'Symlink directory was traversed')
            return scandir(path)
        with patch('os.scandir', side_effect=guarded_scandir):
            atoms, _tools, _issues = self.service.catalog()
        self.assertEqual({}, atoms)

    def test_nested_control_copy_is_omitted_without_hiding_canonical_source(self):
        control = self.root / '.caprmedio_caprmedio'
        canonical = control / '101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/003_PROJECT_CONFIGURATION/active.md'
        nested = control / '101_LAYER_1_FRAMEWORK_METHODOLOGY/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/003_PROJECT_CONFIGURATION/active.md'
        text = '---\natom_id: CA-O-999\nstatus: Active\ncontent_role: Operations\n---\n# Summary\nCanonical\n'
        for path in (canonical, nested):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)
        atoms, _tools, issues = self.service.catalog()
        self.assertEqual(str(canonical.resolve().relative_to(self.root.resolve())), atoms['CA-O-999']['source_path'])
        self.assertNotIn('ambiguous Atom ID: CA-O-999', issues)

    def test_true_authoritative_duplicate_remains_explicit(self):
        control = self.root / '.caprmedio_caprmedio'
        text = '---\natom_id: CA-O-999\nstatus: Active\ncontent_role: Operations\n---\n# Summary\nCanonical\n'
        for name in ('one.md', 'two.md'):
            (control / name).write_text(text)
        atoms, _tools, issues = self.service.catalog()
        self.assertNotIn('CA-O-999', atoms)
        self.assertIn('ambiguous Atom ID: CA-O-999', issues)

    def test_traversal_rejected(self):
        with self.assertRaises(ValueError):
            self.service.status(Observation(run_id='../outside'))

    def test_unknown_run_explicit(self):
        with self.assertRaisesRegex(ValueError, 'backend'):
            self.service.status(Observation(run_id='missing'))

    def test_watch_replays_confirmed_only(self):
        folder = self.root / '.caprmedio_tmp/rmed-base-revise/run1'
        folder.mkdir(parents=True)
        state = {'workflow_run_id': 'run1', 'outcome': 'completed',
                 'events': [{'event': {'event_id': 'confirmed'}, 'receipt': {'ok': True}},
                            {'event': {'event_id': 'pending'}, 'receipt': None}]}
        (folder / 'progress.json').write_text(json.dumps(state))
        first = asyncio.run(self.service.watch(Watch(run_id='run1')))
        self.assertEqual(len(first['notifications']), 1)
        second = asyncio.run(self.service.watch(Watch(run_id='run1', cursor=first['cursor'])))
        self.assertEqual(second['notifications'], [])
        self.assertFalse(second['changed'])

    def test_symlink_rejected(self):
        target = self.root / 'target'
        target.write_text('safe')
        link = self.root / 'link'
        link.symlink_to(target)
        with self.assertRaises(ValueError):
            self.service.read(link)

    def test_binding_refresh_and_ambiguity(self):
        control = self.root / '.caprmedio_caprmedio'
        source = control / 'binding.md'
        text = ('---\natom_id: CA-D-1\nstatus: Active\ncontent_role: Delivery\n---\n'
                '# Summary\nDiscover mock\n```toml\n[tool_binding]\nname="MOCK"\n'
                'entrypoint="mock.py"\naction_ids=[]\n```\n')
        source.write_text(text)
        self.assertEqual(self.service.discover(Query())['matches'][0]['availability'], 'missing')
        (self.root / 'mock.py').write_text('mock implementation')
        self.assertEqual(self.service.discover(Query())['matches'][0]['availability'], 'source')
        (control / 'duplicate.md').write_text(text)
        self.assertEqual(self.service.discover(Query())['matches'], [])

    def test_source_only_package_admission_is_internal_not_exposed_and_has_no_effects(self):
        delivery = (REPOSITORY_ROOT / D602_RELATIVE).read_bytes()
        self._seed_source_admission_binding(delivery_payload=delivery)
        before = self._files(self.root)

        operation = self._operation(self.service)
        context = self._context(self.service)

        self.assertEqual('unresolved', operation['availability'])
        self.assertEqual([], operation['tools'])
        self.assertIsNone(context['input_schema'])
        self.assertEqual(before, self._files(self.root))

    def test_exposed_package_admission_remains_internal_without_effects(self):
        delivery = (REPOSITORY_ROOT / D602_RELATIVE).read_bytes()
        self._seed_source_admission_binding(delivery_payload=delivery)
        service = Service(self.root, exposed=('admit_package_sources',))
        before = self._files(self.root)

        operation = self._operation(service)
        context = self._context(service)

        self.assertEqual([], service.discover(Query(query='ADMIT_PACKAGE_SOURCES'))['matches'])
        self.assertEqual('unresolved', operation['availability'])
        self.assertEqual([], operation['tools'])
        self.assertIsNone(context['input_schema'])
        self.assertEqual(before, self._files(self.root))

    def test_malformed_source_admission_binding_is_unresolved_without_effects(self):
        delivery = (REPOSITORY_ROOT / D602_RELATIVE).read_bytes().replace(
            b'entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/source_admission_mcp.py"',
            b'entrypoint = "other.py"',
        )
        self._seed_source_admission_binding(delivery_payload=delivery)
        service = Service(self.root, exposed=('admit_package_sources',))
        before = self._files(self.root)

        self.assertEqual('unresolved', self._operation(service)['availability'])
        self.assertIsNone(self._context(service)['input_schema'])
        self.assertEqual(before, self._files(self.root))

    def test_ambiguous_source_admission_binding_is_unresolved_without_effects(self):
        delivery = (REPOSITORY_ROOT / D602_RELATIVE).read_bytes()
        canonical = self._seed_source_admission_binding(delivery_payload=delivery)
        duplicate = canonical.with_name('CA-D-603-TOOLS-DELIVERY--ambiguous-source-admission.md')
        duplicate.write_bytes(delivery.replace(b'atom_id: CA-D-602', b'atom_id: CA-D-603'))
        service = Service(self.root, exposed=('admit_package_sources',))
        before = self._files(self.root)

        self.assertEqual('unresolved', self._operation(service)['availability'])
        self.assertIsNone(self._context(service)['input_schema'])
        self.assertEqual(before, self._files(self.root))

    def test_missing_source_admission_binding_is_unresolved_without_effects(self):
        self._seed_source_admission_binding()
        service = Service(self.root, exposed=('admit_package_sources',))
        before = self._files(self.root)

        self.assertEqual('unresolved', self._operation(service)['availability'])
        self.assertIsNone(self._context(service)['input_schema'])
        self.assertEqual(before, self._files(self.root))

    def test_runtime_installation_source_only_is_unresolved_without_effects(self):
        delivery = (REPOSITORY_ROOT / RUNTIME_INSTALLATION_DELIVERY).read_bytes()
        self._seed_runtime_installation_binding(delivery_payload=delivery)
        before = self._files(self.root)

        operation = self._runtime_operation(self.service)
        context = self._runtime_context(self.service)

        self.assertEqual('unresolved', operation['availability'])
        self.assertEqual(['INSTALL_FRAMEWORK_RUNTIME'], operation['tools'])
        self.assertIsNone(context['input_schema'])
        self.assertEqual(before, self._files(self.root))

    def test_exposed_runtime_installation_returns_the_exact_adapter_schema_without_effects(self):
        delivery = (REPOSITORY_ROOT / RUNTIME_INSTALLATION_DELIVERY).read_bytes()
        self._seed_runtime_installation_binding(delivery_payload=delivery)
        service = Service(self.root, exposed=('install_framework_runtime',))
        before = self._files(self.root)

        tool = next(
            row for row in service.discover(Query(query='INSTALL_FRAMEWORK_RUNTIME'))['matches']
            if row['name'] == 'INSTALL_FRAMEWORK_RUNTIME'
        )
        operation = self._runtime_operation(service)
        context = self._runtime_context(service)
        schema = context['input_schema']

        self.assertEqual('mcp', tool['availability'])
        self.assertEqual('mcp', operation['availability'])
        self.assertEqual(runtime_installation_input_schema(), schema)
        encoded = json.dumps(schema, sort_keys=True)
        self.assertIn('native_packet', encoded)
        self.assertIn('command_id', encoded)
        self.assertIn('additionalProperties', encoded)
        self.assertEqual(before, self._files(self.root))

    def test_malformed_runtime_installation_binding_is_unresolved_without_effects(self):
        delivery = (REPOSITORY_ROOT / RUNTIME_INSTALLATION_DELIVERY).read_bytes().replace(
            b'entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/framework_runtime_installation_mcp.py"',
            b'entrypoint = "other.py"',
        )
        self._seed_runtime_installation_binding(delivery_payload=delivery)
        before = self._files(self.root)

        self.assertEqual('unresolved', self._runtime_operation(self.service)['availability'])
        self.assertIsNone(self._runtime_context(self.service)['input_schema'])
        self.assertEqual(before, self._files(self.root))

    def test_ambiguous_runtime_installation_binding_is_unresolved_without_effects(self):
        delivery = (REPOSITORY_ROOT / RUNTIME_INSTALLATION_DELIVERY).read_bytes()
        canonical = self._seed_runtime_installation_binding(delivery_payload=delivery)
        duplicate = canonical.with_name('CA-D-611-MCP-DELIVERY--ambiguous-runtime-installation.md')
        duplicate.write_bytes(delivery.replace(b'atom_id: CA-D-620', b'atom_id: CA-D-621'))
        before = self._files(self.root)

        self.assertEqual('unresolved', self._runtime_operation(self.service)['availability'])
        self.assertIsNone(self._runtime_context(self.service)['input_schema'])
        self.assertEqual(before, self._files(self.root))

    def test_selected_package_binding_is_discovered_without_a_control_source_fallback(self):
        self._retain_fixture = True
        package = seed_selected_runtime_binding_package(self.root)
        self.assertFalse((self.root / RUNTIME_INSTALLATION_DELIVERY).exists())
        self.assertFalse((self.root / '.git').exists())
        service = Service(self.root, exposed=('install_framework_runtime',))
        before = self._files(self.root)

        tool = next(
            row for row in service.discover(Query(query='INSTALL_FRAMEWORK_RUNTIME'))['matches']
            if row['name'] == 'INSTALL_FRAMEWORK_RUNTIME'
        )
        context = service.context(type('Request', (), {'id': 'INSTALL_FRAMEWORK_RUNTIME'})())

        self.assertEqual(package.manifest_digest, (self.root / '.caprmedio_install/current.toml').read_text().split('package_manifest_sha256 = "', 1)[1].split('"', 1)[0])
        self.assertEqual('mcp', tool['availability'])
        self.assertEqual(RUNTIME_INSTALLATION_DELIVERY.as_posix(), tool['source_path'])
        self.assertEqual(runtime_installation_input_schema(), context['input_schema'])
        self.assertEqual(before, self._files(self.root))

    def test_selected_package_binding_refuses_a_conflicting_current_declaration(self):
        self._retain_fixture = True
        seed_selected_runtime_binding_package(self.root)
        conflicting = self.root / RUNTIME_INSTALLATION_DELIVERY
        conflicting.parent.mkdir(parents=True, exist_ok=True)
        conflicting.write_bytes(
            (REPOSITORY_ROOT / RUNTIME_INSTALLATION_DELIVERY).read_bytes().replace(
                b'Expose direct Framework runtime installation',
                b'Conflicting direct Framework runtime installation',
                1,
            )
        )
        service = Service(self.root, exposed=('install_framework_runtime',))
        before = self._files(self.root)

        discovered = service.discover(Query(query='INSTALL_FRAMEWORK_RUNTIME'))

        self.assertEqual([], discovered['matches'])
        self.assertIn('ambiguous package binding: CA-D-620', discovered['coverage_issues'])
        with self.assertRaisesRegex(ValueError, 'Unknown or ambiguous capability'):
            service.context(type('Request', (), {'id': 'INSTALL_FRAMEWORK_RUNTIME'})())
        self.assertEqual(before, self._files(self.root))

    def test_selected_package_binding_refuses_a_different_delivery_claiming_its_tool_namespace(self):
        self._retain_fixture = True
        seed_selected_runtime_binding_package(self.root)
        duplicate = (self.root / RUNTIME_INSTALLATION_DELIVERY).with_name(
            'CA-D-621-MCP-DELIVERY--duplicate-runtime-installation.md'
        )
        duplicate.parent.mkdir(parents=True, exist_ok=True)
        duplicate.write_bytes(
            (REPOSITORY_ROOT / RUNTIME_INSTALLATION_DELIVERY).read_bytes().replace(
                b'atom_id: CA-D-620', b'atom_id: CA-D-621', 1,
            )
        )
        service = Service(self.root, exposed=('install_framework_runtime',))
        before = self._files(self.root)

        discovered = service.discover(Query(query='INSTALL_FRAMEWORK_RUNTIME'))

        self.assertEqual([], discovered['matches'])
        self.assertIn('ambiguous package binding: CA-D-620', discovered['coverage_issues'])
        self.assertEqual(before, self._files(self.root))

    def test_selected_package_binding_allows_distinct_entrypoint_only_declarations(self):
        projection = type('Projection', (), {
            'atom_id': 'CA-D-620',
            'source_path': 'methodology/bindings/CA-D-620.md',
            'source_sha256': 'a' * 64,
            'tool_binding': {
                'entrypoint': '102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/one.py',
            },
        })()
        current_sources = {
            'CA-D-621': [{
                'atom_id': 'CA-D-621',
                'source_path': 'methodology/bindings/CA-D-621.md',
                'sha256': 'b' * 64,
                'tool_binding': {
                    'entrypoint': '102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/two.py',
                },
            }],
        }

        self.assertFalse(Service._package_binding_conflicts(projection, current_sources))

    def test_selected_package_deduplicates_the_same_current_source_identity(self):
        self._retain_fixture = True
        seed_selected_runtime_binding_package(self.root)
        current = self.root / RUNTIME_INSTALLATION_DELIVERY
        current.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPOSITORY_ROOT / RUNTIME_INSTALLATION_DELIVERY, current)
        service = Service(self.root, exposed=('install_framework_runtime',))

        discovered = service.discover(Query(query='INSTALL_FRAMEWORK_RUNTIME'))

        self.assertEqual(1, discovered['total'])
        self.assertEqual('mcp', discovered['matches'][0]['availability'])
        self.assertNotIn('ambiguous package binding: CA-D-620', discovered['coverage_issues'])

    def test_invalid_selected_package_never_falls_back_to_a_current_source(self):
        self._retain_fixture = True
        seed_selected_runtime_binding_package(self.root)
        current = self.root / RUNTIME_INSTALLATION_DELIVERY
        current.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPOSITORY_ROOT / RUNTIME_INSTALLATION_DELIVERY, current)
        selector = self.root / '.caprmedio_install/current.toml'
        selector.write_text('schema_version = 1\n', encoding='utf-8')
        service = Service(self.root, exposed=('install_framework_runtime',))
        before = self._files(self.root)

        discovered = service.discover(Query(query='INSTALL_FRAMEWORK_RUNTIME'))

        self.assertEqual([], discovered['matches'])
        self.assertIn('installed package binding unavailable', discovered['coverage_issues'])
        self.assertEqual(before, self._files(self.root))

    def test_admitted_release_route_is_discoverable_and_has_compact_context(self):
        control = self.root / '.caprmedio_caprmedio'
        operation = control / 'release.md'
        operation.write_text(
            '---\natom_id: CA-O-164\nstatus: Active\ncontent_role: Operations\ntype: Workflow\n---\n'
            '# Summary\nRelease selected Framework Version\n'
        )
        manifest = {
            'manifest_ref': '.caprmedio_caprmedio/_projection/selected_workflow_bindings.json',
            'canonical_manifest_sha256': 'a' * 64,
            'source_freshness': {'selected_binding_digest': 'b' * 64},
            'routes': [{'route': 'release_version', 'workflow': {'atom_id': 'CA-O-164'},
                        'ordered_actions': [{'atom_id': 'CA-O-165'}]}],
        }
        self.service.exposed.add('release_version')
        with patch('selected_routes.load_selected_manifest', return_value=manifest):
            tools = self.service.discover(Query(query='release_version'))
            operations = self.service.discover(Query(query='CA-O-164'), operations=True)
            context = self.service.context(type('Request', (), {'id': 'CA-O-164'})())

        self.assertEqual(['release_version'], [row['name'] for row in tools['matches']])
        self.assertEqual('mcp', operations['matches'][0]['availability'])
        self.assertEqual(['release_version'], operations['matches'][0]['tools'])
        self.assertEqual([], context['related_definitions'])
        self.assertTrue(context['context_complete'])
        self.assertEqual('release_version', context['input_schema']['properties']['operation_route']['const'])

    def test_admitted_selected_routes_keep_route_and_workflow_context_exact(self):
        control = self.root / '.caprmedio_caprmedio'
        for identity, role in (('CA-O-127', 'Workflow'), ('CA-O-130', 'Workflow'), ('CA-O-128', 'Action')):
            (control / f'{identity}.md').write_text(
                f'---\natom_id: {identity}\nstatus: Active\ncontent_role: Operations\ntype: {role}\n---\n'
                f'# Summary\n{identity}\n'
            )
        manifest = {
            'manifest_ref': '.caprmedio_caprmedio/_projection/selected_workflow_bindings.json',
            'canonical_manifest_sha256': 'a' * 64,
            'source_freshness': {'selected_binding_digest': 'b' * 64},
            'routes': [
                {'route': 'create_atom', 'workflow': {'atom_id': 'CA-O-127'},
                 'ordered_actions': [{'atom_id': 'CA-O-128'}]},
                {'route': 'update_atom', 'workflow': {'atom_id': 'CA-O-130'},
                 'ordered_actions': [{'atom_id': 'CA-O-128'}]},
            ],
        }
        self.service.exposed.update(('create_atom', 'update_atom'))
        with patch('selected_routes.load_selected_manifest', return_value=manifest):
            route = self.service.context(type('Request', (), {'id': 'create_atom'})())
            workflow = self.service.context(type('Request', (), {'id': 'CA-O-127'})())
            action = self.service.context(type('Request', (), {'id': 'CA-O-128'})())

        for context in (route, workflow, action):
            self.assertTrue(context['context_complete'])
            self.assertEqual('a' * 64, context['definition']['definition_manifest']['manifest_digest'])
        self.assertEqual(['create_atom'], route['definition']['tools'])
        self.assertEqual('create_atom', route['input_schema']['properties']['operation_route']['const'])
        self.assertEqual(['create_atom'], workflow['definition']['tools'])
        self.assertEqual('create_atom', workflow['input_schema']['properties']['operation_route']['const'])
        self.assertEqual(['create_atom', 'update_atom'], action['definition']['tools'])
        self.assertIsNone(action['input_schema'])

    def test_unadmitted_release_route_is_not_synthesized(self):
        manifest = {
            'manifest_ref': '.caprmedio_caprmedio/_projection/selected_workflow_bindings.json',
            'canonical_manifest_sha256': 'a' * 64,
            'source_freshness': {}, 'routes': [],
        }
        self.service.exposed.add('release_version')
        with patch('selected_routes.load_selected_manifest', return_value=manifest):
            self.assertEqual([], self.service.discover(Query(query='release_version'))['matches'])

    def test_source_operation_is_not_executable_when_selected_manifest_admission_fails(self):
        manifest = {
            'manifest_ref': '.caprmedio_caprmedio/_projection/selected_workflow_bindings.json',
            'canonical_manifest_sha256': 'a' * 64,
            'source_freshness': {'selected_binding_digest': 'b' * 64},
            'routes': [{'route': 'create_atom', 'workflow': {'atom_id': 'CA-O-127'},
                        'ordered_actions': [{'atom_id': 'CA-O-128'}]}],
        }
        with patch('selected_routes.load_selected_manifest', return_value=manifest):
            self.assertEqual([], self.service.discover(Query(query='create_atom'))['matches'])
        control = self.root / '.caprmedio_caprmedio'
        (control / 'workflow.md').write_text(
            '---\natom_id: CA-O-127\nstatus: Active\ncontent_role: Operations\ntype: Workflow\n---\n'
            '# Summary\nSource workflow\n'
        )
        self.service.exposed.add('create_atom')
        secret = '.env/secret'
        with patch('selected_routes.load_selected_manifest', side_effect=ValueError(f'source pin is stale: {secret}')):
            tools = self.service.discover(Query(query='create_atom'))
            operations = self.service.discover(Query(query='CA-O-127'), operations=True)

        self.assertEqual([], tools['matches'])
        self.assertEqual('unresolved', operations['matches'][0]['availability'])
        self.assertEqual([], operations['matches'][0]['tools'])
        self.assertEqual(['binding evidence stale: refresh source bindings, then re-preview selected routes'],
                         tools['coverage_issues'])
        self.assertNotIn(secret, json.dumps(tools['coverage_issues']))

    def test_selected_manifest_missing_evidence_reports_sanitized_recovery(self):
        self.service.exposed.add('create_atom')

        with patch('selected_routes.load_selected_manifest', side_effect=OSError('/private/missing-secret')):
            result = self.service.discover(Query(query='create_atom'))

        self.assertEqual([], result['matches'])
        self.assertEqual(['binding evidence unavailable: restore or regenerate binding evidence, then re-preview selected routes'],
                         result['coverage_issues'])
        self.assertNotIn('missing-secret', json.dumps(result['coverage_issues']))

    def test_selected_manifest_malformed_evidence_reports_sanitized_recovery(self):
        self.service.exposed.add('create_atom')

        with patch('selected_routes.load_selected_manifest', side_effect=ValueError('malformed /private/secret')):
            result = self.service.discover(Query(query='create_atom'))

        self.assertEqual([], result['matches'])
        self.assertEqual(['binding evidence invalid: correct bindings, then re-preview selected routes'],
                         result['coverage_issues'])
        self.assertNotIn('secret', json.dumps(result['coverage_issues']))

    def test_source_only_action_is_not_upgraded_to_an_admitted_selected_route(self):
        control = self.root / '.caprmedio_caprmedio'
        (control / 'action.md').write_text(
            '---\natom_id: CA-O-128\nstatus: Active\ncontent_role: Operations\ntype: Action\n---\n'
            '# Summary\nSource-only Action\n'
        )
        manifest = {
            'manifest_ref': '.caprmedio_caprmedio/_projection/selected_workflow_bindings.json',
            'canonical_manifest_sha256': 'a' * 64,
            'source_freshness': {'selected_binding_digest': 'b' * 64},
            'routes': [{'route': 'create_atom', 'workflow': {'atom_id': 'CA-O-127'},
                        'ordered_actions': [{'atom_id': 'CA-O-999'}]}],
        }
        self.service.exposed.add('create_atom')
        with patch('selected_routes.load_selected_manifest', return_value=manifest):
            context = self.service.context(type('Request', (), {'id': 'CA-O-128'})())

        self.assertNotIn('tools', context['definition'])
        self.assertIsNone(context['input_schema'])

    def test_stale_release_manifest_is_not_synthesized_even_when_exposed(self):
        self.service.exposed.add('release_version')
        with patch('selected_routes.load_selected_manifest', side_effect=ValueError('source pin is stale')):
            self.assertEqual([], self.service.discover(Query(query='release_version'))['matches'])

    def test_selected_source_registry_pin_stale_reports_sanitized_recovery(self):
        self.service.exposed.add('create_atom')
        secret = '/private/selected-source-registry-secret'

        with patch(
            'selected_routes.load_selected_manifest',
            side_effect=ValueError(f'selected source registry pin is stale: {secret}'),
        ):
            result = self.service.discover(Query(query='create_atom'))

        self.assertEqual([], result['matches'])
        self.assertEqual(
            ['binding evidence stale: refresh source bindings, then re-preview selected routes'],
            result['coverage_issues'],
        )
        self.assertNotIn(secret, json.dumps(result['coverage_issues']))

    def test_admitted_release_route_is_not_advertised_when_unexposed(self):
        manifest = {
            'manifest_ref': '.caprmedio_caprmedio/_projection/selected_workflow_bindings.json',
            'canonical_manifest_sha256': 'a' * 64,
            'source_freshness': {'selected_binding_digest': 'b' * 64},
            'routes': [{'route': 'release_version', 'workflow': {'atom_id': 'CA-O-164'},
                        'ordered_actions': [{'atom_id': 'CA-O-165'}]}],
        }
        with patch('selected_routes.load_selected_manifest', return_value=manifest):
            self.assertEqual([], self.service.discover(Query(query='release_version'))['matches'])

    def test_unknown_properties_rejected(self):
        with self.assertRaises(ValueError):
            Query.model_validate({'query': 'hello', 'extra': True})

    def test_cursor_invalid(self):
        with self.assertRaises(ValueError):
            asyncio.run(self.service.watch(Watch(run_id='one', cursor='invalid')))


if __name__ == '__main__':
    unittest.main()
