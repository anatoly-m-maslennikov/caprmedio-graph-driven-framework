---
atom_id: CA-O-draft
role: Operations
form: Step
status: Draft
version: 1
updated_at: '2026-11-03 18:54:48 +0400'
tier: 3
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Step'
  passive:
    - 'CAPRMEDIO_MODEL <+ Atom'
    - 'CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION'
relations: {}
---
## Summary

Archive the selected Current Atom

## Claim scope

This Step is the single Step of Archive Atom and handles its exact selected non-container Current Atom, or an explicitly selected Archived version for a no-op check.

## Claim

The Archive the selected Current Atom Step names [Archive Atom](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--archive-atom.md) as its parent Workflow and **RUNS** [Archive one Current Atom Action](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--archive-one-current-atom.md) exactly once.

- Bind the exact selected source version, applicable model and Scope Unit from the enclosing Workflow inputs; use the fixed target status `Archived`. The Action owns Current admission and the explicit Archived-version no-op check.
- Pass the Action's actual terminal result back to the parent Workflow unchanged, including `archived`, `already_archived`, or attributable diagnostics and any completed result.
- Add no descendant traversal, Draft promotion, reference retargeting, retry, rollback, or alternative Action binding; the reusable archive behavior remains in the linked Action.
