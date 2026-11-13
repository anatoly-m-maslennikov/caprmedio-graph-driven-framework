---
identity:
  atom_id: CA-E-677
  ref_id: CA-E-677
context:
  container:
    scope_unit: CA-SU-45
  role: evaluation
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
  status: active
  version: 31
  updated_at: '2026-11-12T17:04:50.228756+00:00'
destination:
  file:
    name: CA-E-677-WORKBENCH_BACKEND-EVAL_CASE--reconcile-source-lifecycle-changes-and-repaired-validity.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Reconcile source lifecycle changes and repaired validity

## Claim scope

Atomic refresh of Workbench source data, Scope Units, and graph facts under the installed model.

## Claim

### Prose Claim

Verify that Workbench publishes selected source changes to `atoms`, `scope_units`, and graph facts together. Ordinary create, update, move, rename, and remove operations change only the affected rows and relation neighbours. Initial indexing and explicit reread may scan the full selected source set. Neither refresh nor reread recompiles the installed model or relation registry.

Verify that startup selects Current, Draft, and Backlog carriers throughout the Project authority root. An explicit Archive request adds only the selected Scope Unit and Role folders. Each readable physical carrier has its own row, including duplicate Atom IDs and Versions. Only eligible Current Scope Unit Declarations and Delegations establish structure. Resolve competing model declarations independently of retaining source rows.

Verify that Mode 1 uses declared Header and Content fields, and Mode 2 uses observed Header fields at cold start and declared Content fields. Both use dotted lowercase snake_case. Verify declared model changes after asset refresh and image rebuild. Source-data changes leave the installed model and registry fixed. Check native direct and derived relations and deterministic SHA-256 row hashes excluding `hash`.

Verify that an unreadable, unstable, or unparseable file is omitted, reported, and skipped without retry. A parseable file remains queryable when it violates the current schema. An index transaction failure or invalid Current structural declaration leaves the owner unavailable pending explicit restart. Audits report findings after source publication and compare duplicate ID and Version only for Current and loaded Archived carriers.

## Details

Run the watcher operations on real Project and disposable sources. Include matching carriers outside declared Role directories, and exclude out-of-root paths and symlinks. Test literal Project prefixes, matching malformed files, nested Header values, and declared Content. Reconcile final rows, relation endpoints and hashes with an explicit reread using the same loaded scope coverage. Check unchanged batches, failed publication, and cleanup. Verify that these operations leave source bytes and Versions unchanged.

Measure cold index, full reread and idle CPU, RAM, and elapsed time without a profiler, using the same inventory and limits. Report image identity and row counts. Keep the existing latency and throughput gates.

For an ordinary Atom delta, verify that source capture, graph updates and audit preparation touch only affected paths, rows and neighbours. Detect full inventory traversal or copies even when no full rebuild runs. Keep the existing latency and throughput limits.
