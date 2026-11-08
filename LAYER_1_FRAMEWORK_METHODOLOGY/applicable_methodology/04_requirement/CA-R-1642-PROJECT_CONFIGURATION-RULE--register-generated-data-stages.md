---
atom_id: CA-R-1642
ref_id: CA-R-1642
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier
tier: 3
relations:
  depends_on:
  - CA-R-1717
status: Active
version: 33
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1642-PROJECT_CONFIGURATION-RULE--register-generated-data-stages.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1642-PROJECT_CONFIGURATION-RULE--register-generated-data-stages.md
  source_atom_id: CA-R-1642
  source_atom_revision: 33
  source_sha256: 4956272b541e8c1fee73e8baad7880752b06d0fb6dcee60753fd0d97518101e4
  original_relations_sha256: f326d4ddaa9bdeea1aa820492e47e3b4c4bd09a8286a8f577571a43d47043668
---
## Summary

Register generated-data stages

## Claim

### Prose Claim


the ordered generated-data pipeline stages.


the following ordered generated-data pipeline stages **must** be registered, referenced by their Carrier prefixes governed by CA-D-388-PROJECT_CONFIGURATION-ENG_DECISION--serialize-generated-data-stage-prefixes-and-formats:

| Stage reference | Stage meaning |
| --- | --- |
| `src` | canonical Journal input; authority comes from the Journal, **not** the prefix. |
| `stg` | deterministic, lossless Projection of a bounded `src` frontier. |
| `mrt` | consumer-ready semantic Projection, including Requirement groupings by scope **and** tier **or** Mermaid relation maps. |
| `biz` | aggregated CAPRMEDIO artifact **and** implementation metrics, including point-in-time snapshots **and** historical trends. |

dependencies **must** move forward through `src → stg → mrt → biz`; a stage **may** depend on **any** earlier registered stage but **must not** depend on a later stage.
