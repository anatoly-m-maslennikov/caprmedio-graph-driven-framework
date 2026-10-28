---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Transformation
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Parsing
  - Subject
version: 21
updated_at: 2026-10-27 19:59:53 +0400
relations:
  child_of:
  - CA-R-2102
atom_id: CA-R-1360
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Definition
---
# Summary
Define Restricted CCE Canonical Signature

## Scope
parenthesized restricted Boolean expression occurrences **in** Atom Claims.

## Claim

a Canonical Signature **means** **`=1`** derived non-authoritative comparison value for **`=1`** parenthesized restricted Boolean expression occurrence **in** one Atom Claim, **where** the following constraints apply:

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

## Details
