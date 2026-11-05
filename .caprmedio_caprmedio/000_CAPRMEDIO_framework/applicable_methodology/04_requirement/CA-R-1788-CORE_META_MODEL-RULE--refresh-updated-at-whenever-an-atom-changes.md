---
atom_id: CA-R-1788
ref_id: CA-R-1788
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Updated At
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Header.Status
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
relations:
  child_of:
  - CA-R-1416
status: Active
version: 20
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-R-1788-CORE_META_MODEL-RULE--refresh-updated-at-whenever-an-atom-changes.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
claim_target_scope_unit: CORE_META_MODEL
current_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1788-CORE_META_MODEL-RULE--refresh-updated-at-whenever-an-atom-changes.md
  source_atom_id: CA-R-1788
  source_atom_revision: 20
  source_sha256: 3687888a36a92a5975717ad9c27c27a13aebfae219e83ef76a632561bd3d7ab0
  original_relations_sha256: f928d2096b701aa0e7852bc6d06e4620a81315e585b6a1074e66973879d77cf5
---
## Summary

Refresh Updated At whenever an Atom changes

## Claim

### Prose Claim


accepted Markdown Atom Carrier edits.


**every** actual accepted edit **to** an Atom Carrier **must** refresh that Current Atom's `updated_at` **to** the actual Project-time edit instant, including a formatting, lossless serialization, Entity-name, admitted Current Status, direct-owner, **or** current-Atom local-placement edit. an exact no-op **must** retain Updated At. When a real update publishes a successor and archives its predecessor, the Archive Carrier **must** retain the predecessor's prior Updated At, numeric Version, and unrelated content while carrying the Archived status and version-qualified identity; Git history preserves the exact pre-archive bytes. Standalone archival is not an edit to the Current Atom's content: it only materializes the Archived representation with its version-qualified identity, filename and location, so it does not create a successor or refresh Updated At.

## Details

an ancestor-only move that changes an Atom's repository locator **without** changing its own bytes, metadata, direct owner **or** placement relative **to** that owner is **not** an edit **to** that Atom. retain its Updated At **and** Version under CA-R-1432. this applies **to** **every** Atom, regardless of Content Role; it does **not** exempt an actual Status, filename, ownership **or** local-placement change. Git history retains exact pre-archive bytes.

changing a Current Atom's Status **and** publishing a Current successor is an actual update governed by CA-R-1432: archive the old-version identity with unchanged numeric Version and Updated At, while the Current successor receives its incremented Version and actual edit time. A standalone transition of the Current representation to Archived follows the exception above. timestamp encoding follows `CA-D-270-CORE_META_MODEL-DELIVERY--serialize-atom-revision-metadata-in-frontmatter`.
