---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-146
scope_path: layer:gov
subject_scopes:
  - layout
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: override_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-145
---

# Keep the applied Implementation layer flat

The applied project layer `400_LAYER_4_IMPLEMENTATION` (`105_LAYER_IMPL`) contains no subfolders for now. Any governed carriers assigned to that layer live directly in its root.

This is a narrow project-layout exception to the recursive Content-role folders required by `CAPRMADIO-REQUIREMENT-GOV-145`. It does not flatten the reusable root methodology, the installed external methodology, another applied layer, a feature scope, or native implementation outside `.caprmadio/`.

Bootstrap, discovery, routing, migration, and validation reproduce and accept this flat applied-layer boundary. A later Requirement must explicitly replace this one before introducing subfolders under `105_LAYER_IMPL`.
