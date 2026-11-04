"""Subject patch selection preserves the actual carrier keys."""
from __future__ import annotations

import hashlib
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOOLS))
import atom_operations as operations  # noqa: E402
import atom_subject_patch as subject_patch  # noqa: E402


class SubjectAliasPatchTests(unittest.TestCase):
    def plan(self, subject_text, patches):
        text = ('---\natom_id: CA-R-1\nversion: 1\nupdated_at: "2026-01-01 00:00:00 +0000"\n'
                'subjects:\n' + subject_text + '---\n## Claim\n\nBody\n')
        raw = text.encode()
        path = Path('/tmp/CA-R-1.md')
        snapshot = subject_patch._SourceSnapshot(path, 'CA-R-1.md', raw, (0, 0, 0, 0, 0))
        item = {'selector': 'CA-R-1.md', 'expected': {'atom_id': 'CA-R-1', 'version': 1,
                'sha256': hashlib.sha256(raw).hexdigest()}, 'subject_patches': patches}
        with patch.object(subject_patch, '_safe_source_path', return_value=path), \
             patch.object(subject_patch, '_read_source_snapshot', return_value=snapshot), \
             patch.object(subject_patch, '_snapshot_identity', return_value=('CA-R-1', 1)), \
             patch.object(subject_patch, '_validate_subject_values'):
            result = subject_patch._plan_item(operations, Path('/tmp'), item, 0, set(), set(), 'legacy',
                                               validate_source_complete=False)
        return subject_patch._apply_replacements(result['frontmatter'], result['subject_replacements'])

    def test_current_and_historical_keys_are_preserved(self):
        changes = [{'field': 'governs', 'old': 'Atom', 'new': 'Node'},
                   {'field': 'depends_on', 'operation': 'replace_set', 'old': ['One'], 'new': ['Two']}]
        for text, expected in (('  active: Atom\n  passive: [One]\n', ('active:', 'passive:')),
                               ('  governs: Atom\n  depends_on: [One]\n', ('governs:', 'depends_on:'))):
            with self.subTest(text=text):
                result = self.plan(text, changes)
                self.assertIn(expected[0] + ' "Node"', result)
                self.assertIn(expected[1] + ' ["Two"]', result)
                self.assertNotIn('governs:' if expected[0] == 'active:' else 'active:', result)

    def test_equal_aliases_remain_equal_when_patched(self):
        result = self.plan('  active: Atom\n  governs: Atom\n  passive: [One]\n  depends_on: [One]\n', [
            {'field': 'governs', 'old': 'Atom', 'new': 'Node'},
            {'field': 'depends_on', 'old': 'One', 'new': 'Two'}])
        self.assertIn('active: "Node"', result)
        self.assertIn('governs: "Node"', result)
        self.assertIn('passive: ["Two"]', result)
        self.assertIn('depends_on: ["Two"]', result)

    def test_equal_dependency_aliases_remain_equal_after_set_replacement(self):
        result = self.plan('  active: Atom\n  passive: [One]\n  depends_on: [One]\n', [
            {'field': 'depends_on', 'operation': 'replace_set', 'old': ['One'], 'new': ['Two', 'Three']}])
        self.assertIn('passive: ["Two", "Three"]', result)
        self.assertIn('depends_on: ["Two", "Three"]', result)

    def test_conflicting_aliases_refuse(self):
        for text in ('  active: Atom\n  governs: Other\n',
                     '  active: Atom\n  passive: [One]\n  depends_on: [Two]\n'):
            with self.subTest(text=text), self.assertRaises(operations.ToolError):
                self.plan(text, [])

    def test_duplicate_passive_values_still_refuse(self):
        with self.assertRaises(operations.ToolError) as caught:
            self.plan('  active: Atom\n  passive: [One, One]\n', [])
        self.assertEqual('subject-dependency-duplicate', caught.exception.code)


if __name__ == '__main__':
    unittest.main()
