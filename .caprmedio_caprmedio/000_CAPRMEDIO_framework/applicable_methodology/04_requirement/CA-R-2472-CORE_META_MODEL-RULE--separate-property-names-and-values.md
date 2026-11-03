---
atom_id: CA-R-2472
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL
version: 8
updated_at: 2026-11-02 14:59:48 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2472-CORE_META_MODEL-RULE--separate-property-names-and-values.md
  source_atom_id: CA-R-2472
  source_atom_revision: 8
  source_sha256: d2e8a10a845996b03cf94b351f05422758f541ea92bf32f0941c10ecb5ff93cf
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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

Property selectors compose from left to right:
- `p.*.*` selects Properties exactly two levels below p.
- `p.*.**` selects Properties two or more levels below p.

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

