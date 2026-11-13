---
identity:
  id: CA-R-3070
  ref_id: CA-R-3070@1
context:
  container:
    scope_unit: CA-SU-11
  role: requirement
  form: declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Context
  tier: 3
state:
  status: archived
  version: 1
  updated_at: 2026-11-11 16:27:40 +0400
destination:
  file:
    name: CA-R-3070@1-CORE_META_MODEL-DECLARATION--declare-atom-header-context.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---

## Summary

Declare Atom.Header.Context

## Claim

### Prose Claim

A Role-specific group uses the Role name. A Form-specific group is nested in its Role-specific group and uses the Form name.

### Formal Claim

```CFEL
# model
Atom.Header.Context{::1} :: []{::0};

Atom.Header.Context.*[in (Container, Role, Form, Label, Topics, Tier, Plan, Concern)]{::5..7};

Atom.Header.Context.Container ;> Atom.Header.Context.Role;

Atom.Header.Context.Role ;> Atom.Header.Context.Form;

Atom.Header.Context.Form ;> Atom.Header.Context.Label;

Atom.Header.Context.Label ;> Atom.Header.Context.Topics;

Atom.Header.Context.Topics ;> Atom.Header.Context.Tier
```
