---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-077
scope_path: layer:meta
subject_scope: lifecycle-traceability
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-120-preserve-bounded-meaning-across-structural-scales
    - CAPRMADIO-REQUIREMENT-122-require-falsifiable-claims-and-stop-conditions
---

# Requirement — Propagate atomic revision impact through lineage

When an Atom receives a new committed revision, is replaced by a successor, or
moves to the archive, CAPRMADIO must assess the impact on every reachable
lineage branch derived from that Atom or one of its earlier revisions.

No dependent child may be silently assumed to remain valid. A branch may stop
propagating only after an explicit determination that the revised parent claim
does not change that child. When a child must be revised or replaced, the same
impact assessment continues recursively through its descendants.

Children that remain valid continue to bind to the exact parent revision they
originally consumed. They are not rewritten merely to point at the newest
revision or successor. Replacing or archiving a parent never deletes, retargets,
or otherwise breaks its existing child links.

META requires complete impact accounting without prescribing the operational
outcome names, review record, traversal implementation, or automation. GOV
defines that procedure.

## Primary claim

Every Atom revision, replacement, or archival requires explicit impact
accounting across its dependent lineage without rewriting historical links.
