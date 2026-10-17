---
subjects:
  governs: "Atom/Content Role: Operations/Type"
  depends_on:
    ["Atom/Content Role: Operations/Type", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Atom/Content Role: Operations/Type: Actor", "Artifact Carrier"]
version: 8
updated_at: "2026-10-15 18:52:04 +0000"
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
  source_atom_revision: 8
  source_sha256: 472728f76d98649be92677d7cb8172fa5e8b7b771325d6065ec3891e800ceb67
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
