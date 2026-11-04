# CA-E-673@2
# CA-E-674@4
# CA-E-676@3
# CA-E-677@6

"""Real Workbench MCP/HTTP proof against the full-suite current-code image."""

from __future__ import annotations

import asyncio
import hashlib
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from uuid import uuid4


REPOSITORY = Path(__file__).resolve().parents[5]
APP_ROOT = REPOSITORY / "LAYER_2_FRAMEWORK_ENGINE" / "FEATURE_PROGRAMMATIC" / "FEATURE_APPS" / "APP_WORKBENCH"
TOOLS_ROOT = REPOSITORY / "LAYER_2_FRAMEWORK_ENGINE" / "FEATURE_PROGRAMMATIC" / "FEATURE_TOOLS"
MCP_ROOT = REPOSITORY / "LAYER_2_FRAMEWORK_ENGINE" / "FEATURE_PROGRAMMATIC" / "FEATURE_MCP"
sys.path[:0] = [str(APP_ROOT), str(TOOLS_ROOT), str(MCP_ROOT)]

from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from smalltest_support import source_path, write_atom, write_settings  # noqa: E402


def _free_port() -> int:
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        return int(probe.getsockname()[1])


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
        cls.addClassCleanup(cls._cleanup_container)
        cls.url = f"http://127.0.0.1:{cls.port}"
        cls.target = next((path for path in REPOSITORY.rglob("CA-R-2723*.md") if "archive" not in {part.casefold() for part in path.parts}), None)
        if cls.target is None:
            raise RuntimeError("current CA-R-2723 source is required for the Workbench Docker proof")
        cls.before_hash = hashlib.sha256(cls.target.read_bytes()).hexdigest()
        cls.stdout = tempfile.TemporaryFile(mode="w+t", encoding="utf-8")
        cls.stderr = tempfile.TemporaryFile(mode="w+t", encoding="utf-8")
        cls.addClassCleanup(cls.stdout.close)
        cls.addClassCleanup(cls.stderr.close)
        cls.process = subprocess.Popen(
            [
                "docker", "run", "--rm", "--name", cls.name,
                "--label", "caprmedio.test=workbench-e2e",
                "--tmpfs", "/tmp:rw,nosuid,nodev,size=256m",
                "--tmpfs", "/project/.caprmedio_runtime:rw,nosuid,nodev,size=64m,mode=1777",
                "-p", f"127.0.0.1:{cls.port}:8092", "-v", f"{REPOSITORY}:/project:ro",
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
                if _request(cls.url + "/health")[0] == 200:
                    mounts = subprocess.run(
                        ["docker", "inspect", "--format", "{{json .Mounts}}", cls.name],
                        capture_output=True, text=True, check=True,
                    ).stdout.strip()
                    project_mounts = [mount for mount in json.loads(mounts) if mount["Destination"] == "/project"]
                    if len(project_mounts) != 1 or project_mounts[0]["RW"]:
                        raise RuntimeError("Workbench MCP project mount is not read-only")
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

    def test_mcp_run_and_check_use_native_project_tables_and_graph(self) -> None:
        from mcp.client.session import ClientSession
        from mcp.client.streamable_http import streamable_http_client

        sql = ("SELECT id AS item, role AS item FROM atoms "
               "WHERE id IN ('CA-R-2723', 'CA-R-2725') ORDER BY 1")

        async def exercise() -> tuple[dict, dict]:
            async with streamable_http_client(self.url + "/mcp") as streams:
                async with ClientSession(*streams, read_timeout_seconds=60) as client:
                    await client.initialize()
                    tools = {tool.name for tool in (await client.list_tools()).tools}
                    self.assertTrue({"query_run", "query_check"} <= tools)
                    checked = await client.call_tool("query_check", {"sql": sql})
                    self.assertFalse(checked.is_error)
                    self.assertIsInstance(checked.structured_content, dict)
                    ran = await client.call_tool("query_run", {"sql": sql})
                    self.assertFalse(ran.is_error)
                    self.assertIsInstance(ran.structured_content, dict)
                    graph = await client.call_tool("query_run", {"sql": "FROM GRAPH_TABLE (caprmedio MATCH (a:Reference) COLUMNS (a.ref AS ref)) LIMIT 1"})
                    self.assertFalse(graph.is_error)
                    for name in ("query_run", "query_check"):
                        invalid = await client.call_tool(name, {"sql": "SELECT FROM"})
                        self.assertTrue(invalid.is_error)
                        self.assertTrue(
                            invalid.structured_content is not None
                            or any(getattr(content, "text", "") for content in invalid.content)
                        )
                        self.assertNotIn("internal_failure", str(invalid.structured_content))
                        self.assertIn("query failed:", str(invalid.structured_content))
                    return ran.structured_content, checked.structured_content

        ran, checked = asyncio.run(exercise())
        expected = {
            "columns": [{"name": "item", "type": "VARCHAR"}, {"name": "item", "type": "VARCHAR"}],
            "rows": [["CA-R-2723", "Requirement"], ["CA-R-2725", "Requirement"]],
            "row_count": 2,
            "column_count": 2,
        }
        self.assertEqual(expected, ran)
        self.assertEqual({"valid": True, "row_count": 2, "column_count": 2}, checked)
        status, web_ran = _request(self.url + "/workbench/run", method="POST", payload={"sql": sql})
        self.assertEqual(200, status)
        self.assertEqual(expected, web_ran)
        status, web_checked = _request(self.url + "/workbench/check", method="POST", payload={"sql": sql})
        self.assertEqual(200, status)
        self.assertEqual(checked, web_checked)

    def test_workbench_http_run_check_and_read_only_failures_do_not_mutate_source(self) -> None:
        status, page = _request(self.url + "/workbench")
        self.assertEqual(200, status)
        self.assertIn("Workbench", page)
        status, checked = _request(self.url + "/workbench/check", method="POST", payload={"sql": "SELECT count(*) FROM atoms"})
        self.assertEqual(200, status)
        self.assertTrue(checked["valid"])
        status, ran = _request(self.url + "/workbench/run", method="POST", payload={"sql": "SELECT id FROM atoms WHERE id = 'CA-R-2723'"})
        self.assertEqual(200, status)
        self.assertEqual([["CA-R-2723"]], ran["rows"])
        for operation in ("run", "check"):
            status, failure = _request(
                self.url + f"/workbench/{operation}", method="POST", payload={"sql": "SELECT FROM"},
            )
            self.assertEqual(400, status)
            self.assertIsInstance(failure.get("error"), str)
            self.assertTrue(failure["error"])
        for sql in ("SELECT 1; SELECT 2", "CREATE TABLE forbidden(x INTEGER)"):
            status, failure = _request(self.url + "/workbench/run", method="POST", payload={"sql": sql})
            self.assertEqual(400, status)
            self.assertIn("error", failure)
        self.assertEqual(self.before_hash, hashlib.sha256(self.target.read_bytes()).hexdigest())

    def test_watchfiles_reloads_source_from_writable_docker_bind_mount(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            root.chmod(0o755)
            control = write_settings(root)
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
                        if _request(url + "/health")[0] == 200:
                            break
                    except OSError:
                        pass
                    time.sleep(0.2)
                else:
                    self.fail("watcher container did not become ready within 45 seconds")

                initial = _request(
                    url + "/workbench/run", method="POST",
                    payload={"sql": "SELECT version FROM atoms WHERE id = 'CA-R-901'"},
                )
                self.assertEqual(200, initial[0])
                self.assertEqual([[1]], initial[1]["rows"])
                write_atom(target, "CA-R-901", version=2, body="# Summary\n\nChanged from the host.\n")
                deadline = time.monotonic() + 20
                while time.monotonic() < deadline:
                    status, result = _request(
                        url + "/workbench/run", method="POST",
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
