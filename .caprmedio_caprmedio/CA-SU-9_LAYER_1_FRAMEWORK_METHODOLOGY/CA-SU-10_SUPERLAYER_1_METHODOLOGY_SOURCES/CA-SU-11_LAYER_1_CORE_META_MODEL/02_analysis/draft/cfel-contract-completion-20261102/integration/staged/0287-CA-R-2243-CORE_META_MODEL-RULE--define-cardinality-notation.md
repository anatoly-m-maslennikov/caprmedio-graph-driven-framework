---
atom_id: CA-R-2243
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Cardinality
  passive:
  - CFEL
version: 7
relations: {}
tier: 1
role: Requirement
form: Rule
updated_at: 2026-11-02 08:06:47 +0400
---

## Summary

Define Cardinality Notation

## Claim

Cardinality annotations state allowed counts; they do not count a value merely
because a dependent Property exists. `{:n}` allows exactly n, `{:n+}` at
least n, and `{:n..m}` the inclusive range for its qualified selection. Bounds
are non-negative integers with n not greater than m. `{=n}` is a count
condition/test and `{==n}` a required or derived count conclusion, not either
form of allowed bound. A direct parent-value count excludes nested child keys and
every descendant value, including every value held by nested children.

Property occurrence, value and dependent-name counts are separate:

```CFEL
p{:occurrence}: [value format]{:value count};
p.*[immediate name format]{:immediate name count};
p.**[recursive name format]{:recursive name count};
p.*[name format]{:name count}: [value format]{:value count}
```

`p{:0}` forbids authored occurrences of p; it does not forbid independently
declared children. `p.*[]{:0}` states that p has no declared immediate
dependents after local and inherited declaration resolution. The value count
to the right of `[value format]` is per selected existing Property occurrence;
the name count is the number of selected dependent Property names. A recursive
name count aggregates selected distinct descendant Property identities under p
within each selected bearer; it does not count direct values or another
bearer's descendants.

`Source {:forward}((RELATION)){:reverse} Target` has independent directional
counts. The first constrains outgoing Relation instances per selected Source;
the second constrains reverse links per selected Target. Reversing the written
Relation swaps the slots. Neither count is a Property value count, a distinct
target count, or Relation arity. An omitted annotation is unspecified.

## Details

This candidate aligns CA-R-2243 with active CFEL Rules CA-R-2471 and
CA-R-2472. It intentionally does not describe a parser, evaluator, implicit
default, or Relation Declaration endpoint signature. Its source SHA-256 is
`5cb106cf38d43db322b1a036c0d6140d8991ee647bc4b1905147d8db3072d4de`.
