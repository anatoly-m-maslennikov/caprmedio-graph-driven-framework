---
atom_id: CA-R-2402@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit.Parent
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Scope Unit Parent

## Claim

Scope Unit.Parent means the optional reference to the immediate containing Scope Unit; the root Project has no Parent.

### Formal claim

```text
Entity/Object/Continuant/Structural Unit/Scope Unit.Parent[string]{0..1}
```

## Details

Source meaning: CA-R-1757, CA-R-1658. Scope-specific constraints remain in their governing Rs.
