# CA-E-677@28

from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
import sys
import unittest

import duckdb


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(APP_ROOT)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.public_rows import insert_public_rows  # noqa: E402


class PublicInsertTest(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = duckdb.connect()
        self.addCleanup(self.connection.close)

    def test_small_batch_insert_preserves_types_values_and_field_order(self) -> None:
        fields = ("row_id", "text_value", "payload", "day", "moment", "flag", "count", "ratio")
        self.connection.execute(
            "CREATE TABLE main.rows("
            "row_id BIGINT, text_value VARCHAR, payload JSON, day DATE, moment TIMESTAMP, "
            "flag BOOLEAN, count BIGINT, ratio DOUBLE)"
        )
        rows = [
            {
                "row_id": 1,
                "text_value": "first line\nsecond line 😀",
                "payload": {"z": [True, None], "a": "é"},
                "day": date(2026, 11, 11),
                "moment": datetime(2026, 11, 11, 12, 34, 56),
                "flag": True,
                "count": 42,
                "ratio": 1.25,
            },
            {
                "row_id": 2,
                "text_value": None,
                "payload": None,
                "day": None,
                "moment": None,
                "flag": False,
                "count": -7,
                "ratio": None,
            },
        ]

        insert_public_rows(self.connection, "rows", fields, rows, json_fields=frozenset({"payload"}))

        self.assertEqual(fields, tuple(column[0] for column in self.connection.execute("SELECT * FROM rows").description))
        self.assertEqual(
            [
                (1, "first line\nsecond line 😀", '{"a":"é","z":[true,null]}',
                 date(2026, 11, 11), datetime(2026, 11, 11, 12, 34, 56), True, 42, 1.25),
                (2, None, None, None, None, False, -7, None),
            ],
            self.connection.execute("SELECT * FROM rows ORDER BY row_id").fetchall(),
        )

    def test_empty_batch_is_a_no_op(self) -> None:
        self.connection.execute("CREATE TABLE main.rows(value VARCHAR)")

        insert_public_rows(self.connection, "rows", ("value",), [], json_fields=frozenset())
        self.assertEqual([(0,)], self.connection.execute("SELECT count(*) FROM rows").fetchall())

    def test_single_row_matches_bulk_values_and_field_order(self) -> None:
        fields = ("row_id", "text_value", "payload", "day", "moment", "flag", "count", "ratio")
        ddl = (
            "(row_id BIGINT, text_value VARCHAR, payload JSON, day DATE, moment TIMESTAMP, "
            "flag BOOLEAN, count BIGINT, ratio DOUBLE)"
        )
        self.connection.execute(f"CREATE TABLE main.single_rows{ddl}")
        self.connection.execute(f"CREATE TABLE main.bulk_rows{ddl}")
        rows = [
            {
                "row_id": 1,
                "text_value": "first line\nsecond line 😀",
                "payload": {"z": [True, None], "a": "é"},
                "day": date(2026, 11, 11),
                "moment": datetime(2026, 11, 11, 12, 34, 56),
                "flag": True,
                "count": 42,
                "ratio": 1.25,
            },
            {
                "row_id": 2,
                "text_value": None,
                "payload": None,
                "day": None,
                "moment": None,
                "flag": False,
                "count": -7,
                "ratio": None,
            },
        ]

        insert_public_rows(
            self.connection, "single_rows", fields, rows[:1], json_fields=frozenset({"payload"}),
        )
        insert_public_rows(
            self.connection, "bulk_rows", fields,
            rows + [{**rows[1], "row_id": row_id} for row_id in (3, 4, 5, 6, 7, 8, 9)],
            json_fields=frozenset({"payload"}),
        )

        self.assertEqual(
            fields,
            tuple(column[0] for column in self.connection.execute("SELECT * FROM single_rows").description),
        )
        self.assertEqual(
            self.connection.execute("SELECT * FROM single_rows").fetchall(),
            self.connection.execute("SELECT * FROM bulk_rows ORDER BY row_id LIMIT 1").fetchall(),
        )

    def test_constraint_failure_is_rolled_back_by_caller(self) -> None:
        fields = ("row_id", "value")
        self.connection.execute("CREATE TABLE main.rows(row_id BIGINT PRIMARY KEY, value VARCHAR)")
        insert_public_rows(
            self.connection, "rows", fields, [{"row_id": 1, "value": "before"}],
            json_fields=frozenset(),
        )

        for count in (2, 9):
            with self.subTest(rows=count):
                self.connection.execute("BEGIN TRANSACTION")
                with self.assertRaises(duckdb.ConstraintException):
                    insert_public_rows(
                        self.connection, "rows", fields,
                        [{"row_id": row_id, "value": "new"} for row_id in range(2, count + 1)]
                        + [{"row_id": 1, "value": "duplicate"}],
                        json_fields=frozenset(),
                    )
                self.connection.execute("ROLLBACK")
                self.assertEqual([(1, "before")], self.connection.execute("SELECT * FROM rows").fetchall())


if __name__ == "__main__":
    unittest.main()
