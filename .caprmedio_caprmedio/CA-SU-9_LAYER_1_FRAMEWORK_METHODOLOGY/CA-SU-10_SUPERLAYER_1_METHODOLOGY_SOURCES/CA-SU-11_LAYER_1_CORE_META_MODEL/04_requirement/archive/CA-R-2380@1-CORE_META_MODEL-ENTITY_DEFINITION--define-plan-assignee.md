---
atom_id: CA-R-2380@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Assignee'
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Plan Assignee

## Claim

Plan.Assignee means an optional local assignee override for Plan work; when it is absent, the applicable inherited or default assignment remains in force.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Assignee[string]{0..1}
```

## Details

Source meaning: CA-R-1338, CA-R-1584, CA-R-1585, CA-D-473. Scope-specific constraints remain in their governing Rs.
