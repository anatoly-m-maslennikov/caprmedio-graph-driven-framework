---
atom_id: CA-R-2669
ref_id: CA-R-2669
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//ADAPTERS
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
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

