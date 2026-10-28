---
version: 28
updated_at: 2026-10-27 19:59:49 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-M-003
subjects:
  governs: 'Subject/caprmedio/Product: CAPRMEDIO Framework'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - Subject/CAPRMEDIO/Graph/Relation
  - Subject
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Decision Confidence
cce_version: cce_1
cce_form: obligation
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: caprmedio
status: Active
atom_id: CA-R-035
type: Rule
tier: 2
---
# Identify necessary information by confidence

an AI Agent's assessment of necessary Project information **must** use progressive context acquisition: read **every** active Project Principle **before** using indexes, Relations, **and** Subjects **to** identify applicable Atoms; read **and** check the full Claims of those Atoms; expand inspection **when** dependencies, conflicts, missing evidence, **or** uncertainty require it. indexes, Relations, **and** Subjects support discovery **and** **must not** substitute for checking the applicable Claims. shared ancestry, descendancy, **or** structural scope alone **must not** require loading **every** Atom's full content.

the information is necessary **when** its omission would leave the AI Agent below the effective Confidence Threshold resolved under CA-M-271. the confidence **and** threshold remain operational heuristics, **not** comparable probabilities across configurations.
