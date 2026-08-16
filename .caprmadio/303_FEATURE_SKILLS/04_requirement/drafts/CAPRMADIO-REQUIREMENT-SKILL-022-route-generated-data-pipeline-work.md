---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-SKILL-022
scope_path: feature:skills
subject_scopes:
  - routing
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-172-register-generated-data-stage-prefixes
    - CAPRMADIO-REQUIREMENT-TOOL-029-validate-generated-data-stage-pipelines
    - CAPRMADIO-REQUIREMENT-TOOL-032-project-src-ndjson-to-stg-toon
    - CAPRMADIO-REQUIREMENT-TOOL-033-generate-mrt-semantic-projections
    - CAPRMADIO-REQUIREMENT-TOOL-034-generate-biz-artifact-and-implementation-metrics
---

# Route generated-data pipeline work

Skills that handle generated-data pipeline work must route stage selection, validation, and materialization through the governed stage vocabulary and deterministic Tools without redefining either.
