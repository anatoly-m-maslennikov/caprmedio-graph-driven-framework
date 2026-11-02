---
subjects:
  governs: Single Source of Truth
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Subject/Domain/Node/Continuant/Project.Structure
  - Structural Entity
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Continuant/Projection
version: 14
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-R-1470@14
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
---
# Summary

Define Single Source of Truth

## Scope

the authority of independently maintained facts.

## Claim

Single Source of Truth **means** **`=1`** canonical authoritative source for **every** independently maintained fact **in** the same applicable context. another representation of that fact references **or** derives from its source **without** becoming an independently maintained authority.

source authority is assigned per fact under the governing model: Atoms carry governing Claims **and** their declared source Relations; Project Structure owns declared Scope Unit facts; Structural Entity Carriers supply materialization observations; Journals preserve recorded historical facts. native Implementation Carriers **may** be authoritative for their actual realized content, structure, dependencies, **and** behavior. other admitted sources retain their declared authority. this does **not** require **all** facts **to** reside **in** **`=1`** Atom, file, **or** Artifact. a derived result **may** use multiple authoritative input facts **without** creating another authoritative source for those input facts.

## Details

Implementation actual-state authority does not establish governing intent, acceptance, or compliance. RMED remains authority for the required result, method, evaluation, and delivery. A dependency graph or another view generated from native I remains a non-authoritative Projection of those actual-state sources.
