---
atom_id: CA-R-2723
ref_id: CA-R-2723
container:
  scope_unit: CA-SU-43
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 3
status: Active
version: 3
updated_at: 2026-11-04 07:39:08 +0400
carrier_destination:
  file:
    name: CA-R-2723-WORKBENCH-RULE--derive-the-query-projection-only-from-governed-atom-sources.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---
## Summary

Derive the query Projection only from governed Atom sources

## Claim scope

The query Projection of canonical Current and Draft Atom carriers in the governed source inventory.

## Claim

### Prose Claim

The query Projection **must**:

- derive its data only from canonical Current and Draft Atom carriers in the governed source inventory; Archived carriers are excluded.
- retain each indexed carrier's source locator, Atom identity, Version, lifecycle group, parsed Header, Markdown Content, and mapped Content Properties.
- make each source-derived Projection row include a hash for that row's complete Projection data.
- include every Current carrier regardless of its status, including Done and Canceled, and keep Current and Draft groups distinct. A carrier in one group **must not** overwrite a carrier in another group solely because they share a base ID.
- derive current Scope Unit structure only from Current Scope Unit Declarations. Draft Declarations remain queryable Atoms but do not establish Current structure. Parse source YAML and Markdown directly; no Declaration-to-reader-schema compiler is required.
- treat an observed Atom identity and Version as source data, not as a fixed-file pin or proof of a Journal record.
- remain derived data that can be rebuilt from its sources.
- never edit, move, archive, promote, or invent a source Atom.
