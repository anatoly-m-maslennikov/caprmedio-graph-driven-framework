---
atom_id: CA-R-2697
ref_id: CA-R-2697
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.State.Updated At
tier: 3
status: Active
version: 1
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-2697-CORE_META_MODEL-DECLARATION--declare-atom-header-updated-at.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom.Header.Updated At

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.State.Updated At{::1}:: [datetime]{::1};

Atom.Header.State.Updated At.*[]{::0};

# instances
Atom//$atom.Header.State.Updated At == MAX(Event Record//$event_record(.object_output{=1}, .object_output.version{=1}, .object_output.id = $atom.Header.Identity.ID, .object_output.version = $atom.Header.State.Version, (.action = create OR .action = update)).happened_at)
```
