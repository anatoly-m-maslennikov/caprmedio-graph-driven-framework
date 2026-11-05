---
atom_id: CA-R-2612
ref_id: CA-R-2612
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL<+Operator//RecursiveWildcard
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-2612-CORE_META_MODEL-DECLARATION--declare-cfel-operator.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2612-CORE_META_MODEL-DECLARATION--declare-cfel-operator.md
  source_atom_id: CA-R-2612
  source_atom_revision: 1
  source_sha256: af4c2bbe262db26f87b074a1a7a469fd455360edc15f80dd40d1b8c1083192be
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare CFEL operator **

## Claim

### Formal Claim

```CFEL
# model
Operator//RecursiveWildcard == "**"
```

## Semantics

Select distinct dependent Property identities recursively below p in one bearer.
A `p.**` count aggregates that selection across all descendant depths; it does
not count values or another bearer's selection.
