---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern'
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - Entity/Object/Continuant/Governing Objects/Atom.Content
version: 27
updated_at: 2026-10-29 10:13:48 +0400
relations: {}
atom_id: CA-R-1336@27
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Concern Content Role

## Claim scope

Atom Claims that identify questions, conflicts, **or** problems.

## Claim

Concern Priority classifies handling priority as High, Medium or Low. Selection and conflict-handling policies remain in their governing Claims; this declaration introduces no automatic conflict winner.

Concern **means** the Content Role of an Atom Claim that identifies one question, conflict, **or** problem.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern.Priority[string]{1}
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern.Priority: High
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern.Priority: Medium
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern.Priority: Low
```
