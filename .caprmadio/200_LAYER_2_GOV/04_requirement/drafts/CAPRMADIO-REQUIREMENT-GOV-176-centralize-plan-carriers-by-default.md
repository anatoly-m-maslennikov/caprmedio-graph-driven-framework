---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-176
scope_path: layer:gov
subject_scopes:
  - layout
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  override_of:
    - CAPRMADIO-REQUIREMENT-GOV-150-register-change-plan-subtype
    - CAPRMADIO-REQUIREMENT-GOV-157-use-flat-numbered-layer-feature-layout
---

# Centralize Plan carriers by default

GOV must place every Plan carrier in the single project-level `.caprmadio/03_plan/` directory by default; a configured project exception may select another location, while each Plan's governed scope remains explicit in the carrier rather than partitioning Plan storage.
