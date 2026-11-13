---
atom_id: CA-R-2499
ref_id: CA-R-2499@6
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Content.Summary
tier: 3
status: archived
version: 6
updated_at: '2026-11-11T18:31:44+04:00'
carrier_destination:
  file:
    name: CA-R-2499@6-CORE_META_MODEL-DECLARATION--declare-atom-content-summary.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom.Content.Summary

## Claim

### Formal Claim

```CFEL
# model
Atom.Content.Summary{::1}:: {::1};

Atom.Content.Summary.*[]{::0};

# instances
DETERMINES(
  Atom//$atom,
  (.Header.Identity.ID),
  (.Content.Summary),
  (Atom.Header.State.Status >| Status Group = Current) OR (Atom.Header.State.Status >| Status Group = Backlog) OR (Atom.Header.State.Status >| Status Group = Archived)
)
```

