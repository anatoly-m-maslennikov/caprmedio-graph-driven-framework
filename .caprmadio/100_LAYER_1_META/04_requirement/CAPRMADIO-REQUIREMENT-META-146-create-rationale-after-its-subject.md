---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-146
scope_path: layer:meta
subject_scope: artifact-model
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-141
  child_of:
    - CAPRMADIO-REQUIREMENT-META-135-preserve-content-role-boundaries-through-caprmadio-loop
    - CAPRMADIO-REQUIREMENT-META-157-separate-artifact-carrier-and-revision
---
# Requirement — Create Rationale after its subject

A Rationale is an Analysis Atom created only after every specification Atom it explains already exists. The Rationale stores the directed relation to its subjects; specification Atoms contain neither embedded rationale nor persisted rationale backlinks.

Rationale is explanatory rather than normative. Changing an obligation, boundary, Method, Assurance condition, Delivery rule, or acceptance meaning requires a new applicable specification Atom rather than a Rationale.

## Primary claim

A Rationale follows and points to its pre-existing specification subjects without modifying them.
