---
subject_scopes:
  - feature-boundary
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 2
updated_at: 2026-08-18 22:44:59
relations:
  child_of:
    - CAPRMEDIO-REQU-702--define-framework-engine-layer-scope
---
# Use one project-local Tool runtime

All Tools in one CAPRMEDIO project must execute through the same project-local managed environment rooted under `.caprmedio_runtime`, with one governed dependency definition and no Tool-specific runtime environments.
