"""Functional gateway-call and bounded-retention checks for MCP health."""
import asyncio
import json
from pathlib import Path
import sys
from mcp import types

sys.path.insert(0, str(Path(__file__).resolve().parent))
from health_fixture import HealthHTTPFixture, PROVIDER_DIAGNOSTIC, SECRET


SAFE_ERROR_CATEGORIES = {"timeout", "connection", "returned-error", "uncertain"}
SAFE_OUTCOMES = {
    "completed", "no_op", "failed", "partial", "cancelled", "interrupted_pending",
    "uncertain", "rejected", "returned", "success", "unknown",
}
SAFE_DISPOSITIONS = {"terminal", "started", "queued", "recording_pending", "uncertain", "unknown"}


class HealthGatewayCallTests(HealthHTTPFixture):
    async def test_real_gateway_calls_are_observed_without_payloads_or_provider_text(self):
        async with self.lifespan():
            client, transport, session = await self.session()
            try:
                returned = await session.call_tool("query_schema", {"secret": SECRET})
                rejected = await session.call_tool("not_registered", {})
                partial = await session.call_tool("query_page", {})
                unsafe = await session.call_tool("query_load", {})
                uncertain = await session.call_tool("query_check", {})
                self.assertFalse(returned.is_error)
                self.assertTrue(rejected.is_error)
                self.assertFalse(partial.is_error)
                self.assertFalse(unsafe.is_error)
                self.assertTrue(uncertain.is_error)

                snapshot = self.app.gateway.health_observations.snapshot()
                self.assertNotIn("workflows", snapshot)
                rows = {row["name"]: row for row in snapshot["calls"]}
                self.assertTrue({"query_schema", "not_registered", "query_page", "query_load", "query_check"} <= set(rows))
                self.assertIn(self.outcome(rows["query_schema"]), {"completed", "returned", "success", "no_op"})
                self.assertEqual("rejected", self.outcome(rows["not_registered"]))
                self.assertIn(self.outcome(rows["query_page"]), {"partial", "failed", "returned"})
                self.assertIn(self.outcome(rows["query_load"]), SAFE_OUTCOMES)
                self.assertIn(self.outcome(rows["query_check"]), {"returned", "uncertain", "failed"})
                for row in rows.values():
                    error = row.get("error_category", row.get("error"))
                    if error is not None:
                        self.assertIn(error, SAFE_ERROR_CATEGORIES)
                    if row.get("outcome") is not None:
                        self.assertIn(row["outcome"], SAFE_OUTCOMES)
                    if row.get("disposition") is not None:
                        self.assertIn(row["disposition"], SAFE_DISPOSITIONS)
                encoded = json.dumps(snapshot, sort_keys=True)
                for secret in (SECRET, "fixture-result", PROVIDER_DIAGNOSTIC, "/fixture/absolute/path"):
                    self.assertNotIn(secret, encoded)
                for row in snapshot["calls"]:
                    for forbidden in ("arguments", "response", "result"):
                        self.assertNotIn(forbidden, row)
            finally:
                await self.close_session(client, transport, session)

    async def test_concurrent_real_calls_keep_names_and_histories_isolated(self):
        async with self.lifespan():
            client, transport, session = await self.session()
            try:
                await asyncio.gather(
                    *(session.call_tool(name, {"delay": 0.02}) for name in ("workspace_list", "query_saved_list") * 4)
                )
                rows = self.app.gateway.health_observations.snapshot()["calls"]
                self.assertEqual(8, len(rows))
                self.assertEqual({"workspace_list", "query_saved_list"}, {row["name"] for row in rows})
                self.assertNotIn("worker", json.dumps(rows))
            finally:
                await self.close_session(client, transport, session)

    async def test_cancelled_real_gateway_call_propagates_and_is_not_returned(self):
        async with self.lifespan():
            pending = asyncio.create_task(self.app.gateway.call(
                None, types.CallToolRequestParams(name="query_run", arguments={"delay": 30.0})))
            try:
                marker = ""
                for _ in range(50):
                    marker = self.marker.read_text() if self.marker.exists() else ""
                    if "slow-started" in marker:
                        break
                    await asyncio.sleep(0.02)
                self.assertIn("slow-started", marker)
                pending.cancel()
                with self.assertRaises(asyncio.CancelledError):
                    await pending
                rows = [row for row in self.app.gateway.health_observations.snapshot()["calls"]
                        if row["name"] == "query_run"]
                self.assertEqual(1, len(rows))
                self.assertIn(self.outcome(rows[0]), {"uncertain", "interrupted_pending"})
                self.assertNotEqual("returned", self.outcome(rows[0]))
            finally:
                if not pending.done():
                    pending.cancel()
                    with self.assertRaises(asyncio.CancelledError):
                        await pending

    async def test_process_local_observer_is_bounded_and_restart_resets_history(self):
        async with self.lifespan():
            observations = self.app.gateway.health_observations
            for index in range(40):
                observations.record(f"tool-{index}", {}, {"outcome": "completed"})
            snapshot = observations.snapshot()
            self.assertEqual(32, len(snapshot["calls"]))
            self.assertEqual([f"tool-{index}" for index in range(8, 40)],
                             [row["name"] for row in snapshot["calls"]])

        second = self.new_app()
        self.assertEqual([], second.gateway.health_observations.snapshot()["calls"])
        self.assertNotIn("workflows", second.gateway.health_observations.snapshot())
