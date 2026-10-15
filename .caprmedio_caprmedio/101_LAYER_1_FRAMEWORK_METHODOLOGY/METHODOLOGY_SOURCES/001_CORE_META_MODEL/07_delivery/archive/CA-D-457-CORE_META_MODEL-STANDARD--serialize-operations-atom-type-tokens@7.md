---
subjects:
  governs: "Atom/Content Role: Operations/Type"
  depends_on:
    ["Atom/Content Role: Operations/Type", "Atom/Content Role: Operations/Type: Action", "Atom/Content Role: Operations/Type: Workflow", "Atom/Content Role: Operations/Type: Step", "Atom/Content Role: Operations/Type: Actor", "Artifact Carrier"]
version: 7
updated_at: "2026-10-15 12:18:40 +0000"
relations: {"relates_to": ["CA-R-1565", "CA-D-283", "CA-D-284", "CA-D-285", "CA-R-1569"]}
atom_id: "CA-D-457"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
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
