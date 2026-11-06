---
atom_id: CA-R-2585
ref_id: CA-R-2585
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2585-CORE_META_MODEL-RULE--count-direct-property-values-and-distinct-values.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2585-CORE_META_MODEL-CFEL--count-property-values-and-distinct-values.md
  source_atom_id: CA-R-2585
  source_atom_revision: 2
  source_sha256: fb8a43bcd01bfaa9d40cd3e5b4635936df6e23342e07e3e19636b5de54e52b34
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Count direct Property values and distinct values

## Claim

### Prose Claim


- Within `COUNT(...)`, `p: $` selects the direct value occurrences of Property p on the current bearer. `$` is anonymous and binds no new named variable. It does not select dependent Property names.
- Repeated equal values remain separate occurrences. A known absent optional p selects an empty selection of value occurrences. An unresolved or malformed bearer, Property population, or value is an error, not an empty set.
- `COUNT(p: $)` returns the nonnegative number of selected direct value occurrences. `COUNT(DISTINCT p: $)` returns the number of their unique values.
- DISTINCT equality is the declared Format equality: no implicit string trimming, case folding, coercion, or canonicalization. A reference Format compares resolved reference identity.
- Counts apply per current bearer, not across Atoms. Existing Property occurrence, value-format, value-count, and source constraints remain in force.
- Outside this COUNT selection, existing `p: literal` and `p: [format]{:n}` meanings are unchanged.

## Details

```CFEL
# instances
Atom//$atom;

COUNT($atom.Header.Subjects.Passive: $) = COUNT(DISTINCT $atom.Header.Subjects.Passive: $)
```
