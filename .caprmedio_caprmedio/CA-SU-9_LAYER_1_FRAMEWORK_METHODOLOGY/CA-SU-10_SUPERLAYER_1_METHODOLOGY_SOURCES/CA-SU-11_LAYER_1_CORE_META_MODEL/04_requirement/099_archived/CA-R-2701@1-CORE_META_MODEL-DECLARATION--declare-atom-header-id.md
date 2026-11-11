---
atom_id: CA-R-2701
ref_id: CA-R-2701@1
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Identity.ID
tier: 3
status: Archived
version: 1
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-2701@1-CORE_META_MODEL-DECLARATION--declare-atom-header-id.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom.Header.ID

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Identity.ID{::1}:: [string]{::1};

Atom.Header.Identity.ID.*[]{::0};

# instances
Atom//$atom;

IF (($atom.Header.State.Status >| Status Group = Current) OR ($atom.Header.State.Status >| Status Group = Archived))
THEN (IMMUTABLE($atom.Header.Identity.ID))
```
