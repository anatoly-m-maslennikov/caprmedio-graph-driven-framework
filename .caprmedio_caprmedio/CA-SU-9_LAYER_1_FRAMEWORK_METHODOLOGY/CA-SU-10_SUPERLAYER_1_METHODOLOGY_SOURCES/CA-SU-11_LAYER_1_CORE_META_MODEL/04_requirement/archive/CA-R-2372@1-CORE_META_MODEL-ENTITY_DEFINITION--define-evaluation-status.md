---
atom_id: CA-R-2372@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Evaluation.Status'
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Evaluation Status

## Claim scope

Lifecycle status of an Evaluation Atom.

## Claim

Evaluation Status is the one-string lifecycle classification of an Evaluation Atom; it inherits Draft, Active and Archived under the applicable status model, with the Core Evaluation Status model admitting exactly those values.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Evaluation.Status[string]{1}
```

## Details

Source meaning: CA-R-1989, CA-R-655, CA-R-1398. Scope-specific constraints remain in their governing Rs.
