---
identity:
  atom_id: CA-R-970308651
  ref_id: CA-R-970308651@2
context:
  role: requirement
  form: declaration
  tier: 3
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Concern)/(.Header.Context.Form
      := Implementation Discrepancy)
  container:
    scope_unit: CA-SU-11
state:
  version: 2
  status: archived
  updated_at: '2026-11-12T17:23:54+00:00'
destination:
  file:
    name: CA-R-970308651@2-CORE_META_MODEL-DECLARATION--declare-implementation-discrepancy-as-a-concern-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---
## Summary

Declare Implementation Discrepancy as a Concern Form

## Claim

### Prose Claim

Identify the applicable RMEDO Atom and the code location. State what the Atom specifies and what the code does.

Resolved means the code and applicable specification agree. Canceled means the recorded comparison is obsolete because the code or specification changed scope or was retired.

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Concern

class ImplementationDiscrepancy(Concern):
    pass

declare_entity(entity_class=ImplementationDiscrepancy, entity_name='Implementation Discrepancy', qualification_property_path="Atom.Header.Context.Form")
```

## Semantics

An Implementation Discrepancy records a mismatch between the code and an applicable RMEDO Atom.
