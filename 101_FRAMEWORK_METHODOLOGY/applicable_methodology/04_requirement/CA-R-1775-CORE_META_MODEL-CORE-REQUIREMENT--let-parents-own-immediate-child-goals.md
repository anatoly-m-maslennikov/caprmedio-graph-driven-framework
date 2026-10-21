---
version: 18
updated_at: "2026-10-19 15:54:04 +0400"
relations:
  child_of:
    - CA-M-001
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Goal"
  depends_on:
    ["Entity/Node/Continuant/Scope Unit", "Entity/Node/Continuant/Atom", "Owned Atoms", "Targeting Atoms"]
atom_id: "CA-R-1775"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1775-CORE_META_MODEL-CORE-REQUIREMENT--let-parents-own-immediate-child-goals.md
  source_atom_id: CA-R-1775
  source_atom_revision: 18
  source_sha256: 898f5a6794485364674bd4a03aac2305ec42f621e3887140ef2a0b68cc9056f4
  original_relations_sha256: 2f95e55e3d0a844c858c40eeab601ef29e88bfb9f5c8b9fd17a85ccd2af662a7
---
# Summary

Let Parents Own Immediate Child Goals

## Scope

parent Scope Units and their immediate child Scope Units.

## Claim

**every** parent Scope Unit **must** own the Goal Atoms for its immediate child Scope Units under CA-R-926; those Goal Atoms belong **to** the parent's Owned Atoms **and** the child's Targeting Atoms **without** transferring their ownership.

## Details
