---
atom_id: CA-R-2697
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Updated At
version: 1
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2697-CORE_META_MODEL-DECLARATION--declare-atom-header-updated-at.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Atom.Header.Updated At

## Claim

### Formal Claim

```CFEL
Atom.Header.Updated At{:1}: [datetime]{:1};
Atom.Header.Updated At.*[]{:0};
Atom//$atom.Header.Updated At == MAX(Event Record//(.object_output{=1}, .object_output.version{=1}, .object_output.id = $atom.Header.ID, .object_output.version = $atom.Header.Version, (.action = create OR .action = update)).happened_at)
```
