"""Functional HTTP checks for the same-listener MCP health view."""
from pathlib import Path
import sys
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent))
from health_fixture import HealthHTTPFixture, PROVIDER_DIAGNOSTIC, SECRET
from health_page import render_health_page


SAFE_OUTCOMES = {
    "completed", "no_op", "failed", "partial", "cancelled", "interrupted_pending",
    "uncertain", "rejected", "returned", "success", "unknown",
}
SAFE_DISPOSITIONS = {"terminal", "started", "queued", "recording_pending", "uncertain", "unknown"}


class HTTPHealthPageTests(HealthHTTPFixture):
    def test_renderer_escapes_dynamic_snapshot_fields(self):
        gateway = SimpleNamespace(
            active=SimpleNamespace(task=SimpleNamespace(done=lambda: False), tools=[])
        )
        html = render_health_page(
            {
                "started_at": "<script>bad</script>",
                "calls": [{"observed_at": "<b>", "name": "<script>", "outcome": "returned"}],
                "workflows": [],
            },
            ready=True,
            gateway=gateway,
        )
        self.assertIn("&lt;script&gt;", html)
        self.assertNotIn("<script>bad</script>", html)

    async def test_machine_readiness_and_explicit_html_negotiation(self):
        async with self.lifespan():
            async with self.raw_client() as client:
                for accept in (None, "application/json", "*/*"):
                    headers = self.headers()
                    if accept is not None:
                        headers["accept"] = accept
                    response = await client.get("/health", headers=headers)
                    self.assertEqual(200, response.status_code)
                    self.assertEqual({"ready": True}, response.json())

                response = await client.get(
                    "/health", headers=self.headers(accept="text/html;q=1,application/json;q=0.8")
                )
                self.assertEqual(200, response.status_code)
                self.assertTrue(response.headers["content-type"].startswith("text/html"))
                self.assertIn("<html", response.text.lower())

                response = await client.get(
                    "/health", headers=self.headers(accept="text/html;q=0,application/json;q=1")
                )
                self.assertEqual(200, response.status_code)
                self.assertEqual({"ready": True}, response.json())

                response = await client.get(
                    "/health",
                    headers=self.headers(accept="text/html;q=.8,application/json;q=0,*/*;q=1"),
                )
                self.assertEqual(200, response.status_code)
                self.assertTrue(response.headers["content-type"].startswith("text/html"))

                self.app.gateway.active = None
                response = await client.get("/health", headers=self.headers())
                self.assertEqual(503, response.status_code)
                self.assertEqual({"ready": False}, response.json())
                response = await client.get("/health", headers=self.headers(accept="text/html;q=1"))
                self.assertEqual(503, response.status_code)
                self.assertTrue(response.headers["content-type"].startswith("text/html"))

    async def test_workflow_scheduler_success_does_not_promote_unknown_or_pending(self):
        async with self.lifespan():
            observations = self.app.gateway.health_observations
            observations.record(
                "workflow_orchestrator",
                {"request": {"run_id": "requested-pending", "token": SECRET}},
                {"workflow_run_id": "actual-pending", "scheduler_status": "SUCCESS",
                 "outcome": "interrupted_pending", "disposition": "started"},
            )
            observations.record(
                "workflow_orchestrator",
                {"request": {"run_id": "requested-unknown", "token": SECRET}},
                {"workflow_run_id": "actual-unknown", "scheduler_status": "SUCCESS"},
            )
            snapshot = observations.snapshot()
            self.assertEqual(2, len(snapshot["calls"]))
            self.assertEqual({"workflow_orchestrator"}, {row["name"] for row in snapshot["calls"]})
            self.assertEqual(2, len(snapshot["workflows"]))
            self.assertEqual("actual-pending", self.run_id(snapshot["workflows"][0]))
            self.assertNotEqual("requested-pending", self.run_id(snapshot["workflows"][0]))
            self.assertEqual("SUCCESS", snapshot["workflows"][0]["scheduler_status"])
            self.assertEqual("interrupted_pending", snapshot["workflows"][0]["outcome"])
            self.assertEqual("unknown", snapshot["workflows"][1]["outcome"])
            self.assertEqual("actual-unknown", self.run_id(snapshot["workflows"][1]))
            for row in snapshot["workflows"]:
                self.assertIn(row["outcome"], SAFE_OUTCOMES)
                self.assertIn(row["disposition"], SAFE_DISPOSITIONS)

            async with self.raw_client() as client:
                response = await client.get("/health", headers=self.headers(accept="text/html;q=1"))
            self.assertEqual(200, response.status_code)
            rendered = response.text.lower()
            self.assertIn("active gateway generation readiness", rendered)
            self.assertIn("provider and worker health are not probed", rendered)
            self.assertIn("observations are historical", rendered)
            for text in ("scheduler", "interrupted_pending", "unknown"):
                self.assertIn(text, rendered)
            self.assertNotIn(SECRET, response.text)

    async def test_html_escapes_dynamic_fields_and_get_has_no_execution_effect(self):
        async with self.lifespan():
            observations = self.app.gateway.health_observations
            observations.record(
                "<script>alert('x')</script>",
                {"token": SECRET, "path": "/private/request/path"},
                {"outcome": "failed", "result": SECRET},
                error=RuntimeError(PROVIDER_DIAGNOSTIC),
            )
            before = observations.snapshot()
            marker_before = self.marker.read_text(encoding="utf-8") if self.marker.exists() else ""
            files_before = sorted(
                path.relative_to(self.root).as_posix()
                for path in self.root.rglob("*")
                if path.is_file() and ("journal" in path.name.lower() or "dbos" in path.name.lower())
            )
            async with self.raw_client() as client:
                response = await client.get("/health", headers=self.headers(accept="text/html;q=1"))
                self.assertEqual(200, response.status_code)
                self.assertNotIn("<script>alert", response.text)
                for secret in (SECRET, "/private/request/path", PROVIDER_DIAGNOSTIC):
                    self.assertNotIn(secret, response.text)
                self.assertEqual(421, (await client.get(
                    "/health", headers=self.headers(host="attacker.invalid")
                )).status_code)
                self.assertEqual(403, (await client.get(
                    "/health", headers=self.headers(origin="https://attacker.invalid")
                )).status_code)
            self.assertEqual(before, observations.snapshot())
            marker_after = self.marker.read_text(encoding="utf-8") if self.marker.exists() else ""
            self.assertEqual(marker_before, marker_after)
            files_after = sorted(
                path.relative_to(self.root).as_posix()
                for path in self.root.rglob("*")
                if path.is_file() and ("journal" in path.name.lower() or "dbos" in path.name.lower())
            )
            self.assertEqual(files_before, files_after)
