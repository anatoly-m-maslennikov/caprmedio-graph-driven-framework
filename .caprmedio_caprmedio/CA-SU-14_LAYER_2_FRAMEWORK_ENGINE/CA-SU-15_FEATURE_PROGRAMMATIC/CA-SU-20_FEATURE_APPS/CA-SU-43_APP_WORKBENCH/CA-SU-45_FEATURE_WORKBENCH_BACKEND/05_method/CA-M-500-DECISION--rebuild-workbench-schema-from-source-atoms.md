---
identity:
  atom_id: CA-M-500
  ref_id: CA-M-500
context:
  container:
    scope_unit: CA-SU-45
  role: Method
  form: Decision
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Schema
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2726
state:
  status: Active
  version: 7
  updated_at: 2026-11-10 22:20:17 +0400
destination:
  file:
    name: CA-M-500-DECISION--rebuild-workbench-schema-from-source-atoms.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method
author: Anatoly Maslennikov
---
## Summary

Rebuild the Workbench schema from source Atoms.

## Claim scope

The schema asset and source tables used by WORKBENCH_BACKEND.

## Claim

### Prose Claim

Keep the Workbench schema a rebuildable asset, not a handwritten Python property list. Header/Markdown SQL names use dotted path levels and lowercase snake_case segments (`header.identity.atom_id`, `header.context.container`, `content.claim.formal_claim`); the asset, SQL interface, MCP results and `query_schema` use those same names.

Mode 1 derives canonical Header names and formats from the existing grouped Header carrier adapter and Current declarations, using accepted aliases only for reads and rejecting conflicts. `Header.ID` binds to `identity.atom_id`; timestamps retain existing offset-bearing `TIMESTAMPTZ` rules. Mode 2, enabled now, retains every observed raw Header path from valid sources—distinct source spellings stay distinct—while Content remains Current-model-declared. It retains empty paths, uses `header.context.container` JSON as the sole grouping-node exception, and exposes `header.relations` as one native direct/derived JSON projection. Neither mode adds a full Form validator or rewrites source Headers.

Generate `workbench_schema.json` at image build and keep selected projection/Content schema state under `.caprmedio_runtime/workbench`; both are derived and validated/rebuilt from valid inputs when stale or missing. Mode 2 rebuilds schema/tables and rereads the complete valid inventory for a new/last-removed Header or model-admitted Content path, format/type change, or previously populated path becoming globally empty; zero and false are values. Mode 1 does so for changed Current-model declared Header/Markdown schema or a new/last-removed Content path admitted by its wildcard declarations. An ordinary value edit with unchanged schema remains incremental.

On every image rebuild, regenerate the rebuildable query model and schema asset from Current Declarations, including Role and Form applicability, Content wildcards and more specific Content rules. Compile those rules as inputs permit and retain exact provenance; specific Prose Claim and fenced-heading rules take precedence over generic wildcard interpretation. This model supports queryable Content across Concern, Analysis & Advisory, Plan, Requirement, Method, Evaluation, Delivery and Operations without a fixed RMEDO or Claim-heading whitelist. Do not relabel other Roles’ bodies as Claims. Candidate schema state is owner-local: preserve invalid-content exclusion, duplicate filtering, relation projection, asset regeneration and full-rebuild boundaries; do not add a second source, public query setting or background schema service.
