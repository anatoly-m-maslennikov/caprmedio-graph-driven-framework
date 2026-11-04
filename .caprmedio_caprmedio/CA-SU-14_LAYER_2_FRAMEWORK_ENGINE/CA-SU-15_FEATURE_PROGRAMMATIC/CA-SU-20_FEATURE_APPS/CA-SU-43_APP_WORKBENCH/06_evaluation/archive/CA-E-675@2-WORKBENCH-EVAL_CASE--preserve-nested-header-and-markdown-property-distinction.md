---
atom_id: CA-E-675
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
author: Anatoly Maslennikov
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
version: 2
role: Evaluation
form: Eval Case
tier: 5
carrier_destination:
  file:
    name: CA-E-675@2-WORKBENCH-EVAL_CASE--preserve-nested-header-and-markdown-property-distinction.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/archive
relations:
  evaluation_for: [CA-R-2726, CA-M-464, CA-D-672]
updated_at: 2026-11-04 00:38:14 +0400
---
## Summary

Preserve nested Header and Markdown Property distinctions

## Claim scope

Current-model-guided in-memory parsing of governed carriers.

## Claim

### Prose Claim

YAML Header and Markdown Content are parsed according to the Current model and applicable Current declarations through an in-memory Reader Schema Projection, not fixed headings. `header_json` retains YAML distinctions and `content_markdown` the raw body. Nested Content Properties retain path segments, heading, direct Markdown, and complete subtree Markdown; parent path derives from segments. No `source_bytes` or `header_raw` is projected.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Header absence, null, empty values, scalar/list shape, false, and zero | `header_json` keeps the values distinct. |
| Duplicate YAML key | The source is rejected with stderr error and no row. |
| Declared nested Property with direct text and child | Direct and subtree Markdown remain separate; parent derives from segments. |
| Current declaration mapping edit | A refresh re-parses affected sources under the new mapping; fixed headings are not invented. |
| Claim with Prose Claim, Formal Claim, and fenced heading-like text | Declared nesting and CFEL fence survive without false Properties. |
