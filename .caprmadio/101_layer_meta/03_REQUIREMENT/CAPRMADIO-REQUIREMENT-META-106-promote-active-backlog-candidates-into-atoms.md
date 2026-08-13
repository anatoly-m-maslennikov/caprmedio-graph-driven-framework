---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-106
scope_path: layer:meta
subject_scope: development-flow
tier: standard
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-058
      - CAPRMADIO-REQUIREMENT-META-090
      - CAPRMADIO-REQUIREMENT-META-105
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-101
      - CAPRMADIO-REQUIREMENT-META-103
---

# Requirement — Promote active backlog candidates into Atoms

Assigning a Development Backlog candidate to a current or future version does
not establish governed truth. The candidate becomes governed only when the
operator selects it for active work and CAPRMADIO materializes the minimum
Requirement, Method, Assurance, Delivery, or other Atoms needed to govern that
work.

One backlog line may produce multiple independently replaceable Atoms. Multiple
closely related backlog lines may produce one Atom only when they resolve to
one independently replaceable claim.

The backlog entry may link the resulting Atoms for navigation but remains a
non-authoritative planning candidate until release finalization removes or
reschedules it.

## Primary claim

A Development Backlog candidate acquires authority only by promotion into the
minimum independently governed Atoms when the operator selects it for active
work; version allocation alone never grants authority.

## Rationale

Separating allocation from promotion allows future plans to move freely while
ensuring active work is governed by precise Atoms rather than one-line backlog
summaries.
