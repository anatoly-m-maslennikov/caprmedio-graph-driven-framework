---
subjects:
  governs: "Implementation Binding"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Evaluation", "Implementation", "Entity/Node/Continuant/Atom.Substance"]
version: 8
updated_at: "2026-10-19 15:53:17 +0400"
relations: {}
atom_id: "CA-R-1504"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1504-CORE_META_MODEL-CORE-REQUIREMENT--keep-evaluation-implementation-coverage-explicit.md
  source_atom_id: CA-R-1504
  source_atom_revision: 8
  source_sha256: 9e851129faa46192a4a6f38fa3ee053de6ec6ad58f70e74b316d3fdd8124d23a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep Evaluation implementation coverage explicit

## Scope

coverage between Evaluation Atoms and their implementation realizations.

## Claim

coverage between Evaluation Atoms **and** their realizations **may** be many-to-many **only** with explicit attribution:

- **`=1`** Evaluation Atom **may** be realized by multiple distinct implementations.
- **`=1`** implementation **may** realize multiple Evaluation Atoms **only** **when** its result remains attributable **to** **every** covered Claim.

## Details

a shared implementation **must not** make its covered Claims **or** their result attribution implicit. this Claim governs coverage, **not** a new Carrier **or** a second implementation registry.
