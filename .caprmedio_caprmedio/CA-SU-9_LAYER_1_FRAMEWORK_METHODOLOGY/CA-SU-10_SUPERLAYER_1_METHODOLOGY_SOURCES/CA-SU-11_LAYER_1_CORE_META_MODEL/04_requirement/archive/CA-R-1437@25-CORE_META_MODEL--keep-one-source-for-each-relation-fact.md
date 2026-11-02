---
subjects:
  governs: Entity/Graph Syntax > Relation
  depends_on:
  - Entity/Graph Syntax > Relation
  - Entity
  - Entity/Object/Continuant/Projection
  - Entity/Aspect/Engineering/Traceability
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity
  - Entity/Object/Continuant/History/Journal
version: 25
updated_at: 2026-10-29 07:17:16 +0400
relations: {}
atom_id: CA-R-1437@25
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
