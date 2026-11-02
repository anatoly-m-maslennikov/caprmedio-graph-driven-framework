---
subjects:
  active: Entity/Aspect/Engineering/Data Handling/Data Transformation
  passive:
  - Atom.Content
  - Entity/Aspect/Engineering/Data Handling/Parsing
  - Entity
version: 26
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2102
atom_id: CA-R-1360@26
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 3
role: Requirement
form: Rule
---
## Summary
Define Restricted CCE Canonical Signature

## Claim scope
parenthesized restricted Boolean expression occurrences **in** Atom Claims.

## Claim

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
