---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  depends_on:
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Entity
version: 19
updated_at: 2026-10-23 22:33:09 +0400
relations: {}
atom_id: CA-R-1339@19
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
status: Archived
author: Anatoly Maslennikov
global_tier: 9
---
# Summary

Define Requirement Content Role

## Scope

the Requirement Content Role.

## Claim

Requirement **means** the Content Role of an Atom Claim that specifies a required outcome or runtime behavior, or defines the governed model and its constraints.

## Details

- Functional requirements specify required business/domain behavior.
- Non-functional requirements specify required runtime qualities, including speed, performance, delivery guarantees and error-rate limits.
- Model definitions and Graph Rules specify the methodology's own governed model and constraints; they remain Requirements.
- Subject and Content Role are independent. A Requirement can govern a Domain, Engineering or global Graph Subject.
- Architecture and coding choices describe how to achieve a result and belong to Method, even when mandatory.
- an obligation, permission, **or** prohibition does **not** by itself select this Content Role; classification follows the Claim's primary contribution.
