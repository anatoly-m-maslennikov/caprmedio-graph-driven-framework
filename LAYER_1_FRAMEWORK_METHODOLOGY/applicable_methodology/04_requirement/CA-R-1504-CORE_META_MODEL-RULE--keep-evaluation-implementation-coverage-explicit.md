---
subjects:
  active: Aspects <+ Engineering <+ Verification <+ Coverage
  passive:
  - Atom/(.Role := Evaluation)
  - Entity/Object/Continuant/Package/Project Implementation
  - Atom.Content
version: 25
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
atom_id: CA-R-1504
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1504-CORE_META_MODEL-RULE--keep-evaluation-implementation-coverage-explicit.md
  source_atom_id: CA-R-1504
  source_atom_revision: 25
  source_sha256: 9390ca2e79803a8ad52ed01b7e349e05ff9fca8c56ff8c955c43827f71c7c556
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Keep Evaluation implementation coverage explicit

## Claim scope

coverage between Evaluation Atoms and their implementation realizations.

## Claim

coverage between Evaluation Atoms **and** their realizations **may** be many-to-many **only** with explicit attribution:

- **`=1`** Evaluation Atom **may** be realized by multiple distinct implementations.
- **`=1`** implementation **may** realize multiple Evaluation Atoms **only** **when** its result remains attributable **to** **every** covered Claim.

## Details

a shared implementation **must not** make its covered Claims **or** their result attribution implicit. this Claim governs coverage, **not** a new Carrier **or** a second implementation registry.
