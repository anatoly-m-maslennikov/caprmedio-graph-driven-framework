---
atom_id: CA-R-2661
ref_id: CA-R-2661
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//AGENTIC
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
---
## Summary

Declare AGENTIC

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//AGENTIC.ID == "CA-SU-22";

Scope Unit//AGENTIC.Name == "AGENTIC";

Scope Unit//AGENTIC.Label == "FEATURE";

Scope Unit//AGENTIC.order.ordered == false;

Scope Unit//AGENTIC ((IS_CONTAINED_BY)) Scope Unit//FRAMEWORK_ENGINE
```

