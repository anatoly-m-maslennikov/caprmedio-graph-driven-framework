---
version: 36
updated_at: 2026-11-02 18:35:20 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-M-448
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
cce_version: cce_1
cce_form: obligation
current_scope_unit: caprmedio
status: Active
atom_id: CA-R-035
tier: 2
role: Requirement
form: Rule
---
## Summary
Identify necessary information by confidence

## Claim

### Prose Claim


an AI Agent's assessment of necessary Project information **must** use progressive context acquisition: read **every** active Project-owned Tier 0 Atom **before** using indexes, Relations, **and** Subjects **to** identify applicable Atoms; read **and** check the full Claims of those Atoms; expand inspection **when** dependencies, conflicts, missing evidence, **or** uncertainty require it. indexes, Relations, **and** Subjects support discovery **and** **must not** substitute for checking the applicable Claims. shared ancestry, descendancy, **or** structural scope alone **must not** require loading **every** Atom's full content.

the information is necessary **when** its omission would leave the AI Agent below the effective Confidence Threshold resolved under CA-M-271. the confidence **and** threshold remain operational heuristics, **not** comparable probabilities across configurations.
