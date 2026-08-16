---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-SKILL-020
scope_path: feature:skills
subject_scopes:
  - skill-boundary
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-026-single-owner-rule-placement
---

# Keep CA and specialist skills thin

`/ca` and specialist skills must only initialize context, pass operator input, select a governed route, and chain the routed methodology or skill without duplicating routing or methodology rules.
