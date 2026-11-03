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

Archive the exact revision predecessor

## Claim scope

This Step is the second Step of [Update Atom via Draft](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--update-atom-via-draft.md) for one selected non-container Atom under the applicable model.

## Claim

This Step is a child of [Update Atom via Draft](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--update-atom-via-draft.md) and RUNS exactly [Archive Atom](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--archive-atom.md).

Bind the exact predecessor and ordinary operation authorization from the enclosing Workflow Run, and its verified source binding from [Create the proposed revision Draft](./CA-O-draft-PROJECT_CONFIGURATION-STEP--create-the-proposed-revision-draft.md). The prior result must identify the prepared validated Draft before this Step is admitted. Bind only that predecessor; no history search or descendant selection is added.

Return the called Workflow's exact archived predecessor and verified result, or diagnostics/partial results, unchanged. Archive Atom owns the archival behavior. The parent graph controls continuation; this Step adds no second effect, retry, rollback or Journal gate.
