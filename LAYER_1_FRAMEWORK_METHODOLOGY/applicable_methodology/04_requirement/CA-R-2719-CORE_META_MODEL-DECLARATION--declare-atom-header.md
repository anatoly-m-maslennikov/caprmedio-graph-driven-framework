---
atom_id: CA-R-2719
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-2719-CORE_META_MODEL-DECLARATION--declare-atom-header.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2719-CORE_META_MODEL-DECLARATION--declare-atom-header.md
  source_atom_id: CA-R-2719
  source_atom_revision: 1
  source_sha256: b44cedbf39e8d65c8dddb21a03370ed744e65daee99eff70cc0007d064ebb0e3
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Header

## Claim

### Prose Claim

Atom.Header groups the Atom Properties carried in YAML frontmatter, including for Draft Atoms.

### Formal Claim

```CFEL
# model
Atom.Header{:1}: []{:0};

Atom.Header.*[string,in(ID, Role, Form, Version, Status, Updated At, Label, Tier, Subjects, Relations, Carrier Destination, Priority, AI Agent Confidence Threshold, Work Sequence Number)]{:0+}
```

