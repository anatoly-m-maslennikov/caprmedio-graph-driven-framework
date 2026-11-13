---
identity:
  id: CA-R-3078
  ref_id: CA-R-3078@1-draft
context:
  container:
    scope_unit: CA-SU-9
  role: requirement
  form: scope_delegation
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//METHODOLOGY_SOURCES
    dependencies:
    - 'Entity/Aspect/Product: CAPRMEDIO Framework'
    - 'Entity/Object/Continuant/Projection/Type: Applicable Methodology'
  tier: 3
state:
  status: draft
  version: 1
  updated_at: '2026-11-11T16:40:25+04:00'
destination:
  file:
    name: CA-R-3078@1-draft-FRAMEWORK_METHODOLOGY-SCOPE_DELEGATION--delegate-responsibility-to-methodology-sources.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/000_draft
---

## Summary

Delegate responsibility to METHODOLOGY_SOURCES

## Claim

### Prose Claim

- METHODOLOGY_SOURCES must make the CAPRMEDIO governing model recursively self-applicable while preserving Operator authority. [CA-R-1172](../CA-R-1172-FRAMEWORK_METHODOLOGY-GOAL-METHODOLOGY_SOURCES--make-the-caprmedio-governing-model-recursively-self-applicable.md)
- METHODOLOGY_SOURCES must provide the authoritative source Layers from which Applicable Methodology is compiled. [CA-R-1173](../CA-R-1173-FRAMEWORK_METHODOLOGY-GOAL-METHODOLOGY_SOURCES--provide-authoritative-source-layers-for-applicable-methodology.md)

### Formal Claim

```CFEL
# instances
Atom//"CA-R-3078" ((HAS_ACTIVE_SUBJECT)) Scope Unit//METHODOLOGY_SOURCES;
```
