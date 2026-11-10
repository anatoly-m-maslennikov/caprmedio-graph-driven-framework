---
identity:
  ref_id: CA-E-803
  id: CA-E-803
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Schema
    dependencies:
    - MODEL//CAPRMEDIO <+ CFEL <+ Relation
  tier: 7
relations:
  evaluation_for:
  - CA-R-2724
  - CA-M-509
state:
  status: Active
  version: 3
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-803-WORKBENCH_BACKEND-EVAL_CASE--verify-canonical-direct-and-inverse-relation-facts.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
author: Anatoly Maslennikov
---
## Summary

Verify canonical direct and inverse relation facts

## Claim

### Prose Claim

Verify Current Requirement relation Declarations, including Relation Declaration, register admitted direct facts and inverse aliases; Draft declarations do not change the Current registry. Either authored direction materializes one canonical direct fact, swaps inverse endpoints once, and does not duplicate direct/inverse views. Exact model addresses are required; unique case-folding applies only to carrier keys.

Use effective Header.Container and resolve Project root as `uppercase(Project prefix)-SU-00`. Ambiguous names, inverse metadata or case-colliding native labels warn and omit affected facts/bindings without choosing a winner; unrelated facts/source bytes remain unchanged. Create/edit/move/rename/delete/invalidate/repair refreshes affected direct/inverse facts and hashes; missing targets remain references and reappearance does not duplicate. Compare single/multi-source final columns, traversal and hashes with a full rebuild, while unrelated edits stay incremental. Prose, general CFEL and qualified derivations are never runtime facts.
