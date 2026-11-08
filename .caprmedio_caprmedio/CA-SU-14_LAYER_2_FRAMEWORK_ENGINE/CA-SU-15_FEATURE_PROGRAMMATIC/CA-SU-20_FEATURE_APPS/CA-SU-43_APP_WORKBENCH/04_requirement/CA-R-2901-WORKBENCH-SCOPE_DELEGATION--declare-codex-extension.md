---
identity:
  atom_id: CA-R-2901
  ref_id: CA-R-2901
context:
  container:
    scope_unit: CA-SU-43
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//CODEX_EXTENSION
  tier: 3
state:
  status: Active
  version: 3
  updated_at: 2026-11-08 22:18:08 +0400
destination:
  file:
    name: CA-R-2901-WORKBENCH-SCOPE_DELEGATION--declare-codex-extension.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Declare CODEX_EXTENSION

## Claim

### Prose Claim

The receiving Scope Unit is CODEX_EXTENSION. These permissions apply only to local Atoms whose Header.Container-derived `IS_CONTAINED_BY` target is CODEX_EXTENSION. Its default local admissions remain applicable. Its explicit local Role/Form pairs are Requirement / Entity Definition, Requirement / Rule, Method / Solution, Evaluation / Eval Case, and Delivery / Decision. Each selection is limited to declared model entities or declared instances resolved at [`CAPRMEDIO_MODEL <+ Workspace`, `CAPRMEDIO_MODEL <+ View`]. These selections identify endpoint objects, not strings, all members of a type, or descendants. An unresolved address is diagnostic and grants no admission.

### Formal Claim

```CFEL
# instances
Scope Unit//CODEX_EXTENSION.ID == "CA-SU-48";
Scope Unit//CODEX_EXTENSION.Name == "CODEX_EXTENSION";
Scope Unit//CODEX_EXTENSION.Label == "FEATURE";
Scope Unit//CODEX_EXTENSION.order.ordered == false;
Scope Unit//CODEX_EXTENSION ((IS_CONTAINED_BY)) Scope Unit//WORKBENCH
```
