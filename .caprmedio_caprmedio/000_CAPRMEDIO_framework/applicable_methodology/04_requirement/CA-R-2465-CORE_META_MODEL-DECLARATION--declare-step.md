---
atom_id: CA-R-2465
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom/(.Role := Operations)/Step
version: 4
updated_at: 2026-11-02 17:54:42 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2465-CORE_META_MODEL-DECLARATION--declare-step.md
  source_atom_id: CA-R-2465
  source_atom_revision: 4
  source_sha256: 1d13c2c0e7b25ad434b9fb913e724ee1a420b2ef8d6715bcbbabc66fe49b8c1e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Step

## Claim

```CFEL
Atom/(.Role: Operations)/Step;
Step//{:1}((IS_CONTAINED_BY)) Workflow//;
IF Step// {=0}((RUNS)) THEN Step// {:1+}((CONTAINS)) Substep//;
IF Step// {>0}((RUNS)) THEN Step// {:0}((CONTAINS));
IF Step// {=0}((CONTAINS)) THEN Step// {:1}((RUNS)) (in (Action, Workflow))//
```

## Semantics

A Step is a unit of work within a Workflow.
