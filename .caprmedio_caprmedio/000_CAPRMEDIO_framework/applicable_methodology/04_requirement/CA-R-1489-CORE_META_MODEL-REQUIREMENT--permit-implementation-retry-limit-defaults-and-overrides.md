---
version: 8
updated_at: "2026-10-15 18:43:38 +0000"
relations:
  child_of:
    - CA-R-1488
subjects:
  governs: "Implementation Retry Limit"
  depends_on:
    ["Implementation Retry Limit", "Entity/Continuant/Actor/Type: Operator", "Atom/Content Role: Plan/Type: Plan", "Entity/Continuant/Object/Project.Framework Settings", "Property"]
atom_id: "CA-R-1489"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1489-CORE_META_MODEL-REQUIREMENT--permit-implementation-retry-limit-defaults-and-overrides.md
  source_atom_id: CA-R-1489
  source_atom_revision: 8
  source_sha256: c625882fe238dd5f66165f6443263590712e2a5bda3bd84f0fd6a230fc5d1bd4
  original_relations_sha256: 3b6a41bc9d7e0c44152670010734eb1413010930f791c90c87f9676ac2766dfe
---
# Summary

Permit implementation retry-limit defaults and overrides

## Scope

effective Implementation Retry Limit selection for a Plan or Framework Instance Settings.

## Claim

an Implementation Retry Limit **must** take its effective value from applicable direct Operator input, an explicit Property on the current Plan, the nearest enclosing Hub Plan with an explicit Property, **or** Framework Instance Settings.

- a Plan **may** have **<=1** explicit Implementation Retry Limit override, regardless of Label.
- an omitted override **must** preserve inheritance **without** copying the inherited value into that Plan.
- a retry decision **must** have **=1** valid effective limit; missing **or** ambiguous authority requires Operator disposition **before** another retry.

## Details
