---
subjects:
  governs: Entity/Object/Continuant/Projection
  depends_on:
  - Entity
  - Entity/Object/Continuant/Projection
  - Entity/Graph Syntax > Relation
version: 24
updated_at: 2026-10-29 17:09:47 +0400
relations: {}
atom_id: CA-R-1408@24
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Define Graph of Graphs

## Claim scope

Graph of Graphs compositions and any generated overview Artifact.

## Claim



The following interpretation is required when this governed concept is used:

a Graph of Graphs **means** a composition of CAPRMEDIO Graphs connected through graph-qualified typed references **or** shared source identities. secondary graphs **in** this composition remain Projections under CA-R-1471-CORE_META_MODEL-CORE-REQUIREMENT--keep-secondary-graphs-derived-from-source-authority, **and** their internal, cross-graph, **and** authoritative-source connections remain governed by CA-R-1472-CORE_META_MODEL-GENERAL-REQUIREMENT--admit-typed-secondary-graph-connections.

the composition does **not**, by itself, require another separately generated overview Artifact. **if** an overview is generated, its represented connections remain derived from the participating graphs **and** their sources **without** becoming another authority.

