---
identity:
  id: CA-R-970308626
  ref_id: CA-R-970308626
context:
  container:
    scope_unit: CA-SU-11
  role: Requirement
  form: Relation Declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_WORK_REPORT_FOR
  tier: 3
state:
  status: Active
  version: 2
  updated_at: 2026-11-08 19:06:46 +0400
destination:
  file:
    name: CA-R-970308626-CORE_META_MODEL-RELATION_DECLARATION--declare-is-work-report-for.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare IS_WORK_REPORT_FOR

## Claim

### Prose Claim

The Host is a Plan / Work Report. The Target is the reported work Plan with Form Plan.

### Formal Claim

```CFEL
# model
Relation//IS_WORK_REPORT_FOR ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
$report[<Atom>, (.Header.Context.Role = Plan) AND (.Header.Context.Form = Work Report)] ((IS_WORK_REPORT_FOR)) $task[<Atom>, (.Header.Context.Role = Plan) AND (.Header.Context.Form = Plan)]
```

## Semantics

IS_WORK_REPORT_FOR relates a Work Report to its Task.
