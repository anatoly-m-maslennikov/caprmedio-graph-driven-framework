---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Content.Details'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan'
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Object/Continuant/Governing Objects/Atom
version: 23
updated_at: 2026-10-29 10:13:49 +0400
relations: {}
atom_id: CA-R-1586@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Plan Details

## Claim scope

Plan Details within the Plan Objective, its restrictions, **and** target.

## Claim

Plan Details **means** supporting information within the Plan Objective, its restrictions, **and** target, **without** additional intended work **or** an independent outcome. the Plan's Definition of Done tests that same Objective; its presence inside Details does **not** introduce another Claim.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Content.Details[string]{0..1}
```
