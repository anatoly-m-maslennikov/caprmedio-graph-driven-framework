---
atom_id: CA-E-634
ref_id: CA-E-634
container:
  scope_unit: CA-SU-17
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Governing Configuration
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
tier: 3
status: Active
version: 12
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-E-634-CONNECTOR_TOOLS-EVAL_CASE--verify-complete-configuration-reads.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-17_FEATURE_CONNECTOR_TOOLS/06_evaluation
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
author: Anatoly Maslennikov
---
# Summary

Verify complete configuration reads

## Scope

future conformance checks for CA-R-1942, CA-M-382, CA-D-631 **and** CA-O-218.

## Claim

Configuration Read passes **only** **when** independent source observations prove a complete faithful result, exact matching state evidence **and** no mutation. missing implementation **or** observations is unavailable evidence, **not** a pass.

## Details

1. use independently pinned Project Structure **and** Project Settings fixtures with unrelated tables, optional values **and** supported typed TOML values. Read **every** logical identity **without** a pre-known pin; compare complete source text, parsed values **and** state evidence against independent observations.
2. verify supplied exact pins **and** an available historical view. reject stale pins, missing history, ambiguous sources **and** a source change that prevents a coherent observation. do **not** accept a guessed latest source **or** mixed-source result.
3. reject unknown keys, wrong kinds, path-based identities, non-null query/delta, unresolved Project/source/schema bindings, denied full-source permission, malformed TOML, duplicate keys, schema-invalid values **and** backend failure. assert the exact declared common error **and** null unavailable data, **not** fabricated full-read success.
4. verify that Read does **not** call Query, Find **or** Modify, choose a schema, repair the source, mutate metadata/history **or** activate a runtime. compare source bytes **and** configuration state **before** **and** **after** successful **and** failed reads.
5. verify normal empty effects, truthful unexpected effect failure **and** `effect_uncertain` for unknown effects. test the same shared connector's separate Read **and** Modify bindings; Read permission is **not** write permission.

these are unexecuted test specifications. independent source acceptance does **not** establish live behavior.
