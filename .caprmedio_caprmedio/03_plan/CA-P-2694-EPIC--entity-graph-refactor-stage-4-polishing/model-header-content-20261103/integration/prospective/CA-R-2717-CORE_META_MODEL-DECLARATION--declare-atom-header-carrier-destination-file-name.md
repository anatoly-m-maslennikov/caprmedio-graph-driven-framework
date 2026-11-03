---
atom_id: CA-R-2717
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 1
relations: {}
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Carrier Destination.File.Name
role: Requirement
form: Declaration
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-2717-CORE_META_MODEL-DECLARATION--declare-atom-header-carrier-destination-file-name.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Atom.Header.Carrier Destination.File.Name

## Claim

### Formal Claim

```CFEL
Atom.Header.Carrier Destination.File.Name{:1}: [string]{:1};
Atom.Header.Carrier Destination.File.Name.*[]{:0}
```

### Prose Claim




Calculated full filename, including its extension.
