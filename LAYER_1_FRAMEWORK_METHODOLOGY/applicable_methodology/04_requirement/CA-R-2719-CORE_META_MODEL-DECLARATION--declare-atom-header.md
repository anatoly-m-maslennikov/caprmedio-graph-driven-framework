---
atom_id: CA-R-2719
ref_id: CA-R-2719
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header
tier: 3
status: Active
version: 3
updated_at: 2026-11-05 22:47:24 +0400
carrier_destination:
  file:
    name: CA-R-2719-CORE_META_MODEL-DECLARATION--declare-atom-header.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2719-CORE_META_MODEL-DECLARATION--declare-atom-header.md
  source_atom_id: CA-R-2719
  source_atom_revision: 3
  source_sha256: 5980f917fe720bbcb23f194d1863f6c0f2f381548290a28d0b5ee43784bdd4fa
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
Atom.Header{::1}:: []{::0};

Atom.Header.*[string,in(ID, Ref ID, Role, Form, Version, Status, Updated At, Label, Tier, Topics, Container, Relations, Carrier Destination, Priority, AI Agent Confidence Threshold, Work Sequence Number)]{::0+};

Atom.Header.ID ;> Atom.Header.Ref ID;

Atom.Header.Ref ID ;> Atom.Header.Container;

Atom.Header.Container ;> Atom.Header.Role;

Atom.Header.Role ;> Atom.Header.Form;

Atom.Header.Form ;> Atom.Header.Label;

Atom.Header.Label ;> Atom.Header.Topics;

Atom.Header.Topics ;> Atom.Header.Tier;

Atom.Header.Tier ;> Atom.Header.Relations;

Atom.Header.Relations ;> Atom.Header.Status;

Atom.Header.Status ;> Atom.Header.Version;

Atom.Header.Version ;> Atom.Header.Updated At;

Atom.Header.Updated At ;> Atom.Header.Carrier Destination
```

