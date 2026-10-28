---
subjects:
  governs: Subject
  depends_on:
  - Subject/CAPRMEDIO/Graph/Rule
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Relation
version: 22
updated_at: 2026-10-27 19:59:55 +0400
relations: {}
atom_id: CA-R-1471
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Keep secondary graphs derived from source authority

## Scope

secondary CAPRMEDIO Graphs.

## Claim

secondary CAPRMEDIO Graphs **must** be Projections derived from their selected authoritative sources **or** source-traceable upstream Projections. their nodes **and** Relations **must** preserve source identities **and** traceability **to** the governing derivation authority **and** source facts.

storing, composing, filtering, **or** rebuilding a secondary graph **must not** make its contents another source of authority. a represented source fact is corrected **at** its authoritative source; an incorrect derivation is corrected under its governing methodology. neither case is resolved by independently editing the projected fact **or** fabricating source history.

## Details
