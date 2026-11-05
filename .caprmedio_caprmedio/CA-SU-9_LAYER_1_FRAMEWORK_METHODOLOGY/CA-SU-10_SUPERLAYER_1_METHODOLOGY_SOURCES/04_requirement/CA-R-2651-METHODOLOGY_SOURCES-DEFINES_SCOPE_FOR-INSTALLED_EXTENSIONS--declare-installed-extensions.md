---
atom_id: CA-R-2651
ref_id: CA-R-2651
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//INSTALLED_EXTENSIONS
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:07:49 +0400
---
## Summary

Declare INSTALLED_EXTENSIONS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//INSTALLED_EXTENSIONS.ID == "CA-SU-12";

Scope Unit//INSTALLED_EXTENSIONS.Name == "INSTALLED_EXTENSIONS";

Scope Unit//INSTALLED_EXTENSIONS.Label == "LAYER";

Scope Unit//INSTALLED_EXTENSIONS.order.ordered == true;

Scope Unit//INSTALLED_EXTENSIONS.order.number == 2;

Scope Unit//INSTALLED_EXTENSIONS ((IS_CONTAINED_BY)) Scope Unit//METHODOLOGY_SOURCES
```

