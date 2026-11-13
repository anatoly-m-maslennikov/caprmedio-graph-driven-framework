import unittest
# CA-E-821@2
from pathlib import Path
import sys

import duckdb

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.audit_tables import create_tables, publish



class Tests(unittest.TestCase):
    def test_duplicate_revision_audit_tracks_cross_status_incremental_changes(self):
        db = duckdb.connect()
        db.execute('''CREATE TABLE atoms (relative_path VARCHAR, filename VARCHAR, status_group VARCHAR,
            reference VARCHAR, "header.identity.atom_id" VARCHAR, "header.state.version" VARCHAR)''')
        db.executemany('INSERT INTO atoms VALUES (?, ?, ?, ?, ?, ?)', [
            ('current', 'a.md', 'Current', 'CA-R-10', 'CA-R-10', '1'),
            ('draft', 'b.md', 'Draft', 'CA-R-10@1-draft', 'CA-R-10@1-draft', '1'),
            ('archive', 'c.md', 'Archived', 'CA-R-10@1', 'CA-R-10@1', '1'),
            ('archive', 'd.md', 'Archived', 'CA-R-10@2', 'CA-R-10', '2'),
            ('draft', 'e.md', 'Draft', 'CA-R-draft:e', 'CA-R-draft', '1'),
            ('draft', 'f.md', 'Draft', 'CA-R-draft:f', 'CA-R-draft', '1'),
            ('backlog', 'g.md', 'Backlog', 'CA-R-10', 'CA-R-10', '1'),
        ])
        create_tables(db)
        publish(db, {}, None, available=True)

        def issues():
            return db.execute("SELECT filename, observed, expected FROM atom_duplicate_revision_issues "
                              "WHERE issue_category = 'duplicate_atom_revision' ORDER BY filename").fetchall()

        assert issues() == [(name, 'CA-R-10', '1') for name in ('a.md', 'c.md')]
        db.execute("DELETE FROM atoms WHERE filename = 'b.md'")
        publish(db, {}, ['draft/b.md'], available=True)
        assert issues() == [(name, 'CA-R-10', '1') for name in ('a.md', 'c.md')]
        db.execute("UPDATE atoms SET \"header.state.version\" = '2' WHERE filename = 'c.md'")
        publish(db, {}, ['archive/c.md'], available=True)
        assert issues() == [(name, 'CA-R-10', '2') for name in ('c.md', 'd.md')]
        assert db.execute('SELECT count(*) FROM atoms').fetchone()[0] == 6
        db.execute("UPDATE atoms SET status_group = 'Draft' WHERE filename = 'c.md'")
        publish(db, {}, ['archive/c.md'], available=True)
        assert issues() == []


    def test_legacy_flat_headers_and_versioned_reference(self):
        db = duckdb.connect()
        db.execute('''CREATE TABLE atoms (relative_path VARCHAR, filename VARCHAR, status_group VARCHAR, reference VARCHAR,
            "header.atom_id" VARCHAR, "header.version" VARCHAR)''')
        db.executemany('INSERT INTO atoms VALUES (?, ?, ?, ?, ?, ?)', [
            ('a', 'a.md', 'Current', 'CA-M-12', 'CA-M-12', '3'),
            ('b', 'b.md', 'Archived', 'CA-M-12@3', None, None),
            ('c', 'c.md', 'Archived', 'CA-M-12@4', 'CA-M-12', '4'),
        ])
        create_tables(db)
        publish(db, {}, None, available=True)
        assert db.execute("SELECT filename FROM atom_duplicate_revision_issues "
                          "WHERE issue_category = 'duplicate_atom_revision' ORDER BY filename").fetchall() == [('a.md',), ('b.md',)]


    def test_padded_ids_are_distinct_and_audited_by_exact_spelling(self):
        db = duckdb.connect()
        db.execute('CREATE TABLE atoms (relative_path VARCHAR, filename VARCHAR, status_group VARCHAR, reference VARCHAR)')
        db.executemany('INSERT INTO atoms VALUES (?, ?, ?, ?)', [
            ('a', 'a.md', 'Current', 'CA-M-096@24'),
            ('b', 'b.md', 'Archived', 'CA-M-096@24'),
            ('c', 'c.md', 'Current', 'CA-M-96@24'),
            ('d', 'd.md', 'Current', 'CA-M-000@24'),
            ('e', 'e.md', 'Archived', 'CA-M-000@24'),
        ])
        create_tables(db)
        publish(db, {}, None, available=True)
        assert db.execute("SELECT filename, observed FROM atom_duplicate_revision_issues ORDER BY filename").fetchall() == [
            ('a.md', 'CA-M-096'), ('b.md', 'CA-M-096'),
            ('d.md', 'CA-M-000'), ('e.md', 'CA-M-000'),
        ]
