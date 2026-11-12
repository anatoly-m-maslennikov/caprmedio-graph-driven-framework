---
identity:
  atom_id: CA-R-2723
  ref_id: CA-R-2723
context:
  container:
    scope_unit: CA-SU-43
  role: requirement
  form: direct_policy
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 3
state:
  status: active
  version: 6
  updated_at: '2026-11-12T01:41:48.589873+00:00'
destination:
  file:
    name: CA-R-2723-WORKBENCH-DIRECT_POLICY--derive-the-query-projection-only-from-governed-atom-sources.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---
## Summary

Derive the query Projection only from governed Atom sources

## Claim scope

The query Projection of governed Atom carriers, including selected Archive folders.

## Claim

### Prose Claim

The query Projection **must**:

- index Current, Draft and Backlog Atom carriers at Workbench startup.
- load Archive contents on demand for one or more requested Scope Unit and Role pairs. Resolve each pair to the model-declared Archive folder and its admitted aliases. Add the selected Archive rows to `atoms` and report the loaded scope coverage. A new Workbench owner starts without loaded Archive scopes.
- keep separate rows for physical files using Project-relative path and filename. A repeated load must not duplicate a physical file.
- reserve known Archive IDs and Versions for lifecycle allocation even when their content rows are unloaded. Use filename metadata where it identifies them. If an exact historical selector or safe allocation needs an unloaded Archive, report that it is unloaded separately from a missing revision. A lifecycle operation may read an exact newly archived file it already identifies.
- retain each indexed carrier's source locator, Atom identity, Version, lifecycle group, parsed Header, Markdown Content, and mapped Content Properties.
- make each source-derived Projection row include a hash for that row's complete Projection data.
- include every Current carrier regardless of its status, including Done and Canceled, and keep Current and Draft groups distinct. A carrier in one group **must not** overwrite a carrier in another group solely because they share a base ID.
- derive current Scope Unit structure only from Current Scope Unit Declarations. Draft Declarations remain queryable Atoms but do not establish Current structure. Parse source YAML and Markdown directly; no Declaration-to-reader-schema compiler is required.
- treat an observed Atom identity and Version as source data, not as a fixed-file pin or proof of a Journal record.
- remain derived data that can be rebuilt from its sources.
- never edit, move, archive, promote, or invent a source Atom.
