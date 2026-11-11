---
atom_id: CA-R-2696
ref_id: CA-R-2696@2
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.State.Status
tier: 3
status: Archived
version: 2
updated_at: '2026-11-11 13:45:22 +0400'
carrier_destination:
  file:
    name: CA-R-2696@2-CORE_META_MODEL-DECLARATION--declare-atom-header-status.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom.Header.Status

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.State.Status{::1}:: [string]{::1};

Atom.Header.State.Status.*[]{::0};

Atom.Header.State.Status :: Draft;

Atom.Header.State.Status :: Active;

Atom.Header.State.Status :: Archived
```
