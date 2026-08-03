---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-120
scope_path: layer:meta
subject_scopes:
  - topology
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-030
      - CARMADIO-REQUIREMENT-META-057
      - CARMADIO-REQUIREMENT-META-096
      - CARMADIO-REQUIREMENT-META-100
      - CARMADIO-REQUIREMENT-META-104
---

# Requirement — Preserve bounded meaning across structural scales

A CARMADIO invariant, claim, relation, or classification retains the same
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

CARMADIO preserves invariant meaning and explicit applicability when authority
is inherited, specialized, or summarized across structural scales.

## Rationale

This adapts FPF Cross-Scale Consistency to CARMADIO scopes without imposing
FPF's specialized mathematical aggregation laws on every project structure.
