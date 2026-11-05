---
atom_id: CA-R-2705
ref_id: CA-R-2705
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Label
tier: 3
status: Active
version: 4
updated_at: 2026-11-04 20:33:16 +0400
carrier_destination:
  file:
    name: CA-R-2705-DECLARATION--declare-atom-header-label.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2705-CORE_META_MODEL-DECLARATION--declare-atom-header-label.md
  source_atom_id: CA-R-2705
  source_atom_revision: 4
  source_sha256: 294518348c7343fad922df0c8738c6d4c9d2319c3ea2265a3045573620582416
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Header.Label

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Label:: [string]{::0..1};

Atom.Header.Label.*[]{::0};

# instances
Atom//$atom;

$atom.Header.Label ?== $atom.Header.Form
```
