---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - Subject/Engineering/Implementation
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations'
version: 30
updated_at: 2026-10-24 01:37:42 +0400
relations: {}
atom_id: CA-R-1694@30
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Requirement — Keep Requirements realization-agnostic

## Scope

Requirement claims and their internal realization.

## Claim

**every** Requirement **must** state its required outcome, obligation, permission, prohibition, **or** accepted external boundary **without** prescribing internal code **or** code organization merely as a construction choice.

- an accepted external interface, protocol, data shape, **or** host obligation **may** be required **when** conformance **to** that boundary is itself the required outcome. this does **not** prescribe an **otherwise** interchangeable internal realization.
- a programming language, library, algorithm, function, class, module, source-file organization, **or** another construction technique does **not** become a Requirement solely because it is normative; classify its primary contribution under CA-R-1531 **and** CA-R-1340.
- packaging, release, deployment, distribution, installation, migration, upgrade, **and** rollback are topics, **not** Content Role selectors. classify a Carrier representation **or** placement under CA-R-1342, reusable Action **or** Workflow behavior under CA-R-1530, **and** an actual realization under CA-R-1343. mentioning one of those topics does **not** turn a procedure into Delivery authority.
- a candidate that combines this independently replaceable outcome with an independently replaceable construction, Carrier, **or** operational Claim requires separate Atoms under the one-Claim authority; a composite Claim is **not** split merely because it has multiple clauses.

## Details

Functional and non-functional Requirements both specify outcomes. A performance target can have an Engineering Subject. Subject and Content Role are independent; architecture remains Method even when mandatory. The methodology's own model definitions and Graph Rules remain within Requirement authority.

CA-R-1339 owns the Requirement Content Role definition. this Atom constrains realization prescription **without** duplicating the definitions of the other Content Roles.
