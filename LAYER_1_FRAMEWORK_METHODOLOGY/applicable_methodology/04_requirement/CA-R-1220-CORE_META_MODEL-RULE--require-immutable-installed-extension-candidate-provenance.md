---
atom_id: CA-R-1220
ref_id: CA-R-1220
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  dependencies:
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//INSTALLED_EXTENSIONS
  - CAPRMEDIO_MODEL <+ Term//Artifact
tier: 3
status: Active
version: 26
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1220-CORE_META_MODEL-RULE--require-immutable-installed-extension-candidate-provenance.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1220-CORE_META_MODEL-RULE--require-immutable-installed-extension-candidate-provenance.md
  source_atom_id: CA-R-1220
  source_atom_revision: 26
  source_sha256: 7cbf5f524c07621b5bd9c5215c77ddab1ed9b0e0bef0bfed62db94dea5a684c8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Require Immutable Installed Extension Candidate Provenance

## Claim

### Prose Claim


Installed Extensions Catalog Entries and immutable Extension Candidates.


**every** Installed Extensions Catalog Entry **must** identify **`=1`** immutable Extension Candidate by stable Identity, Version, Author, Source, Source Version, Origin, **and** Content Digest.
