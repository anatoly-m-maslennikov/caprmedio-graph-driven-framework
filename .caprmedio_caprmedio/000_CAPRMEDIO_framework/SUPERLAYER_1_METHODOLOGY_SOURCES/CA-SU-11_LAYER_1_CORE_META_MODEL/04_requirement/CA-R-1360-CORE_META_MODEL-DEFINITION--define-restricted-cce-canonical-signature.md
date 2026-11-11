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
