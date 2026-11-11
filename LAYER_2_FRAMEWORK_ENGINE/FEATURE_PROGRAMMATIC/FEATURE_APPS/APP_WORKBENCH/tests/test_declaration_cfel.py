# CA-E-675@11

from pathlib import Path
import sys
import unittest

APP_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(APP_ROOT))

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.declaration_cfel import (  # noqa: E402
    formal_claim_blocks,
    model_statements,
)


class FormalInputTests(unittest.TestCase):
    def test_only_direct_formal_claim_cfel_fences_supply_expressions(self):
        body = """## Claim
### Prose Claim
```CFEL
Atom.Content.FromProse[string]{::1};
```
### Formal Claim
Text outside the fence is not a declaration.
```sql
Atom.Content.WrongLanguage[string]{::1};
```
```CFEL
Atom.Content.Summary[string]{::1};
```
#### Example
```CFEL
Atom.Content.NestedExample[string]{::1};
```
## Semantics
```CFEL
Atom.Content.FromSemantics[string]{::1};
```
## Details
```CFEL
Atom.Content.FromDetails[string]{::1};
```
"""
        self.assertEqual(
            ("Atom.Content.Summary[string]{::1};\n",), formal_claim_blocks(body),
        )
        self.assertEqual((), formal_claim_blocks("```CFEL\nAtom.Content.Unscoped[string];\n```\n"))

    def test_comments_have_no_section_or_declaration_meaning(self):
        body = """## Claim
### Formal Claim
```CFEL
# Atom.Content.FromComment[string]{::1};
Atom.Content.Summary[string]{::1}; # ignore this; and the rest
# model
Atom.Content.Details[string]{::0..1};
# instances
Atom.Content.Semantics[string]{::0..1};
```
"""
        self.assertEqual(
            [
                "Atom.Content.Summary[string]{::1}",
                "Atom.Content.Details[string]{::0..1}",
                "Atom.Content.Semantics[string]{::0..1}",
            ],
            model_statements(formal_claim_blocks(body)[0]),
        )

    def test_quoted_hashes_semicolons_and_escaped_quotes_are_values(self):
        expression = r'''Thing.Value == "a#b; c\"#d"; Thing.Other == 'e#f; g'; Thing ;> Other;'''
        body = "## Claim\n### Formal Claim\n```CFEL\n" + expression + " # not a value\n```\n"
        self.assertEqual(
            [r'''Thing.Value == "a#b; c\"#d"''', "Thing.Other == 'e#f; g'", "Thing ;> Other"],
            model_statements(formal_claim_blocks(body)[0]),
        )

    def test_markerless_blocks_work_and_unrelated_heading_levels_do_not(self):
        body = """## Claim
### Formal Claim
```cfel
Atom.Content.One[string];
```
```CFEL
Atom.Content.Two[string];
```
## Formal Claim
```CFEL
Atom.Content.NotUnderClaim[string];
```
"""
        self.assertEqual(
            ("Atom.Content.One[string];\n", "Atom.Content.Two[string];\n"),
            formal_claim_blocks(body),
        )


if __name__ == "__main__":
    unittest.main()
