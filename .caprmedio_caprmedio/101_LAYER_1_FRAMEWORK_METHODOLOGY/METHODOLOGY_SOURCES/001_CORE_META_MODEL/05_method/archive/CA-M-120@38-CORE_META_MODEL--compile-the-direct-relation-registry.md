---
subjects:
  governs: 'Entity/Object/Continuant/Projection/Type: Direct Relation Registry'
  depends_on:
  - Entity/Graph Syntax > Relation
  - Entity
  - 'Entity/Object/Continuant/Projection/Type: Applicable Methodology'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement'
  - Entity/Object/Continuant/Projection
  - Entity/Object/Continuant/Package
  - Entity/Aspect/Engineering/Traceability
version: 38
updated_at: 2026-10-29 14:16:32 +0400
relations:
  method_for:
  - CA-R-806
  - CA-R-1246
  - CA-R-1437
  - CA-R-1472
atom_id: CA-M-120@38
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Implementation Method
---
## Summary

Compile the direct-relation registry

## Claim scope

direct-relation registry compilation.

## Claim

**to** compile the optional direct-relation registry Projection, the Generator **must** perform **all** of:

1. read each declared Relation Type from its governing R Claim(s). The Claim(s) must provide the canonical name and meaning; preserve any relevant inverse, derivation, or transitivity semantics when explicitly stated. report missing **or** conflicting defining Claims without inventing a name, meaning, direction, or derivation.
2. Keep governing Entity Definition constraints separate from descriptive Relation Type metadata. Preserve their endpoint classes, contexts, counts and permissions in the model; a known Type does not require a separate Rule record.

3. derive inverse navigation from the defining Type authority **without** independently authoring an inverse Relation fact. distinguish an independently authored Relation fact from the governing derivation authority and input facts under CA-R-1437; do **not** invent a direct source declaration for a computed result.
4. retain source traceability for the non-authoritative registry Projection. resolve cross-graph and authoritative-source endpoints against any applicable governing constraint contexts under CA-R-1472. cross-graph references **or** views **must not** admit a foreign Type natively **or** reclassify an external endpoint as a native node of the receiving graph.
