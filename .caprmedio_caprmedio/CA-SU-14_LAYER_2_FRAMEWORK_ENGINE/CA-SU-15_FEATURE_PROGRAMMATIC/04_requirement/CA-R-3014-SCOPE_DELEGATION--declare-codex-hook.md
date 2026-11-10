---
identity:
  atom_id: CA-R-3014
  ref_id: CA-R-3014
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//CODEX_HOOK
  tier: 3
state:
  status: Active
  version: 1
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-3014-SCOPE_DELEGATION--declare-codex-hook.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
author: Anatoly Maslennikov
---

## Summary

Declare CODEX_HOOK

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//CODEX_HOOK.ID == "CA-SU-49";
Scope Unit//CODEX_HOOK.Name == "CODEX_HOOK";
Scope Unit//CODEX_HOOK.Label == "FEATURE";
Scope Unit//CODEX_HOOK.order.ordered == false;
Scope Unit//CODEX_HOOK ((IS_CONTAINED_BY)) Scope Unit//PROGRAMMATIC
```

### Prose Claim

CODEX_HOOK owns the generic Codex command hook, its host installation and the context passed to CAPRMEDIO MCP. The hook works without a plugin. Workbench UI integration remains separate.

Admit local Requirement/Requirement, Method/Decision, Evaluation/Eval Case and Delivery/Decision pairs for the host-adapter contract. Their exact HAS_ACTIVE_SUBJECT target is `MODEL//CAPRMEDIO <+ Atom`. It selects that declared object, not its descendants or other type members. Their precise Content Scope is this hook's CAPRMEDIO request binding. An unresolved target grants no admission. Existing default admissions remain unchanged.
