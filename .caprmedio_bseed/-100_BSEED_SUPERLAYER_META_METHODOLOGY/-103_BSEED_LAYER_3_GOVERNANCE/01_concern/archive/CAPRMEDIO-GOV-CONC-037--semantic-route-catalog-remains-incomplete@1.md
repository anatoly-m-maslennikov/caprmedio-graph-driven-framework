---
artifact_subtype: problem
subject_scopes:
  - artifact-catalog
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-CONC-036--route-catalog-is-not-total-or-one-to-one
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-258--derive-artifact-coordinates-from-registered-types
      - CAPRMEDIO-META-REQU-248--three-artifact-forms
      - CAPRMEDIO-META-REQU-257--coordinate-artifacts-without-a-72-type-bijection
      - CAPRMEDIO-GOV-REQU-470--register-current-atom-type-surface
      - CAPRMEDIO-GOV-REQU-317--register-evaluation-atom-subtypes
---

# Problem — Semantic route catalog remains incomplete

META requires exactly one canonical Type for every combination of three
Revision modes, seven Content roles, and three Governance loci: 63 semantic
routes.

Current GOV authority names one internal, external, and relational Type for
each Content role, producing 21 named Types. Because each registered Type
resolves to exactly one Revision mode, the other 42 full routes have no
canonical Type.

The accepted role-and-locus matrix is therefore a valid partial naming surface
but not yet the total three-axis catalog required by META. Project settings and
validators cannot fail closed against a complete whitelist until GOV either
names the remaining routes or a new accepted META successor changes the
totality invariant.

## Primary claim

The current 21-Type GOV matrix leaves 42 of 63 required three-axis semantic
routes unnamed and therefore does not satisfy the active total-catalog
invariant.

## Rationale

The predecessor counted six Content roles and 54 routes and described an older
catalog. Evaluation added a seventh role, while the accepted role-and-locus
matrix clarified 21 names without completing all Revision-mode variants.
