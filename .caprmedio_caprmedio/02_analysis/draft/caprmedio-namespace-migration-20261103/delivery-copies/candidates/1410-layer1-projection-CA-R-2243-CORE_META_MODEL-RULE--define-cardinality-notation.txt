---
atom_id: CA-R-2243
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Cardinality
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL
version: 11
relations: {}
tier: 1
role: Requirement
form: Rule
updated_at: 2026-11-02 17:54:42 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2243-CORE_META_MODEL-RULE--define-cardinality-notation.md
  source_atom_id: CA-R-2243
  source_atom_revision: 11
  source_sha256: b7a322529911e357cd1c148f11d4c75c934f4294db7d4adedb7d870df751fbc5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Define Cardinality Notation

## Claim

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

