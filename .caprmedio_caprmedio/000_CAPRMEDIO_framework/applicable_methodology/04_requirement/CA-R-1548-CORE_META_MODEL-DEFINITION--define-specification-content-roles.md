---
subjects:
  active: Entity/Object/Continuant/Selection
  passive:
  - Atom/(.Role := Requirement)
  - Atom/(.Role := Method)
  - Atom/(.Role := Evaluation)
  - Atom/(.Role := Delivery)
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - Entity/Object/Continuant/Package/Project Implementation
  - Carrier
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1548
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1548-CORE_META_MODEL-DEFINITION--define-specification-content-roles.md
  source_atom_id: CA-R-1548
  source_atom_revision: 24
  source_sha256: 88cf9876901a33127c85534581693af34b35f023dd5b2da91b3268ab81af96b1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Specification Content Roles

## Claim scope

Specification Content Roles (Spec, RMED).

## Claim

Specification Content Roles (Spec, RMED) **means** the set (Requirement, Method, Evaluation, Delivery) that specifies governed content **and** Entities, including CAPO **and** I.

## Details

- Requirement establishes required outcomes and runtime behavior, including functional and non-functional requirements, and the methodology's own model definitions and constraints.
- Method establishes how those outcomes are achieved, including architecture, coding policies, engineering decisions, construction and authorship conventions.
- Evaluation establishes correctness checks.
- Delivery establishes Carrier contents, representation, **and** placement.

The methodology's own model and specification content are also within this specification domain; RMED is not limited to native Implementation. Subject and Content Role are independent: any RMED Role can govern a Domain, Engineering or global Graph Subject.
