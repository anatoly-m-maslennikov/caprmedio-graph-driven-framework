---
atom_id: CA-R-2638
ref_id: CA-R-2638@4-draft
status: Draft
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//RUNS
version: 4
updated_at: 2026-11-05 02:06:39 +0400
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2638@4-draft-DECLARATION--define-runs.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
container:
  scope_unit: CA-SU-11
---
## Summary

Define RUNS

## Claim

### Formal Claim

```CFEL
# model
Relation//RUNS ((HAS_INVERSE)) Relation//IS_RUN_BY;

Relation//RUNS ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Step//$step ((RUNS)) (in (Action, Workflow))//$selected
```

### Prose Claim

RUNS binds a Step to its Action or Workflow target. Its inverse is IS_RUN_BY.
