---
atom_id: CA-R-2612
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL<+Operator//RecursiveWildcard
version: 1
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2612-CORE_META_MODEL-DECLARATION--declare-cfel-operator.md
  source_atom_id: CA-R-2612
  source_atom_revision: 1
  source_sha256: 0567adc90377d2a5f3fa560a8da2d1fea6ce1d1c5920310816d8bcbea60c9104
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare CFEL operator **

## Claim

```CFEL
@Operator//RecursiveWildcard == "**"
```

## Semantics

Select distinct dependent Property identities recursively below p in one bearer.
A `p.**` count aggregates that selection across all descendant depths; it does
not count values or another bearer's selection.
