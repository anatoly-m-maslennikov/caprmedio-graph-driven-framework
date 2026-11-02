---
subjects:
  governs: Entity
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  - Entity/Carrier
  - Entity/Object/Continuant/History/Journal
  - Entity/Object/Continuant/Projection
version: 25
updated_at: 2026-10-29 09:43:32 +0400
relations: {}
atom_id: CA-R-1470@25
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Define Single Source of Truth

## Claim scope

the authority of independently maintained facts.

## Claim

Single Source of Truth **means** **`=1`** canonical authoritative source for **every** independently maintained fact **in** the same applicable context. another representation of that fact references **or** derives from its source **without** becoming an independently maintained authority.

source authority is assigned per fact under the governing model: Atoms carry governing Claims **and** their declared source Relations; Project Structure owns declared Scope Unit facts; Structural Entity Carriers supply materialization observations; Journals preserve recorded historical facts. native Implementation Carriers **may** be authoritative for their actual realized content, structure, dependencies, **and** behavior. other admitted sources retain their declared authority. this does **not** require **all** facts **to** reside **in** **`=1`** Atom, file, **or** Artifact. a derived result **may** use multiple authoritative input facts **without** creating another authoritative source for those input facts.

## Details

Implementation actual-state authority does not establish governing intent, acceptance, or compliance. RMED remains authority for the required result, method, evaluation, and delivery. A dependency graph or another view generated from native I remains a non-authoritative Projection of those actual-state sources.
