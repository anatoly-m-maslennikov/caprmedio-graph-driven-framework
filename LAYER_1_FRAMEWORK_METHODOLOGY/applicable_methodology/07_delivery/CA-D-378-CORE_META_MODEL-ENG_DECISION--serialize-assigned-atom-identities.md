---
atom_id: CA-D-378
ref_id: CA-D-378
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.ID
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
tier: 3
status: active
version: 31
updated_at: 2026-11-09 00:51:00 +0400
carrier_destination:
  file:
    name: CA-D-378-CORE_META_MODEL-ENG_DECISION--serialize-assigned-atom-identities.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-378-CORE_META_MODEL-ENG_DECISION--serialize-assigned-atom-identities.md
  source_atom_id: CA-D-378
  source_atom_revision: 31
  source_sha256: c573495a8f88f13ab1b6d0ab0fb76d79dec923631294c67f2d182cac1a3f0e2b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Assigned Atom Identities

## Claim

### Prose Claim

Every assigned Current or Archived Atom ID must begin with the registered uppercase Project identity prefix and match `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-<GLOBAL_NUMBER_WITHIN_CONTENT_ROLE>`. The Content Role Identity Letter is one of `C`, `A`, `P`, `R`, `M`, `E`, `D`, or `O`.

Every Draft carries its exact base canonical ID and positive integer Version at their declared Header paths. The logical Status is Draft, encoded as `draft` by the common YAML rule. Its filename carries exactly one `<canonical-ID>@<version>-draft` marker before the remaining mutable filename components.

For a Draft revision of an existing Atom, `<version>` follows the applicable current-version-plus-one rule. A new Atom Draft allocates an unused canonical ID and uses integer Version 1 at its declared Header path with the same qualified `@1-draft` filename marker. Classification-only changes and other non-replacement edits retain the ordinary identity rule; this Draft marker does not add a new identity meaning.

Existing legacy Draft filenames are not normalized, renamed, or migrated automatically by this rule.
