---
atom_id: CA-R-2201
ref_id: CA-R-2201
container:
  scope_unit: CA-SU-13
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/Pull Request
tier: 1
status: active
version: 8
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-2201-PROJECT_CONFIGURATION-DECLARATION--define-pull-request-carrier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
---
## Summary

Define Pull Request Carrier

## Claim

### Prose Claim

A Pull Request is a repository-hosted Carrier of a proposed change and its review state.
### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Carrier

class PullRequest(Carrier):
    pass

declare_entity(entity_class=PullRequest, entity_name='Pull Request')
```

