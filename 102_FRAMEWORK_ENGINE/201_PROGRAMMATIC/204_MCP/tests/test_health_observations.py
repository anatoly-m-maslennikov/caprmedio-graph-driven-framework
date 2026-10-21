"""Bounded, process-local MCP health observations."""
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import sys
import unittest


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))
from health_observations import HealthObservations  # noqa: E402


SAFE_ERROR_CATEGORIES = {"timeout", "connection", "returned-error", "uncertain"}
SAFE_OUTCOMES = {
    "completed", "no_op", "failed", "partial", "cancelled", "interrupted_pending",
    "uncertain", "rejected", "returned", "success", "unknown",
}
SAFE_DISPOSITIONS = {"terminal", "started", "queued", "recording_pending", "uncertain", "unknown"}
FORBIDDEN_FIELDS = {"args", "arguments", "response", "result", "path", "provider_error"}


def _row_error(row):
    return row.get("error_category", row.get("error"))


def _run_id(row):
    return row.get("run_id", row.get("workflow_run_id", row.get("actual_run_id")))


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
        self.assertEqual({"started_at", "calls", "workflows"}, set(snapshot))
        self.assertEqual(started_at, snapshot["started_at"])
        self.assertEqual(32, len(snapshot["calls"]))
        self.assertEqual([f"tool-{index}" for index in range(8, 40)],
                         [row["name"] for row in snapshot["calls"]])
        self.assertEqual([], snapshot["workflows"])

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

    def test_workflow_observations_keep_scheduler_and_actual_state_separate(self):
        self.observations.record(
            "workflow_orchestrator",
            {"request": {"run_id": "requested-pending", "secret": "SECRET_ARGUMENT"}},
            {
                "workflow_run_id": "actual-pending",
                "scheduler_status": "SUCCESS",
                "outcome": "interrupted_pending",
                "disposition": "started",
            },
        )
        self.observations.record(
            "workflow_orchestrator",
            {"request": {"run_id": "requested-unknown", "secret": "SECRET_ARGUMENT"}},
            {"workflow_run_id": "actual-unknown", "scheduler_status": "SUCCESS"},
        )

        snapshot = self.observations.snapshot()
        self.assertEqual(2, len(snapshot["calls"]))
        self.assertEqual({"workflow_orchestrator"}, {row["name"] for row in snapshot["calls"]})
        self.assertEqual(2, len(snapshot["workflows"]))
        pending, unknown = snapshot["workflows"]
        self.assertEqual("actual-pending", _run_id(pending))
        self.assertNotEqual("requested-pending", _run_id(pending))
        self.assertEqual("SUCCESS", pending["scheduler_status"])
        self.assertEqual("interrupted_pending", pending["outcome"])
        self.assertEqual("started", pending["disposition"])
        self.assertEqual("SUCCESS", unknown["scheduler_status"])
        self.assertEqual("unknown", unknown["outcome"])
        self.assertEqual("actual-unknown", _run_id(unknown))
        for row in snapshot["workflows"]:
            self.assertIn(row["outcome"], SAFE_OUTCOMES)
            self.assertIn(row["disposition"], SAFE_DISPOSITIONS)
        encoded = json.dumps(snapshot, sort_keys=True)
        self.assertNotIn("SECRET_ARGUMENT", encoded)

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
        self.assertEqual([], snapshot["workflows"])
        self.assertIsInstance(snapshot["started_at"], str)


if __name__ == "__main__":
    unittest.main()
