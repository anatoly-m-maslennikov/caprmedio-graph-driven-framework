---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-158
scope_path: layer:gov
subject_scopes:
  - relation-model
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-GOV-156-register-rationale-for-relation
  child_of:
    - CAPRMADIO-REQUIREMENT-META-144-store-each-semantic-relation-once
    - CAPRMADIO-REQUIREMENT-META-145-let-the-dependent-atom-own-the-relation
    - CAPRMADIO-REQUIREMENT-META-146-create-rationale-after-its-subject
    - CAPRMADIO-REQUIREMENT-META-147-keep-analysis-optional-before-specification
    - CAPRMADIO-REQUIREMENT-META-148-store-only-direct-semantic-relations
    - CAPRMADIO-REQUIREMENT-GOV-101-derive-locus-and-declare-endpoint-origins
    - CAPRMADIO-REQUIREMENT-GOV-155-register-rationale-analysis-subtype
---

# Register dependent-to-subject relations

GOV registers the following directed relations. The artifact on the left stores the relation to its pre-existing subject on the right:

| Relation | Owning artifact | Allowed target |
| --- | --- | --- |
| `derived_from` | specification or Rationale Atom | source Analysis Report |
| `rationale_for` | Rationale Analysis Atom | Requirement, Method, Assurance, or Delivery Atom |
| `method_for` | Method Atom | Requirement Atom |
| `assurance_for` | Assurance Atom | Requirement or Method Atom |
| `delivery_for` | Delivery Atom | Requirement or Method Atom |
| `implementation_of` | governed Implementation carrier | specification Atom |
| `evidence_for` | Evidence carrier | Assurance or Implementation carrier |
| `concern_about` | Concern Atom | Observation or another directly affected artifact |

Each relation is persisted only by its owning artifact. Inverse navigation is derived and must not be stored as a backlink. An artifact may store both `derived_from` and another registered relation when they express different direct facts, such as a Rationale derived from an Analysis Report and explaining a Requirement.

The registered relations do not imply transitive links. Additional relation meanings require separate GOV authority rather than reuse of the nearest-sounding relation.
