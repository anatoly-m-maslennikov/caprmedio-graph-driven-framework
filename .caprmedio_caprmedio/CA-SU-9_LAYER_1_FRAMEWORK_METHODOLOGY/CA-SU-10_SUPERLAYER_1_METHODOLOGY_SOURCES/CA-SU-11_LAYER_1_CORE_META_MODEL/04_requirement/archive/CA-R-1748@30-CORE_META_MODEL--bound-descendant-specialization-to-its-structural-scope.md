---
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Content
  - Subject/Domain/Node/Continuant/Atom.Tier
  - Methodology Source
  - Subject/Domain/Node/Continuant/Scope Unit//CORE_META_MODEL
  - Subject/Domain/Node/Continuant/Selection//Extension Sources
  - Subject/Domain/Node/Continuant/Scope Unit//PROJECT_CONFIGURATION
version: 30
updated_at: 2026-10-24 19:39:48 +0400
relations:
  child_of:
  - CA-R-033
atom_id: CA-R-1748@30
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Bound descendant specialization to its structural scope

## Scope

Applicable inherited authority in descendant Scope Units and specializations within their permitted boundaries.

## Claim

applicable inherited authority **must** remain effective **in** a descendant Scope Unit **unless** that authority explicitly permits a specialization **and** the specialization stays within the permitted boundary.

- the specialization **must not** change the parent meaning outside its declared descendant scope.
- ancestor Core authority remains protected under CA-R-033; a child declaration **or** an override label does **not** grant permission **to** weaken it.
- Extension **and** Project Configuration additions **must** also preserve Core Meta-Model authority at **every** numeric Tier under CA-R-1375-CORE_META_MODEL--restrict-methodology-source-expansion-to-core-permission. changing the descendant's numeric Tier **or** retaining unchanged Core Carrier bytes does **not** bypass that boundary. No Content-Role or Type-to-Tier restriction is introduced.

## Details
