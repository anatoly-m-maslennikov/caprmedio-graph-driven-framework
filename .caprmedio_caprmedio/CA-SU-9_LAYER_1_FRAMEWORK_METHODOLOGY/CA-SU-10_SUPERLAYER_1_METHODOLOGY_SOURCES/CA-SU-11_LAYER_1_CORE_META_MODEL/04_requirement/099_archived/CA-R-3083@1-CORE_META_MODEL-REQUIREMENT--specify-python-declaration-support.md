---
identity:
  atom_id: CA-R-3083
  ref_id: CA-R-3083@1
context:
  role: requirement
  form: requirement
  tier: 3
  container:
    scope_unit: CA-SU-11
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom.Content.Claim.Formal Claim
state:
  version: 1
  status: archived
  updated_at: '2026-11-12T12:28:47.734063+00:00'
destination:
  file:
    name: CA-R-3083@1-CORE_META_MODEL-REQUIREMENT--specify-python-declaration-support.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---
## Summary

Specify Python declaration support

## Claim

### Prose Claim

- Use ordinary Python types, literals, comparisons, comprehensions, and standard-library functions in Claims.
- Use standard-library dataclasses for typed declaration records. Use an integer for an exact cardinality. Use `Cardinality(minimum=..., maximum=...)` for an inclusive range, with `None` for an unbounded maximum.
- Carry dependent Property names, traversal depth, and Relation endpoints as typed declaration data.
- Statically resolve declaration functions, class imports, Model addresses, and Relation names. Resolve callbacks separately from declaration loading. Use typed Engine data when evaluating reviewed callbacks.
- Declare singleton populations as exactly one instance within the Project. Apply this to the Project and its root Project Package.
- Preserve the full qualified Topic address and the one Main Subject per Atom.

- Apply dependent Property constraints to immediate children by default. An explicit recursive selector covers descendants at every depth and preserves the original declaring Atom.
- Resolve omitted Property occurrence constraints from the effective Model. Keep field presence, direct value cardinality, and dependent Property cardinality distinct.
- Preserve both a direct Markdown value and declared dependent Properties when a field has both. Bind only declared headings as Properties.
