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

This Step is the single ordered Step of [Atom Lifecycle_Change Current Status](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-change-current-status.md) and handles exactly one non-container Current Atom. It does not widen the Workflow boundary or select descendants.

## Claim

This Step belongs to [Atom Lifecycle_Change Current Status](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-change-current-status.md) and RUNS exactly [Set one Current Atom Status](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--set-one-current-atom-status.md) under [CA-R-2638](../../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2638-CORE_META_MODEL-DECLARATION--define-runs.md).

Bind the exact Current Atom, qualified model, requested Current-group Status, expected source/currentness, placement and authorization under [CA-R-2639](../../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2639-CORE_META_MODEL-RULE--bind-step-parameters.md). Pass the Action's saved result or explicit error with completed partial outputs unchanged. Do not retry, replay, or roll back; this Step adds no transition matrix, second Action, promotion, or descendant selection.
