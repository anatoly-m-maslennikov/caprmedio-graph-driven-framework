---
atom_id: CA-R-2472
ref_id: CA-R-2472
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
version: 9
updated_at: 2026-11-04 05:21:15 +0400
tier: 3
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2472-CORE_META_MODEL-RULE--separate-property-names-and-values.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Separate Property names and values

## Claim

### Prose Claim


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

Each applicable named Property occurs at most once per corresponding bearer. A leaf with a positive applicable value minimum is required; a zero minimum by itself does not require presence. Explicit occurrence and other applicable constraints still apply. A present Property has a value; nonempty child structure can provide a structural parent value when direct-value count is zero. `p: {:0..1}` specifies direct-value count while using the applicable inherited format. Missing direct-value, Format, and other count annotations remain unspecified. For `p.**`, the recursive count aggregates the selected
distinct descendant Property identities below p within each selected bearer.
It counts each selected descendant once regardless of depth; it neither counts
direct values nor combines descendants from different bearers. Sibling names
remain unique within that bearer.

## Details

```CFEL
# model
Atom.Content.**[string]{:0+}: [markdown]{:1}
```

