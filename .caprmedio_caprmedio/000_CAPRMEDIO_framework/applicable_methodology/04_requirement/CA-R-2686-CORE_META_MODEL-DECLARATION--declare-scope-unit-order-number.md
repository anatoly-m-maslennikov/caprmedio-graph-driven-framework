---
atom_id: CA-R-2686
ref_id: CA-R-2686
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.order.number
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit.order
  - CAPRMEDIO_MODEL <+ Scope Unit.order.ordered
  - CAPRMEDIO_MODEL <+ CFEL <+ Format/int
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:17:40 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2686-CORE_META_MODEL-DECLARATION--declare-scope-unit-order-number.md
  source_atom_id: CA-R-2686
  source_atom_revision: 1
  source_sha256: e2dc865be1cf7d6dafdaea097135546320b5c5a7a145e244d3501e6c8667aa47
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Scope Unit.order.number

## Claim

### Formal Claim

```CFEL
# model
Scope Unit.order.number: IF order.ordered = true THEN [int, 1+]{::1} ELSE []{::0};

Scope Unit.order.number.*[]{::0}
```

## Semantics

`order.ordered` is the Boolean value on the same Scope Unit. `1+` admits integer values of at least 1; `{:1}` requires one value. When order.ordered is false, order.number has no value.

The number is the position among ordered siblings with the same direct parent. Displayed positions do not establish parentage, ownership or Atom authority.
