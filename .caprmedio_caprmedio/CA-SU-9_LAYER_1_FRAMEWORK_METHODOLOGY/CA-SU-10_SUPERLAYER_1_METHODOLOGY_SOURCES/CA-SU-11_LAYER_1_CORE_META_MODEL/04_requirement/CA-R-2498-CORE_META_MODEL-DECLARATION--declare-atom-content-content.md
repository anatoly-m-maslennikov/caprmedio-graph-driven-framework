---
atom_id: CA-R-2498
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content
version: 4
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2498-CORE_META_MODEL-DECLARATION--declare-atom-content-content.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Atom.Content

## Claim

### Formal Claim

```CFEL
# model
Atom.Content{:1}: []{:0};

Atom.Content.*[string]{:0+};

Atom.Content.**[string]{:0+}: [markdown]{:0..1}
```

