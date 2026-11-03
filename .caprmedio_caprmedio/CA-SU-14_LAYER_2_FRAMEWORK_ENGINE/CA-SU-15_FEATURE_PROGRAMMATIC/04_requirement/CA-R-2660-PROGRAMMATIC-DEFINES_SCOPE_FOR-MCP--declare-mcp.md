---
atom_id: CA-R-2660
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//MCP
relations: {}
---
## Summary

Declare MCP

## Claim

### Formal Claim

```CFEL
Scope Unit//MCP.ID == "CA-SU-21";
Scope Unit//MCP.Name == "MCP";
Scope Unit//MCP.Label == "FEATURE";
Scope Unit//MCP.order.ordered == false;
Scope Unit//MCP ((IS_CONTAINED_BY)) Scope Unit//PROGRAMMATIC
```

