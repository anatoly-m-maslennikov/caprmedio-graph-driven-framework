---
atom_id: CA-R-2180@5
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Object/Continuant/Package > Documentation
  depends_on:
  - Entity/Object/Continuant/Package
  - Entity/Object/Continuant/Package > Asset
  - Entity/Object/Continuant/Package > Prompt
version: 5
updated_at: 2026-10-29 07:32:39 +0400
relations: {}
tier: 2
---
## Summary

Define Documentation

## Claim

Documentation is non-executable Implementation content that describes, explains or provides reference information about the project and framework for users and LLMs. Its role is descriptive/reference information rather than required runtime or evaluation input. It is a Package part separate from runtime/evaluation Asset content and from executable Prompt instructions.

### Formal claim

```text
Package > Documentation
```

## Semantics

A reader can be a person or an LLM; that alone does not turn descriptive content into a Prompt. Runtime/test dependency and instructional execution purpose are different criteria. The logical Documentation item is distinct from its File or other Carrier.

## Details

