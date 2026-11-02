---
subjects:
  governs: Canonical Signature Derivation Validation
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Content
  - Atom Claim Canonical Signature
  - Subject/Engineering/CCE Operator
version: 20
updated_at: 2026-10-24 19:39:48 +0400
relations:
  evaluation_for:
  - CA-R-1360
  - CA-M-240
atom_id: CA-E-405@20
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Policy
tier: 5
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
