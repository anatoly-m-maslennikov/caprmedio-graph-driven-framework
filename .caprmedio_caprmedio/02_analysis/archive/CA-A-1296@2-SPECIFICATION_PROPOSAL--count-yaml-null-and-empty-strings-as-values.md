---
atom_id: CA-A-1296@2
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Model::CAPRMEDIO::Graph Syntax.Cardinality Notation
version: 2
relations: {}
tier: 3
updated_at: 2026-10-29 21:51:04 +0400
---
# Summary

Count YAML null and empty strings as values

## Decision

Follow standard YAML value interpretation rather than inventing another null or empty-string policy. Both null and an empty string are values and each contributes one direct value to cardinality. An omitted property has zero direct values. Null is not silently converted into absence.

```yaml
plain_string: asdf
null_value: null
also_null:
empty_string: ""
quoted_null_string: "null"
```

The first value is a string; the next two are null; the last two are strings. Quoting and the YAML parser determine the resulting values. The installed YAML parser was checked on these examples when this proposal was recorded.

The declared value Format and any applicable conditions in prose determine admissibility. An empty string passes the basic string type but may fail a separate nonempty-content condition. Null contributes one value even when it fails a property's declared format. Cardinality alone is not a complete validity check. This adds no universal null prohibition, universal nonempty-string condition or new null Format.

The grouping rule remains independent: subjects{0} has no direct values but may have declared child properties. A YAML mapping carrying those children does not become an extra direct value. A direct subjects null would instead contribute one direct value.

## State

The Cardinality and Value Format Definition Drafts, related R/M/E/D syntax guidance and the main Model proposal state this distinction. Current sources, YAML reader code and runtime remain unchanged.
