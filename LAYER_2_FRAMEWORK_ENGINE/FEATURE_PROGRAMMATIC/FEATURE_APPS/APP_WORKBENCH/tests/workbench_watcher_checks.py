# CA-E-780@1

"""Docker watcher checks mixed into the existing Workbench E2E fixture."""

from __future__ import annotations

import asyncio
import datetime as dt
import json
from pathlib import Path
import subprocess
import tempfile
import time
from uuid import uuid4

from scope_declaration_test_support import write_scope_unit_declarations
from smalltest_support import source_path, write_atom, write_settings
from workbench_docker_support import free_port, project_name as read_project_name, request
from http_paths import HEALTH_PATH, MCP_PATH, WORKBENCH_PATH


CHANGE_LOG_FIELDS = ("observed_at", "operation", "old_path", "new_path")


def _event_rows(path: Path) -> list[dict[str, object]]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def _event_sort_key(row: dict[str, object]) -> tuple[str, str, str, str]:
    observed_at = dt.datetime.fromisoformat(str(row["observed_at"])).astimezone(dt.UTC).isoformat()
    return (
        observed_at,
        str(row["operation"]),
        str(row["old_path"] or ""),
        str(row["new_path"] or ""),
    )


class WorkbenchWatcherDockerMixin:
    """Native filesystem watcher proof composed into WorkbenchDockerE2E."""

    def test_watchdog_records_native_events_and_retains_them_across_reread_and_restart(self) -> None:  # noqa: C901
        with tempfile.TemporaryDirectory() as temporary:
            temporary_root = Path(temporary)
            root = temporary_root / "repository"
            root.mkdir()
            root.chmod(0o755)
            control = write_settings(root)
            fixture_project_name = read_project_name(control)
            workbench_path = f"{WORKBENCH_PATH}/{fixture_project_name}"
            declarations = write_scope_unit_declarations(root, control_root=control)
            source_directory = source_path(declarations, "fixture", "04_requirement", "placeholder.md").parent
            write_atom(source_directory / "CA-R-901-docker.md", "CA-R-901")
            moved_parent = source_directory / "move-parent"
            moved_parent.mkdir()
            directory_parent = control / "watch-dir-parent"
            directory_parent.mkdir()
            outside = root / "outside"
            outside.mkdir()
            incoming = outside / "incoming.md"
            write_atom(incoming, "CA-R-903")
            workbench_state = temporary_root / "workbench"
            workbench_state.mkdir()
            workbench_state.chmod(0o777)

            def relative(path: Path) -> str:
                return path.relative_to(root).as_posix()

            def query_rows(url: str) -> list[dict[str, object]]:
                status, result = request(
                    url + f"{workbench_path}/run", method="POST",
                    payload={
                        "sql": (
                            "SELECT observed_at, operation, old_path, new_path FROM change_log "
                            "ORDER BY observed_at, operation, old_path NULLS FIRST, new_path NULLS FIRST"
                        ),
                        "page_size": 1000,
                    },
                )
                if status != 200 or not isinstance(result, dict):
                    return []
                columns = [column["name"] for column in result["columns"]]
                self.assertEqual(list(CHANGE_LOG_FIELDS), columns)
                self.assertFalse(result["has_more"], result)
                return [dict(zip(columns, row, strict=True)) for row in result["rows"]]

            def assert_same_log(rows: list[dict[str, object]]) -> None:
                file_rows = _event_rows(workbench_state / "watcher-change-log.ndjson")
                for row in file_rows:
                    self.assertEqual(set(CHANGE_LOG_FIELDS), set(row), row)
                self.assertEqual(
                    sorted(_event_sort_key(row) for row in rows),
                    sorted(_event_sort_key(row) for row in file_rows),
                )

            def wait_for_events(
                url: str, expected: list[tuple[str, str | None, str | None]],
            ) -> list[dict[str, object]]:
                deadline = time.monotonic() + 20
                while time.monotonic() < deadline:
                    rows = query_rows(url)
                    keys = {
                        (str(row["operation"]), row["old_path"], row["new_path"])
                        for row in rows
                    }
                    if set(expected) <= keys:
                        try:
                            assert_same_log(rows)
                        except AssertionError:
                            time.sleep(0.2)
                            continue
                        return rows
                    time.sleep(0.2)
                self.fail(f"watcher did not deliver expected events: {expected}; file={_event_rows(workbench_state / 'watcher-change-log.ndjson')}")

            def wait_for_atom(url: str, atom_id: str, expected_rows: list[list[object]]) -> None:
                deadline = time.monotonic() + 20
                while time.monotonic() < deadline:
                    status, result = request(
                        url + f"{workbench_path}/run", method="POST",
                        payload={
                            "sql": f"SELECT version, \"relative path\", filename FROM atoms WHERE id = '{atom_id}'",
                        },
                    )
                    if status == 200 and isinstance(result, dict) and result.get("rows") == expected_rows:
                        return
                    time.sleep(0.2)
                self.fail(f"watcher did not refresh atom {atom_id}: expected={expected_rows}")

            def start_container():
                name = f"caprmedio-workbench-watch-{uuid4().hex}"
                port = free_port()
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
                        "-v", f"{workbench_state}:/project/.caprmedio_runtime/workbench:rw",
                        self.image, "mcp-http",
                    ],
                    cwd=Path(__file__).resolve().parents[5], stdout=stdout, stderr=stderr, text=True,
                )
                deadline = time.monotonic() + 45
                while time.monotonic() < deadline:
                    if process.poll() is not None:
                        stdout.seek(0)
                        stderr.seek(0)
                        raise AssertionError(
                            f"watcher container exited during startup\nstdout:\n{stdout.read()}\nstderr:\n{stderr.read()}"
                        )
                    try:
                        if request(url + HEALTH_PATH)[0] == 200:
                            return process, name, url, stdout, stderr
                    except OSError:
                        pass
                    time.sleep(0.2)
                self.fail("watcher container did not become ready within 45 seconds")

            def stop_container(handle) -> None:
                process, name, _url, stdout, stderr = handle
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

            handle = start_container()
            try:
                _process, _name, url, _stdout, _stderr = handle
                status, schema = request(url + f"{workbench_path}/schema", method="POST", payload={})
                self.assertEqual(200, status, schema)
                self.assertEqual({"atoms", "scope_units", "change_log"}, set(schema["tables"]))
                self.assertEqual(
                    list(CHANGE_LOG_FIELDS),
                    [column["name"] for column in schema["tables"]["change_log"]],
                )
                initial = request(
                    url + f"{workbench_path}/run", method="POST",
                    payload={"sql": "SELECT version FROM atoms WHERE id = 'CA-R-901'"},
                )
                self.assertEqual(200, initial[0], initial[1])
                self.assertEqual([[1]], initial[1]["rows"])
                baseline = query_rows(url)
                assert_same_log(baseline)

                expected: list[tuple[str, str | None, str | None]] = []

                def observe(operation: str, old_path: Path | None, new_path: Path | None) -> None:
                    expected.append((operation, relative(old_path) if old_path else None, relative(new_path) if new_path else None))
                    wait_for_events(url, expected)

                created = source_directory / "CA-R-902-created.md"
                write_atom(created, "CA-R-902")
                wait_for_atom(url, "CA-R-902", [[1, relative(created.parent), created.name]])
                observe("create", None, created)
                write_atom(created, "CA-R-902", version=2, body="# Summary\n\nChanged from the host.\n")
                wait_for_atom(url, "CA-R-902", [[2, relative(created.parent), created.name]])
                observe("update", None, created)
                renamed = source_directory / "renamed.md"
                created.rename(renamed)
                wait_for_atom(url, "CA-R-902", [[2, relative(renamed.parent), renamed.name]])
                observe("rename", created, renamed)
                moved = moved_parent / "moved-name.md"
                renamed.rename(moved)
                wait_for_atom(url, "CA-R-902", [[2, relative(moved.parent), moved.name]])
                observe("move", renamed, moved)
                moved.unlink()
                wait_for_atom(url, "CA-R-902", [])
                observe("remove", moved, None)

                directory_source = control / "watch-dir-source"
                directory_source.mkdir()
                observe("create", None, directory_source)
                directory_target = directory_parent / "watch-dir-target"
                directory_source.rename(directory_target)
                observe("move", directory_source, directory_target)
                directory_target.rmdir()
                observe("remove", directory_target, None)

                entered = source_directory / "entered.md"
                incoming.rename(entered)
                wait_for_atom(url, "CA-R-903", [[1, relative(entered.parent), entered.name]])
                observe("create", None, entered)
                outgoing = outside / "outgoing.md"
                entered.rename(outgoing)
                wait_for_atom(url, "CA-R-903", [])
                observe("remove", entered, None)

                outside_only = outside / "outside.md"
                write_atom(outside_only, "CA-R-904")
                write_atom(outside_only, "CA-R-904", version=2)
                outside_renamed = outside / "outside-renamed.md"
                outside_only.rename(outside_renamed)
                outside_renamed.unlink()

                rows = wait_for_events(url, expected)
                assert_same_log(rows)
                self.assertTrue(rows)
                self.assertFalse(
                    any(
                        str(row["old_path"] or "").startswith("outside/")
                        or str(row["new_path"] or "").startswith("outside/")
                        for row in rows
                    )
                )
                directory_paths = {relative(directory_source), relative(directory_target)}
                self.assertFalse(
                    any(
                        row["operation"] == "update"
                        and (row["old_path"] in directory_paths or row["new_path"] in directory_paths)
                        for row in rows
                    )
                )

                before_reread = sorted(_event_sort_key(row) for row in rows)

                async def reread() -> dict[str, object]:
                    from mcp.client.session import ClientSession
                    from mcp.client.streamable_http import streamable_http_client

                    async with streamable_http_client(url + MCP_PATH) as streams:
                        async with ClientSession(*streams, read_timeout_seconds=120) as client:
                            await client.initialize()
                            result = await client.call_tool("workbench_reread", {})
                            self.assertFalse(result.is_error, result.structured_content)
                            return result.structured_content

                self.assertEqual({"service": "workbench", "status": "ready"}, asyncio.run(reread()))
                reread_rows = wait_for_events(url, expected)
                self.assertEqual(before_reread, sorted(_event_sort_key(row) for row in reread_rows))
                assert_same_log(reread_rows)

                stop_container(handle)
                handle = start_container()
                _process, _name, restarted_url, _stdout, _stderr = handle
                restarted_rows = wait_for_events(restarted_url, expected)
                self.assertEqual(before_reread, sorted(_event_sort_key(row) for row in restarted_rows))
                assert_same_log(restarted_rows)
            finally:
                stop_container(handle)
