---
subjects:
  governs: Subject/Graph
  depends_on:
  - Subject/Graph/Rule
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Content
  - Subject/Domain/Node
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Graph/Relation
version: 20
updated_at: 2026-10-25 00:56:39 +0400
relations: {}
atom_id: CA-R-1471@20
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
