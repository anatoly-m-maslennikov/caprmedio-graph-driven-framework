---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Content Role
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Term//Property
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Object/Continuant/Governing Objects
version: 21
updated_at: 2026-10-30 07:00:34 +0400
relations: {}
atom_id: CA-R-1531@21-draft
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define the Content Role Property

## Claim scope

The Content Role classification of Atoms.

## Claim

Content Role is the classification parameter of an Atom that identifies the primary contribution of its Claim. The parameter has an allowed value, such as Requirement or Plan; it is not a separate entity kind.

Within `Entity/Object/Continuant/Governing Objects`, `Atom.Content Role` names the Atom's Content Role Property. `Atom/(.Content Role: Requirement)` names the narrower Atom kind qualified by that Property and its independently admitted value. That narrower kind inherits Atom's applicable features and constraints. The full canonical Subject uses the Entity root and complete path.

### Formal claim

```text
Atom.Content Role[string]{1}
```

## Semantics

A Subject may name a thing or a topic. Having a Subject does not make the named topic a separate entity kind. Defining Content Role therefore does not introduce an intermediate Entity kind between Atom and its role-qualified kinds; the Property remains directly addressable.

The stored Content Role value classifies a particular Atom. The Subject notation describes the classification axis or a role-qualified Atom kind; it does not assign a value to a particular Atom instance.

## Details

The allowed values and the requirement for one value per Atom remain governed by CA-R-1283 and CA-R-740. This definition does not change those rules.
