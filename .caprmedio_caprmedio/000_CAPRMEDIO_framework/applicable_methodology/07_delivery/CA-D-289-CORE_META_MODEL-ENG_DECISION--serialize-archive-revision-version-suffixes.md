---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Header.Version
version: 25
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
atom_id: CA-D-289
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-289-CORE_META_MODEL-ENG_DECISION--serialize-archive-revision-version-suffixes.md
  source_atom_id: CA-D-289
  source_atom_revision: 25
  source_sha256: bc3bca6d64669800aab3c661cbc2cc6e1756fa84db0438617d6f09dd3f0314e0
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Archive Revision Version Suffixes

## Claim

### Prose Claim


Archive Carrier basenames for Archived Atom versions.


**every** Archived Atom Carrier basename **must** serialize the archived Atom's canonical ID with exactly one `@<version>` marker, where `<version>` is the unchanged numeric Version Number of that Archived Atom version. The marker **must** occur in the filename's Atom-ID segment under CA-D-283; do **not** append a second `@<version>` to a basename that already carries the marker. Existing legacy archive basenames are not normalized automatically.
