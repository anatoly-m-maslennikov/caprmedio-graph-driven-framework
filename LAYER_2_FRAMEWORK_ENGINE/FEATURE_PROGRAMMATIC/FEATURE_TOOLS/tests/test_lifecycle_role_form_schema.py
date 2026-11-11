from pathlib import Path
import sys
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS.parent / 'FEATURE_APPS/APP_WORKBENCH'))
from ATOM_LIFECYCLE.role_form_schema import compile_role_form  # noqa: E402


class RoleFormCompilationTests(unittest.TestCase):
    def test_grouped_paths_match_flat_declarations(self):
        flat = '''## Claim

### Formal Claim

```CFEL
Atom.Header.Role :: Method;
Atom.Header.Form :: Decision;
Atom/(.Header.Role in (Method)).Header.Form :: Solution;
FOR EACH $a[<Atom>, (.Header.Form = Decision)]: (
    $a.Header.Role :: [in (Method, Evaluation)]{::1};
)
```
'''
        grouped = flat.replace('.Header.Role', '.Header.Context.Role').replace(
            '.Header.Form', '.Header.Context.Form')
        def compile_text(value):
            return compile_role_form([{'id': 'CA-R-1', '_content_bytes': value.encode()}])
        self.assertEqual(compile_text(flat), compile_text(grouped))
        self.assertEqual({('role', 'Method', ''), ('form', 'Decision', ''),
                          ('qualified', 'Solution', 'Method'),
                          ('constraint', 'Decision', 'Method'),
                          ('constraint', 'Decision', 'Evaluation')},
                         {(x['kind'], x['value'], x['role']) for x in compile_text(grouped)})


if __name__ == '__main__':
    unittest.main()
