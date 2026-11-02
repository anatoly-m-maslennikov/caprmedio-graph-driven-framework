---
subjects:
  governs: 'Entity/Object/Continuant/Projection/Type: Catalog'
  depends_on:
  - Entity/Object/Continuant/Term
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Entity Definition'
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Object/Continuant/Governing Objects/Atom.Subjects
  - Entity/Object/Continuant/Term//Artifact
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - Entity/Object/Continuant/Actor
  - Entity
  - Entity/Object/Continuant/Projection
  - Entity/Graph Syntax > Relation
  - Entity/Graph Syntax > Relation
  - 'Entity/Object/Continuant/Projection/Type: Terms Graph'
version: 23
updated_at: 2026-10-29 07:17:16 +0400
relations:
  child_of:
  - CA-R-1318
  - CA-R-1319
  - CA-R-1320
  - CA-R-1437
atom_id: CA-R-1455@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Preserve evidence and uncertainty in vocabulary diagnostic indexes

## Scope

Catalogs used as vocabulary diagnostic indexes.

## Claim

a Catalog used as a vocabulary diagnostic index **must** distinguish ordinary English use under CA-R-1320 from evidence of unresolved Project-specific use, with **every** entry bound **to** its exact source occurrence, surrounding Claim **or** reference context, **and** Artifact Revision. the index **must** declare the source selection **and** checked definition coverage that bound its judgments. capitalization, consistent use, occurrence **in** GOVERNS **or** DEPENDS_ON, **or** the appearance of a Scope Unit name, Actor name, identifier, path, **or** syntax token alone **must not** establish Project-specific Term status **or** a missing definition.

an unresolved Project-specific candidate **must** retain the source evidence that indicates Project-specific use **without** treating a suspected meaning as established authority. missing defining authority **must** be distinguished from conflicting defining authority **or** conflicting Project-specific uses. a missing-authority judgment requires complete checked definition coverage for its declared applicable source authority boundary; absence from an incomplete **or** filtered selection alone **must not** establish that judgment. **if** the evidence cannot settle ordinary versus Project-specific use, defining authority, **or** definition coverage, the affected case **must** remain explicitly uncertain with its source occurrence **and** the reason for uncertainty available for review. spelling alone **must not** transfer one occurrence's classification **to** another.

these indexes **must** remain non-authoritative Projections of the cited source evidence; they **must not** supply missing definitions, require **every** word **to** acquire a Project-specific definition, promise mechanical certainty about meaning, **or** introduce another Terms Graph **or** invented Relation edges. **any** graph representation additionally requires independently admitted Relation Kind **and** source Relation authority; index membership alone establishes neither.

## Details
