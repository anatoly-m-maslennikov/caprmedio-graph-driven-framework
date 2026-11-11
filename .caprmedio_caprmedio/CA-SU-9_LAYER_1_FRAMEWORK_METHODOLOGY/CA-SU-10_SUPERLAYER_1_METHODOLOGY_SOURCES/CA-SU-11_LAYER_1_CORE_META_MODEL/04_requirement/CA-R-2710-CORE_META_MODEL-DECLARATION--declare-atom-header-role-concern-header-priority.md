---
atom_id: CA-R-2710
ref_id: CA-R-2710
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Concern).Header.Context.Concern.Priority
tier: 3
status: Active
version: 2
updated_at: '2026-11-11 16:04:42 +0400'
carrier_destination:
  file:
    name: CA-R-2710-CORE_META_MODEL-DECLARATION--declare-atom-header-role-concern-header-priority.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom/(.Header.Role := Concern).Header.Priority

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in (Concern)).Header.Context.Concern.Priority{::1}:: [string]{::1};

Atom/(.Header.Context.Role in (Concern)).Header.Context.Concern.Priority.*[]{::0};

Atom/(.Header.Context.Role in (Concern)).Header.Context.Concern.Priority :: High;

Atom/(.Header.Context.Role in (Concern)).Header.Context.Concern.Priority :: Medium;

Atom/(.Header.Context.Role in (Concern)).Header.Context.Concern.Priority :: Low
```
