---
atom_id: CA-R-2696
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Status
version: 1
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2696-CORE_META_MODEL-DECLARATION--declare-atom-header-status.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Atom.Header.Status

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Status{:1}: [string]{:1};

Atom.Header.Status.*[]{:0};

Atom.Header.Status: Draft;

Atom.Header.Status: Active;

Atom.Header.Status: Archived
```
