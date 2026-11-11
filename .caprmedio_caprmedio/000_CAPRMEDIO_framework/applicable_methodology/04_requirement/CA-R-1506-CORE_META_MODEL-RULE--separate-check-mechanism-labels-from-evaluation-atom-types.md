---
atom_id: CA-R-1506
ref_id: CA-R-1506
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation).Header.Form'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Quality <+ Verification"
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation).Header.Form'
tier: 1
status: Active
version: 21
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1506-CORE_META_MODEL-RULE--separate-check-mechanism-labels-from-evaluation-atom-types.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1506-CORE_META_MODEL-RULE--separate-check-mechanism-labels-from-evaluation-atom-types.md
  source_atom_id: CA-R-1506
  source_atom_revision: 21
  source_sha256: a3343b98851dfb1edab2c3d034993124784bbbbe6c8d4db6c0876524835da46c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Separate check mechanism labels from Evaluation Atom Types

## Claim

### Prose Claim


mechanism labels and admitted Type values for Evaluation Atoms.


the mechanism labels `Test` **and** `Evaluation` **must** describe implementation mechanisms, **not** Type values under `Atom/(.Header.Role := Evaluation).Header.Form`. the governing Evaluation Atom **and** its realization **must not** acquire the same classification merely because their names overlap.

## Details

this distinction does **not** define another Content Role **or** close the admitted Evaluation Type domain. its separately governed Type values remain subject **to** the applicable Type authority.
