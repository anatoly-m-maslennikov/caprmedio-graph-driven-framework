---
atom_id: CA-R-2468
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Requirement).Form
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---

## Summary

Register Declaration as a Requirement Form

## Claim

Declaration is a Requirement Form.

Its Claim uses:

- CFEL for expressible constraints.
- Prose for the remaining constraints.

A Primary Node has brief Semantics. A Property has none.

A Property Declaration specifies:

1. Property occurrence, where constrained.
2. Allowed value Format.
3. Value cardinality.
4. Dependent-name Format.
5. Dependent-name cardinality.

An unchanged inherited Property keeps its original Declaration. An explicit local MODEL override selects its effective replacement.
