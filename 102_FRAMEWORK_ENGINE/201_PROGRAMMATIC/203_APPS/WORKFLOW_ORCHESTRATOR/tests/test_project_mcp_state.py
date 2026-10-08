"""Project-local state and endpoint-only mount declaration, without Docker."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

import yaml

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP.parents[1] / '201_TOOLS'))
from project_selection import resolve_project


class ProjectStateTests(unittest.TestCase):
    def test_two_nested_projects_have_distinct_all_runtime_namespaces(self):
        parent = Path(tempfile.mkdtemp(dir=APP.parents[3] / '.caprmedio_tmp'))
        selections = []
        for name in ('alpha', 'beta'):
            root = parent / 'repository' / 'projects' / name
            control = root / f'.caprmedio_{name}'
            control.mkdir(parents=True)
            (control / 'caprmedio_project_settings.toml').write_text(
                f'[paths]\ncontrol_root=".caprmedio_{name}"\n[project]\nname="{name}"\n')
            (control / 'project_structure.toml').write_text('schema_version=1\n')
            selections.append(resolve_project(root))
        left, right = selections
        for field in ('instance_id', 'compose_project', 'launcher_state', 'reload_state'):
            self.assertNotEqual(getattr(left, field), getattr(right, field))
        for selection in selections:
            self.assertTrue(selection.launcher_state.is_relative_to(selection.root))
            self.assertTrue(selection.reload_state.is_relative_to(selection.root))
        left.reload_state.mkdir(parents=True)
        (left.reload_state / 'same-id.json').write_text(json.dumps({'receipt': 'left'}))
        self.assertFalse((right.reload_state / 'same-id.json').exists())

    def test_compose_mount_and_resource_boundary_is_mcp_only(self):
        spec = yaml.safe_load((APP / 'docker/project-mcp.compose.yaml').read_text())
        self.assertEqual({'mcp-http'}, set(spec['services']))
        service = spec['services']['mcp-http']
        self.assertEqual(['mcp-http'], service['command'])
        self.assertEqual(['127.0.0.1::8092'], service['ports'])
        self.assertEqual([{'type': 'bind', 'source': '${CAPRMEDIO_PROJECT_ROOT}',
                          'target': '/project'}], service['volumes'])
        self.assertTrue(service['read_only'])
        self.assertEqual('no', service['restart'])
        self.assertEqual('512m', service['mem_limit'])
        self.assertEqual(1, service['cpus'])
        self.assertNotIn('CODEX_AUTHFILE', service['environment'])
        self.assertNotIn('worker', json.dumps(spec))
        self.assertNotIn('docker.sock', json.dumps(spec))


if __name__ == '__main__':
    unittest.main()
