---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Governance Origin
  passive:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Term//Artifact
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
version: 39
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
atom_id: CA-R-1645
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1645-PROJECT_CONFIGURATION-RULE--define-self-hosted-governance-origins.md
  source_atom_id: CA-R-1645
  source_atom_revision: 39
  source_sha256: bc03be5ab06b03fb47c5c315b4ca0c248ccf7df9e4a9244e95220b80dccf7f37
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define self-hosted Governance origins

## Claim

### Prose Claim


Governance Origin for the self-hosted caprmedio Project and its distributed CAPRMEDIO sources.


Governance Origin for the self-hosted caprmedio Project **and** its distributed CAPRMEDIO sources follows the ownership distinction **in** CA-R-1709@38-CORE_META_MODEL-DEFINITION--define-two-governance-origins:

- within the caprmedio Project, its Project-owned Methodology authority, framework authority, **and** other Project-owned Artifacts have internal Governance Origin.
- a distributed CAPRMEDIO framework source has external Governance Origin relative **to** a consuming Project. that Project's own adaptation authority has internal Governance Origin; creating it does **not** transfer ownership of the external source **or** change that source's origin.
- graph Relations, version-control authorship, filesystem ownership, **and** byte identity do **not** replace the governing ownership distinction.
