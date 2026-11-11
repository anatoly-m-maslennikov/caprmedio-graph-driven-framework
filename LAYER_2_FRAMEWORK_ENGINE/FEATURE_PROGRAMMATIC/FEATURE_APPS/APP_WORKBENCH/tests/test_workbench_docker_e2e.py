# CA-E-753@2
# CA-E-676@12
# CA-E-683@6
# CA-E-780@8
# CA-E-677@23
# CA-E-784@2
# CA-E-785@2
# CA-E-787@3
"""Real Workbench MCP/HTTP proof against the full-suite current-code image."""

from __future__ import annotations

import asyncio
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time
import unittest
from uuid import uuid4


REPOSITORY = Path(__file__).resolve().parents[5]
APP_ROOT = REPOSITORY / "LAYER_2_FRAMEWORK_ENGINE" / "FEATURE_PROGRAMMATIC" / "FEATURE_APPS" / "APP_WORKBENCH"
FRONTEND_ROOT = APP_ROOT / "FEATURE_WORKBENCH_FRONTEND"
TOOLS_ROOT = REPOSITORY / "LAYER_2_FRAMEWORK_ENGINE" / "FEATURE_PROGRAMMATIC" / "FEATURE_TOOLS"
MCP_ROOT = REPOSITORY / "LAYER_2_FRAMEWORK_ENGINE" / "FEATURE_PROGRAMMATIC" / "FEATURE_MCP"
sys.path[:0] = [str(APP_ROOT / "tests"), str(APP_ROOT), str(TOOLS_ROOT), str(MCP_ROOT)]

from workbench_docker_support import (  # noqa: E402
    assert_legacy_files_unchanged,
    assert_legacy_saved,
    assert_journal_unchanged,
    assert_not_saved,
    assert_saved,
    assert_saved_journal,
    container_memory_metrics,
    free_port,
    journal_snapshot,
    project_name as read_project_name,
    request,
)
from http_paths import HEALTH_PATH, MCP_PATH, WORKBENCH_PATH  # noqa: E402
from work_journal import configured_journal_root  # noqa: E402
from workbench_grid_checks import WorkbenchGridDockerMixin  # noqa: E402
from workbench_watcher_checks import WorkbenchWatcherDockerMixin  # noqa: E402
from workbench_performance_checks import WorkbenchPerformanceDockerMixin  # noqa: E402


