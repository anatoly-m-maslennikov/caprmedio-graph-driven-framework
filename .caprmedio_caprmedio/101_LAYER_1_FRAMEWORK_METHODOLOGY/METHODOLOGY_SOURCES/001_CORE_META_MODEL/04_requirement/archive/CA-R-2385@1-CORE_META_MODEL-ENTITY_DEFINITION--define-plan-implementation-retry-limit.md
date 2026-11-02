---
atom_id: CA-R-2385@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Implementation Retry Limit'
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Plan Implementation Retry Limit

## Claim

Plan.Implementation Retry Limit means an optional explicit retry-limit override participating in effective retry-limit resolution for a Plan.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Implementation Retry Limit[int]{0..1}
```

## Details

Source meaning: CA-R-1338, CA-R-1489. Scope-specific constraints remain in their governing Rs.
