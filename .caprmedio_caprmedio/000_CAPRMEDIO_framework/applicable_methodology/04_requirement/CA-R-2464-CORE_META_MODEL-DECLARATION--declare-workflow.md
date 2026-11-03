---
atom_id: CA-R-2464
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom/(.Role := Operations)/Workflow
version: 4
updated_at: 2026-11-02 17:54:42 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2464-CORE_META_MODEL-DECLARATION--declare-workflow.md
  source_atom_id: CA-R-2464
  source_atom_revision: 4
  source_sha256: e92583eb2784f9404d3378c5cbd52b3bc6d1783d54ce4dc8778bd0987ebaf0ae
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Workflow

## Claim

```CFEL
Atom/(.Role: Operations)/Workflow;
Workflow//{:1+}((CONTAINS)) Step//;
Workflow//{:0+}((IS_RUN_BY)) Step//
```

## Semantics

A Workflow defines a graph of Steps for governed work.
