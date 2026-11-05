---
atom_id: CA-R-2499
ref_id: CA-R-2499
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Content.Summary
tier: 3
status: Active
version: 5
updated_at: 2026-11-04 05:21:15 +0400
carrier_destination:
  file:
    name: CA-R-2499-CORE_META_MODEL-DECLARATION--declare-atom-content-summary.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
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
  (.ID),
  (.Content.Summary),
  (Atom.Header.Status >| Status Group = Current) OR (Atom.Header.Status >| Status Group = Archived)
)
```

