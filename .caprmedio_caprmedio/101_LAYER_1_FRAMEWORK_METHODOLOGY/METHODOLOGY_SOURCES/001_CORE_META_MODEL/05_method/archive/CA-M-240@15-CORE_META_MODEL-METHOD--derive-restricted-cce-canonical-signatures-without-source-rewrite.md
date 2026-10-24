---
subjects:
  governs: Canonical Signature Derivation
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Atom Claim Canonical Signature
  - Subject/Engineering/CCE Operator
version: 15
updated_at: 2026-10-24 01:18:03 +0400
relations:
  child_of:
  - CA-M-115
atom_id: CA-M-240@15
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Derive Restricted CCE Canonical Signatures **without** Source Rewrite

## Scope

derivation of Canonical Signatures from one selected Atom Carrier folder.

## Claim

**to** derive Canonical Signatures from one selected Atom Carrier folder, the Tool **must** inspect **only** active single-statement Atom Claims, identify **every** outermost parenthesized expression that **contains** the **and** Operator **or** the **or** Operator, derive a Canonical Signature **only** **if** the expression satisfies the Restricted Boolean Expression grammar, emit source-identity evidence **and** **every** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, **or** authority decision.

## Details
