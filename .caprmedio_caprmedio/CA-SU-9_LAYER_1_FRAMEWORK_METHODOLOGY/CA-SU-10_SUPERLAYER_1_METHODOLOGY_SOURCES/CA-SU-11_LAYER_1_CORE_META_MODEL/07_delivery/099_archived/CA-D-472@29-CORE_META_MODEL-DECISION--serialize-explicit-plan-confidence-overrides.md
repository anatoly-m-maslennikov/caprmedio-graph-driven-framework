---
atom_id: CA-D-472
ref_id: CA-D-472@29
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Plan).Header.AI Agent Confidence Threshold
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)/(.Header.Form := Plan)
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
  - CAPRMEDIO_MODEL <+ Carrier/File
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Content.Definition of Done
tier: 3
status: archived
version: 29
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-D-472@29-CORE_META_MODEL-DECISION--serialize-explicit-plan-confidence-overrides.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Serialize explicit Plan confidence overrides

## Claim

### Prose Claim


explicit Plan Autonomous Confidence Threshold overrides in Plan Atom Markdown File Carriers.


an explicit Plan Autonomous Confidence Threshold override **must** use the top-level integer frontmatter field `autonomous_confidence_threshold` **in** that Plan Atom's own mandatory Markdown File Carrier.

- a Hub uses that same file, **not** a separately identified Objective **or** Epic settings file.
- omit an unselected override **without** copying its inherited value; the mandatory file requirement does **not** turn inheritance into a local selection.
- retain an explicit override even **when** it equals the inherited value.
- `epic_overrides` is **not** an alternative canonical encoding.
