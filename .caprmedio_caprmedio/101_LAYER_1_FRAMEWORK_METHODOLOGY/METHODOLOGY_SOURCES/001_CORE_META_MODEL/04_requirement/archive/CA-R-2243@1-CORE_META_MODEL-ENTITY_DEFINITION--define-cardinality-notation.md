---
atom_id: CA-R-2243@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Syntax > Cardinality
  depends_on:
  - Entity/Graph Syntax
version: 1
relations: {}
tier: 1
updated_at: 2026-10-29 07:32:39 +0400
---
## Summary

Define Cardinality Notation

## Claim

Cardinality annotations count an addressed property's direct values. Nested
keys and their values do not contribute to the parent's count. `{n}` requires
exactly n, `{n+}` at least n with no upper bound, and `{n..m}` the inclusive
range n through m. Bounds are non-negative integers and n is not greater than
m.

`{0}` forbids direct values without forbidding declared child properties;
`subjects{0}` therefore permits its independently counted governs and
dependency children. In `Whole >{n+} Part`, the suffix counts immediate Parts
per Whole. It does not change the separate exactly-one-immediate-whole rule.
An omitted annotation leaves cardinality undefined.

### Formal claim

```text
Atom/Content Role: Operations/Type: Workflow >{1+} Atom/Content Role: Operations/Type: Step >{0+} Atom/Content Role: Operations/Type: Sub-step
atom.version_number[int]{1}
atom.content.claim[string]{1}
atom.content.claim.formal_claim[string]{0..1}
subjects{0}
subjects.governs[string]{1}
subjects.depends_on[string]{0+}
```

## Semantics

Counts apply independently to direct values and never to nested keys. A YAML
sequence carries multiple values under one unique property key; it is not a
list value Format. A formal Claim child does not satisfy the required prose
Claim.

## Details

YAML null and an empty string are direct values when YAML interprets them as
such; omission is zero values. Their admissibility follows the declared value
Format and prose conditions. General formulas and functions remain separate.
