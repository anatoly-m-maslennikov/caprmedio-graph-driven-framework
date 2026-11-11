# CA-E-677@16
# CA-E-780@7
"""Disposable Docker performance gates composed into the Workbench E2E case."""

from __future__ import annotations

import asyncio
from pathlib import Path
import shutil
import subprocess
import tempfile
import time
from typing import Callable
from uuid import uuid4

from http_paths import HEALTH_PATH, MCP_PATH, WORKBENCH_PATH
from workbench_docker_support import free_port, project_name, request
from workbench_performance_assertions import assert_performance_batch
from workbench_performance_fixture import (
    BATCH_COUNT,
    FIXTURE_ATOM_COUNT,
    RENAMED_TARGET_SCOPE,
    SOURCE_SCOPE,
    TARGET_SCOPE,
    prepare_fixture,
)
from workbench_performance_metrics import (
    BATCH_BUDGET_SECONDS,
    MOVE_BUDGET_SECONDS,
    REBUILD_BUDGET_SECONDS,
    STRUCTURAL_BUDGET_SECONDS,
    record_performance,
)


POLL_SECONDS = 0.05
OBSERVATION_TIMEOUT_SECONDS = 90


class WorkbenchPerformanceDockerMixin:
    """Bulk source lifecycle and cold rebuild gates; the main test owns image setup."""

    def test_workbench_performance_gates(self) -> None:  # noqa: C901
        with tempfile.TemporaryDirectory() as temporary:
            fixture = prepare_fixture(Path(temporary))
            state = Path(temporary) / "workbench"
            state.mkdir()
            state.chmod(0o777)
            handle = self._start_performance_container(fixture.root, state)
            _process, name, url, stdout, stderr = handle
            workbench_path = f"{WORKBENCH_PATH}/{project_name(fixture.control)}"
            database = state / "projection.duckdb"

            def rows(sql: str) -> list[dict[str, object]]:
                status, result = request(
                    url + f"{workbench_path}/run",
                    method="POST",
                    payload={"sql": sql, "page_size": 1_000, "result_delivery": "inline"},
                )
                self.assertEqual(200, status, result)
                self.assertIsInstance(result, dict)
                self.assertFalse(result["has_more"], result)
                columns = [column["name"] for column in result["columns"]]
                return [dict(zip(columns, row, strict=True)) for row in result["rows"]]

            def scalar(sql: str) -> object:
                result = rows(sql)
                self.assertEqual(1, len(result), result)
                self.assertEqual(1, len(result[0]), result)
                return next(iter(result[0].values()))

            def relation_count(
                relation: str, *, source: str | None = None, target: str | None = None
            ) -> int:
                conditions = []
                if source is not None:
                    conditions.append(f"source = '{source}'")
                if target is not None:
                    conditions.append(f"target = '{target}'")
                where = "" if not conditions else "\nwhere " + "\n  and ".join(conditions)
                return int(
                    scalar(
                        "SELECT count(*)\n"
                        "FROM GRAPH_TABLE (\n"
                        f"  caprmedio MATCH (a:Reference)-[e:{relation}]->(b:Reference)\n"
                        "  COLUMNS (a.ref AS source, b.ref AS target)\n"
                        ")"
                        f"{where}\n;"
                    )
                )

            def assert_batch(
                *,
                version: int,
                scope_id: str,
                scope_name: str,
                suffix: str,
                expected_total: int,
                batch_present: bool = True,
                content_changed: bool = False,
                content_version: int = 1,
                absent_scope_name: str | None = None,
            ) -> None:
                assert_performance_batch(
                    self,
                    fixture,
                    rows,
                    scalar,
                    relation_count,
                    version=version,
                    scope_id=scope_id,
                    scope_name=scope_name,
                    suffix=suffix,
                    expected_total=expected_total,
                    batch_present=batch_present,
                    content_changed=content_changed,
                    content_version=content_version,
                    absent_scope_name=absent_scope_name,
                )

            def wait_for(
                operation: str,
                started_at: float,
                budget: float,
                probe: Callable[[], None],
                *,
                items: int,
            ) -> None:
                deadline = started_at + OBSERVATION_TIMEOUT_SECONDS
                failure: AssertionError | None = None
                while time.monotonic() < deadline:
                    try:
                        probe()
                    except AssertionError as error:
                        failure = error
                        time.sleep(POLL_SECONDS)
                    else:
                        record_performance(
                            self,
                            operation=operation,
                            measurement="filesystem_mutation_to_verified_graph",
                            started_at=started_at,
                            budget_seconds=budget,
                            items=items,
                        )
                        return
                self.fail(f"{operation} did not reach its expected graph state: {failure}")

            def wait_batch(
                operation: str,
                started_at: float,
                budget: float,
                *,
                version: int,
                scope_id: str,
                scope_name: str,
                suffix: str,
                content_changed: bool = False,
                content_version: int = 1,
                absent_scope_name: str | None = None,
            ) -> None:
                wait_for(
                    operation,
                    started_at,
                    budget,
                    lambda: assert_batch(
                        version=version,
                        scope_id=scope_id,
                        scope_name=scope_name,
                        suffix=suffix,
                        expected_total=FIXTURE_ATOM_COUNT + BATCH_COUNT,
                        content_changed=content_changed,
                        content_version=content_version,
                        absent_scope_name=absent_scope_name,
                    ),
                    items=BATCH_COUNT,
                )

            try:
                self.assertFalse(database.exists(), "health must not warm the Workbench index")
                cold_started = time.monotonic()
                assert_batch(
                    version=1,
                    scope_id=fixture.source_scope_id,
                    scope_name=SOURCE_SCOPE,
                    suffix="created",
                    expected_total=FIXTURE_ATOM_COUNT,
                    batch_present=False,
                )
                self.assertTrue(
                    database.is_file(), "first query must create the persistent projection"
                )
                record_performance(
                    self,
                    operation="cold_index",
                    measurement="fresh_store_to_verified_graph",
                    started_at=cold_started,
                    budget_seconds=REBUILD_BUDGET_SECONDS,
                    fixture_atom_count=FIXTURE_ATOM_COUNT,
                )

                created = fixture.batch_directory
                create_started = time.monotonic()
                fixture.staging_directory.rename(created)
                fixture.batch_directory = created
                wait_batch(
                    "batch_create",
                    create_started,
                    BATCH_BUDGET_SECONDS,
                    version=1,
                    scope_id=fixture.source_scope_id,
                    scope_name=SOURCE_SCOPE,
                    suffix="created",
                )

                update_started = time.monotonic()
                fixture.rewrite_batch(
                    version=2,
                    scope_id=fixture.source_scope_id,
                    scope_name=SOURCE_SCOPE,
                    changed=True,
                )
                wait_batch(
                    "batch_update",
                    update_started,
                    BATCH_BUDGET_SECONDS,
                    version=2,
                    scope_id=fixture.source_scope_id,
                    scope_name=SOURCE_SCOPE,
                    suffix="created",
                    content_changed=True,
                    content_version=2,
                )

                rename_started = time.monotonic()
                fixture.rename_batch_files(version=3, suffix="renamed", changed=False)
                wait_batch(
                    "batch_rename",
                    rename_started,
                    MOVE_BUDGET_SECONDS,
                    version=3,
                    scope_id=fixture.source_scope_id,
                    scope_name=SOURCE_SCOPE,
                    suffix="renamed",
                    content_changed=True,
                    content_version=2,
                )

                combined_started = time.monotonic()
                fixture.rename_batch_files(version=4, suffix="combined", changed=True)
                wait_batch(
                    "batch_rename_update",
                    combined_started,
                    MOVE_BUDGET_SECONDS,
                    version=4,
                    scope_id=fixture.source_scope_id,
                    scope_name=SOURCE_SCOPE,
                    suffix="combined",
                    content_changed=True,
                    content_version=4,
                )

                move_started = time.monotonic()
                fixture.move_batch_to_target(version=5)
                wait_batch(
                    "batch_move",
                    move_started,
                    MOVE_BUDGET_SECONDS,
                    version=5,
                    scope_id=fixture.target_scope_id,
                    scope_name=TARGET_SCOPE,
                    suffix="combined",
                    content_changed=True,
                    content_version=4,
                )

                rename_scope_started = time.monotonic()
                fixture.rename_target_scope(version=6)
                wait_batch(
                    "scope_rename",
                    rename_scope_started,
                    STRUCTURAL_BUDGET_SECONDS,
                    version=6,
                    scope_id=fixture.target_scope_id,
                    scope_name=RENAMED_TARGET_SCOPE,
                    suffix="combined",
                    content_changed=True,
                    content_version=4,
                    absent_scope_name=TARGET_SCOPE,
                )
                remove_started = time.monotonic()
                shutil.rmtree(fixture.batch_directory)
                wait_for(
                    "batch_remove",
                    remove_started,
                    BATCH_BUDGET_SECONDS,
                    lambda: assert_batch(
                        version=6,
                        scope_id=fixture.target_scope_id,
                        scope_name=RENAMED_TARGET_SCOPE,
                        suffix="combined",
                        expected_total=FIXTURE_ATOM_COUNT,
                        batch_present=False,
                    ),
                    items=BATCH_COUNT,
                )

                reread_started = time.monotonic()
                self.assertEqual(
                    {"service": "workbench", "status": "ready"}, self._full_reread(url)
                )
                assert_batch(
                    version=6,
                    scope_id=fixture.target_scope_id,
                    scope_name=RENAMED_TARGET_SCOPE,
                    suffix="combined",
                    expected_total=FIXTURE_ATOM_COUNT,
                    batch_present=False,
                )
                record_performance(
                    self,
                    operation="full_reread",
                    measurement="discarded_store_to_verified_graph",
                    started_at=reread_started,
                    budget_seconds=REBUILD_BUDGET_SECONDS,
                    fixture_atom_count=FIXTURE_ATOM_COUNT,
                )
            except Exception:
                logs = subprocess.run(
                    ["docker", "logs", name],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                print(f"WORKBENCH_PERFORMANCE_FAILURE_LOGS\n{logs.stdout}{logs.stderr}")
                raise
            finally:
                self._stop_performance_container(handle)

    def _start_performance_container(self, root: Path, state: Path):
        name = f"caprmedio-workbench-performance-{uuid4().hex}"
        port = free_port()
        url = f"http://127.0.0.1:{port}"
        stdout = tempfile.TemporaryFile(mode="w+t", encoding="utf-8")
        stderr = tempfile.TemporaryFile(mode="w+t", encoding="utf-8")
        process = subprocess.Popen(
            [
                "docker",
                "run",
                "--rm",
                "--name",
                name,
                "--label",
                "caprmedio.test=workbench-performance",
                "--memory=1536m",
                "--memory-swap=1536m",
                "--tmpfs",
                "/tmp:rw,nosuid,nodev,size=256m",
                "-p",
                f"127.0.0.1:{port}:8092",
                "-v",
                f"{root}:/project:rw",
                "-v",
                f"{state}:/project/.caprmedio_runtime/workbench:rw",
                self.image,
                "mcp-http",
            ],
            cwd=Path(__file__).resolve().parents[5],
            stdout=stdout,
            stderr=stderr,
            text=True,
        )
        deadline = time.monotonic() + 45
        while time.monotonic() < deadline:
            if process.poll() is not None:
                stdout.seek(0)
                stderr.seek(0)
                raise AssertionError(
                    f"performance container exited during startup\nstdout:\n{stdout.read()}\nstderr:\n{stderr.read()}"
                )
            try:
                if request(url + HEALTH_PATH)[0] == 200:
                    return process, name, url, stdout, stderr
            except OSError:
                pass
            time.sleep(0.2)
        raise AssertionError("performance container did not become healthy within 45 seconds")

    @staticmethod
    def _stop_performance_container(handle: tuple[object, str, str, object, object]) -> None:
        process, name, _url, stdout, stderr = handle
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
        subprocess.run(
            ["docker", "container", "rm", "-f", name], capture_output=True, text=True, check=False
        )
        stdout.close()
        stderr.close()

    @staticmethod
    def _full_reread(url: str) -> dict[str, object]:
        from mcp.client.session import ClientSession
        from mcp.client.streamable_http import streamable_http_client

        async def reread() -> dict[str, object]:
            async with streamable_http_client(url + MCP_PATH) as streams:
                async with ClientSession(*streams, read_timeout_seconds=120) as client:
                    await client.initialize()
                    result = await client.call_tool("workbench_reread", {})
                    if result.is_error or not isinstance(result.structured_content, dict):
                        raise AssertionError(result.structured_content or result.content)
                    return result.structured_content

        return asyncio.run(reread())
