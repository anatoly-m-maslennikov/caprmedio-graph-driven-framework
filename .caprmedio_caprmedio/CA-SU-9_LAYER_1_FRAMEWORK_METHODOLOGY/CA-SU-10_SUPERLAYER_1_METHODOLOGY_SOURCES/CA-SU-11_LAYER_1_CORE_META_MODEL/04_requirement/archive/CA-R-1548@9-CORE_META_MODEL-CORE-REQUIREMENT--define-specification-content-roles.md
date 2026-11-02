---
subjects:
  governs: Spec Content Roles
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - Change Content Roles
  - Implementation
  - Entity
version: 9
updated_at: 2026-10-23 22:33:09 +0400
relations:
  relates_to:
  - CA-R-1339
  - CA-R-1340
  - CA-R-1341
  - CA-R-1342
atom_id: CA-R-1548@9
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
status: Archived
author: Anatoly Maslennikov
global_tier: 9
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
