---
subjects:
  governs: Canonical Signature Derivation Validation
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Atom Claim Canonical Signature
  - CCE Operator
version: 16
updated_at: 2026-10-24 00:38:25 +0400
relations:
  evaluation_for:
  - CA-R-1360
  - CA-M-240
atom_id: CA-E-405@16
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Policy
tier: 3
---
# Summary

Validate Restricted CCE Canonical Signature Boundary

## Scope

Canonical Signature derivations evaluated against the restricted CCE boundary.

## Claim

the Evaluation **must** reject a Canonical Signature derivation **if** any of the following is true:

- it rewrites one source Claim.
- it treats one Canonical Signature as authority.
- it accepts mixed **and** **or** groups.
- it rewrites negation, implication, **where**, **without**, temporal condition, quantifier, extension-defined CCE Operator, **or** unparseable prose.
- it fails **to** flatten nested same-operator groups.
- it retains duplicate atomic predicates.
- it yields different Canonical Signatures from Boolean groups that differ **only** by operand order.

## Details
