---
atom_id: CA-O-draft
role: Operations
form: Step
status: Draft
version: 1
updated_at: '2026-11-03 18:54:48 +0400'
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Step
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
relations: {}
---
## Summary

Create the requested Atom Draft

## Claim scope

PROJECT_CONFIGURATION

## Claim

This is the sole ordered Step of [Create one Atom Draft](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--create-atom-draft.md). It `RUNS` exactly one Action, [Create one Atom Draft](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--create-one-atom-draft.md), once. It binds the enclosing Workflow's exact source, distinct destination, complete proposed content/changes, requested Summary and Role, proposedVersion when applicable, model, permission, and expected preconditions; it binds the fixed result status `Draft` explicitly. No earlier Step output, hidden edit Step, source inference, history gate, container selection, or executable grammar is introduced.

Before dispatch it preserves the Workflow's one non-container target boundary and exact-once source resolution. It forwards missing/null, explicit Current, explicit Draft-copy, and explicit Archived-as-new-Draft cases to the Action without changing their meaning. It returns the Action's materialized carrier, marker, proposed Version, replacementSummaryRole mapping, diagnostics, choices, and partial-result evidence unchanged to the parent Workflow; it adds no retry, rollback, or routing decision.

