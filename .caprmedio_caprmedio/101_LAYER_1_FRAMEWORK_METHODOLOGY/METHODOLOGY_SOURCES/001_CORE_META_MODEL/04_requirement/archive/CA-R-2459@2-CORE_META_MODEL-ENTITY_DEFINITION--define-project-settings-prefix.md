---
atom_id: CA-R-2459@2
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
version: 2
updated_at: 2026-10-30 14:21:10 +0400
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings.Prefix
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Actor/Operator
relations: {}
---
## Summary

Define Project Settings Prefix

## Claim scope

The Prefix property in Project Settings.

## Claim

Project.Settings.Prefix **means** the required Operator-selected Project
Prefix initialization input in Project Settings.

### Formal claim

```text
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings.Prefix[string]{1}
```

## Semantics

Prefix is one child Property of Project.Settings. The parent Project Settings
definition owns its Property group and its initialization context;
this definition owns the Prefix Property and its declared string Format and
cardinality. Usage policies, assignment grammar, schema keys, storage,
identifier grammar, value encoding and lifecycle are separate concerns.

## Details

This is a fresh role-only Draft because the new Summary and complete target
differ from Current CA-R-2413. It allocates no canonical Requirement identity
and does not retire the older field definition. It does not automatically
introduce a lexical Term or a Method Term Definition.

The Delivery Decision for Prefix serialization is pending separately; this
structural Draft neither substitutes for it nor creates a stored settings
Carrier.

### Source pins

- [Current CA-R-2413@1 — Project Settings Atom Prefix](../CA-R-2413-CORE_META_MODEL-ENTITY_DEFINITION--define-project-settings-atom-prefix.md), SHA-256 `f27b7d0f5e60396f48c7f5ba660aeb34a8fe7ac7272f228ed212d80c9760607c`.
- [Pending parent CA-R-1738@40 — Project Settings](CA-R-1738@40-draft-CORE_META_MODEL--define-project-settings.md), SHA-256 `38829815e44ed95f5c7831301b669c594b1ad1e5fbfca039e74700e3be78df32`.

The Current comparison source remains unchanged; the pending parent is pinned at its coordinated Draft state. This Draft performs no promotion, retirement,
storage-key rename, implementation, or runtime change.
