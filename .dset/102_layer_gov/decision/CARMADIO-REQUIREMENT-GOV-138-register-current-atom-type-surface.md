---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-GOV-138
scope_path: layer:gov
subject_scopes:
  - artifact-catalog
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - DSET-REQUIREMENT-GOV-131
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-088
      - CARMADIO-REQUIREMENT-META-089
      - CARMADIO-REQUIREMENT-META-102
---

# Requirement — Register the current Atom Type surface

GOV registers these top-level Atom Types for the currently admitted Content-role
and Governance-locus coordinates:

| Content role | Internal | External | Relation |
|---|---|---|---|
| `concern` | `concern` | `external_problem` | `conflict` |
| `analysis` | `analysis` | `external_analysis_report` | `conflict_analysis` |
| `requirement` | `requirement` | `constraint` | `contract` |
| `method` | `method` | `implementation_methodology` | `integration_decision` |
| `assurance` | `assurance` | `assurance_standard` | `review_protocol` |
| `delivery` | `delivery` | — | — |
| `implementation` | `implementation` | `external_git_commit` | `pull_request` |
| `ops` | `ops` | `external_evidence_record` | `verification_record` |

The eight internal names are fixed by META. GOV owns the external and relational
names. A dash means that the coordinate is not currently admitted; writers fail
closed rather than substituting another Type.

Every external Atom identifies the outside authority or system that owns or
imposes its meaning. Every relational Atom declares its registered relation
kind and explicit endpoints. Direct subtypes refine a registered Type without
creating another top-level Type or changing its semantic coordinate.

## Primary claim

GOV registers one current top-level Atom Type for every admitted Content-role
and Governance-locus coordinate under CARMADIO's eight-role model.

## Rationale

The predecessor encoded seven roles and the retired Observation vocabulary and
also bundled subtype-specific assurance rules into the top-level Type surface.
The successor restores the META-owned eight-role boundary while leaving direct
subtype registration to separate GOV Atoms.
