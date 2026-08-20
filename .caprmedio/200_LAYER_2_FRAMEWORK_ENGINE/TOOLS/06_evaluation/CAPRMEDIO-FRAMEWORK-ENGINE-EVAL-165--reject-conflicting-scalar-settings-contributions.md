---
artifact_subtype: qa_case
subject_scopes:
  - project-settings
version: 2
updated_at: 2026-08-18 22:44:59
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-674--derive-project-settings-and-map-from-rmed
---
# Reject conflicting scalar settings contributions

## Test case

**Fixture:** Add two active RMED `project_settings` contributions for the same scalar leaf.

**Expected result:** Generation fails before either output changes and identifies the multiply owned scalar path.
