---
atom_id: CA-M-452
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Term//Term
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity
  - CAPRMEDIO <+ MODEL <+ Term
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Method)/(.Type: Term Definition)'
version: 3
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 1
role: Method
form: Term Definition
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-452-CORE_META_MODEL-TERM_DEFINITION--define-term.md
  source_atom_id: CA-M-452
  source_atom_revision: 3
  source_sha256: ef78a7cfe7e2b521d9ef8b6baefbc5211fc5d200f01c5d4fb1bdabad6bd1308a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Term

## Claim scope

The reusable lexical Term `Term` used in complete or qualified entity names and
authored content.

## Claim

Term **means** a reusable word **or** phrase component of complete **or**
qualified entity names **and** authored content whose approved Project-specific
meaning remains consistent across **all** its uses. This Claim explicitly
introduces the lexical Term instance named Term at `Term//Term`.

## Semantics

This Method governs the lexical word `Term`. The R / Entity Definition at
`Term` governs the Term kind and its inherited structure. The matching
word does not merge those distinct targets.

Self-reference does not require an infinite sequence of lexical instances such
as `Term Term`, `Term Term Term`, or further repetitions. This one explicit
Method Atom of Type Term Definition governs `Term//Term`; using the word `Term` in this
Claim or elsewhere does not introduce another instance.

An Entity outside `Term` uses its full source-admitted expression as its
complete canonical name. It cannot use one registered Term alone as that name,
except for the Subject root `Entity`. The target of this Method is within the
Term branch, so it is not an additional exception.

`Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: X)/(.Type: X)` is a qualified expression that reuses the Term
`X` in separately qualified value contexts. Each context still requires its
own governing admission; repeated components neither introduce `X` nor
transfer an admission.

## Details

This role-only Draft allocates no canonical Method identity and performs no
promotion, runtime change, Terms Graph implementation, dictionary extraction,
or inferred Term creation. A lexical occurrence, parser result, or entity-name
component is not a replacement for this explicit governing Claim.

### Pending governing declarations

- [Entity root with the Term branch](../../04_requirement/draft/CA-R-1248@24-draft-CORE_META_MODEL-DEFINITION--define-entity.md).
- [Term kind and inherited structure](../../04_requirement/draft/CA-R-1318@30-draft-CORE_META_MODEL-DEFINITION--define-term.md).
- [Method Type Term Definition](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-method-type-term-definition.md).
- [Dedicated Method meaning owner](../../04_requirement/draft/CA-R-1319@26-draft-CORE_META_MODEL--define-governed-term.md).

These links identify pending Draft dependencies, not Current admission.
