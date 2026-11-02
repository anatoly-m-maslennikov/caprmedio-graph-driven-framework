---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Actor'
  - Subject/Engineering/Carrier
version: 14
updated_at: 2026-10-24 00:51:05 +0400
relations:
  relates_to:
  - CA-R-1565
  - CA-D-283
  - CA-D-284
  - CA-D-651
  - CA-R-1569
atom_id: CA-D-457@14
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
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
