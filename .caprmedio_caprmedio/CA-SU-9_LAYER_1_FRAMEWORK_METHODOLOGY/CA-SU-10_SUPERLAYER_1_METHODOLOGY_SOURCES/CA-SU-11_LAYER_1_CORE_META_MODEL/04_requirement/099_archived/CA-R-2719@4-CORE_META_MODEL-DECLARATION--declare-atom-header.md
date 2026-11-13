---
atom_id: CA-R-2719
ref_id: CA-R-2719@4
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header
tier: 3
status: archived
version: 4
updated_at: 2026-11-11 16:27:40 +0400
carrier_destination:
  file:
    name: CA-R-2719@4-CORE_META_MODEL-DECLARATION--declare-atom-header.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom.Header

## Claim

### Prose Claim

Atom.Header groups the Atom Properties carried in YAML frontmatter, including for Draft Atoms.

### Formal Claim

```CFEL
# model
Atom.Header{::1} :: []{::0};

Atom.Header.*[string, in (Identity, Context, Relations, State, Destination)]{::0+};

Atom.Header.Identity ;> Atom.Header.Context;

Atom.Header.Context ;> Atom.Header.Relations;

Atom.Header.Relations ;> Atom.Header.State;

Atom.Header.State ;> Atom.Header.Destination
```

