---
subject_scopes:
  - artifact-catalog
project_settings:
  artifacts:
    enabled_types:
      - ops:release_record
      - ops:deployment_record
      - ops:environment_state
      - ops:health_record
      - ops:incident_record
version: 1
updated_at: 2026-08-19 04:55:53
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
  replacement_of:
    - CAPRMEDIO-GOV-REQU-332--register-ops-subtypes
---
# Register Ops Types

GOV registers `release_record`, `deployment_record`, `environment_state`, `health_record`, and `incident_record` as internal Ops Types for their corresponding enacted facts.
