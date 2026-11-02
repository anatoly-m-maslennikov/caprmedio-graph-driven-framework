---
atom_id: CA-R-2243@5
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
subjects:
  active: CFEL <+ Cardinality
  passive:
  - CFEL
version: 5
relations: {}
tier: 1
updated_at: 2026-11-02 00:55:09 +0400
role: Requirement
form: Entity Definition
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
dependency children. A Relation uses two independent directional slots:
`Source {forward-count}RELATION{reverse-count} Target`. In
`Step {1}+>{1+} Workflow`, the pre-operator count requires one Workflow per
Step and the post-operator count requires one or more Steps per Workflow. The
equivalent reverse writing is `Workflow {1+}<+{1} Step`. Neither spelling
changes the separate exactly-one-immediate-whole rule.
In `Source {forward-count}((RELATION_TOKEN)){reverse-count} Target`, the
pre-operator slot counts outgoing Relation instances of that Type per source
occurrence and the post-operator slot counts reverse links per target
occurrence. Each actual Relation connects two nodes or node instances, its
source and target; neither slot counts Relation arity or the two endpoints
inside a Relation. `Property {1}((IS_PROPERTY_OF)) Bearer` constrains exactly
one outgoing IS_PROPERTY_OF Relation per Property occurrence; it does not set
the Property's value count. A postfix-only count would constrain the reverse
count per Bearer instead.
The endpoints in these schematics stand for actual full admitted Entity
expressions, not a new Relation between kind nodes. An omitted annotation
leaves cardinality undefined.

### Formal claim

```text
Atom/(.Content Role: Operations)/(.Type: Step) {1}+>{1+} Atom/(.Content Role: Operations)/(.Type: Workflow)
Atom/(.Content Role: Operations)/(.Type: Sub-step) {1}+>{0+} Atom/(.Content Role: Operations)/(.Type: Step)
atom.version_number[int]{1}
Atom/(.Content Role: Requirement).Content.Claim[string]{1}
Atom.Subjects{0}
Atom.Subjects.Governs[string]{1}
Atom.Subjects.Depends On[string]{0+}
```

## Semantics

The lowercase `atom.version_number` example illustrates logical Carrier access under CA-D-478; it is not a canonical Subject-path declaration.

The same cardinality notation applies to different explicitly identified counts. `[format]` specifies a Property's direct-value Format, while a post-Property `{cardinality}` counts those direct values. A Relation's pre-operator and post-operator slots count its independent forward and reverse directions. These dimensions remain independent.

Counts apply independently to direct values and never to nested keys. A YAML
sequence carries multiple values under one unique property key; it is not a
list value Format. A CFEL expression in the Claim is part of its direct value; a separate Formal Claim child is not required.

## Details

YAML null and an empty string are direct values when YAML interprets them as
such; omission is zero values. Their admissibility follows the declared value
Format and prose conditions. General formulas and functions remain separate.

This N+1 Draft extends Current CA-R-2243@2 (SHA-256 `e5da9f652f641d011bc52c9c10afab6a4985577a694fec48d8a95fad3b2dba81`) with the Operator-selected two-sided Relation cardinality, superseding the earlier postfix-only outgoing convention. No Current source or parser is changed.
