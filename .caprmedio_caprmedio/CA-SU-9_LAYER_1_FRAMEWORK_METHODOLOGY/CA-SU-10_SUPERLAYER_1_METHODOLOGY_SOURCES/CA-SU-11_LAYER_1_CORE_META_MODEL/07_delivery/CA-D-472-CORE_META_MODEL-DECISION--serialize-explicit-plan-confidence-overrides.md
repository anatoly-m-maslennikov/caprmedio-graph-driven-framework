---
atom_id: CA-D-472
ref_id: CA-D-472
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role:=Plan).Header.Context.Plan.AI Agent Confidence Threshold
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)/(.Header.Context.Form := Plan)
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Decision Confidence"
  - CAPRMEDIO_MODEL <+ Carrier/File
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Content.Definition of Done
tier: 3
status: active
version: 31
updated_at: 2026-11-09 00:51:00 +0400
carrier_destination:
  file:
    name: CA-D-472-CORE_META_MODEL-DECISION--serialize-explicit-plan-confidence-overrides.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Serialize explicit Plan confidence overrides

## Claim

### Prose Claim


explicit Plan AI Agent Confidence Threshold overrides in Plan Atom Markdown File Carriers.


An explicit Plan AI Agent Confidence Threshold override is an integer at its declared Header path in that Plan Atom’s own Markdown File Carrier. Apply the common recursive name encoding.

- a Hub uses that same file, **not** a separately identified Objective **or** Epic settings file.
- omit an unselected override **without** copying its inherited value; the mandatory file requirement does **not** turn inheritance into a local selection.
- retain an explicit override even **when** it equals the inherited value.
- `epic_overrides` is **not** an alternative canonical encoding.
