---
subjects:
  governs: Entity/Carrier/File.Filename
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Demand.Target Scope Unit'
version: 27
updated_at: 2026-10-29 10:13:50 +0400
relations: {}
atom_id: CA-D-287@27
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Decision
---
## Summary

Serialize Demand Type and Producer Scope

## Claim scope

Demand Atom filenames.

## Claim

**every** Demand Atom filename **must** serialize its Type **and** Producer Scope as `DEMANDS_FROM-<PRODUCER_SCOPE>`.
