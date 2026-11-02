---
atom_id: CA-D-559
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Journal
  passive:
  - Entity/Aspect/Engineering/Data Handling/Output Publication
  - Projection
  - Journal
  - Carrier
version: 17
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Delivery
form: Decision
---
## Summary

Deliver runtime Journals to configured sinks

## Claim scope

technical and business runtime Journal Carriers.

## Claim

runtime technical **and** business Journals **may** be delivered **to** an explicitly configured local database, remote database, **or** governed logging sink. these Carriers **need not** reside under `.caprmedio_<project_name>/_journal/` **or** `.caprmedio_runtime/`.

## Details

Journal classification and recorded-history authority are independent of storage technology. The configuration identifies the intended sink; applicable production logging policy remains in force. The shared Project-control Work Journal and persistent view Projections retain their separate _journal and _projection locations. Runtime cleanup and sink migration must preserve accepted Journal history; this Delivery does not authorize history deletion or change retention policy.
