---
atom_id: CA-R-2709
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Relations
version: 2
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
updated_at: 2026-11-05 03:53:43 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2709@2-draft-CORE_META_MODEL-DECLARATION--declare-atom-header-relations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Declare Atom.Header.Relations

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Relations{::0..1} :: []{::0};

# instances
Atom.Header.Relations.*[Relation//$relation]{::0+}
```
