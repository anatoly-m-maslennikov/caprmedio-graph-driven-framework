---
subjects:
  governs: 'Entity/Object/Continuant/Projection/Type: Scope Unit Graph'
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - Entity/Object/Continuant/History/Journal
version: 37
updated_at: 2026-10-29 10:13:49 +0400
relations:
  child_of:
  - CA-R-1052
  - CA-R-007
atom_id: CA-R-1740@37
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Rule
---
## Summary

Bind every Project Scope Unit Graph value to exact sources

## Claim scope

Project Scope Unit Graph Projection values.

## Claim

**every** Project Scope Unit Graph Projection value **must** retain traceability **to** the exact Project Structure state, Settings state, Atom Revisions, Carrier observations, **or** Journal Records actually used **to** derive it. an unavailable **or** contradictory source **must** produce an explicit unresolved result for the affected value **without** erasing independent observations **or** claiming complete source coverage. declared values **and** observed materialization **must not** be conflated.
