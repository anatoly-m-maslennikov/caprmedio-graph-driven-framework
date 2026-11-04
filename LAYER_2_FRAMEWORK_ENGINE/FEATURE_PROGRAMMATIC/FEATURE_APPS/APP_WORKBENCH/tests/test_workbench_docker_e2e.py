# CA-E-673@3
# CA-E-674@5
# CA-E-676@8
# CA-E-677@8

"""Real Workbench MCP/HTTP proof against the full-suite current-code image."""

from __future__ import annotations

import asyncio
import hashlib
import json
import os
from pathlib import Path
import re
import socket
import subprocess
import sys
import tempfile
import time
import tomllib
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from uuid import UUID, uuid4


REPOSITORY = Path(__file__).resolve().parents[5]
APP_ROOT = REPOSITORY / "LAYER_2_FRAMEWORK_ENGINE" / "FEATURE_PROGRAMMATIC" / "FEATURE_APPS" / "APP_WORKBENCH"
TOOLS_ROOT = REPOSITORY / "LAYER_2_FRAMEWORK_ENGINE" / "FEATURE_PROGRAMMATIC" / "FEATURE_TOOLS"
MCP_ROOT = REPOSITORY / "LAYER_2_FRAMEWORK_ENGINE" / "FEATURE_PROGRAMMATIC" / "FEATURE_MCP"
sys.path[:0] = [str(APP_ROOT / "tests"), str(APP_ROOT), str(TOOLS_ROOT), str(MCP_ROOT)]

from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from smalltest_support import source_path, write_atom, write_settings  # noqa: E402
from http_paths import HEALTH_PATH, MCP_PATH, WORKBENCH_PATH  # noqa: E402
from work_journal import configured_journal_root  # noqa: E402


def _free_port() -> int:
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        return int(probe.getsockname()[1])


def _project_name(control_root: Path) -> str:
    settings_path = control_root / "caprmedio_project_settings.toml"
    settings = tomllib.loads(settings_path.read_text(encoding="utf-8"))
    return settings["project"]["name"]


def _request(url: str, *, method: str = "GET", payload: dict | None = None) -> tuple[int, dict | str]:
    body = None if payload is None else json.dumps(payload).encode()
    request = Request(url, data=body, method=method, headers={"content-type": "application/json"})
    try:
        with urlopen(request, timeout=60) as response:  # noqa: S310 -- loopback test server
            data = response.read().decode()
            return response.status, json.loads(data) if response.headers.get_content_type() == "application/json" else data
    except HTTPError as error:
        with error:
            data = error.read().decode()
        return error.code, json.loads(data) if data else {}


def _container_memory_metrics(name: str) -> tuple[str, dict[str, int], int | None]:
    for events_path in ("/sys/fs/cgroup/memory.events", "/sys/fs/cgroup/memory/memory.events"):
        result = subprocess.run(
            ["docker", "exec", name, "cat", events_path],
            capture_output=True, text=True, check=False,
        )
        if result.returncode != 0:
            continue
        events = {}
        for line in result.stdout.splitlines():
            key, _, value = line.partition(" ")
            if key and value:
                try:
                    events[key] = int(value)
                except ValueError:
                    pass
        peak_result = subprocess.run(
            ["docker", "exec", name, "cat", events_path.replace("memory.events", "memory.peak")],
            capture_output=True, text=True, check=False,
        )
        peak = int(peak_result.stdout.strip()) if peak_result.returncode == 0 else None
        return events_path, events, peak
    raise AssertionError("Workbench container did not expose cgroup memory.events")


