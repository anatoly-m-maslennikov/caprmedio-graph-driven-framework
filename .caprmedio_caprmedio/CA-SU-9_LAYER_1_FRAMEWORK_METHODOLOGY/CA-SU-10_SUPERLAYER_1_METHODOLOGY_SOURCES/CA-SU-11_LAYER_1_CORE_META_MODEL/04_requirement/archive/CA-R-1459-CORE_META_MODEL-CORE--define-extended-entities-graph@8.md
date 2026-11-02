---
subjects:
  governs: "Entity/Node/Continuant/Projection/Type: Extended Entities Graph"
  depends_on:
    ["Entity/Node/Continuant/Projection", "Entity/Node/Continuant/Projection/Type: Entities Graph", "Entity", "Entity/Node/Continuant/Atom", "Entity/Node/Continuant/Atom.Subjects", "Subject Path", "GOVERNS", "DEPENDS_ON", "Entity/Relation", "Relation Kind"]
version: 8
updated_at: "2026-10-19 15:53:09 +0400"
relations: {}
atom_id: "CA-R-1459"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define Extended Entities Graph

## Scope

the Extended Entities Graph Projection Type.

## Claim

Extended Entities Graph **means** the Type value under Projection whose instances compose an Entities Graph Projection with representations of the Atoms that govern **or** depend on its represented Entities, using the source Atoms' direct Subjects references **and** canonical identities.

the composite view derives its Atom links **and** Entity structure from their authoritative sources **or** source-traceable upstream Projections. represented Atoms, Entities, **and** Relation facts retain their existing identities **and** source authority; repeated participation does **not** create another Atom, Entity, **or** independently authored Relation fact. the composite Projection Type does **not** become another owner of the represented graph-specific Relation Kinds. this admission establishes the composite Projection's classification **and** source-authority boundary; direct Atom-link mechanics **and** composed navigation remain governed by their corresponding authority.

## Details
