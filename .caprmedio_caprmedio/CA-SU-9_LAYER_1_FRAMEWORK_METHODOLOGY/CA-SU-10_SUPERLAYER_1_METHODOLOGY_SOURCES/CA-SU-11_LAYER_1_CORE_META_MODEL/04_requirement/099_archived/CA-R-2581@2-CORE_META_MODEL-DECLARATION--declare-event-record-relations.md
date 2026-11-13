---
atom_id: CA-R-2581
ref_id: CA-R-2581@2
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Event Record.Relations
tier: 3
status: archived
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2581@2-CORE_META_MODEL-DECLARATION--declare-event-record-relations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
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

