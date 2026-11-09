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
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data
      Handling <+ Schema
    dependencies:
    - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  tier: 7
relations:
  evaluation_for:
  - CA-R-2724
  - CA-M-509
state:
  status: Active
  version: 2
  updated_at: 2026-11-09 07:45:14 +0400
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

Verify canonical relation materialization from Current Requirement relation Declarations:

- Accept the admitted Declaration Forms, including Relation Declaration. A Draft declaration does not register a type or change the Current registry.
- For a declared direct relation and its inverse alias, materialize the same canonical direct fact from either authored direction. Swap inverse endpoints once. When both writings occur, do not duplicate that fact or its inverse view.
- Accept an explicit inverse alias without a separate Declaration for that alias. Resolve exact model addresses; use unique case-folded spelling only for carrier relation keys.
- On ambiguous names, case-colliding native labels or inverse metadata, warn and omit the affected facts or bindings without choosing a winner. Keep unrelated valid facts and source files unchanged.
- Use effective Header.Container, including its Context carrier layout. Resolve the Project root as uppercase(Project prefix) followed by -SU-00.
- After source create, edit, move, rename, deletion, invalidation or repair, update the affected direct and inverse facts and row hashes. A still-referenced missing target remains a typed reference; its source reappearance does not duplicate facts.
- After a relevant Declaration edit, refresh the registry and the graph from the same source state. Ordinary unrelated edits retain the incremental path.
- Run these lifecycle cases as single-source events and multi-source batches. Compare their final relation columns, traversal results and row hashes with a full rebuild from the same final source state.
- Do not evaluate prose, general CFEL formulas or qualified Model derivations as runtime relation facts.

Check the outgoing relation columns and native SQL/PGQ traversal against the same expected facts. Check source bytes separately to prove indexing did not edit them.
