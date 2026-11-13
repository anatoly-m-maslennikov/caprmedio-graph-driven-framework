"""Bounded, process-local MCP health observations."""
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))
from health_observations import HealthObservations  # noqa: E402


SAFE_ERROR_CATEGORIES = {"timeout", "connection", "returned-error", "uncertain"}
FORBIDDEN_FIELDS = {"args", "arguments", "response", "result", "path", "provider_error"}


def _row_error(row):
    return row.get("error_category", row.get("error"))




class HealthObservationsTests(unittest.TestCase):
    def setUp(self):
        self.observations = HealthObservations()

    def test_snapshot_is_since_start_bounded_and_redacted(self):
        snapshot = self.observations.snapshot()
        started_at = snapshot["started_at"]
        for index in range(40):
            self.observations.record(
                f"tool-{index}",
                {"token": "SECRET_ARGUMENT", "path": "/private/argument/path"},
                {"result": "SECRET_RESULT", "path": "/private/result/path"},
            )

        snapshot = self.observations.snapshot()
        self.assertEqual({"started_at", "calls"}, set(snapshot))
        self.assertEqual(started_at, snapshot["started_at"])
        self.assertEqual(32, len(snapshot["calls"]))
        self.assertEqual([f"tool-{index}" for index in range(8, 40)],
                         [row["name"] for row in snapshot["calls"]])
        self.assertNotIn("workflows", snapshot)

        encoded = json.dumps(snapshot, sort_keys=True)
        for secret in ("SECRET_ARGUMENT", "SECRET_RESULT", "/private/argument/path",
                       "/private/result/path"):
            self.assertNotIn(secret, encoded)
        for row in snapshot["calls"]:
            self.assertTrue(FORBIDDEN_FIELDS.isdisjoint(row))

    def test_safe_error_categories_preserve_uncertainty_without_provider_text(self):
        provider_message = "provider exception /srv/project/secret SECRET_PROVIDER_TEXT"
        self.observations.record("timeout-tool", {}, None, error=TimeoutError(provider_message))
        self.observations.record("connection-tool", {}, None, error=ConnectionError(provider_message))
        self.observations.record("failed-tool", {}, {"outcome": "failed"},
                                 error=RuntimeError(provider_message))
        self.observations.record("uncertain-tool", {}, None, error=RuntimeError(provider_message))
        snapshot = self.observations.snapshot()

        self.assertEqual(4, len(snapshot["calls"]))
        categories = {_row_error(row) for row in snapshot["calls"]}
        self.assertTrue(categories <= SAFE_ERROR_CATEGORIES)
        self.assertIn("timeout", categories)
        self.assertIn("connection", categories)
        self.assertEqual("uncertain", snapshot["calls"][-1]["outcome"])
        encoded = json.dumps(snapshot, sort_keys=True)
        self.assertNotIn(provider_message, encoded)
        self.assertNotIn("/srv/project/secret", encoded)
        self.assertNotIn("SECRET_PROVIDER_TEXT", encoded)


    def test_invalid_tool_names_do_not_become_truncated_paths(self):
        self.observations.record("../../private/provider-secret", {}, {"outcome": "completed"})
        row = self.observations.snapshot()["calls"][-1]
        self.assertIn(row["name"], {"unknown"})
        self.assertRegex(row["name"], r"^[A-Za-z0-9_.-]{1,128}$|^unknown$")
        self.assertNotIn("/", row["name"])

    def test_concurrent_records_remain_bounded_and_do_not_leak_payloads(self):
        def record(index):
            self.observations.record(
                "alpha" if index % 2 == 0 else "beta",
                {"token": f"TOKEN-{index}"},
                {"outcome": "completed", "result": f"RESULT-{index}"},
            )

        with ThreadPoolExecutor(max_workers=8) as executor:
            list(executor.map(record, range(64)))

        snapshot = self.observations.snapshot()
        self.assertEqual(32, len(snapshot["calls"]))
        self.assertEqual({"alpha", "beta"}, {row["name"] for row in snapshot["calls"]})
        encoded = json.dumps(snapshot, sort_keys=True)
        self.assertNotIn("TOKEN-", encoded)
        self.assertNotIn("RESULT-", encoded)

    def test_new_observer_starts_empty(self):
        self.observations.record("old", {}, {"outcome": "completed"})
        restarted = HealthObservations()
        snapshot = restarted.snapshot()
        self.assertEqual([], snapshot["calls"])
        self.assertNotIn("workflows", snapshot)
        self.assertIsInstance(snapshot["started_at"], str)

    def test_typed_lifecycle_statuses_and_mcp_error_are_not_rpc_success(self):
        for status in ("completed", "needs_input", "cancelled", "failed", "blocked", "partial"):
            self.observations.record("lifecycle", {}, SimpleNamespace(
                structured_content={"status": status, "errors": ["private"]}, is_error=False))
        self.observations.record("error", {}, SimpleNamespace(
            structured_content={"detail": "private"}, is_error=True))
        rows = self.observations.snapshot()["calls"]
        self.assertEqual(["completed", "needs_input", "cancelled", "failed", "blocked", "partial", "failed"],
                         [row["outcome"] for row in rows])
        self.assertEqual("returned-error", rows[-1]["error_category"])
        self.assertNotIn("private", json.dumps(rows))


if __name__ == "__main__":
    unittest.main()
