---
atom_id: CA-R-2472
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---

## Summary

Separate Property names and values

## Claim

- `p{:occurrence}` constrains occurrences of the named Property.
- `p{:occurrence}: [value format]{:value count}` constrains its direct values.
- `p.*[name format]{:child count}` constrains immediate dependent names.
- `p.**[name format]{:recursive count}` constrains recursive dependent names
  across every descendant depth.
- `p.*[name format]{:child count}: [value format]{:value count}` also
  constrains each selected immediate dependent Property's direct values.
- The name count and value count are different counts. Separate complete
  expressions use `;`.

Names are unique within one bearer. `x.y.z` differs from `x.z`. Resolve local
declarations first and inherited declarations next. If neither declares
dependents for p, the effective immediate-child constraint is `p.*[]{:0}`:
undeclared dependent entities are forbidden. An explicit applicable child-name
selector, including an explicit wildcard selector, is the stated exception;
it permits only the names and counts that it declares.

Missing occurrence, direct-value, Format, and non-default count annotations
remain unspecified. For `p.**`, the recursive count aggregates the selected
distinct descendant Property identities below p within each selected bearer.
It counts each selected descendant once regardless of depth; it neither counts
direct values nor combines descendants from different bearers. Sibling names
remain unique within that bearer.

## Details

```CFEL
Atom.Content.**[string]{:0+}: [markdown]{:1}
```

This candidate preserves the active Rule's separation of values from names and
makes the approved undeclared-child default explicit. Its source SHA-256 is
`ac46573baa3df390f285bcdece3f84f4abb65eca4ec5580b4cbabe1debe556b1`.
