---
atom_id: CA-D-507
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 16
updated_at: 2026-11-02 00:18:22 +0400
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity
  - CAPRMEDIO <+ MODEL <+ Carrier.Format
  - CAPRMEDIO <+ MODEL <+ Carrier/File.Extension
relations: {}
tier: 1
role: Delivery
form: Decision
---
## Summary

Separate Entity identity from Carrier format

## Claim scope

changes limited **to** Carrier Format **or** File Carrier Extension.

## Claim

a change **to** Carrier Format **or** File Carrier Extension alone **must not** establish **or** change Entity identity.
