---
atom_id: CA-A-1280
ref_id: CA-A-1280
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Model::CAPRMEDIO::Graph Syntax.Cardinality Notation
tier: 3
status: Done
version: 3
updated_at: 2026-11-02 15:49:28 +0400
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Use compact cardinality notation

## Decision

Cardinality annotations count occurrences. `{n}` requires exactly n, `{n+}` requires at least n with no upper bound, and `{n..m}` permits the inclusive range from n to m. Bounds are non-negative integers and a bounded range requires n <= m.

A suffix on a property constrains that property's values for one bearer. In `X >{n+} Y`, it counts immediate Y parts per X whole. It does not change the separately established rule that each contained part has exactly one immediate whole. An omitted annotation leaves cardinality unspecified; it does not imply optionality or an unlimited count.

| Notation | Meaning | Example |
| --- | --- | --- |
| `{n}` | Exactly n | `{1}`: exactly one |
| `{n+}` | At least n, no upper bound | `{2+}`: two or more |
| `{n..m}` | From n to m, inclusive | `{2..5}`: two through five |
| `{0}` | None | A forbidden part or property |
| `{0+}` | Zero or more | Optional collection of any size |
| `{1+}` | One or more | At least one part or value |
| `{0..1}` | Zero or one | An optional single value |
| `{0..m}` | At most m | `{0..3}`: zero through three |

Use the compact forms in the prepared model:

```text
Workflow >{1+} Step >{0+} Substep
Substep >{0} @(Substep)
```

The latest compact spelling replaces the earlier >= and open-range spellings in this prepared packet. Historical proposals remain unchanged; no parser aliases or runtime implementation are introduced.

## State

A Cardinality Notation Definition Draft and the affected notation, authoring, evaluation, delivery and container Drafts are prepared. Current methodology and Engine behavior remain unchanged.
