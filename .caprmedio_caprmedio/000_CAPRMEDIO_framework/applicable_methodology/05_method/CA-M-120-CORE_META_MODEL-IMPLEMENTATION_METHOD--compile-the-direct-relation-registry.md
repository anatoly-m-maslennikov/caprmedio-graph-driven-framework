---
subjects:
  active: Projection/(.Form:=Direct Relation Registry)
  passive:
  - CFEL <+ Relation
  - Entity
  - Projection/(.Form:=Applicable Methodology)
  - Atom/(.Role := Requirement)
  - Projection
  - Package
  - Aspects <+ Engineering <+ Traceability
version: 43
updated_at: 2026-11-02 18:35:20 +0400
relations:
  method_for:
  - CA-R-806
  - CA-R-1246
  - CA-R-1437
  - CA-R-1472
atom_id: CA-M-120
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-120-CORE_META_MODEL-IMPLEMENTATION_METHOD--compile-the-direct-relation-registry.md
  source_atom_id: CA-M-120
  source_atom_revision: 43
  source_sha256: 3ba6847a3e1faff5ac1eb81521ebc1d4b48814ad5af77626e458daa6b7324aaa
  original_relations_sha256: 68a2c39318c77d63e9da6b3745d4ed6a600564f503add663a28df99ecce4edd3
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
