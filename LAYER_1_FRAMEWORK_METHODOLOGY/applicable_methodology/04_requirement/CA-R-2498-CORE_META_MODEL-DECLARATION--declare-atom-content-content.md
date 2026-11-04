---
atom_id: CA-R-2498
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content
version: 5
updated_at: 2026-11-04 05:21:15 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2498-CORE_META_MODEL-DECLARATION--declare-atom-content-content.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2498-CORE_META_MODEL-DECLARATION--declare-atom-content-content.md
  source_atom_id: CA-R-2498
  source_atom_revision: 5
  source_sha256: 1c9fc5041d0eda8854d2a1793e93f9eb873f0f305e2db29846e20cf2db843609
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Content

## Claim

### Formal Claim

```CFEL
# model
Atom.Content{:1}: []{:0};

Atom.Content.*[string]{:0+};

Atom.Content.**[string]{:0+};

Atom.Content.**: [markdown]
```

