import unittest
from claim import Ambiguous, migrate_claim


class ClaimTests(unittest.TestCase):
    def test_scope_and_undeclared_headings_preserved(self):
        source = '## Summary\n\nS\n\n## Claim scope\n\nScope.\n\n## Claim\n\nA\n\n## Other\n\nB\n\n### More\nC\n\n## Details\n\nD\n'
        result = migrate_claim(source)
        self.assertIn('### Prose Claim\n\n\nScope.\n\n\nA\n\n## Other\n\nB\n\n### More\nC\n', result)
        self.assertIn('## Details\n\nD\n', result)
        self.assertNotIn('## Claim scope', result)
        self.assertEqual(migrate_claim(result), result)

    def test_formal_only_and_fence_headings(self):
        source = '## Claim\n\n```CFEL\n## Claim\nAtom.ID\n```\n\n## Details\nD\n'
        result = migrate_claim(source)
        self.assertIn('### Formal Claim\n\n```CFEL\n## Claim\nAtom.ID\n```', result)
        self.assertNotIn('### Prose Claim', result)

    def test_interleaved_prose_preserved(self):
        result = migrate_claim('## Claim\nBefore\n```CFEL\nx\n```\nAfter\n')
        self.assertIn('Before\nAfter\n', result)
        self.assertEqual(migrate_claim(result), result)

    def test_legacy_formal_child_with_direct_prose(self):
        result = migrate_claim('## Claim\nBefore\n### Formal Claim\n```CFEL\nx\n```\nAfter\n')
        self.assertEqual(result.count('### Formal Claim'), 1)
        self.assertEqual(result.count('### Prose Claim'), 1)
        self.assertIn('Before\nAfter\n', result)
        self.assertEqual(migrate_claim(result), result)

    def test_non_cfel_payload_keeps_language_and_heading(self):
        result = migrate_claim('## Claim\n```yaml\nroots: [A]\n```\n#### Custom\nwords\n')
        self.assertNotIn('### Formal Claim', result)
        self.assertIn('```yaml\nroots: [A]\n```\n#### Custom\nwords', result)

    def test_duplicate_and_unclosed(self):
        for source in ('## Claim\na\n## Claim\nb\n', '## Claim\n```CFEL\nx\n'):
            with self.assertRaises(Ambiguous): migrate_claim(source)


if __name__ == '__main__':
    unittest.main()
