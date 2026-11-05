---
atom_id: CA-R-2790
role: Requirement
form: Scope Unit Declaration
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH_CODEX
status: Archived
version: 1
author: Anatoly Maslennikov
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKBENCH_CODEX
relations: {}
updated_at: 2026-11-05 14:23:38 +0400
carrier_destination:
  file:
    name: CA-R-2790@1-WORKBENCH-DEFINES_SCOPE_FOR-WORKBENCH_CODEX--declare-workbench-codex.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
---

## Summary

Declare WORKBENCH_CODEX

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//WORKBENCH_CODEX.ID == "CA-SU-47";
Scope Unit//WORKBENCH_CODEX.Name == "WORKBENCH_CODEX";
Scope Unit//WORKBENCH_CODEX.Label == "FEATURE";
Scope Unit//WORKBENCH_CODEX.order.ordered == false;
Scope Unit//WORKBENCH_CODEX ((IS_CONTAINED_BY)) Scope Unit//WORKBENCH
```

### Prose Claim

Own Codex integration in Workbench: one chat per Project, its conversation interface, Project context, sessions and turns, streamed output, calls to all Tools exposed by the enabled configured MCP servers, and approval interaction. CAPRMEDIO calls carry the selected Project root; other servers retain their own inputs. Shared Workbench contracts remain in WORKBENCH.
