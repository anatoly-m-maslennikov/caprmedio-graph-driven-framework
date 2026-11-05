---
atom_id: CA-R-2581
ref_id: CA-R-2581
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Event Record.Relations
version: 2
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Declaration
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2581-CORE_META_MODEL-DECLARATION--declare-event-record-relations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Event Record.Relations

## Claim

### Formal Claim

```CFEL
# model
Event Record.Relations{::1}:: []{::0};

# instances
Event Record.Relations.*[Relation//$relation]{::0+}
```

