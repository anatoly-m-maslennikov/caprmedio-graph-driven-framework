---
atom_id: CA-R-2368@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery.Content.Claim'
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Delivery Content Claim

## Claim scope

The primary Delivery contribution carried by a Delivery Atom.

## Claim

Delivery Content Claim is the one direct prose Claim carrying one complete scoped Delivery contribution under the Delivery Atom role and Type. It names the governed Entity or Carrier and states the relevant representation, storage, placement or lifecycle constraint without redefining separately governed authority.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery.Content.Claim[string]{1}
```

## Details

Source meaning: CA-R-1269, CA-M-313. Scope-specific constraints remain in their governing Rs.
