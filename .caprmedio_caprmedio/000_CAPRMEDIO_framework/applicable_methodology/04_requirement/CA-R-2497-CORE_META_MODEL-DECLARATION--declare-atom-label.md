---
atom_id: CA-R-2497
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Label
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2497-CORE_META_MODEL-DECLARATION--declare-atom-label.md
  source_atom_id: CA-R-2497
  source_atom_revision: 2
  source_sha256: 7d063295096037da8299c8fa2291ace5f454c18904baeea7e125c80b71509724
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Label

## Claim

```CFEL
Atom.Label{:0..1}: [string]{:1};
Atom.Label.*[]{:0};
Atom.Label ?= Atom.Form
```
