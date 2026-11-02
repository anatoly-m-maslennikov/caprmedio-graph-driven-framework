---
atom_id: CA-R-2472@2
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
subjects:
  active: CFEL
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

Separate Property names and values

## Claim

- `p{:n}` constrains occurrences of the named Property.
- `p: [format]{:n}` constrains its allowed values.
- `p.*[format]{:n}` constrains immediate dependent names.
- `p.**[format]{:n}` constrains dependent names recursively.
- `p.*[name format]{:n}: [value format]{:m}` also constrains each selected Property's values.
- The left count is the number of selected Property names.
- The right count is the number of values per existing Property.
- Separate expressions use `;`.

Names are unique within one bearer. `x.y.z` differs from `x.z`.

Resolve local declarations first. Resolve inherited declarations next. If neither declares dependents, state `p.*[]{:0}`. Missing annotations remain undefined.

## Details

```CFEL
asdf: [string]{:1};
asdf.*[in (aaa, bbb)]{:1};
asdf.aaa{:0..1}: [atom id]{:1};
asdf.bbb{:0..1}: [scope unit]{:1}
```

```CFEL
Atom.Content.**[string]{:0+}: [markdown]{:1}
```
