"""Public command output/exit gates; no Docker or workflow dispatch."""
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP / 'docker'))
import runtime


class ProjectMcpCommandTests(unittest.TestCase):
    def invoke(self, result, *options):
        output = io.StringIO()
        with patch.object(sys, 'argv', ['runtime.py', '--project-root', '/project',
                                      'project-mcp', *options]), \
             patch('project_mcp_launcher.Launcher.launch', return_value=result) as launch, \
             patch.object(runtime, 'Runtime', side_effect=AssertionError('legacy worker must not start')), \
             patch.dict(runtime.os.environ, {'CAPRMEDIO_MCP_HTTP_SECRET_TOKEN': 'synthetic-cli-token'}), \
             redirect_stdout(output):
            code = runtime.main()
        self.assertNotIn('synthetic-cli-token', output.getvalue())
        return code, output.getvalue(), launch

    def test_json_ready_and_url_ready_outputs(self):
        result = {'disposition': 'started', 'condition': 'READY_STARTED',
                  'readiness': True, 'url': 'http://127.0.0.1:8099/mcp'}
        code, output, launch = self.invoke(result)
        self.assertEqual(0, code)
        self.assertEqual(result, json.loads(output))
        self.assertEqual(Path('/project'), launch.call_args.args[0])
        code, output, _ = self.invoke(result, '--output', 'url')
        self.assertEqual(0, code)
        self.assertEqual(result['url'], output.strip())

    def test_each_failure_stays_json_nonzero_even_in_url_mode(self):
        for disposition, condition in [('refused', 'PROJECT_SELECTION_REFUSED'),
            ('failed', 'BUILD_FAILED'), ('busy', 'PROJECT_LOCK_BUSY'),
            ('failed', 'READINESS_FAILED')]:
            with self.subTest(condition=condition):
                result = {'disposition': disposition, 'condition': condition, 'readiness': False}
                code, output, _ = self.invoke(result, '--output', 'url', '--no-build')
                self.assertEqual(1, code)
                self.assertEqual(result, json.loads(output))
                self.assertNotIn('url', json.loads(output))

    def test_source_root_build_switch_and_time_bounds_forward_exactly(self):
        result = {'disposition': 'failed', 'condition': 'IMAGE_INPUT_UNAVAILABLE', 'readiness': False}
        _, _, launch = self.invoke(result, '--source-root', '/source', '--no-build',
                                   '--startup-timeout', '20', '--build-timeout', '120')
        self.assertEqual(Path('/source'), launch.call_args.kwargs['source_root'])
        self.assertFalse(launch.call_args.kwargs['build_if_missing'])
        self.assertEqual(20, launch.call_args.kwargs['timeout'])
        self.assertEqual(120, launch.call_args.kwargs['build_timeout'])


if __name__ == '__main__':
    unittest.main()
