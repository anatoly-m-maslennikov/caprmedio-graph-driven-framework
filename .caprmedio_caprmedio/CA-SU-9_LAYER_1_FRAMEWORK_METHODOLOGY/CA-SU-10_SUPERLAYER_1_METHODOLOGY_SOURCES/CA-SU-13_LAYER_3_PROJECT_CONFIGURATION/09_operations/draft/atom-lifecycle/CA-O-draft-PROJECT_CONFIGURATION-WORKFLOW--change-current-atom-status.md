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

Change Current Atom Status

## Claim scope

This Workflow coordinates one exact non-container Current Atom under its applicable model and one requested Status admitted to that model's Current group. The Current group includes model-admitted statuses beyond Active when present and excludes Draft and Archived. It rejects containers, semantically contained Atoms, descendant selection and cascade; it does not change scope or tier.

## Claim

Change Current Atom Status **means** the reusable Workflow that enters [Set the selected Current Atom status](./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--change-current-atom-status/CA-O-draft-PROJECT_CONFIGURATION-STEP--set-the-selected-current-status.md) for the selected Atom and exact target Status.

- **Inputs:** the exact selected Current non-container Atom, its applicable model, and the requested model-admitted Current Status. The target is not selected through a custom transition matrix and is never inferred as Active.
- **Entry and order:** enter the linked Step once. A confirmed no-op or actual status change terminates complete; invalid input, missing or ambiguous artifacts, failed validation, failed effect, or uncertain readback terminates stopped. There is no automatic retry or rollback.
- **Outputs:** return the truthful no-op or changed result, including the selected predecessor, any exact archived `ID@N`, the published canonical `ID@N+1` and actual Updated At when changed, status-dependent placement, and attributable diagnostics or partial results.
- **Boundary:** an actual change preserves Atom identity, Summary, Role and content, archives the exact selected predecessor at Version N, and publishes Version N+1 under the target Status's admitted Current placement. Same Status preserves Version, time and carriers as a no-op. No promotion, Draft handling, scope/tier change, graph rebuild or descendant effect is hidden here.

The Workflow owns this single-Step graph, entry, order, transition, terminals, inputs, outputs and target boundary. It does not duplicate the Action algorithm or claim an implementation/provider binding.
