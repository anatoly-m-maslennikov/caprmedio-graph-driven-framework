---
atom_id: CA-R-2549
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2549-CORE_META_MODEL-CFEL--compare-numeric-values.md
  source_atom_id: CA-R-2549
  source_atom_revision: 2
  source_sha256: eb5ab30a14d689864cfa62b5c214c92dff04ad43a6b0f2826f60a0bab92207f3
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Compare and add numeric values in CFEL

## Claim

### Prose Claim


- `x > y`: x is greater than y.
- `x >= y`: x is greater than or equal to y.
- `x < y`: x is less than y.
- `x <= y`: x is less than or equal to y.
- `x + y` returns the numeric sum of two numeric operands. If both operands are integers, the result is an exact integer.
- Each operand resolves to one numeric value. No string coercion is allowed.
- Evaluate `+` before `=`, `!=`, `>`, `>=`, `<` and `<=`. Parentheses override this order.
- `=` tests equality, including in a Claim invariant; it does not assign a value.
- A missing or multi-valued operand makes an evaluated comparison invalid.
- Guard optional Properties by their occurrence before comparing their values.
- A comparison in Claim must hold. In an IF condition, it tests the values.
- An IF conclusion is evaluated only when its condition holds.
- A Declaration applies the comparison to each matching instance.
- Comparisons do not assign values or change occurrence counts.
- `+>`, `<+`, `>|` and `|<` remain distinct Relation operators.

## Details

```CFEL
# model
Atom.Header.Version >= 1;

Atom.Header.Tier >= -1;

# instances
Atom/(.Header.Role: Plan)//$atom;

IF ($atom.Header.Work Sequence Number{=1})
THEN ($atom.Header.Work Sequence Number > 0);
```
