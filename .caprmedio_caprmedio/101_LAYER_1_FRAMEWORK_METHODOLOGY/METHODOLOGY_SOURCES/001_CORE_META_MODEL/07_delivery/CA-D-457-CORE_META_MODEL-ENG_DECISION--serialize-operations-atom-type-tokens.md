---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - Subject/CAPRMEDIO/Carrier
version: 22
updated_at: 2026-10-27 19:59:25 +0400
relations: {}
atom_id: CA-D-457
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
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

## Details
