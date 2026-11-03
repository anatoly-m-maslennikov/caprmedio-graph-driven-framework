---
atom_id: CA-O-draft
role: Operations
form: Workflow
status: Draft
version: 1
updated_at: '2026-11-03 18:54:48 +0400'
tier: 3
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Workflow'
  passive:
    - 'CAPRMEDIO_MODEL <+ Atom'
    - 'CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION'
relations: {}
---
## Summary

Archive Atom

## Claim scope

This Workflow targets exactly one explicitly selected non-container Current Atom under its applicable model, or one explicitly selected Archived version for a no-op check. Containers and implicitly selected descendants or collections are outside scope, even when no containing folder is present.

## Claim

The Archive Atom Workflow **means** a one-step lifecycle transition that enters with the exact selected source and exits with the actual archive result.

- **Step reference:** invoke [Archive the selected Current Atom](CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--archive-atom/CA-O-draft-PROJECT_CONFIGURATION-STEP--archive-the-selected-current-atom.md) once, in its declared order.
- **Inputs:** the exact explicitly selected source version, its applicable model and Scope Unit; resolve it once rather than inferring an Archived target from a missing Current. An effect uses Current version N; an explicit Archived version is admitted only for the no-op check.
- **Transition:** validate the selected source's admitted fields, Status branch, non-container boundary, placement, and write target before the Step acts. Current archival requires the qualified model to admit Archived; an explicit Archived version can only return the no-op. Do not overwrite another target.
- **Outputs:** return the Step's actual `archived` result, including the materialized ID@N/status Archived carrier and preserved Version N, Updated At, and content body; return `already_archived` when the explicitly selected version is already Archived and no write is needed.
- **Terminals:** `archived`, `already_archived`, or attributable `diagnostics` for invalid, ambiguous, missing, or conflicting input/artifact conditions. Preserve completed results on partial work; do not retry or roll back automatically.

The Workflow never creates Version N+1, promotes a Draft, cascades to descendants, retargets inbound references, deletes the Atom, or reactivates an already Archived version. Journal entries record actual business events and are not permission, completeness, or success gates.
