---
identity:
  atom_id: CA-R-2726
  ref_id: CA-R-2726@7
context:
  container:
    scope_unit: CA-SU-43
  role: Requirement
  form: Direct Policy
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 3
state:
  status: Archived
  version: 7
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-2726@7-WORKBENCH-DIRECT_POLICY--preserve-atom-header-and-markdown-content-faithfully-in-query-projection.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---
## Summary

Preserve Atom Header and Markdown Content faithfully in the query Projection

## Claim scope

The parsed Header and Markdown Content of every valid canonical Atom carrier.

## Claim

### Prose Claim

The Projection preserves complete parsed YAML Header and Markdown body, including nested mappings/lists, lists/links/tables/fences/indentation/line breaks, actual heading paths and complete mapped Content sections. It distinguishes absent/null/empty scalar-or-collection/false/zero; display metadata treats null/empty string/list/map as empty while false/zero remain values without changing SQL values/counts.

Mode 1 exposes model-declared Header paths; enabled Mode 2 exposes every observed valid Header path, including null/empty. Both use dotted full Header paths with snake_case segments and remove short `id`/`role`/`status` aliases; Header has no wrapper or flat copy. Declared Content paths use the same notation, preserve parent direct value separately from nested Properties, and arbitrary presentation headings never become columns. Complete parser data remains private: `atoms` exposes no raw Header/Markdown/property/relation JSON buckets.

Parse YAML and the actual CommonMark tree directly: no Form conformance or graph authority, synthetic skipped-level Properties or fenced-text headings. Reject duplicate YAML keys and colliding normalized declared child headings; allow repeated arbitrary prose headings. Never interpret arbitrary CFEL or prose as Projection data.
