---
atom_id: CA-R-2243
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Syntax > Cardinality
  depends_on:
  - Entity/Graph Syntax
version: 2
relations: {}
tier: 1
updated_at: 2026-10-29 09:50:47 +0400
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
`Atom.Subjects{0}` therefore permits its independently counted governs and
dependency children. In `Whole >{n+} Part`, the suffix counts immediate Parts
per Whole. It does not change the separate exactly-one-immediate-whole rule.
An omitted annotation leaves cardinality undefined.

### Formal claim

```text
Atom/Content Role: Operations/Type: Workflow >{1+} Atom/Content Role: Operations/Type: Step >{0+} Atom/Content Role: Operations/Type: Sub-step
atom.version_number[int]{1}
Atom/Content Role: Requirement.Content.Claim[string]{1}
Atom/Content Role: Requirement.Content.Claim.Formal Claim[string]{0..1}
Atom.Subjects{0}
Atom.Subjects.Governs[string]{1}
Atom.Subjects.Depends On[string]{0+}
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
