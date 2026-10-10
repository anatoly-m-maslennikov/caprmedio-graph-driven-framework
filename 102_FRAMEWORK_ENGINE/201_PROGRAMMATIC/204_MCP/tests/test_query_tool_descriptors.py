"""Descriptor and adapter proofs for the two native read-only query Tools."""
from __future__ import annotations

import importlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


MCP_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = MCP_ROOT.parent / "201_TOOLS"
TEST_TEMP_ROOT = MCP_ROOT.parents[2] / ".caprmedio_tmp"
for location in (MCP_ROOT, TOOLS_ROOT):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import registered_tool_registry as registry  # noqa: E402


ARTIFACT_ENTRYPOINT = (
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/"
    "FIND_AND_FETCH_ARTIFACTS/find_and_fetch_artifacts.py"
)
JOURNAL_ENTRYPOINT = (
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/"
    "FIND_AND_FETCH_JOURNAL_EVENTS/find_and_fetch_journal_events.py"
)


def _binding(name: str, mcp_name: str, entrypoint: str, delivery: int, action: int) -> dict[str, object]:
    return {
        "name": name,
        "mcp_name": mcp_name,
        "entrypoint": entrypoint,
        "action_ids": [f"CA-O-{action}"],
        "source_atom": f"CA-D-{delivery}",
        "source_path": f"methodology/{name}.md",
        "sha256": "a" * 64,
    }


class QueryToolDescriptorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.artifacts = importlib.import_module("FIND_AND_FETCH_ARTIFACTS.find_and_fetch_artifacts")
        cls.journal = importlib.import_module("FIND_AND_FETCH_JOURNAL_EVENTS.find_and_fetch_journal_events")

    def setUp(self) -> None:
        registry._MODULE_CACHE.clear()
        self.addCleanup(registry._MODULE_CACHE.clear)

    def test_descriptors_compile_without_creating_or_invoking_query_adapters(self) -> None:
        bindings = [
            _binding("FIND_AND_FETCH_ARTIFACTS", "artifact_query_provider", ARTIFACT_ENTRYPOINT, 551, 159),
            _binding("FIND_AND_FETCH_JOURNAL_EVENTS", "journal_query_provider", JOURNAL_ENTRYPOINT, 557, 162),
        ]

        snapshot = registry.compile_registry("descriptor-test-root", bindings)

        self.assertEqual({"artifact_query_provider", "journal_query_provider"}, snapshot.registered_names)
        self.assertEqual((), snapshot.quarantined)
        records = {record["name"]: record for record in snapshot.tools}
        for name, entrypoint, request_symbol, result_symbol, delivery, action in (
            ("FIND_AND_FETCH_ARTIFACTS", ARTIFACT_ENTRYPOINT, "ArtifactQueryRequest", "ArtifactQueryResult", "CA-D-551", "CA-O-159"),
            ("FIND_AND_FETCH_JOURNAL_EVENTS", JOURNAL_ENTRYPOINT, "JournalQueryRequest", "JournalQueryResult", "CA-D-557", "CA-O-162"),
        ):
            with self.subTest(tool=name):
                descriptor = records[name]["descriptor"]
                self.assertEqual(entrypoint, descriptor["models"]["input"]["module"])
                self.assertEqual(request_symbol, descriptor["models"]["input"]["symbol"])
                self.assertEqual(entrypoint, descriptor["models"]["output"]["module"])
                self.assertEqual(result_symbol, descriptor["models"]["output"]["symbol"])
                self.assertEqual({"delivery_atom_id": delivery, "action_ids": [action]}, descriptor["source_pins"])
                self.assertTrue(descriptor["effect_hints"]["read_only_hint"])
                self.assertFalse(descriptor["failure_contract"]["invokes_on_discovery"])
                self.assertNotIn("request", records[name]["input_schema"]["properties"])
                json.dumps(descriptor, sort_keys=True, allow_nan=False)

    def test_artifact_adapter_binds_root_and_preserves_the_native_query_request(self) -> None:
        returned = {
            "snapshot": {"reference": "snapshot:token", "token": "token", "digest": "digest"},
            "snapshot_reference": "snapshot:token",
            "examined_count": 1,
            "matched_count": 1,
            "returned_count": 1,
            "coverage": {"examined_count": 1, "matched_count": 1, "returned_count": 1, "complete": True, "incomplete": False},
            "has_more": False,
            "next_cursor": None,
            "results": [{"artifact_id": "A", "fm:/title": "One"}],
            "diagnostics": {"complete": True, "incomplete": False, "findings": []},
        }
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True) as temporary:
            root = Path(temporary)
            adapter = self.artifacts.create_adapter(root)
            request = self.artifacts.ArtifactQueryRequest(
                filter='"fm:/state" = "open"', select=["fm:/title"], limit=1,
            )
            with patch.object(self.artifacts, "query_artifacts", return_value=returned) as query:
                result = adapter.invoke(request)

        self.assertEqual("A", result.results[0]["artifact_id"])
        query.assert_called_once_with(
            root.resolve(),
            {"filter": '"fm:/state" = "open"', "select": ["fm:/title"], "limit": 1},
        )

    def test_artifact_adapter_refuses_unknown_input_before_native_query(self) -> None:
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True) as temporary:
            adapter = self.artifacts.create_adapter(temporary)
            with patch.object(self.artifacts, "query_artifacts") as query:
                with self.assertRaises(self.artifacts.ArtifactQueryError):
                    adapter.invoke({"root": "outside", "limit": 1})
        query.assert_not_called()

    def test_journal_adapter_preserves_frozen_filter_and_pagination(self) -> None:
        snapshot = {
            "snapshot_handle": "handle",
            "id": "snapshot-id",
            "source_root": ".caprmedio_fixture/_journal",
            "prefix_bytes": 10,
            "prefix_digest": "digest",
            "event_ids": ["E-1"],
        }
        returned = {
            "status": "complete",
            "snapshot": snapshot,
            "results": ["E-1"],
            "next_cursor": None,
            "coverage": {"scanned": 1, "matched": 1, "returned": 1, "complete": True},
            "limits": {},
            "findings": [],
        }
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True) as temporary:
            root = Path(temporary)
            adapter = self.journal.create_adapter(root)
            request = self.journal.JournalQueryRequest(
                filter='"event:/state" = "open"', limit=1,
            )
            with (
                patch.object(self.journal, "capture_snapshot", return_value=snapshot) as capture,
                patch.object(self.journal, "query", return_value=returned) as query,
            ):
                result = adapter.invoke(request)

        self.assertEqual("complete", result.status)
        capture.assert_called_once_with(root.resolve())
        query.assert_called_once_with(
            snapshot,
            {"filter": '"event:/state" = "open"', "mode": "ids", "limit": 1},
        )

    def test_journal_continuation_uses_only_returned_snapshot_and_rejects_partial_state(self) -> None:
        snapshot = {
            "snapshot_handle": "handle",
            "id": "snapshot-id",
            "source_root": ".caprmedio_fixture/_journal",
            "prefix_bytes": 10,
            "prefix_digest": "digest",
            "event_ids": ["E-1", "E-2"],
        }
        returned = {
            "status": "incomplete",
            "snapshot": snapshot,
            "results": ["E-2"],
            "next_cursor": "next",
            "coverage": {"scanned": 2, "matched": 2, "returned": 1, "complete": False},
            "limits": {},
            "findings": [],
        }
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True) as temporary:
            adapter = self.journal.create_adapter(temporary)
            continuation = self.journal.JournalQueryRequest(
                snapshot=self.journal.JournalQuerySnapshot.model_validate(snapshot),
                cursor="cursor",
                filter='"event:/state" = "open"',
                limit=1,
            )
            with (
                patch.object(self.journal, "capture_snapshot") as capture,
                patch.object(self.journal, "query", return_value=returned) as query,
            ):
                adapter.invoke(continuation)
            capture.assert_not_called()
            query.assert_called_once_with(
                snapshot,
                {"filter": '"event:/state" = "open"', "mode": "ids", "limit": 1, "cursor": "cursor"},
            )
            with patch.object(self.journal, "capture_snapshot") as capture:
                with self.assertRaises(self.journal.JournalQueryError):
                    adapter.invoke({"snapshot": snapshot})
            capture.assert_not_called()

    def test_bindings_are_exact_and_do_not_admit_a_different_delivery(self) -> None:
        artifact = _binding("FIND_AND_FETCH_ARTIFACTS", "artifact_query_provider", ARTIFACT_ENTRYPOINT, 551, 159)
        journal = _binding("FIND_AND_FETCH_JOURNAL_EVENTS", "journal_query_provider", JOURNAL_ENTRYPOINT, 557, 162)
        self.assertTrue(self.artifacts.binding_is_admitted(artifact))
        self.assertTrue(self.journal.binding_is_admitted(journal))
        artifact["source_atom"] = "CA-D-999"
        journal["action_ids"] = ["CA-O-999"]
        self.assertFalse(self.artifacts.binding_is_admitted(artifact))
        self.assertFalse(self.journal.binding_is_admitted(journal))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
