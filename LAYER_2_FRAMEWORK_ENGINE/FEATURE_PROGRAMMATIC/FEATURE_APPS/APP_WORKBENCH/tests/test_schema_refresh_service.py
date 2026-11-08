# CA-E-675@6
# CA-E-677@14
"""Publish source delta state only after the database accepts it."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import sys
import unittest
from unittest.mock import ANY, Mock, call, patch

APP_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(APP_ROOT))
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.content_schema import compile_content_schema  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.index_delta import MaterializationDelta  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService  # noqa: E402

PREFIX = "APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service."
EVENT = {"operation": "update", "old_path": None, "new_path": "source/ordinary.md"}


class SchemaRefreshServiceTests(unittest.TestCase):
    def service(self, *, changed=True, captures=None):
        rows, scopes = [{"source_path": "source/ordinary.md"}], [{"name": "project"}]
        reader = Mock(capture=Mock(return_value=(rows, scopes)), excluded_count=0,
                      capture_changed=changed, capture_delta={EVENT["new_path"]: rows[0]},
                      content_schema=compile_content_schema([]))
        if captures is not None:
            reader.capture.side_effect = captures
        with patch(PREFIX + "SourceReader", return_value=reader):
            service = WorkbenchService(Path("/project"))
        service._store = Mock(apply=Mock(return_value=True), schema_changed=False)
        service._relation_state = Mock()
        return service, reader, rows, scopes

    def test_ordinary_delta_does_not_request_a_full_source_capture(self):
        service, reader, rows, scopes = self.service()
        old_state, next_state = service._relation_state, Mock()
        delta = MaterializationDelta({}, {EVENT["new_path"]: rows[0]}, {}, {})
        with patch(PREFIX + "materialize_delta", return_value=(rows, scopes, set(), {}, next_state, delta)) as materialize, redirect_stdout(StringIO()):
            service._refresh([EVENT])
        reader.capture.assert_called_once_with([EVENT])
        materialize.assert_called_once_with(rows, scopes, old_state, changes=reader.capture_delta)
        service._store.apply.assert_called_once_with(rows, scopes, relation_types=set(), content_schema=reader.content_schema, delta=delta)
        service._store.replace.assert_not_called()
        self.assertIs(next_state, service._relation_state)

    def test_schema_change_recaptures_then_replaces_without_touching_results(self):
        final = [{"source_path": "source/after.md"}]
        service, reader, rows, scopes = self.service()
        reader.capture.side_effect = [(rows, scopes), (final, scopes)]
        service._store.schema_changed = True
        old_state, next_state = service._relation_state, Mock()
        delta = MaterializationDelta({}, {EVENT["new_path"]: rows[0]}, {}, {})
        with patch(PREFIX + "materialize_delta", side_effect=[(rows, scopes, set(), {}, Mock(), delta), (final, scopes, set(), {}, next_state, None)]) as materialize, redirect_stdout(StringIO()):
            service._refresh([EVENT])
        reader.capture.assert_has_calls([call([EVENT]), call()])
        materialize.assert_has_calls([call(rows, scopes, old_state, changes=reader.capture_delta), call(final, scopes, old_state)])
        service._store.replace.assert_called_once_with(
            final, scopes, relation_types=set(), content_schema=reader.content_schema, header_schema=ANY,
        )
        service._store.drop.assert_not_called()
        service._store.unpin.assert_not_called()
        self.assertIs(next_state, service._relation_state)

    def test_no_source_change_skips_materialization_and_database(self):
        service, reader, rows, scopes = self.service(changed=False)
        prior = service._relation_state
        with patch(PREFIX + "materialize_delta") as materialize, redirect_stdout(StringIO()) as output:
            service._refresh([EVENT])
        materialize.assert_not_called()
        service._store.apply.assert_not_called()
        service._store.replace.assert_not_called()
        self.assertIs(prior, service._relation_state)
        self.assertIsNotNone(service.sync_status()["last_synced_at"])
        self.assertIn("changed=false", output.getvalue())

    def test_failed_database_write_does_not_publish_reused_state(self):
        service, reader, rows, scopes = self.service()
        service._store.apply.side_effect = RuntimeError("write failed")
        prior = service._relation_state
        delta = MaterializationDelta({}, {EVENT["new_path"]: rows[0]}, {}, {})
        with patch(PREFIX + "materialize_delta", return_value=(rows, scopes, set(), {}, Mock(), delta)):
            with self.assertRaisesRegex(RuntimeError, "write failed"):
                service._refresh([EVENT])
        self.assertIs(prior, service._relation_state)
        self.assertIsNone(service.sync_status()["last_synced_at"])


if __name__ == "__main__":
    unittest.main()
