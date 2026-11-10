---
identity:
  atom_id: CA-E-677
  ref_id: CA-E-677
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Indexing
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 5
relations:
  evaluation_for:
  - CA-R-2723
  - CA-R-2725
  - CA-M-465
  - CA-M-500
  - CA-D-672
  - CA-D-675
state:
  status: Active
  version: 25
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-677-WORKBENCH_BACKEND-EVAL_CASE--reconcile-source-lifecycle-and-invalid-repair-state.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Reconcile source lifecycle changes and repaired validity

## Claim scope

Atomic file-backed refresh of governed sources, Current declarations, and the rebuildable derived schema.

## Claim

### Prose Claim

Transactionally apply selected source changes to `atoms`, `scope_units` and graph facts. Ordinary Atom create/edit/rename/move/removal updates only changed rows and affected relation neighbours; initial indexing, explicit reread, actual structural/registry changes and complete-inventory schema changes retain their rebuild path. Current/Draft carriers—including Done/Canceled Current—are included; Archived is excluded. Only Current Scope Unit Declarations/Delegations establish structure; Draft structural carriers remain Atom rows.

The schema asset is derived state under `.caprmedio_runtime/workbench`. Mode 1 exposes current-model declared Header/Content; enabled Mode 2 exposes dotted lowercase-snake-case observed Header paths plus model-declared Content. No CFEL/prose evaluation occurs. Mode-specific complete-inventory schema triggers preserve their declared boundaries; same-schema value edits stay incremental. Row hashes are SHA-256 of deterministic canonical row JSON excluding `hash`, including materialized Atom relations.

Ordinary invalid/unreadable/unstable capture is excluded, reported to stderr and not retried. Index transaction failure, invalid Current Scope Unit Declaration/Delegation makes the owner unavailable pending explicit restart; do not skip structural sources or serve partial/stale state. Saved SQL remains a separate UTF-8 runtime artifact. Verify real-project and fixture incremental matrices before/after change, cleanup, full reread/structural/schema rebuild and failed-write nonpublication; an unchanged/non-source batch performs no graph/hash/database work.

Resource measurement compares unprofiled CPU/RAM on the same frozen inventory/budget, separately reporting cold index, full reread and idle period with CPU/elapsed/sampled usage, RAM accounting, image IDs and row counts. Preserve existing latency/throughput gates and investigate repeatable slowdown; never relax limits for savings.

## Details

Exercise lifecycle, schema and graph cases for Current/Draft/Archived carriers, structural Current-only admission, duplicate/invalid exclusion, exact Header path/type/empty semantics, model Content schema changes, Task `IS_CONTAINED_BY`/derived `CONTAINS`, ambiguity/case collision omission, source removal/repair, registry change and reappearance. Compare final rows, relations, traversal and hashes with a full rebuild; source bytes/Versions stay unchanged. Validate native direct/derived relation facts and no third source/graph table, source copy, retry, rollback or fabricated watcher event.
