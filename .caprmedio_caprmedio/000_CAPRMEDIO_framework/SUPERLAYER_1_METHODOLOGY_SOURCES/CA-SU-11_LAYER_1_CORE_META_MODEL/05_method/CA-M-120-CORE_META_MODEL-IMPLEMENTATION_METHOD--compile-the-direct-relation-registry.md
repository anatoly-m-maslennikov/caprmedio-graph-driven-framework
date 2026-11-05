---
atom_id: CA-M-120
ref_id: CA-M-120
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection/(.Form:=Direct Relation Registry)
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Projection/(.Form:=Applicable Methodology)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ Package
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Traceability
tier: 3
relations:
  method_for:
  - CA-R-806
  - CA-R-1246
  - CA-R-1437
  - CA-R-1472
status: Active
version: 43
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-M-120-CORE_META_MODEL-IMPLEMENTATION_METHOD--compile-the-direct-relation-registry.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Compile the direct-relation registry

## Claim

### Prose Claim


direct-relation registry compilation.


**to** compile the optional direct-relation registry Projection, the Generator **must** perform **all** of:

1. read each declared Relation Type from its governing R Claim(s). The Claim(s) must provide the canonical name and meaning; preserve any relevant inverse, derivation, or transitivity semantics when explicitly stated. report missing **or** conflicting defining Claims without inventing a name, meaning, direction, or derivation.
2. Keep governing Entity Definition constraints separate from descriptive Relation Type metadata. Preserve their endpoint classes, contexts, counts and permissions in the model; a known Type does not require a separate Rule record.

3. derive inverse navigation from the defining Type authority **without** independently authoring an inverse Relation fact. distinguish an independently authored Relation fact from the governing derivation authority and input facts under CA-R-1437; do **not** invent a direct source declaration for a computed result.
4. retain source traceability for the non-authoritative registry Projection. resolve cross-graph and authoritative-source endpoints against any applicable governing constraint contexts under CA-R-1472. cross-graph references **or** views **must not** admit a foreign Type natively **or** reclassify an external endpoint as a native node of the receiving graph.
