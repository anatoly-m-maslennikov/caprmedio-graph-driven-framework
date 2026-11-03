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

Promote the prepared revision Draft

## Claim scope

This Step is the terminal Step of [Update Atom via Draft](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--update-atom-via-draft.md) for one selected non-container Atom under the applicable model.

## Claim

This Step is a child of [Update Atom via Draft](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--update-atom-via-draft.md) and RUNS exactly [Promote Atom Draft](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--promote-atom-draft.md).

Bind the exact prepared Draft from [Create the proposed revision Draft](./CA-O-draft-PROJECT_CONFIGURATION-STEP--create-the-proposed-revision-draft.md), the verified exact archived predecessor from [Archive the exact revision predecessor](./CA-O-draft-PROJECT_CONFIGURATION-STEP--archive-the-exact-revision-predecessor.md), and the previously resolved model-admitted Current Status, destination placement and ordinary authorization from the enclosing Workflow Run. Admit this Step only after both prior results are verified.

Return the called Workflow's actual publication and identity mapping, or diagnostics/partial results, unchanged. The parent Workflow retains the explicit predecessor/successor replacement mapping when identities differ. Promote Atom Draft owns publication and selected Draft cleanup; this Step adds no archival, identity inference, retry, rollback or Journal gate.
