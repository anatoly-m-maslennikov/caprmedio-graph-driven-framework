---
atom_id: CA-R-3005
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Decision)
tier: 3
ref_id: CA-R-3005
status: Active
version: 2
updated_at: "2026-11-07 15:18:44 +0400"
carrier_destination:
  file:
    name: CA-R-3005-CORE_META_MODEL-DECLARATION--declare-decision-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-3005-CORE_META_MODEL-DECLARATION--declare-decision-form.md
  source_atom_id: CA-R-3005
  source_atom_revision: 2
  source_sha256: 09589e43a945feb50797f1572e4d665805f52d1b2f70d1d58aaca9fbed54d348
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Decision Form

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Form := Decision);

# instances
Atom/(.Header.Form := Decision)//$decision.Header.Role:: [in (Method, Evaluation, Delivery, Operations)]{::1}
```

## Semantics

A Decision records a particular local choice. Applicable governing constraints continue to apply.
