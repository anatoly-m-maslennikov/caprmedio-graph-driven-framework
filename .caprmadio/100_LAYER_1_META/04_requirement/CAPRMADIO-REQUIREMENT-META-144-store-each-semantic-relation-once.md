---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-144
scope_path: layer:meta
subject_scopes:
  - artifact-model
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-121-bind-traceability-to-exact-claims-and-revisions
    - CAPRMADIO-REQUIREMENT-META-157-separate-artifact-carrier-and-revision
---

# Store each semantic relation once

CAPRMADIO persists each semantic relation in exactly one artifact carrier. It must not store an inverse backlink, reciprocal copy, or second representation of the same relation in another carrier.

Tools and projections derive inverse navigation from the one persisted relation whenever readers need to traverse it in the opposite direction.

Every semantic relation has one persisted owner and any inverse view is derived.
