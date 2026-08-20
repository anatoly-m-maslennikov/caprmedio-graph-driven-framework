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
# Rebuild both settings outputs from RMED

## Test case

**Fixture:** Remove both generated settings outputs from an isolated current-project fixture whose active RMED contributions and Framework Settings revision are valid.

**Expected result:** One authorized generator run recreates both outputs with the same effective values, exact contributor revisions, and one shared current source frontier without reading a prior Map or Project Settings carrier.
