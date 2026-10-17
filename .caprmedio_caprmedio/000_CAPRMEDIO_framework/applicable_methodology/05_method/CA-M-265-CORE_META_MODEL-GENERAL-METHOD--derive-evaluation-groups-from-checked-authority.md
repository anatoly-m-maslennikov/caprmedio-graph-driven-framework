---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Evaluation"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role", "Entity/Continuant/Object/Relation/Type: evaluation_for"]
version: 12
updated_at: "2026-10-16 12:09:03 +0000"
relations: {}
atom_id: "CA-M-265"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/05_method/CA-M-265-CORE_META_MODEL-GENERAL-METHOD--derive-evaluation-groups-from-checked-authority.md
  source_atom_id: CA-M-265
  source_atom_revision: 12
  source_sha256: ae6537ce21d40d851898851e145c0ec337e92586b6c8b047d3ffd4bb2e8cd221
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Derive evaluation groups from checked authority

## Scope

derivation of Er, Em, and Ed groups from checked authority.

## Claim

**to** derive Er, Em, **and** Ed groups, resolve the Content Role of **every** `evaluation_for` target **and** include the Evaluation **in** the corresponding Requirement, Method, **or** Delivery group; **if** targets span multiple roles, **then** include it **in** **every** applicable group **without** assigning a new Content Role **or** persisting a duplicate target-role field. absence of individual targets on a Core **or** General Evaluation policy admitted by CA-R-1018-CORE_META_MODEL-CORE-REQUIREMENT--register-evaluation-targets **must not** require an invented classification.

## Details
