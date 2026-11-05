---
atom_id: CA-R-2580
ref_id: CA-R-2580
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Event Record.action
version: 2
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Declaration
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2580-CORE_META_MODEL-DECLARATION--declare-event-record-action.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Event Record.action

## Claim

### Formal Claim

```CFEL
# model
Event Record.action{::1}:: [string]{::1};

Event Record.action.*[]{::0};

Event Record.action: create;

Event Record.action: update;

Event Record.action: archive
```

