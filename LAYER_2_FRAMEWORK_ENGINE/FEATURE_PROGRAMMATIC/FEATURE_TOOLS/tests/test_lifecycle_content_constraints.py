import sys
from pathlib import Path
import unittest

TOOLS = Path(__file__).resolve().parents[1]
WORKBENCH = TOOLS.parent / 'FEATURE_APPS/APP_WORKBENCH'
sys.path[:0] = [str(TOOLS), str(WORKBENCH)]
from ATOM_LIFECYCLE.content_constraints import compile_content_constraints, load_content_constraints  # noqa: E402


def declaration(text):
    return {'status_group': 'Current', 'role': 'Requirement', 'form': 'Declaration',
            'id': 'CA-R-1', 'ref': 'CA-R-1', 'version': 1, 'source_path': 'CA-R-1.md',
            '_content_bytes': ('## Claim\n### Formal Claim\n```CFEL\n' + text + '\n```\n').encode()}


class ContentConstraintsTests(unittest.TestCase):
    def test_grouped_context_selector_applies_to_encoded_role(self):
        records = compile_content_constraints([declaration('''
Atom/(.Header.Context.Role := Method)/(.Header.Context.Form := Direct Policy).Content.Claim{::1}:: []{::0};
''')])
        schema = load_content_constraints(records, {'CA-R-1'})
        with self.assertRaisesRegex(ValueError, 'claim'):
            schema.validate({'role': 'method', 'form': 'direct_policy', 'content_markdown': ''})
        schema.validate({'role': 'plan', 'form': 'direct_policy', 'content_markdown': ''})

    def test_required_and_allowed_claim_children(self):
        records = compile_content_constraints([declaration('''
Atom.Content.Summary{::1}:: {::1};
Atom/(.Header.Role in RMED).Content.Claim{::1}:: []{::0};
Atom/(.Header.Role in RMED).Content.Claim.*[string, in (Formal Claim, Prose Claim)]{::1..2};
Atom/(.Header.Role in (Plan))/(.Header.Form in (Work Report)).Content.Details:: {::1};
''')])
        schema = load_content_constraints(records, {'CA-R-1'})
        def check(body, role='Method'):
            schema.validate({'role': role, 'form': 'Declaration', 'content_markdown': body})
        check('## Summary\nText\n## Claim\n### Prose Claim\nText\n')
        check('## Summary\nText\n', 'Operations')
        with self.assertRaisesRegex(ValueError, 'summary'):
            check('## Claim\n### Prose Claim\nText\n')
        with self.assertRaisesRegex(ValueError, 'claim'):
            check('## Summary\nText\n## Claim\n')
        with self.assertRaisesRegex(ValueError, 'children'):
            check('## Summary\nText\n## Claim\n### Other\nText\n')
        with self.assertRaisesRegex(ValueError, 'children'):
            check('## Summary\nText\n## Claim\n### Prose Claim\nA\n### Prose Claim\nB\n')
        with self.assertRaisesRegex(ValueError, 'claim'):
            check('## Summary\nText\n```md\n## Claim\n### Prose Claim\n```\n')
        with self.assertRaisesRegex(ValueError, 'details.*direct Markdown'):
            schema.validate({'role': 'Plan', 'form': 'Work Report',
                             'content_markdown': '## Summary\nText\n## Details\n### Result\nText\n'})
        schema.validate({'role': 'Plan', 'form': 'Work Report',
                         'content_markdown': '## Summary\nText\n## Details\nText\n'})

    def test_untrusted_asset_is_checked(self):
        with self.assertRaises(ValueError):
            load_content_constraints([{'path': ['summary'], 'roles': None, 'forms': None,
                'min': 1, 'max': 1, 'children': [], 'source': 'CA-R-unknown'}], {'CA-R-1'})


if __name__ == '__main__':
    unittest.main()
