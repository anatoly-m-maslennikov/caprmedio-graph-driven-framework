---
atom_id: CA-R-2651
ref_id: CA-R-2651@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//INSTALLED_EXTENSIONS
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2651@1-METHODOLOGY_SOURCES-DEFINES_SCOPE_FOR-INSTALLED_EXTENSIONS--declare-installed-extensions.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/04_requirement/099_archived
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

