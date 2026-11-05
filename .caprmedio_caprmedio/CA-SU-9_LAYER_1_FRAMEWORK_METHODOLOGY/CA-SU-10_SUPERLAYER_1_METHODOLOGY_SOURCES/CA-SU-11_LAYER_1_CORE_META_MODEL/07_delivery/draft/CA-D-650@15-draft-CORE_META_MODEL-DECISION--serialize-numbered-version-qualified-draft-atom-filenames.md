---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/File
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.ID
  - CAPRMEDIO_MODEL <+ Atom.Header.Version
version: 15
updated_at: 2026-11-05 22:19:14 +0400
atom_id: CA-D-650@15-draft
ref_id: CA-D-650@15-draft
status: Draft
tier: 3
role: Delivery
form: Decision
carrier_destination:
  file:
    name: CA-D-650@15-draft-CORE_META_MODEL-DECISION--serialize-numbered-version-qualified-draft-atom-filenames.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/draft
container:
  scope_unit: CA-SU-11
---
## Summary

Serialize numbered version-qualified Draft Atom filenames

## Claim

### Prose Claim

[CA-D-378@30-draft](CA-D-378@30-draft-CORE_META_MODEL-DECISION--serialize-assigned-atom-identities.md) defines the Draft `atom_id` marker. Assemble that exact marker as the filename's Atom-ID segment before the remaining mutable filename components.

Existing legacy Draft filenames remain readable and are not normalized, renamed, or migrated automatically.
