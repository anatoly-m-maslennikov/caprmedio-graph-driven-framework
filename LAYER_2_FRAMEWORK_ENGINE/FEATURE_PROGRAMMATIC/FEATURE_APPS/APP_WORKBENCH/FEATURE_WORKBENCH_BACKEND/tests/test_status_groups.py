"""Model-declared status groups retain latest Atom identity."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tests"))

import test_source_reader as fixtures
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.content_schema import compile_content_schema
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relation_registry import RelationRegistry
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relations import _atom_facts
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_reader import SourceReader
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.workbench_schema_asset import (
    compile_schema, compile_status_groups, load_image_schema, schema_asset,
)


class StatusGroupTests(unittest.TestCase):
    def test_numbered_history_cold_scan_and_incremental_moves(self):
        fixture = fixtures.SourceReaderTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        current = fixture._write_atom('MAIN', '04_requirement', 'current.md', atom_id='CA-R-820', status='Active')
        history = fixture._write_atom('MAIN', '04_requirement', 'history.md', atom_id='CA-R-821', status='Active', parts=('099_archived',))
        draft = fixture._write_atom('MAIN', '04_requirement', 'drafted.md', atom_id='CA-R-822', status='Active', version=2, parts=('000_draft',))
        projection = fixture._write_atom('MAIN', '04_requirement', 'projection.md', atom_id='CA-R-823', status='Active', parts=('_projection',))
        done = fixture._write_atom('MAIN', '04_requirement', 'done.md', atom_id='CA-R-824', status='Active', parts=('020_done',))
        legacy = fixture._write_atom('MAIN', '04_requirement', 'legacy.md', atom_id='CA-R-825', status='Active', parts=('archive',))
        reader = SourceReader(fixture.root)
        rows, _ = reader.capture()
        by_id = {row['id']: row for row in rows}
        self.assertNotIn('CA-R-821', by_id)
        self.assertNotIn('CA-R-823', by_id)
        self.assertNotIn('CA-R-825', by_id)
        self.assertEqual('Current', by_id['CA-R-824']['status_group'])
        self.assertEqual(('Draft', 'CA-R-822@2-draft'), (by_id['CA-R-822']['status_group'], by_id['CA-R-822']['ref']))
        moved = history.parent.parent / history.name
        history.rename(moved)
        rows, _ = reader.capture([{'operation': 'move', 'old_path': history.relative_to(fixture.root).as_posix(), 'new_path': moved.relative_to(fixture.root).as_posix()}])
        self.assertIn('CA-R-821', {row['id'] for row in rows})
        target = history.parent / current.name
        current.rename(target)
        rows, _ = reader.capture([{'operation': 'move', 'old_path': current.relative_to(fixture.root).as_posix(), 'new_path': target.relative_to(fixture.root).as_posix()}])
        self.assertNotIn('CA-R-820', {row['id'] for row in rows})

    def test_formal_mapping_round_trips_and_keeps_latest_references(self):
        statements = [('Atom/(.Header.Context.Role := Plan)/(.Header.State.Status := Backlog)'
                       '.Header.State.Status >| Status Group == Backlog', None)]
        groups = compile_status_groups(statements)
        self.assertEqual((("Plan", "Backlog", "Backlog"),), groups)
        with tempfile.TemporaryDirectory() as directory:
            asset = Path(directory) / 'schema.json'
            asset.write_bytes(schema_asset([], compile_schema([], compile_content_schema([]), status_groups=groups)))
            self.assertEqual(3, json.loads(asset.read_bytes())['schema_version'])
            self.assertEqual(groups, load_image_schema(asset).status_groups)

        fixture = fixtures.SourceReaderTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        backlog = fixture._write_atom('MAIN', '03_plan', 'backlog.md', atom_id='CA-P-810', status='Backlog', form='Plan')
        active = fixture._write_atom('MAIN', '03_plan', 'active.md', atom_id='CA-P-811', status='Active', form='Plan')
        draft = fixture._write_atom('MAIN', '03_plan', 'draft.md', atom_id='CA-P-812', status='Draft', form='Plan', version=2)
        path_draft = fixture._write_atom('MAIN', '03_plan', 'path-draft.md', atom_id='CA-P-813', status='Backlog', form='Plan', version=2, parts=('draft',))
        archived = fixture._write_atom('MAIN', '03_plan', 'archived.md', atom_id='CA-P-814', status='Archived', form='Plan')
        for path in (backlog, active, draft, path_draft, archived):
            path.write_text(path.read_text().replace('role: "Requirement"', 'role: "Plan"'))
        reader = SourceReader(fixture.root, status_groups=groups)
        rows, _ = reader.capture()
        rows = {row['id']: row for row in rows}
        self.assertEqual(('Backlog', 'CA-P-810'), (rows['CA-P-810']['status_group'], rows['CA-P-810']['ref']))
        self.assertEqual(('Current', 'CA-P-811'), (rows['CA-P-811']['status_group'], rows['CA-P-811']['ref']))
        self.assertEqual(('Draft', 'CA-P-812@2-draft'), (rows['CA-P-812']['status_group'], rows['CA-P-812']['ref']))
        self.assertEqual(('Draft', 'CA-P-813@2-draft'), (rows['CA-P-813']['status_group'], rows['CA-P-813']['ref']))
        self.assertNotIn('CA-P-814', rows)
        rows['CA-P-810']['header_json']['relations'] = {'RELATES_TO': ['CA-P-811']}
        registry = RelationRegistry(frozenset({'RELATES_TO'}), {}, {}, frozenset())
        self.assertIn(('Atom', 'CA-P-810', 'RELATES_TO', 'Atom', 'CA-P-811'),
                      list(_atom_facts(rows['CA-P-810'], {}, registry)))
        backlog.write_text(backlog.read_text().replace('status: "Backlog"', 'status: "Active"'))
        changed, _ = reader.capture([{'operation': 'update', 'old_path': None, 'new_path': backlog.relative_to(fixture.root).as_posix()}])
        row = next(row for row in changed if row['id'] == 'CA-P-810')
        self.assertEqual(('Current', 'CA-P-810'), (row['status_group'], row['ref']))


if __name__ == '__main__':
    unittest.main()
