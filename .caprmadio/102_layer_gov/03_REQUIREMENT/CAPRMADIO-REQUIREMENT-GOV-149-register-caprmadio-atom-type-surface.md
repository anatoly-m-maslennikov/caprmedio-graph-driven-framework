---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-149
scope_path: layer:gov
subject_scope: artifact-catalog
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-138
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-131
      - CAPRMADIO-REQUIREMENT-META-133
      - CAPRMADIO-REQUIREMENT-META-134
  - type: resolution_of
    targets:
      - CAPRMADIO-PROBLEM-GOV-009
      - CAPRMADIO-QUESTION-GOV-017
---

# Requirement — Register the CAPRMADIO Atom Type surface

GOV registers these top-level Atom Types for the currently admitted
Content-role and Governance-locus coordinates:

| Content role | Internal | External | Relation |
|---|---|---|---|
| `concern` | `concern` | `external_problem` | `conflict` |
| `analysis` | `analysis` | `external_analysis_report` | `conflict_analysis` |
| `plan` | `plan` | — | — |
| `requirement` | `requirement` | `constraint` | `contract` |
| `method` | `method` | `implementation_methodology` | `integration_decision` |
| `assurance` | `assurance` | `assurance_standard` | `review_protocol` |
| `delivery` | `delivery` | — | — |
| `implementation` | — | `external_git_commit` | `pull_request` |
| `ops` | `ops` | `external_evidence_record` | `verification_record` |

A dash is an intentionally unadmitted coordinate. Writers fail closed rather
than inventing a placeholder Type or substituting another route.

The internal `plan` Type is fixed by META. The internal Implementation Atom
route is not admitted because native project artifacts are the Implementation;
Journals and Projections about them retain their own forms and Types. Existing
external and relational Implementation routes remain admitted as governed
claims about explicit outside or cross-boundary carriers.

Every external Atom identifies the outside authority or system that owns or
imposes its meaning. Every relational Atom declares its registered relation
kind and explicit endpoints. Direct subtypes refine a registered Type without
creating another top-level Type or changing its semantic coordinate.

## Primary claim

GOV registers the current CAPRMADIO Atom Type surface with an internal Plan
route and no internal Implementation Atom route.

## Rationale

The registry reflects semantic need rather than matrix completion: plans can be
accepted as atomic claims, whereas the realized project must not be replaced by
an artificial Atom about implementation.
