---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-TOOL-029
scope_path: feature:tools
subject_scopes:
  - projection-pipeline
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-172-register-generated-data-stage-prefixes
---

# Validate generated-data stage pipelines

The framework must provide a deterministic Tool that validates the registered `src → stg → mrt → biz` prefixes, forward-only dependencies, declared source frontiers, and the separation of generated outputs from semantic authority.
