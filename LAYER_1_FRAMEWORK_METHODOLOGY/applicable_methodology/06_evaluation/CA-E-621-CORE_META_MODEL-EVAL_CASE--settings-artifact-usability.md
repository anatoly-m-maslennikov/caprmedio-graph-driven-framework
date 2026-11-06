---
atom_id: CA-E-621
ref_id: CA-E-621
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings
  dependencies:
  - CAPRMEDIO_MODEL <+ Project.Settings
  - Entity/Object/Continuant/Actor/Operator
tier: 3
status: Active
version: 37
updated_at: 2026-11-02 20:07:03 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-621-CORE_META_MODEL-EVAL_CASE--settings-artifact-usability.md
  source_atom_id: CA-E-621
  source_atom_revision: 37
  source_sha256: 51bcd2e2bf8fd91b29295d1e17d6414ad3d9d6775764f3f21fb2d98850ad649a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Settings Artifact Usability

## Claim scope

The Operator has no undocumented Framework knowledge and must not edit the Framework Catalog.

## Claim

An Operator unfamiliar with the repository can configure Framework behavior, including default and Project Authority Modes, through Framework Instance Settings and Project initialization inputs through Project Settings using the owning Settings Artifacts and their in-file documentation. Scope Unit Declarations are the separate owner of Scope Unit structure. No structural Projection is required to make these choices.

## Details

### Acceptance criteria

Every intended change is made through its owning Settings Artifact or Scope Unit Declaration, and at least 90% of classifications distinguish Project choices from methodology definitions.

### Failure disposition

Record a Concern for every misleading or missing Settings instruction and stop settings-usability readiness until it is corrected.
