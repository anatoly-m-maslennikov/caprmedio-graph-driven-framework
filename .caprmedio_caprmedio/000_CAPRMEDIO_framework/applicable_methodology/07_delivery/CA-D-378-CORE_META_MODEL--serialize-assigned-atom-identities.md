---
subjects:
  governs: "Entity/Continuant/Object/Atom.ID"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role", "Entity/Continuant/Object/Project", "Entity/Continuant/Object/Atom/Content Role: Plan.ID"]
version: 13
updated_at: "2026-10-16 12:09:22 +0000"
relations: {}
atom_id: "CA-D-378"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-378-CORE_META_MODEL--serialize-assigned-atom-identities.md
  source_atom_id: CA-D-378
  source_atom_revision: 13
  source_sha256: 6a6f9b3658df81fab494845509c977f497a4d86d2dd72b8f0781340635d134d6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Assigned Atom Identities

## Scope

assigned Atom IDs.

## Claim

**every** assigned Atom ID **must** begin with the registered uppercase Project identity prefix. the Project-owned Atom ID encoding **must** match `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-<GLOBAL_NUMBER_WITHIN_CONTENT_ROLE>`. the Atom Content Role Identity Letter **must** be **in** (Concern: C, Analysis: A, Plan: P, Requirement: R, Method: M, Evaluation: E, Delivery: D, Implementation: I, Operations: O). a `<PROJECT_PREFIX>-P` Identifier **must** identify a Plan Atom, including one labeled Epic, **and** **must not** identify a separate non-Atom collection.

## Details
