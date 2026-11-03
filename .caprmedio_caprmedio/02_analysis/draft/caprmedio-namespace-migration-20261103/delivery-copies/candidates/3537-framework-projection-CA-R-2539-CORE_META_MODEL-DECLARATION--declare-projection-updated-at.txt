---
atom_id: CA-R-2539
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Projection.Updated At
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2539-CORE_META_MODEL-DECLARATION--declare-projection-updated-at.md
  source_atom_id: CA-R-2539
  source_atom_revision: 2
  source_sha256: ba93b15cbc71766ead790f8e96dc9663270f97b03a367ec157e13050364e5e5b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Projection.Updated At

## Claim

```CFEL
Projection.Updated At{:1}: [datetime]{:1};
Projection.Updated At.*[]{:0};
Projection//$projection.Updated At == MAX(Event Record//(.object_output{=1}, .object_output.version{=0}, .object_output.id = $projection.ID, (.action = create OR .action = update)).happened_at)
```
