---
atom_id: CA-R-2499
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content.Summary
version: 4
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2499-CORE_META_MODEL-DECLARATION--declare-atom-content-summary.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Atom.Content.Summary

## Claim

### Formal Claim

```CFEL
# model
Atom.Content.Summary{:1}: [markdown]{:1};

Atom.Content.Summary.*[]{:0};

# instances
DETERMINES(
  Atom//$atom,
  (.ID),
  (.Content.Summary),
  (Atom.Header.Status >| Status Group = Current) OR (Atom.Header.Status >| Status Group = Archived)
)
```

