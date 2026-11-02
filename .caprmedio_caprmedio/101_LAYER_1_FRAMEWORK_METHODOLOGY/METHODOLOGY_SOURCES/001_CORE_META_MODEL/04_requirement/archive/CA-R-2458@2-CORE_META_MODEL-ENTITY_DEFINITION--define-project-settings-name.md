---
atom_id: CA-R-2458@2
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
version: 2
updated_at: 2026-10-30 14:19:42 +0400
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings.Name
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Actor/Operator
relations: {}
---
## Summary

Define Project Settings Name

## Claim scope

The Name property in Project Settings.

## Claim

Project.Settings.Name **means** the required Operator-selected Project name
initialization input in Project Settings.

### Formal claim

```text
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings.Name[string]{1}
```

## Semantics

Name is one child Property of Project.Settings. The parent Project Settings
definition owns its Property group and its initialization context;
this definition owns only the Name Property. The existing delivery storage key
`project.name` remains unchanged. This definition does not prescribe that
key's encoding, Case, Format, Carrier, identifier, or lifecycle.

## Details

This is a fresh role-only Draft because the new Summary and complete target
differ from Current CA-R-2414. It allocates no canonical Requirement identity
and does not retire the older field definition. It does not automatically
introduce a lexical Term or a Method Term Definition.

### Source pins

- [Current CA-R-2414@1 — Project Settings Project Name](../CA-R-2414-CORE_META_MODEL-ENTITY_DEFINITION--define-project-settings-project-name.md), SHA-256 `462e610a4808574eec843bc8bfd61a024933a604ff34c49ceedd81317da85a54`.
- [Pending parent CA-R-1738@40 — Project Settings](CA-R-1738@40-draft-CORE_META_MODEL--define-project-settings.md), SHA-256 `38829815e44ed95f5c7831301b669c594b1ad1e5fbfca039e74700e3be78df32`.

The Current comparison source remains unchanged; the pending parent is pinned at its coordinated Draft state. This Draft performs no promotion, retirement,
storage-key rename, implementation, or runtime change.
