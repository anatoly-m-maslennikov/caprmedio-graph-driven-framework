---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-170
scope_path: layer:gov
subject_scopes:
  - routing
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-167-register-one-canonical-routing-tree
---

# Resolve skill routing precedence

Skill routes must resolve by explicit precedence: project-local CAPRMADIO routes override framework routes, which override provider-global routes.
