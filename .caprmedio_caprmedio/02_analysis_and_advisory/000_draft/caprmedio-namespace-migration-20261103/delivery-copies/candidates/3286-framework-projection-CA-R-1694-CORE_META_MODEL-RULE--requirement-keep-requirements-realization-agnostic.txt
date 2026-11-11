---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Requirement)
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom.Content
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Method)
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Delivery)
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Package/Project Implementation
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Operations)
version: 41
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1694
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1694-CORE_META_MODEL-RULE--requirement-keep-requirements-realization-agnostic.md
  source_atom_id: CA-R-1694
  source_atom_revision: 41
  source_sha256: 046050052a8d13c16b6f00bd4335330c3185f38213b1957cbe0fe70b7bad6d96
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Requirement — Keep Requirements realization-agnostic

## Claim scope

Requirement claims and their internal realization.

## Claim

**every** Requirement **must** state its required outcome, obligation, permission, prohibition, **or** accepted external boundary **without** prescribing internal code **or** code organization merely as a construction choice.

- an accepted external interface, protocol, data shape, **or** host obligation **may** be required **when** conformance **to** that boundary is itself the required outcome. this does **not** prescribe an **otherwise** interchangeable internal realization.
- a programming language, library, algorithm, function, class, module, source-file organization, **or** another construction technique does **not** become a Requirement solely because it is normative; classify its primary contribution under CA-R-1531@20 **and** CA-R-2513.
- packaging, release, deployment, distribution, installation, migration, upgrade, **and** rollback are topics, **not** Content Role selectors. classify a Carrier representation **or** placement under CA-R-2515, reusable Action **or** Workflow behavior under CA-R-2463, **and** treat an actual realization as native Implementation rather than an Atom Content Role. mentioning one of those topics does **not** turn a procedure into Delivery authority.
- a candidate that combines this independently replaceable outcome with an independently replaceable construction, Carrier, **or** operational Claim requires separate Atoms under the one-Claim authority; a composite Claim is **not** split merely because it has multiple clauses.

## Details

Functional and non-functional Requirements both specify outcomes. A performance target can have an Engineering Subject. Subject and Content Role are independent; architecture remains Method even when mandatory. The methodology's own model definitions and Entity Definition constraints remain within Requirement authority.

CA-R-2512 owns the Requirement Content Role definition. this Atom constrains realization prescription **without** duplicating the definitions of the other Content Roles.
