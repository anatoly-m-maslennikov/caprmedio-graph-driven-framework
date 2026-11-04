---
atom_id: CA-M-462
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
version: 5
author: Anatoly Maslennikov
role: Method
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  method_for:
  - CA-R-2728
carrier_destination:
  file:
    name: CA-M-462-WORKBENCH-ENG_DECISION--constrain-public-duckdb-queries-to-native-read-only-access.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method
updated_at: 2026-11-04 15:43:14 +0400
---

## Summary

Constrain public DuckDB queries to native read-only access.

## Claim scope

Public SQL access to the in-memory DuckDB Projection.

## Claim

### Prose Claim

Accept one read query from trusted Operator or MCP input. Use DuckDB's native parsing/query APIs, including DuckPGQ's native SQL/PGQ grammar. Where the statement-extraction utility does not support that grammar, use DuckDB's native tokenization to count statements and select query input. Do not introduce a regular-expression SQL filter, homemade parser, function sandbox, or second query language.

Execute the exact accepted SQL once in a native `BEGIN TRANSACTION READ ONLY` transaction, fetch its complete result, and finish normally with `COMMIT`. Multiple statements and write commands are unsupported. Known invalid requests, rejected SQL and result-delivery errors return their useful reason to the originating MCP or web caller through the existing public error boundary, and report stderr. They are not empty successful results or retried requests. An ordinary rejected query leaves the valid owner available for the next request. A known failed owner returns an explicit Workbench-unavailable, restart-required message; its technical detail stays on stderr. Unexpected internal failures use the existing generic public error boundary instead of exposing arbitrary exception detail.

Trusted startup loads DuckPGQ and enables its grammar before disabling external access, extension autoinstall/autoload, and configuration changes. The public request does not install extensions or change source files. Graph setup and refresh remain trusted application work. Ordinary internal engine caching is not a change to logical Projection facts.

This MVP does not promise a capability sandbox against DuckPGQ's internal management functions. Those calls are unsupported and can invalidate the connection even in a read-only transaction. Report that engine failure explicitly; a Workbench restart may be required. Do not add automatic query retries, application rollback, retained-state restoration, or connection recovery.

Use an empty temporary directory, no Sequences, and only the two public tables plus internal in-memory graph mappings. The selected runtime must prove that normal queries do not spill to files. No database, snapshot, schema, or log file is created by the Projection.
