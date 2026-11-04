---
atom_id: CA-R-2719
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header
version: 2
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-05 03:53:43 +0400
carrier_destination:
  file:
    name: CA-R-2719@2-draft-CORE_META_MODEL-DECLARATION--declare-atom-header.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
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

Atom.Header.*[string,in(ID, Role, Form, Version, Status, Updated At, Label, Tier, Subjects, Relations, Container, Carrier Destination, Priority, AI Agent Confidence Threshold, Work Sequence Number)]{::0+}
```

