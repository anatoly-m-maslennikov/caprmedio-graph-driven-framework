---
artifact_type: requirement
artifact_id: DSET-REQUIREMENT-META-072
scope_path: layer:meta
subject_scopes:
  - governance-surface
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - DSET-REQUIREMENT-META-054
  - type: relates_to
    targets:
      - DSET-REQUIREMENT-META-064
      - DSET-REQUIREMENT-META-071
---

# Requirement — Keep the current governance phase atomic-only

The applied META and GOV layers currently contain only Atomic Artifacts.
Maintained hubs, plans, specifications, projections, and generated views are
not part of the current governance surface.

Existing non-atomic carriers in those layers are deleted. DSET may introduce
maintained artifacts later only after a new Atomic Artifact defines their
semantics, ownership, lifecycle, and relation to Atomic Artifacts.

This phase constraint does not classify Atomic Artifacts by their folder name.
Identity-bearing records remain atomic whether active or archived.

## Primary claim

META and GOV remain atomic-only until maintained artifacts receive new explicit
governance.

## Rationale

Removing partially governed maintained carriers keeps the current control
surface internally coherent while the Atomic Artifact model is finalized.
Their later reintroduction can then follow one deliberate contract instead of
preserving premature structures.
