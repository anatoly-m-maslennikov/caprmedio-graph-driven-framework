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
# Restore direct settings output edits

## Test case

**Fixture:** Change one value directly in either generated output without changing any source RMED Atom.

**Expected result:** A read-only generator run reports the outputs stale and an authorized rebuild restores both canonical outputs from RMED authority.
