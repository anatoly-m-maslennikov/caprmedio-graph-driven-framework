---
atom_id: CA-R-2365@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern.Priority'
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Concern Priority

## Claim scope

Handling priority carried by a Concern Atom.

## Claim

Concern Priority is exactly one handling-priority value—High, Medium or Low—for a Concern. Selection and conflict handling remain separate governed policy; the Delivery carrier stores lowercase high, medium or low and never virtual highest.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern.Priority[string]{1}
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern.Priority: High
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern.Priority: Medium
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern.Priority: Low
```

## Details

Source meaning: CA-R-1336, CA-R-1629, CA-E-623, CA-D-386. Scope-specific constraints remain in their governing Rs.
