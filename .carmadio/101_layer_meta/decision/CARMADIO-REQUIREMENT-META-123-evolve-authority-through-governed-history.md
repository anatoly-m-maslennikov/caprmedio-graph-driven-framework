---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-123
scope_path: layer:meta
subject_scopes:
  - lifecycle
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-076
      - CARMADIO-REQUIREMENT-META-080
      - CARMADIO-REQUIREMENT-META-101
      - CARMADIO-REQUIREMENT-META-103
      - CARMADIO-REQUIREMENT-META-113
      - CARMADIO-REQUIREMENT-META-121
---

# Requirement — Evolve authority through governed history

CARMADIO evolves governed meaning without erasing the exact historical state
on which accepted downstream work relied.

An Atom may be clarified within its primary claim until a committed dependency
binds to that revision. Later semantic change creates a new committed revision
with lineage impact review or a successor Atom when identity must change.
Accepted Journal records remain append-only, and corrections or removals are
new records. Projections are replaced by regeneration from their declared
sources.

Currentness, active placement, replacement, archive, and effective Journal
frontiers are derived from governed history and explicit relations rather than
duplicated writable status properties. Git preserves committed carriers, while
governed Journals preserve semantic histories that must survive Git graph
transformations.

## Primary claim

CARMADIO changes authority through replayable Atom revisions, successor
lineage, append-only Journal records, and regenerable Projections without
rewriting relied-upon history or duplicating lifecycle state.

## Rationale

This adapts FPF State Explicitness and Open-Ended Evolution to CARMADIO's Atom,
Journal, Projection, archive, and revision model.
