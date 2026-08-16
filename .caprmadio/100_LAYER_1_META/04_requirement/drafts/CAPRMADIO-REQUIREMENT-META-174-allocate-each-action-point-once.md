---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-174
scope_path: layer:meta
subject_scopes:
  - development-flow
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
    - CAPRMADIO-REQUIREMENT-META-131-nine-content-roles-with-plan
  relates_to:
    - CAPRMADIO-REQUIREMENT-META-108-reconcile-the-backlog-after-release
---

# Allocate each action point once

CAPRMADIO must place every active planning action point in exactly one Development Backlog section or, after an approved split, exactly one Plan file. Assigning, rescheduling, unscheduling, or abandoning an action point moves or removes it without copying it into another active planning location. Change Plans may reference or decompose allocated action points but do not duplicate their planning ownership.
