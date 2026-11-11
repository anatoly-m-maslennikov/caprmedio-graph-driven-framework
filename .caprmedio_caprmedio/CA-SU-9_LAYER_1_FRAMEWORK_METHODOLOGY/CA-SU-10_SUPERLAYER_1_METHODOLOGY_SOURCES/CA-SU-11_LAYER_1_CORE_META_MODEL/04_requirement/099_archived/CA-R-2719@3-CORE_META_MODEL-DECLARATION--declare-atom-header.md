---
atom_id: CA-R-2719
ref_id: CA-R-2719@3
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header
tier: 3
status: Archived
version: 3
updated_at: 2026-11-05 22:47:24 +0400
carrier_destination:
  file:
    name: CA-R-2719@3-CORE_META_MODEL-DECLARATION--declare-atom-header.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archived
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

