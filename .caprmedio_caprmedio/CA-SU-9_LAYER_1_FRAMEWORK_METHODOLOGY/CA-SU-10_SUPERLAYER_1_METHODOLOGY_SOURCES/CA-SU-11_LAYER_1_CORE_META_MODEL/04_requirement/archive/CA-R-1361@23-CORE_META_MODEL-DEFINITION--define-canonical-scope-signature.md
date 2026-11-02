---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Projection/Type: Canonical Scope Signature'
  depends_on:
  - Scope Expression
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.ID
  - Subject/Engineering/Carrier
  - Subject/Engineering/CCE Operator
version: 23
updated_at: 2026-10-24 11:58:20 +0400
relations: {}
atom_id: CA-R-1361@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Definition
---
# Summary

Define Canonical Scope Signature

## Scope

parenthesized Scope Expression occurrences considered for a Canonical Scope Signature.

## Claim

a Canonical Scope Signature **means** a derived non-authoritative comparison value for **`=1`** parenthesized Scope Expression occurrence satisfying **all** of the following boundaries.

## Details

### admitted expression

- a group **contains** **`>=2`** operands **and** uses **`=1`** Boolean Operator value from (**`and`**, **`or`**). its operands are joined **only** by repetitions of that Operator.
- an operand is an exact Atom ID **or** a nested parenthesized group with the same Boolean Operator as its containing group.
- **every** exact Atom ID resolves **to** **`=1`** active Atom Carrier inside the selected source frontier.

### canonical value

- the value preserves whether the root Boolean Operator is **`and`** **or** **`or`**.
- the value represents the flattened same-operator group as unique exact Atom IDs **in** canonical lexical order.
- groups that differ **only** by same-operator nesting, repeated exact Atom IDs, **or** operand order have the same value.

### exclusions

mixed Boolean Operators, **without**, **where**, **all**, **every** other CCE Operator, functions, Entity-kind selectors, descendant **or** dynamic selectors, unresolved identities, a changing source frontier, **and** unparseable prose are outside this signature domain.
