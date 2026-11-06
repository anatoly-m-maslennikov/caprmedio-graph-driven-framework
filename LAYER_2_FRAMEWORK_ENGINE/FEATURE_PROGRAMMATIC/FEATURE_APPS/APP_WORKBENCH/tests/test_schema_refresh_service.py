# CA-E-675@6
# CA-E-677@13
"""Service rebuilds only when the QueryStore detects a Header-schema change."""

from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock, call, patch


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(APP_ROOT))

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relations import canonical  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService  # noqa: E402


class SchemaRefreshServiceTests(unittest.TestCase):
    @staticmethod
    def _rows(name: str) -> list[dict[str, str]]:
        return [{"source_path": f"source/{name}.md"}]

    @staticmethod
    def _scopes() -> list[dict[str, str]]:
        return [{"name": "project"}]

    def _service(self, reader: Mock) -> WorkbenchService:
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader", return_value=reader):
            return WorkbenchService(Path("/project"))

    def _prepare_delta(self, service: WorkbenchService, scopes: list[dict[str, str]]) -> None:
        service._scope_signature = canonical(scopes)
        service._relation_registry = canonical([[], []])

    def test_ordinary_delta_does_not_request_a_full_source_capture(self) -> None:
        rows, scopes = self._rows("ordinary"), self._scopes()
        reader = Mock(capture=Mock(return_value=(rows, scopes)), excluded_count=0, capture_changed=True)
        service = self._service(reader)
        store = Mock(apply=Mock(return_value=True), schema_changed=False)
        service._store = store
        self._prepare_delta(service, scopes)

        with (
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.materialize_with_registry", return_value=(rows, scopes, set(), {}, {})) as materialize,
            redirect_stdout(StringIO()),
        ):
            service._refresh([{"operation": "update", "old_path": None, "new_path": "source/ordinary.md"}])

        reader.capture.assert_called_once_with([{"operation": "update", "old_path": None, "new_path": "source/ordinary.md"}])
        store.apply.assert_called_once_with(rows, scopes, relation_types=set())
        store.replace.assert_not_called()
        self.assertEqual(1, materialize.call_count)

    def test_schema_change_recaptures_then_replaces_without_touching_results(self) -> None:
        initial_rows, final_rows, scopes = self._rows("before"), self._rows("after"), self._scopes()
        reader = Mock(capture=Mock(side_effect=[(initial_rows, scopes), (final_rows, scopes)]), excluded_count=0, capture_changed=True)
        service = self._service(reader)
        store = Mock(apply=Mock(return_value=True), schema_changed=True)
        service._store = store
        self._prepare_delta(service, scopes)

        with (
            patch(
                "APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.materialize_with_registry",
                side_effect=[(initial_rows, scopes, set(), {}, {"before": {}}), (final_rows, scopes, set(), {}, {"after": {}})],
            ),
            redirect_stdout(StringIO()),
        ):
            service._refresh([{"operation": "update", "old_path": None, "new_path": "source/before.md"}])

        reader.capture.assert_has_calls([
            call([{"operation": "update", "old_path": None, "new_path": "source/before.md"}]),
            call(),
        ])
        store.apply.assert_called_once_with(initial_rows, scopes, relation_types=set())
        store.replace.assert_called_once_with(final_rows, scopes, relation_types=set())
        store.drop.assert_not_called()
        store.unpin.assert_not_called()
        self.assertEqual({"after": {}}, service._materialized_atoms)

    def test_no_source_change_skips_materialization_and_database(self) -> None:
        rows, scopes = self._rows("unchanged"), self._scopes()
        reader = Mock(capture=Mock(return_value=(rows, scopes)), excluded_count=0, capture_changed=False)
        service = self._service(reader)
        service._store = Mock()
        prior = {"unchanged": {}}
        service._materialized_atoms = prior
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.materialize_with_registry") as materialize, redirect_stdout(StringIO()) as output:
            service._refresh([{"operation": "update", "old_path": None, "new_path": "source/unchanged.md"}])
        materialize.assert_not_called()
        service._store.apply.assert_not_called()
        service._store.replace.assert_not_called()
        self.assertIs(prior, service._materialized_atoms)
        self.assertIsNotNone(service.sync_status()["last_synced_at"])
        self.assertIn("changed=false", output.getvalue())

    def test_failed_database_write_does_not_publish_reused_state(self) -> None:
        rows, scopes = self._rows("changed"), self._scopes()
        reader = Mock(capture=Mock(return_value=(rows, scopes)), excluded_count=0, capture_changed=True)
        service = self._service(reader)
        self._prepare_delta(service, scopes)
        service._store = Mock(apply=Mock(side_effect=RuntimeError("write failed")))
        prior = {"prior": {}}
        service._materialized_atoms = prior
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.materialize_with_registry", return_value=(rows, scopes, set(), {}, {"next": {}})) as materialize:
            with self.assertRaisesRegex(RuntimeError, "write failed"):
                service._refresh([{"operation": "update", "old_path": None, "new_path": "source/changed.md"}])
        materialize.assert_called_once_with(rows, scopes, prior)
        self.assertIs(prior, service._materialized_atoms)
        self.assertIsNone(service.sync_status()["last_synced_at"])


if __name__ == "__main__":
    unittest.main()
