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

Promote Atom Draft

## Claim scope

This Workflow handles one exact selected Draft for one non-container Atom under the applicable model. It rejects semantic containers and does not select descendants or perform a cascade.

## Claim

Promote Atom Draft **means** the one-target Workflow that publishes a validated proposal from a Draft into its canonical Current destination. The caller supplies the exact Draft, complete proposed content/Role/meaning, and an explicit target Status admitted as Current by the applicable qualified model. In a composed Create Draft -> Archive -> Promote update, this Workflow starts only after the separate Archive Workflow has returned its verified result; it does not hide or perform archival.

The Workflow's boundary is exactly one non-container Atom. Its entry inputs are that exact Draft, its destination placement and proposed Version (plus its intended canonical ID only for an existing-Atom Draft), the applicable model and placement, and the explicit target Status. The Workflow declares one ordered Step, [`Promote the selected Atom Draft`](CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--promote-atom-draft/CA-O-draft-PROJECT_CONFIGURATION-STEP--promote-the-selected-atom-draft.md), invoked once. Its output is the actual published Current and verified Draft removal, or the attributable collision, handoff, diagnostic, partial, or unknown result with completed effects retained. A valid Step completes the Workflow; any failure or uncertainty stops it without automatic retry, rollback, or a second Step.

The referenced Step owns the single Action binding and its execution details. This Workflow owns only the one-target boundary, entry, order, transitions, terminals, and inputs/outputs; it does not duplicate the Action algorithm.

