---
atom_id: CA-P-036
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - metamodel-authority
    occurrent:
      - development-flow
version: 5
updated_at: 2026-08-26 15:38:45 +0400
autonomous_confidence_threshold: 98
---
# Reconcile METAMODEL authority

THE Assignee MUST make every Atom in Task Scope consistent with the accepted METAMODEL authority.

## Scope

`(ALL Atoms WHERE Current Scope = METAMODEL)`

## Definition of Done

THE Task is NOT DONE IF (ANY Atom in Task Scope conflicts with active METAMODEL authority OR ANY detected conflict lacks an Operator disposition OR the Task Scope Resolution is not recorded).

## Details

The reconciliation includes the accepted Atom, Scope Unit, Job, Requirement, relation, Epic, Task, and Subject metamodel.
