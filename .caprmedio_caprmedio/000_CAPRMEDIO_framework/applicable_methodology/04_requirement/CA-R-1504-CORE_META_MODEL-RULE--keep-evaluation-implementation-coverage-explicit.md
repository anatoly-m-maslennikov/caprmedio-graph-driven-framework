---
atom_id: CA-R-1504
ref_id: CA-R-1504
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Verification <+ Coverage
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Package/Implementation
  - CAPRMEDIO_MODEL <+ Atom.Content
tier: 1
status: Active
version: 25
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1504-CORE_META_MODEL-RULE--keep-evaluation-implementation-coverage-explicit.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1504-CORE_META_MODEL-RULE--keep-evaluation-implementation-coverage-explicit.md
  source_atom_id: CA-R-1504
  source_atom_revision: 25
  source_sha256: 3e92191bf4d9e65fd372f4595c65bfcb91cc124d553427cc7dc52022f299e473
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Keep Evaluation implementation coverage explicit

## Claim

### Prose Claim


coverage between Evaluation Atoms and their implementation realizations.


coverage between Evaluation Atoms **and** their realizations **may** be many-to-many **only** with explicit attribution:

- **`=1`** Evaluation Atom **may** be realized by multiple distinct implementations.
- **`=1`** implementation **may** realize multiple Evaluation Atoms **only** **when** its result remains attributable **to** **every** covered Claim.

## Details

a shared implementation **must not** make its covered Claims **or** their result attribution implicit. this Claim governs coverage, **not** a new Carrier **or** a second implementation registry.
