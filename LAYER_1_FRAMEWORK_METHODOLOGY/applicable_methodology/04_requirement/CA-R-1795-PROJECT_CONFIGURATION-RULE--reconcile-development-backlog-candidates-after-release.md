---
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering
version: 15
updated_at: 2026-11-02 19:44:26 +0400
relations:
  depends_on:
  - CA-O-058
  - CA-R-1702
atom_id: CA-R-1795
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 4
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1795-PROJECT_CONFIGURATION-RULE--reconcile-development-backlog-candidates-after-release.md
  source_atom_id: CA-R-1795
  source_atom_revision: 15
  source_sha256: fe8a849ec38c7da928011fb3d4220c0c023fbbf4025d9a7655e4ebb8aa1bff1d
  original_relations_sha256: 6da6e9e2e72a9ce628eefef9aaece62f50d1f274270b6bdf901b54734f13f8ee
---
## Summary
Reconcile Development Backlog candidates **after** release

## Claim

### Prose Claim

Development Backlog candidates **after** a Release Record is accepted.


CAPRMEDIO **must** reconcile the Development Backlog against its exact released manifest as follows:

- remove a candidate whose promoted Atoms were fully delivered **in** that release.
- **every** candidate that is unfinished, partially delivered, excluded, **or** newly deferred **must** remain unscheduled **or** move **to** another target version.
- a candidate **must not** be removed as shipped **unless** the released manifest accounts for its promoted Atoms.
