---
atom_id: CA-R-2685
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Scope Unit.order.ordered
  passive:
  - CAPRMEDIO_MODEL <+ Scope Unit.order
  - CAPRMEDIO_MODEL <+ CFEL <+ Format/bool
version: 1
updated_at: 2026-11-02 19:17:40 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2685-CORE_META_MODEL-DECLARATION--declare-scope-unit-order-ordered.md
  source_atom_id: CA-R-2685
  source_atom_revision: 1
  source_sha256: ba8aa90d9993eccbb28ecf956e6a6784dd195690e3a281b0795bde101c6c75b8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Scope Unit.order.ordered

## Claim

### Formal Claim

```CFEL
# model
Scope Unit.order.ordered: [bool]{:1};

Scope Unit.order.ordered.*[]{:0}
```

