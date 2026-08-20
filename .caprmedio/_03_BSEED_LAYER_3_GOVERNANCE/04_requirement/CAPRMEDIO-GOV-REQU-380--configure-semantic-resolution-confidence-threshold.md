---
subject_scopes:
  - settings
version: 3
updated_at: 2026-08-20 20:58:02
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-M-092-IMPL_METHOD--resolve-only-concerns-autonomously-from-active-atoms
---
# Configure semantic-resolution confidence threshold

`caprmedio_framework_settings.toml` must expose `confidence.semantic_resolution_threshold_percent` as an integer percentage from 0 through 100 with an initial value of 95.
