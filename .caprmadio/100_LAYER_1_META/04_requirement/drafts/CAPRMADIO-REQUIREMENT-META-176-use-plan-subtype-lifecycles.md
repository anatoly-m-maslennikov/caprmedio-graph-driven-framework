---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-176
scope_path: layer:meta
subject_scopes:
  - lifecycle-traceability
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-136-use-short-lived-action-only-plans
  child_of:
    - CAPRMADIO-REQUIREMENT-META-131-nine-content-roles-with-plan
    - CAPRMADIO-REQUIREMENT-META-161-define-role-specific-atom-atomicity
---

# Use Plan subtype lifecycles

CAPRMADIO must apply the lifecycle of a Plan according to its direct subtype while keeping every Plan action-only and structurally single-scope. The Development Backlog remains active across versions; a Version Plan remains active until its target version is released or the Plan is abandoned; and a Change Plan remains a bounded execution package. Executed Version Plans and Change Plans move to `done/`, while abandoned or absorbed Plans move to `archive/`. Findings, alternatives, interpretation, and rationale remain Analysis rather than Plan content.
