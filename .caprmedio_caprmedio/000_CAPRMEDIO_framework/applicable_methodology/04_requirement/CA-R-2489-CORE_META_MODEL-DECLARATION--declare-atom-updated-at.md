---
atom_id: CA-R-2489
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom.Updated At
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2489-CORE_META_MODEL-DECLARATION--declare-atom-updated-at.md
  source_atom_id: CA-R-2489
  source_atom_revision: 2
  source_sha256: 21a3f0aecf5fdc0446ad0a2e45b9588ec115575b8f0849457ea9f2078f01975c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Updated At

## Claim

```CFEL
Atom.Updated At{:1}: [datetime]{:1};
Atom.Updated At.*[]{:0};
Atom//$atom.Updated At == MAX(Event Record//(.object_output{=1}, .object_output.version{=1}, .object_output.id = $atom.ID, .object_output.version = $atom.Version, (.action = create OR .action = update)).happened_at)
```
