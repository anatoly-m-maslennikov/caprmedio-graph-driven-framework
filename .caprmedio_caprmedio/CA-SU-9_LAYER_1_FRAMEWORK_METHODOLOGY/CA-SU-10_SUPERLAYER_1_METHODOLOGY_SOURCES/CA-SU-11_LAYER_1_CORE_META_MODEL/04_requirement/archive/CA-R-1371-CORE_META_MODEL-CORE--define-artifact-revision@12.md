---
subjects:
  governs: "Entity/Continuant/Node/History/Revision"
  depends_on:
  - "Entity/Continuant/Node/History"
version: 12
updated_at: "2026-10-18 03:33:24 +0400"
relations: {}
atom_id: "CA-R-1371"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define Artifact Revision

## Scope

Preserved historical states of Artifacts.

## Claim

a Revision **means** a preserved historical state of an Artifact. it belongs to History; it is **not** a dependent property of the current Artifact. the preserved state **must not** be edited as though it were the current state.

## Details

A current Atom remains an Atom with its own Version Number and Updated At. Its accepted updates follow CA-R-1432 and CA-R-1788. An archived Atom itself represents the earlier Atom state; no additional Revision wrapper is required. This definition does not require a separate snapshot operation, Journal record, historical baseline or permission check. Journal records describe events, not Journal snapshots.

