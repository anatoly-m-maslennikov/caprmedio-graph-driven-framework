---
artifact_subtype: qa_case
subject_scopes:
  - project-settings
version: 3
updated_at: 2026-08-22 04:20:12
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-674--derive-project-graph-state-and-map-from-configuration-authority
---
# Restore direct Graph State output edits

## Test case

**Fixture:** Change one value directly in either generated Graph State output
without changing the Configuration Atom or an admitted source.

**Expected result:** A read-only generator run reports the outputs stale and an
authorized rebuild restores both canonical outputs from Configuration authority
and admitted Graph State sources.
