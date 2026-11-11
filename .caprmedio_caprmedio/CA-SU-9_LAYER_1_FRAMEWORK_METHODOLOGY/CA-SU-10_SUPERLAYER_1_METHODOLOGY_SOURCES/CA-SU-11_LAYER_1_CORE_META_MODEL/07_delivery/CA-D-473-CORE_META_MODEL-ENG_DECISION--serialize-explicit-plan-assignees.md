---
atom_id: CA-D-473
ref_id: CA-D-473
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Assignee
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Assignee
  - CAPRMEDIO_MODEL <+ Carrier/File
tier: 3
relations:
  delivery_for:
  - CA-R-1585
status: active
version: 27
updated_at: 2026-11-09 00:51:00 +0400
carrier_destination:
  file:
    name: CA-D-473-CORE_META_MODEL-ENG_DECISION--serialize-explicit-plan-assignees.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Serialize explicit Plan Assignees

## Claim

### Prose Claim


explicit Plan Assignee overrides in Plan File Carriers.


Where the model admits an explicit Assignee override, a Plan File Carrier serializes **`=1`** such value at its declared Header path through the common name encoding; omission **must** preserve CA-R-1585-CORE_META_MODEL-RULE--default-plan-work-assignment-to-an-ai-agent for its own work rather than copying the default.
