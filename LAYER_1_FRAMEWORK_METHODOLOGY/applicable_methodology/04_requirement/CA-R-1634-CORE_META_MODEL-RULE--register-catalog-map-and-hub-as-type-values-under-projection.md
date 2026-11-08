---
atom_id: CA-R-1634
ref_id: CA-R-1634
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection.Form
  dependencies:
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ Projection.Form
  - CAPRMEDIO_MODEL <+ Projection/(.Form:=Catalog)
  - 'CAPRMEDIO_MODEL <+ Projection/(.Form:=Map)'
  - 'CAPRMEDIO_MODEL <+ Projection/(.Form:=Hub)'
  - CAPRMEDIO_MODEL <+ Atom.Content
tier: 2
status: Active
version: 45
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-1634-CORE_META_MODEL-RULE--register-catalog-map-and-hub-as-type-values-under-projection.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1634-CORE_META_MODEL-RULE--register-catalog-map-and-hub-as-type-values-under-projection.md
  source_atom_id: CA-R-1634
  source_atom_revision: 45
  source_sha256: 7bc1e0a29bb9ba64c275fc10754ee7e3c5e56a255c34e7c702b53ab369df4f4a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register Catalog, Map, and Hub as Type Values under Projection

## Claim

### Prose Claim


Projection Type values and derived terminology lists or vocabulary diagnostic indexes.


Catalog, Map, **and** Hub **must** be distinct Type values under Projection with no authority over linked Artifact Claims.

a derived terminology list **or** vocabulary diagnostic index **must** use Catalog as its Projection Type; its purpose **and** selected population do **not** admit another Type.
