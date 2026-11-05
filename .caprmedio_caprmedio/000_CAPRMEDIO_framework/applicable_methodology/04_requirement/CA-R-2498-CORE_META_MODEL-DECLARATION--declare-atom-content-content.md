---
atom_id: CA-R-2498
ref_id: CA-R-2498
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Content
tier: 3
status: Active
version: 6
updated_at: 2026-11-05 22:47:24 +0400
carrier_destination:
  file:
    name: CA-R-2498-CORE_META_MODEL-DECLARATION--declare-atom-content.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2498-CORE_META_MODEL-DECLARATION--declare-atom-content-content.md
  source_atom_id: CA-R-2498
  source_atom_revision: 6
  source_sha256: 433cb32f1c406bd5adfb0baaa1f9fa58561a2a4c8807dbf764a6fdb666ea08fd
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Content

## Claim

### Formal Claim

```CFEL
# model
Atom.Content{::1}:: []{::0};

Atom.Content.*[string]{::0+};

Atom.Content.**[string]{::0+};

Atom.Content.**:: [markdown];

Atom/(.Header.Role in RMED).Content.Summary ;> Atom/(.Header.Role in RMED).Content.Claim;

Atom/(.Header.Role in RMED).Content.Claim ;> Atom/(.Header.Role in RMED).Content.Semantics;

Atom/(.Header.Role in RMED).Content.Semantics ;> Atom/(.Header.Role in RMED).Content.Details
```

