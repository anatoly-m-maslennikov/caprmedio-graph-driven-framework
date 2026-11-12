"""Unloaded history is distinct from a missing Atom during lifecycle writes."""
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE import backend, draft, publish, source  # noqa: E402
from project_selection import ProjectSelection  # noqa: E402


class ArchiveNotLoadedTests(unittest.TestCase):
    def setUp(self):
        self.error = source.ArchiveNotLoadedError('Load the requested Archive first.')

    def test_draft_stops_before_draft_fallback(self):
        missing = source.SourceSelectionError('Current missing')
        with patch.object(draft, 'select_source', side_effect=[missing, self.error]) as select:
            with self.assertRaises(source.ArchiveNotLoadedError):
                draft._source(object(), {'ref_id': 'CA-R-1', 'version': 1})
        self.assertEqual(2, select.call_count)

    def test_version_allocation_propagates_unloaded_archive(self):
        reader = SimpleNamespace(lifecycle_latest_version=Mock(side_effect=self.error))
        with patch.object(draft, 'query_reader', return_value=reader):
            with self.assertRaises(source.ArchiveNotLoadedError):
                draft._next_version(object(), SimpleNamespace(atom_id='CA-R-1', version=1))

    def test_replacement_propagates_unloaded_archive(self):
        selection = object.__new__(ProjectSelection)
        object.__setattr__(selection, 'root', Path('/project'))
        object.__setattr__(selection, 'settings', {'artifacts': {'identity': {'project_prefix': 'CA'}}})
        with patch.object(source, 'query_reader', return_value=object()), \
                patch.object(source, '_candidate_paths', side_effect=self.error):
            with self.assertRaises(source.ArchiveNotLoadedError):
                publish.resolve_replacement(selection, 'CA-R-1')
        self.assertEqual('archive_not_loaded', publish._error(self.error)['code'])

    def test_batch_preserves_error_and_remaining_targets(self):
        selection = object.__new__(ProjectSelection)
        object.__setattr__(selection, 'settings', {'artifacts': {'identity': {'project_prefix': 'CA'}}})
        entries = [{'target': {'ref_id': f'CA-R-{number}', 'version': 1}} for number in (1, 2)]
        outcome = backend._batch(selection, object(), 'atom_lifecycle_archive', {'targets': entries},
                                 Mock(side_effect=self.error))
        self.assertEqual('archive_not_loaded', outcome['errors'][0]['code'])
        self.assertEqual(entries[1:], outcome['remaining_targets'])


if __name__ == '__main__':
    unittest.main()
