---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  dependencies:
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//INSTALLED_EXTENSIONS
  - CAPRMEDIO_MODEL <+ Term//Artifact
version: 26
updated_at: 2026-11-02 00:18:22 +0400
atom_id: CA-R-1220
ref_id: CA-R-1220
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-1220-CORE_META_MODEL-RULE--require-immutable-installed-extension-candidate-provenance.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Require Immutable Installed Extension Candidate Provenance

## Claim

### Prose Claim


Installed Extensions Catalog Entries and immutable Extension Candidates.


**every** Installed Extensions Catalog Entry **must** identify **`=1`** immutable Extension Candidate by stable Identity, Version, Author, Source, Source Version, Origin, **and** Content Digest.
