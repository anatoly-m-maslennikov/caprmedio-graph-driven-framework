---
subjects:
  governs: Canonical Signature Derivation
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Atom Claim Canonical Signature
  - CCE Operator
version: 13
updated_at: 2026-10-23 03:20:06 +0400
relations:
  child_of:
  - CA-M-115
atom_id: CA-M-240@13
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
status: Archived
author: Anatoly Maslennikov
global_tier: 11
---
# Summary

Derive Restricted CCE Canonical Signatures **without** Source Rewrite

## Scope

derivation of Canonical Signatures from one selected Atom Carrier folder.

## Claim

**to** derive Canonical Signatures from one selected Atom Carrier folder, the Tool **must** inspect **only** active single-statement Atom Claims, identify **every** outermost parenthesized expression that **contains** the **and** Operator **or** the **or** Operator, derive a Canonical Signature **only** **if** the expression satisfies the Restricted Boolean Expression grammar, emit source-identity evidence **and** **every** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, **or** authority decision.

## Details
