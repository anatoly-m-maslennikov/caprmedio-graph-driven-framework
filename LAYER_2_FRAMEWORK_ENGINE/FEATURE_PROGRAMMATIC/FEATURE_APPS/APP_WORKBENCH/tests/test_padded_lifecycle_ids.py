import unittest
# CA-E-827@1
from pathlib import Path
import sys
import threading

import duckdb

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_store import QueryStore
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.header_columns import HeaderSchema



class Tests(unittest.TestCase):
    def test_padded_id_lookup_and_numeric_allocator(self):
        store = object.__new__(QueryStore)
        store._lock = threading.RLock()
        store._header_schema = HeaderSchema(())
        store._connection = duckdb.connect()
        store._connection.execute('CREATE TABLE atoms (reference VARCHAR, relative_path VARCHAR, filename VARCHAR)')
        store._connection.executemany('INSERT INTO atoms VALUES (?, ?, ?)', [
            ('CA-M-096@24', 'a', 'a.md'), ('CA-M-100', 'b', 'b.md'),
            ('CA-M-0000099', 'c', 'c.md'), ('CA-M-000', 'd', 'd.md'),
        ])
        assert store.lifecycle_candidates(atom_ids=('CA-M-096',)) == [('CA-M-096@24', 'a', 'a.md')]
        assert store.lifecycle_candidates(atom_ids=('CA-M-96',)) == []
        assert store.lifecycle_candidates(atom_ids=('CA-M-000',)) == [('CA-M-000', 'd', 'd.md')]
        assert store.lifecycle_last_id('CA-M-') == 'CA-M-100'

        long_id = 'CA-M-00' + '9' * 80
        store._connection.execute('INSERT INTO atoms VALUES (?, ?, ?)', [long_id, 'e', 'e.md'])
        assert store.lifecycle_candidates(atom_ids=(long_id,)) == [(long_id, 'e', 'e.md')]
        assert store.lifecycle_last_id('CA-M-') == long_id
        assert store.lifecycle_last_id('CA-M-', ceiling=100) == 'CA-M-100'
        assert store.lifecycle_last_id('CA-M-', ceiling=99) == 'CA-M-0000099'
