---
atom_id: CA-R-2178@4
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Object/Continuant/Package
version: 4
updated_at: 2026-10-29 07:32:39 +0400
relations: {}
tier: 3
---
## Summary

Define Package

## Claim

A Package is a logical collection of Modules, Prompts, runtime/evaluation Assets, Documentation and nested Packages. Runtime Package and Eval Package specialize Package for their respective uses. Project Implementation is the root specialization of Package and has no enclosing Package; each non-root Package has one immediate Package parent. Implementation is only a section heading, not a separate containing kind.

### Formal claim

```text
Package/Runtime Package
Package/Eval Package
Package > @(Package)
Package > Module
Package > Prompt
Package > Asset
Package > Documentation
```

## Semantics

References reuse the same kind, not a new Package kind. Its directory representation remains a Delivery concern.

## Details

