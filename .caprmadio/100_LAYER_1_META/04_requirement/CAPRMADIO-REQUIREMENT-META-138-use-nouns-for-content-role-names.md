---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-138
scope_path: layer:meta
subject_scope: semantics
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-131-nine-content-roles-with-plan
    - CAPRMADIO-REQUIREMENT-META-132-caprmadio-framework-identity
---
# Requirement — Use nouns for Content-role names

Every canonical CAPRMADIO Content-role name is a noun naming the primary kind
of contribution represented by that role. A role name must not be a verb,
imperative, workflow instruction, status, or activity label.

The canonical labels are Concern, Analysis, Plan, Requirement, Method,
Assurance, Delivery, Implementation, and Ops. Grammatical variants such as
`planning`, `implementing`, or `operating` may appear in explanatory prose but
must not replace the canonical role names in identifiers, schemas, settings,
folder names, diagrams, or public expansions of CAPRMADIO.

Any future role proposal must supply a noun that remains semantically stable
when the workflow, actor, tool, or implementation mechanism changes.

## Primary claim

CAPRMADIO Content-role names are nouns that classify contributions rather than
verbs that prescribe activities.
