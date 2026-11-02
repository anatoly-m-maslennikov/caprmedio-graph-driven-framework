---
atom_id: CA-R-2376@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations.Status'
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Operations Status

## Claim scope

Lifecycle status of Operations Atoms with Type Workflow, Step or Action.

## Claim

Operations Status is the one-string lifecycle classification of an Operations Atom with Type Workflow, Step or Action. The Core values are Draft, Active and Archived; this status is not a run outcome, receipt, retry state, result or completion state.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations.Status[string]{1}
```

## Details

Source meaning: CA-R-1989, CA-R-655, CA-R-1874. Scope-specific constraints remain in their governing Rs.
