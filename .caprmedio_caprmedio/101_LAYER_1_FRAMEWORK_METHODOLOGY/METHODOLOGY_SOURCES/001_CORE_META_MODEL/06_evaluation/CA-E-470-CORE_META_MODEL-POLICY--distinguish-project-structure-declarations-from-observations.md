---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement/Type: Goal'
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Scope Unit Graph'
version: 19
updated_at: 2026-10-27 19:59:35 +0400
relations:
  evaluation_for:
  - CA-R-1483
  - CA-R-1484
  - CA-R-926
  - CA-R-626
  - CA-M-291
atom_id: CA-E-470
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
type: Policy
tier: 6
---
# Summary

Distinguish Project Structure declarations from observations

## Scope

Project Structure declarations and observations.

## Claim

the Evaluation **must** fail **if** a consumer requires a structural Projection, promotes an observed folder **or** Goal into a declaration, conceals a declared unit because its Carrier **or** Active Goal is absent, treats a Draft **or** archived Goal as Active coverage, **or** repairs contradictory sources **without** authorization. test declared-and-materialized, declared-but-unmaterialized, undeclared folder candidate, missing Active Goal, mismatched Carrier Name, logical-parent/physical-parent exception, **and** retired structural Projection cases. findings **must** retain their category **and** exact source evidence; an undeclared candidate **or** Goal coverage gap alone **must not** erase a declaration **or** authorize a mutation.

## Details
