---
subjects:
  governs: "Entity/Continuant/Projection/Type: Extended Entities Graph"
  depends_on:
    ["Entity/Continuant/Projection", "Entity/Continuant/Projection/Type: Entities Graph", "Entity", "Entity/Continuant/Object/Atom", "Entity/Continuant/Object/Atom.Subjects", "Subject Path", "GOVERNS", "DEPENDS_ON", "Entity/Continuant/Object/Relation", "Relation Kind"]
version: 7
updated_at: "2026-10-15 18:43:17 +0000"
relations: {}
atom_id: "CA-R-1459"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1459-CORE_META_MODEL-CORE--define-extended-entities-graph.md
  source_atom_id: CA-R-1459
  source_atom_revision: 7
  source_sha256: 61b73b94a825cd2f5121566f4dd95e9c62adcab592b12df70165caf99aea34fa
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Extended Entities Graph

## Scope

the Extended Entities Graph Projection Type.

## Claim

Extended Entities Graph **means** the Type value under Projection whose instances compose an Entities Graph Projection with representations of the Atoms that govern **or** depend on its represented Entities, using the source Atoms' direct Subjects references **and** canonical identities.

the composite view derives its Atom links **and** Entity structure from their authoritative sources **or** source-traceable upstream Projections. represented Atoms, Entities, **and** Relation facts retain their existing identities **and** source authority; repeated participation does **not** create another Atom, Entity, **or** independently authored Relation fact. the composite Projection Type does **not** become another owner of the represented graph-specific Relation Kinds. this admission establishes the composite Projection's classification **and** source-authority boundary; direct Atom-link mechanics **and** composed navigation remain governed by their corresponding authority.

## Details
