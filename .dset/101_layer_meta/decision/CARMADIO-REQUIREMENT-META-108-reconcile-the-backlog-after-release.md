---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-108
scope_path: layer:meta
subject_scopes:
  - release-reconciliation
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-105
      - CARMADIO-REQUIREMENT-META-107
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-076
      - CARMADIO-REQUIREMENT-META-077
      - CARMADIO-REQUIREMENT-META-106
---

# Requirement — Reconcile the Development Backlog after release

After the Release Record is accepted, CARMADIO reconciles the Development
Backlog against its exact released manifest.

Candidates whose promoted Atoms were fully delivered in that release are
removed from the Development Backlog. Unfinished, partially delivered,
excluded, or newly deferred candidates remain unscheduled or move to another
target version. A candidate cannot be removed as shipped unless the released
manifest accounts for its promoted Atoms.

The Development Backlog does not retain a completed-work section. The release
Record and Git history preserve what shipped and how the planning allocation
changed.

## Primary claim

Release reconciliation removes fully shipped candidates from the Development
Backlog and retains or reschedules every candidate not fully accounted for by
the released manifest.

## Rationale

The backlog remains a compact statement of future work, while immutable release
Records and Git preserve completed history without a second historical backlog.
