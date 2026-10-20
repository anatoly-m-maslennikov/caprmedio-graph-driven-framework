---
subjects:
  governs: "Prepare Structural Change"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Project.Structure", "Entity/Node/Continuant/Scope Unit", "Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Goal", "Entity/Carrier"]
version: 9
updated_at: "2026-10-19 15:56:36 +0400"
relations:
  relates_to:
    - "CA-M-291"
    - "CA-R-926"
atom_id: "CA-O-012"
content_role: "Operations"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-012-PROJECT_CONFIGURATION-ACTION--prepare-structural-change.md
  source_atom_id: CA-O-012
  source_atom_revision: 9
  source_sha256: a46406c43c552c11dee98161a8a52a174d04774f00d3b9fb7897ac5f1ea7a5ff
  original_relations_sha256: 08dceb7951a19459d315b2a173b7f929ab36215f5b2a5295c1defac06f5086a7
---
# Summary

Prepare structural change

## Operation

Prepare Structural Change **means** the Action that produces one bounded change proposal against the exact current Project Structure state. the proposal identifies the requested creation, rename, reparenting, reorder, path rebinding, removal, **or** reconciliation; its expected declarations; affected references, Goals, descendants **and** Carriers; required source changes; validation conditions; **and** a recoverable cutover boundary. a rename **or** reparenting **must** account for incoming references **and** parent-owned Goals, rather than leaving them attached **to** a different unit. declaration removal **must not** imply Carrier deletion. an undeclared folder, missing folder, **or** missing Active Goal is an observation requiring an explicit disposition, **not** permission **to** invent, erase, **or** accept authority.

## Details
