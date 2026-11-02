---
atom_id: CA-R-2453@2
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Method)/(.Type: Term Definition)'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Method)'
  - Entity/Term
  - Entity/Term//Empty
  - Entity/Term//ID
version: 2
updated_at: 2026-10-30 09:02:56 +0400
relations: {}
tier: 1
---
## Summary

Define Method Type Term Definition

## Claim scope

The Term Definition value in the qualified Method Type domain and the lexical meaning owned by an Atom of that Type.

## Claim

Term Definition **means** the dedicated Method Type whose Claim states the authoritative meaning of **`=1`** reusable lexical Term as its authoring and interpretation convention. It is distinct from the Requirement Type Entity Definition, which defines an Entity kind or property structure and constraints, and from an Implementation Method describing how to author definition content. The Term Definition Type has the shared Method Claim contract; this Type declaration does not create actual Term Definition Method Atoms.

## Details

The Operator's latest confirmed decision assigns authoritative lexical Term Definitions to M and places Terms directly under `Entity/Term`, initially flat. Exactly one active Method Atom of Type Term Definition owns a Governed Term's approved meaning under the proposed successor of CA-R-1319. This Requirement Atom defines the Method-qualified Type value; it is not itself a lexical Term Definition or a retyping of the R definition of the Term kind.

The Method-qualified Type target is `Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Method)/(.Type: Term Definition)`. Concrete lexical definitions govern `Entity/Term//<Name>`, including the approved `Entity/Term//Empty` and `Entity/Term//ID` target names, with explicit defining authority under CA-R-1194 and CA-R-1931. An occurrence in a property name, parser output, or this Type declaration does not introduce a lexical instance or supply its meaning. M carries the authoritative lexical meaning, an authoring Method describes how to write it, and E checks well-formedness and conflicts.

Reusable `Package`, `Unit`, and `ID` retain approved meanings across complete names. A lexical Term is distinct from a qualified property entity such as `atom.id`; this role decision adds no lifecycle identity semantics to the ID examples. No Term groups, mandatory dictionary Projection, extractor, lookup service, synthetic domain entities, or Terms Graph implementation is introduced.

The specialized Method contribution is an authorship convention under Current CA-R-1340@32: authors and readers use and interpret the Term with its declared meaning. It is not an Entity-kind structure declaration or an operational instruction. Under CA-R-2278, the R definition of the Term kind supplies its inherited structure; a concrete `Entity/Term//Name` definition supplies instance-specific lexical meaning, not a duplicate R definition of that structure. This Draft does not convert existing structural Requirements or Rules into lexical Methods merely because they govern a Term-instance path.

### Coordinated replacement and retirement plan

Current CA-R-2229@2 declares the different, Requirement-qualified Type `Term Definition` with Summary `Define Requirement Type Term Definition`. It remains unchanged. Changing that Summary and qualified Type target into this Method-Type declaration would cross the replacement boundary under CA-R-1432 and CA-R-1464; this new declaration therefore retains a role-only Draft marker until fresh identity allocation is admitted.

Before adopting the new meaning-owner rule, coordinate admission of the Method-qualified Type, reviewed Method replacements for existing authoritative lexical Requirement definitions, their exact canonical Term targets, and affected consumers. Content Role changes require fresh Atom identities under CA-R-1432; no old Requirement ID is silently retyped or reused for a Method. Preserve the predecessor/successor evidence and source content, and retire obsolete Requirement-role lexical definitions and CA-R-2229 only after their admitted replacement authority is active. This is a plan, not an archival or promotion effect. It does not resolve or mutate the separately reported CA-R-2275 identity collision.

### Draft source pins

This is a new unallocated R/Entity Definition Draft, not a successor revision of CA-R-2229. Comparison source: Current CA-R-2229@2 at `/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2229-CORE_META_MODEL-ENTITY_DEFINITION--define-requirement-type-term-definition.md`, SHA-256 `a59dc893faf3bbfa976eae63bcb99726583b3258342e4710239b3b23c8f34fe4`. Structural and ownership source pins are Current CA-R-1318@29 (`02063cdcc24fa8ccc40ad6008958c821ccbf3608229a80f454a5d81a441e928d`) and CA-R-1319@25 (`831b4543ceced91376af9e3c494a5f37e8dd1d2d9766b14810ec6f6194b49f78`).

Source-fingerprint snapshot: `/tmp/cce-term-root-migration-20261029/current-before.json`; snapshot SHA-256: `23c1414c96d6e57cdc9f1bf50569de396ef130a7231b765cd8b4511bcb573ad5`. This Draft changes no Current source, allocates no canonical number and performs no promotion or retirement.
