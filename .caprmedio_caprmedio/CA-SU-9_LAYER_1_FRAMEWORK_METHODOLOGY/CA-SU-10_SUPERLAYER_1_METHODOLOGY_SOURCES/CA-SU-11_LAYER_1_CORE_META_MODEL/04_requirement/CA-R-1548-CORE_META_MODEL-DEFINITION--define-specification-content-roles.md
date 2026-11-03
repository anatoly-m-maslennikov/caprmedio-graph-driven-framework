---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Method)
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Delivery)
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Package/Project Implementation
  - CAPRMEDIO_MODEL <+ Carrier
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
