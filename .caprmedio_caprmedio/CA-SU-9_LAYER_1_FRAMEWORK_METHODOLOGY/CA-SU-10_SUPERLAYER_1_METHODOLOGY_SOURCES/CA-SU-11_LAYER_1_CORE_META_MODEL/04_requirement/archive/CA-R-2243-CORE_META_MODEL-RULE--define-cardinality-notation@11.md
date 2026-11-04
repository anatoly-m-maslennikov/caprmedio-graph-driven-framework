---
atom_id: CA-R-2243
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Cardinality
  passive:
  - CAPRMEDIO_MODEL <+ CFEL
version: 11
relations: {}
tier: 1
role: Requirement
form: Rule
updated_at: 2026-11-02 17:54:42 +0400
---

## Summary

Define Cardinality Notation

## Claim

### Formal Claim

```CFEL
# model
p{:occurrence}: [value format]{:value count};

p.*[immediate name format]{:immediate name count};

p.**[recursive name format]{:recursive name count};

p.*[name format]{:name count}: [value format]{:value count}
```

### Prose Claim


Cardinality annotations state allowed counts; they do not count a value merely
because a dependent Property exists. `{:n}` allows exactly n, `{:n+}` at
least n, and `{:n..m}` the inclusive range for its qualified selection. Bounds
are non-negative integers with n not greater than m. `{=n}` is a count
condition/test, `{>n}` is a count condition/test that compares the actual count
with n using the existing numeric `>`, and `{==n}` a required or derived count
conclusion; none is an allowed bound. A direct parent-value count excludes
nested child keys and every descendant value, including every value held by
nested children.

Property occurrence, value and dependent-name counts are separate:


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

