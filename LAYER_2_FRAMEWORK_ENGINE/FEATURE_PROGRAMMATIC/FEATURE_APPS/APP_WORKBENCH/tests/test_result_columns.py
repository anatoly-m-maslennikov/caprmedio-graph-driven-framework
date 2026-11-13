# CA-E-675@14
"""Whole-result column visibility does not discard SQL values or later pages."""

from pathlib import Path
import sys
import unittest

import duckdb

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.result_columns import result_columns  # noqa: E402


class ResultColumnsTest(unittest.TestCase):
    def setUp(self):
        self.connection = duckdb.connect()
        self.connection.execute("CREATE SCHEMA workbench_results")

    def tearDown(self):
        self.connection.close()

    def metadata(self, query):
        relation = self.connection.sql(query)
        columns = [{"name": name, "type": str(kind)}
                   for name, kind in zip(relation.columns, relation.types, strict=True)]
        self.connection.execute(f"CREATE TABLE workbench_results.result AS {query}")
        return result_columns(self.connection, '"result"', columns)

    def test_later_row_keeps_column_and_null_only_column_hides(self):
        columns, count = self.metadata(
            "SELECT NULL AS empty, CASE WHEN range = 100 THEN 'last' END AS later FROM range(101)"
        )
        self.assertEqual(101, count)
        self.assertEqual([False, True], [column["has_values"] for column in columns])
        self.assertEqual((None, "last"), self.connection.execute(
            "SELECT * FROM workbench_results.result ORDER BY rowid LIMIT 1 OFFSET 100"
        ).fetchone())

    def test_false_zero_remain_while_empty_strings_and_collections_hide(self):
        columns, count = self.metadata(
            "SELECT 0 AS same, NULL AS same, false AS flag, '' AS text, [] AS items, '{}'::JSON AS object"
        )
        self.assertEqual(1, count)
        self.assertEqual([True, False, True, False, False, False],
                         [column["has_values"] for column in columns])
        self.assertEqual(["same", "same"], [column["name"] for column in columns[:2]])

    def test_json_whitespace_nested_values_and_empty_maps(self):
        columns, count = self.metadata(
            "SELECT ' { } '::JSON AS object, ' [ ] '::JSON AS array, 'null'::JSON AS nil, "
            "'\"\"'::JSON AS text, MAP() AS mapping, '[null]'::JSON AS nested, "
            "'{\"value\":null}'::JSON AS keyed, 'false'::JSON AS flag, '0'::JSON AS zero, "
            "'[]' AS literal_text, [NULL] AS one_item"
        )
        self.assertEqual(1, count)
        self.assertEqual([False] * 5 + [True] * 6,
                         [column["has_values"] for column in columns])

    def test_zero_row_headers_stay_visible(self):
        columns, count = self.metadata("SELECT NULL AS empty, 1 AS value WHERE false")
        self.assertEqual(0, count)
        self.assertTrue(all(column["has_values"] for column in columns))
