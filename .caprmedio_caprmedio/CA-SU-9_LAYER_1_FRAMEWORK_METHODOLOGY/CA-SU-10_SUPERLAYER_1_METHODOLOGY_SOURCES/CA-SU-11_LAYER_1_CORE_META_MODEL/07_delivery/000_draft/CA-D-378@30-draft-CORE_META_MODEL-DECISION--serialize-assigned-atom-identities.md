---
atom_id: CA-D-378@30-draft
ref_id: CA-D-378@30-draft
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Identity.ID
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Role
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)
tier: 3
status: Draft
version: 30
updated_at: 2026-11-05 22:19:14 +0400
carrier_destination:
  file:
    name: CA-D-378@30-draft-CORE_META_MODEL-DECISION--serialize-assigned-atom-identities.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/000_draft
---
## Summary

Serialize Assigned Atom Identities

## Claim

### Prose Claim

Every assigned Current or Archived Atom ID must begin with the registered uppercase Project identity prefix and match `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-<GLOBAL_NUMBER_WITHIN_CONTENT_ROLE>`. The Content Role Identity Letter is one of `C`, `A`, `P`, `R`, `M`, `E`, `D`, or `O`.

For an existing-Atom Draft, `atom_id` is exactly `<canonical-ID>@<proposed-version>-draft`. Use the numeric Header `version` as `<proposed-version>`; its filename identity segment is that same marker.

For a role-only Draft, `atom_id` and its filename identity segment are the role-only `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-draft` marker. [CA-R-1432@28-draft](../../04_requirement/draft/lifecycle-in-place-edits/CA-R-1432@28-draft-CORE_META_MODEL-RULE--govern-atom-lifecycle-identity-and-version.md) governs which marker applies and, at successful publication, the fresh canonical ID and Version 1 outcome.

[CA-D-650@15-draft](CA-D-650@15-draft-CORE_META_MODEL-DECISION--serialize-numbered-version-qualified-draft-atom-filenames.md) assembles the marker into the filename.
