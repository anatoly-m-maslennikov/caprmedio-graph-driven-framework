---
subjects:
  active: Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
  passive:
  - 'Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Plan)/(.Type: Plan)'
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - Term//Property
  - Entity/Object/Continuant/Actor/AI Agent
version: 29
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-R-1428
atom_id: CA-M-271
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-271-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-confidence-thresholds-by-source-precedence.md
  source_atom_id: CA-M-271
  source_atom_revision: 29
  source_sha256: 8f365c2803346143e92d76b4be3732bea149c3436ed574a23692ad708f10045c
  original_relations_sha256: 57a2d15d1c076f7de9a5434f2b010760681bcef356d85d254dae9d1bb3d233dd
---
## Summary
Resolve confidence thresholds by source precedence

## Claim scope
resolution of a Confidence Threshold.

## Claim
**to** resolve an effective Confidence Threshold, select the first applicable explicit source **in** this precedence:

1. direct Operator input for the current decision context.
2. an explicit value on the current Plan.
3. the nearest Hub with an explicit value, walking `IS_CONTAINED_BY` from nearest **to** farthest; read its own current Plan File Carrier under `CA-D-472-CORE_META_MODEL-DELIVERY--serialize-explicit-plan-confidence-overrides`, **not** a separate Objective targeting a folder.
4. the Framework Instance Settings default.

### resolution constraints

- an omitted optional override preserves inheritance; another explicit field does **not** stop lookup for the omitted field. a missing mandatory Plan file is invalid, **not** an inherited-setting selection.
- use current Plan Revisions, **not** historical Carrier copies **or** unrelated nearby files; a Label is **not** an override source.
- **if** a reached source is invalid **or** ambiguous, **or** no source supplies a value, request Operator disposition **before** the affected autonomous action; do **not** invent a value **or** silently fall through past invalid authority.
- direct Operator input applies **only** within its stated context.
- do **not** copy inherited values into Plan overrides. preserve an explicit selection even **when** it **`=`** the inherited value; a later upstream change **must not** overwrite it.
- this resolution **must not** create another Atom, settings file, **or** execution permission.
