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
    - CAPRMADIO-REQUIREMENT-TOOL-028-own-deterministic-scripts-in-tools
---

# Keep CA and specialist skills thin

`/ca` and specialist Skills must contain only agent-facing instructions and thin routing or chaining declarations; they must reference Tools rather than embed or copy deterministic scripts and executable helpers.
