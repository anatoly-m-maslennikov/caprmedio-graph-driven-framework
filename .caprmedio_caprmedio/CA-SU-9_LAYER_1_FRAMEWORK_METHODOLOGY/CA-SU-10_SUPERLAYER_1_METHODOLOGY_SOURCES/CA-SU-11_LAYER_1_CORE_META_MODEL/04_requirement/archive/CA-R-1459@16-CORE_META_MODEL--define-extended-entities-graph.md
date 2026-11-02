---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Projection/Type: Extended Entities Graph'
  depends_on:
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Projection/Type: Entities Graph'
  - Subject/Domain/Node
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Subjects
  - Subject
  - 'Subject/Graph/Relation/Type: GOVERNS'
  - 'Subject/Graph/Relation/Type: DEPENDS_ON'
  - Subject/Graph/Relation
  - Subject/Graph/Relation/Type
version: 16
updated_at: 2026-10-24 10:48:25 +0400
relations: {}
atom_id: CA-R-1459@16
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Definition
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
