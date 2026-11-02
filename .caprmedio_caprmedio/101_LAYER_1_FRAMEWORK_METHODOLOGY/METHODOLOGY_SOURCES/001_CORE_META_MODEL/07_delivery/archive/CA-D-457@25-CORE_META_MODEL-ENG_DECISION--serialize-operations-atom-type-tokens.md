---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - Entity/Carrier
version: 25
updated_at: 2026-10-29 10:13:51 +0400
relations: {}
atom_id: CA-D-457@25
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Decision
---
## Summary

Serialize Operations Atom Type tokens

## Claim scope

Operations Atom File Carriers and their Type filename tokens.

## Claim

an Operations Atom File Carrier **must** serialize its Type using this filename-token mapping:

| Operations Atom Type | Filename token |
|---|---|
| Action | `ACTION` |
| Workflow | `WORKFLOW` |
| Step | `STEP` |
