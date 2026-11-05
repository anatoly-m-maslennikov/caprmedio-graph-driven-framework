---
atom_id: CA-R-2701
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.ID
version: 1
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2701-CORE_META_MODEL-DECLARATION--declare-atom-header-id.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Atom.Header.ID

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.ID{:1}: [string]{:1};

Atom.Header.ID.*[]{:0};

# instances
Atom//$atom;

IF (($atom.Header.Status >| Status Group = Current) OR ($atom.Header.Status >| Status Group = Archived))
THEN (IMMUTABLE($atom.Header.ID))
```
