---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Relation
  depends_on:
  - Subject/CAPRMEDIO/Graph/Relation/Type
  - Subject
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Traceability
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 24
updated_at: 2026-10-27 19:59:54 +0400
relations: {}
atom_id: CA-R-1437
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Keep one source for each relation fact

## Scope

authoritative source declarations for Relation facts.

## Claim

**every** independently authored Relation fact **must** have **`=1`** authoritative source declaration under Single Source of Truth. its representation **in** multiple CAPRMEDIO Graph views remains a reference **or** derived Projection of that declaration **without** creating another independently maintained source.

a Relation derived under admitted derivation authority **must** remain traceable **to** that authority **and** its authoritative input facts, including through upstream Projections. it does **not** require a fabricated direct source declaration for the derived result. this distinction **must not** weaken a Relation Kind's requirement for an explicit source fact **or** permit unsupported inference.

## Details
