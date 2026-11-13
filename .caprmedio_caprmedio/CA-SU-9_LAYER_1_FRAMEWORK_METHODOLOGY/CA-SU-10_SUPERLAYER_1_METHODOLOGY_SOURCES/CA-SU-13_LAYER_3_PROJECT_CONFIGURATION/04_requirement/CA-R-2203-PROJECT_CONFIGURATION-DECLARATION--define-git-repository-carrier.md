---
atom_id: CA-R-2203
ref_id: CA-R-2203
container:
  scope_unit: CA-SU-13
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/Git Repository
tier: 1
status: active
version: 9
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-2203-PROJECT_CONFIGURATION-DECLARATION--define-git-repository-carrier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
---
## Summary

Define Git Repository Carrier

## Claim

### Prose Claim

A Git Repository is a Carrier of versioned content and Git references.

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Carrier

class GitRepository(Carrier):
    pass

declare_entity(entity_class=GitRepository, entity_name='Git Repository')
```

## Semantics

Git Repository contains Git Branches; this is containment, not specialization.
