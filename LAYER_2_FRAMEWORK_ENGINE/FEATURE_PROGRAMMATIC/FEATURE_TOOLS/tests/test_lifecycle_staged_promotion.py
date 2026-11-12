"""Staged exact predecessors do not require loading unrelated Archive history."""
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOLS), str(TOOLS / 'tests')]
from ATOM_LIFECYCLE import effects, publish, source  # noqa: E402
from test_lifecycle_publish import DRAFT, ROOT, pin  # noqa: E402
from lifecycle_placement_test_support import bind_placement, fixture_rules  # noqa: E402


class StagedPromotionTests(unittest.TestCase):
    def test_exact_archived_same_id_and_explicit_replacement(self):
        for same_id in (True, False):
            with self.subTest(same_id=same_id):
                raw = DRAFT.replace(b'is_replacement_for: [CA-R-1, CA-R-1, CA-R-2]',
                                    b'is_replacement_for: []' if same_id else b'is_replacement_for: [CA-R-1]')
                if same_id:
                    raw = raw.replace(b'CA-R-9@1-draft', b'CA-R-9@2-draft').replace(b'version: 1', b'version: 2')
                draft = pin('CA-R-9', raw=raw, status='Draft', version=2 if same_id else 1,
                            ref='CA-R-9@2-draft' if same_id else 'CA-R-9@1-draft')
                predecessor_id = 'CA-R-9' if same_id else 'CA-R-1'
                predecessor = pin(predecessor_id, raw=raw, status='Archived', version=1, ref=f'{predecessor_id}@1')
                pins = {draft.ref_id: draft, predecessor.ref_id: predecessor}
                selection = SimpleNamespace(root=ROOT)
                model = SimpleNamespace(allowed=lambda role, form: {'Draft', 'Active', 'Archived'})
                with (bind_placement(fixture_rules()),
                      patch.object(publish, 'read_target', return_value=draft),
                      patch.object(publish, 'resolve_replacement', side_effect=source.ArchiveNotLoadedError('older unloaded')) as wide,
                      patch.object(publish, '_current_collision', return_value=False),
                      patch.object(publish, '_destination', return_value=ROOT / 'current.md'),
                      patch.object(publish, 'validate_candidate'),
                      patch.object(publish.source, 'select_source', side_effect=lambda _s, ref, **kw: pins[ref]),
                      patch.object(publish.source, 'select_sources', side_effect=lambda _s, refs: {r: pins[r] for r in refs}),
                      patch.object(publish, 'write_destination', return_value=effects.Result(effects=[{'operation': 'create'}])),
                      patch.object(publish.effects, 'remove', return_value=effects.Result(effects=[{'operation': 'remove'}]))):
                    result = publish._promote_draft(selection, model,
                        {'target': {'ref_id': draft.ref_id, 'version': draft.version}, 'targetStatus': 'Active'},
                        staged={predecessor_id: predecessor}, expected_draft=draft)
                self.assertEqual('completed', result['outcome'], result)
                wide.assert_not_called()

    def test_pinned_archive_rejects_current_conflict_and_digest_change(self):
        predecessor = pin('CA-R-1', status='Archived', version=1, ref='CA-R-1@1')
        with patch.object(publish, '_current_collision', return_value=True):
            with self.assertRaises(publish.SourceChanged):
                publish._promotion_predecessor(object(), 'CA-R-1', {'CA-R-1': predecessor})
        changed = source.SourcePin(predecessor.path, predecessor.atom_id, predecessor.ref_id,
                                   predecessor.version, predecessor.status, 'changed', predecessor.raw, predecessor.metadata)
        with patch.object(publish, '_current_collision', return_value=False), \
                patch.object(source, 'select_source', return_value=changed):
            with self.assertRaises(publish.SourceChanged):
                publish._promotion_predecessor(object(), 'CA-R-1', {'CA-R-1': predecessor})

    def test_unstaged_still_reports_unloaded_archive(self):
        with patch.object(publish, 'resolve_replacement', side_effect=source.ArchiveNotLoadedError('unloaded')):
            with self.assertRaises(source.ArchiveNotLoadedError):
                publish._promotion_predecessor(object(), 'CA-R-1', None)


if __name__ == '__main__':
    unittest.main()
