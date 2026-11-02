---
atom_id: CA-R-2231@2
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Aspect/Engineering/Architecture/Communication/API/Self Documentation
  depends_on:
  - Entity/Object/Continuant/Package
version: 2
updated_at: 2026-10-29 10:13:49 +0400
relations: {}
tier: 1
---
## Summary

Define API Self Documentation

## Claim

API Self Documentation is information made available by an API that describes how callers can use its operations, including their invocation inputs and expected results. It can be human-readable, machine-readable or both, as required by the applicable Package specification. A particular Package is obliged to supply it only where its specification requires it.

## Semantics

CLI help, a Web API schema and RPC discovery illustrate different forms. The former Tool Self Description meant the machine-readable invocation-contract case; its useful meaning is preserved here without retaining Tool as a primary kind. Generated versus authored documentation is a Method/Delivery choice, not decided by this Definition.
