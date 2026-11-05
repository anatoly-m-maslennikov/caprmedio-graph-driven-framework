# CA-E-684@2
# CA-E-788@1

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
import sys
import tempfile
import unittest


APP_ROOT = Path(__file__).resolve().parents[2]
TOOLS_ROOT = APP_ROOT.parent / "FEATURE_TOOLS"
sys.path[:0] = [str(APP_ROOT), str(TOOLS_ROOT), str(TOOLS_ROOT / "VALIDATE_ATOMS"), str(Path(__file__).parent)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.errors import WorkbenchUnavailableError  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from smalltest_support import extension_directory, write_settings  # noqa: E402


class WorkspaceBackendTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "project"
        self.root.mkdir()
        control = write_settings(self.root)
        write_scope_unit_declarations(
            self.root,
            ({"scope_unit_name": "ENGINE", "scope_unit_type": "Ordered", "scope_unit_label": "LAYER", "local_order": 1},),
            control_root=control,
        )
        self.service = WorkbenchService(self.root, extension_directory=extension_directory(APP_ROOT.parents[2]))
        self.addCleanup(self.service.close)

    def call(self, operation: str, **arguments):
        return self.service.interface_call(operation, arguments)

    def test_isolated_workspace_views_results_log_and_save(self) -> None:
        first, second = self.call("workspace_open", session_id="native-a"), self.call("workspace_open", session_id="native-b")
        first_view, second_view = first["views"][0], second["views"][0]
        self.assertEqual("native-a", first["workspace_id"])
        self.assertEqual([{"workspace_id": "native-a"}, {"workspace_id": "native-b"}], self.call("workspace_list")["items"])
        self.assertNotIn("sql", self.call("view_list", workspace_id="native-a")["views"][0])
        with self.assertRaisesRegex(ValueError, "unknown view_id"):
            self.call("view_get", workspace_id="native-b", view_id=first_view["id"])

        created = self.call("view_create", workspace_id="native-a", position="first", name="First")
        query_view = created["views"][0]
        self.assertEqual(created["view_id"], query_view["id"])
        updated = self.call("view_update", workspace_id="native-a", view_id=query_view["id"], sql="SELECT range AS value FROM range(3)", expected_revision=0)
        self.assertEqual(1, updated["revision"])
        with self.assertRaisesRegex(ValueError, "expected_revision does not match"):
            self.call("view_update", workspace_id="native-a", view_id=query_view["id"], sql="SELECT 2", expected_revision=0)

        run = self.call("view_run", workspace_id="native-a", view_id=query_view["id"])
        self.assertEqual({"workspace_id", "view_id", "revision", "status", "error", "query_id", "row_count", "column_count"}, set(run))
        self.assertEqual(("success", None, 3, 1), (run["status"], run["error"], run["row_count"], run["column_count"]))
        fetched = self.call("view_fetch", workspace_id="native-a", view_id=query_view["id"], offset=1, page_size=2, preview=1)
        self.assertEqual([[1]], fetched["rows"])
        ordered = self.call(
            "view_fetch", workspace_id="native-a", view_id=query_view["id"], offset=0,
            page_size=2, grid={"sort": [{"column": 0, "direction": "desc"}]},
        )
        self.assertEqual([[2], [1]], ordered["rows"])
        self.assertEqual([], self.call("view_fetch", workspace_id="native-a", view_id=query_view["id"], offset=0, preview=0)["rows"])
        for arguments, message in (
            ({"cursor_position": 999}, "cursor_position is outside SQL"),
            ({"preview": True}, "preview must be a non-negative integer"),
            ({"save": "yes"}, "save must be a boolean"),
            ({"name": "forbidden"}, "name is only supported when save is true"),
        ):
            with self.subTest(arguments=arguments), self.assertRaisesRegex(ValueError, message):
                self.call("view_run", workspace_id="native-a", view_id=query_view["id"], **arguments)
            self.assertEqual([[1], [2]], self.call("view_fetch", workspace_id="native-a", view_id=query_view["id"], offset=1, page_size=2)["rows"])
        before_check = len(self.call("query_log_list", limit=20)["items"])
        self.call("view_check", workspace_id="native-a", view_id=query_view["id"])
        self.assertEqual(before_check, len(self.call("query_log_list", limit=20)["items"]))

        self.call("view_update", workspace_id="native-a", view_id=query_view["id"], sql="SELECT FROM", expected_revision=1)
        self.assertEqual(
            [[0], [1]],
            self.call(
                "view_fetch", workspace_id="native-a", view_id=query_view["id"],
                offset=0, page_size=2,
            )["rows"],
        )
        failed = self.call("view_run", workspace_id="native-a", view_id=query_view["id"])
        self.assertEqual(("failed", None, None), (failed["status"], failed["row_count"], failed["column_count"]))
        self.assertTrue(failed["error"])
        with self.assertRaisesRegex(ValueError, "no current result"):
            self.call("view_fetch", workspace_id="native-a", view_id=query_view["id"])
        logs = self.call("query_log_list", limit=20)["items"]
        self.assertEqual("SELECT FROM", logs[0]["sql"])
        self.assertEqual("failed", logs[0]["outcome"])

        saved = self.call("view_save", workspace_id="native-a", view_id=query_view["id"])
        self.assertEqual(query_view["id"], saved["view_id"])
        self.assertEqual("SELECT FROM", self.service.load(saved["saved_query_id"])["sql"])
        with self.assertRaisesRegex(ValueError, "cannot remove the last view"):
            self.call("view_remove", workspace_id="native-b", view_id=second_view["id"])

        self.call(
            "view_update", workspace_id="native-a", view_id=query_view["id"],
            sql="SELECT error('restart required')", expected_revision=2,
        )
        ordinary_failure = self.call("view_run", workspace_id="native-a", view_id=query_view["id"])
        self.assertEqual("failed", ordinary_failure["status"])
        self.assertIn("restart required", ordinary_failure["error"])

        expired_at = dt.datetime.now(dt.UTC) - dt.timedelta(days=8)
        log_path = self.service._query_log._hour_path(expired_at)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text(json.dumps({
            "log_id": "expired", "at": expired_at.isoformat(), "sql": "SELECT old",
            "outcome": "success", "error": None, "row_count": 1, "column_count": 1,
        }) + "\n", encoding="utf-8")
        self.assertNotIn("expired", [item["log_id"] for item in self.call("query_log_list", limit=20)["items"]])
        self.assertFalse(log_path.exists())

    def test_view_run_propagates_an_unavailable_startup(self) -> None:
        opened = self.call("workspace_open", session_id="invalid-runtime-settings")
        view = opened["views"][0]
        self.call(
            "view_update", workspace_id=opened["workspace_id"], view_id=view["id"],
            sql="SELECT 1", expected_revision=0,
        )
        settings = self.root / ".caprmedio_runtime" / "caprmedio_runtime_settings.toml"
        settings.parent.mkdir(parents=True, exist_ok=True)
        settings.write_text("[workbench]\nresult_ttl_seconds = 0\n", encoding="utf-8")

        with self.assertRaisesRegex(WorkbenchUnavailableError, "positive integer"):
            self.call("view_run", workspace_id=opened["workspace_id"], view_id=view["id"])


if __name__ == "__main__":
    unittest.main()
