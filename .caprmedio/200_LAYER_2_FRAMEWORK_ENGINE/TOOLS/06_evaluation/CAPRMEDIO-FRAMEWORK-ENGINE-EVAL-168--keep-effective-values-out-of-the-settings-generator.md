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
# Keep effective values out of the settings generator

## Test case

**Fixture:** Inspect the registered generator implementation and change one effective setting only in its owning RMED Atom.

**Expected result:** The generator contains no project-specific effective-value catalog, and rebuilding changes the projected value and binding solely from the Atom revision.
