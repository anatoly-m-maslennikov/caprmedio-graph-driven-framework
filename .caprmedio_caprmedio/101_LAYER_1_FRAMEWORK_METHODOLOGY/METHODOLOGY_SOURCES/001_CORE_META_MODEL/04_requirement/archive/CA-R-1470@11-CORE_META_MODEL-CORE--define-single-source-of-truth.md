---
subjects:
  governs: Single Source of Truth
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Entity/Node/Continuant/Atom.Substance
  - Entity/Node/Continuant/Project.Structure
  - Structural Entity
  - Entity/Node/Continuant/History/Journal
  - Entity/Node/Continuant/Projection
version: 11
updated_at: 2026-10-23 03:06:32 +0400
relations: {}
atom_id: CA-R-1470@11
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 9
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
