"""Replacement resolution reads only the selected indexed Archive carrier."""
import sys
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from ATOM_LIFECYCLE import publish, source  # noqa: E402
from ATOM_LIFECYCLE.common import InputError  # noqa: E402
import test_lifecycle_source as fixtures  # noqa: E402


class IndexedReader:
    def __init__(self, current=(), archived=(), error=None):
        self.current = current
        self.archived = archived
        self.error = error
        self.reads = []
        self.archive_calls = 0

    def lifecycle_candidates(self, selection, *, atom_ids=(), prefix=None, under=None, references=()):
        return [('CA-R-10', path) for path in self.current]

    def lifecycle_archive_candidates(self, selection, atom_id):
        self.archive_calls += 1
        if self.error:
            raise self.error
        return self.archived

    def lifecycle_read(self, path):
        self.reads.append(path)
        return path.read_bytes()


class ReplacementIndexTest(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.SourceTest()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.selection = self.fixture.selection

    def carrier(self, name, **kwargs):
        return self.fixture.carrier(name, **kwargs)

    def resolve(self, reader):
        with source.bind_query_reader(reader):
            return publish.resolve_replacement(self.selection, 'CA-R-10')

    def test_newest_archive_requires_one_read(self):
        versions = [(f'CA-R-10@{version}', self.carrier(
            f'CA-R-10@{version}-example.md', version=version, status='Archived'))
            for version in range(12, 0, -1)]
        reader = IndexedReader(archived=versions)
        result = self.resolve(reader)
        self.assertEqual((result.version, result.path), (12, versions[0][1]))
        self.assertEqual(reader.reads, [versions[0][1]])

    def test_retained_archive_accepts_versioned_header_identity(self):
        archive = self.carrier('CA-R-10@22-example.md', version=22, status='Archived')
        archive.write_text(archive.read_text().replace('atom_id: CA-R-10', 'atom_id: CA-R-10@22')
                           .replace('version: 22', 'ref_id: CA-R-10@22\nversion: 22'))
        reader = IndexedReader(archived=[('CA-R-10@22', archive)])
        before = archive.read_bytes()
        result = self.resolve(reader)
        self.assertEqual((result.atom_id, result.ref_id, result.version), ('CA-R-10', 'CA-R-10@22', 22))
        self.assertEqual(reader.reads, [archive])
        self.assertEqual(archive.read_bytes(), before)
        reader.current = [archive]
        with source.bind_query_reader(reader):
            self.assertEqual(source.select_source(self.selection, 'CA-R-10@22').path, archive)
            self.assertEqual(source.select_sources(self.selection, ['CA-R-10@22'])['CA-R-10@22'].path, archive)

    def test_retained_archive_rejects_wrong_versioned_header(self):
        archive = self.carrier('CA-R-10@22-example.md', version=22, status='Archived')
        archive.write_text(archive.read_text().replace('atom_id: CA-R-10', 'atom_id: CA-R-10@21')
                           .replace('version: 22', 'ref_id: CA-R-10@21\nversion: 22'))
        reader = IndexedReader(archived=[('CA-R-10@22', archive)])
        with self.assertRaisesRegex(InputError, 'Archived replacement is stale or invalid'):
            self.resolve(reader)
        self.assertEqual(reader.reads, [archive])

    def test_unbound_retained_archive_accepts_versioned_header_identity(self):
        archive = self.carrier('CA-R-10@22-example.md', version=22, status='Archived')
        archive.write_text(archive.read_text().replace('atom_id: CA-R-10', 'atom_id: CA-R-10@22')
                           .replace('version: 22', 'ref_id: CA-R-10@22\nversion: 22'))
        result = publish.resolve_replacement(self.selection, 'CA-R-10')
        self.assertEqual((result.atom_id, result.ref_id, result.version), ('CA-R-10', 'CA-R-10@22', 22))

    def test_current_takes_priority_over_archive(self):
        current = self.carrier('CA-R-10-current.md', version=13)
        reader = IndexedReader(current=[current], error=AssertionError('Archive must not be queried'))
        self.assertEqual(self.resolve(reader).path, current)
        self.assertEqual(reader.reads, [current])
        self.assertEqual(reader.archive_calls, 0)

    def test_stale_current_does_not_fall_back_to_archive(self):
        stale = self.carrier('CA-R-10-current.md', identity='CA-R-11')
        archive = self.carrier('CA-R-10@5-example.md', version=5, status='Archived')
        reader = IndexedReader(current=[stale], archived=[('CA-R-10@5', archive)])
        with self.assertRaisesRegex(InputError, 'Current replacement is stale or invalid'):
            self.resolve(reader)
        self.assertEqual(reader.reads, [stale])
        self.assertEqual(reader.archive_calls, 0)

    def test_current_duplicates_fail_without_reads_and_block_collision(self):
        invalid = self.carrier('CA-R-10-a.md', identity='CA-R-11')
        valid = self.carrier('CA-R-10-b.md')
        reader = IndexedReader(current=[invalid, valid])
        with self.assertRaisesRegex(InputError, 'Current replacement is stale or invalid'):
            self.resolve(reader)
        with source.bind_query_reader(reader):
            self.assertTrue(publish._current_collision(self.selection, 'CA-R-10'))
        self.assertEqual(reader.reads, [])

    def test_stale_latest_does_not_fall_back_to_older(self):
        stale = self.carrier('CA-R-10@5-first.md', identity='CA-R-11', version=5, status='Archived')
        older = self.carrier('CA-R-10@4-older.md', version=4, status='Archived')
        reader = IndexedReader(archived=[('CA-R-10@5', stale), ('CA-R-10@4', older)])
        with self.assertRaisesRegex(InputError, 'Archived replacement is stale or invalid'):
            self.resolve(reader)
        self.assertEqual(reader.reads, [stale])

    def test_latest_archive_duplicates_fail_without_reads(self):
        first = self.carrier('CA-R-10@5-first.md', version=5, status='Archived')
        second = self.carrier('CA-R-10@5-second.md', version=5, status='Archived')
        older = self.carrier('CA-R-10@4-older.md', version=4, status='Archived')
        reader = IndexedReader(archived=[('CA-R-10@4', older), ('CA-R-10@5', first), ('CA-R-10@5', second)])
        with self.assertRaisesRegex(InputError, 'Archived replacement is stale or invalid'):
            self.resolve(reader)
        self.assertEqual(reader.reads, [])

    def test_draft_is_never_selected(self):
        draft = self.carrier('CA-R-10@6-draft-example.md', version=6, status='Draft')
        archive = self.carrier('CA-R-10@5-example.md', version=5, status='Archived')
        reader = IndexedReader(archived=[('CA-R-10@6-draft', draft), ('CA-R-10@5', archive)])
        self.assertEqual(self.resolve(reader).path, archive)
        self.assertEqual(reader.reads, [archive])

    def test_archive_boundary_and_unloaded_errors(self):
        reader = IndexedReader(archived=[('CA-R-10@2', Path('/outside/CA-R-10@2-example.md'))])
        with self.assertRaises(InputError):
            self.resolve(reader)
        self.assertEqual(reader.reads, [])
        reader = IndexedReader(error=source.ArchiveNotLoadedError('not loaded'))
        with self.assertRaises(source.ArchiveNotLoadedError):
            self.resolve(reader)


if __name__ == '__main__':
    unittest.main()
