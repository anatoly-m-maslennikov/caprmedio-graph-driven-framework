---
atom_id: CA-R-2709
ref_id: CA-R-2709@2-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Relations
tier: 3
status: Draft
version: 2
updated_at: 2026-11-05 03:53:43 +0400
carrier_destination:
  file:
    name: CA-R-2709@2-draft-DECLARATION--declare-atom-header-relations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Declare Atom.Header.Relations

## Claim

### Prose Claim

Each child name is the canonical name of a declared Relation, and each child has one or more base Atom ID values. A present Relations group has at least one child.

### Formal Claim

```CFEL
# model
Atom.Header.Relations{::0..1} :: []{::0};

Atom.Header.Relations.*[string]{::1+};

Atom.Header.Relations.* :: [string]{::1+}
```
