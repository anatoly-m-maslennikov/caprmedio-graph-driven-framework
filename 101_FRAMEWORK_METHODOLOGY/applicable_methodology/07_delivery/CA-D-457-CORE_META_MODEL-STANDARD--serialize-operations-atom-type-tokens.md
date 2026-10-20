---
subjects:
  governs: "Atom/Content Role: Operations/Type"
  depends_on:
    ["Atom/Content Role: Operations/Type", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Atom/Content Role: Operations/Type: Actor", "Artifact Carrier"]
version: 9
updated_at: "2026-10-19 15:55:50 +0400"
relations: {"relates_to": ["CA-R-1565", "CA-D-283", "CA-D-284", "CA-D-285", "CA-R-1569"]}
atom_id: "CA-D-457"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-457-CORE_META_MODEL-STANDARD--serialize-operations-atom-type-tokens.md
  source_atom_id: CA-D-457
  source_atom_revision: 9
  source_sha256: 5bf9fe349894a20ab62c7b888a0ffcbc3860ed46e4cbab1c983ac640374f752c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Operations Atom Type tokens

## Scope

Operations Atom File Carriers and their Type filename tokens.

## Claim

an Operations Atom File Carrier **must** serialize its Type using this filename-token mapping:

| Operations Atom Type | Filename token |
|---|---|
| Action | `ACTION` |
| Workflow | `WORKFLOW` |
| Step | `STEP` |
| Actor | `ACTOR` |

## Details
