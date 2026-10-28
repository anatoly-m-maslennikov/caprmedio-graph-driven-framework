---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Direct Relation Registry'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Relation/Type
  - Subject
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
  - Subject/CAPRMEDIO/Graph/Relation.Authority
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool
  - Subject/CAPRMEDIO/Graph/Relation
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Traceability
version: 32
updated_at: 2026-10-27 19:59:39 +0400
relations:
  method_for:
  - CA-R-806
  - CA-R-1246
  - CA-R-1437
  - CA-R-1472
atom_id: CA-M-120
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Implementation Method
---
# Summary

Compile the direct-relation registry

## Scope

direct-relation registry compilation.

## Claim

**to** compile the optional direct-relation registry Projection, the Generator **must** perform **all** of:

1. read each declared Relation Type from its governing R Claim(s). The Claim(s) must provide the canonical name and meaning; preserve any relevant inverse, derivation, or transitivity semantics when explicitly stated. report missing **or** conflicting defining Claims without inventing a name, meaning, direction, or derivation.
2. collect selected Graph Rule declarations separately from Relation Type metadata. When such Rules are selected, retain their graph-specific endpoint classes, endpoint graph contexts, cardinality, permissions, and prohibitions; do **not** require a Graph Rule declaration solely because a Relation Type is known, require a metadata registry, or copy Rule constraints into a Type record.
3. derive inverse navigation from the defining Type authority **without** independently authoring an inverse Relation fact. distinguish an independently authored Relation fact from the governing derivation authority and input facts under CA-R-1437; do **not** invent a direct source declaration for a computed result.
4. retain source traceability for the non-authoritative registry Projection. resolve cross-graph and authoritative-source endpoints against any applicable Graph Rule contexts under CA-R-1472. cross-graph references **or** views **must not** admit a foreign Type natively **or** reclassify an external endpoint as a native node of the receiving graph.

## Details
