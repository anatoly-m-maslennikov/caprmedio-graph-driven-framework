---
atom_id: CA-R-2686
status: Active
subjects:
  active: Scope Unit.order.number
  passive:
  - Scope Unit.order
  - Scope Unit.order.ordered
  - CFEL <+ Format/int
version: 1
updated_at: 2026-11-02 19:17:40 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2686-CORE_META_MODEL-DECLARATION--declare-scope-unit-order-number.md
  source_atom_id: CA-R-2686
  source_atom_revision: 1
  source_sha256: 0e50074d20e35f44ebc22355e6bc659d89554ace3761e1938ef68230caf3e687
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Scope Unit.order.number

## Claim

```CFEL
Scope Unit.order.number: IF order.ordered = true THEN [int, 1+]{:1} ELSE []{:0};
Scope Unit.order.number.*[]{:0}
```

## Semantics

`order.ordered` is the Boolean value on the same Scope Unit. `1+` admits integer values of at least 1; `{:1}` requires one value. When order.ordered is false, order.number has no value.

The number is the position among ordered siblings with the same direct parent. Displayed positions do not establish parentage, ownership or Atom authority.
