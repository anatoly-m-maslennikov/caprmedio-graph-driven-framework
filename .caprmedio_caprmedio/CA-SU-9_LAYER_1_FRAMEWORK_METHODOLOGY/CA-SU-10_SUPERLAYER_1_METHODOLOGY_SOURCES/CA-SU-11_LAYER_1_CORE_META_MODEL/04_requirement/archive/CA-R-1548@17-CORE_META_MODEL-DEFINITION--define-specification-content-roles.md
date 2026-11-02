---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Selection
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Method'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Delivery'
  - Subject/Graph Node/Domain/Continuant/Atom/Content Role
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Engineering/Continuant/Carrier
version: 17
updated_at: 2026-10-25 17:32:27 +0400
relations:
  relates_to:
  - CA-R-1339
  - CA-R-1340
  - CA-R-1341
  - CA-R-1342
atom_id: CA-R-1548@17
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
