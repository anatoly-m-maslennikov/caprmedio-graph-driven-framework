---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Scope Unit Graph'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 34
updated_at: 2026-10-27 20:00:02 +0400
relations:
  child_of:
  - CA-R-1052
  - CA-R-007
atom_id: CA-R-1740
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Bind every Project Scope Unit Graph value to exact sources

## Scope

Project Scope Unit Graph Projection values.

## Claim

**every** Project Scope Unit Graph Projection value **must** retain traceability **to** the exact Project Structure state, Settings state, Atom Revisions, Carrier observations, **or** Journal Records actually used **to** derive it. an unavailable **or** contradictory source **must** produce an explicit unresolved result for the affected value **without** erasing independent observations **or** claiming complete source coverage. declared values **and** observed materialization **must not** be conflated.

## Details
