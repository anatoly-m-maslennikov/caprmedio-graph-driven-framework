---
atom_id: CA-M-295
ref_id: CA-M-295
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run.Implementation Retry Limit
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)/(.Header.Form := Plan)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Implementation Retry Limit'
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Governing Configuration
  - CAPRMEDIO_MODEL <+ Carrier/File
tier: 5
relations:
  child_of:
  - CA-R-1489
  depends_on:
  - CA-M-279
status: Active
version: 32
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-M-295-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-implementation-retry-limits-by-source-precedence.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-295-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-implementation-retry-limits-by-source-precedence.md
  source_atom_id: CA-M-295
  source_atom_revision: 32
  source_sha256: e808ae02e8bfbbd893269bd2b4dd09b0c4bec7db85dc170ca510b75589d2710d
  original_relations_sha256: af9265e195c1136864429621ff445e736ff343e267c5ed7ec1b4671a862e6364
---
## Summary

Resolve implementation retry limits by source precedence

## Claim

### Prose Claim


an effective Implementation Retry Limit resolved from direct Operator input, a Plan, the nearest Hub, Framework Instance Settings, **or** Default Settings.


**to** resolve an effective Implementation Retry Limit, select the first applicable explicit source **in** this precedence:

1. direct Operator input for the current execution context.
2. the current Plan's explicit Implementation Retry Limit.
3. the nearest Hub with an explicit limit, walking `IS_CONTAINED_BY` from nearest **to** farthest **and** reading its own current Plan File Carrier under CA-D-447-CORE_META_MODEL-DELIVERY--serialize-the-implementation-retry-limit-setting.
4. Framework Instance Settings, resolving an omitted instance parameter through Default Settings under CA-M-279-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-missing-framework-parameters-from-default-settings.

### resolution constraints

- an omitted optional retry override preserves inheritance; another explicit field does **not** stop this lookup. a missing mandatory Plan file is invalid, **not** an inherited-setting selection.
- determine presence, **not** truthiness: **`=0`** is an explicit limit.
- an invalid **or** ambiguous reached source requires Operator disposition **without** silent fallback; an absent effective value stops the affected retry decision.
- direct Operator input applies **only** within its stated context.
- do **not** copy inherited values **or** create separate Objective/settings files. retain explicit overrides even **when** equal **to** the inherited value.
- use the same Plan identity for a Hub's file **and** folder.
- resolution does **not** reset the consumed retry count governed by CA-O-024-CORE_META_MODEL-ACTION--control-implementation-retries.
