---
atom_id: CA-R-1608
ref_id: CA-R-1608
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Concern).Header.State.Status'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Concern)
  - CAPRMEDIO_MODEL <+ Atom.Header.State.Status
tier: 2
status: Active
version: 23
updated_at: '2026-11-11T19:34:00+04:00'
carrier_destination:
  file:
    name: CA-R-1608-CORE_META_MODEL-DECLARATION--register-core-concern-status-values.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Register Core Concern Status Values

## Claim

### Prose Claim


the Core Concern Status model.


the Core Concern Status model **must** inherit the allowed values of Atom.Header.Status and add (Resolved, Canceled).

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in (Concern)).Header.State.Status :: Resolved;

Atom/(.Header.Context.Role in (Concern)).Header.State.Status :: Canceled;

Atom/(.Header.State.Status := Resolved).Header.State.Status >| (Status Order Number == 21);
```
