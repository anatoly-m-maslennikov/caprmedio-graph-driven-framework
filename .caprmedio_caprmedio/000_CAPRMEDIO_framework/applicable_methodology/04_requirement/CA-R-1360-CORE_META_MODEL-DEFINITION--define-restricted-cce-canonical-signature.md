---
atom_id: CA-R-1360
ref_id: CA-R-1360
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Data Transformation"
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Content
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Parsing"
  - CAPRMEDIO_MODEL <+ Entity
tier: 3
relations:
  child_of:
  - CA-R-2102
status: Active
version: 28
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1360-CORE_META_MODEL-RULE--define-restricted-cce-canonical-signature.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1360-CORE_META_MODEL-DEFINITION--define-restricted-cce-canonical-signature.md
  source_atom_id: CA-R-1360
  source_atom_revision: 28
  source_sha256: 89fe5b953a22e83b874d1563e80e372959e992f0ff3f48a007291260f2bcaf28
  original_relations_sha256: 7d43ce9d2b05a49959ad5ed2f3146bfc7d86fbb84ab03a1c36f7042098dc0a67
---
## Summary
Define Restricted CCE Canonical Signature

## Claim

### Prose Claim

parenthesized restricted Boolean expression occurrences **in** Atom Claims.


Where a Canonical Signature is interpreted for a parenthesized restricted Boolean expression occurrence in one Atom Claim, the interpretation **must** produce **`=1`** derived non-authoritative comparison value, subject to the following constraints:

- the grammar is:
  - `group ::= (operand **and** operand [**and** operand ...]) | (operand **or** operand [**or** operand ...])`;
  - `operand ::= atomic predicate | nested group with the same Boolean Operator`;
  - `atomic predicate ::= subject path: value`.
- canonicalization:
  - flattens nested same-operator groups;
  - removes duplicate atomic predicates;
  - sorts the remaining atomic predicates;
  - preserves the root Boolean Operator.
- canonicalization excludes:
  - mixed Boolean Operators;
  - **every** other CCE Operator;
  - unrecognized bold token;
  - unbalanced parentheses;
  - unparseable prose.
