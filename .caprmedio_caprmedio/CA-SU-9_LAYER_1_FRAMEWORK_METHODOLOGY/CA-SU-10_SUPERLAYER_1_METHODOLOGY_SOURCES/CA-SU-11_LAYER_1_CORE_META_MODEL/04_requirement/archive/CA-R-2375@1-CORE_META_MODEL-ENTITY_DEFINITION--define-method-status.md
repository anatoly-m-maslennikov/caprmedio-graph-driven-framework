---
atom_id: CA-R-2375@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Method.Status'
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Method Status

## Claim scope

Lifecycle status of a Method Atom.

## Claim

Method Status is the one-string lifecycle classification of a Method Atom; it inherits Draft, Active and Archived under the applicable status model, and the Core Method Status model admits exactly those values.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Method.Status[string]{1}
```

## Details

Source meaning: CA-R-1989, CA-R-655, CA-R-1397. Scope-specific constraints remain in their governing Rs.
