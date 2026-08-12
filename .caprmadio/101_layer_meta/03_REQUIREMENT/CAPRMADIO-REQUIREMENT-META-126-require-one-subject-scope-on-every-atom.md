---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-126
scope_path: layer:meta
subject_scope: artifact-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-080
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-100
      - CAPRMADIO-REQUIREMENT-META-114
      - CAPRMADIO-REQUIREMENT-META-117
      - CAPRMADIO-REQUIREMENT-META-120
      - CAPRMADIO-REQUIREMENT-META-124
---

# Requirement — Require one Subject scope on every Atom

Every CAPRMADIO Atom declares exactly one singular `subject_scope`, including
draft, active, and archived Atoms. The value is selected from the closed
Subject-scope vocabulary governed for the Atom's structural owner.

`subject_scope` classifies the Atom's primary semantic subject for discovery,
comparison, and review. It is independent of `scope_path` and does not change
structural ownership, applicability, authority, priority, lifecycle, or
relations. Cross-cutting relevance is expressed through typed relations rather
than multiple Subject scopes.

A missing, multiple, unknown, or fallback value is invalid. When an accepted
claim fits no governed Subject scope, its owning vocabulary must first be
extended with a precise, non-overlapping value through the normal governance
process. `other`, `misc`, and implicit near-match assignment are forbidden.

## Primary claim

Every CAPRMADIO Atom has exactly one governed `subject_scope`, regardless of its
structural scope, lifecycle placement, or Content role.

## Rationale

A universal single-subject invariant keeps every Atom discoverable and makes
scope catalogs complete without confusing semantic classification with
structural ownership or adding fallback buckets.
