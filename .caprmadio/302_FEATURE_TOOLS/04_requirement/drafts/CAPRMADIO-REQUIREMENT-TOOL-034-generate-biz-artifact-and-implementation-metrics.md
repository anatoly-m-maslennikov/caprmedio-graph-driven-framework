---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-TOOL-034
scope_path: feature:tools
subject_scopes:
  - projection-pipeline
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-172-register-generated-data-stage-prefixes
    - CAPRMADIO-REQUIREMENT-TOOL-033-generate-mrt-semantic-projections
---

# Generate biz artifact and implementation metrics

The framework must provide deterministic Tools that generate `biz` aggregate metrics for CAPRMADIO artifacts and implementation as both point-in-time snapshots and historical series, including active Requirement-count growth over time.
