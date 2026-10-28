---
subjects:
  governs: Subject/Graph Relation
  depends_on:
  - Subject/Graph Relation/Type
  - Subject
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Engineering/Traceability
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node
  - Subject/Graph Node/Domain/Continuant/History/Journal
version: 23
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-R-1437@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
