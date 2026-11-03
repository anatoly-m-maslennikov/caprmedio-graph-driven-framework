---
atom_id: CA-M-454
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Term//Artifact
  passive:
  - CAPRMEDIO <+ MODEL <+ Term
  - CAPRMEDIO <+ MODEL <+ Entity
  - CAPRMEDIO <+ MODEL <+ Carrier
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Method)/(.Type: Term Definition)'
version: 4
updated_at: 2026-11-02 19:46:47 +0400
relations: {}
tier: 1
role: Method
form: Term Definition
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-454-CORE_META_MODEL-TERM_DEFINITION--define-artifact.md
  source_atom_id: CA-M-454
  source_atom_revision: 4
  source_sha256: 2dc1a6986e45636ab50d316fea99bc5f47dbd1e01c709dce6bda678825c39a6b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Artifact

## Claim scope

The reusable lexical Term Artifact in model statements about Entity instances
and their Carrier representations.

## Claim

Artifact **means** an Entity instance represented in a Carrier. This Claim
explicitly introduces the lexical Term instance Artifact at
`Term//Artifact`.

## Semantics

A file, folder or database row can serve as a Carrier. The Term refers to the
Entity instance, not its Carrier. An Entity retains its
identity when referred to as an Artifact, including where more than one
Carrier represents it. Artifact does not declare another Entity kind,
classification axis, Property, or second identity.

Entity admission remains governed by the pending Entity Definition; Carrier
binding remains governed by CARRIES. This lexical Definition adds neither
admission policy nor Carrier-binding policy.

## Details

The Operator states that Artifact is a Term for Entity instances represented
in Carriers. This supersedes the proposed new Artifact classification. The
role-only marker allocates no canonical Method identity.

Current R1994@14 is historical evidence for this Draft package and is planned
for future Retirement after its Entity constraints move to the Entity
Definition. It remains Current until coordinated retirement; in the proposed owner
structure it will not own the lexical Artifact meaning.

### Pending governing declarations

- [Term kind](../../04_requirement/draft/CA-R-1318@30-draft-CORE_META_MODEL-DEFINITION--define-term.md).
- [Method Type Term Definition](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-method-type-term-definition.md).
- [Governed Term meaning ownership](../../04_requirement/draft/CA-R-1319@26-draft-CORE_META_MODEL--define-governed-term.md).
- [Pending Entity Definition](../../04_requirement/draft/CA-R-1248@24-draft-CORE_META_MODEL-DEFINITION--define-entity.md).
- [Current CARRIES Relation](../../04_requirement/CA-R-1993-CORE_META_MODEL-DEFINITION--define-carries.md).

CARRIES is Current; the linked Term, Method-Type and Entity successors are
pending. These links do not establish adoption of this Draft.

### Current source evidence

Exact historical source: `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1994-CORE_META_MODEL--define-entity-node.md`, Version 14, SHA-256 `41b8b0ef51a71969db07cec2008a19e3c6372e90ae9cc66727de31287d722ce8`. It is evidence for the planned consolidation and future Retirement, not the ongoing owner of this lexical meaning.
