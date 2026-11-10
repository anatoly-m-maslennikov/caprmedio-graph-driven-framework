---
identity:
  atom_id: CA-E-675
  ref_id: CA-E-675@8
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data
      Handling <+ Source Retrieval
    dependencies:
    - CAPRMEDIO_MODEL <+ Projection
  tier: 5
relations:
  evaluation_for:
  - CA-R-2726
  - CA-M-464
  - CA-D-672
state:
  status: Archived
  version: 8
  updated_at: 2026-11-09 07:45:14 +0400
destination:
  file:
    name: CA-E-675@8-WORKBENCH_BACKEND-EVAL_CASE--preserve-nested-header-and-markdown-property-distinction.md
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

YAML Header and Markdown Content are parsed directly with the safe YAML reader and actual CommonMark heading tree, with Content columns generated from Current model Declarations rather than a fixed heading list. Private parsed Header and Markdown data retain their distinctions and complete body. The public `atoms` table supports Mode 1 with only model-declared Header paths and declared Markdown Content, or Mode 2, enabled by default, with every observed Header path from valid source Atoms and declared Markdown Content, including paths with null or empty values. Header paths use dots between levels and snake_case within each segment, without old short-name aliases such as `id`, `status` or `role`. Source Header nesting and values stay unchanged. It also exposes declared `content.*` columns, using full lowercase snake_case paths such as `content.claim.prose_claim` and `content.claim.formal_claim`; it does not expose raw `header_json`, `content_markdown`, `content_properties_json` or `relation_edges_json` buckets. Nested Content Properties retain path segments, heading, direct Markdown, and complete subtree Markdown; parent path derives from segments. No `source_bytes` or `header_raw` is projected.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Header absence, null, empty values, scalar/list shape, false, and zero | Private parsed Header data keeps the values distinct; no raw `header_json` column is exposed publicly. |
| LF, CRLF, or mixed frontmatter delimiter line endings | Parse the Header and preserve the Markdown body’s exact original line endings. |
| Duplicate YAML key | The source is rejected with stderr error and no row. |
| Declared nested Property with direct text and child | Direct and subtree Markdown remain separate; parent derives from segments. |
| New or changed real Markdown heading | Its actual normalized path and direct/complete section values remain available to the parser; only declared Content Properties become public columns after refresh. Regenerate the Content schema from the applicable Current Declarations; arbitrary CFEL formulas and prose are not evaluated. |
| Claim with Prose Claim, Formal Claim, and fenced heading-like text | Declared nesting and CFEL fence survive without false Properties; public values use quoted full paths such as `"content.claim.prose_claim"`. |

Verify `Header.Context.Plan` maps to `header.context.plan`, and serialized nested `context.plan.work_sequence_number` maps to `header.context.plan.work_sequence_number`, without adding a YAML Header wrapper. Cover optional/missing values, null, empty string, false, zero, collections and nested direct values. An ambiguous flattening of distinct source paths fails explicitly instead of merging them or creating aliases. Atom `header.relations` still matches native direct-and-derived graph facts with no duplicate raw relation bucket. Scope Unit and technical metadata columns keep their distinct meaning.

Under Mode 2, verify that a newly observed Header path, removal of its last occurrence, a format/type change, or a previously populated path becoming empty across the complete valid source inventory rebuilds the schema asset and affected source tables and rereads the inventory. A path still present with null, an empty string or an empty collection remains queryable; only a removed path loses its column. Display metadata marks wholly empty result columns for hiding without changing SQL values or counts. False and zero are values. A normal edit with the same schema updates only affected rows. Arbitrary Markdown headings still do not create Content columns.
