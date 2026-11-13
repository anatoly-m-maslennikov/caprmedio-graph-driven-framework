---
identity:
  id: CA-R-3055
  ref_id: CA-R-3055
context:
  container:
    scope_unit: CA-SU-11
  role: Requirement
  form: Relation Declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_WORK_REPORT_FOR
  tier: 3
state:
  status: active
  version: 3
  updated_at: '2026-11-12T12:33:04.158402+00:00'
destination:
  file:
    name: CA-R-3055-CORE_META_MODEL-RELATION_DECLARATION--declare-is-work-report-for.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare IS_WORK_REPORT_FOR

## Claim

### Prose Claim

The Host is a Plan / Work Report. The Target is the reported work Plan with Form Plan.

### Formal Claim

```python
from caprmedio.formal_claims import declare_relation

declare_relation(
    relation_name='IS_WORK_REPORT_FOR',
    source_endpoint={'level': 'instances',
 'entity_paths': ('Atom/(.Header.Context.Role := Plan)/(.Header.Context.Form := Work '
                  'Report)',)},
    target_endpoint={'level': 'instances',
 'entity_paths': ('Atom/(.Header.Context.Role := Plan)/(.Header.Context.Form := '
                  'Plan)',)},
)
```

## Semantics

IS_WORK_REPORT_FOR relates a Work Report to its Task.
