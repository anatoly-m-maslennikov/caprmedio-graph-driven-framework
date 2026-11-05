---
atom_id: CA-R-2156
ref_id: CA-R-2156
container:
  scope_unit: CA-SU-00
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
status: Active
version: 10
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2156-CAPRMEDIO-RULE--distinguish-human-operators-from-ai-agents.md
    path: .caprmedio_caprmedio/04_requirement
current_scope_unit: caprmedio
cce_version: cce_1
cce_form: classification
---
## Summary

Distinguish human Operators from AI Agents

## Claim

### Prose Claim


**every** Actor that performs **or** authorizes a governed action **must** have **`=1`** Type **in** (Operator, AI Agent).
