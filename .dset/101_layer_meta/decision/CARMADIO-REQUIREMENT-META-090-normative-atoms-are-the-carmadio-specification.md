---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-090
scope_path: layer:meta
subject_scopes:
  - governance-surface
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-REQUIREMENT-META-084
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-080
      - CARMADIO-REQUIREMENT-META-086
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-103
      - CARMADIO-REQUIREMENT-META-077
      - CARMADIO-REQUIREMENT-META-097
      - CARMADIO-REQUIREMENT-META-088
      - CARMADIO-REQUIREMENT-META-089
---

# Requirement — Treat normative Atoms as the distributed specification

Applicable active Requirement, Method, Assurance, and Delivery Atoms across all Governance loci collectively form the project's normative specification. Each Atom owns one independently replaceable outcome, obligation, construction rule, assurance criterion, delivery rule, boundary, invariant, or other normative claim.

A second maintained document must not become another specification authority by rephrasing those claims. Full written Specifications are retired as an independent maintained semantic surface.

Projects may expose thin Projections over the Atom set. A conforming Projection:

- names its declared source Atoms directly;
- organizes them through selection, grouping, ordering, navigation, or already-governed relations;
- remains rebuildable from its declared sources;
- introduces no independently normative paraphrase of a source claim;
- never becomes evidence merely by citing an Atom; and
- never overrides an Atom or hides which Atom owns a represented claim.

Catalog, map, and hub are permitted GOV-level Projection vocabularies. A specification catalog may provide sections and lists of normative Atom IDs; a specification map may render their governed relations; a specification hub may provide navigation to scoped catalogs, maps, and Atoms. Correct interpretation of an Atom must never depend on wording present only in a Projection.

Concern and Analysis Atoms inform normative work, Implementation Atoms realize it, and Ops Atoms record enacted operation or factual results. These roles may appear in role-appropriate Projections but do not become normative merely because a Projection groups them with the distributed specification.

## Primary claim

Applicable Requirement, Method, Assurance, and Delivery Atoms are the distributed normative specification, while catalogs, maps, and hubs are thin non-authoritative Projections rather than rewritten Specifications.

## Rationale

When each normative claim is already an independently governed Atom, a second prose specification duplicates authority and creates drift. Thin Projections preserve overview and navigation while every normative change remains localized to its owning Atom.
