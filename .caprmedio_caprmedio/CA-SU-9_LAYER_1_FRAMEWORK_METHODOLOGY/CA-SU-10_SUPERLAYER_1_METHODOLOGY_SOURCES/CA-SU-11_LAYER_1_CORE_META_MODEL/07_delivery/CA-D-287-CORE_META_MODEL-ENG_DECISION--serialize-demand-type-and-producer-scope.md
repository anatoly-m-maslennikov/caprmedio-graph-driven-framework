---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File.Filename
  passive:
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Demand.Target Scope Unit'
version: 28
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-287
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize Demand Type and Producer Scope

## Claim scope

Demand Atom filenames.

## Claim

**every** Demand Atom filename **must** serialize its Type **and** Producer Scope as `DEMANDS_FROM-<PRODUCER_SCOPE>`.
