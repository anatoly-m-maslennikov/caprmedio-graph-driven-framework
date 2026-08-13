---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-077
scope_path: layer:meta
subject_scope: lifecycle-traceability
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-075
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-076
---

# Requirement — Propagate atomic revision impact through lineage

When an Atom receives a new committed revision, CAPRMADIO must assess the
impact on every reachable lineage branch derived from an earlier revision of
that atom.

No dependent child may be silently assumed to remain valid. A branch may stop
propagating only after an explicit determination that the revised parent claim
does not change that child. When a child must be revised or replaced, the same
impact assessment continues recursively through its descendants.

Children that remain valid continue to bind to the exact parent revision they
originally consumed. They are not rewritten merely to point at the newest
revision.

META requires complete impact accounting without prescribing the operational
outcome names, review record, traversal implementation, or automation. GOV
defines that procedure.

## Primary claim

Every new Atom revision requires explicit impact accounting across
its dependent lineage.

## Rationale

Revision-bound provenance is reliable only when downstream effects are either
propagated or explicitly found to be absent. Preserving compatible historical
bindings avoids unnecessary churn while preventing silent semantic drift.
