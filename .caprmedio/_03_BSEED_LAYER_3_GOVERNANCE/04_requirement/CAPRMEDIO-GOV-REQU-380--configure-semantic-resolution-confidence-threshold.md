---
subject_scopes:
  - settings
version: 2
updated_at: 2026-08-18 03:25:18
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-050--auto-resolve-high-confidence-semantic-issues
---
# Configure semantic-resolution confidence threshold

`caprmedio_framework_settings.toml` must expose `confidence.semantic_resolution_threshold_percent` as an integer percentage from 0 through 100 with an initial value of 95.
