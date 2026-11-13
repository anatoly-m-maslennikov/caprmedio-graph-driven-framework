---
identity:
  atom_id: CA-R-3145
  ref_id: CA-R-3145
context:
  role: requirement
  form: declaration
  tier: 3
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Concern)/(.Header.Context.Form
      := Code-Spec Mismatch)
  container:
    scope_unit: CA-SU-11
state:
  version: 2
  status: active
  updated_at: '2026-11-13T15:52:15.014000+00:00'
destination:
  file:
    name: CA-R-3145-CORE_META_MODEL-DECLARATION--declare-code-spec-mismatch-as-a-concern-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
relations:
  is_replacement_for:
  - CA-R-970308651
  - CA-R-3127
---
## Summary

Declare Code-Spec Mismatch as a Concern Form

## Claim

### Prose Claim

Identify the applicable RMEDO Atom and the code location. State what the Atom specifies and what the code does.

Resolved means the code and applicable specification agree. Canceled means the recorded comparison is obsolete because the code or specification changed scope or was retired.

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Concern

class CodeSpecMismatch(Concern):
    pass

declare_entity(entity_class=CodeSpecMismatch, entity_name='Code-Spec Mismatch', qualification_property_path="Atom.Header.Context.Form")
```

## Semantics

A Code-Spec Mismatch records a mismatch between the code and an applicable RMEDO Atom.
