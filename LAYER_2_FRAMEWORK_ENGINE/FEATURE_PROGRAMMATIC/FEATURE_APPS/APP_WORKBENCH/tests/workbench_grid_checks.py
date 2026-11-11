# CA-E-784@1
# CA-E-785@1
# CA-E-787@1
"""Real HTTP/MCP acceptance checks for cached Workbench grids and retention."""

from __future__ import annotations

import asyncio
import datetime as dt
import json
import time
from typing import Any
from uuid import uuid4

from http_paths import MCP_PATH
from workbench_docker_support import request


GRID_SQL = (
    "SELECT CASE WHEN i % 4 = 0 THEN 'Alpha%Hit' "
    "WHEN i % 4 = 1 THEN 'alphahit' WHEN i % 4 = 2 THEN 'beta' "
    "ELSE NULL END AS \"dup\", i % 3 AS \"dup\", i AS rowid, "
    "random() AS marker FROM range(0, 240) AS t(i) ORDER BY i"
)
PAGE_METADATA = (
    "query_id", "columns", "row_count", "source_row_count", "column_count",
    "offset", "page_size", "has_more",
)


class WorkbenchGridDockerMixin:
    """Grid and result-lifecycle tests composed into the existing Docker class."""

    def _http_interface(self, operation: str, arguments: dict[str, Any]) -> dict[str, Any]:
        status, value = request(
            self.url + f"{self.workbench_path}/interface", method="POST",
            payload={"operation": operation, "arguments": arguments},
        )
        self.assertEqual(200, status, value)
        self.assertIsInstance(value, dict)
        return value

    async def _mcp_sequence(self, calls: tuple[tuple[str, dict[str, Any]], ...]) -> tuple[Any, ...]:
        from mcp.client.session import ClientSession
        from mcp.client.streamable_http import streamable_http_client

        async with streamable_http_client(self.url + MCP_PATH) as streams:
            async with ClientSession(*streams, read_timeout_seconds=120) as client:
                await client.initialize()
                results = []
                for name, arguments in calls:
                    results.append(await client.call_tool(name, arguments))
                return tuple(results)

    def _mcp(self, *calls: tuple[str, dict[str, Any]]) -> tuple[Any, ...]:
        return asyncio.run(self._mcp_sequence(tuple(calls)))

    def test_workbench_grid_is_cached_and_identical_over_http_and_mcp(self) -> None:
        status, run = request(
            self.url + f"{self.workbench_path}/run", method="POST",
            payload={"result_delivery": "inline", "sql": GRID_SQL, "page_size": 5},
        )
        self.assertEqual(200, status, run)
        self.assertEqual(240, run["row_count"])
        self.assertEqual(5, len(run["rows"]))
        self.assertTrue(run["has_more"])
        self.assertEqual(["dup", "dup", "rowid", "marker"], [column["name"] for column in run["columns"]])
        self.assertEqual(4, run["column_count"])
        query_id = run["query_id"]

        sort_grid = {"sort": [{"column": 1, "direction": "desc"}, {"column": 2, "direction": "asc"}]}
        status, sorted_page = request(
            self.url + f"{self.workbench_path}/page", method="POST",
            payload={"result_delivery": "inline", "query_id": query_id, "offset": 0, "page_size": 8, "grid": sort_grid},
        )
        self.assertEqual(200, status, sorted_page)
        self.assertEqual(240, sorted_page["source_row_count"])
        self.assertEqual(240, sorted_page["row_count"])
        self.assertNotIn("groups", sorted_page)
        self.assertEqual([2, 5, 8, 11, 14, 17, 20, 23], [row[2] for row in sorted_page["rows"]])
        self.assertEqual(["dup", "dup", "rowid", "marker"], [column["name"] for column in sorted_page["columns"]])

        literal_grid = {"filters": [
            {"column": 0, "operator": "contains", "value": "%HIT"},
            {"column": 0, "operator": "contains", "value": "alpha"},
        ]}
        status, literal_page = request(
            self.url + f"{self.workbench_path}/page", method="POST",
            payload={"result_delivery": "inline", "query_id": query_id, "offset": 0, "page_size": 100, "grid": literal_grid},
        )
        self.assertEqual(200, status, literal_page)
        self.assertEqual(60, literal_page["row_count"])
        self.assertEqual(240, literal_page["source_row_count"])
        self.assertTrue(all(row[0] == "Alpha%Hit" for row in literal_page["rows"]))
        self.assertEqual(60, len(literal_page["rows"]))

        group_grid = {
            "sort": [{"column": 2, "direction": "asc"}],
            "group_by": {"column": 1, "direction": "asc"},
        }
        status, group_page = request(
            self.url + f"{self.workbench_path}/page", method="POST",
            payload={"result_delivery": "inline", "query_id": query_id, "offset": 0, "page_size": 5, "grid": group_grid},
        )
        self.assertEqual(200, status, group_page)
        self.assertEqual([0, 3, 6, 9, 12], [row[2] for row in group_page["rows"]])
        self.assertEqual([{"value": 0, "count": 80}], group_page["groups"])
        status, boundary_page = request(
            self.url + f"{self.workbench_path}/page", method="POST",
            payload={"result_delivery": "inline", "query_id": query_id, "offset": 79, "page_size": 2, "grid": group_grid},
        )
        self.assertEqual(200, status, boundary_page)
        self.assertEqual([237, 1], [row[2] for row in boundary_page["rows"]])
        self.assertEqual(
            [{"value": 0, "count": 80}, {"value": 1, "count": 80}], boundary_page["groups"],
        )

        status, repeated_page = request(
            self.url + f"{self.workbench_path}/page", method="POST",
            payload={"result_delivery": "inline", "query_id": query_id, "offset": 0, "page_size": 8, "grid": sort_grid},
        )
        self.assertEqual(200, status, repeated_page)
        self.assertEqual(sorted_page["rows"], repeated_page["rows"])

        mcp_sorted, mcp_group, mcp_bad = self._mcp(
            ("query_page", {"result_delivery": "inline", "query_id": query_id, "offset": 0, "page_size": 8, "grid": sort_grid}),
            ("query_page", {"result_delivery": "inline", "query_id": query_id, "offset": 79, "page_size": 2, "grid": group_grid}),
            ("query_page", {"result_delivery": "inline", "query_id": query_id, "offset": 0, "grid": {"sort": [{"column": 99, "direction": "asc"}]}}),
        )
        self.assertFalse(mcp_sorted.is_error, mcp_sorted.structured_content or mcp_sorted.content)
        self.assertFalse(mcp_group.is_error, mcp_group.structured_content or mcp_group.content)
        self.assertTrue(mcp_bad.is_error)
        for field in PAGE_METADATA:
            self.assertEqual(sorted_page[field], mcp_sorted.structured_content[field], field)
        self.assertEqual(sorted_page["rows"], mcp_sorted.structured_content["rows"])
        self.assertEqual(boundary_page["groups"], mcp_group.structured_content["groups"])
        self.assertEqual(boundary_page["rows"], mcp_group.structured_content["rows"])

        status, malformed = request(
            self.url + f"{self.workbench_path}/page", method="POST",
            payload={
                "query_id": query_id, "offset": 0,
                "grid": {"filters": [{"column": 0, "operator": "contains", "value": 4}]},
            },
        )
        self.assertEqual(400, status, malformed)
        status, ordinary = request(
            self.url + f"{self.workbench_path}/page", method="POST",
            payload={"result_delivery": "inline", "query_id": query_id, "offset": 0, "page_size": 5},
        )
        self.assertEqual(200, status, ordinary)
        self.assertEqual(query_id, ordinary["query_id"])
        self.assertEqual(run["rows"], ordinary["rows"])
        self.assertNotIn("sql", run)
        self.assertNotIn("sql", ordinary)

    def test_workbench_rejects_whole_query_at_http_and_mcp_without_mutating_cache(self) -> None:
        sql = "SELECT 1701 AS value"
        status, run = request(
            self.url + f"{self.workbench_path}/run", method="POST", payload={"result_delivery": "inline", "sql": sql, "page_size": 1},
        )
        self.assertEqual(200, status, run)
        cursor = len("SELECT 1; ".encode("utf-16-le")) // 2
        multi = {"sql": "SELECT 1; SELECT 2", "cursor_position": cursor}
        status, failed = request(self.url + f"{self.workbench_path}/run", method="POST", payload=multi)
        self.assertEqual(400, status, failed)
        self.assertIsInstance(failed.get("error"), str)
        (mcp_failed,) = self._mcp(("query_run", multi))
        self.assertTrue(mcp_failed.is_error)
        status, page = request(
            self.url + f"{self.workbench_path}/page", method="POST",
            payload={"result_delivery": "inline", "query_id": run["query_id"], "offset": 0, "page_size": 1},
        )
        self.assertEqual(200, status, page)
        self.assertEqual([[1701]], page["rows"])
        self.assertEqual(run["query_id"], page["query_id"])

    def test_workbench_result_ttl_pin_unpin_rerun_restart_and_hourly_log(self) -> None:  # noqa: C901
        settings = self.runtime_root / "caprmedio_runtime_settings.toml"
        self.assertFalse(settings.exists())
        watcher_log = self.workbench_state / "watcher-change-log.ndjson"

        def watcher_events() -> set[tuple[object, object, object, object]]:
            if not watcher_log.exists():
                return set()
            return {
                (
                    event.get("observed_at"), event.get("operation"),
                    event.get("old_path"), event.get("new_path"),
                )
                for line in watcher_log.read_text(encoding="utf-8").splitlines()
                if line and (event := json.loads(line))
            }

        def assert_runtime_settings_are_excluded(events: set[tuple[object, object, object, object]]) -> None:
            self.assertFalse(any(
                ".caprmedio_runtime/caprmedio_runtime_settings.toml" in {old, new}
                for _at, _operation, old, new in events
            ))

        watcher_before = watcher_events()

        status, default_result = request(
            self.url + f"{self.workbench_path}/run", method="POST",
            payload={"result_delivery": "inline", "sql": "SELECT random() AS default_marker", "page_size": 1},
        )
        self.assertEqual(200, status, default_result)
        default_query_id = default_result["query_id"]
        settings.write_text("[workbench]\nresult_ttl_seconds = 1\n", encoding="utf-8")
        time.sleep(1.2)
        status, before_restart = request(
            self.url + f"{self.workbench_path}/page", method="POST",
            payload={"result_delivery": "inline", "query_id": default_query_id, "offset": 0, "page_size": 1},
        )
        self.assertEqual(200, status, before_restart)
        self.assertEqual(default_result["rows"], before_restart["rows"])
        watcher_after_edit = watcher_events()
        self.assertTrue(watcher_before <= watcher_after_edit)
        assert_runtime_settings_are_excluded(watcher_after_edit)

        (restart,) = self._mcp(("workbench_restart", {}))
        self.assertFalse(restart.is_error, restart.structured_content or restart.content)
        status, after_restart = request(
            self.url + f"{self.workbench_path}/page", method="POST",
            payload={"result_delivery": "inline", "query_id": default_query_id, "offset": 0, "page_size": 1},
        )
        self.assertEqual(400, status, after_restart)
        watcher_after_restart = watcher_events()
        self.assertTrue(watcher_after_edit <= watcher_after_restart)
        assert_runtime_settings_are_excluded(watcher_after_restart)

        status, young = request(
            self.url + f"{self.workbench_path}/run", method="POST",
            payload={"result_delivery": "inline", "sql": "SELECT 7 AS young_value", "page_size": 1},
        )
        self.assertEqual(200, status, young)
        young_query_id = young["query_id"]
        time.sleep(0.3)
        status, young_page = request(
            self.url + f"{self.workbench_path}/page", method="POST",
            payload={"result_delivery": "inline", "query_id": young_query_id, "offset": 0, "page_size": 1},
        )
        self.assertEqual(200, status, young_page)
        time.sleep(1.0)
        status, expired = request(
            self.url + f"{self.workbench_path}/page", method="POST",
            payload={"result_delivery": "inline", "query_id": young_query_id, "offset": 0, "page_size": 1},
        )
        self.assertEqual(400, status, expired)

        session_id = f"docker-retention-{uuid4().hex}"
        (opened,) = self._mcp(("workspace_open", {"session_id": session_id}),)
        self.assertFalse(opened.is_error, opened.structured_content or opened.content)
        workspace = opened.structured_content
        workspace_id = workspace["workspace_id"]
        base_view_id = workspace["views"][0]["id"]
        (created,) = self._mcp(("view_create", {"workspace_id": workspace_id, "position": "last"}),)
        self.assertFalse(created.is_error, created.structured_content or created.content)
        pinned_view_id = created.structured_content["view_id"]
        (updated,) = self._mcp(("view_update", {
            "workspace_id": workspace_id, "view_id": pinned_view_id,
            "sql": "SELECT 8 AS pinned_value", "expected_revision": 0,
        }),)
        self.assertFalse(updated.is_error, updated.structured_content or updated.content)
        (pinned_run,) = self._mcp(("view_run", {"workspace_id": workspace_id, "view_id": pinned_view_id}),)
        self.assertFalse(pinned_run.is_error, pinned_run.structured_content or pinned_run.content)
        pinned_query_id = pinned_run.structured_content["query_id"]
        time.sleep(1.2)
        (pinned_page,) = self._mcp(("view_fetch", {
            "workspace_id": workspace_id, "view_id": pinned_view_id, "offset": 0, "page_size": 1,
        }),)
        self.assertFalse(pinned_page.is_error, pinned_page.structured_content or pinned_page.content)
        self.assertEqual(pinned_query_id, pinned_page.structured_content["query_id"])

        young_view_created = self._http_interface("view_create", {"workspace_id": workspace_id, "position": "last"})
        young_view_id = young_view_created["view_id"]
        young_view_update = self._http_interface("view_update", {
            "workspace_id": workspace_id, "view_id": young_view_id,
            "sql": "SELECT 9 AS young_view_value", "expected_revision": 0,
        })
        self.assertEqual(1, young_view_update["revision"])
        young_view_run = self._http_interface("view_run", {"workspace_id": workspace_id, "view_id": young_view_id})
        young_view_query_id = young_view_run["query_id"]
        self._http_interface("view_remove", {"workspace_id": workspace_id, "view_id": young_view_id})
        time.sleep(0.3)
        status, young_after_close = request(
            self.url + f"{self.workbench_path}/page", method="POST",
            payload={"result_delivery": "inline", "query_id": young_view_query_id, "offset": 0, "page_size": 1},
        )
        self.assertEqual(200, status, young_after_close)
        time.sleep(1.0)
        status, young_after_ttl = request(
            self.url + f"{self.workbench_path}/page", method="POST",
            payload={"result_delivery": "inline", "query_id": young_view_query_id, "offset": 0, "page_size": 1},
        )
        self.assertEqual(400, status, young_after_ttl)
        (removed_pinned,) = self._mcp(("view_remove", {"workspace_id": workspace_id, "view_id": pinned_view_id}),)
        self.assertFalse(removed_pinned.is_error, removed_pinned.structured_content or removed_pinned.content)
        (old_after_close,) = self._mcp(("query_page", {"result_delivery": "inline", "query_id": pinned_query_id, "offset": 0, "page_size": 1}),)
        self.assertTrue(old_after_close.is_error)

        (base_update,) = self._mcp(("view_update", {
            "workspace_id": workspace_id, "view_id": base_view_id,
            "sql": "SELECT 10 AS stable_value", "expected_revision": 0,
        }),)
        self.assertFalse(base_update.is_error, base_update.structured_content or base_update.content)
        (base_run,) = self._mcp(("view_run", {"workspace_id": workspace_id, "view_id": base_view_id}),)
        self.assertFalse(base_run.is_error, base_run.structured_content or base_run.content)
        old_query_id = base_run.structured_content["query_id"]
        (bad_update,) = self._mcp(("view_update", {
            "workspace_id": workspace_id, "view_id": base_view_id,
            "sql": "SELECT CAST('not-an-integer' AS INTEGER) AS bad_value", "expected_revision": 1,
        }),)
        self.assertFalse(bad_update.is_error, bad_update.structured_content or bad_update.content)
        (before_failed_run,) = self._mcp(("query_page", {"result_delivery": "inline", "query_id": old_query_id, "offset": 0, "page_size": 1}),)
        self.assertFalse(before_failed_run.is_error, before_failed_run.structured_content or before_failed_run.content)
        (failed_run,) = self._mcp(("view_run", {"workspace_id": workspace_id, "view_id": base_view_id}),)
        self.assertFalse(failed_run.is_error, failed_run.structured_content or failed_run.content)
        self.assertEqual("failed", failed_run.structured_content["status"])
        (after_failed_run,) = self._mcp(("query_page", {"result_delivery": "inline", "query_id": old_query_id, "offset": 0, "page_size": 1}),)
        self.assertTrue(after_failed_run.is_error)

        (saved,) = self._mcp(("view_save", {"sql": "SELECT 11 AS permanent_value", "name": "retention permanent"}),)
        self.assertFalse(saved.is_error, saved.structured_content or saved.content)
        saved_id = saved.structured_content["saved_query_id"]
        success_sql = "SELECT 12 AS hourly_success"
        failure_sql = "SELECT CAST('bad' AS INTEGER) AS hourly_failure"
        status, success = request(
            self.url + f"{self.workbench_path}/run", method="POST",
            payload={"result_delivery": "inline", "sql": success_sql, "page_size": 1},
        )
        self.assertEqual(200, status, success)
        status, failure = request(
            self.url + f"{self.workbench_path}/run", method="POST",
            payload={"result_delivery": "inline", "sql": failure_sql, "page_size": 1},
        )
        self.assertEqual(400, status, failure)

        (restart_again,) = self._mcp(("workbench_restart", {}))
        self.assertFalse(restart_again.is_error, restart_again.structured_content or restart_again.content)
        (loaded,) = self._mcp(("query_load", {"reference": saved_id}),)
        self.assertFalse(loaded.is_error, loaded.structured_content or loaded.content)
        self.assertEqual(saved_id, loaded.structured_content["saved_query_id"])
        self._assert_hourly_query_log(success_sql, failure_sql)

    def _assert_hourly_query_log(self, success_sql: str, failure_sql: str) -> None:
        query_log_directory = self.workbench_state / "query_log"
        query_log_directory.mkdir(parents=True, exist_ok=True)
        expired_id = f"expired-{uuid4().hex}"
        expired_at = dt.datetime.now(dt.UTC) - dt.timedelta(hours=49)
        expired_path = query_log_directory / f"query-log-{expired_at:%Y-%m-%d-%H}.ndjson"
        expired_record = {
            "log_id": expired_id, "at": expired_at.isoformat(), "sql": "SELECT expired",
            "outcome": "success", "error": None, "row_count": 1, "column_count": 1,
        }
        with expired_path.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(expired_record, separators=(",", ":")) + "\n")
        legacy = self.workbench_state / "query-log.json"
        legacy_before = legacy.read_bytes() if legacy.exists() else None
        (mcp_logs,) = self._mcp(("query_log_list", {"limit": 100}),)
        self.assertFalse(mcp_logs.is_error, mcp_logs.structured_content or mcp_logs.content)
        status, http_logs = request(
            self.url + f"{self.workbench_path}/interface", method="POST",
            payload={"operation": "query_log_list", "arguments": {"limit": 100}},
        )
        self.assertEqual(200, status, http_logs)
        self.assertEqual(
            {item["log_id"] for item in mcp_logs.structured_content["items"]},
            {item["log_id"] for item in http_logs["items"]},
        )
        records = mcp_logs.structured_content["items"]
        self.assertNotIn(expired_id, {item["log_id"] for item in records})
        self.assertTrue(any(item["sql"] == success_sql and item["outcome"] == "success" for item in records))
        self.assertTrue(any(item["sql"] == failure_sql and item["outcome"] == "failed" for item in records))
        selected = records[0]
        (mcp_record,) = self._mcp(("query_log_get", {"log_id": selected["log_id"]}),)
        self.assertFalse(mcp_record.is_error, mcp_record.structured_content or mcp_record.content)
        status, http_record = request(
            self.url + f"{self.workbench_path}/interface", method="POST",
            payload={"operation": "query_log_get", "arguments": {"log_id": selected["log_id"]}},
        )
        self.assertEqual(200, status, http_record)
        self.assertEqual(selected, mcp_record.structured_content)
        self.assertEqual(selected, http_record)
        for record in records:
            self.assertEqual(
                {"log_id", "at", "sql", "outcome", "error", "row_count", "column_count"}, set(record), record,
            )
            observed = dt.datetime.fromisoformat(record["at"])
            self.assertIsNotNone(observed.tzinfo)
            self.assertLess(dt.datetime.now(dt.UTC) - observed.astimezone(dt.UTC), dt.timedelta(hours=48))

        hourly_files = sorted(query_log_directory.glob("query-log-*.ndjson"))
        self.assertTrue(hourly_files, query_log_directory)
        file_records = []
        for path in hourly_files:
            self.assertRegex(path.name, r"^query-log-\d{4}-\d{2}-\d{2}-\d{2}\.ndjson$")
            hour = dt.datetime.strptime(path.stem.removeprefix("query-log-"), "%Y-%m-%d-%H").replace(tzinfo=dt.UTC)
            for line in path.read_text(encoding="utf-8").splitlines():
                if not line:
                    continue
                record = json.loads(line)
                observed = dt.datetime.fromisoformat(record["at"]).astimezone(dt.UTC)
                self.assertEqual(hour, observed.replace(minute=0, second=0, microsecond=0))
                file_records.append(record)
        self.assertTrue(file_records)
        self.assertTrue({record["log_id"] for record in records} <= {record["log_id"] for record in file_records})
        legacy_after = legacy.read_bytes() if legacy.exists() else None
        self.assertEqual(legacy_before, legacy_after)
