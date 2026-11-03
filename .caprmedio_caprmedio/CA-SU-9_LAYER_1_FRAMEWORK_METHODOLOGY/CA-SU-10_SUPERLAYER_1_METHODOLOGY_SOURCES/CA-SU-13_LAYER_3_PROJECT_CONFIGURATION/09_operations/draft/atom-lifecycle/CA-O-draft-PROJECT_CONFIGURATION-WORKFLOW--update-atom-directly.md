---
atom_id: CA-O-draft
role: Operations
form: Workflow
status: Draft
version: 1
updated_at: '2026-11-03 19:01:50 +0400'
tier: 3
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Workflow'
  passive:
    - 'CAPRMEDIO_MODEL <+ Atom'
    - 'CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION'
relations: {}
---
## Summary

Update Atom Directly

## Claim scope

One explicitly selected non-container Atom: an editable Draft, or a Current or Archived Atom needing technical changes.

## Claim

Accept the selected Atom and requested changes. Derive the update case from its resolved Status and applicable model; the caller does not choose a separate mode.

Entry and sole node: [Apply the requested Direct Atom Update](CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--update-atom-directly/CA-O-draft-PROJECT_CONFIGURATION-STEP--apply-the-requested-direct-atom-update.md). Run it once and return its actual changed Atom, no-op, diagnostics, partial result, or handoff. A valid semantic change to Current returns a handoff to Update Atom via Draft without invoking it. Invalid, ambiguous or stale inputs return diagnostics.

Draft proposal content is editable in place. Technical Current and Archived changes follow the linked Action's ordinary validation and update rules. Git retains previous carrier revisions; Archived repairs have no special metadata-preservation requirement.

The Workflow owns its entry, order and terminal results. The Step owns its binding. Containers and descendants are outside scope; failures retain actual completed results without automatic retry or rollback. Journal recording is not an admission or success gate.
