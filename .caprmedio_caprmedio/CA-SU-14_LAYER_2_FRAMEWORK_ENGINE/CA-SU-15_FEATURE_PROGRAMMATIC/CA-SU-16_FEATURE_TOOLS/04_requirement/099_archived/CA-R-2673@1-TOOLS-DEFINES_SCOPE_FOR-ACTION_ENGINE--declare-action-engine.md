---
atom_id: CA-R-2673
ref_id: CA-R-2673@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//ACTION_ENGINE
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2673@1-TOOLS-DEFINES_SCOPE_FOR-ACTION_ENGINE--declare-action-engine.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/04_requirement/099_archived
---
## Summary

Declare ACTION_ENGINE

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//ACTION_ENGINE.ID == "CA-SU-34";

Scope Unit//ACTION_ENGINE.Name == "ACTION_ENGINE";

Scope Unit//ACTION_ENGINE.Label == "FEATURE_GROUP";

Scope Unit//ACTION_ENGINE.order.ordered == false;

Scope Unit//ACTION_ENGINE ((IS_CONTAINED_BY)) Scope Unit//TOOLS
```

