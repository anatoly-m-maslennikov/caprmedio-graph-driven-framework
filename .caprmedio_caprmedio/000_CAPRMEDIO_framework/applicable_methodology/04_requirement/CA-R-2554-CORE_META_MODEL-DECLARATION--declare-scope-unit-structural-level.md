---
atom_id: CA-R-2554
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Scope Unit.structural_level
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2554-CORE_META_MODEL-DECLARATION--declare-scope-unit-structural-level.md
  source_atom_id: CA-R-2554
  source_atom_revision: 2
  source_sha256: b213bbc740dfdb5c34b54bb544baee9a945d16509b5303017272d3349ff95ad7
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Scope Unit.structural_level

## Claim

```CFEL
Scope Unit.structural_level{:1}: [int]{:1};
Scope Unit.structural_level.*[]{:0};
Scope Unit.structural_level >= 0;
Scope Unit/Project//$project.structural_level = 0;
IF (Scope Unit//$contained ((IS_CONTAINED_BY)) Scope Unit//$container)
THEN ($contained.structural_level = $container.structural_level + 1)
```
