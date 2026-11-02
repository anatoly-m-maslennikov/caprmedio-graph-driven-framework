---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Work Sequence Number'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan'
version: 36
updated_at: 2026-10-29 10:13:50 +0400
relations: {}
atom_id: CA-R-991@36
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Work Sequence Number

## Claim scope

Work Sequence Numbers for Plans directly contained by one Plan or sharing one top-level Plan container.

## Claim

The optional explicit ordinal does not determine execution order; when supplied, its existing positive and local-uniqueness rules remain applicable.

a Work Sequence Number **means** a mutable ordinal navigation value for a Plan among Plans directly contained by the same Plan **or** sharing a top-level Plan container; it does **not** establish execution order.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Work Sequence Number[int]{0..1}
```
