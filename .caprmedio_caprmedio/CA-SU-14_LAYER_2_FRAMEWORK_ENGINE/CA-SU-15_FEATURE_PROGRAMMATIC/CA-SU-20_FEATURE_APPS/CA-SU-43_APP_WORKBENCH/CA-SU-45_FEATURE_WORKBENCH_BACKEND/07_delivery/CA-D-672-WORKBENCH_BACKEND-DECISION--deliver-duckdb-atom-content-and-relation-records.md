---
identity:
  atom_id: CA-D-672
  ref_id: CA-D-672
context:
  container:
    scope_unit: CA-SU-45
  role: Delivery
  form: Decision
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Schema
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 4
relations:
  delivery_for:
  - CA-R-2723
  - CA-R-2726
  - CA-R-2724
  depends_on:
  - CA-M-509
  - CA-D-715
state:
  status: Active
  version: 19
  updated_at: 2026-11-11 01:07:01 +0400
destination:
  file:
    name: CA-D-672-WORKBENCH_BACKEND-DECISION--deliver-duckdb-atom-content-and-relation-records.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/07_delivery
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Deliver DuckDB Atom, Content Property, and relation records

## Claim scope

The derived `atoms` and `scope_units` tables and their complete parsed Header, Markdown heading paths, nested values, and materialized outgoing Relations.

## Claim

### Prose Claim

Read governed sources directly through the Current-model parser into a file-backed DuckDB Projection. Expose `atoms` and `scope_units` as graph-source tables. Technical `change_log` and the audit tables delivered under CA-D-715 are queryable derived metadata, not graph sources or sources of truth. Internal mappings/results, database/spill, selected schema and incremental snapshots belong under the Workbench runtime directory. Do not retain source-byte/frontmatter/intermediate copies.

Parse complete YAML and actual Markdown heading paths, preserving missing/null/empty/scalar/list/map/false/zero distinctions and complete mapped content. Current structural Declarations/Delegations establish `scope_units`; Draft structural carriers remain atoms. Mode 1 exposes current-model declared Header/Content through the grouped adapter and accepted read aliases only; enabled Mode 2 exposes every observed raw Header path plus declared Content. Names use dotted lowercase snake_case paths. Header relations are one native `header.relations` JSON projection; `header.context.container` is the Mode-2 grouping-node exception. Do not expose whole Header/Markdown/property buckets, short aliases, second source tables or arbitrary CFEL/prose evaluation.

Both modes retain their schema triggers: Mode 2 complete-inventory new/last-removed/type-changed/globally emptied path; Mode 1 changed declaration schema or new/last-removed wildcard-admitted Content path. Same-schema edits remain incremental. Generate and validate `workbench_schema.json` on every image rebuild with the query model generated from Current Declarations, including Role and Form applicability; runtime schema state stays derived.

`atoms` identifies carrier path/filename, Current-or-Draft lifecycle, exact reference, typed `header.*`/`content.*`, native `header.relations` and deterministic row hash excluding `hash`. `scope_units` identifies declared name/ID/parent/label/order, Current structural source path/version, native relations and the same hash rule. Relations use the CA-M-509 registry: exact canonical/declared inverse aliases or unique case-folded carrier spelling normalize once without source edits; ambiguity/case collision warns and omits affected projected links. References remain typed references, and direct/derived counterparts refresh with their supporting source while source bytes/Versions do not change. DuckPGQ uses typed Atom/Scope Unit identities and declared labels only; it is derived implementation state, not another table or authority.
