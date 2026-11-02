---
atom_id: CA-R-2160@4
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
version: 4
updated_at: 2026-10-29 07:17:20 +0400
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Content.Claim Scope
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Object/Continuant/Governing Objects/Atom.Subjects
  - Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
relations: {}
---

# Summary

Define Atom Content Scope

## Scope

The applicability boundary of an Atom's role-specific Content.

## Claim

Content.Scope, called Content Scope, **means** the part of an Atom's Content
that states exactly which cases, parts or conditions that Content governs.
It qualifies the role-specific Claim, Operation, Concern, Objective or
Question/Analysis and its supporting content. It is not another Scope Unit
or the reference that assigns the Atom's Local or Target Scope Unit.

## Semantics

The logical property path is Atom.Content.Scope. Its physical representation
is governed by D; the name does not require another Carrier or a duplicate
metadata value. This replaces the old Substance Scope name without restoring
a generic Atom.Substance property.

Scope may be omitted for full applicability only when the content covers both
the whole governed Subject and the whole Local Scope Unit. Otherwise its exact
boundary must be explicit. Apply a more-specific Role/Type scope contract
where declared; do not invent a Local Scope Unit for an Operator-owned Goal.

## Details
