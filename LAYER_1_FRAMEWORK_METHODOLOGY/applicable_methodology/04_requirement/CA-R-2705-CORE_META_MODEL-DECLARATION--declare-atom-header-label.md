---
atom_id: CA-R-2705
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Label
version: 4
updated_at: 2026-11-04 20:33:16 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2705-CORE_META_MODEL-DECLARATION--declare-atom-header-label.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2705-CORE_META_MODEL-DECLARATION--declare-atom-header-label.md
  source_atom_id: CA-R-2705
  source_atom_revision: 4
  source_sha256: 10aa1de37838a749b0309925b90b395999f8ddff50a2c0b28fdc1fed94085f44
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---
## Summary

Declare Atom.Header.Label

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Label: [string]{:0..1};

Atom.Header.Label.*[]{:0};

# instances
Atom//$atom;

$atom.Header.Label ?== $atom.Header.Form
```
