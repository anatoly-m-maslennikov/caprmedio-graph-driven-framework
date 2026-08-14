---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-106
scope_path: layer:meta
subject_scope: development-flow
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-058
      - CAPRMADIO-REQUIREMENT-META-090
      - CAPRMADIO-REQUIREMENT-META-105
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-101
      - CAPRMADIO-REQUIREMENT-META-103
---

# Requirement — Promote active backlog candidates into Atoms

Assigning a Development Backlog candidate to a current or future version does
not establish governed truth. The candidate becomes active work only when the
operator selects it and CAPRMADIO creates one bounded Plan containing its action
points. Execution then materializes the minimum Requirement, Method, Assurance,
Delivery, or future Ops Atoms needed to govern that work.

One backlog line may produce multiple Atoms. Multiple closely related backlog
lines may produce one Concern or RMAD Atom only when they resolve to one
independently replaceable claim. Analysis, Plan, Implementation, and Ops use
their separately governed atomicity models.

The backlog entry may link the resulting Atoms for navigation but remains a
non-authoritative planning candidate until release finalization removes or
reschedules it.

## Primary claim

A Development Backlog candidate becomes active only through a bounded Plan;
specification or other semantic authority arises only from the applicable
`CARMAD + O` Atoms created or revised during execution.
