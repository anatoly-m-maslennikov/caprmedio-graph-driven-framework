---
subjects:
  governs: Entity/Object/Continuant/Term
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
version: 27
updated_at: 2026-10-29 10:03:18 +0400
relations: {}
atom_id: CA-R-1318@27
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Term

## Claim scope

Project-specific vocabulary, including the word `Term` itself.

## Claim

A Term has one Name, the word or phrase used for its meaning. This declares the existing vocabulary properties and does not implement or review the deferred Terms Graph.

a Term **means** a word **or** phrase with a Project-specific meaning that remains consistent across **all** its uses **in** the same applicable context.

### Formal claim

```text
Entity/Object/Continuant/Term.Name[string]{1}
Entity/Object/Continuant/```

## Details

the word `Term` has the Project-specific meaning defined here, so it is itself a Term. using a Term self-referentially does **not** change its defined meaning **or** require a separate definition layer.
