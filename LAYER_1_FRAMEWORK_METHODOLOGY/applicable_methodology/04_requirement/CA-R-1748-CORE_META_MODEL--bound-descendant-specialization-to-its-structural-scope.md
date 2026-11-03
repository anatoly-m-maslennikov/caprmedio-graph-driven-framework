---
subjects:
  active: Scope Unit
  passive:
  - Atom.Content
  - Atom.Tier
  - Scope Unit
  - Scope Unit//CORE_META_MODEL
  - Entity/Object/Continuant/Selection//Extension Sources
  - Scope Unit//PROJECT_CONFIGURATION
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
  source_sha256: 32702767986294a9ac8296bfc1b7f73eb18825608027851a03f096c7ffb40264
  original_relations_sha256: 6448b762c698736659af7a49194381ae30d43e0901edf16ef3ba48f0e484c7b2
---
## Summary

Bound descendant specialization to its structural scope

## Claim scope

Applicable inherited authority in descendant Scope Units and specializations within their permitted boundaries.

## Claim

applicable inherited authority **must** remain effective **in** a descendant Scope Unit **unless** that authority explicitly permits a specialization **and** the specialization stays within the permitted boundary.

- the specialization **must not** change the parent meaning outside its declared descendant scope.
- ancestor Core authority remains protected under CA-R-033; a child declaration **or** an override label does **not** grant permission **to** weaken it.
- Extension **and** Project Configuration additions **must** also preserve Core Meta-Model authority at **every** numeric Tier under CA-R-1375-CORE_META_MODEL--restrict-methodology-source-expansion-to-core-permission. changing the descendant's numeric Tier **or** retaining unchanged Core Carrier bytes does **not** bypass that boundary. No Content-Role or Type-to-Tier restriction is introduced.
