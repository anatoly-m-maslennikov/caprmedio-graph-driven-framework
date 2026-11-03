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

Set the selected Current Status

## Claim scope

This Step is the single ordered Step of [Change current Atom status](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--change-current-atom-status.md) and handles exactly one non-container Current Atom. It does not widen the Workflow boundary or select descendants.

## Claim

Set the selected Current Atom Status **means** the Step that runs exactly [Set one Current Atom status](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--set-one-current-atom-status.md).

- **Inputs bound from the enclosing Workflow:** the exact selected Current Atom, its applicable model and the requested exact model-admitted Current Status.
- **Action binding:** the linked Action is the only operation run by this Step; no second Action, hidden promotion, Draft handling, transition matrix, scope/tier change or graph operation is introduced.
- **Result:** pass through the Action's truthful no-op, changed, stopped, partial or diagnostic result to the enclosing Workflow, including exact predecessor/successor identities, versions, actual time and placement when supplied.

This Step defines only the parent link, one Action binding and input/result handoff; the status-effect algorithm remains in the linked Action.
