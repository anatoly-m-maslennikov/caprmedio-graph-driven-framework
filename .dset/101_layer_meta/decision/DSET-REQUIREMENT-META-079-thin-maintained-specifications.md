---
artifact_type: requirement
artifact_id: DSET-REQUIREMENT-META-079
scope_path: layer:meta
subject_scopes:
  - governance-surface
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - DSET-REQUIREMENT-META-072
  - type: relates_to
    targets:
      - DSET-REQUIREMENT-META-054
      - DSET-REQUIREMENT-META-074
      - DSET-REQUIREMENT-META-075
      - DSET-REQUIREMENT-META-077
---

# Requirement — Enable thin maintained Specifications

META and GOV may each own maintained Specifications as reasoned current views
over applicable active Atomic Artifacts. Atomic Artifacts remain the semantic
authority; a Specification interprets and organizes them without replacing,
overriding, or mechanically concatenating their claims.

A conforming Specification:

- owns one declared structural scope and bounded subject;
- starts with a domain-level Mermaid flow when a flow materially improves
  comprehension;
- defines each domain entity using only ordinary language and entities already
  defined above it;
- records forward connections outside entity definitions;
- gives every stateful entity its identity, invariants, derived states, entry
  and exit criteria, transition authority, permitted transitions, required
  evidence, and failure behavior;
- links represented semantic claims directly to Atomic Artifact IDs rather
  than to another maintained view; and
- distinguishes current normative meaning from rationale, examples, and
  historical explanation.

Specifications use Revision mode `maintained`. They are refreshed through
reasoned synthesis only on explicit request or before a gate that requires a
current Specification. A changed atomic source invokes lineage-impact review:
a compatible result leaves the Specification unchanged and bound to its prior
source revision; any affected result requires a new committed Specification
revision before the relevant gate may pass.

This requirement enables Specifications only. Plans, dashboards, generated
views, and other maintained governance surfaces require their own admitted
semantics before they become part of the active META or GOV surface.

## Primary claim

META and GOV Specifications are enabled as thin maintained semantic views whose
meaning remains directly traceable to Atomic Artifacts.

## Rationale

A small maintained domain model gives operators a coherent current view
without duplicating atomic authority. Dependency-ordered definitions,
explicit lifecycle tables, and direct atomic provenance keep the view useful,
reviewable, and refreshable.
