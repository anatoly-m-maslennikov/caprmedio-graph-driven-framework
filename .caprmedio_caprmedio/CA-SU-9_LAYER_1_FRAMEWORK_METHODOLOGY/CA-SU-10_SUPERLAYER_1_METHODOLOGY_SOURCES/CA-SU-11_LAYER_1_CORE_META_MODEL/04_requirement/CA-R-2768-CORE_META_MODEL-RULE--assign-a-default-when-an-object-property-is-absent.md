---
atom_id: CA-R-2768
ref_id: CA-R-2768
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
tier: 3
status: active
version: 3
updated_at: 2026-11-05 14:25:52 +0400
carrier_destination:
  file:
    name: CA-R-2768-CORE_META_MODEL-RULE--assign-a-default-when-an-object-property-is-absent.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Assign a default when an Object Property is absent

## Claim

### Prose Claim



- A fallback chain returns the first available value from left to right. An omitted value, null, or an empty string is empty. Zero and false are values.
- A reached nonempty value must satisfy the applicable Format and cardinality. Invalid values are errors.
- Evaluate each fallback only when needed. An exhausted chain, an evaluated cycle, or multiple applicable chains is an error.
- A fallback expression can read a literal, a Property on the same bearer, an explicitly bound Property, or a contextual lookup. An explicit foreign-bearer read requires one resolved target.
- The result is an effective value. The Property and its Carrier retain their authored values.

### Formal Claim

```CFEL
# model
p ?== expression
```

## Details

```CFEL
# model
Atom.Header.Label ?== Atom.Header.Form
```
