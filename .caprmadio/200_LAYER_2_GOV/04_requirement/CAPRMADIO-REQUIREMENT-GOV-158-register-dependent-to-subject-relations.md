---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-158
scope_path: layer:gov
subject_scopes:
  - relation-model
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-GOV-156-register-rationale-for-relation
  child_of:
    - CAPRMADIO-REQUIREMENT-META-144
    - CAPRMADIO-REQUIREMENT-META-146
    - CAPRMADIO-REQUIREMENT-META-147
    - CAPRMADIO-REQUIREMENT-META-148
---
# Register dependent-to-subject relations

GOV registers the following directed relations. The artifact on the left stores the relation to its pre-existing subject on the right:

| Relation | Owning artifact | Allowed target |
| --- | --- | --- |
| `derived_from` | internal Concern, Analysis, Plan, Requirement, Method, Assurance, Delivery, or Rationale Atom | source Analysis Atom |
| `rationale_for` | Rationale Analysis Atom | Requirement, Method, Assurance, or Delivery Atom |
| `method_for` | Method Atom | Requirement Atom |
| `assurance_for` | Assurance Atom | Requirement or Method Atom |
| `delivery_for` | Delivery Atom | Requirement or Method Atom |
| `implementation_of` | governed Implementation carrier | specification Atom |
| `evidence_for` | Evidence carrier | Assurance or Implementation carrier |
| `concern_about` | Concern Atom | Observation or another directly affected artifact |

Each relation is persisted only by its owning artifact. Inverse navigation is derived and must not be stored as a backlink. An artifact may store both `derived_from` and another registered relation when they express different direct facts, such as a Rationale derived from an Analysis Report and explaining a Requirement.

The registered relations do not imply transitive links. Additional relation meanings require separate GOV authority rather than reuse of the nearest-sounding relation.
