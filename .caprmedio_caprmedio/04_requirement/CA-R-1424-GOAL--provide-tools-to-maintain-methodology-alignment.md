---
atom_id: CA-R-1424
ref_id: CA-R-1424
container:
  scope_unit: CA-SU-00
role: Requirement
form: Goal
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/Type: Applicable Methodology'
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Package
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Term//Artifact
tier: 4
relations:
  child_of:
  - CA-M-006
  - CA-R-2157
status: Active
version: 28
updated_at: 2026-11-02 18:35:20 +0400
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: caprmedio
claim_target_scope_unit: FRAMEWORK_ENGINE
---
## Summary
Provide tools to maintain methodology alignment

## Claim

### Prose Claim


the CAPRMEDIO Framework Instance **must** provide Tools sufficient **to** evaluate, repair, **and** maintain instance alignment with the current Applicable Methodology from the Project's registered Framework Instance directory, including accurate reporting of orphan Atoms **and** other nonconformance; repair **must** remain under Operator control, **and** the Operator **may** leave findings unresolved **or** retain nonconforming Artifacts.
