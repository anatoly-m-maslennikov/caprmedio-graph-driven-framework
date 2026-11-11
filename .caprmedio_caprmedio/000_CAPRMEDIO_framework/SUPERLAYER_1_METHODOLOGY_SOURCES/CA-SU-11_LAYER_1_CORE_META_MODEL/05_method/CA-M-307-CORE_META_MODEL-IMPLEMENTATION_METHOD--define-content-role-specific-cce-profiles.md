---
atom_id: CA-M-307
ref_id: CA-M-307
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Role
  dependencies:
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Controlled English"
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Atom.Header.Form
tier: 5
relations:
  child_of:
  - CA-M-113
  - CA-M-230
  - CA-M-234
status: Active
version: 31
updated_at: "2026-11-07 17:10:31 +0400"
carrier_destination:
  file:
    name: CA-M-307-CORE_META_MODEL-IMPLEMENTATION_METHOD--define-content-role-specific-cce-profiles.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Define Content-role-specific CCE Profiles

## Claim

### Prose Claim

A CCE Role Profile restricts shared CCE for one Role, narrower Form or content slot. It specifies:

- permitted primary Claim contributions;
- permitted CCE Operator uses;
- permitted subordinate content slots;
- excluded primary contributions.

The registered Role profiles apply to Plan, Requirement, Method, Evaluation, Delivery and Operations. Concern, Analysis & Advisory and Implementation use shared CCE unless an applicable profile is separately registered.

An absent profile leaves the Role’s meaning and authority unchanged. A narrower profile preserves its parent Role’s primary contribution. It can restrict that profile and define subordinate Operator use.
