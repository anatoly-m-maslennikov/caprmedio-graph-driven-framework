"""Functional HTTP checks for the same-listener MCP health view."""
from pathlib import Path
import sys
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent))
from health_fixture import HealthHTTPFixture, PROVIDER_DIAGNOSTIC, SECRET
from health_page import render_health_page
from http_paths import HEALTH_PATH


class HTTPHealthPageTests(HealthHTTPFixture):
    def test_renderer_escapes_dynamic_snapshot_fields(self):
        gateway = SimpleNamespace(
            ready=True, tools=[]
        )
        html = render_health_page(
            {
                "started_at": "<script>bad</script>",
                "calls": [{"observed_at": "<b>", "name": "<script>", "outcome": "returned"}],
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
                    response = await client.get(HEALTH_PATH, headers=headers)
                    self.assertEqual(200, response.status_code)
                    self.assertEqual({"ready": True}, response.json())

                response = await client.get(
                    HEALTH_PATH, headers=self.headers(accept="text/html;q=1,application/json;q=0.8")
                )
                self.assertEqual(200, response.status_code)
                self.assertTrue(response.headers["content-type"].startswith("text/html"))
                self.assertIn("<html", response.text.lower())
                self.assertNotIn("Workflow", response.text)
                self.assertIn("Workbench health is not probed", response.text)

                response = await client.get(
                    HEALTH_PATH, headers=self.headers(accept="text/html;q=0,application/json;q=1")
                )
                self.assertEqual(200, response.status_code)
                self.assertEqual({"ready": True}, response.json())

                response = await client.get(
                    HEALTH_PATH,
                    headers=self.headers(accept="text/html;q=.8,application/json;q=0,*/*;q=1"),
                )
                self.assertEqual(200, response.status_code)
                self.assertTrue(response.headers["content-type"].startswith("text/html"))

                self.app.gateway.ready = False
                response = await client.get(HEALTH_PATH, headers=self.headers())
                self.assertEqual(503, response.status_code)
                self.assertEqual({"ready": False}, response.json())
                response = await client.get(HEALTH_PATH, headers=self.headers(accept="text/html;q=1"))
                self.assertEqual(503, response.status_code)
                self.assertTrue(response.headers["content-type"].startswith("text/html"))


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
                response = await client.get(HEALTH_PATH, headers=self.headers(accept="text/html;q=1"))
                self.assertEqual(200, response.status_code)
                self.assertNotIn("<script>alert", response.text)
                for secret in (SECRET, "/private/request/path", PROVIDER_DIAGNOSTIC):
                    self.assertNotIn(secret, response.text)
                self.assertEqual(421, (await client.get(
                    HEALTH_PATH, headers=self.headers(host="attacker.invalid")
                )).status_code)
                self.assertEqual(403, (await client.get(
                    HEALTH_PATH, headers=self.headers(origin="https://attacker.invalid")
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
