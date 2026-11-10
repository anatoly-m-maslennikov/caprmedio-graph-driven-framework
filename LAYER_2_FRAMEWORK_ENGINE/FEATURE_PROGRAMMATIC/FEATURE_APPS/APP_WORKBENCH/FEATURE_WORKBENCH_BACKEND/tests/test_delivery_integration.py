"""Result delivery through the Workbench service and cached DuckDB result."""
import json
from pathlib import Path
import sys
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tests"))
from test_incremental_indexing import IncrementalIndexingTests


class ResultDeliveryTests(IncrementalIndexingTests):
    def test_full_file_and_page_and_check(self):
        result = self.service.run("select i from range(250) t(i)", page_size=10)
        self.assertNotIn("sql", result)
        self.assertNotIn("rows", result)
        data = json.loads((self.root / result["result_file"]["path"]).read_text())
        self.assertEqual(250, len(data["rows"]))
        page = self.service.page(result["query_id"], 100, page_size=10)
        data = json.loads((self.root / page["result_file"]["path"]).read_text())
        self.assertEqual([[i] for i in range(100, 110)], data["rows"])
        inline = self.service.page(result["query_id"], 0, page_size=2, result_delivery="inline")
        self.assertEqual([[0], [1]], inline["rows"])
        self.assertNotIn("sql", inline)
        self.assertNotIn("sql", self.service.check("select 1"))

    def test_export_failure_leaves_cached_result_available(self):
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.result_delivery.write_result_file", side_effect=OSError("disk unavailable")):
            result = self.service.run("select 42")
        self.assertEqual("partial", result["outcome"])
        self.assertNotIn("result_file", result)
        page = self.service.page(result["query_id"], 0, result_delivery="inline")
        self.assertEqual([[42]], page["rows"])


if __name__ == "__main__":
    import unittest
    unittest.main()
