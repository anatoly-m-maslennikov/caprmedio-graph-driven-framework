---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Demand"
  depends_on:
    ["Consumer Goal", "Producer Result"]
version: 20
updated_at: "2026-10-19 15:54:30 +0400"
relations:
  child_of:
    - CA-R-932
atom_id: "CA-R-933"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-933-CORE_META_MODEL-CORE-REQUIREMENT--restrict-demand-to-one-depended-on-result.md
  source_atom_id: CA-R-933
  source_atom_revision: 20
  source_sha256: 1463ca3bd3210bd9a6ffcafda85221d4ad1aa584b920f8aa648113cbabd61929
  original_relations_sha256: 986ab56d61737841b77ed4fc4f1a391a0c8ad370d896e576cf2be7bdd2bdf459
---
# Summary
Restrict Demand to one depended-on result

## Scope

Demand Atoms.

## Claim

**every** Demand Atom **must** constrain **`=1`** Producer result on which its Consumer's accepted Goal depends.

## Details
