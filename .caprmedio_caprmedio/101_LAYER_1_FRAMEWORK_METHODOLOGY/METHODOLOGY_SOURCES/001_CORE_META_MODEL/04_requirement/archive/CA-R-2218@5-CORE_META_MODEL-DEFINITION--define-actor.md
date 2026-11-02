---
atom_id: CA-R-2218@5
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Continuant/Actor
version: 5
updated_at: 2026-10-29 09:06:21 +0400
relations: {}
tier: 1
---
## Summary

Define Actor

## Claim scope

Actor in the Subject model.

## Claim

An Actor is a participant that performs work, provides input or exercises authority in the project.

### Formal claim

```text
Actor.Name[string]{0..1}
```

## Semantics

Operator and AI Agent are existing Actor kinds. An Actor is who participates; an Atom describing the Actor and a Carrier representing that description are different things. This definition grants no permission or authority.
