---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-130
scope_path: layer:meta
subject_scope: artifact-model
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-080
      - CAPRMADIO-REQUIREMENT-META-086
      - CAPRMADIO-REQUIREMENT-META-090
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-095
      - CAPRMADIO-REQUIREMENT-META-101
      - CAPRMADIO-REQUIREMENT-META-113
---

# Requirement — Use Change Plans and Implementation Record Projections

The Implementation Content role admits two non-authoritative Projection contributions in addition to native implementation and Implementation Journals:

- a **Change Plan** is an accepted operative planning Projection for changing the distributed specification and the implementation that realizes it; and
- an **Implementation Record** is a source-derived Projection of what the current specification, Implementation Journal frontier, native targets, and available Git provenance show as implemented.

An Analysis Report remains an Analysis Atom. It investigates what may need to change, alternatives, impacts, causes, and uncertainty. It does not become operative merely by recommending work.

A Change Plan identifies the Requirement, Method, Assurance, Delivery, and other governed artifacts to add, revise, replace, archive, or review; the resulting native code, configuration, documentation, assurance mechanism, and delivery changes; their order and dependencies; and completion conditions. The plan coordinates the complete accepted change, not only code implementation, but does not itself establish or modify the normative specification.

An Implementation Record reports current realization, coverage, source-to-target bindings, relevant commits, and unresolved implementation gaps. It is regenerated mechanically or rebuilt through governed reasoning from its declared source frontier. It is never an Atom and cannot replace the normative Atoms, canonical Implementation Journal, native implementation, Ops evidence, or Verification.

## Primary claim

CAPRMADIO uses Change Plans as operative planning Projections and Implementation Records as derived current-state Projections within the Implementation Content role, while Analysis Reports remain investigative Analysis Atoms.

## Rationale

This gives the Implementation role real governed control-plane content before and after native changes without misclassifying execution plans as code-writing Methods or turning mutable implementation summaries into immutable claims.
