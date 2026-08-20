---
subject_scopes:
  - artifact-catalog
version: 4
updated_at: 2026-08-19 04:55:53
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
  replacement_of:
    - CAPRMEDIO-GOV-REQU-456--separate-route-catalog-and-project-whitelist
---
# Resolve artifact routes from governed authority and project settings

CAPRMEDIO resolves Content roles, Artifact Types, class short names, semantic routes, carriers, and persistence behavior from active GOV authority, then applies the project selections projected in `.caprmedio/caprmedio_project_settings.toml`; writers and validators fail closed for unknown, disabled, multiply mapped, or ambiguous classifications.
