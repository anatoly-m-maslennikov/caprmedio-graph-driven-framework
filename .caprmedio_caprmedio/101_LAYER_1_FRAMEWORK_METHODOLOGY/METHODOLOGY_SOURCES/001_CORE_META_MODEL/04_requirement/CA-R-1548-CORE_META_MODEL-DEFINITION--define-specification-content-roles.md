---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  - Subject/CAPRMEDIO/Carrier
version: 20
updated_at: 2026-10-27 19:59:57 +0400
relations: {}
atom_id: CA-R-1548
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define Specification Content Roles

## Scope

Specification Content Roles (Spec, RMED).

## Claim

Specification Content Roles (Spec, RMED) **means** the set (Requirement, Method, Evaluation, Delivery) that specifies governed content **and** Entities, including CAPO **and** I.

## Details

- Requirement establishes required outcomes and runtime behavior, including functional and non-functional requirements, and the methodology's own model definitions and constraints.
- Method establishes how those outcomes are achieved, including architecture, coding policies, engineering decisions, construction and authorship conventions.
- Evaluation establishes correctness checks.
- Delivery establishes Carrier contents, representation, **and** placement.

The methodology's own model and specification content are also within this specification domain; RMED is not limited to native Implementation. Subject and Content Role are independent: any RMED Role can govern a Domain, Engineering or global Graph Subject.
