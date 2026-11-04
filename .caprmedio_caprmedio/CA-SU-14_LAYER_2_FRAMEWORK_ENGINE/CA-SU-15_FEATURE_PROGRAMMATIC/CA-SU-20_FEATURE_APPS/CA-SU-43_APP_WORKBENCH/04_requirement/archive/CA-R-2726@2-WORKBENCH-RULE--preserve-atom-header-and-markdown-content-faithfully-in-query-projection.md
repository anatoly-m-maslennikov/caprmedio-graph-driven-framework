---
atom_id: CA-R-2726
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
version: 2
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations: {}
carrier_destination:
  file:
    name: CA-R-2726@2-WORKBENCH-RULE--preserve-atom-header-and-markdown-content-faithfully-in-query-projection.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
updated_at: 2026-11-04 00:38:14 +0400
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
- preserve the complete Markdown body unchanged, including lists, links, tables, fences, fence labels, indentation, and line breaks.
- retain every mapped Content Property's complete path, heading, heading level, position, direct Markdown value and complete section Markdown; derive its parent path from the complete path.
- keep a Property's direct value separate from its descendants. A complete section includes its heading and descendants; a direct-value count does not count descendant text.
- use the applicable Header and Markdown declarations to distinguish mapped Properties from Markdown values. Heading-like text in a code fence or an undeclared child position remains Markdown value, and skipped heading levels create no Properties.
- reject duplicate YAML mapping keys and colliding normalized heading paths under one parent rather than silently merging or choosing one.
- not interpret arbitrary CFEL or prose to establish Projection data.
