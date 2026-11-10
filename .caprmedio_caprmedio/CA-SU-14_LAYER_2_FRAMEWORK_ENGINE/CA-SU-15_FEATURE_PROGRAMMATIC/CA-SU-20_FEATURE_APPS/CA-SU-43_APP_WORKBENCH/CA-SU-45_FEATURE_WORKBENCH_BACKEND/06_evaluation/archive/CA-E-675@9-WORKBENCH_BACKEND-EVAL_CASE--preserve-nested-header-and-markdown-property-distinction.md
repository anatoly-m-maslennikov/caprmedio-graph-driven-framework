---
identity:
  atom_id: CA-E-675
  ref_id: CA-E-675@9
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Source Retrieval
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 5
relations:
  evaluation_for:
  - CA-R-2726
  - CA-M-464
  - CA-D-672
state:
  status: Archived
  version: 9
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-675@9-WORKBENCH_BACKEND-EVAL_CASE--preserve-nested-header-and-markdown-property-distinction.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation/archive
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Preserve nested Header and Markdown Property distinctions

## Claim scope

Current-model-guided in-memory parsing of governed carriers.

## Claim

### Prose Claim

Parse YAML Header and actual CommonMark headings directly. Private parsed Header/Markdown retain their distinction and complete body; public Mode 1 exposes only model-declared Header/Content paths, while enabled Mode 2 exposes every observed valid Header path and declared Content columns. Names use dotted lowercase snake_case paths, never old `id`/`status`/`role` aliases; do not expose raw Header/Markdown/property/relation buckets or source bytes.

## Details

Verify absence/null/empty/scalar/list/map/false/zero distinctions; LF/CRLF preservation; duplicate-key rejection; nested direct versus subtree Markdown; actual headings versus declared public Content; and Prose Claim/Formal Claim/fenced-heading handling. `Header.Context.Plan` maps to `header.context.plan` without a wrapper; ambiguous flattening fails rather than merging paths. `header.relations` matches native facts once. Mode 2 rebuilds for new/last-removed/type-changed/globally emptied Header paths, keeps observed empty paths and treats false/zero as values; same-schema edits stay incremental and arbitrary headings do not become Content columns.
