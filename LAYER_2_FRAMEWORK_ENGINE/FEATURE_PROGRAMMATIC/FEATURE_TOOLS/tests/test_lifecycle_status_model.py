import json
import re
import subprocess
from pathlib import Path
import sys
import tempfile
import unittest
import yaml

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE.status_model import StatusModel, StatusModelError, canonical_status, compile_status_model, load_status_model  # noqa: E402
from carrier_aliases import carrier_read_view  # noqa: E402

ROOT = TOOLS.parents[2]
CORE = ROOT / '.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement'


class StatusModelTests(unittest.TestCase):
    def test_carrier_values_and_collision(self):
        model = StatusModel(((None, None, 'In Progress'),))
        self.assertEqual(canonical_status(model, 'Plan', 'Task', 'in_progress'), 'In Progress')
        self.assertEqual(canonical_status(model, 'Plan', 'Task', 'In Progress'), 'In Progress')
        with self.assertRaises(StatusModelError):
            canonical_status(model, 'Plan', 'Task', 'IN_PROGRESS')
        collision = StatusModel(((None, None, 'In Progress'), (None, None, 'In_Progress')))
        with self.assertRaises(StatusModelError):
            canonical_status(collision, 'Plan', 'Task', 'In Progress')

    def sources(self):
        return [next(CORE.glob(f'CA-R-{number}-*.md')) for number in (2696, 1539, 1608, 1875)]

    def cfel_base_source(self):
        from ATOM_LIFECYCLE.status_model import _formal_claim_blocks, _statements

        source = self.sources()[0].read_text()
        statements = [statement for block in _formal_claim_blocks(source) for statement in _statements(block)]
        self.assertTrue(statements)
        fence = '```CFEL\n# model\n' + ';\n'.join(statements) + ';\n```'
        converted, count = re.subn(r'```python\n.*?\n```', lambda _: fence, source, count=1, flags=re.DOTALL)
        self.assertEqual(count, 1)
        return converted

    def test_current_sources_inheritance_and_union(self):
        sources = self.sources()
        payload = compile_status_model(sources)
        asset = json.loads(payload)
        headers = [carrier_read_view(yaml.safe_load(path.read_text().split('---', 2)[1])) for path in sources]
        self.assertEqual(10, len(asset['declarations']))
        self.assertEqual({header['atom_id']: header['version'] for header in headers},
                         {source['atom_id']: source['version'] for source in asset['sources']})
        self.assertEqual(payload, compile_status_model(reversed(sources)))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'status.json'
            path.write_bytes(payload)
            model = load_status_model(path)
            base = {'Draft', 'Active', 'Archived'}
            self.assertEqual(base, model.allowed('Requirement', 'Declaration'))
            self.assertEqual(base | {'Backlog', 'Done', 'Canceled'}, model.allowed('Plan', 'Plan'))
            self.assertEqual(base | {'Resolved', 'Canceled'}, model.allowed('Concern', 'Issue'))
            self.assertEqual(base | {'Done'}, model.allowed('Analysis and Advisory', 'Rationale'))
            self.assertEqual(base, model.allowed('Analysis and Advisory', 'Other'))
            self.assertEqual(base, model.allowed('Analysis and Advisory', 'Code Synopsis'))
            self.assertEqual(base, model.allowed('Other', 'Code Synopsis'))

    def test_role_and_form_domains_are_unioned(self):
        source = self.cfel_base_source().replace('Atom.Header.State.Status', 'Atom.Header.Status').replace(
            'Atom.Header.Status :: Archived',
            'Atom.Header.Status :: Archived;\nAtom/(.Header.Context.Form in (Report)).Header.State.Status :: Reviewed'
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'source.md'
            path.write_text(source)
            payload = compile_status_model([path, self.sources()[1]])
            path.write_bytes(payload)
            self.assertEqual({'Draft', 'Active', 'Archived', 'Backlog', 'Done', 'Canceled', 'Reviewed'},
                             load_status_model(path).allowed('Plan', 'Report'))

    def test_reject_old_single_colon(self):
        source = self.cfel_base_source().replace('Status :: Active', 'Status: Active')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'source.md'
            path.write_text(source)
            with self.assertRaisesRegex(StatusModelError, 'unsupported Status declaration'):
                compile_status_model([path])

    def test_backlog_group_is_not_a_status_membership_and_malformed_refuses(self):
        sources = self.sources()
        current = sources[1].read_text()
        group = 'status_groups={"Backlog": "Backlog"},'
        self.assertIn(group, current)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'plan.md'
            path.write_text(current.replace(group, ''))
            self.assertEqual(json.loads(compile_status_model(sources))['declarations'],
                             json.loads(compile_status_model([sources[0], path, *sources[2:]]))['declarations'])
            for malformed, diagnostic in (
                ('status_groups=None,', 'Status Groups require allowed values and one Role'),
                ('status_groups={"Unlisted": "Backlog"},', 'Status Groups require allowed values and one Role'),
                ('status_group={"Backlog": "Backlog"},', 'unsupported declare_entity arguments: status_group'),
            ):
                with self.subTest(malformed=malformed):
                    path.write_text(current.replace(group, malformed))
                    with self.assertRaisesRegex(ValueError, diagnostic):
                        compile_status_model([sources[0], path])

    def test_plan_constraints_do_not_add_status_memberships(self):
        sources = self.sources()
        plan = next(CORE.glob('CA-R-2511-*.md'))
        base = json.loads(compile_status_model(sources))
        compiled = json.loads(compile_status_model([*sources, plan]))
        self.assertEqual(base['declarations'], compiled['declarations'])

    def test_cli_reads_only_current_staged_sources(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sources = root / 'sources'
            sources.mkdir()
            for path in self.sources():
                (sources / path.name).write_bytes(path.read_bytes())
            archived = sources / 'archive'
            archived.mkdir()
            (archived / self.sources()[0].name).write_text('invalid')
            _, header, body = self.sources()[1].read_text().split('---', 2)
            metadata = yaml.safe_load(header)
            metadata.get('state', metadata)['status'] = 'draft'
            (sources / 'CA-R-9999-draft.md').write_text('---\n' + yaml.safe_dump(metadata) + '---' + body)
            output = root / 'asset.json'
            subprocess.run([sys.executable, str(TOOLS / 'ATOM_LIFECYCLE/status_model.py'),
                            '--model-root', str(sources), '--output', str(output)], check=True)
            self.assertEqual(compile_status_model(self.sources()), output.read_bytes())

    def test_grouped_headers_comments_and_multiline_statements(self):
        original = self.cfel_base_source()
        _, header, body = original.split('---', 2)
        metadata = yaml.safe_load(header)
        for group, names in {
            'identity': ('atom_id', 'ref_id'),
            'context': ('container', 'role', 'form', 'topics', 'tier'),
            'state': ('status', 'version', 'updated_at'),
        }.items():
            metadata[group] = {name: metadata.pop(name) for name in names if name in metadata}
        body = body.replace('# model', '# this comment is not a parsing gate')
        body = body.replace('Atom.Header.State.Status', 'Atom.Header.Status')
        body = body.replace('Atom.Header.Status :: Active;',
                            'Atom.Header.State.Status # inline comment\n ::\n "Live #1";')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sources = root / 'sources'
            sources.mkdir()
            source = sources / self.sources()[0].name
            source.write_text('---\n' + yaml.safe_dump(metadata, sort_keys=False) + '---' + body)
            output = root / 'asset.json'
            subprocess.run([sys.executable, str(TOOLS / 'ATOM_LIFECYCLE/status_model.py'),
                            '--model-root', str(sources), '--output', str(output)], check=True)
            self.assertEqual({'Draft', 'Live #1', 'Archived'}, load_status_model(output).allowed('Plan', 'Plan'))

    def test_asset_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'status.json'
            for data in ('{}', '{"schema":1,"schema":1}', '{"schema":1,"sources":[],"declarations":[]}'):
                path.write_text(data)
                with self.assertRaises(StatusModelError):
                    load_status_model(path)

    def test_grouped_status_paths_compile_and_staged_detection(self):
        from ATOM_LIFECYCLE.status_model import _staged_declarations
        source = self.cfel_base_source()
        source = source.replace('.Header.Status', '.Header.State.Status')
        source = source.replace('Atom.Header.State.Status :: Archived',
            'Atom.Header.State.Status :: Archived;\n'
            'Atom/(.Header.Context.Role in (Plan))/(.Header.Context.Form in (Report))'
            '.Header.State.Status :: Reviewed')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'CA-R-1-test.md'
            path.write_text(source)
            self.assertEqual([path], _staged_declarations(Path(directory)))
            asset = json.loads(compile_status_model([path]))
            self.assertIn({'source': asset['sources'][0]['atom_id'], 'role': 'Plan',
                           'form': 'Report', 'value': 'Reviewed'}, asset['declarations'])
            path.write_text(source.replace('Status :: Reviewed', 'Status : Reviewed'))
            with self.assertRaisesRegex(StatusModelError, 'unsupported Status declaration'):
                compile_status_model([path])


if __name__ == '__main__':
    unittest.main()
