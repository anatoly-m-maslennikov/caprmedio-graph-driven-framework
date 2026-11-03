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

Create the proposed revision Draft

## Claim scope

This Step is the entry Step of [Update Atom via Draft](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--update-atom-via-draft.md) for one selected non-container Atom under the applicable model.

## Claim

This Step is a child of [Update Atom via Draft](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--update-atom-via-draft.md) and RUNS exactly [Create Atom Draft](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--create-atom-draft.md).

Bind the exact Current predecessor, complete proposed content or changes, explicit Draft destination, source pin, applicable model, placement and ordinary operation authorization from the enclosing Workflow Run. This Step has no prior local Step output. Its fixed boundary is one non-container target.

Return the called Workflow's exact prepared Draft and source binding, or its diagnostics/partial result, unchanged. The parent graph advances only on the verified successful result. The called Workflow owns Draft creation and identity classification; this Step adds no mutation, retry or Journal gate.
