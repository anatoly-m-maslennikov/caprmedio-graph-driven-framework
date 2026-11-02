---
atom_id: CA-R-2238@2
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Aspect/Engineering/Architecture/Communication/API
  depends_on:
  - Entity/Object/Continuant/Package
version: 2
updated_at: 2026-10-29 10:13:49 +0400
relations: {}
tier: 1
---
## Summary

Define Package API

## Claim

An API is a declared invocation interface exposed by a Package to its callers. Its forms can include CLI, Web API/REST API, RPC and other interfaces. Public means exposed for use outside the Package boundary; it does not require Internet exposure. The applicable specification determines which Packages must expose an API.

## Semantics

API is the shared Engineering topic for these interface forms. This Definition does not create a separate CLI primary kind, a particular endpoint, or an actual running interface.
