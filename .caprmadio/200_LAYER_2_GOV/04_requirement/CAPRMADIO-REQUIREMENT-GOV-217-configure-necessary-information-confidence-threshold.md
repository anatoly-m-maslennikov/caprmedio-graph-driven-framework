---
subject_scopes:
  - settings
version: 1
updated_at: 2026-08-17 17:29:05
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  relates_to:
    - CAPRMADIO-REQUIREMENT-231-identify-necessary-information-by-confidence
---
# Configure necessary-information confidence threshold

The canonical project settings must expose `confidence.necessary_information_threshold_percent` as an integer percentage from 0 through 100 and resolve an omitted value to 95.
