---
subjects:
  governs: "Canonical Signature Derivation Validation"
  depends_on:
    ["Entity/Continuant/Object/Atom.Substance", "Atom Claim Canonical Signature", "CCE Operator"]
version: 12
updated_at: "2026-10-15 18:49:12 +0000"
relations:
  evaluation_for:
    - CA-R-1360
    - CA-M-240
atom_id: "CA-E-405"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-405-CORE_META_MODEL-EVALUATION_APPROACH--validate-restricted-cce-canonical-signature-boundary.md
  source_atom_id: CA-E-405
  source_atom_revision: 12
  source_sha256: 1bd532485ec8c47302ce2fabfa6783d34453199b8d23bf38163bbe8be3b43cfb
  original_relations_sha256: 7dd373415c940e6e37f65dd1259b1a506ecf9af8fcf83fd941c984daf3095a31
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
