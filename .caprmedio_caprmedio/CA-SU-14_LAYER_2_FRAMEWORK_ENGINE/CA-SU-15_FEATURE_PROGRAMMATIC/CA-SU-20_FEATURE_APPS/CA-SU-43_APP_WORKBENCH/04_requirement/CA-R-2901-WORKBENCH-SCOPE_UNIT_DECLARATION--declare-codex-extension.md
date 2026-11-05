---
atom_id: CA-R-2901
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
version: 2
author: Anatoly Maslennikov
role: Requirement
form: Scope Unit Declaration
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//CODEX_EXTENSION
relations: {}
carrier_destination:
  file:
    name: CA-R-2901-WORKBENCH-SCOPE_UNIT_DECLARATION--declare-codex-extension.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
updated_at: 2026-11-05 17:14:39 +0400
---

## Summary

Declare CODEX_EXTENSION

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//CODEX_EXTENSION.ID == "CA-SU-48";
Scope Unit//CODEX_EXTENSION.Name == "CODEX_EXTENSION";
Scope Unit//CODEX_EXTENSION.Label == "FEATURE";
Scope Unit//CODEX_EXTENSION.order.ordered == false;
Scope Unit//CODEX_EXTENSION ((IS_CONTAINED_BY)) Scope Unit//WORKBENCH
```
