---
subjects:
  governs: Entity/Aspect/Engineering/Data Handling/Data Validation
  depends_on:
  - Entity/Object/Occurrent/Runtime/Session
version: 31
updated_at: 2026-10-29 10:13:49 +0400
relations: {}
atom_id: CA-R-1650@31
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary

Define the bounded session-state envelope

## Claim scope

the bounded session-state envelope.

## Claim

the bounded session-state envelope **must** contain **only** routing invariants, current scope, applicable settings, compact session state, **and** references needed **to** load active authority on demand.
