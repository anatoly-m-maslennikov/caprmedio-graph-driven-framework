from contextlib import nullcontext, redirect_stdout
import io
import json
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE import backend, effects  # noqa: E402
from ATOM_LIFECYCLE.placement import PlacementError  # noqa: E402
from ATOM_LIFECYCLE.timing import lifecycle_tool, span, trace  # noqa: E402

SELECTION = SimpleNamespace(root=Path('/project'), settings={'artifacts': {'identity': {'project_prefix': 'CA'}}})


class LifecycleTimingTests(unittest.TestCase):
    def test_all_tools_emit_start_and_done_without_inputs(self):
        model = SimpleNamespace(candidate_schema=SimpleNamespace(placement=object()))

        @trace('validation.candidate')
        def action(_selection, _model, _params):
            return {'outcome': 'completed', 'effects': [], 'errors': []}

        output = io.StringIO()
        with (patch.object(backend, '_project_write_lock', return_value=nullcontext()),
              patch.object(backend, 'bind_placement', return_value=nullcontext()),
              patch.dict(backend.ROUTES, {name: action for name in backend.ROUTES}),
              redirect_stdout(output)):
            for name in backend.ROUTES:
                backend.execute(SELECTION, model, name, {'secret': 'never-log-this'})

        logs = output.getvalue()
        rows = [json.loads(line) for line in logs.splitlines()]
        for name in backend.ROUTES:
            self.assertEqual(
                [(row['code'], row['outcome']) for row in rows if row['operation'] == name],
                [('execute', 'started'), ('validation.candidate', 'started'),
                 ('validation.candidate', 'done'), ('execute', 'done')],
            )
        self.assertTrue(all(row['severity'] == 'INFO' and row['project_prefix'] == 'CA' for row in rows))
        self.assertTrue(all(row['elapsed_ms'] >= 0 for row in rows if row['outcome'] == 'done'))
        self.assertNotIn('never-log-this', logs)

    def test_returned_errors_and_exceptions_emit_failed(self):
        @trace('filesystem.create')
        def failure():
            return effects.Result(errors=[{'message': 'private'}])

        @lifecycle_tool
        def execute(_selection, _model, _name, _params):
            failure()
            return {'outcome': 'failed', 'errors': [{'message': 'private'}]}

        output = io.StringIO()
        with redirect_stdout(output):
            execute(SELECTION, None, 'atom_lifecycle_update', {})
            with self.assertRaisesRegex(ValueError, 'private'):
                with span('project_refresh', tool='atom_lifecycle_update', selection=SELECTION):
                    raise ValueError('private')
        logs = output.getvalue()
        self.assertEqual(
            {row['code'] for row in map(json.loads, logs.splitlines()) if row['outcome'] == 'failed'},
            {'filesystem.create', 'execute', 'project_refresh'},
        )
        self.assertNotIn('private', logs)

    def test_backend_reports_placement_error_and_logs_its_type(self):
        model = SimpleNamespace(candidate_schema=SimpleNamespace(placement=object()))
        name = 'atom_lifecycle_create_draft'

        @trace('placement.derive_destination')
        def action(_selection, _model, _params):
            raise PlacementError('Unsupported Summary serialization')

        output = io.StringIO()
        with (patch.object(backend, '_project_write_lock', return_value=nullcontext()),
              patch.object(backend, 'bind_placement', return_value=nullcontext()),
              patch.dict(backend.ROUTES, {name: action}), redirect_stdout(output)):
            result = backend.execute(SELECTION, model, name, {'summary': 'private value'})

        self.assertEqual(result['effects'], [])
        self.assertEqual(result['errors'], [{'code': 'invalid_placement',
                         'message': 'Unsupported Summary serialization', 'field': None}])
        rows = [json.loads(line) for line in output.getvalue().splitlines()]
        self.assertTrue(any(row['code'] == 'placement.derive_destination'
                            and row.get('exception_class') == 'PlacementError' for row in rows))
        self.assertNotIn('private value', output.getvalue())

    def test_logging_failure_does_not_change_operation_result(self):
        @lifecycle_tool
        def execute(_selection, _model, _name, _params):
            return {'outcome': 'completed'}

        output = io.StringIO()
        output.close()
        with redirect_stdout(output):
            self.assertEqual(execute(SELECTION, None, 'atom_lifecycle_archive', {}), {'outcome': 'completed'})


if __name__ == '__main__':
    unittest.main()
