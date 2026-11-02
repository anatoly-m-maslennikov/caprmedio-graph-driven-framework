---
subjects:
  governs: Subject/Engineering/Carrier/File Carrier.Filename
  depends_on:
  - 'Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Demand.Target Scope Unit'
version: 18
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-D-287@18
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Serialize Demand Type and Producer Scope

## Scope

Demand Atom filenames.

## Claim

**every** Demand Atom filename **must** serialize its Type **and** Producer Scope as `DEMANDS_FROM-<PRODUCER_SCOPE>`.

## Details
