---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)
version: 35
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-M-447
atom_id: CA-R-1767
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1767-CORE_META_MODEL--distinguish-implementation-methods-from-implementation-decisions.md
  source_atom_id: CA-R-1767
  source_atom_revision: 35
  source_sha256: d0e2bbf50312b707627a49652e690252bf6280907141b73dcf102e30306a2c8e
  original_relations_sha256: cda81380ab057c4da428dab72b93f65bb72092983ee69756870fff6e5dc9bea9
---
## Summary

Distinguish Implementation Methods from Implementation Decisions

## Claim

### Prose Claim


Method Eng Policy/Eng Decision and Delivery Policy/Decision Types.


A Method Eng Policy governs reusable engineering policy and an Eng Decision selects a bounded engineering approach. A Delivery Policy governs a reusable representation or delivery family, while a Delivery Decision selects a bounded representation or delivery choice. **neither** Eng Policy **nor** Eng Decision is an execution Plan **or** native Implementation.

## Details

These names replace the legacy Implementation Method and Implementation Decision labels for this distinction. Eng Policy ownership requires an actual declared child and automatic application to every child under genuine topic or environment conditions; Eng Decision does not automatically inherit to every child. A named technology alone does not select either Type. This distinction does not impose a Type-to-Tier restriction; the applicable Method definitions are CA-R-2119@8 and CA-R-2120@8; Delivery uses CA-R-2267@2 and CA-R-2268@1. The Method actual-child rule is not an extra prerequisite on the Core representation-policy family.
