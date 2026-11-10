---
identity:
  atom_id: CA-M-464
  ref_id: CA-M-464@11
context:
  container:
    scope_unit: CA-SU-45
  role: Method
  form: Solution
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Source Retrieval
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2723
  - CA-R-2726
  - CA-R-2728
  - CA-R-2724
  depends_on:
  - CA-M-509
state:
  status: Archived
  version: 11
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-464@11-WORKBENCH_BACKEND-SOLUTION--preserve-governed-atom-data-and-reuse-native-sql.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method/archive
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Preserve governed Atom data and reuse native SQL.

## Claim scope

Direct file reading and native query semantics for Current and Draft Atom carriers excluding Archived carriers.

## Claim

### Prose Claim

Read Current and Draft Atom carriers, excluding Archived carriers, into the derived DuckDB database; every Current status, including Done and Canceled, remains included. Parse YAML and actual CommonMark headings with the existing safe reader. Generate Content schema from Current model Declarations and applicability; do not evaluate arbitrary CFEL or prose as schema. Use the selected SQL engine’s semantics and native tokenization, without another SQL parser or evaluator.

Preserve raw Header properties, original Markdown and real heading paths privately without a fixed heading list or Form validation. Build one flattened SQL column for each observed raw Header path and model-declared Content columns; source carriers, intermediate files and a third public source table are not created. Only Current Scope Unit Declarations establish current Scope Unit inventory; a Draft Declaration remains queryable only.

Normalize admitted authored inverse writing before materializing canonical direct facts. Each object row carries outgoing direct and declared-derived Relations; source or relevant Declaration changes refresh affected source/counterpart rows, mappings and hashes without source edits or Version changes. Use DuckDB and DuckPGQ for SQL/PGQ, pattern matching and traversal rather than a CAPRMEDIO traversal engine. Reachability resolves an unambiguous typed seed, selected relation types/directions, includes each typed reference once and terminates cycles; querying an inverse uses its materialized fact once.

Use CA-M-509's registry for relation names, exact inverse aliases and literal unqualified inverse bindings. Ambiguity is diagnosed and omitted, never guessed; qualified model derivations remain out of runtime facts. Keep timezone-aware values until the shared encoder returns ISO strings; retain required `pytz` rather than changing source-column casts.
