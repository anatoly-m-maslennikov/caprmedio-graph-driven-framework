---
atom_id: CA-R-2667
ref_id: CA-R-2667@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//COMMUNITY_EXTENSIONS
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2667@1-caprmedio-DEFINES_SCOPE_FOR-COMMUNITY_EXTENSIONS--declare-community-extensions.md
    path: .caprmedio_caprmedio/04_requirement/099_archived
---
## Summary

Declare COMMUNITY_EXTENSIONS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//COMMUNITY_EXTENSIONS.ID == "CA-SU-28";

Scope Unit//COMMUNITY_EXTENSIONS.Name == "COMMUNITY_EXTENSIONS";

Scope Unit//COMMUNITY_EXTENSIONS.Label == "FEATURE";

Scope Unit//COMMUNITY_EXTENSIONS.order.ordered == false;

Scope Unit//COMMUNITY_EXTENSIONS ((IS_CONTAINED_BY)) Project//caprmedio
```

