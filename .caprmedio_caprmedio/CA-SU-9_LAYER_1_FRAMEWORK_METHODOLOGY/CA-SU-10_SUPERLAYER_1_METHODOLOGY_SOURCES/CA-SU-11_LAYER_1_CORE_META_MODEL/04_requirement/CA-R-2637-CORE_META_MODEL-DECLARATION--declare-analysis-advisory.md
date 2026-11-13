---
atom_id: CA-R-2637
ref_id: CA-R-2637
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := "Analysis and Advisory")
tier: 3
status: active
version: 5
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-2637-CORE_META_MODEL-DECLARATION--declare-analysis-advisory.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Analysis & Advisory

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Atom

class AnalysisAndAdvisory(Atom):
    pass

declare_entity(entity_class=AnalysisAndAdvisory, entity_name='Analysis and Advisory', qualification_property_path="Atom.Header.Context.Role", classifications={"Role Order Number": 2})
```

## Semantics

Analysis and Advisory covers analysis reports, rationales and spec proposals. It establishes findings, explanations, comparisons, reasons or proposed changes.

For reading historical Atom carriers, `Analysis & Advisory` is an alias for this same Role. New and updated Atom carriers use the canonical Role value `Analysis and Advisory`.
