---
atom_id: CA-R-draft
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: Model::CAPRMEDIO::Graph Syntax.Format Notation
  depends_on:
  - Model::CAPRMEDIO::Graph Syntax::Format
  - Model::CAPRMEDIO::Continuant/Selection
version: 1
relations: {}
tier: 1
updated_at: 2026-10-29 03:22:57 +0400
---
# Summary

Define Value Constraint Annotations

## Claim

A [format, condition] annotation specifies the format of each direct property value and an additional condition on it. Its expressions are interpreted as materialized values or value domains needed for checking the annotation. An explicit execute_selection() or materialization call is not required in this context.

For a named Selection followed by a member property, materialize the Selection's result and obtain that property from each selected member. Thus Selection//All Scope Unit.Name supplies the selected Scope Unit names, not the Selection entity's own Name. The membership condition uses those resulting strings. A lower-bound condition >=1 requires the direct numeric value to be at least one.

This value context does not change the independent cardinality suffix, count nested keys, make @ itself a materialization operator, or redefine ordinary Model-property paths outside the annotation.

### Formal claim

```text
atom.version_number[int, >=1]
atom.scope_owner[string, in Selection//All Scope Unit.Name]
```

## Semantics

Named selections define their result population. The format-and-condition annotation makes clear that the population's values are being used rather than its graph identity. Materialization here describes obtaining values for the check; it does not prescribe persistence or create new model entities.

## Details

A1291 records the Operator decision. The owner expression is an illustrative logical property path, not a YAML field rename or an automatically registered Selection. This prepared Definition does not implement a parser or evaluator or promote general formula/function syntax.
