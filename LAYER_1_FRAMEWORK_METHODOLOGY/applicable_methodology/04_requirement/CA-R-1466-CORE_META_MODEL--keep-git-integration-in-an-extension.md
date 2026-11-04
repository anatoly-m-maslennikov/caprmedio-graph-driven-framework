---
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Architecture <+ Component Structure
  passive:
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//CORE_META_MODEL
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
version: 23
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
atom_id: CA-R-1466
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1466-CORE_META_MODEL--keep-git-integration-in-an-extension.md
  source_atom_id: CA-R-1466
  source_atom_revision: 23
  source_sha256: 8ea6435ccf86e81aae52d60c231d5692568624b95ce59dffb27caeaa05a34aa0
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Keep Git integration in an Extension

## Claim

### Prose Claim


Git integration in the Core Meta-Model.


Git integration **must** be optional Extension authority, **not** a prerequisite of the Core Meta-Model. Git commit policies, commit-message encodings, hooks, **and** event-to-commit references belong **to** that Extension; selecting it **must not** replace the authoritative Journal **or** make Git history an independent source for the same recorded facts. the Core Meta-Model **must** remain applicable **without** Git integration.
