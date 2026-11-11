---
subjects:
  active: 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Evaluation/Type'
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Evaluation)
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Verification
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Evaluation/Type'
version: 21
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
atom_id: CA-R-1506
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1506-CORE_META_MODEL-RULE--separate-check-mechanism-labels-from-evaluation-atom-types.md
  source_atom_id: CA-R-1506
  source_atom_revision: 21
  source_sha256: f37d37820aed224f18a506f6ddac3b167d2542ea78a9154bca26f32868bb342b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Separate check mechanism labels from Evaluation Atom Types

## Claim scope

mechanism labels and admitted Type values for Evaluation Atoms.

## Claim

the mechanism labels `Test` **and** `Evaluation` **must** describe implementation mechanisms, **not** Type values under `Atom/Content Role: Evaluation/Type`. the governing Evaluation Atom **and** its realization **must not** acquire the same classification merely because their names overlap.

## Details

this distinction does **not** define another Content Role **or** close the admitted Evaluation Type domain. its separately governed Type values remain subject **to** the applicable Type authority.
