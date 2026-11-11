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

Atom/(.Header.Context.Role in RMED).Content.Summary ;> Atom/(.Header.Context.Role in RMED).Content.Claim;

Atom/(.Header.Context.Role in RMED).Content.Claim ;> Atom/(.Header.Context.Role in RMED).Content.Semantics;

Atom/(.Header.Context.Role in RMED).Content.Semantics ;> Atom/(.Header.Context.Role in RMED).Content.Details
```

