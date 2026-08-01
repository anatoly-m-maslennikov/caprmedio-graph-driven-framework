---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-004
scope_path: layer:meta
subject_scopes:
  - lifecycle
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
---

# Requirement — Bound effect guarantees

## Primary claim

CARMADIO permits an effect guarantee only when its scope, assumptions, owner,
temporal boundary, and enforcement conditions are explicit. A bounded local
guarantee must never be presented as universal exactly-once execution.

## Rationale

For example, at-least-once delivery plus receiving-side deduplication or
idempotency may produce effectively-once effects only within the declared key,
retention, ownership, and atomic check/write boundary. The general invariant is
the explicit boundary; downstream profiles own the mechanism.
