---
atom_id: CA-R-2521
ref_id: CA-R-2521@3
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Action.Execution
    Kind
tier: 3
status: archived
version: 3
updated_at: 2026-11-11 16:04:42 +0400
carrier_destination:
  file:
    name: CA-R-2521@3-CORE_META_MODEL-DECLARATION--declare-action-execution-kind.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom/(.Role := Operations)/Action.Execution Kind

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in (Operations))/Action.Execution Kind{::1}:: [string]{::1};

Atom/(.Header.Context.Role in (Operations))/Action.Execution Kind.*[]{::0};

Atom/(.Header.Context.Role in (Operations))/Action.Execution Kind :: Programmatic;

Atom/(.Header.Context.Role in (Operations))/Action.Execution Kind :: Agentic
```

