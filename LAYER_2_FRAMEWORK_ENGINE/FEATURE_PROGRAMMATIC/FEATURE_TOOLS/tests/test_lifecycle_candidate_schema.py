import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE.candidate_schema import compile_candidate_schema, load_candidate_schema  # noqa: E402
from ATOM_LIFECYCLE.role_form_schema import RoleFormSchema  # noqa: E402

CORE = TOOLS.parents[2] / '.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL'


def source(atom_id, status='Active', body=''):
    return f'''---
atom_id: {atom_id}
role: Requirement
form: Declaration
status: {status}
version: 1
---
{body}
'''


class CandidateSchemaTests(unittest.TestCase):
    def test_cli_selects_sources_and_only_formal_cfel(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / 'model'
            root.mkdir()
            encoded = source('CA-R-1', status='active', body='''## Claim
### Formal Claim
```CFEL
# a comment is not a gate
Atom.Header.Role :: Plan;
Atom.Header.Role :: Method;
Atom.Header.Form :: Decision;
# Atom.Header.Role :: Phantom;
Atom/(.Header.Role in (Plan)).Header.Form :: Plan;
FOR EACH $a[<Atom>, (.Header.Form = Decision)]:
(
    $a.Header.Role:: [in (Method)]{::1}
);
Atom.Header.ID:: [atom id]{::1};
Atom.Content.Summary:: {::1}; # inline comment
# Atom.Content.Secret:: {::1};
```
## Other
```CFEL
Atom.Content.Hidden:: {::1};
```
''')
            (root / 'CA-R-1.md').write_text(encoded.replace('role: Requirement', 'role: requirement')
                                           .replace('form: Declaration', 'form: declaration'))
            (root / 'CA-R-2.md').write_text(source('CA-R-2', status='Draft', body='invalid'))
            (root / 'archive').mkdir()
            (root / 'archive/CA-R-3.md').write_text('invalid')
            output = Path(directory) / 'output/schema.json'
            subprocess.run([sys.executable, str(TOOLS / 'ATOM_LIFECYCLE/candidate_schema.py'),
                            '--model-root', str(root), '--output', str(output)], check=True)
            asset = json.loads(output.read_text())
            self.assertEqual([('CA-R-1', 1, 'CA-R-1.md')],
                             [(s['atom_id'], s['version'], s['path']) for s in asset['workbench']['sources']])
            compiled = load_candidate_schema(output)
            self.assertIn('header.identity.atom_id', compiled.header(1).names)
            self.assertEqual(('content.summary',), compiled.content.names)
            rule = compiled.content.rules[0]
            self.assertEqual(('CA-R-1', 1, 'CA-R-1.md'),
                             (rule.source.reference, rule.source.version, rule.source.source_path))
            compiled.validate_role_form('Plan', 'Plan')
            compiled.validate_role_form('Method', 'Decision')
            with self.assertRaisesRegex(ValueError, 'not permitted'):
                compiled.validate_role_form('Plan', 'Decision')
            with self.assertRaisesRegex(ValueError, 'not declared'):
                compiled.validate_role_form('Unknown', 'Decision')
            compiled.validate_role_form('Plan', 'Unclassified')
            self.assertEqual('decision', compiled.role_form.encode('form', 'Decision'))
            self.assertEqual('Decision', compiled.role_form.decode('form', 'decision'))
            self.assertEqual('Unclassified', compiled.role_form.encode('form', 'Unclassified'))
            self.assertNotIn('Phantom', compiled.role_form.roles)
            self.assertEqual(output.read_bytes(), compile_candidate_schema(root))
            asset['role_form'][0]['value'] = 'tampered'
            output.write_text(json.dumps(asset))
            with self.assertRaisesRegex(ValueError, 'digest mismatch'):
                load_candidate_schema(output)

    def test_current_core_compiles(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'schema.json'
            path.write_bytes(compile_candidate_schema(CORE))
            asset = json.loads(path.read_text())
            self.assertTrue(asset['workbench']['sources'])
            compiled = load_candidate_schema(path)
            self.assertTrue(compiled.header(1).names)
            self.assertTrue(compiled.content.rules)
            compiled.validate_role_form('Method', 'Decision')
            compiled.validate_role_form('Operations', 'Direct Policy')
            compiled.validate_role_form('Operations', 'Workflow')
            with self.assertRaises(ValueError):
                compiled.validate_role_form('Requirement', 'Decision')
            with self.assertRaises(ValueError):
                compiled.validate_role_form('Method', 'Work Report')
            with self.assertRaises(ValueError):
                compiled.validate_role_form('Plan', 'Workflow')
            self.assertIn(('Requirement', 'Declaration'), compiled.role_form.qualified)
            self.assertIn('Work Report', compiled.role_form.forms)

    def test_codec_rejects_collisions(self):
        schema = RoleFormSchema(frozenset(), frozenset({'Work Report', 'Work-Report'}), frozenset(), ())
        with self.assertRaisesRegex(ValueError, 'Ambiguous'):
            schema.encode('form', 'Work Report')


if __name__ == '__main__':
    unittest.main()
