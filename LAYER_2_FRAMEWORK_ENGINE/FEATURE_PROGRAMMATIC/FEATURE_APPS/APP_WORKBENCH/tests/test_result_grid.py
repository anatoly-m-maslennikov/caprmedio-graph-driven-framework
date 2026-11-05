# CA-E-784@1
# CA-E-788@1
# CA-M-493@1

from __future__ import annotations

from pathlib import Path
import sys
import time
import unittest


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(APP_ROOT), str(Path(__file__).parent)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_store import QueryStore  # noqa: E402
from smalltest_support import extension_directory  # noqa: E402


class ResultGridTest(unittest.TestCase):
    def setUp(self) -> None:
        self.store = QueryStore(extension_directory=extension_directory(APP_ROOT.parents[2]))

    def tearDown(self) -> None:
        self.store.close()

    def test_native_grid_uses_positions_literal_filters_and_page_groups(self) -> None:
        result = self.store.run(
            "WITH source(ord, label, bucket) AS (VALUES "
            "(2, 'draft %', 'alpha'), (1, 'DRAFT plain', 'alpha'), "
            "(3, 'draft %', 'beta'), (1, 'other', 'beta'), (1, 'draft _', 'beta')) "
            'SELECT ord AS duplicate, ord AS duplicate, label AS "dotted.alias", bucket AS rowid FROM source'
        )
        query_id = result["query_id"]
        self.assertEqual(["duplicate", "duplicate", "dotted.alias", "rowid"],
                         [column["name"] for column in result["columns"]])

        grid = {
            "filters": [{"column": 2, "operator": "contains", "value": "draft"}],
            "sort": [{"column": 0, "direction": "asc"}],
            "group_by": {"column": 3, "direction": "desc"},
        }
        first = self.store.page(query_id, 0, page_size=1, grid=grid)
        second = self.store.page(query_id, 1, page_size=1, grid=grid)
        third = self.store.page(query_id, 2, page_size=1, grid=grid)

        self.assertEqual([[1, 1, "draft _", "beta"]], first["rows"])
        self.assertEqual([[3, 3, "draft %", "beta"]], second["rows"])
        self.assertEqual([[1, 1, "DRAFT plain", "alpha"]], third["rows"])
        self.assertEqual(4, first["row_count"])
        self.assertEqual(5, first["source_row_count"])
        self.assertEqual([{"value": "beta", "count": 2}], first["groups"])
        self.assertEqual([{"value": "beta", "count": 2}], second["groups"])
        self.assertEqual([{"value": "alpha", "count": 2}], third["groups"])
        self.assertEqual(result["columns"], first["columns"])

        literal = self.store.page(
            query_id, 0, page_size=10,
            grid={"filters": [{"column": 2, "operator": "contains", "value": "%"}]},
        )
        self.assertEqual([[2, 2, "draft %", "alpha"], [3, 3, "draft %", "beta"]], literal["rows"])
        self.assertEqual(2, literal["row_count"])
        self.assertNotIn("groups", literal)

        with self.assertRaisesRegex(ValueError, "out of range"):
            self.store.page(query_id, 0, grid={"sort": [{"column": 4, "direction": "asc"}]})
        for invalid in (
            {"unknown": []},
            {"group_by": None},
            {"filters": [{"column": 2, "operator": "like", "value": "%"}]},
        ):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                self.store.page(query_id, 0, grid=invalid)
        self.assertEqual(result["rows"], self.store.page(query_id, 0, page_size=100)["rows"])

    def test_cte_preview_and_unpinned_result_ttl_are_native(self) -> None:
        preview = self.store.run(
            "WITH values_cte AS (SELECT range AS value FROM range(5)) "
            "SELECT value AS rowid FROM values_cte ORDER BY value DESC",
            preview=2,
        )
        self.assertEqual([[4], [3]], preview["rows"])
        self.assertEqual(
            [[3], [4]],
            self.store.page(
                preview["query_id"], 0,
                grid={"sort": [{"column": 0, "direction": "asc"}]},
            )["rows"],
        )

        ttl_store = QueryStore(extension_directory=extension_directory(APP_ROOT.parents[2]), result_ttl_seconds=1)
        try:
            unpinned = ttl_store.run("SELECT 1", include_rows=False)["query_id"]
            pinned = ttl_store.run("SELECT 2", include_rows=False)["query_id"]
            ttl_store.pin(pinned)
            time.sleep(1.05)
            self.assertIsNone(ttl_store.prune_results())
            with self.assertRaisesRegex(ValueError, "unknown query_id"):
                ttl_store.page(unpinned, 0)
            self.assertEqual([[2]], ttl_store.page(pinned, 0)["rows"])
            ttl_store.unpin(pinned)
            ttl_store.prune_results()
            with self.assertRaisesRegex(ValueError, "unknown query_id"):
                ttl_store.page(pinned, 0)
            with self.assertRaisesRegex(ValueError, "unknown query_id"):
                ttl_store.pin("missing")
            with self.assertRaisesRegex(ValueError, "unknown query_id"):
                ttl_store.unpin("missing")
        finally:
            ttl_store.close()


if __name__ == "__main__":
    unittest.main()
