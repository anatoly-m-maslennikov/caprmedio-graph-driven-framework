---
atom_id: CA-R-2966
ref_id: CA-R-2966
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Ref ID
tier: 3
status: Active
version: 1
updated_at: 2026-11-05 22:47:24 +0400
carrier_destination:
  file:
    name: CA-R-2966-CORE_META_MODEL-DECLARATION--declare-atom-header-ref-id.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2966-CORE_META_MODEL-DECLARATION--declare-atom-header-ref-id.md
  source_atom_id: CA-R-2966
  source_atom_revision: 1
  source_sha256: b422959cc8d649c07cd8fda6f2cbdb91d5c4b546af46790618380da3cdf01bf2
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Header.Ref ID

## Claim

### Prose Claim

For a Current Atom, Ref ID is its base Atom ID. For an Archived Atom, Ref ID is `<ID>@<Version>`. For a Draft Atom, Ref ID is `<ID>@<Version>-draft`.

### Formal Claim

```CFEL
# model
Atom.Header.Ref ID{::1} :: [string]{::1};

Atom.Header.Ref ID.*[]{::0}
```
