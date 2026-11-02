---
atom_id: CA-R-2179@6
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Object/Continuant/Package > Prompt
version: 6
updated_at: 2026-10-29 10:13:49 +0400
relations: {}
tier: 2
---
## Summary

Define Prompts

## Claim

A Prompt is instructions executable on an LLM AI Agent engine.

### Formal claim

```text
Package > Prompt
```

## Semantics

Prompt describes the executable instructional role, not a file extension or operating-system permission. Its representation is a Carrier. This distinguishes Prompt execution from Module execution on a language engine, without adding an engine kind or execution Relation Type.
