---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Projection/(.Form:=Catalog)'
  passive:
  - CAPRMEDIO_MODEL <+ Term
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Requirement)/(.Header.Form: Entity Definition)'
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Header.Subjects
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Actor
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/(.Form: Terms Graph)'
version: 27
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-1318
  - CA-R-1319
  - CA-R-1320
  - CA-R-1437
atom_id: CA-R-1455
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Preserve evidence and uncertainty in vocabulary diagnostic indexes

## Claim

### Prose Claim


Catalogs used as vocabulary diagnostic indexes.


a Catalog used as a vocabulary diagnostic index **must** distinguish ordinary English use under CA-R-1320 from evidence of unresolved Project-specific use, with **every** entry bound **to** its exact source occurrence, surrounding Claim **or** reference context, **and** Artifact Revision. the index **must** declare the source selection **and** checked definition coverage that bound its judgments. capitalization, consistent use, occurrence **in** GOVERNS **or** DEPENDS_ON, **or** the appearance of a Scope Unit name, Actor name, identifier, path, **or** syntax token alone **must not** establish Project-specific Term status **or** a missing definition.

an unresolved Project-specific candidate **must** retain the source evidence that indicates Project-specific use **without** treating a suspected meaning as established authority. missing defining authority **must** be distinguished from conflicting defining authority **or** conflicting Project-specific uses. a missing-authority judgment requires complete checked definition coverage for its declared applicable source authority boundary; absence from an incomplete **or** filtered selection alone **must not** establish that judgment. **if** the evidence cannot settle ordinary versus Project-specific use, defining authority, **or** definition coverage, the affected case **must** remain explicitly uncertain with its source occurrence **and** the reason for uncertainty available for review. spelling alone **must not** transfer one occurrence's classification **to** another.

these indexes **must** remain non-authoritative Projections of the cited source evidence; they **must not** supply missing definitions, require **every** word **to** acquire a Project-specific definition, promise mechanical certainty about meaning, **or** introduce another Terms Graph **or** invented Relation edges. **any** graph representation additionally requires independently admitted Relation Kind **and** source Relation authority; index membership alone establishes neither.
