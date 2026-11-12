"""Batch refresh grouping is limited to independent, flat targets."""
from contextlib import contextmanager
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE import backend  # noqa: E402
from project_selection import ProjectSelection  # noqa: E402


def pin(ref, *, role='Requirement', version=1, container=None, relations=None, status='Active'):
    identity = ref.split('@')[0]
    return SimpleNamespace(atom_id=identity, version=version, status=status,
                           path=Path('/no-such-project') / (identity + '.md'),
                           metadata={'role': role, 'container': container or {'scope_unit': 'TEST'},
                                     'relations': relations or {}})


class GroupingTests(unittest.TestCase):
    def setUp(self):
        self.selection = object.__new__(ProjectSelection)
        object.__setattr__(self.selection, 'settings', {'artifacts': {'identity': {'project_prefix': 'CA'}}})
        self.events = []
        @contextmanager
        def group():
            self.events.append('enter')
            try:
                yield
            finally:
                self.events.append('exit')
        self.reader = SimpleNamespace(group_lifecycle_refresh=group, lifecycle_candidates=Mock(return_value=[]))
        self.model = object()

    def test_flat_archive_group_and_failure_flush(self):
        targets = [{'target': {'ref_id': f'CA-R-{i}', 'version': 1}} for i in (1, 2)]
        pins = {e['target']['ref_id']: pin(e['target']['ref_id']) for e in targets}
        action = Mock(side_effect=[{'outcome': 'completed', 'effects': [], 'warnings': [], 'errors': []},
                                   {'outcome': 'failed', 'effects': [], 'warnings': [], 'errors': [{'code': 'failed'}]}])
        with patch.object(backend, 'query_reader', return_value=self.reader), \
                patch.object(backend, 'select_sources', return_value=pins):
            result = backend._batch(self.selection, self.model, 'atom_lifecycle_archive', {'targets': targets}, action)
        self.assertEqual(['enter', 'exit'], self.events)
        self.assertEqual('failed', result['errors'][0]['code'])

    def test_publication_failure_keeps_effects_and_target_results(self):
        targets = [{'target': {'ref_id': 'CA-R-1', 'version': 1}}]
        @contextmanager
        def failed_publication():
            publication = {}
            yield publication
            publication['error'] = 'Projection refresh failed.'
        self.reader.group_lifecycle_refresh = failed_publication
        action = Mock(return_value={'outcome': 'completed', 'effects': ['written'], 'warnings': [], 'errors': []})
        with patch.object(backend, 'query_reader', return_value=self.reader), \
                patch.object(backend, 'select_sources', return_value={'CA-R-1': pin('CA-R-1')}):
            outcome = backend._batch(self.selection, self.model, 'atom_lifecycle_archive', {'targets': targets}, action)
        self.assertEqual('failed', outcome['outcome'])
        self.assertEqual('projection_refresh_failed', outcome['errors'][0]['code'])
        self.assertEqual(['written'], outcome['effects'])
        self.assertEqual(1, len(outcome['target_results']))
        self.assertEqual([], outcome['remaining_targets'])

    def test_nonflat_and_duplicate_fall_back(self):
        targets = [{'target': {'ref_id': f'CA-R-{i}', 'version': 1}} for i in (1, 2)]
        for first in (pin('CA-R-1', role='Plan'), pin('CA-R-1', container={'atom': 'CA-P-1'})):
            pins = {'CA-R-1': first, 'CA-R-2': pin('CA-R-2')}
            with patch.object(backend, 'query_reader', return_value=self.reader), \
                    patch.object(backend, 'select_sources', return_value=pins):
                with backend._batch_refresh(self.selection, self.model, 'atom_lifecycle_archive', targets):
                    pass
        self.assertEqual([], self.events)
        self.assertIsNone(backend._flat_targets(self.selection, self.model, [targets[0], targets[0]]))

    def test_promotion_requires_archived_predecessor_no_current_or_replacements(self):
        targets = [{'target': {'ref_id': 'CA-R-1@2-draft', 'version': 2}, 'targetStatus': 'Active'}]
        draft = pin('CA-R-1@2-draft', version=2, status='Draft')
        previous = pin('CA-R-1@1', status='Archived')
        with patch.object(backend, 'query_reader', return_value=self.reader), \
                patch.object(backend, 'select_sources', side_effect=[{'CA-R-1@2-draft': draft}, {'CA-R-1@1': previous}]):
            with backend._batch_refresh(self.selection, self.model, 'atom_lifecycle_promote_draft', targets):
                pass
        self.assertEqual(['enter', 'exit'], self.events)
        self.events.clear()
        self.reader.lifecycle_candidates.return_value = [('CA-R-1', '/current')]
        with patch.object(backend, 'query_reader', return_value=self.reader), \
                patch.object(backend, 'select_sources', return_value={'CA-R-1@2-draft': draft}):
            with backend._batch_refresh(self.selection, self.model, 'atom_lifecycle_promote_draft', targets):
                pass
        self.assertEqual([], self.events)


if __name__ == '__main__':
    unittest.main()
