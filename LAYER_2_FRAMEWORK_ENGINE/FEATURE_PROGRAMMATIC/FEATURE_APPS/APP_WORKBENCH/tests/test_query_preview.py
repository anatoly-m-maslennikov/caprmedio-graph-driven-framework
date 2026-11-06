# CA-E-676@10
from __future__ import annotations

from pathlib import Path
import sys
import unittest


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(APP_ROOT), str(Path(__file__).parent)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_store import QueryStore  # noqa: E402
from smalltest_support import extension_directory  # noqa: E402


class QueryPreviewTests(unittest.TestCase):
    def setUp(self) -> None:
        self.store = QueryStore(extension_directory=extension_directory(APP_ROOT.parents[2]))

    def tearDown(self) -> None:
        self.store.close()

    def test_preview_caps_native_result_without_changing_public_sql(self) -> None:
        sql = "WITH values_cte AS (SELECT range AS value FROM range(5)) SELECT value FROM values_cte ORDER BY value DESC"

        result = self.store.run(sql, preview=2)

        self.assertEqual(sql, result["sql"])
        self.assertEqual([[4], [3]], result["rows"])
        self.assertEqual(2, result["row_count"])
        self.assertEqual(sql, self.store.page(result["query_id"], 0)["sql"])

    def test_omitted_preview_keeps_the_complete_result(self) -> None:
        result = self.store.run("SELECT range AS value FROM range(20)")

        self.assertEqual(20, result["row_count"])
        self.assertEqual(20, len(result["rows"]))

    def test_preview_preserves_existing_limit_and_validates_value(self) -> None:
        self.assertEqual(
            [[0], [1]],
            self.store.run("SELECT range AS value FROM range(10) LIMIT 2", preview=5)["rows"],
        )
        self.assertEqual([], self.store.run("SELECT 1", preview=0)["rows"])
        for value in (True, -1, 1.5, "1"):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "preview"):
                    self.store.run("SELECT 1", preview=value)
