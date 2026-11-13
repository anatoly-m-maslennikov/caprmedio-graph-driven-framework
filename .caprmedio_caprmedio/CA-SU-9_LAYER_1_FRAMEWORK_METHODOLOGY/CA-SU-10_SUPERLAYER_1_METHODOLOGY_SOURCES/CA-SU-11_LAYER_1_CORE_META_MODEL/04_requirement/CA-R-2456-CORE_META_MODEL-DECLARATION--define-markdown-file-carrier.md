---
atom_id: CA-R-2456
ref_id: CA-R-2456
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/File/Markdown
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier/File
tier: 1
status: active
version: 6
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-2456-CORE_META_MODEL-DECLARATION--define-markdown-file-carrier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Markdown File Carrier

## Claim

### Prose Claim

A Markdown File Carrier is a File Carrier represented using Markdown.
### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import File

class Markdown(File):
    pass

declare_entity(entity_class=Markdown, entity_name='Markdown')
```

