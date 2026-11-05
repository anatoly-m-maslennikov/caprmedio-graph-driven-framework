---
subjects:
  active: CAPRMEDIO_MODEL <+ Scope Unit
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//CORE_META_MODEL
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Extension Sources
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
version: 37
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-033
atom_id: CA-R-1748
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1748-CORE_META_MODEL--bound-descendant-specialization-to-its-structural-scope.md
  source_atom_id: CA-R-1748
  source_atom_revision: 37
  source_sha256: ce03304d1e005d516eff374e672e2e76b3c3f4c1669e328fe3827f7650850491
  original_relations_sha256: 6448b762c698736659af7a49194381ae30d43e0901edf16ef3ba48f0e484c7b2
---
## Summary

Bound descendant specialization to its structural scope

## Claim

### Prose Claim


Applicable inherited authority in descendant Scope Units and specializations within their permitted boundaries.


applicable inherited authority **must** remain effective **in** a descendant Scope Unit **unless** that authority explicitly permits a specialization **and** the specialization stays within the permitted boundary.

- the specialization **must not** change the parent meaning outside its declared descendant scope.
- ancestor Core authority remains protected under CA-R-033; a child declaration **or** an override label does **not** grant permission **to** weaken it.
- Extension **and** Project Configuration additions **must** also preserve Core Meta-Model authority at **every** numeric Tier under CA-R-1375-CORE_META_MODEL--restrict-methodology-source-expansion-to-core-permission. changing the descendant's numeric Tier **or** retaining unchanged Core Carrier bytes does **not** bypass that boundary. No Content-Role or Type-to-Tier restriction is introduced.
