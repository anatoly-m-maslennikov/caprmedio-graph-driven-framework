---
atom_id: CA-R-2663
ref_id: CA-R-2663
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//PROMPTS
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
---
## Summary

Declare PROMPTS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//PROMPTS.ID == "CA-SU-24";

Scope Unit//PROMPTS.Name == "PROMPTS";

Scope Unit//PROMPTS.Label == "FEATURE";

Scope Unit//PROMPTS.order.ordered == false;

Scope Unit//PROMPTS ((IS_CONTAINED_BY)) Scope Unit//AGENTIC
```

