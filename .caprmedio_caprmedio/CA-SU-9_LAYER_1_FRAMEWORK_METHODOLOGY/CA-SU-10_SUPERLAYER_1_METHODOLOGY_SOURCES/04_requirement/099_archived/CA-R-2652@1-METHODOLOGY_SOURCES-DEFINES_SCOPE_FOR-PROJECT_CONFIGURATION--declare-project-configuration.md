---
atom_id: CA-R-2652
ref_id: CA-R-2652@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2652@1-METHODOLOGY_SOURCES-DEFINES_SCOPE_FOR-PROJECT_CONFIGURATION--declare-project-configuration.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/04_requirement/099_archived
---
## Summary

Declare PROJECT_CONFIGURATION

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//PROJECT_CONFIGURATION.ID == "CA-SU-13";

Scope Unit//PROJECT_CONFIGURATION.Name == "PROJECT_CONFIGURATION";

Scope Unit//PROJECT_CONFIGURATION.Label == "LAYER";

Scope Unit//PROJECT_CONFIGURATION.order.ordered == true;

Scope Unit//PROJECT_CONFIGURATION.order.number == 3;

Scope Unit//PROJECT_CONFIGURATION ((IS_CONTAINED_BY)) Scope Unit//METHODOLOGY_SOURCES
```

