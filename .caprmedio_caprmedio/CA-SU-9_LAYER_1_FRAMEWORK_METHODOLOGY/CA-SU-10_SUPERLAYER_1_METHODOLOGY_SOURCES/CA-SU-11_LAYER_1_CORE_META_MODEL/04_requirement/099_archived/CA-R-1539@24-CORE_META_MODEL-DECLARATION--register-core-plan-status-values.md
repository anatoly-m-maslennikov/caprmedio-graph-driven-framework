---
atom_id: CA-R-1539
ref_id: CA-R-1539@24
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.State.Status'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom.Header.State.Status
tier: 2
status: Archived
version: 24
updated_at: '2026-11-11T18:31:44+04:00'
carrier_destination:
  file:
    name: CA-R-1539@24-CORE_META_MODEL-DECLARATION--register-core-plan-status-values.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Register Core Plan Status Values

## Claim

### Prose Claim


Core Plan Status values.


the Core Plan Status model **must** inherit the allowed values of Atom.Header.Status and add (Backlog, Done, Canceled). Planned **must not** be a distinct Plan Status.

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in (Plan)).Header.State.Status :: Backlog;

Atom/(.Header.Context.Role := Plan)/(.Header.State.Status := Backlog).Header.State.Status >| Status Group == Backlog;

Atom/(.Header.Context.Role in (Plan)).Header.State.Status :: Done;

Atom/(.Header.Context.Role in (Plan)).Header.State.Status :: Canceled
```
