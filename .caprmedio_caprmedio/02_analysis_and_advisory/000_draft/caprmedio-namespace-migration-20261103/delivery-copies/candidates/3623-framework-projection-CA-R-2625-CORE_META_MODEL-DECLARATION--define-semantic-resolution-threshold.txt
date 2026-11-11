---
atom_id: CA-R-2625
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Project.Settings.Confidence.Semantic Resolution Threshold
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2625-CORE_META_MODEL-DECLARATION--define-semantic-resolution-threshold.md
  source_atom_id: CA-R-2625
  source_atom_revision: 1
  source_sha256: 53792d380d3397af8b39dabd2d526325705a124c14fa0056ae87f0f2a3c7f7a1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Define Semantic Resolution Threshold

## Claim

An absent override uses the governed default.

```CFEL
Project.Settings.Confidence.Semantic Resolution Threshold{:0..1}: [int]{:1};
Project.Settings.Confidence.Semantic Resolution Threshold.*[]{:0}
```
