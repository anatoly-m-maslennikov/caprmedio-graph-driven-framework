---
atom_id: CA-R-2239@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Continuant/Package/Project Implementation
version: 1
updated_at: 2026-10-29 07:32:39 +0400
relations: {}
tier: 1
---
## Summary

Define Project Implementation

## Claim

Project Implementation is the single root Package of a Project's implementation. It has no enclosing Package. It realizes RMED and may be directly edited; it is not automatically a Projection merely because it realizes a specification.

### Formal claim

```text
Package/Project Implementation
Project Implementation > @(Package)
```

## Semantics

Implementation is the section heading for this model area. Project Implementation is the root Package kind, rather than a part of a second Implementation kind. Modules execute on their language engine; Prompts execute on an LLM AI Agent engine; Assets are non-executable content. Logical parts remain distinct from their Carriers and from live Runtimes.

## Details

CA-A-1259 records this decision. Numeric identity is pending; no Current source promotion is claimed. CA-A-1266 places Documentation directly in Package, separately from runtime-required Asset. Former Resources members are classified as Assets, Prompts or Documentation; Current migration remains pending.
