---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-168
scope_path: layer:gov
subject_scopes:
  - routing
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-167-register-one-canonical-routing-tree
---

# Validate the routing tree

GOV must reject a routing tree with an invalid schema, unknown target, ambiguous precedence, duplicate route identity, or authority effect that is not explicitly declared.
