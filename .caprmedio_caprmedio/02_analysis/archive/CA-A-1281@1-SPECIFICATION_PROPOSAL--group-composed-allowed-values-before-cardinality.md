---
atom_id: CA-A-1281@1
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Model::CAPRMEDIO::Graph Syntax.Cardinality Notation
version: 1
relations: {}
tier: 3
updated_at: 2026-10-29 01:27:27 +0400
---
# Summary

Group composed allowed values before cardinality

## Decision

Use the Operator expression:

```text
atom.id: (@(Project.name.prefix)-@(content role.first letter)-number[int, unique(its current kind)]){1}
```

Parentheses group the entire composed allowed-value expression after the colon. The following `{1}` applies to the complete group, not only to the final number component. `[int, unique(its current kind)]` still qualifies that number component. The colon retains its allowed-value meaning. Do not move the count or invent a string-format annotation before the colon for this expression.

The value-group parentheses are distinct from `@(...)` reference delimiters, `unique(...)` selection arguments and `((RELATION_TYPE))` relation delimiters. This settles this grouping boundary, not a complete general-purpose expression grammar.

## State

The Model proposal and R/M/E/D syntax Drafts are aligned. The canonical governed property selector remains the existing Atom ID property; no Subject rename, new stored ID component, Current migration or parser implementation is introduced.
