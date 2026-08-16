---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-TOOL-032
scope_path: feature:tools
subject_scopes:
  - projection-pipeline
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-TOOL-024-project-ndjson-logs-to-toon
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-172-register-generated-data-stage-prefixes
---

# Project src NDJSON to stg TOON

The framework must provide a deterministic Tool that losslessly projects an exact `src` NDJSON Journal frontier into a replaceable `stg` TOON carrier with source-frontier provenance.
