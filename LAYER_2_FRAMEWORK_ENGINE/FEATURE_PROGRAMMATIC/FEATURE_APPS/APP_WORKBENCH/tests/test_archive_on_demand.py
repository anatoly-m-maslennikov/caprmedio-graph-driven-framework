from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent))
from test_source_reader import SourceReaderTests
from smalltest_support import write_atom
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_reader import SourceReader


class ArchiveOnDemandTest(unittest.TestCase):
    def setUp(self):
        fixture = SourceReaderTests('runTest')
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        self.root, self.control = fixture.root, fixture.control
        self.folder = self.control / '04_requirement' / 'archived'
        self.one = write_atom(self.folder / 'CA-R-100@1-RULE--first.md', 'CA-R-100', status='Archived')
        self.two = write_atom(self.folder / 'CA-R-100@2-RULE--second.md', 'CA-R-100', status='Archived', version=2)
        self.reader = SourceReader(self.root, include_archived=False)

    def relative(self, path):
        return path.relative_to(self.root).as_posix()

    def test_catalog_load_file_then_folder_and_rebuild(self):
        original = self.reader._read_source
        read = []
        def recording(path, *args, **kwargs):
            read.append(path)
            return original(path, *args, **kwargs)
        with patch.object(self.reader, '_read_source', recording):
            rows, _ = self.reader.capture()
        self.assertNotIn(self.one, read)
        self.assertNotIn(self.two, read)
        self.assertEqual(set(self.reader.archive_catalog()), {self.relative(self.one), self.relative(self.two)})
        self.assertEqual({(r[0], r[1]) for r in self.reader.archive_reservations('CA-R-100')}, {('CA-R-100', 1), ('CA-R-100', 2)})
        self.assertGreaterEqual(self.reader.max_atom_number('R'), 100)
        rows, _ = self.reader.capture(self.reader.load_archive_file(self.relative(self.one)))
        self.assertEqual([r['ref'] for r in rows if r['status_group'] == 'Archived'], ['CA-R-100@1'])
        third = write_atom(self.folder / 'CA-R-100-RULE--third@9.md', 'CA-R-100', status='Archived', version=9)
        rows, _ = self.reader.capture(self.reader.load_archive_folder(self.relative(self.folder)))
        self.assertIn(('CA-R-100', 9, self.relative(third)), self.reader.archive_reservations('CA-R-100'))
        self.assertEqual(self.reader.archive_reservations('CA-R-100', unloaded_only=True), ())
        self.assertEqual({r['ref'] for r in rows if r['status_group'] == 'Archived'}, {'CA-R-100@1', 'CA-R-100@2', 'CA-R-100@9'})
        self.assertEqual(self.reader.load_archive_folder(self.relative(self.folder)), [])
        fourth = write_atom(self.folder / 'CA-R-101@1.md', 'CA-R-101', status='Archived')
        rows, _ = self.reader.capture(self.reader.load_archive_folder(self.relative(self.folder)))
        self.assertIn('CA-R-101@1', {r['ref'] for r in rows})
        fourth.unlink()
        self.reader.capture([{'operation': 'remove', 'old_path': self.relative(fourth)}])
        self.reader.release_cache()
        rows, _ = self.reader.capture()
        self.assertEqual({r['ref'] for r in rows if r['status_group'] == 'Archived'}, {'CA-R-100@1', 'CA-R-100@2', 'CA-R-100@9'})

    def test_projection_is_not_hidden_and_unload_takes_effect_on_reread(self):
        projection = write_atom(self.control / '04_requirement' / '_projection' / 'CA-R-101.md', 'CA-R-101')
        rows, _ = self.reader.capture()
        self.assertIn('CA-R-101', {r['ref'] for r in rows})
        self.assertNotIn(self.relative(projection), self.reader.archive_catalog())
        self.reader.capture(self.reader.load_archive_folder(self.relative(self.folder)))
        self.reader.unload_archive_folder(self.relative(self.folder))
        self.reader.release_cache()
        rows, _ = self.reader.capture()
        self.assertFalse(any(r['status_group'] == 'Archived' for r in rows))

    def test_bulk_load_invalid_folder_leaves_all_unregistered(self):
        self.reader.capture()
        invalid = self.control / '04_requirement' / 'not_a_folder'
        invalid.write_text('x')
        with self.assertRaises(ValueError):
            self.reader.load_archive_folders([self.relative(self.folder), self.relative(invalid)])
        self.assertNotIn(self.folder, self.reader._loaded_archive_folders)
        rows, _ = self.reader.capture([{'operation': 'update', 'new_path': self.relative(self.one)}])
        self.assertNotIn('CA-R-100@1', {row['ref'] for row in rows})

    def test_missing_loaded_folder_and_later_watcher_create(self):
        self.reader.capture()
        folder = self.control / '04_requirement' / 'not_created_yet'
        self.assertEqual(self.reader.load_archive_folder(self.relative(folder)), [])
        created = write_atom(folder / 'CA-R-601@1.md', 'CA-R-601', status='Archived')
        rows, _ = self.reader.capture([{'operation': 'create', 'new_path': self.relative(created)}])
        self.assertIn('CA-R-601@1', {row['ref'] for row in rows})
        regular_file = self.control / '04_requirement' / 'not_a_folder'
        regular_file.write_text('x')
        with self.assertRaises(ValueError):
            self.reader.load_archive_folder(self.relative(regular_file))

    def test_declared_custom_alias_is_skipped_on_cold_start(self):
        class Placement:
            role_folders = {'requirement': '04_requirement'}
            def role_folder(self, role):
                return self.role_folders[role]
            def archive_folders(self, role):
                return ('archived', 'historic_versions')
        alias = self.control / '04_requirement' / 'historic_versions'
        atom = write_atom(alias / 'CA-R-602@1.md', 'CA-R-602', status='Active')
        reader = SourceReader(self.root, include_archived=False, archive_placement=Placement())
        with patch.object(reader, '_read_source', wraps=reader._read_source) as read:
            rows, _ = reader.capture()
        self.assertFalse(any(call.args[0] == atom for call in read.call_args_list))
        self.assertNotIn('CA-R-602', {row['ref'] for row in rows})
        self.assertIn(self.relative(atom), reader.archive_catalog())
        rows, _ = reader.capture(reader.load_archive_folder(self.relative(alias)))
        self.assertIn('CA-R-602@1', {row['ref'] for row in rows})

    def test_explicit_custom_archive_alias(self):
        self.reader.capture()
        alias = self.control / '04_requirement' / 'history_vault'
        atom = write_atom(alias / 'CA-R-555@1.md', 'CA-R-555', status='Active')
        rows, _ = self.reader.capture(self.reader.load_archive_folder(self.relative(alias)))
        self.assertEqual([r['status_group'] for r in rows if r['source_path'] == self.relative(atom)], ['Archived'])

    def test_padded_archive_id_reservation_and_removal(self):
        padded = write_atom(self.folder / 'CA-R-000096@24.md', 'CA-R-000096', status='Archived', version=24)
        zero = write_atom(self.folder / 'CA-R-000000@1.md', 'CA-R-000000', status='Archived')
        self.reader.capture()
        self.assertEqual(self.reader.archive_reservations('CA-R-000096'),
                         (('CA-R-000096', 24, self.relative(padded)),))
        self.assertEqual(self.reader.archive_reservations('CA-R-96'), ())
        self.assertEqual(self.reader.archive_reservations('CA-R-000000'),
                         (('CA-R-000000', 1, self.relative(zero)),))
        padded.unlink()
        self.reader.capture([{'operation': 'remove', 'old_path': self.relative(padded)}])
        self.assertEqual(self.reader.archive_reservations('CA-R-000096'), ())
        self.assertTrue(zero.exists())

    def test_watcher_catalog_skipped_files_and_header_archives(self):
        self.reader.capture()
        hidden = write_atom(self.control / '04_requirement' / 'CA-R-200.md', 'CA-R-200', status='Archived')
        rows, _ = self.reader.capture([{'operation': 'create', 'new_path': self.relative(hidden)}])
        self.assertIn(self.relative(hidden), self.reader.archive_catalog())
        self.assertNotIn('CA-R-200@1', {r['ref'] for r in rows})
        rows, _ = self.reader.capture(self.reader.load_archive_file(self.relative(hidden)))
        self.assertIn('CA-R-200@1', {r['ref'] for r in rows})
        new = write_atom(self.folder / 'CA-R-999999999@1-RULE--new.md', 'CA-R-999999999', status='Archived')
        rows, _ = self.reader.capture(self.reader.load_archive_file(self.relative(new)))
        self.assertIn('CA-R-999999999@1', {r['ref'] for r in rows})
        self.assertEqual(self.reader.max_atom_number('R'), 999999999)
        self.one.unlink()
        self.reader.capture([{'operation': 'remove', 'old_path': self.relative(self.one)}])
        self.assertNotIn(self.relative(self.one), self.reader.archive_catalog())


if __name__ == '__main__':
    unittest.main()
