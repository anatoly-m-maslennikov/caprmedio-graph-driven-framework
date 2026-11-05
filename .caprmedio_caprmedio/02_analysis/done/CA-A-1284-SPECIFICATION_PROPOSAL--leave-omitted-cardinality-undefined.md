---
atom_id: CA-A-1284
ref_id: CA-A-1284
role: Analysis & Advisory
form: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
topics:
  main_subject: Model::CAPRMEDIO::Graph Syntax.Cardinality Notation
version: 3
updated_at: 2026-11-02 15:49:28 +0400
tier: 3
container:
  scope_unit: CA-SU-00
---
# Summary

Leave omitted cardinality undefined

## Decision

A property without a cardinality suffix has undefined cardinality. Omission does not mean zero, one, optional or unlimited. For example:

```text
subjects       — undefined direct-value cardinality
subjects{0}    — exactly zero direct values
subjects{1}    — exactly one direct value
subjects{0+}   — zero or more direct values
```

Declared child properties retain their independent counts. The explicit subjects{0} grouping contract in CA-A-1283 remains unchanged.

## State

The Cardinality Notation Definition Draft and main Model proposal state this distinction. Current sources and runtime are unchanged.
