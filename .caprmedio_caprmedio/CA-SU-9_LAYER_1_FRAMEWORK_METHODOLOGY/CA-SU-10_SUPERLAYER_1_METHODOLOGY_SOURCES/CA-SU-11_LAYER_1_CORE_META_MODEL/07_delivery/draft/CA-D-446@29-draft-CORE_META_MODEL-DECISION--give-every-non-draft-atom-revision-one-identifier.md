---
atom_id: CA-D-446@29-draft
ref_id: CA-D-446@29-draft
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.ID
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Version
  - 'CAPRMEDIO_MODEL <+ Atom.Header.Status: Draft'
tier: 1
status: Draft
version: 29
updated_at: 2026-11-05 22:19:14 +0400
carrier_destination:
  file:
    name: CA-D-446@29-draft-CORE_META_MODEL-DECISION--give-every-non-draft-atom-revision-one-identifier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/draft
---
## Summary

Give Every Non-Draft Atom Revision One Identifier

## Claim

### Prose Claim

For each canonical Atom ID, at most one Current Atom source may exist across all admitted Status values. Every Current or Archived Atom version is identified by exactly one canonical Atom ID and numeric `version`; no second `identifier` field is admitted. Archived versions retain that canonical ID at distinct Version Numbers.

Draft markers are defined by [CA-D-378@30-draft](CA-D-378@30-draft-CORE_META_MODEL-DECISION--serialize-assigned-atom-identities.md), and Draft filename assembly is defined by [CA-D-650@15-draft](CA-D-650@15-draft-CORE_META_MODEL-DECISION--serialize-numbered-version-qualified-draft-atom-filenames.md). Those markers do not change the Current-source uniqueness rule.

An admitted status edit does not create a second concurrent Draft Carrier. [CA-R-1432@28-draft](../../04_requirement/draft/lifecycle-in-place-edits/CA-R-1432@28-draft-CORE_META_MODEL-RULE--classify-admitted-atom-changes-by-semantic-effect.md) governs semantic operation and Version outcomes; [CA-R-1788@19-draft](../../04_requirement/draft/lifecycle-in-place-edits/CA-R-1788@19-draft-CORE_META_MODEL-RULE--refresh-updated-at-whenever-an-atom-changes.md) governs timestamps; [CA-D-568@20-draft](lifecycle-in-place-edits/CA-D-568@20-draft-CORE_META_MODEL-DECISION--bind-draft-identity-continuity-evidence.md) governs historical-ID retention.
