---
identity:
  atom_id: CA-R-2709
  ref_id: CA-R-2709
context:
  container:
    scope_unit: CA-SU-11
  role: Requirement
  form: Declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Relations
  tier: 3
state:
  status: Active
  version: 5
  updated_at: 2026-11-08 20:06:37 +0400
destination:
  file:
    name: CA-R-2709-CORE_META_MODEL-DECLARATION--declare-atom-header-relations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2709-CORE_META_MODEL-DECLARATION--declare-atom-header-relations.md
  source_atom_id: CA-R-2709
  source_atom_revision: 5
  source_sha256: f8328fd465ef0adcafb16c1480712a99b3d738add52689dcc655b9ece90822e3
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Header.Relations

## Claim

### Prose Claim

Each child name is the canonical name of a declared Relation, and each child has one or more base Atom ID values. A present Relations group has at least one child.

The replacement Atom stores IS_REPLACEMENT_FOR with its predecessor Atom IDs.

### Formal Claim

```CFEL
# model
Atom.Header.Relations{::0..1} :: []{::0};

Atom.Header.Relations.*[string]{::1+};

Atom.Header.Relations.* :: [string]{::1+}
```
