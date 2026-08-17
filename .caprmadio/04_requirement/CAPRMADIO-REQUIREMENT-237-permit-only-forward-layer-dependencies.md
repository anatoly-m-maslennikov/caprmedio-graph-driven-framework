---
subject_scopes:
  - scope-topology
version: 1
updated_at: 2026-08-17 19:07:59
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-065-ordered-realization-topology
    - CAPRMADIO-REQUIREMENT-227-model-project-structure-as-numbered-levels
---
# Permit only forward Layer dependencies

Every dependency between Project Layers must point from the Project root or an earlier Layer to a later Layer in the cumulative order.
