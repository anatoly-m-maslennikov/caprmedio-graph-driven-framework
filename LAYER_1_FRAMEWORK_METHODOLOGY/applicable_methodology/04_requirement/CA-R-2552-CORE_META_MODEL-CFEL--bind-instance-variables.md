---
atom_id: CA-R-2552
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2552-CORE_META_MODEL-CFEL--bind-instance-variables.md
  source_atom_id: CA-R-2552
  source_atom_revision: 2
  source_sha256: 8fe35e468fcd60793bad1887ad9b5e600c57e1a59958206961a18499218c6c4a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Bind instance variables

## Claim

- `Kind//` selects existing instances of Kind and its narrower kinds.
- `Kind//{:n}` applies the existing cardinality to the selected logical instances within the Project context. Resolve the complete selection and count each instance once across repeated references or Carrier representations. An unresolved population is an error.
- `Kind//$x` ranges over the selected instances. Each constraint must hold for every matching binding. Repeated `$x` references in one Claim block identify the same instance within each binding.
- `in` and `not in` test an instance's identity against a selected instance set. `=` and `!=` compare bound instance references by identity; they do not test kind membership or broadcast a scalar comparison over a set.
- `Kind//$x.p` selects and binds an instance and reads its Property `p`. `$x.p` reads that same bound instance's Property.
- In an IF condition, `Kind//$c ((R)) Kind//$p` tests a link that already exists, including a legitimately derived inverse. It is not an endpoint signature and does not create a link.
- Evaluate the condition for candidate bindings. Its THEN conclusion applies only to bindings for which that link exists; it does not require links between every candidate pair.
- Endpoint counts aggregate matching links per endpoint; they do not require a link between every pair of bindings.
- Binding selects existing instances. It does not create an instance named `$x` or assign a value imperatively. `@` continues to reference an existing target.

## Details

```CFEL
Kind//$x
```

This binds one existing selected instance.
