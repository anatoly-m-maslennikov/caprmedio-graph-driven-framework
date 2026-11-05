---
atom_id: CA-R-2123
ref_id: CA-R-2123
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
tier: 1
status: Active
version: 9
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2123-PROJECT_CONFIGURATION-RULE--limit-programmatic-method-and-delivery-types.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
---
## Summary

Limit PROGRAMMATIC Method and Delivery Types

## Claim

### Prose Claim


Method and Delivery Atoms whose Local Scope Unit is PROGRAMMATIC or one of its declared descendants.


Each Current Method Atom in this Scope must use Eng Policy or Eng Decision. Each Current Delivery Atom uses Policy or Decision under the general Delivery Type definitions.

## Details

Subjects and Content Roles remain independent. This rule restricts admitted Type values, not Subject branches or Tier numbers. Other Content Roles and specialized Types outside this Scope are not restricted by this rule.

Method Eng Policy ownership requires at least one actual declared child and automatic application to every child under genuine topic or environment conditions. A leaf may inherit a Policy but cannot locally own one. Eng Decision records a Scope-Unit-specific choice without automatic every-child inheritance.

Incomplete Drafts remain allowed. Apply this Type restriction before promotion to Current. During this Candidate #7 migration, classification-only Type corrections retain the base ID when Summary and Substance are unchanged.

The reusable definitions are CA-R-2119@8 and CA-R-2120@8 for Method, and CA-R-2267@2 and CA-R-2268@1 for Delivery. This source rule does not claim that their existing consumers have been migrated or that runtime validation implements it.
