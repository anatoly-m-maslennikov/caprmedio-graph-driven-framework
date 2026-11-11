---
atom_id: CA-D-650
ref_id: CA-D-650@14
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/File
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.ID
  - CAPRMEDIO_MODEL <+ Atom.Header.Version
tier: 3
status: archived
version: 14
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-D-650@14-CORE_META_MODEL-ENG_DECISION-CORE_META_MODEL--serialize-numbered-version-qualified-draft-atom-filenames.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Serialize numbered version-qualified Draft Atom filenames

## Claim

### Prose Claim

A Draft revision of an existing Atom carries its base canonical ID in the Header as `atom_id: <canonical-ID>`, with `status: Draft` and `version: <proposed-version>`. Its filename carries exactly one `<canonical-ID>@<proposed-version>-draft` marker as the Atom-ID segment before the remaining mutable filename components.

For an existing Atom, `<proposed-version>` follows the applicable current revision rule, normally `<current-version> + 1`. The filename marker qualifies the proposed revision; it is not a second Header identity.

A new Atom Draft allocates an unused canonical ID, carries `status: Draft` and `version: 1`, and uses the same qualified filename marker with `@1-draft`. Classification-only changes and other non-replacement edits keep the ordinary identity rule; this filename contract adds no new identity meaning.

Existing legacy Draft filenames are not normalized, renamed, or migrated automatically by this rule.
