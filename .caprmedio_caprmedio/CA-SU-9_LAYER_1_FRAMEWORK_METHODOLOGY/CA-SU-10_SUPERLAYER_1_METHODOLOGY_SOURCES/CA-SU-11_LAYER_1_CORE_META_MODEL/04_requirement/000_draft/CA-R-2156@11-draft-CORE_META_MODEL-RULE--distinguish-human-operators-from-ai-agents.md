---
atom_id: CA-R-2156
ref_id: CA-R-2156@11-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Actor
  dependencies:
  - CAPRMEDIO_MODEL <+ Actor
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
tier: 3
relations:
  child_of:
  - CA-R-2452
status: Draft
version: 11
updated_at: "2026-11-11 18:12:55 +0400"
carrier_destination:
  file:
    name: CA-R-2156@11-draft-CORE_META_MODEL-RULE--distinguish-human-operators-from-ai-agents.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
current_scope_unit: CORE_META_MODEL
cce_version: cce_1
cce_form: classification
---
## Summary

Distinguish human Operators from AI Agents

## Claim

### Prose Claim


**every** Actor that performs **or** authorizes a governed action **must** have **`=1`** Type **in** (Operator, AI Agent).
