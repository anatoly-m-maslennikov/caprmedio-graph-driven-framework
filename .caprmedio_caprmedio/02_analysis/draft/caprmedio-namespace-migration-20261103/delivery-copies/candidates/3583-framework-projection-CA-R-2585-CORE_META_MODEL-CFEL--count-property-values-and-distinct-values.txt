---
atom_id: CA-R-2585
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2585-CORE_META_MODEL-CFEL--count-property-values-and-distinct-values.md
  source_atom_id: CA-R-2585
  source_atom_revision: 2
  source_sha256: e7e8d0d9a7b41c432428cbd0af84290da3a32b4bd98218ccf49298e9fc400837
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Count direct Property values and distinct values

## Claim

- Within `COUNT(...)`, `p: $` selects the direct value occurrences of Property p on the current bearer. `$` is anonymous and binds no new named variable. It does not select dependent Property names.
- Repeated equal values remain separate occurrences. A known absent optional p selects an empty selection of value occurrences. An unresolved or malformed bearer, Property population, or value is an error, not an empty set.
- `COUNT(p: $)` returns the nonnegative number of selected direct value occurrences. `COUNT(DISTINCT p: $)` returns the number of their unique values.
- DISTINCT equality is the declared Format equality: no implicit string trimming, case folding, coercion, or canonicalization. A reference Format compares resolved reference identity.
- Counts apply per current bearer, not across Atoms. Existing Property occurrence, value-format, value-count, and source constraints remain in force.
- Outside this COUNT selection, existing `p: literal` and `p: [format]{:n}` meanings are unchanged.

## Details

```CFEL
COUNT(Atom.Subjects.Passive: $) = COUNT(DISTINCT Atom.Subjects.Passive: $)
```
