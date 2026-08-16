---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-120
subject_scopes:
  - scope-topology
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
---

# Requirement — Preserve bounded meaning across structural scales

A CAPRMADIO invariant, claim, relation, or classification retains the same
meaning when applied recursively at project, layer, feature group, feature, or
deeper configured structural scopes. Each use remains bounded to its declared
scope and applicability; recursion does not widen authority, evidence,
assurance, or implementation coverage.

A narrower scope may specialize inherited authority through an explicit child
or override relation. If no narrower artifact exists, applicable inherited
authority remains directly effective. A local exception must identify its
boundary and cannot change the meaning of the parent claim outside that
boundary.

Aggregation, summaries, dashboards, and Projections must preserve the declared
scope of their inputs and must not inflate truth, completeness, assurance, or
priority by combining them. One-way layer dependencies remain in force at every
scale.

## Primary claim

CAPRMADIO preserves invariant meaning and explicit applicability when authority
is inherited, specialized, or summarized across structural scales.
