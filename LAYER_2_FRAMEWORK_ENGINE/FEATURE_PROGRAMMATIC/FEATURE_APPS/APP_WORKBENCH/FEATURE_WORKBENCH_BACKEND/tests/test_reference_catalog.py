"""The SQL carrier lookup keeps the standalone selection semantics."""
from pathlib import Path
import sys
import threading
import unittest

import duckdb

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.reference_catalog import ReferenceCatalog
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_rows import ReferenceIndex


class ReferenceCatalogTests(unittest.TestCase):
    def test_rebuild_and_incremental_selection_match_fallback(self):
        root = Path('/project')
        authority, projection, other, no_ref = (root / path for path in
            ('z/atom.md', '_projection/a.md', 'a/atom.md', 'none.md'))
        rows = {authority: {'ref': 'A'}, projection: {'ref': 'A'}, no_ref: {'ref': None}}
        connection = duckdb.connect(':memory:')
        sql = ReferenceCatalog(connection, threading.RLock(), root)
        fallback = ReferenceIndex()
        try:
            for index in (sql, fallback):
                index.rebuild(rows)
            self.assertEqual({authority, no_ref}, sql.accepted_paths())
            before = {authority: rows.pop(authority), other: None}
            rows[other] = {'ref': 'A'}
            self.assertEqual(fallback.update(before, rows.get, {authority, other}),
                             sql.update(before, rows.get, {authority, other}))
            self.assertEqual(fallback.accepted_paths(), sql.accepted_paths())
            self.assertEqual({other, projection}, sql.paths_for('A'))
            self.assertEqual({other}, sql.accepted_paths({other, projection}))
        finally:
            connection.close()


if __name__ == '__main__':
    unittest.main()