def _is_uuid7(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = UUID(value)
    except ValueError:
        return False
    return parsed.version == 7 and str(parsed) == value


class WorkbenchDockerE2E(unittest.TestCase):
    """One owned container; tests make no image, project, or Docker-global changes."""

    @classmethod
    def setUpClass(cls) -> None:
        image = os.environ.get("CAPRMEDIO_IMAGE")
        if not image:
            raise RuntimeError("CAPRMEDIO_IMAGE is required; the full suite builds the current-code image once")
        cls.image = image
        cls.port = _free_port()
        cls.name = f"caprmedio-workbench-e2e-{uuid4().hex}"
        cls.url = f"http://127.0.0.1:{cls.port}"
        cls.target = next((path for path in REPOSITORY.rglob("CA-R-2723*.md") if "archive" not in {part.casefold() for part in path.parts}), None)
        if cls.target is None:
            raise RuntimeError("current CA-R-2723 source is required for the Workbench Docker proof")
        cls.before_hash = hashlib.sha256(cls.target.read_bytes()).hexdigest()
        cls.project_name = _project_name(REPOSITORY / ".caprmedio_caprmedio")
        cls.workbench_path = f"{WORKBENCH_PATH}/{cls.project_name}"
        cls.journal_relative = configured_journal_root(REPOSITORY)
        cls.runtime = tempfile.TemporaryDirectory()
        cls.workbench_state = Path(cls.runtime.name) / "workbench"
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
                "--tmpfs", "/project/.caprmedio_runtime:rw,nosuid,nodev,size=64m,mode=1777",
                "-p", f"127.0.0.1:{cls.port}:8092", "-v", f"{REPOSITORY}:/project:ro",
                "-v", f"{cls.workbench_state}:/project/.caprmedio_runtime/workbench:rw",
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
                if _request(cls.url + HEALTH_PATH)[0] == 200:
                    mounts = subprocess.run(
                        ["docker", "inspect", "--format", "{{json .Mounts}}", cls.name],
                        capture_output=True, text=True, check=True,
                    ).stdout.strip()
                    project_mounts = [mount for mount in json.loads(mounts) if mount["Destination"] == "/project"]
                    if len(project_mounts) != 1 or project_mounts[0]["RW"]:
                        raise RuntimeError("Workbench MCP project mount is not read-only")
                    state_mounts = [mount for mount in json.loads(mounts) if mount["Destination"] == "/project/.caprmedio_runtime/workbench"]
                    if (len(state_mounts) != 1 or not state_mounts[0]["RW"]
                            or Path(state_mounts[0]["Source"]).resolve() != cls.workbench_state.resolve()):
                        raise RuntimeError("Workbench runtime state mount is not writable")
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

    def assert_saved(self, value: dict, *, kind: str, sql: str) -> None:
        identifier = value.get("saved_query_id")
        self.assertTrue(_is_uuid7(identifier), identifier)
        self.assertEqual(kind, value.get("kind"))
        self.assertEqual(sql, value.get("sql"))
        self.assertIsInstance(value.get("saved_at"), str)
        self.assertEqual(
            f"{self.url}{self.workbench_path}?query={identifier}", value.get("saved_query_url"),
        )

    def assert_legacy_saved(self, value: dict, *, identifier: str, kind: str, sql: str) -> None:
        self.assertEqual(identifier, value.get("saved_query_id"))
        self.assertEqual(kind, value.get("kind"))
        self.assertEqual(sql, value.get("sql"))
        self.assertEqual(f"{self.url}{self.workbench_path}?query={identifier}", value.get("saved_query_url"))

    def assert_saved_journal(self, *saved: dict) -> None:
        paths = sorted(self.journal_state.glob("workbench-saved-items-*-part-*.ndjson"))
        self.assertTrue(paths, "saved items must use the configured Journal root")
        records = [json.loads(line) for path in paths for line in path.read_text(encoding="utf-8").splitlines()]
        for value in saved:
            matching = [record for record in records if record["saved_query_id"] == value["saved_query_id"]]
            self.assertEqual(1, len(matching), value)
            record = matching[0]
            self.assertEqual(value["kind"], record["kind"])
            self.assertEqual(value["sql"], record["sql"])
            self.assertEqual(value.get("name"), record.get("name"))
            self.assertIsInstance(record["saved_at"], str)

    def assert_legacy_files_unchanged(self) -> None:
        legacy_directory = self.workbench_state / "saved_queries"
        self.assertEqual(
            self.legacy_hashes,
            {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in legacy_directory.iterdir()},
        )

    def test_mcp_exposes_all_workbench_tools_and_saved_query_identity(self) -> None:
        from mcp.client.session import ClientSession
        from mcp.client.streamable_http import streamable_http_client

        worksheet_sql = "SELECT 'λ'; SELECT 2"
        cursor_position = len("SELECT 'λ'; ".encode("utf-16-le")) // 2

        async def exercise() -> tuple[dict, ...]:
            async with streamable_http_client(self.url + MCP_PATH) as streams:
                async with ClientSession(*streams, read_timeout_seconds=120) as client:
                    await client.initialize()
                    tools = {tool.name for tool in (await client.list_tools()).tools}
                    self.assertTrue({
                        "query_run", "query_check", "query_page", "query_schema", "query_save",
                        "worksheet_save", "query_load", "query_saved_list",
                    } <= tools)
                    self.assertFalse({"query_rename", "worksheet_rename"} & tools)
                    schema = await client.call_tool("query_schema", {})
                    self.assertFalse(schema.is_error)
                    ran = await client.call_tool("query_run", {
                        "sql": worksheet_sql, "cursor_position": cursor_position,
                    })
                    self.assertFalse(ran.is_error)
                    page = await client.call_tool("query_page", {
                        "query_id": ran.structured_content["query_id"], "offset": 0,
                    })
                    self.assertFalse(page.is_error, page.structured_content or page.content)
                    checked = await client.call_tool("query_check", {
                        "sql": worksheet_sql, "cursor_position": cursor_position,
                    })
                    self.assertFalse(checked.is_error)
                    saved = await client.call_tool("query_save", {
                        "sql": worksheet_sql, "cursor_position": cursor_position, "name": "MCP query",
                    })
                    worksheet = await client.call_tool("worksheet_save", {
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
                    invalid = await client.call_tool("query_run", {"sql": "SELECT FROM"})
                    return (
                        schema.structured_content, ran.structured_content, page.structured_content,
                        checked.structured_content, saved.structured_content, worksheet.structured_content,
                        loaded_by_id.structured_content, loaded_by_url.structured_content,
                        recent.structured_content, legacy_query.structured_content,
                        legacy_worksheet.structured_content, invalid.structured_content, invalid.is_error,
                    )

        (schema, ran, page, checked, saved, worksheet, loaded_by_id, loaded_by_url, recent,
         legacy_query, legacy_worksheet, invalid, invalid_is_error) = asyncio.run(exercise())
        self.assertEqual({"atoms", "scope_units"}, set(schema["tables"]))
        status_column = next(column for column in schema["tables"]["atoms"] if column["name"] == "status")
        self.assertTrue(all(isinstance(value, str) for value in status_column.get("values", [])))
        self.assertEqual([[2]], ran["rows"])
        self.assertIsInstance(ran.get("query_id"), str)
        self.assert_saved(ran, kind="query", sql=" SELECT 2")
        self.assertNotIn("name", ran)
        self.assertEqual(ran["query_id"], page["query_id"])
        self.assertEqual(ran["saved_query_id"], page["saved_query_id"])
        self.assert_saved(page, kind="query", sql=" SELECT 2")
        self.assertTrue(checked["valid"])
        self.assert_saved(checked, kind="query", sql=" SELECT 2")
        self.assertNotIn("name", checked)
        self.assertNotIn("query_id", saved)
        self.assert_saved(saved, kind="query", sql=" SELECT 2")
        self.assertEqual("MCP query", saved["name"])
        self.assertNotIn("query_id", worksheet)
        self.assert_saved(worksheet, kind="worksheet", sql=worksheet_sql)
        self.assertEqual("MCP worksheet", worksheet["name"])
        self.assert_saved(loaded_by_id, kind="query", sql=" SELECT 2")
        self.assert_saved(loaded_by_url, kind="worksheet", sql=worksheet_sql)
        self.assert_legacy_saved(
            legacy_query, identifier=self.legacy_query_id, kind="query", sql="SELECT 'legacy query'",
        )
        self.assert_legacy_saved(
            legacy_worksheet, identifier=self.legacy_worksheet_id,
            kind="worksheet", sql="SELECT 'legacy worksheet'",
        )
        self.assertTrue({
            saved["saved_query_id"], worksheet["saved_query_id"],
            self.legacy_query_id, self.legacy_worksheet_id,
        } <= {
            item["saved_query_id"] for item in recent["items"]
        })
        recent_names = {item["saved_query_id"]: item["name"] for item in recent["items"]}
        self.assertEqual("MCP query", recent_names[saved["saved_query_id"]])
        self.assertEqual("MCP worksheet", recent_names[worksheet["saved_query_id"]])
        self.assertTrue(invalid_is_error)
        self.assert_saved(invalid, kind="query", sql="SELECT FROM")
        self.assert_saved_journal(ran, checked, saved, worksheet, invalid)
        self.assert_legacy_files_unchanged()
        self.assertTrue((self.workbench_state / "projection.duckdb").is_file())
        events_path, events, peak = _container_memory_metrics(self.name)
        self.assertEqual(0, events.get("oom_kill"), f"cgroup memory.events from {events_path}: {events}")
        print(f"Workbench Docker memory.events={events_path} oom_kill={events['oom_kill']} memory.peak={peak}")

    def test_workbench_http_run_check_and_read_only_failures_do_not_mutate_source(self) -> None:
        status, page = _request(self.url + self.workbench_path)
        self.assertEqual(200, status)
        self.assertIn("Workbench", page)
        asset_paths = [
            path for path in re.findall(r'(?:src|href)="([^"]+)"', page)
            if path.startswith(f"{WORKBENCH_PATH}/assets/")
        ]
        self.assertGreaterEqual(len(asset_paths), 2, page)
        for asset_path in asset_paths:
            asset_status, _ = _request(self.url + asset_path)
            self.assertEqual(200, asset_status, asset_path)
        worksheet_sql = "SELECT 'λ'; SELECT 2"
        cursor_position = len("SELECT 'λ'; ".encode("utf-16-le")) // 2
        status, schema = _request(self.url + f"{self.workbench_path}/schema", method="POST", payload={})
        self.assertEqual(200, status, schema)
        self.assertEqual({"atoms", "scope_units"}, set(schema["tables"]))
        status_column = next(column for column in schema["tables"]["atoms"] if column["name"] == "status")
        self.assertTrue(all(isinstance(value, str) for value in status_column.get("values", [])))
        status, ran = _request(
            self.url + f"{self.workbench_path}/run", method="POST",
            payload={"sql": worksheet_sql, "cursor_position": cursor_position},
        )
        self.assertEqual(200, status, ran)
        self.assertEqual([[2]], ran["rows"])
        self.assert_saved(ran, kind="query", sql=" SELECT 2")
        self.assertNotIn("name", ran)
        status, checked = _request(
            self.url + f"{self.workbench_path}/check", method="POST",
            payload={"sql": worksheet_sql, "cursor_position": cursor_position},
        )
        self.assertEqual(200, status, checked)
        self.assertTrue(checked["valid"])
        self.assert_saved(checked, kind="query", sql=" SELECT 2")
        self.assertNotIn("name", checked)
        status, saved = _request(
            self.url + f"{self.workbench_path}/save", method="POST",
            payload={"sql": worksheet_sql, "cursor_position": cursor_position, "name": "HTTP query"},
        )
        self.assertEqual(200, status, saved)
        self.assertNotIn("query_id", saved)
        self.assert_saved(saved, kind="query", sql=" SELECT 2")
        self.assertEqual("HTTP query", saved["name"])
        status, worksheet = _request(
            self.url + f"{self.workbench_path}/worksheet-save", method="POST",
            payload={"sql": worksheet_sql, "name": "HTTP worksheet"},
        )
        self.assertEqual(200, status, worksheet)
        self.assertNotIn("query_id", worksheet)
        self.assert_saved(worksheet, kind="worksheet", sql=worksheet_sql)
        self.assertEqual("HTTP worksheet", worksheet["name"])
        status, loaded_by_id = _request(
            self.url + f"{self.workbench_path}/load", method="POST",
            payload={"reference": saved["saved_query_id"]},
        )
        self.assertEqual(200, status, loaded_by_id)
        self.assert_saved(loaded_by_id, kind="query", sql=" SELECT 2")
        status, loaded_by_url = _request(
            self.url + f"{self.workbench_path}/load", method="POST",
            payload={"reference": worksheet["saved_query_url"]},
        )
        self.assertEqual(200, status, loaded_by_url)
        self.assert_saved(loaded_by_url, kind="worksheet", sql=worksheet_sql)
        status, recent = _request(
            self.url + f"{self.workbench_path}/saved-list", method="POST", payload={"limit": 20},
        )
        self.assertEqual(200, status, recent)
        self.assertTrue({
            saved["saved_query_id"], worksheet["saved_query_id"],
            self.legacy_query_id, self.legacy_worksheet_id,
        } <= {
            item["saved_query_id"] for item in recent["items"]
        })
        recent_names = {item["saved_query_id"]: item["name"] for item in recent["items"]}
        self.assertEqual("HTTP query", recent_names[saved["saved_query_id"]])
        self.assertEqual("HTTP worksheet", recent_names[worksheet["saved_query_id"]])
        status, legacy_query = _request(
            self.url + f"{self.workbench_path}/load", method="POST", payload={"reference": self.legacy_query_id},
        )
        self.assertEqual(200, status, legacy_query)
        self.assert_legacy_saved(
            legacy_query, identifier=self.legacy_query_id, kind="query", sql="SELECT 'legacy query'",
        )
        status, legacy_worksheet = _request(
            self.url + f"{self.workbench_path}/load", method="POST",
            payload={"reference": f"{self.url}{self.workbench_path}?query={self.legacy_worksheet_id}"},
        )
        self.assertEqual(200, status, legacy_worksheet)
        self.assert_legacy_saved(
            legacy_worksheet, identifier=self.legacy_worksheet_id,
            kind="worksheet", sql="SELECT 'legacy worksheet'",
        )
        status, full = _request(
            self.url + f"{self.workbench_path}/run", method="POST", payload={"sql": "SELECT * FROM atoms"},
        )
        self.assertEqual(200, status, full)
        self.assertEqual(100, len(full["rows"]))
        self.assertGreater(full["row_count"], len(full["rows"]))
        self.assertTrue(full["has_more"])
        status, next_page = _request(
            self.url + f"{self.workbench_path}/page", method="POST",
            payload={"query_id": full["query_id"], "offset": len(full["rows"])},
        )
        self.assertEqual(200, status, next_page)
        self.assertEqual(full["saved_query_id"], next_page["saved_query_id"])
        self.assertEqual(full["saved_query_url"], next_page["saved_query_url"])
        status, failure = _request(
            self.url + f"{self.workbench_path}/run", method="POST", payload={"sql": "SELECT FROM"},
        )
        self.assertEqual(400, status)
        self.assertIsInstance(failure.get("error"), str)
        self.assert_saved(failure, kind="query", sql="SELECT FROM")
        self.assert_saved_journal(ran, checked, saved, worksheet, full, failure)
        self.assert_legacy_files_unchanged()
        for sql in ("SELECT 1; SELECT 2", "CREATE TABLE forbidden(x INTEGER)"):
            status, failure = _request(self.url + f"{self.workbench_path}/run", method="POST", payload={"sql": sql})
            self.assertEqual(400, status)
            self.assertIn("error", failure)
        status, _ = _request(self.url + f"{WORKBENCH_PATH}/not-{self.project_name}")
        self.assertEqual(404, status)
        self.assertEqual(self.before_hash, hashlib.sha256(self.target.read_bytes()).hexdigest())

    def test_watchfiles_reloads_source_from_writable_docker_bind_mount(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            root.chmod(0o755)
            control = write_settings(root)
            project_name = _project_name(control)
            workbench_path = f"{WORKBENCH_PATH}/{project_name}"
            declarations = write_scope_unit_declarations(root, control_root=control)
            target = write_atom(
                source_path(declarations, "fixture", "04_requirement", "CA-R-901-docker.md"),
                "CA-R-901",
            )
            name = f"caprmedio-workbench-watch-{uuid4().hex}"
            port = _free_port()
            url = f"http://127.0.0.1:{port}"
            stdout = tempfile.TemporaryFile(mode="w+t", encoding="utf-8")
            stderr = tempfile.TemporaryFile(mode="w+t", encoding="utf-8")
            process = subprocess.Popen(
                [
                    "docker", "run", "--rm", "--name", name,
                    "--label", "caprmedio.test=workbench-watch",
                    "--tmpfs", "/tmp:rw,nosuid,nodev,size=256m",
                    "--tmpfs", "/project/.caprmedio_runtime:rw,nosuid,nodev,size=64m,mode=1777",
                    "-p", f"127.0.0.1:{port}:8092", "-v", f"{root}:/project:rw",
                    self.image, "mcp-http",
                ],
                cwd=REPOSITORY, stdout=stdout, stderr=stderr, text=True,
            )
            try:
                deadline = time.monotonic() + 45
                while time.monotonic() < deadline:
                    if process.poll() is not None:
                        stdout.seek(0)
                        stderr.seek(0)
                        raise AssertionError(
                            f"watcher container exited during startup\nstdout:\n{stdout.read()}\nstderr:\n{stderr.read()}"
                        )
                    try:
                        if _request(url + HEALTH_PATH)[0] == 200:
                            break
                    except OSError:
                        pass
                    time.sleep(0.2)
                else:
                    self.fail("watcher container did not become ready within 45 seconds")

                initial = _request(
                    url + f"{workbench_path}/run", method="POST",
                    payload={"sql": "SELECT version FROM atoms WHERE id = 'CA-R-901'"},
                )
                self.assertEqual(200, initial[0])
                self.assertEqual([[1]], initial[1]["rows"])
                write_atom(target, "CA-R-901", version=2, body="# Summary\n\nChanged from the host.\n")
                deadline = time.monotonic() + 20
                while time.monotonic() < deadline:
                    status, result = _request(
                        url + f"{workbench_path}/run", method="POST",
                        payload={"sql": "SELECT version FROM atoms WHERE id = 'CA-R-901'"},
                    )
                    if status == 200 and result["rows"] == [[2]]:
                        return
                    time.sleep(0.2)
                self.fail("watcher did not deliver the writable bind-mount edit")
            finally:
                if process.poll() is None:
                    process.terminate()
                    try:
                        process.wait(timeout=10)
                    except subprocess.TimeoutExpired:
                        process.kill()
                subprocess.run(
                    ["docker", "container", "rm", "-f", name],
                    capture_output=True, text=True, check=False,
                )
                stdout.close()
                stderr.close()


if __name__ == "__main__":
    unittest.main()
