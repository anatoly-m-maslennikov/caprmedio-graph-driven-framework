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
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//CODEX_EXTENSION
  tier: 3
state:
  status: Active
  version: 7
  updated_at: 2026-11-11 15:29:41 +0400
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

The receiving Scope Unit is CODEX_EXTENSION. Existing default Role and Form admissions remain applicable. The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared entities or instances at these addresses:

- `MODEL//CAPRMEDIO <+ View`;
- `MODEL//CAPRMEDIO <+ Workspace`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts`;

Each address selects one endpoint object, not the address string, other members of its type or descendants. An unresolved address is diagnostic and grants no admission. These permissions apply only to local Atoms whose Header.Container resolves to CODEX_EXTENSION. The Scope Unit identity, Parent, responsibility and structural tree are unchanged.

### Formal Claim

```CFEL
# instances
Scope Unit//CODEX_EXTENSION.ID == "CA-SU-48";
Scope Unit//CODEX_EXTENSION.Name == "CODEX_EXTENSION";
Scope Unit//CODEX_EXTENSION.Label == "FEATURE";
Scope Unit//CODEX_EXTENSION.order.ordered == false;
Scope Unit//CODEX_EXTENSION ((IS_CONTAINED_BY)) Scope Unit//WORKBENCH;

Atom/(.Header.Context.Container.scope_unit in ("CA-SU-48"))/(.Header.Context.Role in (Delivery)).Header.Context.Form :: Solution;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-48"))/(.Header.Context.Role in (Method)).Header.Context.Form :: Solution;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-48"))/(.Header.Context.Role in (Requirement)).Header.Context.Form :: Rule;
```
