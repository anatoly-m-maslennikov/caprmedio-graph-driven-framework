---
atom_id: CA-R-1578
ref_id: CA-R-1578
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Content
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)/(.Header.Form := Plan)'
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Label'
tier: 1
status: Active
version: 25
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1578-CORE_META_MODEL-RULE--define-hub-atom-as-a-derived-description.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1578-CORE_META_MODEL-DEFINITION--define-hub-atom-as-a-derived-description.md
  source_atom_id: CA-R-1578
  source_atom_revision: 25
  source_sha256: 33275c90ea456e5678e964dc08c4a4bc056b50ef5007d2adc4eeef974cfeb70f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Hub Atom as a derived description

## Claim

### Prose Claim


Hub Atom descriptions.


Hub Atom **means** a derived description of a Plan Atom with **`>0`** outgoing derived `CONTAINS` links to Plan Atoms; it does **not** introduce another Type, Subtype, stored classification, identity, **or** authority tier. contained Atoms retain their own Claims rather than becoming parts of the Hub Claim.
