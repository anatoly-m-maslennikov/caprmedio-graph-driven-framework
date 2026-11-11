---
atom_id: CA-R-2158
ref_id: CA-R-2158@13-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Effect Authorization"
tier: 4
relations:
  child_of:
  - CA-R-2157
status: Draft
version: 13
updated_at: "2026-11-11 18:12:55 +0400"
carrier_destination:
  file:
    name: CA-R-2158@13-draft-CORE_META_MODEL-RULE--ai-agents-act-within-permission.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
current_scope_unit: CORE_META_MODEL
cce_version: cce_1
cce_form: permission
---
## Summary

AI Agents act within permission

## Claim

### Prose Claim


an AI Agent has no original authority, **must not** create **or** expand its own authority, **and** **may** perform **or** authorize a governed action **only** **when** a current Operator-established AI Agent Delegation **or** authorization rule identifies that AI Agent **and** permits the complete action, its target, **and** its decision boundary.
