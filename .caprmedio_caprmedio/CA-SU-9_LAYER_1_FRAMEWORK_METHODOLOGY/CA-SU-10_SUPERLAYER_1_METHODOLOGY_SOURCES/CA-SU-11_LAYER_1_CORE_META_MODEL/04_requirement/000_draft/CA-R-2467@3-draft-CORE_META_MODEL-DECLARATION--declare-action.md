---
atom_id: CA-R-2467
ref_id: CA-R-2467@3-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Action
tier: 3
status: Draft
version: 3
updated_at: 2026-11-05 02:11:07 +0400
carrier_destination:
  file:
    name: CA-R-2467@3-draft-CORE_META_MODEL-DECLARATION--declare-action.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---

## Summary

Declare Action

## Claim

### Formal Claim

```python
# model
subject_path(address='Atom/(.Header.Context.Role in (Operations))/Action')
relation(source='Action', name='NARROWER_THAN', target='Atom/(.Header.Context.Role in (Operations))')
# instances
relation(source='Action//$action', name='IS_RUN_BY', target='Step//$step', source_count='0+')
relation(source='Action//$definition', name='HAS_EXECUTION', target='Action Run//$run', source_count='0+')
```

## Semantics

An Action is a reusable operational building block. Its boundary reflects one modeled responsibility.
