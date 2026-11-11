---
atom_id: CA-R-2710
ref_id: CA-R-2710@1
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern).Header.Priority
tier: 3
status: Archived
version: 1
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-2710@1-CORE_META_MODEL-DECLARATION--declare-atom-header-role-concern-header-priority.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom/(.Header.Role := Concern).Header.Priority

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role: Concern).Header.Priority{::1}:: [string]{::1};

Atom/(.Header.Role: Concern).Header.Priority.*[]{::0};

Atom/(.Header.Role: Concern).Header.Priority: High;

Atom/(.Header.Role: Concern).Header.Priority: Medium;

Atom/(.Header.Role: Concern).Header.Priority: Low
```
