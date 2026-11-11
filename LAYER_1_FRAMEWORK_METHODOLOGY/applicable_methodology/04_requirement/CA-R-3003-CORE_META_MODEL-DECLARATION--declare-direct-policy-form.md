---
atom_id: CA-R-3003
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Direct Policy)
tier: 3
ref_id: CA-R-3003
status: Active
version: 2
updated_at: "2026-11-07 15:18:44 +0400"
carrier_destination:
  file:
    name: CA-R-3003-CORE_META_MODEL-DECLARATION--declare-direct-policy-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-3003-CORE_META_MODEL-DECLARATION--declare-direct-policy-form.md
  source_atom_id: CA-R-3003
  source_atom_revision: 2
  source_sha256: c0a574d3f7c738740e8aee9b33b1900c349c02c8c3bcb47ea8229727b837f255
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Direct Policy Form

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Form := Direct Policy);

# instances
Atom/(.Header.Form := Direct Policy)//$direct_policy.Header.Role:: [in (Requirement, Method, Evaluation, Delivery, Operations)]{::1}
```

## Semantics

A Direct Policy applies to all descendants recursively without a local copy. A genuine SPECIALIZES Atom may add applicable detail while preserving parent constraints.
