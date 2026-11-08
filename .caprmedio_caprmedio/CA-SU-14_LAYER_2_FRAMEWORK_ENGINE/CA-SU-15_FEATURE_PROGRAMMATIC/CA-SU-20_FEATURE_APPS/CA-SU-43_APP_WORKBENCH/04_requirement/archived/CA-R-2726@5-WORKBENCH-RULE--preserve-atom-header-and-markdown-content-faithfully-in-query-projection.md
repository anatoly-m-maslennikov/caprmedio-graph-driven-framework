---
atom_id: CA-R-2726
ref_id: CA-R-2726@5
container:
  scope_unit: CA-SU-43
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 3
status: Archived
version: 5
updated_at: 2026-11-06 20:37:19 +0400
carrier_destination:
  file:
    name: CA-R-2726@5-WORKBENCH-RULE--preserve-atom-header-and-markdown-content-faithfully-in-query-projection.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archived
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

The query Projection **must**:

- preserve the complete parsed YAML Header, including nested mappings and lists.
- preserve the difference between an absent key, null, an empty string, an empty list or mapping, a scalar, a one-item list, false, and zero.
- for display metadata, treat null, an empty string, an empty list and an empty mapping as empty; treat false and zero as values. This does not change the SQL values or counts.
- preserve the complete Markdown body unchanged, including lists, links, tables, fences, fence labels, indentation, and line breaks.
- retain every mapped Content Property's complete path, heading, heading level, position, direct Markdown value and complete section Markdown; derive its parent path from the complete path.
- expose every observed Header Property path found in valid source Atoms, including paths with null or empty values as a full lowercase snake_case SQL column, such as `header_context_plan`. The name preserves the full Header path with underscores in place of separators and spaces. Remove short Header convenience names such as `id`, `role` and `status` rather than retain aliases. Header remains the logical frontmatter root; no YAML wrapper or authored flat copy is added.
- expose declared Markdown Content Properties as dot-separated SQL paths with snake_case segments, such as `content.summary`, `content.claim.prose_claim`, `content.claim.formal_claim`, and `content.details`. Preserve the complete prose and every nested heading; a parent content column keeps its direct value and each declared nested Content Property gets a separate column. Arbitrary prose presentation headings remain inside the value and never become SQL columns.
- keep complete parsed Header and Markdown data private to the reader and graph pipeline. The public `atoms` table does not expose raw `header_json`, `content_markdown`, `content_properties_json`, or `relation_edges_json` columns.
- keep a Property's direct value separate from its descendants. A complete section includes its heading and descendants; a direct-value count does not count descendant text.
- parse YAML properties and the actual Markdown heading tree directly. The first heading may have any level; skipped levels create no synthetic Properties. Heading-like text inside code is Markdown value, not a section. Parsing does not establish Atom Form conformance or graph authority.
- reject duplicate YAML mapping keys and colliding normalized declared Content Property heading paths under one parent rather than silently merging or choosing one; repeated arbitrary prose headings are allowed.
- not interpret arbitrary CFEL or prose to establish Projection data.
