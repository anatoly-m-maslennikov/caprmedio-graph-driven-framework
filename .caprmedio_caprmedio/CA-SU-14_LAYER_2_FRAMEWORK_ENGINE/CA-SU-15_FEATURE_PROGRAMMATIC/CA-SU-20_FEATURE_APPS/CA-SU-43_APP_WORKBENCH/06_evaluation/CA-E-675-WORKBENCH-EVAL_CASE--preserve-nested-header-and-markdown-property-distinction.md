---
atom_id: CA-E-675
ref_id: CA-E-675
container:
  scope_unit: CA-SU-43
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 5
relations:
  evaluation_for: [CA-R-2726, CA-M-464, CA-D-672]
status: Active
version: 5
updated_at: 2026-11-04 21:06:25 +0400
carrier_destination:
  file:
    name: CA-E-675-WORKBENCH-EVAL_CASE--preserve-nested-header-and-markdown-property-distinctions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---
## Summary

Preserve nested Header and Markdown Property distinctions

## Claim scope

Current-model-guided in-memory parsing of governed carriers.

## Claim

### Prose Claim

YAML Header and Markdown Content are parsed directly with the safe YAML reader and actual CommonMark heading tree, not a fixed heading list or Declaration-to-schema compiler. Private parsed Header and Markdown data retain their distinctions and complete body. The public `atoms` table exposes only declared `content.*` columns, using quoted lowercase business-language paths such as `content.claim.prose claim` and `content.claim.formal claim`; it does not expose raw `header_json`, `content_markdown`, `content_properties_json` or `relation_edges_json` buckets. Nested Content Properties retain path segments, heading, direct Markdown, and complete subtree Markdown; parent path derives from segments. No `source_bytes` or `header_raw` is projected.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Header absence, null, empty values, scalar/list shape, false, and zero | Private parsed Header data keeps the values distinct; no raw `header_json` column is exposed publicly. |
| LF, CRLF, or mixed frontmatter delimiter line endings | Parse the Header and preserve the Markdown body’s exact original line endings. |
| Duplicate YAML key | The source is rejected with stderr error and no row. |
| Declared nested Property with direct text and child | Direct and subtree Markdown remain separate; parent derives from segments. |
| New or changed real Markdown heading | Its actual normalized path and direct/complete section values remain available to the parser; only declared Content Properties become public columns after refresh. No Declaration schema compiler is invoked. |
| Claim with Prose Claim, Formal Claim, and fenced heading-like text | Declared nesting and CFEL fence survive without false Properties; public values use quoted full paths such as `"content.claim.prose claim"`. |
