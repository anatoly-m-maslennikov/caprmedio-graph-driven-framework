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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-970308626-CORE_META_MODEL-RELATION_DECLARATION--declare-is-work-report-for.md
  source_atom_id: CA-R-970308626
  source_atom_revision: 2
  source_sha256: 9e65c03f0ba11a3f5e4ea83d2d375f449083e616875881572841a6bdd5692360
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
$report[<Atom>, (.Header.Role = Plan) AND (.Header.Form = Work Report)] ((IS_WORK_REPORT_FOR)) $task[<Atom>, (.Header.Role = Plan) AND (.Header.Form = Plan)]
```

## Semantics

IS_WORK_REPORT_FOR relates a Work Report to its Task.
