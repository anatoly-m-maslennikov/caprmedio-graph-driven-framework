---
subjects:
  governs: "Entity/Node/Continuant/Projection/Type: Extended Entities Graph"
  depends_on:
    ["Entity/Node/Continuant/Projection", "Entity/Node/Continuant/Projection/Type: Entities Graph", "Entity", "Entity/Node/Continuant/Atom", "Entity/Node/Continuant/Atom.Subjects", "Subject Path", "Subject Target", "GOVERNS", "DEPENDS_ON", "Entity/Relation", "Relation Kind"]
version: 9
updated_at: "2026-10-21 01:47:52 +0400"
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
  source_atom_revision: 9
  source_sha256: 149347abfeef1d82c056745f18a9ad09218e6464461df47e8bc0c87fc6366a0d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Extended Entities Graph

## Scope

the Extended Entities Graph Projection Type.

## Claim

Extended Entities Graph **means** the Type value under Projection whose instances compose an Entities Graph Projection with representations of the Atoms that govern **or** depend on its represented Entity-root Subject Targets, using the source Atoms' direct Subjects references **and** canonical identities.

the composite view derives its Atom links **and** Entity structure from their authoritative sources **or** source-traceable upstream Projections. represented Atoms, Entities, **and** Relation facts retain their existing identities **and** source authority; repeated participation does **not** create another Atom, Entity, or independently authored Relation fact. the composite Projection Type does **not** become another owner of the represented graph-specific Relation Kinds. this admission establishes the composite Projection's classification **and** source-authority boundary; direct Atom-link mechanics **and** composed navigation remain governed by their corresponding authority.

## Details

Method-root Subject Targets are not Entity identities and are excluded from the Entities Graph's native Entity membership. an Atom with a Method-root Subject may be shown only when an explicit view rule admits it as a source reference; that reference does not create a Method Topic Object or silently enlarge the Entity graph.
