---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-188
scope_path: layer:meta
subject_scopes:
  - lifecycle
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-129-bound-git-authority-to-repository-provenance
    - CAPRMADIO-REQUIREMENT-META-154-three-artifact-forms-with-generated-projections
---
# Preserve governed action history in Journals

Every governed action with persisted or externally visible effects must remain reconstructible from an append-only Work Journal independently of Git topology.
