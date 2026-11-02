---
subjects:
  governs: Entity/Object/Continuant/Actor/AI Agent
  depends_on:
  - Entity/Object/Continuant/Actor/AI Agent
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Aspect/Engineering/Execution Control/Effect Authorization
  - Entity/Aspect/Engineering/Execution Control/Decision Confidence
version: 20
updated_at: 2026-10-29 10:13:49 +0400
relations:
  child_of:
  - CA-R-1713
atom_id: CA-R-1555@20
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary
Govern CA execution gates

## Claim scope
identified AI Agents considering clarification omission under applicable configured confidence requirements.

## Claim

an identified AI Agent **may** omit clarification **only** **when** confidence **in** **every** following item meets its applicable configured requirement:

- intent;
- scope;
- route;
- entry criteria.

confidence **must not** create delegated authority **or** bypass per-action Operator approval **when** active authority requires it.
