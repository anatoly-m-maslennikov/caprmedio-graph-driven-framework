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

Promote the selected Atom Draft

## Claim scope

This Step operates on the one exact non-container Draft selected by its parent Workflow. It has no descendant selection or cascade and no earlier Step output.

## Claim

Promote the selected Atom Draft is the single Step of [Promote Atom Draft](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--promote-atom-draft.md) and RUNS exactly [Promote one Atom Draft](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--promote-one-atom-draft.md).

Bind every variable input from the enclosing Promote Workflow Run: the exact Draft, its destination placement, complete proposal, applicable model and permissions, explicit model-admitted Current Status, and any explicitly supplied archived predecessor. An existing-Atom Draft supplies its intended canonical ID and proposed Version; a role-only Draft leaves canonical ID allocation to the Action. The caller may supply an earlier outer Workflow result as this Workflow's input; this Step does not read foreign Step outputs directly.

Return the Action's actual publication, verified Draft removal, collision/handoff, diagnostics or partial result unchanged. Add no archival, other Action, retry or rollback; the linked Action owns publication behavior.

