---
atom_id: CA-R-2669
ref_id: CA-R-2669@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//ADAPTERS
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2669@1-TOOLS-DEFINES_SCOPE_FOR-ADAPTERS--declare-adapters.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/04_requirement/099_archived
---
## Summary

Declare ADAPTERS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//ADAPTERS.ID == "CA-SU-30";

Scope Unit//ADAPTERS.Name == "ADAPTERS";

Scope Unit//ADAPTERS.Label == "FEATURE_GROUP";

Scope Unit//ADAPTERS.order.ordered == false;

Scope Unit//ADAPTERS ((IS_CONTAINED_BY)) Scope Unit//TOOLS
```

