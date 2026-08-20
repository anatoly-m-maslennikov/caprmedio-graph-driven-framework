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
# Compose list settings in canonical source order

## Test case

**Fixture:** Provide disjoint list fragments for one setting from active RMED Atoms discovered in different filesystem orders.

**Expected result:** Every run emits the same concatenated list in canonical source-identity order and the Map binds that leaf to exactly those contributors in the same order.
