---
subjects:
  governs: "Entity/Continuant/Node/Atom.ID"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role", "Entity/Continuant/Node/Project", "Entity/Continuant/Node/Atom/Content Role: Plan.ID"]
version: 14
updated_at: "2026-10-18 03:34:43 +0400"
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
  source_atom_revision: 14
  source_sha256: 269c4e94fa6b29adeef0b05cb22d21ac4699eae4dd7aae9ca56b65d647987ea8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Assigned Atom Identities

## Scope

assigned Atom IDs.

## Claim

**every** assigned Atom ID **must** begin with the registered uppercase Project identity prefix. the Project-owned Atom ID encoding **must** match `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-<GLOBAL_NUMBER_WITHIN_CONTENT_ROLE>`. the Atom Content Role Identity Letter **must** be **in** (Concern: C, Analysis: A, Plan: P, Requirement: R, Method: M, Evaluation: E, Delivery: D, Implementation: I, Operations: O). a `<PROJECT_PREFIX>-P` Identifier **must** identify a Plan Atom, including one labeled Epic, **and** **must not** identify a separate non-Atom collection.

## Details
