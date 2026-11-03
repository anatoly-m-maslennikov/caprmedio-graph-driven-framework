---
atom_id: CA-R-2718
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 2
relations: {}
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Carrier Destination.File.Path
role: Requirement
form: Declaration
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-R-2718-CORE_META_MODEL-DECLARATION--declare-atom-header-carrier-destination-file-path.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Atom.Header.Carrier Destination.File.Path

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Carrier Destination.File.Path: [string]{:1};

Atom.Header.Carrier Destination.File.Path.*[]{:0}
```

### Prose Claim




Calculated path of the containing directory, relative to the repository root.
