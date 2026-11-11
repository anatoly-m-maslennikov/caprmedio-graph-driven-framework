---
atom_id: CA-R-2766
ref_id: CA-R-2766@3-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//SPECIALIZES
tier: 1
status: Draft
version: 3
updated_at: 2026-11-05 18:23:39 +0400
carrier_destination:
  file:
    name: CA-R-2766@3-draft-DECLARATION--declare-specializes.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---

## Summary

Declare SPECIALIZES

## Claim

### Prose Claim

The child Atom's Claim is more specific or stricter than the parent Atom's Claim in the same or a narrower Scope and preserves the parent's applicable constraints. A conditional specialization is included. A reference or dependency alone does not establish SPECIALIZES. IS_SPECIALIZED_BY is the inverse alias, with parent and child endpoints reversed.

### Formal Claim

```CFEL
# model
Relation//IS_SPECIALIZED_BY ((IS_INVERSE_ALIAS_FOR)) Relation//SPECIALIZES;

Relation//SPECIALIZES ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
$specializing_atom[<Atom>] ((SPECIALIZES)) $specialized_atom[<Atom>]
```

## Semantics

SPECIALIZES relates a child Atom to the Atom whose Claim it specializes.
