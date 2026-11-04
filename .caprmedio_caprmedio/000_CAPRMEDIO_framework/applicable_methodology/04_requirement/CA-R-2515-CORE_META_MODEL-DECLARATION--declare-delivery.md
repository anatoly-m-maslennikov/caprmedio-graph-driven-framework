---
atom_id: CA-R-2515
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
version: 2
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2515-CORE_META_MODEL-DECLARATION--declare-delivery.md
  source_atom_id: CA-R-2515
  source_atom_revision: 2
  source_sha256: 20d6125efa919b669f8230f905d394ee3bf79233d4c14ea18eb9f216f8cf6867
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom/(.Role := Delivery)

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role: Delivery)
```

## Semantics

A Delivery specifies how something is represented, stored, or placed in a Carrier.
