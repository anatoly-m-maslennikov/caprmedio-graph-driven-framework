---
identity:
  id: CA-R-3077
  ref_id: CA-R-3077@1-draft
context:
  container:
    scope_unit: CA-SU-10
  role: requirement
  form: scope_delegation
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//INSTALLED_EXTENSIONS
    dependencies:
    - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling
      <+ Source Selection
  tier: 3
state:
  status: draft
  version: 1
  updated_at: '2026-11-11T16:40:25+04:00'
destination:
  file:
    name: CA-R-3077@1-draft-METHODOLOGY_SOURCES-SCOPE_DELEGATION--delegate-responsibility-to-installed-extensions.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/04_requirement/000_draft
---

## Summary

Delegate responsibility to INSTALLED_EXTENSIONS

## Claim

### Prose Claim

- INSTALLED_EXTENSIONS must preserve exact installed Extension source revisions and their provenance as immutable candidate inputs to methodology compilation without activating or modifying them. [CA-R-1175](../CA-R-1175-METHODOLOGY_SOURCES-GOAL-INSTALLED_EXTENSIONS--preserve-installed-extension-revisions-as-candidate-inputs.md)

### Formal Claim

```CFEL
# instances
Atom//"CA-R-3077" ((HAS_ACTIVE_SUBJECT)) Scope Unit//INSTALLED_EXTENSIONS;
```
