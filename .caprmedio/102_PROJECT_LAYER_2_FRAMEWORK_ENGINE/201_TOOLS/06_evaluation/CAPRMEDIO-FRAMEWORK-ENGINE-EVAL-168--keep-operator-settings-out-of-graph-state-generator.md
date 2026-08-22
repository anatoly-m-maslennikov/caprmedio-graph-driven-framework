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
# Keep operator settings out of the Graph State generator

## Test case

**Fixture:** Inspect the registered generator implementation and change one
operator-selected value only in the governed Project Configuration Atom.

**Expected result:** The generator contains no project-specific effective-value
catalog or non-Configuration `project_settings` input. Rebuilding changes the
projected value and binding solely from the Configuration revision and admitted
Graph State sources.
