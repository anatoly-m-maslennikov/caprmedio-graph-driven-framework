---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Transformation
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Transformation
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Parsing
version: 23
updated_at: 2026-10-27 19:59:41 +0400
relations:
  child_of:
  - CA-M-115
atom_id: CA-M-240
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 4
type: Implementation Method
---
# Summary

Derive Restricted CCE Canonical Signatures **without** Source Rewrite

## Scope

derivation of Canonical Signatures from one selected Atom Carrier folder.

## Claim

**to** derive Canonical Signatures from one selected Atom Carrier folder, the Tool **must** inspect **only** active single-statement Atom Claims, identify **every** outermost parenthesized expression that **contains** the **and** Operator **or** the **or** Operator, derive a Canonical Signature **only** **if** the expression satisfies the Restricted Boolean Expression grammar, emit source-identity evidence **and** **every** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, **or** authority decision.

## Details
