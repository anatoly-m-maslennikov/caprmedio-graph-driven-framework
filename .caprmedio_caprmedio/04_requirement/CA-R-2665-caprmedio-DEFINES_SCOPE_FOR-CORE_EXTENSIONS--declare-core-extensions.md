---
atom_id: CA-R-2665
role: Requirement
form: Scope Unit Declaration
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//CORE_EXTENSIONS
relations: {}
---
## Summary

Declare CORE_EXTENSIONS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//CORE_EXTENSIONS.ID == "CA-SU-26";

Scope Unit//CORE_EXTENSIONS.Name == "CORE_EXTENSIONS";

Scope Unit//CORE_EXTENSIONS.Label == "LAYER";

Scope Unit//CORE_EXTENSIONS.order.ordered == true;

Scope Unit//CORE_EXTENSIONS.order.number == 4;

Scope Unit//CORE_EXTENSIONS ((IS_CONTAINED_BY)) Project//caprmedio
```

