---
atom_id: CA-R-035
ref_id: CA-R-035@37-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Entity
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Decision Confidence"
tier: 2
relations:
  child_of:
  - CA-M-448
status: Draft
version: 37
updated_at: "2026-11-11 18:12:55 +0400"
carrier_destination:
  file:
    name: CA-R-035@37-draft-CORE_META_MODEL-RULE--identify-necessary-information-by-confidence.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
cce_version: cce_1
cce_form: obligation
current_scope_unit: CORE_META_MODEL
---
## Summary
Identify necessary information by confidence

## Claim

### Prose Claim


an AI Agent's assessment of necessary Project information **must** use progressive context acquisition: read **every** active Project-owned Tier 0 Atom **before** using indexes, Relations, **and** Subjects **to** identify applicable Atoms; read **and** check the full Claims of those Atoms; expand inspection **when** dependencies, conflicts, missing evidence, **or** uncertainty require it. indexes, Relations, **and** Subjects support discovery **and** **must not** substitute for checking the applicable Claims. shared ancestry, descendancy, **or** structural scope alone **must not** require loading **every** Atom's full content.

the information is necessary **when** its omission would leave the AI Agent below the effective Confidence Threshold resolved under CA-M-271. the confidence **and** threshold remain operational heuristics, **not** comparable probabilities across configurations.
