---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Transformation
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Controlled English
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Canonical Scope Signature'
  - Subject/CAPRMEDIO/Carrier/File
version: 23
updated_at: 2026-10-27 19:59:34 +0400
relations:
  evaluation_for:
  - CA-R-1361
  - CA-M-241
atom_id: CA-E-407
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
type: Policy
tier: 5
---
# Summary

Validate Canonical Scope Signature Boundary

## Scope

Canonical Scope Signature derivations.

## Claim

the Evaluation **must** reject a Canonical Scope Signature derivation **if** **any** of the following holds:

- it rewrites one source Carrier.
- it treats one Signature as authority **or** Claim equivalence.
- it accepts mixed **and** **or** groups, **without**, **where**, **all**, **any** other CCE Operator, function, Entity-kind selector, descendant **or** dynamic selector, unresolved identity, changing source frontier, **or** unparseable prose.
- it fails **to** flatten nested same-operator groups, retains duplicate exact Atom IDs, loses the distinction between **and** **and** **or**, **or** yields different Signatures from same-operator groups that differ **only** by operand order.

## Details
