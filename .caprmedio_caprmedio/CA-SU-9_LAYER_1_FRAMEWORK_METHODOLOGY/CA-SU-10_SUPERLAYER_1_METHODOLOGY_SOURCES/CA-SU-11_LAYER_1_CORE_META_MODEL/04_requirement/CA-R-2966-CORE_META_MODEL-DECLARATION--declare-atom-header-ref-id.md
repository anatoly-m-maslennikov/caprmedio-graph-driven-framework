---
atom_id: CA-R-2966
ref_id: CA-R-2966
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Identity.Ref ID
tier: 3
status: Active
version: 2
updated_at: '2026-11-11T18:31:44+04:00'
carrier_destination:
  file:
    name: CA-R-2966-CORE_META_MODEL-DECLARATION--declare-atom-header-ref-id.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Atom.Header.Ref ID

## Claim

### Prose Claim

For an Atom in the Current or Backlog Status Group, Ref ID is its base Atom ID. For an Archived Atom, Ref ID is `<ID>@<Version>`. For a Draft Atom, Ref ID is `<ID>@<Version>-draft`.

### Formal Claim

```CFEL
# model
Atom.Header.Identity.Ref ID{::1} :: [string]{::1};

Atom.Header.Identity.Ref ID.*[]{::0}
```
