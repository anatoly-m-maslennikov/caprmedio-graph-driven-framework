---
identity:
  id: CA-R-970308658
  ref_id: CA-R-970308658@1-draft
context:
  container:
    scope_unit: CA-SU-00
  role: requirement
  form: scope_delegation
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//CORE_EXTENSIONS
    dependencies:
    - CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
  tier: 3
state:
  status: draft
  version: 1
  updated_at: '2026-11-11T16:40:25+04:00'
destination:
  file:
    name: CA-R-970308658@1-draft-CAPRMEDIO-SCOPE_DELEGATION--delegate-responsibility-to-core-extensions.md
    path: .caprmedio_caprmedio/04_requirement/000_draft
---

## Summary

Delegate responsibility to CORE_EXTENSIONS

## Claim

### Prose Claim

- CORE_EXTENSIONS must provide CAPRMEDIO-maintained Extensions that add or specialize optional CAPRMEDIO capabilities without modifying canonical Core Meta-Model authority. [CA-R-1180](../CA-R-1180-CAPRMEDIO-SCOPE_CONTRACT-GOAL--provide-caprmedio-maintained-optional-extensions.md)

### Formal Claim

```CFEL
# instances
Atom//"CA-R-970308658" ((HAS_ACTIVE_SUBJECT)) Scope Unit//CORE_EXTENSIONS;
```
