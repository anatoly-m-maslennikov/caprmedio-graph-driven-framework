---
atom_id: CA-R-2233@2
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Continuant/Package/Eval Package
  depends_on:
  - Entity/Object/Continuant/Package > Module
  - Entity/Object/Continuant/Package > Prompt
  - Entity/Object/Continuant/Package > Asset
version: 2
updated_at: 2026-10-29 10:13:49 +0400
relations: {}
tier: 1
---
## Summary

Define Eval Package

## Claim

An Eval Package is a Package for evaluation implementation. It can contain executable Modules and executable Prompts, together with the Assets needed by those evaluations. Module-based tests are one supported evaluation mechanism; evaluations are not restricted to tests written as code. The common Package structure also applies.

### Formal claim

```text
Package/Eval Package
Eval Package > @(Module)
Eval Package > @(Prompt)
```

## Semantics

An Eval Package is still a Package; it is not a new executable kind. Modules run on their language engine and Prompts on an LLM AI Agent engine. Assets are their non-executable inputs, distinct from their Carriers.
