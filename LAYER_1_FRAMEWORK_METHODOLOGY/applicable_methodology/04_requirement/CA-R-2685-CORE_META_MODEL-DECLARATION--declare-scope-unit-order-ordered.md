---
atom_id: CA-R-2685
ref_id: CA-R-2685
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.order.ordered
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit.order
  - CAPRMEDIO_MODEL <+ CFEL <+ Format/bool
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:17:40 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2685-CORE_META_MODEL-DECLARATION--declare-scope-unit-order-ordered.md
  source_atom_id: CA-R-2685
  source_atom_revision: 1
  source_sha256: 211a823a95658543289212a290164a11eddaf5f5638aedffa24bf4428f307f0f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Scope Unit.order.ordered

## Claim

### Formal Claim

```CFEL
# model
Scope Unit.order.ordered:: [bool]{::1};

Scope Unit.order.ordered.*[]{::0}
```

