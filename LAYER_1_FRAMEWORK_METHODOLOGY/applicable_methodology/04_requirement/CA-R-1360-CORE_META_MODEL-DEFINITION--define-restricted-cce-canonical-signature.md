---
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Data Transformation
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Parsing
  - CAPRMEDIO_MODEL <+ Entity
version: 28
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-R-2102
atom_id: CA-R-1360
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1360-CORE_META_MODEL-DEFINITION--define-restricted-cce-canonical-signature.md
  source_atom_id: CA-R-1360
  source_atom_revision: 28
  source_sha256: 731c2fb05fe6cf6657f2c5dcd82524cbf66c740a2c30b46067a18f05181a56b3
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