class WorkbenchDockerE2E(
    WorkbenchGridDockerMixin, WorkbenchWatcherDockerMixin, WorkbenchPerformanceDockerMixin, unittest.TestCase,
):
    """One owned container; tests make no image, project, or Docker-global changes."""

    @classmethod
    def setUpClass(cls) -> None:  # noqa: C901
        image = os.environ.get("CAPRMEDIO_IMAGE")
        if not image:
            raise RuntimeError("CAPRMEDIO_IMAGE is required; the full suite builds the current-code image once")
        cls.image = image
        cls.port = free_port()
        cls.name = f"caprmedio-workbench-e2e-{uuid4().hex}"
        cls.url = f"http://127.0.0.1:{cls.port}"
        cls.target = next((path for path in (REPOSITORY / ".caprmedio_caprmedio").rglob("CA-R-2723-*.md") if not
                           {"archive", "archived", "draft", "drafts"}.intersection(
                               part.casefold() for part in path.relative_to(REPOSITORY).parts)), None)
        if cls.target is None:
            raise RuntimeError("current CA-R-2723 source is required for the Workbench Docker proof")
        cls.before_hash = hashlib.sha256(cls.target.read_bytes()).hexdigest()
        cls.project_name = read_project_name(REPOSITORY / ".caprmedio_caprmedio")
        cls.workbench_path = f"{WORKBENCH_PATH}/{cls.project_name}"
        cls.journal_relative = configured_journal_root(REPOSITORY)
        cls.runtime = tempfile.TemporaryDirectory()
        cls.runtime_root = Path(cls.runtime.name) / "runtime"
        cls.runtime_root.mkdir()
        cls.runtime_root.chmod(0o777)
        cls.result_root = Path(cls.runtime.name) / "results"
        cls.result_root.mkdir()
        cls.result_root.chmod(0o777)
        cls.workbench_state = cls.runtime_root / "workbench"
        cls.workbench_state.mkdir()
        cls.workbench_state.chmod(0o777)
        cls.journal_state = Path(cls.runtime.name) / "journal"
        cls.journal_state.mkdir()
        cls.journal_state.chmod(0o777)
        cls.journal_mount = f"/project/{cls.journal_relative.as_posix()}"
        legacy_directory = cls.workbench_state / "saved_queries"
        legacy_directory.mkdir()
        cls.legacy_query_id = f"q_{'1' * 32}"
        cls.legacy_worksheet_id = f"w_{'2' * 32}"
        (legacy_directory / f"{cls.legacy_query_id}.sql").write_text("SELECT 'legacy query'", encoding="utf-8")
        (legacy_directory / f"{cls.legacy_worksheet_id}.json").write_text(
            json.dumps({"sql": "SELECT 'legacy worksheet'"}), encoding="utf-8",
        )
        cls.legacy_hashes = {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in legacy_directory.iterdir()
        }
        cls.addClassCleanup(cls.runtime.cleanup)
        cls.stdout = tempfile.TemporaryFile(mode="w+t", encoding="utf-8")
        cls.stderr = tempfile.TemporaryFile(mode="w+t", encoding="utf-8")
        cls.addClassCleanup(cls.stdout.close)
        cls.addClassCleanup(cls.stderr.close)
        cls.addClassCleanup(cls._cleanup_container)
        cls.process = subprocess.Popen(
            [
                "docker", "run", "--rm", "--name", cls.name,
                "--label", "caprmedio.test=workbench-e2e",
                "--memory=1536m", "--memory-swap=1536m",
                "--tmpfs", "/tmp:rw,nosuid,nodev,size=256m",
                "-p", f"127.0.0.1:{cls.port}:8092", "-v", f"{REPOSITORY}:/project:ro",
                "-v", f"{cls.runtime_root}:/project/.caprmedio_runtime:rw",
                "-v", f"{cls.result_root}:/project/.caprmedio_tmp:rw",
                "-v", f"{cls.journal_state}:{cls.journal_mount}:rw",
                image, "mcp-http",
            ],
            cwd=REPOSITORY, stdout=cls.stdout, stderr=cls.stderr, text=True,
        )
        deadline = time.monotonic() + 45
        while time.monotonic() < deadline:  # readiness polling is test-only.
            if cls.process.poll() is not None:
                cls.stdout.seek(0)
                cls.stderr.seek(0)
                stdout, stderr = cls.stdout.read(), cls.stderr.read()
                raise RuntimeError(f"Workbench MCP container exited during startup\nstdout:\n{stdout}\nstderr:\n{stderr}")
            try:
                if request(cls.url + HEALTH_PATH)[0] == 200:
                    mounts = subprocess.run(
                        ["docker", "inspect", "--format", "{{json .Mounts}}", cls.name],
                        capture_output=True, text=True, check=True,
                    ).stdout.strip()
                    project_mounts = [mount for mount in json.loads(mounts) if mount["Destination"] == "/project"]
                    if len(project_mounts) != 1 or project_mounts[0]["RW"]:
                        raise RuntimeError("Workbench MCP project mount is not read-only")
                    runtime_mounts = [mount for mount in json.loads(mounts) if mount["Destination"] == "/project/.caprmedio_runtime"]
                    if (len(runtime_mounts) != 1 or not runtime_mounts[0]["RW"]
                            or Path(runtime_mounts[0]["Source"]).resolve() != cls.runtime_root.resolve()):
                        raise RuntimeError("Workbench runtime root is not the owned writable host directory")
                    state_mounts = [mount for mount in json.loads(mounts) if mount["Destination"] == "/project/.caprmedio_runtime/workbench"]
                    if state_mounts or cls.workbench_state.parent != cls.runtime_root:
                        raise RuntimeError("Workbench state must use the owned runtime mount")
                    journal_mounts = [mount for mount in json.loads(mounts) if mount["Destination"] == cls.journal_mount]
                    if (len(journal_mounts) != 1 or not journal_mounts[0]["RW"]
                            or Path(journal_mounts[0]["Source"]).resolve() != cls.journal_state.resolve()):
                        raise RuntimeError("Workbench Journal mount is not the owned writable host directory")
                    return
            except OSError:
                pass
            time.sleep(0.2)
        raise RuntimeError("Workbench MCP container did not become ready within 45 seconds")

    @classmethod
    def _cleanup_container(cls) -> None:
        process = getattr(cls, "process", None)
        if process is not None and process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
        subprocess.run(["docker", "container", "rm", "-f", getattr(cls, "name", "")], capture_output=True, text=True, check=False)
        stderr = getattr(cls, "stderr", None)
        if stderr is not None:
            try:
                stderr.seek(0)
                (REPOSITORY / ".caprmedio_tmp/workbench/latest-container.stderr.log").write_text(stderr.read())
            except OSError:
                pass

    def test_mcp_exposes_all_workbench_tools_and_saved_query_identity(self) -> None:
        from mcp.client.session import ClientSession
        from mcp.client.streamable_http import streamable_http_client

        run_sql = "SELECT 'λ' AS unicode_value"
        worksheet_sql = "SELECT 'λ'; SELECT 2"
        cursor_position = len("SELECT 'λ' ".encode("utf-16-le")) // 2
        journal_before = journal_snapshot(self.journal_state)

        async def exercise() -> tuple[dict, ...]:
            async with streamable_http_client(self.url + MCP_PATH) as streams:
                async with ClientSession(*streams, read_timeout_seconds=120) as client:
                    await client.initialize()
                    tools = {tool.name for tool in (await client.list_tools()).tools}
                    self.assertTrue({
                        "query_run", "query_check", "query_page", "query_schema",
                        "view_save", "query_load", "query_saved_list",
                        "workbench_reread",
                    } <= tools)
                    self.assertNotIn("query_save", tools)
                    previewed = await client.call_tool("query_run", {
                        "sql": "SELECT 1", "preview": 0, "save": False, "result_delivery": "inline",
                    })
                    self.assertFalse(previewed.is_error, previewed.structured_content)
                    self.assertEqual([], previewed.structured_content["rows"])
                    self.assertEqual(0, previewed.structured_content["row_count"])
                    self.assertEqual(1, previewed.structured_content["column_count"])
                    self.assertNotIn("saved_query_id", previewed.structured_content)
                    self.assertFalse({"query_rename", "worksheet_rename"} & tools)
                    schema = await client.call_tool("query_schema", {})
                    self.assertFalse(schema.is_error)
                    ran = await client.call_tool("query_run", {
                        "sql": run_sql, "cursor_position": cursor_position, "result_delivery": "inline",
                    })
                    self.assertFalse(ran.is_error)
                    page = await client.call_tool("query_page", {
                        "query_id": ran.structured_content["query_id"], "offset": 0, "result_delivery": "inline",
                    })
                    self.assertFalse(page.is_error, page.structured_content or page.content)
                    checked = await client.call_tool("query_check", {
                        "sql": run_sql, "cursor_position": cursor_position,
                    })
                    self.assertFalse(checked.is_error)
                    invalid = await client.call_tool("query_run", {"sql": "SELECT FROM"})
                    self.assertTrue(invalid.is_error)
                    assert_journal_unchanged(self, self.journal_state, journal_before)
                    saved = await client.call_tool("query_run", {
                        "sql": run_sql, "cursor_position": cursor_position,
                        "save": True, "name": "MCP query", "result_delivery": "inline",
                    })
                    worksheet = await client.call_tool("view_save", {
                        "sql": worksheet_sql, "name": "MCP worksheet",
                    })
                    self.assertFalse(saved.is_error)
                    self.assertFalse(worksheet.is_error)
                    loaded_by_id = await client.call_tool("query_load", {
                        "reference": saved.structured_content["saved_query_id"],
                    })
                    loaded_by_url = await client.call_tool("query_load", {
                        "reference": worksheet.structured_content["saved_query_url"],
                    })
                    recent = await client.call_tool("query_saved_list", {"limit": 20})
                    legacy_query = await client.call_tool("query_load", {"reference": self.legacy_query_id})
                    legacy_worksheet = await client.call_tool("query_load", {
                        "reference": f"{self.url}{self.workbench_path}?query={self.legacy_worksheet_id}",
                    })
                    return (
                        schema.structured_content, ran.structured_content, page.structured_content,
                        checked.structured_content, saved.structured_content, worksheet.structured_content,
                        loaded_by_id.structured_content, loaded_by_url.structured_content,
                        recent.structured_content, legacy_query.structured_content,
                        legacy_worksheet.structured_content, invalid.structured_content, invalid.is_error,
                    )

        (schema, ran, page, checked, saved, worksheet, loaded_by_id, loaded_by_url, recent,
         legacy_query, legacy_worksheet, invalid, invalid_is_error) = asyncio.run(exercise())
        self.assertEqual({"atoms", "scope_units", "change_log", "atom_physical_carrier_issues", "atom_declared_carrier_issues", "atom_content_issues"}, set(schema["tables"]))
        status_column = next(
            column for column in schema["tables"]["atoms"] if column["name"] == "header.status"
        )
        self.assertTrue(all(isinstance(value, str) for value in status_column.get("values", [])))
        self.assertEqual([["λ"]], ran["rows"])
        self.assertIsInstance(ran.get("query_id"), str)
        self.assertNotIn("sql", ran)
        assert_not_saved(self, ran)
        self.assertEqual(ran["query_id"], page["query_id"])
        self.assertNotIn("sql", page)
        assert_not_saved(self, page)
        self.assertTrue(checked["valid"])
        self.assertNotIn("sql", checked)
        assert_not_saved(self, checked)
        self.assertIsInstance(saved.get("query_id"), str)
        self.assertNotEqual(saved["query_id"], saved["saved_query_id"])
        self.assertEqual([["λ"]], saved["rows"])
        self.assertNotIn("sql", saved)
        self.assertEqual("query", saved["kind"])
        self.assertEqual("MCP query", saved["name"])
        self.assertNotIn("query_id", worksheet)
        assert_saved(self, worksheet, url=self.url, workbench_path=self.workbench_path, kind="view", sql=worksheet_sql)
        self.assertEqual("MCP worksheet", worksheet["name"])
        assert_saved(self, loaded_by_id, url=self.url, workbench_path=self.workbench_path, kind="query", sql=run_sql)
        assert_saved(self, loaded_by_url, url=self.url, workbench_path=self.workbench_path, kind="view", sql=worksheet_sql)
        assert_legacy_saved(
            self, legacy_query, url=self.url, workbench_path=self.workbench_path,
            identifier=self.legacy_query_id, kind="query", sql="SELECT 'legacy query'",
        )
        assert_legacy_saved(
            self, legacy_worksheet, url=self.url, workbench_path=self.workbench_path, identifier=self.legacy_worksheet_id,
            kind="view", sql="SELECT 'legacy worksheet'",
        )
        self.assertTrue({
            saved["saved_query_id"], worksheet["saved_query_id"],
            self.legacy_query_id, self.legacy_worksheet_id,
        } <= {
            item["saved_query_id"] for item in recent["items"]
        })
        recent_by_id = {item["saved_query_id"]: item for item in recent["items"]}
        self.assertEqual("MCP query", recent_by_id[saved["saved_query_id"]].get("name"))
        self.assertEqual("MCP worksheet", recent_by_id[worksheet["saved_query_id"]].get("name"))
        self.assertTrue(invalid_is_error)
        assert_not_saved(self, invalid)
        assert_saved_journal(self, self.journal_state, loaded_by_id, worksheet)
        assert_legacy_files_unchanged(self, self.workbench_state, self.legacy_hashes)
        self.assertTrue((self.workbench_state / "projection.duckdb").is_file())
        events_path, events, peak = container_memory_metrics(self.name)
        self.assertEqual(0, events.get("oom_kill"), f"cgroup memory.events from {events_path}: {events}")
        print(f"Workbench Docker memory.events={events_path} oom_kill={events['oom_kill']} memory.peak={peak}")

    def test_workbench_browser_flows(self) -> None:
        environment = os.environ | {
            "WORKBENCH_E2E_URL": f"{self.url}{self.workbench_path}",
            "PLAYWRIGHT_BROWSERS_PATH": str(REPOSITORY / ".caprmedio_tmp/workbench/playwright-browsers"),
        }
        try:
            result = subprocess.run(
                ["npm", "run", "test:e2e"], cwd=FRONTEND_ROOT, env=environment,
                capture_output=True, text=True, timeout=120, check=False,
            )
        except subprocess.TimeoutExpired as error:
            self.fail(f"Workbench browser E2E timed out\nstdout:\n{error.stdout}\nstderr:\n{error.stderr}")
        self.assertEqual(
            0, result.returncode,
            f"Workbench browser E2E failed\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}",
        )

    def test_workbench_http_run_check_and_read_only_failures_do_not_mutate_source(self) -> None:
        status, page = request(self.url + self.workbench_path)
        self.assertEqual(200, status)
        self.assertIn("Workbench", page)
        asset_paths = [
            path for path in re.findall(r'(?:src|href)="([^"]+)"', page)
            if path.startswith(f"{WORKBENCH_PATH}/assets/")
        ]
        self.assertGreaterEqual(len(asset_paths), 2, page)
        for asset_path in asset_paths:
            asset_status, _ = request(self.url + asset_path)
            self.assertEqual(200, asset_status, asset_path)
        run_sql = "SELECT 'λ' AS unicode_value"
        worksheet_sql = "SELECT 'λ'; SELECT 2"
        cursor_position = len("SELECT 'λ' ".encode("utf-16-le")) // 2
        journal_before = journal_snapshot(self.journal_state)
        status, schema = request(self.url + f"{self.workbench_path}/schema", method="POST", payload={})
        self.assertEqual(200, status, schema)
        status, default_file = request(
            self.url + f"{self.workbench_path}/run", method="POST",
            payload={"sql": "SELECT 123 AS value"},
        )
        self.assertEqual(200, status, default_file)
        self.assertNotIn("rows", default_file)
        self.assertNotIn("sql", default_file)
        artifact = default_file["result_file"]
        self.assertEqual("json_matrix", artifact["format"])
        self.assertEqual(1, artifact["row_count"])
        result_path = Path(artifact["path"])
        self.assertEqual((".caprmedio_tmp", "workbench", "query_results"), result_path.parts[:3])
        self.assertEqual({"columns": ["value"], "rows": [[123]]}, json.loads(
            (self.result_root / Path(*result_path.parts[1:])).read_text(encoding="utf-8")
        ))
        self.assertEqual({"atoms", "scope_units", "change_log", "atom_physical_carrier_issues", "atom_declared_carrier_issues", "atom_content_issues"}, set(schema["tables"]))
        status_column = next(
            column for column in schema["tables"]["atoms"] if column["name"] == "header.status"
        )
        self.assertTrue(all(isinstance(value, str) for value in status_column.get("values", [])))
        status, ran = request(
            self.url + f"{self.workbench_path}/run", method="POST",
            payload={"sql": run_sql, "cursor_position": cursor_position, "result_delivery": "inline"},
        )
        self.assertEqual(200, status, ran)
        self.assertEqual([["λ"]], ran["rows"])
        self.assertNotIn("sql", ran)
        self.assertIsInstance(ran.get("query_id"), str)
        assert_not_saved(self, ran)
        status, checked = request(
            self.url + f"{self.workbench_path}/check", method="POST",
            payload={"sql": run_sql, "cursor_position": cursor_position},
        )
        self.assertEqual(200, status, checked)
        self.assertTrue(checked["valid"])
        self.assertNotIn("sql", checked)
        assert_not_saved(self, checked)
        assert_journal_unchanged(self, self.journal_state, journal_before)
        status, saved = request(
            self.url + f"{self.workbench_path}/run", method="POST",
            payload={"sql": run_sql, "cursor_position": cursor_position, "save": True, "name": "HTTP query"},
        )
        self.assertEqual(200, status, saved)
        self.assertIsInstance(saved.get("query_id"), str)
        self.assertNotIn("sql", saved)
        self.assertEqual("query", saved["kind"])
        self.assertEqual("HTTP query", saved["name"])
        status, worksheet = request(
            self.url + f"{self.workbench_path}/view-save", method="POST",
            payload={"sql": worksheet_sql, "name": "HTTP worksheet"},
        )
        self.assertEqual(200, status, worksheet)
        self.assertNotIn("query_id", worksheet)
        assert_saved(self, worksheet, url=self.url, workbench_path=self.workbench_path, kind="view", sql=worksheet_sql)
        self.assertEqual("HTTP worksheet", worksheet["name"])
        status, loaded_by_id = request(
            self.url + f"{self.workbench_path}/load", method="POST",
            payload={"reference": saved["saved_query_id"]},
        )
        self.assertEqual(200, status, loaded_by_id)
        assert_saved(self, loaded_by_id, url=self.url, workbench_path=self.workbench_path, kind="query", sql=run_sql)
        status, loaded_by_url = request(
            self.url + f"{self.workbench_path}/load", method="POST",
            payload={"reference": worksheet["saved_query_url"]},
        )
        self.assertEqual(200, status, loaded_by_url)
        assert_saved(self, loaded_by_url, url=self.url, workbench_path=self.workbench_path, kind="view", sql=worksheet_sql)
        status, recent = request(
            self.url + f"{self.workbench_path}/saved-list", method="POST", payload={"limit": 20},
        )
        self.assertEqual(200, status, recent)
        self.assertTrue({
            saved["saved_query_id"], worksheet["saved_query_id"],
            self.legacy_query_id, self.legacy_worksheet_id,
        } <= {
            item["saved_query_id"] for item in recent["items"]
        })
        recent_by_id = {item["saved_query_id"]: item for item in recent["items"]}
        self.assertEqual("HTTP query", recent_by_id[saved["saved_query_id"]].get("name"))
        self.assertEqual("HTTP worksheet", recent_by_id[worksheet["saved_query_id"]].get("name"))
        status, legacy_query = request(
            self.url + f"{self.workbench_path}/load", method="POST", payload={"reference": self.legacy_query_id},
        )
        self.assertEqual(200, status, legacy_query)
        assert_legacy_saved(
            self, legacy_query, url=self.url, workbench_path=self.workbench_path,
            identifier=self.legacy_query_id, kind="query", sql="SELECT 'legacy query'",
        )
        status, legacy_worksheet = request(
            self.url + f"{self.workbench_path}/load", method="POST",
            payload={"reference": f"{self.url}{self.workbench_path}?query={self.legacy_worksheet_id}"},
        )
        self.assertEqual(200, status, legacy_worksheet)
        assert_legacy_saved(
            self, legacy_worksheet, url=self.url, workbench_path=self.workbench_path, identifier=self.legacy_worksheet_id,
            kind="view", sql="SELECT 'legacy worksheet'",
        )
        journal_before_page = journal_snapshot(self.journal_state)
        status, full = request(
            self.url + f"{self.workbench_path}/run", method="POST", payload={"sql": "SELECT * FROM atoms", "result_delivery": "inline"},
        )
        self.assertEqual(200, status, full)
        self.assertEqual(100, len(full["rows"]))
        self.assertGreater(full["row_count"], len(full["rows"]))
        self.assertTrue(full["has_more"])
        self.assertNotIn("sql", full)
        assert_not_saved(self, full)
        status, next_page = request(
            self.url + f"{self.workbench_path}/page", method="POST",
            payload={"query_id": full["query_id"], "offset": len(full["rows"]), "result_delivery": "inline"},
        )
        self.assertEqual(200, status, next_page)
        self.assertEqual(full["query_id"], next_page["query_id"])
        self.assertNotIn("sql", next_page)
        assert_not_saved(self, next_page)
        status, failure = request(
            self.url + f"{self.workbench_path}/run", method="POST", payload={"sql": "SELECT FROM"},
        )
        self.assertEqual(400, status)
        self.assertIsInstance(failure.get("error"), str)
        assert_not_saved(self, failure)
        assert_saved_journal(self, self.journal_state, loaded_by_id, worksheet)
        assert_legacy_files_unchanged(self, self.workbench_state, self.legacy_hashes)
        for sql in ("SELECT 1; SELECT 2", "CREATE TABLE forbidden(x INTEGER)"):
            status, failure = request(self.url + f"{self.workbench_path}/run", method="POST", payload={"sql": sql})
            self.assertEqual(400, status)
            self.assertIn("error", failure)
            assert_not_saved(self, failure)
        assert_journal_unchanged(self, self.journal_state, journal_before_page)
        status, _ = request(self.url + f"{WORKBENCH_PATH}/not-{self.project_name}")
        self.assertEqual(404, status)
        self.assertEqual(self.before_hash, hashlib.sha256(self.target.read_bytes()).hexdigest())


if __name__ == "__main__":
    unittest.main()
