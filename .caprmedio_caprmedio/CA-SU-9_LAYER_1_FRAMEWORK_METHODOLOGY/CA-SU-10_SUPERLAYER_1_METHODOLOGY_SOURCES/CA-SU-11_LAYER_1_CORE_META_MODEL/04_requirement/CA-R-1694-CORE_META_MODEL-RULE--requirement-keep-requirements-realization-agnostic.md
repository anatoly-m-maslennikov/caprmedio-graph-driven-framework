---
atom_id: CA-R-1694
ref_id: CA-R-1694
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Role
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Method)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Delivery)
  - CAPRMEDIO_MODEL <+ Package/Project Package
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)
tier: 1
status: Active
version: 42
updated_at: 2026-11-10 14:38:45 +0400
carrier_destination:
  file:
    name: CA-R-1694-CORE_META_MODEL-RULE--requirement-keep-requirements-realization-agnostic.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Requirement — Keep Requirements realization-agnostic

## Claim

### Prose Claim


Requirement claims and their internal realization.


**every** Requirement **must** state its required outcome, obligation, permission, prohibition, **or** accepted external boundary **without** prescribing internal code **or** code organization merely as a construction choice.

- an accepted external interface, protocol, data shape, **or** host obligation **may** be required **when** conformance **to** that boundary is itself the required outcome. this does **not** prescribe an **otherwise** interchangeable internal realization.
- a programming language, library, algorithm, function, class, module, source-file organization, **or** another construction technique does **not** become a Requirement solely because it is normative; classify its primary contribution under CA-R-1531@20 **and** CA-R-2513.
- packaging, release, deployment, distribution, installation, migration, upgrade, **and** rollback are topics, **not** Content Role selectors. classify a Carrier representation **or** placement under CA-R-2515, reusable Action **or** Workflow behavior under CA-R-2463, **and** treat an actual realization as native Implementation rather than an Atom Content Role. mentioning one of those topics does **not** turn a procedure into Delivery authority.
- a candidate that combines this independently replaceable outcome with an independently replaceable construction, Carrier, **or** operational Claim requires separate Atoms under the one-Claim authority; a composite Claim is **not** split merely because it has multiple clauses.

## Details

Functional and non-functional Requirements both specify outcomes. A performance target can have an Engineering Subject. Subject and Content Role are independent; architecture remains Method even when mandatory. The methodology's own model definitions and Entity Definition constraints remain within Requirement authority.

CA-R-2512 owns the Requirement Content Role definition. this Atom constrains realization prescription **without** duplicating the definitions of the other Content Roles.
