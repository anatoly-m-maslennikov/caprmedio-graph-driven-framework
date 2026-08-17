---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-111
scope_path: layer:gov
subject_scopes:
  - runtime
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-043
      - CAPRMADIO-REQUIREMENT-GOV-100
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-053
---

# Requirement — Separate control, journal, runtime, and scratch state

Every CAPRMADIO project uses four distinct storage boundaries:

| Boundary | Owned content | Revision behavior |
|---|---|---|
| `.caprmadio/` | Governed Atoms and Projections, installed methodology, settings, tools, skill instructions, schemas, and templates | Atom revisions are Git-bound; Projections and configuration update through Git |
| `.caprmadio_journal/` | Canonical running logs, event streams, audit trails, and ordered record sequences | Append-only NDJSON |
| `.caprmadio_runtime/` | Ignored reconstructible or resumable run state, checkpoints, caches, recovery material, and temporary materializations | Mutable and disposable between completed workflows |
| Host temporary root | Process scratch and test workspaces | Disposable; cleaned when the owning operation exits |

Nothing under `.caprmadio_runtime` or the host temporary root may be the only copy
of governed truth, durable history, or canonical evidence. CAPRMADIO scratch uses
the operating system's native temporary root and never an ambient path that
places scratch in the repository. Cleanup failure is reported as failure.

Every journal line is one complete UTF-8 JSON record followed by a newline.
Accepted records are never edited, reordered, or deleted. Rotation may create
or seal carriers without rewriting accepted records. A persisted TOON or other
summary is a Projection; the selected NDJSON frontier remains canonical for
its Ops records.

Short-lived same-directory swap state may exist only for atomic publication
and must be replaced or removed before the operation returns.

## Primary claim

CAPRMADIO separates governed control state, canonical append-only journals,
reconstructible runtime state, and disposable host scratch into four explicit
boundaries.

## Rationale

The merged boundary removes the former conflict over whether runtime state is
resumable or scratch and protects append-only Ops records from both cleanup
paths.
